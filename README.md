Weather Data Engineering Pipeline

An end-to-end data engineering project that extracts weather data from an external API, stores it in PostgreSQL, orchestrates pipeline tasks with Apache Airflow, transforms data using dbt, and enables visualization through Apache Superset.

Project Overview

This project demonstrates a containerized data pipeline designed to collect, store, transform, and visualize weather data. It integrates data ingestion, database storage, workflow orchestration, data transformation, and visualization within a single environment.

Architecture

Data Flow:

Weatherstack API → Python Data Ingestion → PostgreSQL → Apache Airflow → dbt Transformations → Apache Superset

Note: This represents the intended logical workflow. The exact execution dependencies should match the implementation in the repository.

Tech Stack

Technology            | Purpose
Python                | Extracts weather data from the external API
Weatherstack API      | Provides weather information
PostgreSQL            | Stores structured weather data
Apache Airflow        | Orchestrates and schedules pipeline tasks
dbt                   | Transforms data for analytical use
Docker Compose        | Runs and manages project services
Apache Superset       | Supports data exploration and visualization
Ubuntu / WSL          | Development environment

Key Features

- API Integration: Retrieves weather information from the Weatherstack API using Python.
- Structured Data Storage: Uses PostgreSQL to store weather data for downstream processing.
- Workflow Orchestration: Uses Apache Airflow to manage pipeline tasks.
- Data Transformation: Uses dbt to organize and transform data for analytics.
- Data Visualization: Integrates Apache Superset to explore weather trends and conditions.
- Containerized Environment: Uses Docker Compose to manage the project's services.

Project Structure

The repository is organized into components for data ingestion, orchestration, database services, transformation, and visualization.

Key components include:

- "api-request/" — Python API ingestion code.
- "docker/" — Docker-related configuration files.
- "dbt/" — dbt project and transformation configuration.
- "docker-compose.yml" — Service orchestration configuration.

Verify the directory and file names against the current repository before publishing.

Prerequisites

- Docker Desktop with WSL 2 integration, or a compatible Docker Engine and Docker Compose installation.
- Ubuntu / WSL or another supported Linux environment.
- A Weatherstack API key.
- Git.

Setup and Installation

1. Clone the repository

git clone https://github.com/Sooriya07/Weather-Data-Project.git
cd Weather-Data-Project

2. Configure environment variables

Create the required environment configuration files based on the configuration expected by the project.

Add your Weatherstack API key to the appropriate environment file:

WEATHER_API_KEY=your_weatherstack_api_key

Replace the placeholder with your own API key.

Security: Never commit ".env" files, API keys, database passwords, or other credentials to GitHub.

3. Start the services

From the project directory, run:

docker compose up -d

Check the service status:

docker compose ps

Review service logs if needed:

docker compose logs

4. Access the applications

Use the host ports configured in your "docker-compose.yml" to access the relevant web interfaces, including Apache Airflow and Apache Superset.

5. Run and verify the pipeline

Follow the project's configured workflow to execute the Python ingestion process, verify the data in PostgreSQL, run the applicable dbt transformations, and inspect the resulting data in Superset.

The exact commands and execution order depend on the repository configuration.

Security Considerations

- Keep API keys and credentials outside version control.
- Use environment variables for sensitive configuration.
- Avoid publishing database credentials in documentation, screenshots, or source files.

Learning Outcomes

This project provided practical experience with:

- Extracting data from an external API using Python.
- Working with PostgreSQL for structured data storage.
- Managing containerized services with Docker Compose.
- Orchestrating data workflows with Apache Airflow.
- Transforming data using dbt.
- Exploring and visualizing data with Apache Superset.

Future Improvements

- Implement stronger error handling and retry logic for API failures.
- Add data quality checks and validation tests.
- Improve logging and monitoring of pipeline execution.
- Extend the pipeline to support additional weather data sources.
- Enhance dashboard visualizations and analytical insights.

Author

Sooriyaprasath R

GitHub: "Sooriya07" (https://github.com/Sooriya07)
