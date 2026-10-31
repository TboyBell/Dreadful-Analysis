# Loan Application Tracking System — Database Design

A relational database modelling project demonstrating **database design, entity relationship modelling, normalisation, relational schema design and data integrity principles**.

The project was completed as part of the DAM106 Database module and focused on translating a set of business requirements for a loan application tracking system into a structured relational data model.

## Technical Focus

The primary purpose of this project was to demonstrate competency in relational database design.

Rather than focusing only on the business scenario, the project required the system requirements to be decomposed into:

- entities
- attributes
- relationships
- primary keys
- foreign keys
- cardinality constraints
- relational tables
- integrity rules

The resulting database model provides a structured representation of the data required to support a loan application workflow.

---

## Technologies & Techniques

### Database Modelling

The system was designed using relational modelling principles.

The modelling process involved identifying real-world concepts within the requirements and representing them as independent entities.

For example, information relating to applicants and loan applications should not be repeatedly stored inside one large record. Instead, separate entities can be created and related using keys.

Conceptually:

```text
Applicant
    │
    │ submits
    ▼
Loan Application
    │
    │ contains / references
    ▼
Associated Application Data
```

This reduces duplication and enables information to be maintained independently.

---

## Entity Relationship Modelling

An **Entity Relationship Diagram (ERD)** was developed to represent the logical structure of the database.

The ERD was used to define:

- entities within the system
- attributes belonging to each entity
- primary keys
- foreign keys
- relationships between entities
- relationship cardinality
- dependency between records

This provided a visual representation of the database before implementation.

### Example relationship structure

```text
ENTITY A
──────────────
PK entity_a_id
   attribute_1
   attribute_2

        │
        │ 1
        │
        │ M
        ▼

ENTITY B
──────────────
PK entity_b_id
FK entity_a_id
   attribute_1
   attribute_2
```

The foreign key allows records in `ENTITY B` to reference the corresponding parent record in `ENTITY A`.

This approach demonstrates understanding of how relational databases represent relationships without duplicating complete records.

---

## Visual Paradigm

The database model was developed using **Visual Paradigm**, with the project stored using its `.vpp` project format.

Visual Paradigm was used to construct and maintain the ERD, allowing the relational structure of the proposed database to be communicated visually.

The modelling process included the representation of:

```text
Entities
   ↓
Attributes
   ↓
Primary Keys
   ↓
Foreign Keys
   ↓
Relationships
   ↓
Cardinality
```

This supported the transition from business requirements to a logical database design.

---

## Primary Keys

Each entity was designed with a mechanism for uniquely identifying individual records.

A primary key provides:

```text
Table
────────────────────
PK record_id
   attribute
   attribute
   attribute
```

The primary key prevents ambiguity between otherwise similar records and provides a stable identifier that can be referenced elsewhere in the database.

---

## Foreign Keys

Foreign keys were used to establish relationships between tables.

For example:

```text
Applicants
────────────────
PK applicant_id
   name
   ...

LoanApplications
────────────────
PK application_id
FK applicant_id
   ...
```

Instead of duplicating all applicant information inside every application record, the application stores a reference to the applicant.

This demonstrates the relational principle of representing associations through keys rather than repeated data.

---

## Cardinality

Relationships were modelled according to the expected number of records that could participate in each relationship.

Examples of relational cardinality include:

```text
1 : 1
One-to-One

1 : M
One-to-Many

M : N
Many-to-Many
```

Understanding cardinality is important because it determines how relationships should be represented within the relational schema.

For example, a one-to-many relationship can typically be implemented using a foreign key on the "many" side:

```text
Applicant             LoanApplication
────────────           ────────────────
PK applicant_id  1 ─── M PK application_id
                         FK applicant_id
```

---

## Database Normalisation

The database design applied **normalisation principles** to reduce unnecessary duplication and improve data integrity.

The modelling process considered the progressive separation of data according to relational dependencies.

### First Normal Form — 1NF

Data should contain atomic values rather than repeating groups.

Instead of:

```text
Applicant
─────────────────────────────
applicant_id
loan_1
loan_2
loan_3
```

a separate application table allows each application to exist as an independent record.

```text
LoanApplication
────────────────
application_id
applicant_id
```

### Second Normal Form — 2NF

Attributes should depend on the full key of the relation rather than only part of a composite identifier.

### Third Normal Form — 3NF

Non-key attributes should describe the entity identified by the primary key rather than depend on other non-key attributes.

Applying these principles helps minimise:

- duplicate data
- update anomalies
- insertion anomalies
- deletion anomalies
- conflicting information

---

## Referential Integrity

The design considered the need to preserve valid relationships between records.

For example:

```text
LoanApplication.applicant_id
              │
              ▼
Applicant.applicant_id
```

An application should not reference an applicant that does not exist.

Foreign-key relationships therefore provide a mechanism for protecting the logical integrity of the data model.

---

## From Requirements to Schema

One of the key competencies demonstrated by this project is translating a non-technical business description into a technical data structure.

The process can be represented as:

```text
Business Requirements
        │
        ▼
Identify Data Concepts
        │
        ▼
Identify Entities
        │
        ▼
Define Attributes
        │
        ▼
Define Primary Keys
        │
        ▼
Define Relationships
        │
        ▼
Determine Cardinality
        │
        ▼
Apply Normalisation
        │
        ▼
Create ERD
        │
        ▼
Relational Database Model
```

This process is fundamental to both **database design and data architecture**.

---

## Design Considerations

The database was designed with several core relational principles in mind.

### Data Integrity

The schema should prevent invalid relationships and minimise inconsistent data.

### Reduced Redundancy

Information should be stored once where possible and referenced through relational keys.

### Maintainability

Separating distinct business concepts into entities makes the database easier to understand and modify.

### Extensibility

A structured relational model makes it easier to introduce additional functionality without redesigning the entire database.

### Traceable Relationships

Foreign keys allow relationships between records to be explicitly represented and queried.

---

## Technical Competencies Demonstrated

This project demonstrates competency in:

**Database Design**

- relational database modelling
- logical data modelling
- schema design
- table decomposition

**Entity Relationship Modelling**

- entity identification
- attribute modelling
- ERD development
- relationship modelling
- cardinality analysis

**Relational Database Concepts**

- primary keys
- foreign keys
- referential integrity
- relational dependencies
- one-to-many relationships

**Data Modelling**

- translating business requirements into data structures
- modelling real-world concepts as entities
- separating logical data domains

**Normalisation**

- reducing data redundancy
- understanding functional dependencies
- avoiding update, insertion and deletion anomalies
- applying normalisation principles

**Architecture & Design**

- designing before implementation
- representing system information structurally
- communicating database architecture visually

---

## Project Files

The original project contains:

```text
├── Answers Template.docx
├── Databases Final Assessment Brief.docx
├── End_Of_Module_Assignment.vpp
└── Loan_Application_Tracker.jpg
```

### `End_Of_Module_Assignment.vpp`

Visual Paradigm modelling project containing the database design.

### `Loan_Application_Tracker.jpg`

Exported visual representation of the database model / ERD.

---

## What This Project Demonstrates

The key outcome of this project was not simply creating a database diagram.

It demonstrated the ability to take a business domain and reason about:

```text
What data exists?

How should that data be grouped?

What uniquely identifies each record?

Which data depends on other data?

How should entities relate?

Where should foreign keys sit?

What cardinality exists between entities?

How can duplication be reduced?

How can data integrity be protected?
```


