---
sidebar_position: 2
title: Abstract
---

> This section is informative

Unlike legacy systems designed for internal data management, DECADE-X as a Data Space is explicitly built to facilitate cross-organizational and cross-domain collaboration while enabling data providers to retain control over the conditions under which their data is shared and used.

A Data Space does not require the creation of a massive, centralized repository; instead, data remains at its source, and transactions occur through secure, peer-to-peer interfaces mediated by standardized protocols and services.

The semantic interoperability layer provides the necessary infrastructure to leverage shared agreements on the meaning and structure of data during inter-company exchanges and for the integration of externally provided information into each participant’s backend systems. It ensures that business data exchanged between participants conforms to published, discoverable, machine-readable, and operational specifications. As a result, data can not only be retrieved, but also read, interpreted, and reused across organizational and domain boundaries.

In such a decentralized environment, each participant remains responsible for transforming and exposing its local data according to two complementary levels of interoperability:

- **Syntactic Interoperability:** Refers to the structure and syntax of the data exchanged, including schemas and models.
- **Semantic Interoperability:** Addresses the meaning and interpretation of data, utilizing ontologies, vocabularies, and relationships.

---
sidebar_position: 3
title: 1. Scope
---

> This section is normative

## General Scope

This standard presents the semantic interoperability layer of the DECADE-X dataspace. In this layer, standard vocabularies and data model specifications are exposed to the dataspace and used to ensure that business exchanges between dataspace partners can be read by any service.

***What is covered:***

*This document provides the standard rules for a service to operate within the DECADE-X semantic interoperability layer to exchange interoperable business data.*

***Applicability:***

*This standard applies to any service exchanging business data across different legal entities in a DECADE-X use case.*

***Target Audience:***

*The target audience for this standard is semantic experts, architects, and service developers.*

***Out of Scope:***

*This standard does not apply to the internal data structures of dataspace participants. It does not apply to technical and workflow synchronisation exchanges within the dataspace ecosystem.*

## Conformance and Notations

If sections are marked as non-normative, all authoring guidelines, diagrams, examples, and notes in these sections are non-normative. Everything else in this specification is normative.

