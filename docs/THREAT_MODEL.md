# Recommendation Service Threat Model

## Protected assets

Tenant boundaries, learner profiles, guardian relationships, interaction history, recommendation integrity, source provenance, child-safety controls and service availability.

## Primary threats and controls

1. **Cross-tenant disclosure** — derive tenant scope only from validated identity claims; reject client tenant overrides.
2. **Sensitive-attribute targeting** — prohibit targeting based on health, religion, ethnicity, disability, sexuality, precise location or financial vulnerability.
3. **Child-content exposure** — require age-band metadata, child safety mode and guardian controls; block mature content.
4. **Restricted-content promotion** — exclude restricted, deleted, expired and unpublished content before candidate generation.
5. **Manipulative ranking** — cap popularity and freshness boosts; require source trust metadata and deterministic tie-breaking.
6. **Filter bubbles** — enforce category and source diversity limits.
7. **Profile leakage** — never log raw profiles or raw interaction histories; redact identifiers.
8. **Model poisoning** — validate ingestion provenance, isolate untrusted sources and monitor ranking shifts.
9. **Resource exhaustion** — cap candidates, results, request rate and execution time.
10. **Unsafe advice** — prohibit health diagnosis, financial advice and political-persuasion recommendations.
11. **Consent bypass** — verify guardian-child relationships before guided-content approval.
12. **Stale entitlement** — re-evaluate eligibility at serving time and remove deleted or expired content.

## Trust boundaries

API gateway, identity provider, recommendation service, feature store, content catalogue, event pipeline, ranking engine, cache and observability platform are separate trust boundaries.

## Release requirement

Production release requires cross-tenant negative tests, child-profile tests, consent tests, abuse simulations, ranking-quality evidence, load tests, rollback evidence and privacy review.
