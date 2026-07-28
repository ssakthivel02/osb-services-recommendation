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
    require(POLICY['allowClientTenantOverride'] is False, 'Cross-tenant override risk')
    require(POLICY['excludeRestrictedContent'] is True, 'Restricted content exposure risk')
    require(POLICY['allowSensitiveAttributeTargeting'] is False, 'Sensitive profiling risk')
    require(POLICY['allowHealthDiagnosisRecommendations'] is False, 'Unsafe health recommendation risk')
    require(POLICY['allowFinancialAdviceRecommendations'] is False, 'Unsafe financial recommendation risk')
    require(POLICY['allowPoliticalPersuasionRecommendations'] is False, 'Political manipulation risk')
    require(POLICY['childSafetyModeRequired'] is True, 'Child safety bypass risk')
    require(POLICY['guardianControlsRequired'] is True, 'Guardian-control bypass risk')
    require(POLICY['maximumResults'] <= 50, 'Unbounded result amplification risk')
    require(POLICY['maximumCandidateCount'] <= 500, 'Candidate explosion risk')
    require(POLICY['requestTimeoutMilliseconds'] <= 3000, 'Backend exhaustion risk')
    require(POLICY['diversity']['maximumSameCategoryRatio'] <= 0.5, 'Filter-bubble concentration risk')
    require(POLICY['diversity']['maximumSameSourceRatio'] <= 0.4, 'Single-source dominance risk')
    require(POLICY['ranking']['needsReviewPenalty'] < 1.0, 'Unverified content promotion risk')
    require(POLICY['privacy']['logRawProfile'] is False, 'Profile leakage risk')
    require(POLICY['privacy']['logRawHistory'] is False, 'History leakage risk')
    require(ELIGIBILITY['sourceClassifications']['restricted']['eligible'] is False, 'Restricted source eligibility risk')
    require(ELIGIBILITY['childProfiles']['allowMature'] is False, 'Mature child-content exposure risk')
    require(ELIGIBILITY['childProfiles']['requireGuardianApprovalForGuided'] is True, 'Guided-content consent risk')
    print('Recommendation negative safety cases passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