The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD and SHOULD NOT in this document are to be interpreted as described in [[BCP 14](https://www.rfc-editor.org/info/bcp14)], [[RFC2119](https://www.w3.org/TR/did-1.0/#bib-rfc2119)], [[RFC8174](https://www.w3.org/TR/did-1.0/#bib-rfc8174)] when, and only when, they appear in all capitals, as shown here.

---
sidebar_position: 4
title: 2. Normative References
---

> This section is normative

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document, including any amendments, applies.

## Standards and technical specifications

**[BCP14]** IETF, *Best Current Practice 14*, comprising RFC 2119 and RFC 8174. [https://www.rfc-editor.org/info/bcp14](https://www.rfc-editor.org/info/bcp14)

**[RFC2119]** Bradner, S., *Key words for use in RFCs to Indicate Requirement Levels*, BCP 14, RFC 2119, March 1997. [https://www.rfc-editor.org/info/rfc2119](https://www.rfc-editor.org/info/rfc2119)

**[RFC8174]** Leiba, B., *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*, BCP 14, RFC 8174, May 2017. [https://www.rfc-editor.org/info/rfc8174](https://www.rfc-editor.org/info/rfc8174)

**[CWA18125]** CEN, *CWA 18125:2024 — Trusted Data Transaction*, July 2024. [https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/RI/2024/cwa18125_2024.pdf](https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/RI/2024/cwa18125_2024.pdf)

**[RFC9110]** Fielding, R., Nottingham, M., and Reschke, J., *HTTP Semantics*, STD 97, RFC 9110, June 2022. [https://www.rfc-editor.org/info/rfc9110](https://www.rfc-editor.org/info/rfc9110)

**[RDF11-CONCEPTS]** W3C, *RDF 1.1 Concepts and Abstract Syntax*, W3C Recommendation, 25 February 2014. [https://www.w3.org/TR/rdf11-concepts/](https://www.w3.org/TR/rdf11-concepts/)

**[RDF11-SEMANTICS]** W3C, *RDF 1.1 Semantics*, W3C Recommendation, 25 February 2014. [https://www.w3.org/TR/rdf11-mt/](https://www.w3.org/TR/rdf11-mt/)

**[RDFS11]** W3C, *RDF Schema 1.1*, W3C Recommendation, 25 February 2014. [https://www.w3.org/TR/rdf-schema/](https://www.w3.org/TR/rdf-schema/)

**[TURTLE]** W3C, *RDF 1.1 Turtle: Terse RDF Triple Language*, W3C Recommendation, 25 February 2014. [https://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/)

**[RDF11-XML]** W3C, *RDF 1.1 XML Syntax*, W3C Recommendation, 25 February 2014. [https://www.w3.org/TR/rdf-syntax-grammar/](https://www.w3.org/TR/rdf-syntax-grammar/)

**[OWL2-SYNTAX]** W3C, *OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition)*, W3C Recommendation, 11 December 2012. [https://www.w3.org/TR/owl2-syntax/](https://www.w3.org/TR/owl2-syntax/)

**[SHACL]** W3C, *Shapes Constraint Language (SHACL)*, W3C Recommendation, 20 July 2017. [https://www.w3.org/TR/shacl/](https://www.w3.org/TR/shacl/)

**[JSON-LD11]** W3C, *JSON-LD 1.1: A JSON-based Serialization for Linked Data*, W3C Recommendation, 16 July 2020. [https://www.w3.org/TR/json-ld11/](https://www.w3.org/TR/json-ld11/)

**[JSON-SCHEMA-CORE]** JSON Schema, *JSON Schema: A Media Type for Describing JSON Documents*, Draft 2020-12, 16 June 2022. [https://json-schema.org/draft/2020-12/json-schema-core.html](https://json-schema.org/draft/2020-12/json-schema-core.html)

**[JSON-SCHEMA-VALIDATION]** JSON Schema, *JSON Schema Validation: A Vocabulary for Structural Validation of JSON*, Draft 2020-12, 16 June 2022. [https://json-schema.org/draft/2020-12/json-schema-validation.html](https://json-schema.org/draft/2020-12/json-schema-validation.html)

**[SEMVER]** Preston-Werner, T., *Semantic Versioning 2.0.0*. [https://semver.org/spec/v2.0.0.html](https://semver.org/spec/v2.0.0.html)

## Other referenced documents and vocabularies

**[RDF11-PRIMER]** W3C, *RDF 1.1 Primer*, W3C Working Group Note, 24 June 2014. [https://www.w3.org/TR/rdf11-primer/](https://www.w3.org/TR/rdf11-primer/)

**[VOCAB-PUB]** W3C, *Best Practice Recipes for Publishing RDF Vocabularies*, W3C Working Group Note, 28 August 2008. [https://www.w3.org/TR/swbp-vocab-pub/](https://www.w3.org/TR/swbp-vocab-pub/)

**[FAIR]** Wilkinson, M. D. et al., *The FAIR Guiding Principles for scientific data management and stewardship*, Scientific Data 3, 160018, 2016. [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

**[MOD]** *MOD: Metadata for Ontology Description and Publication*, release 2.0, 6 December 2021. [https://www.isibang.ac.in/ns/mod/](https://www.isibang.ac.in/ns/mod/)

**[CC-BY-4.0]** Creative Commons, *Attribution 4.0 International (CC BY 4.0)*, Version 4.0. [https://creativecommons.org/licenses/by/4.0/legalcode.en](https://creativecommons.org/licenses/by/4.0/legalcode.en)

---
sidebar_position: 5
title: 3. Terms and Definitions
---

> This section is normative

In this standard, the terms and definitions of the CEN Workshop Agreement on Trusted Data Transaction (CWA 18125) are used when applicable.

Additionally, several terms used in this standard are defined in the following table:

| Term | Relationship to the Business Object | Definition |
| --- | --- | --- |
| Business Object | The Anchor | The conceptual or physical object of interest (e.g., a "Battery," a "Wind Turbine," or a "Shipment") that is the subject of an exchange in the context of a use case. |
| Source Data | The Raw Evidence | The records residing in local systems (ERP, IoT, CRM) that describe the state or history of the Business Object. Example: For a Purchase Order (Business Object), SAP is the local system, while the EKPO table/dataset is the Source Data. |
| Conceptual Model | The Definition | The semantic blueprint (Ontology) that provides a shared meaning and language for the Business Object across the Data Space. |
| Data model | The logical definition | The logical class/attribute-based definition of the Business Object. |
| Data Schema | The Technical Mold | The structural specification (e.g., JSON Schema) defining the fields, types, and constraints required to digitally represent the Business Object. |
| Standardized Dataset | The Implementation | The digital resource resulting from mapping Source Data onto the Data Schema and Conceptual Model for a specific Business Object. |
| Semantic Hub | Where dataproduct specifications are exposed | The digital service that exposes the applicable semantic models defining the semantics and syntax of DECADE-X dataproducts. |

---
sidebar_position: 1
title: 4.1 Business Context
---

> This section is mixed

The main objective of this standard is to enable reliable inter-company exchanges of business information between dataspace participants. This means that exchanged data must not only be technically transferred from one participant to another. It must also be sufficiently structured, explicit, and documented to be interpreted in the same way by the data provider, the data consumer, and the services processing the information.

In this context, interoperability is not limited to the ability to send or receive data. It includes the ability to understand what the data represents, determine the role of each business object, identify the context of use, verify conformity against the applicable standard, and reuse the information in downstream processes.

The standard supports a common operational objective: allowing each participant to expose or consume data through the dataspace while keeping its internal systems and processes under its own responsibility. Participants are not required to use the same backend applications or the same internal data models. However, they are expected to exchange information according to normalized dataproducts that conform to the DECADE-X standard.

## Actors Impacted by the Standard

The standard impacts all actors involved in the preparation, exchange, validation, integration, and consumption of business data within the dataspace.

**Data providers** are responsible for exposing business data in a form that conforms to the applicable DECADE-X dataproduct specification. They remain responsible for transforming information from their local systems into the normalized exchange structure expected by the dataspace.

**Data consumers** rely on the standard to retrieve, interpret, validate, and integrate externally provided information into their own business processes and information systems. The standard reduces the risk of misunderstanding by making the exchanged data explicit and aligned with a shared business meaning.

**Business application providers** are impacted because their services must be able to produce, consume, or process standard dataproducts according to the relevant use case context. These applications often ensure local data conformity against the standard definition by performing data quality tests.

**Backend integration services** are impacted because they bridge the participant’s internal information systems with the standardized dataspace exchanges. They support the transformation between local data structures and the normalized dataproduct representation used in DECADE-X.

**Business users** are impacted because the standard defines the shared meaning of exchanged information. It supports a common understanding of business objects, statuses, classifications, traceability information, and declarations exchanged between organizations.

**Governance and conformity actors** are impacted because the standard provides the reference against which exchanged data can be checked. This supports trust, consistency, and interoperability across the dataspace.

## Standard dataproduct

In DECADE-X, standardized business data is exchanged in the form of standard dataproducts. A dataproduct is the normalized exchange unit used to carry business information between dataspace participants, together with the metadata required to support interoperability, traceability, auditability, and conformity.

The purpose of a dataproduct is to prevent ambiguity during inter-company exchanges. A conformant dataproduct should provide enough information for the receiving participant or service to understand what is being exchanged, in which context it is exchanged, who provided it, which version is concerned, and which business interpretation must be applied.

A DECADE-X dataproduct typically contains:

- **Business objects:** They are the subject of the exchange (see the Business Object definition in the glossary).
- **Synchronisation objects:** They are objects used for business synchronisation between partners. They are not the main focus of the exchange but are essential to provide the business context and intended use of the Business Objects (i.e., projects, milestones, technical agreements, etc.).
- **Traceability metadata:** The dataproduct always specifies the data provider, publication date, version, and all necessary information to ensure the traceability of the dataproduct across different companies.
- **Data classification:** The dataproduct should include the data governance classifications required by regulation, contractual commitments, or industrial policies.
- **Declaration of conformity:** A valid dataproduct always specifies the DECADE-X standard specification against which its conformity can be assessed. This conformity can be checked at any time by any stakeholder using the dataproduct.

The same business or synchronisation object may be represented differently in different dataproducts, depending on the operational purpose of the exchange. For example, one exchange may require a complete representation of a business object, while another may only require a reference or a subset of key information sufficient to synchronize status, traceability, or decision-making between partners.

## Technical Notifications Supporting Business Synchronization

In addition to standard dataproducts carrying business information, technical notifications may be specified to support synchronization between services and participants.

A notification is not intended to replace the business dataproduct itself. Its purpose is to inform another service or participant that a relevant event has occurred, such as a change of status, an update of an exchanged object, the availability of a new version, or the need to trigger a downstream process.

Notifications support operational coordination in a decentralized environment. Since participants do not operate on a single shared platform, services may need to be informed when an exchanged resource changes or when an action is expected. The standard may therefore define notification patterns where they are required by the business workflow.

The business meaning of a notification must remain explicit. A receiving service or participant should be able to understand what changed, which business object or dataproduct is concerned, and what action or interpretation is expected in the use case context.

## Accessibility and Publication of Data Models

The data models supporting the standard are made accessible to participants so that the rules, concepts, and expected structures of the exchanged data can be found, understood, and reused. Therefore, the DECADE-X data standard exposition follows the FAIR principles. This means that DECADE-X standard models are Findable, Accessible, Interoperable, and Reusable.

The Semantic Hub acts as the operational access point for these models. It exposes the shared definitions, vocabularies, data models, and related semantic resources required to interpret and validate standardized data exchanges. This supports a common understanding across companies, business applications, and digital services.

The publication of data models is essential because each participant remains responsible for its own implementation. A participant must be able to retrieve the relevant model, identify the applicable version, understand the expected business structure, and apply it consistently in its own environment.

## Normalization of Local Data for Inter-Company Exchange

Participants may manage their business information in historical backend systems, proprietary applications, local databases, or domain-specific tools. These systems may use internal structures, local identifiers, company-specific terminology, or formats that are not directly understandable outside the organization.

Before information is exchanged with another dataspace participant, it must be normalized according to the applicable DECADE-X dataproduct specification. This normalization transforms local business information into a shared representation that can be interpreted and reused outside the original company context.

This does not require all participants to change their internal systems. Instead, the standard provides the common exchange representation that each participant must produce or consume at the boundary of the dataspace. Backend integration services and business applications may use the data models to map local information to the normalized dataproduct structure.

The normalization process supports both outbound and inbound flows. For outbound exchanges, local data is transformed into a standard dataproduct before being shared with another participant. For inbound exchanges, a received standard dataproduct can be interpreted, validated, and integrated into the receiving participant’s own information system.

## Business Workflow Overview

In order to provide information to another DECADE-X participant, the data provider prepares the relevant information from its local systems and business processes. Depending on the business context (often defined in a DECADE-X use case workflow), the data provider selects a target DECADE-X dataproduct to transfer its data. The local information is then normalized into the expected structure of the target dataproduct model. Mandatory metadata is added to assemble a dataproduct instance before information sharing.

Before exchange, the dataproduct should be checked against the applicable standard model. This conformity step ensures that the exchanged information follows the expected structure and business rules. It also helps identify missing, inconsistent, or ambiguous information before the data is consumed by another participant or service.

Once the dataproduct is available, it can be exchanged through the dataspace according to the applicable business and technical conditions. The receiving participant retrieves the dataproduct and interprets it using the same shared model definitions. The received information can then be validated, processed, displayed to business users, or integrated into local backend systems with a denormalization step.

If the use case requires synchronization between services, a notification may be exchanged to indicate that a relevant event has occurred. The receiving service can then react according to the business process, for example by retrieving an updated dataproduct, updating a local status, or continuing a workflow.

The workflow is therefore based on a shared responsibility model: the provider is responsible for exposing conformant and meaningful data; the consumer is responsible for validating and integrating the received data according to the same standard; and the shared semantic layer provides the common reference needed by both sides.

## Expected Business Result

The expected result of this standard is to make inter-company data exchanges reliable, interpretable, and reusable across the DECADE-X ecosystem.

A participant should be able to exchange data with another participant without requiring a specific bilateral interpretation agreement for each new interface. The standard provides the common business meaning and normalized structure needed to scale exchanges across multiple companies, applications, and use cases.

The standard also supports digital continuity across organizational boundaries. Business information created in one company can be retrieved and reused by another company or service while preserving its meaning, context, and traceability. This enables more consistent collaboration across the supply chain and reduces the effort required to integrate external information into local operations.

By using standard dataproducts, accessible data models, conformity verification, and normalized exchange structures, DECADE-X creates the conditions for scalable interoperability between partners. The business value of the semantic interoperability layer is therefore not limited to data description. It enables operational data exchange, local integration, automated validation, and trusted reuse across the decentralized dataspace.

---
sidebar_position: 2
title: 4.2 Technical Architecture
---

> This section is mixed

## Conformity Test (Business Application Point of View): How to Send and Receive a Conformant Dataproduct and When to Use the Semantic Hub in the Workflow

## Model exposition on the DECADE-X semantic hub

DECADE-X standard models **SHALL** be exposed by a DECADE-X semantic hub at the [vocabulary.decade-x.org](http://vocabulary.decade-x.org) subdomain address.

The DECADE-X semantic hub **SHOULD** follow the ‘Best Practice Recipes for Publishing RDF Vocabularies’ ([https://www.w3.org/TR/swbp-vocab-pub/](https://www.w3.org/TR/swbp-vocab-pub/)) of the W3C.

In particular:

DECADE-X standard models’ documentation **SHALL** be accessible by a GET request at the model’s URI address with the header `Accept: text/html`.

DECADE-X standard models’ content **SHALL** be accessible by a GET request at the model’s URI address and **SHALL** support HTTP content negotiation for standard W3C RDF serialization formats ([https://www.w3.org/TR/rdf11-primer/#section-graph-syntax](https://www.w3.org/TR/rdf11-primer/#section-graph-syntax)), including Turtle (`text/turtle`) and RDF/XML (`application/rdf+xml`), according to the value of the `Accept` header.

A DECADE-X Application Profile **SHALL** have an associated JSON Schema specification. This JSON Schema specification **SHALL** be accessible by a GET request at the model’s URI address with the header `Accept: application/schema+json`.

A DECADE-X standard model version that is not fully specified **SHALL** resolve to the latest available version matching the specified version components according to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html), regardless of the representation format requested through HTTP content negotiation using the `Accept` header. For example, version `1.1` **SHALL** resolve to the latest `1.1.x` version (e.g. `1.1.4`), and version `2` **SHALL** resolve to the latest `2.x.x` version (e.g. `2.3.1`).

## Rules and Recommendations for Model Use

Before being exchanged, any dataproduct instance **SHALL** be validated against the applicable DECADE-X SHACL models in order to assess and declare its conformity.

A semantic processing engine using DECADE-X standard models **SHALL** support the W3C [Shapes Constraint Language (SHACL) Recommendation](https://www.w3.org/TR/shacl/).

A dataproduct **SHALL NOT** be exchanged when the validation against the applicable DECADE-X SHACL models fails or cannot be completed.

The semantic processing engine **SHALL** recursively resolve and load all dependencies declared through `owl:imports`.

The semantic processing engine **SHALL** support RDFS inference and SHALL apply inference before SHACL conformity validation.

The SHACL processor **SHALL** support SHACL Core constraints.

Conformity validation **SHALL** take into account the data graph, the applicable SHACL shapes, the ontology definitions and their imported dependencies.

A service **SHALL NOT** declare a dataproduct conformant when a semantic feature required by the applicable DECADE-X model cannot be processed.

Implementations **MAY** use any RDF, inference and SHACL processing libraries provided that the requirements defined in this section are fulfilled.

---
sidebar_position: 3
title: 4.3 Data Models and Semantics
---

> This section is mixed

Three types of documents are exposed by the DECADE-X Semantic Interoperability Layer:

- **Ontologies:** they provide definitions of classes, relations and properties used in DECADE-X.
- **SHACL models:** they provide conformity rules and constraints for DECADE-X data products.
- **JSON Schemas:** they provide a JSON specification for conformant DECADE-X data product exchanges using REST APIs.

**This section is normative:**

DECADE-X ontologies and SHACL models **SHALL** declare their model IRI as an instance of `owl:Ontology` using `rdf:type` (`a owl:Ontology`).

DECADE-X ontologies and SHACL models **SHALL** provide their model version using the `owl:versionInfo` property. The version **SHALL** follow the [Semantic Versioning](https://semver.org/spec/v2.0.0.html) specification.

DECADE-X ontologies and SHACL models **SHALL** provide an `owl:versionIRI` identifying the specific published version of the model.

Previous published versions of DECADE-X ontologies and SHACL models **SHALL** remain accessible through their version IRIs.

DECADE-X ontologies and SHACL models **SHALL** include the metadata required for their identification and publication within the DECADE-X Semantic Hub.

DECADE-X ontologies and SHACL models **SHOULD** use the [MOD vocabulary](https://www.isibang.ac.in/ns/mod/) for model metadata where an appropriate MOD property exists.

DECADE-X ontologies and SHACL models **SHALL** use RDF as their data model and **SHALL** provide a normative serialization using the [Turtle syntax](https://www.w3.org/TR/turtle/).

DECADE-X IRIs for ontologies **SHALL** use the pattern `https://vocabulary.decade-x.org/ontology/xxxx/n#`, where “xxxx” is the ontology short name and “n” is the major version according to the [Semantic Versioning](https://semver.org/spec/v2.0.0.html) specification.

DECADE-X IRIs for SHACL models **SHALL** use the pattern `https://vocabulary.decade-x.org/semanticModel/xxxx/n#`, where “xxxx” is the SHACL model short name and “n” is the major version according to the [Semantic Versioning](https://semver.org/spec/v2.0.0.html) specification.

The `owl:versionIRI` of DECADE-X ontologies and SHACL models **SHALL** identify the complete published version of the model, including its major, minor, and patch version.

DECADE-X ontologies and SHACL models **SHALL** use `owl:imports` to explicitly declare dependencies on other DECADE-X ontologies or SHACL models.

DECADE-X SHACL models **SHALL** conform to the [W3C Shapes Constraint Language (SHACL) Recommendation of 20 July 2017](https://www.w3.org/TR/shacl/).

DECADE-X SHACL models **SHALL** be the source of truth for all conformity constraints applicable to DECADE-X data products.

A maximum of one JSON Schema **SHOULD** be provided for each SHACL model. When provided, the JSON Schema file **SHOULD** use the filename `schema.json`.

DECADE-X JSON Schemas **SHALL NOT** define any conformity rule or constraint that is not explicitly defined in the corresponding SHACL model.

How to create a conformant dataproduct.

Formal rules (which vocabulary to use, how to declare conformity, etc.): JSON-LD and the DX vocabulary (generic data package model).

All models shall be versioned using [Semantic Versioning](https://semver.org), with `owl:versionInfo` and the corresponding `owl:versionIRI`.

---
sidebar_position: 4
title: 4.4 Legal & Regulatory Framework
---

> This section is mixed

All DECADE-X data standard models **SHALL** be published under the [https://creativecommons.org/licenses/by/4.0/deed.en](https://creativecommons.org/licenses/by/4.0/deed.en) licence.

