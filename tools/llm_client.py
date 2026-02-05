#!/usr/bin/env python3
"""
PM-OS Brain LLM Client

Unified interface for multiple LLM providers with automatic fallback.
Supports: OpenAI, Anthropic (Claude), Gemini, Mistral, Ollama, Azure, Bedrock

Usage:
    from llm_client import LLMClient
    
    client = LLMClient()  # Uses config/env for provider selection
    
    # Simple completion
    response = client.complete("Extract entities from this text: ...")
    
    # With specific provider
    response = client.complete("...", provider="anthropic")
    
    # Embeddings
    embeddings = client.embed("Some text to embed")

Author: PM-OS Team
"""

import os
import sys
import logging
from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

# Provider availability flags
OPENAI_AVAILABLE = False
ANTHROPIC_AVAILABLE = False
GEMINI_AVAILABLE = False
MISTRAL_AVAILABLE = False
OLLAMA_AVAILABLE = False
LITELLM_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    pass

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    pass

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    pass

try:
    from mistralai.client import MistralClient
    from mistralai.models.chat_completion import ChatMessage
    MISTRAL_AVAILABLE = True
except ImportError:
    pass

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    pass

try:
    import litellm
    LITELLM_AVAILABLE = True
except ImportError:
    pass


@dataclass
class LLMResponse:
    """Standardized LLM response."""
    content: str
    provider: str
    model: str
    usage: Dict[str, int]
    raw_response: Any = None


@dataclass
class EmbeddingResponse:
    """Standardized embedding response."""
    embeddings: List[List[float]]
    provider: str
    model: str
    dimensions: int


