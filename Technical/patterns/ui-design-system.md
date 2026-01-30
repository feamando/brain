---
$schema: brain://entity/project/v1
$id: entity/project/ui-design-system
$type: project
$version: 1
$created: '2026-01-22T08:31:01.778050Z'
$updated: '2026-01-30T10:28:13.216061'
$confidence: 0.36
$source: unknown
$status: active
$relationships:
- type: mentioned_in
  target: entity/project/hellofresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/engagement
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/project/fresh
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/desi
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
- type: mentioned_in
  target: entity/person/mark
  confidence: 0.6
  source: body_text_extraction
  last_verified: '2026-01-30'
$tags: []
$aliases: []
$events:
- event_id: evt-migration-20260122
  timestamp: '2026-01-22T08:31:01.778050Z'
  type: entity_create
  actor: system/schema_migrator
  changes:
  - field: $schema
    operation: set
    value: brain://entity/project/v1
  message: Migrated from v1 to v2 schema
name: Ui Design System
$orphan_reason: pending_enrichment
---

# Ui Design System Patterns

*Source: hellofresh/spec-machine/profiles/engagement-dau/standards/ui-design-system/*

### accessibility

# Accessibility Standards  ## Overview  Provide accessibility labels, roles, and hints for all interactive elements. Use altText for icons and images.  **Why**: Accessibility ensures the app is usable by everyone, including users with disabilities.  ## Icon Accessibility  ### altText for Icons  Alwa...
### images

# Image Standards  ## Overview  Standards for loading, optimizing, and displaying images in React Native applications using Cloudinary CDN.  **Why**: Proper image handling ensures fast loading times, optimal quality, and responsive designs across all devices. Cloudinary provides automatic format sel...
### responsive-design

# Responsive Design Patterns  ## Overview  Standards for implementing responsive designs that adapt to different device sizes, screen dimensions, and orientations in React Native applications.  **Why**: Responsive design ensures optimal user experience across all device sizes (iPhone SE to iPad) by...
### styling-patterns

# Styling Patterns  ## Overview  Use Zest design tokens for all styling. Follow the styling hierarchy: Zest components with variants first, then useZestStyles for custom layouts.  **Why**: Zest provides consistent theming, accessibility, and responsive design across the app.  ## Styling Hierarchy  #...
### zest-components

# Zest Components Guide  <!-- AGENT NOTE: When reading this file for best practices and component usage examples, DO NOT read beyond the "MAINTENANCE SECTION" marker below. The appendix after that marker is only for updating this document itself. -->  ## Overview  Use Zest design system components f...

---

*Synced from spec-machine. Run `/sync-tech-context` to update.*
