#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / 'config/recommendation-policy.json').read_text(encoding='utf-8'))
ELIGIBILITY = json.loads((ROOT / 'config/content-eligibility.json').read_text(encoding='utf-8'))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    require(POLICY['apiPrefix'].startswith('/api/v1/'), 'API must be versioned')
    require(POLICY['requireAuthentication'] is True, 'Authentication must be required')
    require(POLICY['enforceTenantIsolation'] is True, 'Tenant isolation must be enforced')
    require(POLICY['allowClientTenantOverride'] is False, 'Tenant override must be rejected')
    require({'en-GB', 'ta-IN'} <= set(POLICY['supportedLocales']), 'English and Tamil locales required')
    require(1 <= POLICY['defaultResults'] <= POLICY['maximumResults'] <= 50, 'Result limits invalid')
    require(POLICY['requestTimeoutMilliseconds'] <= 3000, 'Timeout exceeds baseline')
    require(POLICY['maximumCandidateCount'] <= 500, 'Candidate cap exceeds baseline')
    require(0 <= POLICY['minimumConfidence'] <= 1, 'Confidence must be bounded')
    require(POLICY['excludeRestrictedContent'] is True, 'Restricted content must be excluded')
    require(POLICY['allowSensitiveAttributeTargeting'] is False, 'Sensitive targeting forbidden')
    require(POLICY['allowHealthDiagnosisRecommendations'] is False, 'Health diagnosis recommendations forbidden')
    require(POLICY['allowFinancialAdviceRecommendations'] is False, 'Financial advice recommendations forbidden')
    require(POLICY['allowPoliticalPersuasionRecommendations'] is False, 'Political persuasion forbidden')
    require(POLICY['childSafetyModeRequired'] is True, 'Child safety mode required')
    require(POLICY['guardianControlsRequired'] is True, 'Guardian controls required')
    require(POLICY['diversity']['enabled'] is True, 'Diversity controls required')
    require(POLICY['diversity']['maximumSameCategoryRatio'] <= 0.5, 'Category concentration too high')
    require(POLICY['diversity']['maximumSameSourceRatio'] <= 0.4, 'Source concentration too high')
    require(POLICY['ranking']['deterministicTieBreak'] == 'content_id', 'Deterministic tie-break required')
    require(POLICY['privacy']['logRawProfile'] is False, 'Raw profile logging forbidden')
    require(POLICY['privacy']['logRawHistory'] is False, 'Raw history logging forbidden')
    require(30 <= POLICY['privacy']['minimumEventRetentionDays'] <= POLICY['privacy']['maximumEventRetentionDays'] <= 365, 'Retention bounds invalid')

    required = set(ELIGIBILITY['requiredMetadata'])
    require({'content_id', 'tenant_id', 'locale', 'age_band', 'content_rating', 'source_id', 'source_classification'} <= required, 'Required metadata incomplete')
    require(ELIGIBILITY['sourceClassifications']['restricted']['eligible'] is False, 'Restricted source must be ineligible')
    require(ELIGIBILITY['childProfiles']['allowMature'] is False, 'Mature content must be blocked for children')
    print('Recommendation baseline validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
