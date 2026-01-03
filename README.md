# AWS Lambda ETL Pipeline

## Purpose

This project demonstrates a simple, testable ETL pipeline implemented using an
AWS Lambda–style execution model. It showcases cloud-native data processing,
transformation logic, and automated validation in a serverless context.

## Architecture Overview

The pipeline follows a lightweight serverless ETL flow:

-   An event or API trigger invokes a Lambda-style handler
-   Incoming data is validated and processed
-   SQL-style transformation logic is applied
-   Results are persisted to a lightweight database
-   Automated tests validate transformation correctness

## Tech Stack

-   Python
-   AWS Lambda (execution model)
-   SQL (SQLite; DuckDB optional)
-   Pytest

## Key Concepts Demonstrated

-   Serverless execution model
-   ETL pipeline design
-   Deterministic data transformations
-   Automated data validation
-   Cloud-first testing mindset

## How to Run Locally

````bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python scripts/run_local.py


---

### 7)

```md
## Status

Initial working version with core ETL functionality in place.
Further enhancements are planned to expand realism and robustness.

````

## Roadmap

-   [ ] Add structured input/output schemas
-   [ ] Expand transformation scenarios and edge cases
-   [ ] Improve test coverage
-   [ ] Add optional cloud integration tests (API Gateway / Lambda endpoint)
