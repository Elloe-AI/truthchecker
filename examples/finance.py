from truthchecker.validator import TruthChecker

checker = TruthChecker()
claim = "Tesla's Q3 profits tripled."
result = checker.validate(claim)
print("📋 Claim:", claim)
print("✅ Verdict:", result['verdict']) 