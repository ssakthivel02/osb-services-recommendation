# Recommendation Production Readiness

Production is **NO-GO** until every applicable control has evidence.

## Required evidence

- Running service with authenticated `/api/v1/recommendations` endpoint
- Tenant claim derived from validated identity token
- Cross-tenant negative integration tests
- Child-profile and guardian-consent tests
- Restricted, deleted and expired content exclusion tests
- Sensitive-attribute targeting review
- Health, financial and political-persuasion prohibitions tested
- Versioned content catalogue, feature definitions and ranking model
- English and Tamil quality corpus
- Approved offline quality thresholds
- Diversity and concentration thresholds
- Cold-start fallback using verified age-safe content
- Load, timeout, rate-limit and dependency-failure tests
- Privacy impact and retention review
- Sanitised audit logging validation
- Dashboards and alert routing
- Rollback and cache-invalidation drill
- Backup and restore evidence
- Named service, security, privacy and safeguarding owners

## Release decision record

Record commit SHA, policy version, model version, dataset version, test evidence, known risks, approvers and rollback target for each deployment.
