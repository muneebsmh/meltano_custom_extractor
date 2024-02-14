# ELT Application with Meltano and SpaceX API

This repository contains a Python-based ELT (Extract, Load, Transform) application built using Meltano and leveraging the SpaceX API. The application extracts data from the SpaceX API, performs transformations using dbt (Data Build Tool), and loads the transformed data into a PostgreSQL database.

## Features

- Custom Extractor Tap: Utilizes a custom extractor tap to pull data from the [SpaceX API](https://github.com/r-spacex/SpaceX-API) into streams.
- Data Loading: Loads the extracted data into PostgreSQL databases.
- Transformations: Applies dbt transformations to the extracted data, enabling powerful and customizable data processing workflows.
- Dockerized Deployment: Provides Docker Compose configurations for simplified deployment and environment setup.

## Prerequisites

- Docker
- Python 3.x
- PostgreSQL

## Getting Started

1. Clone this repository:

    ```git clone https://github.com/your-username/your-repo.git ```

2. Navigate to the project directory:

3. Update the `.env` file with your PostgreSQL database credentials and configurations.

4. Build and run the Docker containers:

5. Access the Meltano UI at `http://localhost:5000` to manage and monitor your ELT pipelines.

## Directory Structure

- `meltano.yml`: Configuration file for Meltano, specifying extractors, loaders, utilities, jobs, and schedules.
- `docker-compose.yml`: Docker Compose configuration for the development environment.
- `.env`: Environment variables file containing database credentials and configurations.
- `custom_extractor/`: Directory containing the custom extractor tap code.
- `transformations/`: Directory containing dbt transformation models.

## Credits

This ELT application was created by Syed Muneeb Hussain and is based on the Meltano framework.
