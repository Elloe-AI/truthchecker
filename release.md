# 🧪 TruthChecker v0.1.0 – Hallucination Detection for LLMs

We're excited to launch **TruthChecker**, a lightweight open-source module for detecting hallucinations and unsupported claims in large language model (LLM) outputs.

Originally developed as a core part of the **Immune System for AI**, TruthChecker is now available as a standalone library under the Apache 2.0 license.

---

## 🔍 What It Does

TruthChecker helps developers and AI safety teams:
- Detect factual errors in LLM responses
- Explain decisions using SHAP
- Run quick CLI- or API-based validation
- Integrate with any model output pipeline

---

## 🚀 Get Started

```bash
pip install truthchecker
```

## 📋 Key Features

- **SHAP-based Validation**: Leverage SHAP (SHapley Additive exPlanations) values for transparent decision-making
- **Confidence Scoring**: Get clear confidence scores for claim validation
- **Context-Aware**: Support for additional context in validation
- **Extensible**: Easy integration with custom validation models
- **Developer-Friendly**: Simple CLI and Python API

## 💻 Quick Example

```python
from truthchecker import TruthChecker

# Initialize the checker
checker = TruthChecker()

# Validate a claim
result = checker.validate(
    claim="The Earth is flat",
    context={"source": "Example source"},
    threshold=0.5
)

print(f"Confidence: {result['confidence']}")
print(f"Explanation: {result['explanation']}")
```

## 🔧 Development

TruthChecker is built with modern Python practices:
- Python 3.8+ support
- Comprehensive test suite
- GitHub Actions CI/CD
- Apache 2.0 licensed

## 🤝 Contributing

We welcome contributions! Check out our [GitHub repository](https://github.com/Elloe-AI/truthchecker) to:
- Report bugs
- Suggest features
- Submit pull requests
- Join our community

## 📚 Documentation

For detailed documentation, visit our [GitHub repository](https://github.com/Elloe-AI/truthchecker).

---

*TruthChecker is part of the Elloe AI initiative to make AI systems more reliable and trustworthy.* 