# Recommendation Quality Evaluation

## Offline evaluation

Evaluate Precision@K, Recall@K, NDCG@K, MRR, catalogue coverage, category diversity, source diversity, novelty, serendipity, calibration, popularity bias and cold-start performance.

## Safety slices

Results must be separately evaluated for:

- English and Tamil locales
- Every supported age band
- Child and guardian-managed profiles
- New users with no history
- Low-activity users
- Each tenant
- Verified versus needs-review sources
- Guided-content consent state

## Hard gates

A release fails if any test exposes cross-tenant content, restricted content, mature content to a child profile, guided content without required guardian approval, sensitive-attribute targeting, or source metadata omission.

## Online evaluation

Use controlled experiments with pre-defined success and guardrail metrics. Guardrails include complaint rate, hide/report rate, unsafe-content exclusions, concentration ratios, latency, empty-result rate and fallback rate.

## Evidence

Store dataset version, policy version, model version, feature definition version, evaluation code commit, metric results, approver and release decision. Never store raw personal profiles in evaluation artefacts.
