# FINAL REPORT Q7 — PRIVACY, LEGISLATION AND MITIGATION DRAFT

## Privacy issues, legislation and mitigations

The current 244-record public analytical dataset contains no direct personal identifiers. Privacy risks would arise only if a future UK public-facing platform processed personal data such as precise locations, account or device identifiers, alert subscriptions or usage histories. The relevant framework would be the UK GDPR and Data Protection Act 2018, as amended by the Data (Use and Access) Act 2025 (Information Commissioner’s Office, 2026).

**1. Data minimisation.** Collecting precise coordinates or persistent identifiers alongside weather observations could reveal routines and exceed the platform’s defined purpose. UK GDPR Article 5(1)(c) requires personal data to be adequate, relevant and limited to what is necessary (Information Commissioner’s Office, n.d.-a). The platform should default to coarse regions, restrict schemas to justified fields, make precise location optional and purpose-bound, and separate identity from pseudonymised analytical records. These controls reduce unnecessary collection and linkage.

**2. Storage limitation.** Replicated raw stores, backups and logs could retain identifiable location or user histories after their operational value ends. Article 5(1)(e) requires identifiable personal data to be kept no longer than necessary (Information Commissioner’s Office, n.d.-b). Field-specific retention schedules, automated deletion or anonymisation, backup lifecycle rules, documented exceptions and periodic reviews would remove or de-identify expired records and provide evidence of retention control.

**3. Integrity, confidentiality and security.** Distributed ingestion, storage, processing and deployment services create risks of unauthorised access, disclosure, alteration or loss. Article 5(1)(f) and Article 32 require security measures appropriate to processing risk (Information Commissioner’s Office, 2023). Encryption in transit and at rest, authentication, administrator MFA, RBAC and least privilege, managed secrets, access logging, patching, tested backups and incident-response procedures would reduce compromise and support recovery. These measures lower risk but do not guarantee compliance or prevent every breach.

---

## Draft control record

**Exact word count:** 288 words, including the section heading, numbered issue labels and in-text citations. The document title and this control record are excluded.

**Three issue–law–mitigation mappings:**

| Issue | Specific law or principle | Risk in the hypothetical platform | Concrete mitigation |
|---|---|---|---|
| Data minimisation | UK GDPR Article 5(1)(c) | Unnecessary precise location, account or persistent device data could reveal routines and exceed the analytical purpose. | Coarse-region defaults, schema restrictions, optional purpose-bound precise location, and separation of identity from pseudonymised analytical records. |
| Storage limitation | UK GDPR Article 5(1)(e) | Raw stores, replicas, backups and logs could retain identifiable histories after their operational purpose ends. | Field-specific retention schedules, automated deletion or anonymisation, backup lifecycle rules, documented exceptions and periodic reviews. |
| Integrity, confidentiality and security | UK GDPR Article 5(1)(f) and Article 32 | Distributed services could expose personal data to unauthorised access, disclosure, alteration or loss. | Encryption, authentication, administrator MFA, RBAC/least privilege, managed secrets, logging, patching, tested backups and incident response. |

**In-text citations used:**
- `(Information Commissioner’s Office, 2026)` — L-03, current UK framework and DUAA relationship.
- `(Information Commissioner’s Office, n.d.-a)` — L-04, Article 5(1)(c) data minimisation.
- `(Information Commissioner’s Office, n.d.-b)` — L-05, Article 5(1)(e) storage limitation.
- `(Information Commissioner’s Office, 2023)` — L-06, Article 5(1)(f) and Article 32 security requirements.

The `n.d.-a` and `n.d.-b` suffixes distinguish the two approved undated ICO principle pages.

**Approved reference-register entries used:** L-03, L-04, L-05 and L-06. L-01 and L-02 remain approved framework references for Q8 but are not separately cited in this compact section.

**Compliance check:**
- Exactly three privacy issues are covered.
- Each issue is linked to a specific UK GDPR principle or article and a concrete technical or organisational mitigation.
- The current public dataset is not described as containing identifiable personal data; risks are framed for a future scaled platform.
- No legal guarantee, definitive legal conclusion or claim of implemented controls appears.
- Only approved legal and regulatory sources were used.
- No visual or unapproved technology detail was added.
- The section is within the 300-word maximum.
