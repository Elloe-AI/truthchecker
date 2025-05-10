"""
Command-line interface for TruthChecker.
"""

import json
import argparse
from .validator import TruthChecker

def main():
    parser = argparse.ArgumentParser(
        description="Validate text for factual errors and hallucinations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  truthchecker "The moon is made of cheese."
  truthchecker "In 2024, AI will achieve general intelligence."
        """
    )
    parser.add_argument("text", help="The text to validate")
    parser.add_argument("--ground-truth", help="Path to ground truth data file (JSON/CSV)")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    
    args = parser.parse_args()
    
    # Initialize checker and validate text
    checker = TruthChecker(ground_truth_path=args.ground_truth)
    result = checker.validate(args.text)
    
    # Output JSON result
    if args.pretty:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps(result))

if __name__ == "__main__":
    main() 