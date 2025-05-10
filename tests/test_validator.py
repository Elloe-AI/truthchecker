"""
Test cases for TruthChecker.
"""

import pytest
from truthchecker.validator import TruthChecker

def test_truthchecker_initialization():
    checker = TruthChecker()
    assert checker.patterns is not None
    assert 'impossible_claims' in checker.patterns
    assert 'temporal_claims' in checker.patterns

def test_validate_impossible_claim():
    checker = TruthChecker()
    result = checker.validate("The moon is made of cheese.")
    assert result['verdict'] == 'false'
    assert result['confidence'] < 1.0
    assert len(result['matches']) > 0
    assert any(m['category'] == 'impossible_claims' for m in result['matches'])

def test_validate_temporal_claim():
    checker = TruthChecker()
    result = checker.validate("In 2024, AI will achieve general intelligence.")
    assert result['verdict'] == 'true'  # Temporal claims are not automatically invalid
    assert len(result['matches']) > 0
    assert any(m['category'] == 'temporal_claims' for m in result['matches'])

def test_validate_factual_claim():
    checker = TruthChecker()
    result = checker.validate("The sun rises in the east.")
    assert result['verdict'] == 'true'
    assert result['confidence'] == 1.0
    assert len(result['matches']) == 0

def test_shap_values_structure():
    checker = TruthChecker()
    result = checker.validate("Test claim")
    assert 'shap_values' in result
    assert 'values' in result['shap_values']
    assert 'feature_names' in result['shap_values']
    assert len(result['shap_values']['values']) == 10  # Placeholder size
    assert len(result['shap_values']['feature_names']) == 10

def test_validate_without_model():
    checker = TruthChecker()
    result = checker.validate("Test claim")
    assert isinstance(result, dict)
    assert 'verdict' in result
    assert 'confidence' in result
    assert 'matches' in result
    assert 'shap_values' in result

def test_validate_with_model():
    # TODO: Add test with mock model
    pass 