# 📄 Product Requirements Document (PRD)  
**Project:** `income-proof`  
**Owner:** Senior Product/Engineering Lead – Axentx  
**Date:** 2026‑06‑13  

---  

## 1. Overview  

`income-proof` is a SaaS tool that enables individuals and small businesses to generate **official‑grade proof‑of‑income documents** directly from their QuickBooks accounting data. By automating the extraction, verification, and formatting of income information, the product removes the manual, error‑prone process of gathering bank statements, tax returns, and payroll slips for loan applications, rental agreements, visa processes, and other compliance‑driven use‑cases.  

The MVP will be built on top of the existing `income-proof` repository, which currently contains a minimal QuickBooks OAuth flow and a script that dumps raw financial data to `financial_data.json`. The PRD expands this foundation into a production‑ready, revenue‑validated offering.

---  

## 2. Problem Statement  

| Pain Point | Who Experiences It | Why It Matters |
|------------|-------------------|----------------|
| **Manual income verification** – Users must collect multiple statements, reconcile them, and manually format a proof document. | Freelancers, gig workers, small‑business owners, and their lenders/landlords. | Time‑consuming, error‑prone, leads to delayed loan approvals or lease sign‑offs. |
| **Lack of a trusted, auditable source** – Third‑party documents (pay stubs, PDFs) are often rejected for not being tied to an accounting system. | Financial institutions, property managers, immigration services. | Increases friction, forces users to pay for expensive accountant services. |
| **Data security & compliance** – Users are hesitant to share raw accounting exports because of privacy concerns. | Any user handling sensitive financial data. | Trust barrier prevents adoption. |

**Result:** A market segment of ~2.5 M U.S. freelancers + ~1 M small businesses actively seeks a fast, secure, and verifiable income‑proof solution. Early validation (via BD interviews) shows willingness to pay **$12‑$20 / month** for a self‑service product.

---  

## 3. Target Users  

| Segment | Primary Persona | Key Characteristics |
|---------|----------------|----------------------|
| **Freelance Professionals** | *Alex*, 32, UI/UX designer on Upwork, earns $8‑12k/mo, needs proof for a mortgage. | Uses QuickBooks Self‑Employed, low technical expertise, values speed. |
| **Micro‑Businesses** | *Sam*, 45, owner of a boutique marketing agency, 5 employees, QuickBooks Online. | Needs periodic income statements for bank lines of credit. |
| **Lenders / Property Managers (B2B)** | *Rita*, 38, loan officer at a community bank, processes 150 applications/mo. | Wants an API to verify income instantly, reduces manual underwriting. |

---  

## 4. Goals & Success Metrics  

| Goal | Metric | Target (12 mo) |
|------|--------|----------------|
| **Revenue** | Monthly Recurring Revenue (MRR) | $120 k |
| **Adoption** | Paid users (individual + B2B) | 5 k |
| **Retention** | Net Revenue Retention (NRR) | 115 % |
| **Product Quality** | 99.5 % successful data imports (no auth errors) | ≥ 99.5 % |
| **Compliance** | SOC‑2 Type II attestation | Achieved by month 9 |
| **Customer Satisfaction** | NPS | ≥ 55 |

---  

## 5. Assumptions  

1. **QuickBooks remains the dominant accounting platform** for the target segments (≥ 70 % market share).  
2. Users already have a QuickBooks account and are comfortable granting OAuth access.  
3. The core data model (Invoices, Payments, Expenses) is stable across QuickBooks Online & Self‑Employed APIs.  
4. Axentx can leverage existing infrastructure (pgvector knowledge store, CI/CD pipelines) for secure storage and model‑driven document generation.  

---  

## 6. Constraints  

| Constraint | Detail |
|------------|--------|
| **Regulatory** | Must store PII/PCI data in encrypted-at‑rest storage (AES‑256) and support GDPR/CCPA deletion requests. |
| **Performance** | Income‑proof PDF generation ≤ 2 seconds for a typical 12‑month data set. |
| **Scalability** | System must handle 10 k concurrent OAuth sessions during peak onboarding. |
| **Budget** | Initial MVP budget capped at $250 k (engineering + security audit). |
| **Technology Stack** | Must stay within the approved stack: Python 3.11, FastAPI, PostgreSQL, AWS (ECS/Fargate), vLLM for any LLM‑based data validation. |

---  

## 7
