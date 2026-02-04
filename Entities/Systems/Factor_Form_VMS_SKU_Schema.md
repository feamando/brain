---
$schema: brain://entity/system/v1
$id: entity/system/factor-form-vms-sku-schema
$type: system
$version: 1
$created: '2026-02-04T10:30:00.000000Z'
$updated: '2026-02-04T10:30:00.000000Z'
$confidence: 0.95
$source: manual_extraction
$status: active
$relationships:
- type: part_of
  target: entity/system/vmsvmsu
  confidence: 1.0
  source: manual
- type: used_by
  target: entity/project/factor-form-rtevms
  confidence: 1.0
  source: manual
$tags:
- factor-form
- sku
- product-encoding
- vms
- vmsu
$aliases:
- VMS SKU
- VMSU SKU
- Factor Form SKU
name: Factor Form VMS SKU Schema
---

# Factor Form VMS SKU Schema

**Type:** system
**Created:** 2026-02-04
**Source:** Manual extraction from product catalog (GDoc 1wF7gMGH866fxGp0BwpAhFPuNwKDhhVsDapbH9Bg1fGg)

## Overview

The VMS/VMSU SKU encoding scheme for Factor Form products. Used to uniquely identify product combinations including meal shakes, greens, and hydration products.

## SKU Structure

### Full Format

```
[BRAND]-[FAMILY]-[BOX_COUNT]-[VARIANT_CODE]-[MODIFIER]
```

**Example:** `FJ-VMS-4-20100100-0`

### Segment Breakdown

| Segment | Position | Description | Values |
|---------|----------|-------------|--------|
| Brand | 1 | Brand identifier | `FJ` = Factor Form |
| Family | 2 | Product family | `VMS` = Subscription, `VMSU` = One-Time Purchase |
| Box Count | 3 | Number of boxes in order | `1`, `2`, `3`, `4` |
| Variant Code | 4 | Product mix encoding (see below) | Positional decimal |
| Modifier | 5 | Reserved for future use | Always `0` |

## Variant Code Encoding

The variant code uses **positional decimal encoding** where each digit position represents a product type, and the digit value represents the quantity of that product.

### Position Mapping (Right to Left)

| Position | Power | Product Type | Product Code |
|----------|-------|--------------|--------------|
| 1 | 10^0 | Chocolate | 6 |
| 2 | 10^1 | Vanilla | 7 |
| 3 | 10^2 | Greens | 5 |
| 4 | 10^3 | Lemon Lime | 2 |
| 5 | 10^4 | Blood Orange Yuzu | 1 |
| 6 | 10^5 | Passion Fruit Guava | 4 |
| 7 | 10^6 | Variety Pack | 3 |
| 8 | 10^7 | Bulk (8-serving) | 8 |

### Product Code Reference

| Code | Product | Base Price |
|------|---------|------------|
| 1 | Blood Orange Yuzu | $24.99 |
| 2 | Lemon Lime | $24.99 |
| 3 | Variety Pack | $24.99 |
| 4 | Passion Fruit Guava | $24.99 |
| 5 | Greens | $78.99 |
| 6 | Chocolate | $34.99 |
| 7 | Vanilla | $34.99 |
| 8 | Bulk (8-serving) | $68.99 |

## Decoding Examples

| SKU | Variant | Decoded | Calculation |
|-----|---------|---------|-------------|
| `FJ-VMS-1-1-0` | 1 | 1× Chocolate | 1 × 10^0 = 1 chocolate |
| `FJ-VMS-2-11-0` | 11 | 1× Vanilla + 1× Chocolate | 1×10^1 + 1×10^0 |
| `FJ-VMS-1-100-0` | 100 | 1× Greens | 1 × 10^2 |
| `FJ-VMS-2-101-0` | 101 | 1× Greens + 1× Chocolate | 1×10^2 + 1×10^0 |
| `FJ-VMS-3-30000000-0` | 30000000 | 3× Bulk | 3 × 10^7 |
| `FJ-VMS-4-20100100-0` | 20100100 | 2× Bulk + 1× Passion Fruit + 1× Greens | 2×10^7 + 1×10^5 + 1×10^2 |

## Decoding Algorithm

```python
def decode_variant(variant_code: int) -> dict:
    """Decode VMS variant code to product quantities."""
    products = {
        'chocolate': variant_code % 10,
        'vanilla': (variant_code // 10) % 10,
        'greens': (variant_code // 100) % 10,
        'lemon_lime': (variant_code // 1000) % 10,
        'blood_orange_yuzu': (variant_code // 10000) % 10,
        'passion_fruit_guava': (variant_code // 100000) % 10,
        'variety': (variant_code // 1000000) % 10,
        'bulk': (variant_code // 10000000) % 10,
    }
    return {k: v for k, v in products.items() if v > 0}

# Example: decode_variant(20100100)
# Returns: {'greens': 1, 'passion_fruit_guava': 1, 'bulk': 2}
```

## Encoding Algorithm

```python
def encode_variant(products: dict) -> int:
    """Encode product quantities to VMS variant code."""
    positions = {
        'chocolate': 1,
        'vanilla': 10,
        'greens': 100,
        'lemon_lime': 1000,
        'blood_orange_yuzu': 10000,
        'passion_fruit_guava': 100000,
        'variety': 1000000,
        'bulk': 10000000,
    }
    return sum(qty * positions[prod] for prod, qty in products.items())

# Example: encode_variant({'bulk': 2, 'passion_fruit_guava': 1, 'greens': 1})
# Returns: 20100100
```

## VMS vs VMSU Family

| Attribute | VMS | VMSU |
|-----------|-----|------|
| Purchase Model | Subscription | One-Time Purchase (OTP) |
| Free Shipping | $50+ | $65+ |
| First Box Discount | 40% (above MOV) | N/A |
| Recurring Discount | 20% (above MOV) | N/A |
| Feature Flag | N/A | `rtevms-2256_vmsu_family` |

## Pricing Model

### OTP (One-Time Purchase)
- Full price, no discounts
- Free shipping at $65+
- Shipping cost below threshold: $5.99

### SNS (Subscribe & Save)
- **First Box (above MOV):** 40% off
- **First Box (below MOV):** 10% off
- **Recurring (above MOV):** 20% off
- **Recurring (below MOV):** 10% off
- Free shipping at $50+

## Related Tickets

- **RTEVMS-2256:** VMSU product family implementation
- **RTEVMS-2186/2362:** Create new product family for OTP
- **TAM-T-53:** De-couple Product SKU business logic

## Source Data

- **Product Catalog:** GDoc `1wF7gMGH866fxGp0BwpAhFPuNwKDhhVsDapbH9Bg1fGg`
- **Contains:** 200+ SKU combinations with pricing

---
*Last updated: 2026-02-04 10:30*
