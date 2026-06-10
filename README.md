<h3 align="center">🛠️ income-proof</h3>

<div align="center">
  <a href="https://github.com/axentx/income-proof/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/axentx/income-proof">
    <img src="https://img.shields.io/github/stars/axentx/income-proof?style=social" alt="Stars">
  </a>
  <a href="https://github.com/axentx/income-proof/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/axentx/income-proof/ci.yml" alt="Build Status">
  </a>
  <a href="https://pypi.org/project/income-proof/">
    <img src="https://img.shields.io/pypi/v/income-proof" alt="PyPI Version">
  </a>
</div>

---

# 🚀 income-proof

**Empower financial institutions and individuals with standardized, legally-compliant income verification documents.**

Automatically generate tax-return extracts, profit-and-loss statements, and bank-statement summaries from user-uploaded data with one-click PDF/JSON exports featuring digital signatures and QR codes.

## Why income-proof?

- **Legal compliance**: Templates adhere to international financial regulations
- **Built for banks**: Streamline loan application processing
- **Time savings**: Reduce manual document preparation by 90%
- **Audit-ready**: Digital signatures and QR codes ensure document integrity
- **Multi-format output**: Generate both PDF and JSON outputs simultaneously
- **Customizable fields**: Adapt templates to different financial products
- **Data security**: End-to-end encryption of sensitive financial information

## Feature Overview

| Feature | Description |
|---------|-------------|
| Template Library | Pre-built, legally-compliant document templates |
| Data Parsing | Automatic extraction of key financial metrics |
| Digital Signatures | Cryptographic verification of document authenticity |
| QR Code Generation | Embedded document verification codes |
| Multi-format Export | Simultaneous PDF and JSON output |
| User Interface | Simple web interface for document generation |

## Tech Stack

- Python 3.11
- FastAPI
- Pandas
- ReportLab
- PyPDF2
- Cryptography
- Jinja2

## Project Structure

```
business/      # Business logic and domain models
src/           # Core application code
tests/         # Test suites
README.md      # Project documentation
pyproject.toml # Project configuration
requirements.txt # Dependency list
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/axentx/income-proof.git
   cd income-proof
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

5. Run tests:
   ```bash
   pytest
   ```

## Deploy

```bash
# Example deployment command (adjust as needed)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.main:app
```

## Status

Last updated: [Date] - [Commit message]

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## License

MIT