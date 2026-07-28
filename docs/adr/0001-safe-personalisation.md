# ADR 0001: Safe, Tenant-Scoped Personalisation

## Status

Accepted for baseline implementation.

## Context

The platform serves multilingual educational and devotional content to adults and children. Personalisation can improve relevance but creates privacy, tenant-isolation, safeguarding, manipulation and concentration risks.

## Decision

Use a tenant-scoped candidate-generation and ranking pipeline. Eligibility filtering occurs before ranking. Identity claims provide tenant and user context; request parameters cannot override tenant scope. Every candidate requires age-band, content-rating, source, status and locale metadata.

Ranking may use behavioural and contextual signals only after privacy and consent checks. Sensitive attributes are prohibited. Popularity and freshness boosts are capped. Verified sources receive a bounded boost; needs-review sources receive a penalty. Diversity constraints and deterministic tie-breaking are mandatory.

Child profiles require safety mode and guardian controls. The service must provide a verified, age-safe fallback that does not depend on behavioural history.

## Consequences

Quality optimisation cannot override safety or tenant boundaries. Model, policy, feature and catalogue versions must be independently auditable and reversible. Production remains blocked until integration, safety, quality, privacy, load and recovery evidence is available.
