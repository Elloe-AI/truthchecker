from truthchecker.validator import TruthChecker

checker = TruthChecker()
claim = "All cancers are curable."
result = checker.validate(claim)
print("📋 Claim:", claim)
print("✅ Verdict:", result['verdict'])
print("🧠 Reason:", result['reason']) 