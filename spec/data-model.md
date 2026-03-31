# Data model summary

The DeDi data model is intentionally small.

## Main entities

- **Namespace:** trust and discovery root
- **Directory:** a collection of records of a defined class
- **Record:** an individual published item
- **Schema:** canonical record shape

## Record classes currently represented in this repository

- public keys,
- revocations,
- memberships,
- Beckn subscribers,
- and references to other registries or records.

## Required implementation properties

Implementations should document:

- which namespace they serve,
- which schemas they expose,
- how records are identified,
- and what lifecycle semantics apply to updates and revocations.
