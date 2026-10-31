# FINAL REPORT ASSEMBLY QA

## Template and assembly scope

- **Template used:** `DAM140_Final_Assignment_Answer_Template-1.docx`, extracted from the frozen authoritative archive.
- **Output:** `DAM140_Final_Assessment_Report_ASSEMBLY_DRAFT.docx`.
- The template title, anonymity instruction, Section 1–4 order, eight assessment prompts, page size, one-inch margins and page-number footer were retained.
- Only approved Q1–Q7 report prose, the five approved figures/captions and the 20 approved Q8 references were inserted. Control records, audit tables, Markdown syntax and reconciliation content were excluded.
- `FINAL_REPORT_Q8_HARVARD_REFERENCES_APPROVED.md` is byte-identical to the passed Q8 draft: `2b8077278319ec5e83bf634e352a30aed006c7da7928cda9350346f664996504`.

## Section word-count and text verification

| Section | Approved count | Exact approved visible text retained | Independent whitespace-token count |
|---|---:|---|---:|
| Q1 | 271 | Yes | 268 |
| Q2 | 281 | Yes | 280 |
| Q3 | 267 | Yes | 266 |
| Q4 | 300 | Yes | 298 |
| Q5 | 270 | Yes | 269 |
| Q6 | 300 | Yes | 300 |
| Q7 | 288 | Yes | 288 |

The approved counts are preserved through exact paragraph-by-paragraph equality with the frozen section prose after converting Markdown formatting to Word formatting. The independent whitespace-token counts are reported separately because punctuation, hyphenation, slash-separated terms and citation formatting are counted differently by different word-count engines. No wording was changed to reconcile those differences.

## Figure placement and embedded-media verification

| Figure | Report section | DOCX media part | SHA-256 | Status |
|---|---|---|---|---|
| Figure B | Q2 | `word/media/image1.png` | `0d03946f78d9c4978d490ee5f4d3c65cd9e5118e8247b55f20ff4531c12c5fd0` | Exact match; embedded once |
| Figure C | Q2 | `word/media/image2.png` | `316792740ac83e737dc53593ac428bb03a4bf29ba9a0569eb93c05d4599fb99e` | Exact match; embedded once |
| Figure D | Q2 | `word/media/image3.png` | `774617e5d0ca2aa4db9dd1b3ff6cd09bc4453140d4857cdeee4e1e8dd50ae3ed` | Exact match; embedded once |
| Figure 4 | Q5 | `word/media/image4.png` | `2711a840931abbaa2ad119e9b8e28f2ef21911622b03c4e54f480cb9aa4f9908` | Exact match; embedded once |
| Figure 5 | Q5 | `word/media/image5.png` | `2c5dca9a6ef035278486b7cb1d657d983b42016bd426557a2b6020d05f28b1a6` | Exact match; embedded once |

- Each approved caption appears once and remains attached to its figure.
- Source PNG bytes are unchanged. Display-only scaling to 6.0 inches maximum width preserves aspect ratio and keeps all figures within the template margins.

## Citation and reference reconciliation

| In-text citation | Approved section(s) | Matching reference present | Exact label match |
|---|---|---|---|
| (Abid, 2019) | Q1 | Yes | Yes |
| (Abid and Izeboudjen, 2020) | Q1, Q2 | Yes | Yes |
| (Apache Software Foundation, n.d.-a) | Q6 | Yes | Yes |
| (Apache Software Foundation, n.d.-b) | Q6 | Yes | Yes |
| (Apache Software Foundation, n.d.-c) | Q6 | Yes | Yes |
| (Apache Software Foundation, n.d.-d) | Q6 | Yes | Yes |
| (Breiman, 2001) | Q4 | Yes | Yes |
| (Breiman et al., 1984) | Q4 | Yes | Yes |
| (Brodersen et al., 2010) | Q4 | Yes | Yes |
| (Hosmer, Lemeshow and Sturdivant, 2013) | Q4 | Yes | Yes |
| (Information Commissioner’s Office, 2023) | Q7 | Yes | Yes |
| (Information Commissioner’s Office, 2026) | Q7 | Yes | Yes |
| (Information Commissioner’s Office, n.d.-a) | Q7 | Yes | Yes |
| (Information Commissioner’s Office, n.d.-b) | Q7 | Yes | Yes |
| (Kubernetes Authors, 2025) | Q6 | Yes | Yes |
| (Kubernetes Authors, 2026) | Q6 | Yes | Yes |
| (Kubernetes Authors, n.d.) | Q6 | Yes | Yes |
| (Prometheus Authors, n.d.) | Q6 | Yes | Yes |
| (Roberts et al., 2017) | Q4 | Yes | Yes |
| (scikit-learn developers, n.d.) | Q4 | Yes | Yes |

- **Unique references:** 20.
- Every reference is cited in at least one approved section; no duplicate, uncited, superseded or unverified entry was added.
- Apache and ICO `n.d.` suffixes match the approved in-text labels. URLs and DOIs match the approved Q8 content and contain no tracking parameters.

## Render and visual inspection

- **Final page count:** 10 pages.
- The DOCX was rendered to page PNGs and PDF using the required DOCX renderer.
- All 10 pages were inspected at full-page resolution. No clipping, overlap, margin overflow, broken glyph, isolated section heading, separated figure caption or unreadable URL was found.
- After removing residual template revision/document identifiers from `word/settings.xml`, the document was rerendered; all 10 final page images were pixel-identical to the inspected render.

## Anonymity, metadata and document-integrity checks

- No name, email address, account identifier, conversation detail, AI reference or tool-generated citation syntax appears in the document body.
- Core-property `creator` and `lastModifiedBy` fields are empty; the custom-properties part is absent; template revision-session and document identifiers were removed.
- No comments, tracked insertions/deletions or reviewer markup are present.
- The DOCX package opens successfully and passes ZIP integrity testing.

## Template-formatting differences

- Blank response placeholders were replaced by the approved answers. The page count expanded naturally to 10 pages.
- The template had no dedicated answer-subheading, caption or reference style. Approved answer headings were formatted as bold Normal paragraphs; captions use centred 9-point Word text; references use a hanging-indent paragraph style based on the template Normal style. No template question, instruction or required section was removed.
- No other unavoidable formatting difference was identified.

**QA result: PASS — assembly content, figures, references, rendering and anonymity checks completed.**
