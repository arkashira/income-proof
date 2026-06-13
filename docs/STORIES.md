# STORIES.md – Income‑Proof

## Overview
The **Income‑Proof** repository delivers a lightweight integration layer between our platform and QuickBooks.  
The backlog below is organized into **Epics** that map to the product’s core capabilities. Stories are ordered from **MVP → Extended** to guide incremental delivery while maintaining shippable increments.

---

## EPIC 1 – QuickBooks Authentication  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1 | **As a** *system administrator*, **I want** to configure QuickBooks OAuth client credentials in a secure `.env` file, **so that** the integration can authenticate without hard‑coding secrets. | - `.env` supports `QB_CLIENT_ID`, `QB_CLIENT_SECRET`, `QB_REDIRECT_URI`.<br>- Missing or malformed variables cause a clear startup error.<br>- Secrets are never logged or written to version‑controlled files. |
| 2 | **As a** *user*, **I want** to be redirected to QuickBooks for OAuth consent, **so that** I can grant the app permission to read my financial data. | - `/auth` endpoint initiates the OAuth flow and redirects to QuickBooks.<br>- After consent, QuickBooks redirects back with an authorization code.<br>- The code is exchanged for an access token and refresh token.<br>- Tokens are stored encrypted in `tokens.json`. |
| 3 | **As a** *system*, **I want** automatic token refresh, **so that** long‑running jobs never fail due to expired access tokens. | - Refresh token is used when API calls return 401.<br>- New access token is persisted to `tokens.json`.<br>- Refresh logic retries the original request once after a successful refresh. |

---

## EPIC 2 – Financial Data Import  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 4 | **As a** *financial analyst*, **I want** to pull a list of accounts from QuickBooks, **so that** I can see the chart of accounts in our system. | - `accounting_platform.py --list-accounts` prints a JSON array of accounts.<br>- API call uses the current access token.<br>- Handles pagination transparently.<br>- Errors are reported with a user‑friendly message. |
| 5 | **As a** *accountant*, **I want** to import transactions for a selectable date range, **so that** I can reconcile periods of interest. | - CLI flag `--from YYYY-MM-DD --to YYYY-MM-DD` filters transactions.<br>- Resulting data is written to `financial_data.json` in a deterministic schema.<br>- The file includes a checksum (SHA‑256) for integrity verification. |
| 6 | **As a** *developer*, **I want** the import process to be idempotent, **so that** re‑running it does not duplicate records. | - Each transaction is keyed by QuickBooks `Id`.<br>- Existing records are up‑serted, not appended.<br>- A log entry records “skipped – already present” for duplicates. |

---

## EPIC 3 – Secure Data Storage  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 7 | **As a** *security officer*, **I want** financial data at rest to be encrypted, **so that** confidential information is protected if the file system is compromised. | - `financial_data.json` is encrypted with AES‑256‑GCM using a key derived from `QB_ENCRYPTION_KEY` in `.env`.<br>- Decryption occurs only in memory during runtime.<br>- Attempting to read the file without the key raises a clear error. |
| 8 | **As a** *compliance auditor*, **I want** audit logs of every import operation, **so that** we have traceability for data handling. | - A `logs/` directory contains `import-<timestamp>.log` files.<br>- Logs capture start/end timestamps, user‑initiated parameters, number of records processed, and any errors.<br>- Logs are write‑only for the process (no external read without proper role). |

---

## EPIC 4 – CLI / UX  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 9 | **As a** *non‑technical user*, **I want** a clear help command (`-h/--help`), **so that** I can discover available actions without reading source code. | - Running `python accounting_platform.py -h` displays usage, description of each flag, and examples.<br>- Help output fits within 80‑character width for terminal readability. |
|10| **As a** *operations engineer*, **I want** a “dry‑run” mode, **so that** I can preview the data that would be imported without persisting it. | - Flag `--dry-run` runs the full fetch pipeline but writes to `dryrun_output.json` (unencrypted) and skips audit logging.<br>- CLI prints a summary: total records fetched, size of payload, and “dry‑run complete”. |

---

## EPIC 5 – Testing, CI & Quality Gates  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
|11| **As a** *QA engineer*, **I want** unit tests covering authentication, token refresh, and data parsing, **so that** regressions are caught early. | - `tests/` contains at least 90 % line coverage (measured by `pytest --cov`).\n- Mocks are used for external QuickBooks calls.\n- CI pipeline fails if coverage drops below 85 %. |
|12| **As a** *release manager*, **I want** a GitHub Actions workflow that runs the full test suite on every PR, **so that** only passing code is merged. | - Workflow triggers on `push` and `pull_request`.\n- Steps: install
