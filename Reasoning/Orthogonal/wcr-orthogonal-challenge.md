# Orthogonal Challenge: Workflow-Centric Reorganization

**Date:** 2026-02-02
**Challenger:** Claude Code (Self-Challenge)
**Subject:** WCR Requirements v1.0

---

## Challenge Categories

### 1. Architecture Challenges

#### 1.1 Three-Folder Simplicity vs Reality
**Challenge:** The clean `/products`, `/team`, `/personal` split assumes work maps neatly to these buckets. Reality is messier.

**Examples of Edge Cases:**
- A meeting about OTP launch with Beatrice - is it `/products/good-chop/discussions/` or `/team/reports/beatrice/meetings/`?
- Career planning for a PM who owns a product - is feedback about their product performance in their career file or the product file?
- A presentation about team velocity - product or team?

**Resolution:**
- **Primary location rule**: File lives where it provides most value for retrieval
- **Symlinks/references**: Context files can reference files in other locations
- **Meeting routing heuristic**: 1:1s → team, group meetings → product, unless override
- **Dual indexing**: Brain entities can reference multiple workspace paths

#### 1.2 Hierarchy Depth
**Challenge:** Requirements allow unlimited nesting (org → brand → product → feature → project). This could become unwieldy.

**Recommendation:**
- Limit to 3 levels: Organization → Product/Brand → Feature/Project
- Features and projects are leaf nodes (no sub-features)
- Use tags/labels for cross-cutting concerns rather than deeper nesting

#### 1.3 Context File Proliferation
**Challenge:** Every folder gets a context file. With 4 brands × ~5 features each = 20+ context files. Maintenance burden?

**Resolution:**
- Context files are auto-generated from brain, not manually maintained
- Only active projects get full context files
- Archived projects get minimal context (status, key dates, final outcomes)
- Implement staleness detection - flag context files not updated in 30 days

### 2. Data Flow Challenges

#### 2.1 Bi-Directional Sync Conflicts
**Challenge:** If both brain and context file are sources of truth, what happens when they conflict?

**Resolution:**
- **Last-write-wins with timestamp**: Most recent change wins
- **Conflict detection**: If both changed since last sync, flag for manual review
- **Field ownership**: Some fields are brain-authoritative (entity relationships), some are context-authoritative (status, current focus)
- **Immutable fields**: IDs, creation dates never change

#### 2.2 Discovery Enrichment Scope
**Challenge:** Auto-enrichment could pull in massive amounts of data when a new product is detected.

**Resolution:**
- **Bounded search**: Limit to last 90 days of data
- **Relevance threshold**: Only include docs with high confidence match
- **User confirmation**: For large enrichments, ask before proceeding
- **Incremental enrichment**: Start minimal, add more on demand

#### 2.3 Meeting Routing Logic
**Challenge:** How does system know if a meeting is about a product vs about a person?

**Routing Rules (in order):**
1. If attendees include only user + one report → `/team/reports/{person}/1on1s/`
2. If meeting title contains product name → `/products/{product}/discussions/`
3. If meeting is recurring series with person name → `/team/.../1on1s/`
4. If meeting has multiple attendees from same squad → `/products/{squad-product}/discussions/`
5. Default → `/products/{default-product}/discussions/` or general inbox

### 3. User Experience Challenges

#### 3.1 Breaking Existing Workflows
**Challenge:** Users who have memorized current paths will be disrupted.

**Mitigations:**
- **Migration script with symlinks**: Old paths redirect to new
- **Transition period**: Support both paths for 30 days
- **Path aliases in tools**: `$SPRINT_REPORTS` resolves dynamically
- **Clear changelog**: Document all path changes

#### 3.2 Config Complexity
**Challenge:** New config sections add significant complexity. Users might not know how to configure.

**Mitigations:**
- **Sensible defaults**: System works without full config
- **Setup wizard**: `/workspace-setup` command guides through configuration
- **Config validation**: Catch errors early with helpful messages
- **Example configs**: Provide templates for different user types (IC PM, PM Manager, Director)

#### 3.3 Navigation Overhead
**Challenge:** Deeper folder structure means more clicks/typing to reach files.

**Mitigations:**
- **Smart aliases**: `/open gc` → opens Good Chop context
- **Recent files**: Track recently accessed for quick access
- **Search integration**: Brain search finds files across structure
- **IDE integration**: VSCode folder shortcuts

### 4. Technical Challenges

#### 4.1 Tool Update Scope
**Challenge:** Many tools need updates. Risk of breaking things.

**Strategy:**
- **Phased rollout**: Update tools one at a time
- **Feature flags**: New paths behind flag until stable
- **Compatibility layer**: `path_resolver.py` abstracts old→new mapping
- **Test coverage**: Add tests before changing paths

#### 4.2 Performance Concerns
**Challenge:** More files, more context files, more sync operations.

**Mitigations:**
- **Lazy loading**: Only sync context files when accessed
- **Caching**: Cache brain queries for repeated access
- **Batch operations**: Group file operations
- **Async sync**: Background sync doesn't block user

#### 4.3 Brain Entity Proliferation
**Challenge:** New workspace fields on all entities increases brain size.

**Resolution:**
- **Sparse fields**: Only add workspace_path to entities that have corresponding folders
- **Reference by ID**: Store folder→entity mapping in separate index file
- **Cleanup routine**: Remove workspace_path for deleted folders

### 5. Scope Challenges

#### 5.1 MVP Definition
**Challenge:** Full implementation is large. What's the MVP?

**MVP Scope:**
1. Config schema for products and team (no auto-detection yet)
2. Folder creation from config
3. Context file generation (brain → context only)
4. Sprint report path update
5. Migration script for existing files

**Phase 2 (Post-MVP):**
- Bi-directional sync
- Auto-detection
- Meeting routing
- Discovery enrichment

#### 5.2 Out of Scope (Explicitly)
- Custom folder structures (user defines their own sub-folders)
- Multi-user PM-OS (shared workspaces)
- Real-time sync with external systems
- Mobile/web access to folders

---

## Challenge Summary

| Category | Challenges Found | Resolution Quality |
|----------|------------------|-------------------|
| Architecture | 3 | ✅ Resolved with constraints |
| Data Flow | 3 | ✅ Resolved with rules |
| User Experience | 3 | ✅ Resolved with mitigations |
| Technical | 3 | ✅ Resolved with phased approach |
| Scope | 2 | ✅ MVP defined |

**Verdict:** Requirements are sound with identified constraints. Proceed with MVP scope.

---

## Recommended Requirement Updates

Based on this challenge, update requirements to:

1. **Add hierarchy limit**: Max 3 levels (org → product → feature)
2. **Add meeting routing rules**: Explicit heuristics for file placement
3. **Add MVP scope section**: Phase 1 vs Phase 2 features
4. **Add conflict resolution rules**: Timestamp-based, field ownership
5. **Add migration compatibility layer**: Symlinks during transition

---

*Challenge completed: 2026-02-02*
*Challenger confidence: HIGH*
*Recommendation: PROCEED with noted constraints*
