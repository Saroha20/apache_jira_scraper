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



## Large Dataset Files

The following large JSON files are hosted externally due to GitHub’s 100 MB file limit:

 File  Download Link 
| `data/hadoop_llm.json` | [Google Drive Link](https://drive.google.com/file/d/1cUk_vADVQPyXMhepaoH_lYO6EmB_8e-X/view?usp=sharing) |
| `data/kafka_issues.json` | [Google Drive Link](https://drive.google.com/file/d/1kBqnxdgQNBZI119YT67mfTdOvyLJ_dIT/view?usp=sharing) |
| `data/hadoop_issues.json` | [Google Drive Link](https://drive.google.com/file/d/1TD_b3-Aew2UV4ir06sTiXkmUQaq7Bxh6/view?usp=sharing) |
| `data/spark_issues.json` | [Google Drive Link](https://drive.google.com/file/d/1gzTH1KYtFoPLaFkDbCitg1NCgRqPpKyh/view?usp=sharing) |

To run the project, download these files and place them in the `data/` folder.

