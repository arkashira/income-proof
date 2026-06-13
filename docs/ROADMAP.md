# ROADMAP.md

## Project: **income‑proof**

> A lightweight service that authenticates with QuickBooks, pulls a user’s financial data, and stores it securely for downstream income‑verification workflows.

---

## Vision

Provide a **trust‑worthy, low‑friction pipeline** that turns a QuickBooks account into a verifiable source of income data for lenders, insurers, and other stakeholders.  
The service will be **API‑first**, secure, and easily extensible to other accounting platforms.

---

## 1. MVP – Must‑Have for Launch

| Feature | Description | MVP‑Critical? |
|---------|-------------|---------------|
| **OAuth2 Authentication** | Securely obtain an access token from QuickBooks using client ID/secret. | ✅ |
| **Data Pull** | Fetch core financial entities (Invoices, Bills, Payments, Accounts, Customers). | ✅ |
| **Data Normalization** | Map QuickBooks entities into a canonical JSON schema. | ✅ |
| **Secure Storage** | Persist the normalized data in an encrypted local file (`financial_data.json`) or a lightweight database (SQLite). | ✅ |
| **CLI Entrypoint** | `python accounting_platform.py` to trigger authentication & import. | ✅ |
| **Unit Tests** | `pytest` suite covering authentication, data mapping, and storage. | ✅ |
| **Documentation** | README with setup, usage, and testing instructions. | ✅ |
| **Error Handling** | Graceful handling of API failures, token refresh, and rate limits. | ✅ |
| **Logging** | Structured logs for auditability. | ✅ |

> **MVP Goal**: Deliver a fully functional, tested CLI that can pull and store data from a QuickBooks sandbox account within 2 weeks.

---

## 2. v1 – Core Platform (Phase 1)

| Theme | Milestones | Deliverables |
|-------|------------|--------------|
| **API Layer** | • Expose REST endpoints (`/auth`, `/import`, `/data`) <br>• Swagger/OpenAPI spec | • FastAPI app <br>• API docs |
| **Data Persistence** | • Migrate from JSON to SQLite <br>• Add schema migrations | • Alembic migrations <br>• ORM models |
| **Data Validation** | • Validate incoming QuickBooks data against schema <br>• Detect missing or inconsistent fields | • Validation module <br>• Error reporting |
| **Reporting** | • Basic financial reports (Income Statement, Balance Sheet) <br>• Export to CSV/Excel | • Report generator <br>• CLI/HTTP export |
| **Security** | • Encrypt database at rest <br>• Store secrets in environment variables | • Encryption utilities <br>• CI secret scan |
| **CI/CD** | • Automated tests, linting, and packaging | • GitHub Actions pipeline |
| **Documentation** | • Developer guide, API reference, deployment instructions | • Updated README & docs folder |

> **MVP‑Critical**: API Layer, Data Persistence, Data Validation.

---

## 3. v2 – Advanced Features (Phase 2)

| Theme | Milestones | Deliverables |
|-------|------------|--------------|
| **Multi‑Platform Support** | • Integrate Xero, FreshBooks, and Wave <br>• Abstract provider adapters | • Adapter interface <br>• Provider modules |
| **Automated Reconciliation** | • Match payments to invoices <br>• Flag discrepancies | • Reconciliation engine <br>• Dashboard |
| **Compliance & Auditing** | • Audit trail for data changes <br>• GDPR data‑subject rights | • Audit logs <br>• Data‑subject API |
| **Analytics & Insights** | • KPI dashboard (Cash Flow, Net Income) <br>• Predictive income forecasting | • Dashboard UI (React/Vue) <br>• Forecasting model |
| **Scalability** | • Containerize service (Docker) <br>• Deploy to Kubernetes | • Helm chart <br>• CI/CD to cluster |
| **Marketplace Integration** | • Publish as a reusable npm package / PyPI module <br>• SDK for other services | • SDK <br>• Publish scripts |
| **User Management** | • OAuth2 login for end‑users <br>• Role‑based access control | • Auth server <br>• RBAC module |

> **MVP‑Critical**: Multi‑Platform Support, Automated Reconciliation, Compliance.

---

## 4. Timeline (High‑Level)

| Sprint | Duration | Focus |
|--------|----------|-------|
| **Sprint 0** | 1 week | Project bootstrap, repo setup, CI pipeline |
| **Sprint 1** | 2 weeks | MVP features (auth, import, storage, tests) |
| **Sprint 2** | 2 weeks | API Layer, SQLite migration, validation |
| **Sprint 3** | 2 weeks | Reporting, security hardening, docs |
| **Sprint 4** | 2 weeks | Xero adapter, reconciliation engine |
| **Sprint 5** | 2 weeks | GDPR audit trail, compliance docs |
| **Sprint 6** | 2 weeks | Dashboard UI, forecasting model |
| **Sprint 7** | 2 weeks | Containerization, Helm chart, deployment |
| **Sprint 8** | 2 weeks | SDK, marketplace publishing, final QA |

---

## 5
