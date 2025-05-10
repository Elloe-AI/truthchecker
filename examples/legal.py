from truthchecker.validator import TruthChecker

checker = TruthChecker()
claim = "This law applies globally with no exception."
result = checker.validate(claim)
print("📋 Claim:", claim)
print("✅ Verdict:", result['verdict']) 