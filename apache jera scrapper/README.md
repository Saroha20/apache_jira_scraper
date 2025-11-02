Apache Jira Web Scraper — LLM Data Preparation Assignment

Overview

This project builds a data scraping and transformation pipeline that extracts public issue data from Apache Jira and converts it into a clean JSONL dataset suitable for training Large Language Models (LLMs).

It focuses on reliability, data quality, and fault tolerance.

Objectives

Scrape issue data (titles, descriptions, comments, metadata) from 3 Apache Jira projects:

Apache Hadoop

Apache Spark

Apache Kafka

Handle pagination, rate limits, and network failures gracefully.

Convert raw issue data into a structured JSONL corpus.

Ensure the system can resume from the last successful batch if interrupted.

Optimization Techniques

Batch saving after every 50 issues to prevent data loss

Backoff strategy for rate-limiting errors

Efficient I/O with streaming writes for large datasets

Modular design — scraper, transformer, and fault-tolerant logic are separate
