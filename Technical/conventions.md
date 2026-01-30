---
$schema: brain://entity/project/v1
$id: entity/project/conventions
$type: project
$version: 7
$created: '2026-01-22T08:31:01.096053Z'
$updated: '2026-01-30T14:33:13.960568+00:00'
$confidence: 0.36
$source: unknown
$status: active
$relationships: []
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.096053Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Conventions
---

# Coding Conventions

Summary of HelloFresh coding standards and patterns. Source: spec-machine standards.

## File Organization

### Feature Folders
```
src/features/<feature-name>/
├── components/       # Feature-specific components
├── hooks/           # Feature-specific hooks
├── stores/          # Zustand stores
├── types.ts         # Type definitions
├── utils.ts         # Utility functions
└── index.ts         # Public exports
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `UserProfile.tsx` |
| Hooks | camelCase, use prefix | `useUserData.ts` |
| Stores | camelCase, store suffix | `userStore.ts` |
| Utils | camelCase | `formatDate.ts` |
| Types | PascalCase | `UserProfileProps` |
| Constants | UPPER_SNAKE | `MAX_RETRY_COUNT` |

## State Management (Zustand)

### Store Pattern
```typescript
import { create } from 'zustand';

interface UserStore {
  user: User | null;
  setUser: (user: User) => void;
  clearUser: () => void;
}

export const useUserStore = create<UserStore>((set) => ({
  user: null,
  setUser: (user) => set({ user }),
  clearUser: () => set({ user: null }),
}));
```

### Key Rules
- One store per domain/feature
- Keep stores flat (avoid nesting)
- Use selectors for derived state
- Actions modify state synchronously

## API Patterns

### GraphQL
- Use Apollo Client
- Colocate queries with components
- Prefer fragments for reusable data
- Cache with `fetchPolicy: 'cache-and-network'`

### REST
- Use native fetch (no axios)
- Centralized error handling
- Type responses with Zod validation

## Testing

### Unit Tests
- Colocate with source: `Component.test.tsx`
- Use React Testing Library
- Test behavior, not implementation
- Avoid snapshot tests for logic

### E2E Tests
- Playwright for web
- Detox for mobile
- Page Object Model pattern
- Test critical user flows

## Feature Flags (Statsig)

```typescript
import { useGate } from 'statsig-react';

const MyComponent = () => {
  const { value: showNewFeature } = useGate('new_feature_gate');

  if (!showNewFeature) return <OldComponent />;
  return <NewComponent />;
};
```

## Error Handling

- Use Error Boundaries for UI errors
- Log errors to monitoring (Datadog)
- User-friendly error messages
- Graceful degradation patterns

---

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/*
*Run `/sync-tech-context` to update*
