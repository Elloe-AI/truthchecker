# AutoRAG

AutoRAG is a compliance-focused RAG (Retrieval-Augmented Generation) engine that enforces citation requirements and content filtering for regulated environments.

## Features

- **Citation Enforcement**
  - Automatic source tracking
  - Citation validation
  - Audit trail generation

- **Compliance Filtering**
  - Content policy enforcement
  - Regulatory requirement checking
  - Risk assessment

- **Integration**
  - Model-agnostic design
  - REST API support
  - Python SDK

## Quick Start

```python
from autorag import AutoRAG

rag = AutoRAG(
    knowledge_base="path/to/docs",
    citation_required=True,
    compliance_rules=["hipaa", "gdpr"]
)

response = rag.query("What are the side effects of X?")
print(response.citations)  # List of sources
print(response.compliance_score)  # Compliance rating
```

## Documentation

For detailed documentation, visit our [GitHub repository](https://github.com/Elloe-AI/autorag). 