# FINAL REPORT Q6 — PROPOSED SCALABLE BIG-DATA ARCHITECTURE DRAFT

## Proposed scalable big-data architecture

The current dataset contains only 244 records. Therefore, this is a hypothetical extension for much larger historical, sensor, weather and regional datasets; it was not implemented, deployed, benchmarked or performance-tested, so no measured speed, cost, throughput, latency or reliability is claimed.

Continuous weather-station and sensor events would enter partitioned Apache Kafka topics, while controlled batch loaders would ingest historical files and external weather data (Apache Software Foundation, n.d.-a). Both paths would write to HDFS or equivalent distributed storage, separating immutable raw, validated and curated zones. Retaining raw inputs and versioned schemas would preserve traceability, while distributed blocks and replication would support larger retained datasets and recovery from node failure (Apache Software Foundation, n.d.-b).

Apache Spark workers would perform distributed cleaning, aggregation, feature preparation and model execution. Schema and data-quality checks would prevent release to the curated zone until validation passed. Spark streaming jobs could evaluate threshold rules and trigger messages, while scheduled batch work would remain separate (Apache Software Foundation, n.d.-c). Apache Airflow DAGs would coordinate ingestion, validation, transformation, modelling and reporting, recording dependencies, retries and execution logs; Airflow would not form the immediate alert path (Apache Software Foundation, n.d.-d).

Containerised analytical services would run across Kubernetes worker nodes and scale horizontally as demand increased, subject to configured metrics (Kubernetes Authors, 2026). Prometheus-style metrics and alerts would track failures, resource use, freshness and service health; data and model-drift monitoring would be a future control, not a completed project feature (Prometheus Authors, n.d.).

Managed secrets encrypted at rest and role-based access would protect credentials (Kubernetes Authors, 2025; Kubernetes Authors, n.d.). Encryption in transit, data minimisation, retention rules, and versioned code, models and logs support governance and reproducibility. This design offers parallelism and traceability beyond a single machine, but adds infrastructure cost, operational complexity and specialist skill requirements.

---

## Draft control record

**Exact word count:** 300 words, including the section heading and in-text citations. The document title and this control record are excluded.

**In-text citations used:**
- `(Apache Software Foundation, n.d.-a)` — A-01, Kafka partitioned ingestion.
- `(Apache Software Foundation, n.d.-b)` — A-02, HDFS distributed storage and replication.
- `(Apache Software Foundation, n.d.-c)` — A-03, Spark distributed and incremental processing.
- `(Apache Software Foundation, n.d.-d)` — A-04, Airflow DAG orchestration, dependencies, retries and monitoring.
- `(Kubernetes Authors, 2026)` — A-05, container scheduling and horizontal scaling.
- `(Prometheus Authors, n.d.)` — A-06, operational metrics and alerting.
- `(Kubernetes Authors, 2025)` — A-07, secret-management security controls.
- `(Kubernetes Authors, n.d.)` — A-08, role-based access control.

The `n.d.-a` to `n.d.-d` suffixes distinguish the four approved Apache Software Foundation sources with the same undated corporate author.

**Reference-register entries used:** A-01, A-02, A-03, A-04, A-05, A-06, A-07 and A-08.

**Compliance check:**
- The architecture is explicitly hypothetical and tied to a future larger version of the 244-record project.
- No implementation, deployment, benchmarking, performance-testing or measured service-level claim appears.
- Ingestion, distributed storage, processing, orchestration, deployment, monitoring, security and governance are covered.
- Data movement from source ingestion through raw, validated and curated zones to processing, threshold alerts and reporting is explained.
- Reliability, reproducibility and raw-to-output traceability are addressed without promising zero downtime.
- Infrastructure cost, operational complexity and specialist skill requirements are acknowledged.
- Only approved architecture sources are cited.
- No privacy-law detail reserved for Q7 and no visual were added.
- The section is within the 300-word maximum.
