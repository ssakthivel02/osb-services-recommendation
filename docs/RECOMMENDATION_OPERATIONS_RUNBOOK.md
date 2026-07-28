# Recommendation Operations Runbook

## Health checks

Verify API health, identity-provider reachability, catalogue freshness, feature-store latency, event-pipeline lag, cache health and ranking-engine availability.

## Key metrics

Track request rate, success rate, p50/p95/p99 latency, candidate count, result count, empty-result rate, fallback rate, tenant-filter failures, child-safety exclusions, restricted-content exclusions, source diversity, category diversity, low-confidence rate and stale-content rate.

## Alerts

- Severity 1: cross-tenant result, restricted-content exposure, child-safety bypass, profile leakage or sustained service outage.
- Severity 2: major latency breach, stale catalogue, ranking anomaly, event-pipeline lag or high fallback rate.
- Severity 3: quality drift, localised empty-result increase or non-critical dependency degradation.

## Incident response

1. Capture request ID and deployment version without recording raw profile/history.
2. Disable affected recommendation strategy using feature flags.
3. Fall back to verified, age-safe, tenant-scoped popular content.
4. Invalidate unsafe caches and revoke affected model/index versions.
5. Preserve sanitised audit evidence.
6. Notify security, privacy, safeguarding and service owners as applicable.
7. Complete root-cause analysis and regression tests before re-enablement.

## Recovery

Restore the last approved policy, model, feature definitions and content snapshot. Confirm tenant isolation, child safety, source eligibility, diversity and latency before reopening traffic.
