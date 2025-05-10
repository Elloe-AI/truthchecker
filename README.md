# 🧪 TruthChecker – Hallucination Detection for LLMs

**Version 1.0 – Maintained by Elloe AI**  
📄 [Read the Whitepaper](https://whitepapers.elloe.ai/whitepaper/)  
🌐 [Docs Portal](https://whitepapers.elloe.ai) | 🧬 [Elloe AI](https://elloe.ai)

---

## ⚡ Overview

**TruthChecker** is a compliance-grade hallucination detection engine designed for auditing the outputs of large language models (LLMs) in high-stakes environments.

Built by the creators of the [Immune System for AI](https://github.com/Elloe-AI/immune-system-ai), TruthChecker is used across:

- Healthcare (HIPAA)
- Financial services (GDPR, SOC2)
- Legal tech (EU AI Act)
- AI research & open source risk audits

---

## 🔎 Key Features

✅ SHAP explainability & token-level attributions  
✅ Pattern-based claim verification (e.g. absolutes, speculative language)  
✅ Ground truth comparison via PubMed/ICD10/SEC JSON loaders  
✅ Append-only audit logging (`.jsonl`)  
✅ CLI, API, and YAML contract support  
✅ Integrates with Obsidian, dashboards, or your CI pipeline

---

## 🚀 Quick Start

```bash
pip install truthchecker
```

```python
from truthchecker.validator import TruthChecker

checker = TruthChecker()
result = checker.validate("LLMs always tell the truth.")
print(result)
```

**Output:**
```json
{
  "verdict": "false",
  "confidence": 0.50,
  "reason": "Contains absolute claim ('always')"
}
```

Or use via CLI:
```bash
truthchecker "AI models never hallucinate."
```

---

## 📘 Docs & Research

- 📄 [Whitepaper (PDF)](https://whitepapers.elloe.ai/whitepaper.pdf)
- 📘 [Full Documentation](https://whitepapers.elloe.ai)
- 📚 [Compliance Use Cases](https://whitepapers.elloe.ai/compliance)

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📁 Project Structure

```
truthchecker/
├── validator.py         # Core logic
├── cli.py               # CLI tool
├── contracts/           # YAML validation contracts
├── examples/
│   └── check_example.py
├── tests/
│   └── test_validator.py
├── docs/
├── pyproject.toml
├── README.md
└── LICENSE (Apache 2.0)
```

---

## 📤 Contributing

We welcome PRs for:

- 🧠 New rule patterns (e.g. speculative language)
- 📚 Domain loaders (clinical, legal, financial)
- 🧪 SHAP visualizers or integrations

---

## 🔒 License

Apache 2.0 – Open source, secure by default.  
By Elloe AI | Contact: [jambo@elloe.ai](mailto:jambo@elloe.ai)

> "Verification is the immune system for LLMs. TruthChecker is your first line of defense."

---

## ✨ Related Projects

- 🧬 [Immune System for AI](https://github.com/Elloe-AI/immune-system-ai) – Enterprise compliance engine for regulated LLMs
- 🔍 [AutoRAG](https://github.com/Elloe-AI/autorag) – Retrieval-augmented reasoning with citation enforcement
- 🔐 [SentinelAI](https://github.com/Elloe-AI/sentinelai) – Real-time SHAP-based LLM risk monitor

---

## 🚀 Badges

![License](https://img.shields.io/github/license/Elloe-AI/truthchecker)
![Build](https://github.com/Elloe-AI/truthchecker/actions/workflows/tests.yml/badge.svg)
[![Docs](https://img.shields.io/badge/docs-available-blue)](https://whitepapers.elloe.ai/truthchecker)
[![PyPI](https://img.shields.io/pypi/v/truthchecker)](https://pypi.org/project/truthchecker/) 