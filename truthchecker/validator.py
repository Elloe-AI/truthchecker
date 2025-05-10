"""
TruthChecker class for validating text using SHAP and pattern matching.
"""

import re
import json
import numpy as np
import shap
from pathlib import Path
from typing import Dict, List, Optional, Union

class TruthChecker:
    """A class for validating text using SHAP and pattern matching."""
    
    def __init__(self, ground_truth_path: Optional[str] = None):
        """
        Initialize the TruthChecker.
        
        Args:
            ground_truth_path: Optional path to a JSON/CSV file containing ground truth data
        """
        # Common factual error patterns
        self.patterns = {
            'impossible_claims': [
                r'made of cheese',
                r'is flat',
                r'is hollow',
                r'caused by bacteria',  # COVID-19 example
                r'is a hoax',
                r'doesn\'t exist',
            ],
            'temporal_claims': [
                r'in \d{4}',
                r'during the \d{4}s',
                r'next year',
                r'in the future',
            ],
            'absolute_claims': [
                r'always',
                r'never',
                r'everyone',
                r'nobody',
                r'every',
                r'all',
            ],
            'scientific_claims': [
                r'proven by science',
                r'scientists say',
                r'research shows',
                r'studies prove',
            ]
        }
        
        # Load ground truth data if provided
        self.ground_truth = self._load_ground_truth(ground_truth_path) if ground_truth_path else {}
        
        # Initialize SHAP explainer (placeholder)
        self.explainer = None
        
    def _load_ground_truth(self, path: str) -> Dict:
        """Load ground truth data from JSON/CSV file."""
        path = Path(path)
        if not path.exists():
            return {}
            
        if path.suffix == '.json':
            with open(path, 'r') as f:
                return json.load(f)
        elif path.suffix == '.csv':
            # TODO: Implement CSV loading
            return {}
        else:
            raise ValueError(f"Unsupported ground truth file format: {path.suffix}")
    
    def _check_patterns(self, text: str) -> dict:
        """Check text against known error patterns."""
        results = {
            'matches': [],
            'confidence': 1.0
        }
        
        for category, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    results['matches'].append({
                        'category': category,
                        'pattern': pattern,
                        'matched_text': re.search(pattern, text, re.IGNORECASE).group(0)
                    })
                    # Reduce confidence based on category severity
                    if category == 'impossible_claims':
                        results['confidence'] *= 0.3
                    elif category == 'scientific_claims':
                        results['confidence'] *= 0.7
                    elif category == 'absolute_claims':
                        results['confidence'] *= 0.5
                    # Temporal claims don't reduce confidence
        
        return results
    
    def _check_ground_truth(self, text: str) -> dict:
        """Check text against ground truth data."""
        if not self.ground_truth:
            return {'matches': [], 'confidence': 1.0}
            
        # TODO: Implement ground truth checking
        return {'matches': [], 'confidence': 1.0}
    
    def _get_shap_values(self, text: str) -> dict:
        """
        Get SHAP values for the text.
        In a real implementation, this would use a trained model.
        """
        # Simulate SHAP values for demonstration
        features = ['word_count', 'has_numbers', 'has_dates', 'has_claims',
                   'sentence_count', 'avg_word_length', 'has_capitals',
                   'has_punctuation', 'has_quotes', 'has_parentheses']
        
        # Generate random SHAP values for demonstration
        values = np.random.normal(0, 1, len(features))
        
        return {
            'values': values.tolist(),
            'feature_names': features,
            'base_value': 0.0,
            'data': [1.0] * len(features)  # Placeholder feature values
        }
    
    def validate(self, text: str) -> dict:
        """
        Validate text for factual errors and hallucinations.
        
        Args:
            text (str): The text to validate
            
        Returns:
            dict: Validation results including verdict and explanation
        """
        # Check patterns
        pattern_results = self._check_patterns(text)
        
        # Check ground truth
        ground_truth_results = self._check_ground_truth(text)
        
        # Get SHAP values
        shap_results = self._get_shap_values(text)
        
        # Determine verdict
        is_valid = pattern_results['confidence'] > 0.5 and ground_truth_results['confidence'] > 0.5
        
        # Prepare explanation
        if pattern_results['matches']:
            matches = pattern_results['matches']
            reason = f"Contains {len(matches)} potential issues: " + \
                    ", ".join(f"{m['category']} ({m['matched_text']})" for m in matches)
        elif ground_truth_results['matches']:
            reason = "Contradicts ground truth data"
        else:
            reason = "No issues detected"
        
        # Combine results
        result = {
            'verdict': 'true' if is_valid else 'false',
            'reason': reason,
            'confidence': min(pattern_results['confidence'], ground_truth_results['confidence']),
            'matches': pattern_results['matches'] + ground_truth_results['matches'],
            'shap_values': shap_results
        }
        
        return result 