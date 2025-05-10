"""
Example usage of TruthChecker.
"""

from truthchecker.validator import TruthChecker

def main():
    # Initialize the checker
    checker = TruthChecker()
    
    # Example claims to validate
    claims = [
        "The moon is made of cheese.",
        "The Earth is flat.",
        "In 2024, AI will achieve general intelligence.",
        "The sun rises in the east.",
        "Everyone knows that AI is dangerous.",
        "Scientists say that COVID-19 is a hoax.",
        "The capital of France is Paris."
    ]
    
    # Validate each claim
    for claim in claims:
        print(f"\nValidating: {claim}")
        result = checker.validate(claim)
        
        # Print results
        print(f"Verdict: {result['verdict']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Reason: {result['reason']}")
        
        if result['matches']:
            print("\nMatched Patterns:")
            for match in result['matches']:
                print(f"- {match['category']}: {match['matched_text']}")
        
        # Print top SHAP features
        if result['shap_values']:
            print("\nTop SHAP Features:")
            values = result['shap_values']['values']
            features = result['shap_values']['feature_names']
            # Sort by absolute SHAP value
            sorted_indices = sorted(range(len(values)), key=lambda i: abs(values[i]), reverse=True)
            for i in sorted_indices[:3]:  # Show top 3 features
                print(f"- {features[i]}: {values[i]:.3f}")

if __name__ == "__main__":
    main() 