class LLMClient:
    """
    Unified LLM client with multi-provider support and automatic fallback.
    
    Supports:
        - OpenAI (GPT-4, GPT-3.5)
        - Anthropic (Claude 3 Opus, Sonnet, Haiku)
        - Google (Gemini Pro, Flash)
        - Mistral (Large, Medium, Small)
        - Ollama (Llama 3, Mistral, etc.)
        - Azure OpenAI
        - AWS Bedrock
        - LiteLLM (unified interface)
    """
    
    def __init__(
        self,
        provider: Optional[str] = None,
        fallback: Optional[List[str]] = None,
        config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize LLM client.
        
        Args:
            provider: Primary provider (openai, anthropic, gemini, mistral, ollama)
            fallback: List of fallback providers
            config: Provider-specific configuration
        """
        self.config = config or {}
        self.provider = provider or os.getenv("LLM_PROVIDER", "openai")
        self.fallback = fallback or self._parse_fallback_env()
        
        # Initialize clients
        self._clients: Dict[str, Any] = {}
        self._init_clients()
    
    def _parse_fallback_env(self) -> List[str]:
        """Parse fallback providers from environment."""
        fallback_str = os.getenv("LLM_FALLBACK_ORDER", "")
        if fallback_str:
            return [p.strip() for p in fallback_str.split(",")]
        return []
    
    def _init_clients(self) -> None:
        """Initialize available provider clients."""
        # OpenAI
        if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
            self._clients["openai"] = openai.OpenAI()
        
        # Anthropic
        if ANTHROPIC_AVAILABLE and os.getenv("ANTHROPIC_API_KEY"):
            self._clients["anthropic"] = anthropic.Anthropic()
        
        # Gemini
        if GEMINI_AVAILABLE and os.getenv("GEMINI_API_KEY"):
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self._clients["gemini"] = genai
        
        # Mistral
        if MISTRAL_AVAILABLE and os.getenv("MISTRAL_API_KEY"):
            self._clients["mistral"] = MistralClient(
                api_key=os.getenv("MISTRAL_API_KEY")
            )
        
        # Ollama (no auth needed)
        if OLLAMA_AVAILABLE:
            self._clients["ollama"] = ollama
        
        # Log available providers
        available = list(self._clients.keys())
        logger.info(f"LLM providers available: {available}")
    
    def complete(
        self,
        prompt: str,
        system: Optional[str] = None,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        max_tokens: int = 4096,
        temperature: float = 0.1,
        **kwargs,
    ) -> LLMResponse:
        """
        Generate a completion from the LLM.
        
        Args:
            prompt: User prompt
            system: System prompt
            provider: Override default provider
            model: Override default model
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Provider-specific arguments
            
        Returns:
            LLMResponse with content and metadata
        """
        provider = provider or self.provider
        providers_to_try = [provider] + [p for p in self.fallback if p != provider]
        
        last_error = None
        for p in providers_to_try:
            if p not in self._clients:
                continue
            
            try:
                return self._complete_with_provider(
                    p, prompt, system, model, max_tokens, temperature, **kwargs
                )
            except Exception as e:
                logger.warning(f"Provider {p} failed: {e}")
                last_error = e
                continue
        
        raise RuntimeError(f"All providers failed. Last error: {last_error}")
    
    def _complete_with_provider(
        self,
        provider: str,
        prompt: str,
        system: Optional[str],
        model: Optional[str],
        max_tokens: int,
        temperature: float,
        **kwargs,
    ) -> LLMResponse:
        """Execute completion with specific provider."""
        
        if provider == "openai":
            return self._complete_openai(prompt, system, model, max_tokens, temperature)
        elif provider == "anthropic":
            return self._complete_anthropic(prompt, system, model, max_tokens, temperature)
        elif provider == "gemini":
            return self._complete_gemini(prompt, system, model, max_tokens, temperature)
        elif provider == "mistral":
            return self._complete_mistral(prompt, system, model, max_tokens, temperature)
        elif provider == "ollama":
            return self._complete_ollama(prompt, system, model, max_tokens, temperature)
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def _complete_openai(self, prompt, system, model, max_tokens, temperature) -> LLMResponse:
        """OpenAI completion."""
        model = model or os.getenv("OPENAI_MODEL", "gpt-4o")
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        response = self._clients["openai"].chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        
        return LLMResponse(
            content=response.choices[0].message.content,
            provider="openai",
            model=model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            },
            raw_response=response,
        )
    
    def _complete_anthropic(self, prompt, system, model, max_tokens, temperature) -> LLMResponse:
        """Anthropic completion."""
        model = model or os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        
        kwargs = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system
        
        response = self._clients["anthropic"].messages.create(**kwargs)
        
        return LLMResponse(
            content=response.content[0].text,
            provider="anthropic",
            model=model,
            usage={
                "prompt_tokens": response.usage.input_tokens,
                "completion_tokens": response.usage.output_tokens,
            },
            raw_response=response,
        )
    
    def _complete_gemini(self, prompt, system, model, max_tokens, temperature) -> LLMResponse:
        """Gemini completion."""
        model_name = model or os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        
        full_prompt = f"{system}\n\n{prompt}" if system else prompt
        
        gen_model = self._clients["gemini"].GenerativeModel(model_name)
        response = gen_model.generate_content(
            full_prompt,
            generation_config={
                "max_output_tokens": max_tokens,
                "temperature": temperature,
            },
        )
        
        return LLMResponse(
            content=response.text,
            provider="gemini",
            model=model_name,
            usage={},  # Gemini doesn't provide token counts easily
            raw_response=response,
        )
    
    def _complete_mistral(self, prompt, system, model, max_tokens, temperature) -> LLMResponse:
        """Mistral completion."""
        model = model or os.getenv("MISTRAL_MODEL", "mistral-large-latest")
        
        messages = []
        if system:
            messages.append(ChatMessage(role="system", content=system))
        messages.append(ChatMessage(role="user", content=prompt))
        
        response = self._clients["mistral"].chat(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        
        return LLMResponse(
            content=response.choices[0].message.content,
            provider="mistral",
            model=model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
            },
            raw_response=response,
        )
    
    def _complete_ollama(self, prompt, system, model, max_tokens, temperature) -> LLMResponse:
        """Ollama completion."""
        model = model or os.getenv("OLLAMA_MODEL", "llama3")
        
        full_prompt = f"{system}\n\n{prompt}" if system else prompt
        
        response = self._clients["ollama"].generate(
            model=model,
            prompt=full_prompt,
            options={
                "num_predict": max_tokens,
                "temperature": temperature,
            },
        )
        
        return LLMResponse(
            content=response["response"],
            provider="ollama",
            model=model,
            usage={},
            raw_response=response,
        )
    
    def embed(
        self,
        texts: Union[str, List[str]],
        provider: Optional[str] = None,
        model: Optional[str] = None,
    ) -> EmbeddingResponse:
        """
        Generate embeddings for text(s).
        
        Args:
            texts: Single text or list of texts
            provider: Override default provider
            model: Override default model
            
        Returns:
            EmbeddingResponse with vectors
        """
        if isinstance(texts, str):
            texts = [texts]
        
        provider = provider or self.provider
        
        if provider == "openai" and "openai" in self._clients:
            return self._embed_openai(texts, model)
        elif provider == "mistral" and "mistral" in self._clients:
            return self._embed_mistral(texts, model)
        else:
            # Fallback to OpenAI if available
            if "openai" in self._clients:
                return self._embed_openai(texts, model)
            raise RuntimeError(f"No embedding provider available")
    
    def _embed_openai(self, texts: List[str], model: Optional[str]) -> EmbeddingResponse:
        """OpenAI embeddings."""
        model = model or os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
        
        response = self._clients["openai"].embeddings.create(
            model=model,
            input=texts,
        )
        
        embeddings = [e.embedding for e in response.data]
        
        return EmbeddingResponse(
            embeddings=embeddings,
            provider="openai",
            model=model,
            dimensions=len(embeddings[0]) if embeddings else 0,
        )
    
    def _embed_mistral(self, texts: List[str], model: Optional[str]) -> EmbeddingResponse:
        """Mistral embeddings."""
        model = model or os.getenv("MISTRAL_EMBEDDING_MODEL", "mistral-embed")
        
        response = self._clients["mistral"].embeddings(
            model=model,
            input=texts,
        )
        
        embeddings = [e.embedding for e in response.data]
        
        return EmbeddingResponse(
            embeddings=embeddings,
            provider="mistral",
            model=model,
            dimensions=len(embeddings[0]) if embeddings else 0,
        )
    
    @property
    def available_providers(self) -> List[str]:
        """List of available (configured) providers."""
        return list(self._clients.keys())


# Convenience function
def get_llm_client(**kwargs) -> LLMClient:
    """Get a configured LLM client."""
    return LLMClient(**kwargs)


if __name__ == "__main__":
    # Test the client
    client = LLMClient()
    print(f"Available providers: {client.available_providers}")
    
    if client.available_providers:
        response = client.complete(
            "What is 2 + 2? Answer in one word.",
            system="You are a helpful assistant. Be concise.",
        )
        print(f"Response from {response.provider}/{response.model}:")
        print(response.content)
