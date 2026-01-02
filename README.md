# AWS Lambda ETL Pipeline

## Purpose

This project demonstrates a simple, testable ETL pipeline built using AWS Lambda.
It is designed to showcase cloud-native data processing, transformation logic,
and automated validation in a serverless environment.

## Architecture Overview

-   Event or API trigger invokes AWS Lambda
-   Lambda processes incoming data
-   Data is transformed using SQL-style logic
-   Results are persisted to a lightweight database
-   Automated tests validate transformations

## Tech Stack

-   Python
-   AWS Lambda
-   SQL (SQLite / DuckDB)
-   Pytest

## Key Concepts Demonstrated

-   Serverless execution model
-   ETL pipeline design
-   Data validation through automated tests
-   Cloud-first testing mindset

## Status

Initial working version. Improvements and optimizations in progress.

## Roadmap

-   [ ] Add structured input/output schemas
-   [ ] Expand transformation logic
-   [ ] Improve test coverage
