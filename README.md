# OSDU Schema Creation Project

This project is designed to assist in creating and managing OSDU schemas, providing tools and utilities to streamline schema generation and data processing. It includes configurable options, sample input data, and a structured workflow for generating schemas.


## Features

- **OSDU Schema Generation**: Streamlined process to create and validate schemas.
- **Configuration Management**: Easily adaptable through a configuration file or directory.
- **Sample Data**: Includes a sample CSV file (`well.csv`) for testing or reference.
- **Output Management**: Generated schemas and outputs are stored in the `output` directory.
- **Modular Utilities**: Reusable utilities available in the `utils` directory.

## Requirements

Ensure you have Python 3.x installed. Install the necessary dependencies by running:

```bash
	pip install -r requirements.txt
```
```bash
	python app.py
```


## Configuration

The project is highly configurable through the `config` directory. Key configuration files include:

### `config.json`

- **`csv_file`**: Name of the input data file (default: `well.csv`).
- **OSDU Platform Settings**:
  - `base_url`: Base URL for OSDU API interactions.
  - `headers`: Authentication and content-related HTTP headers.
- **Schema Metadata**:
  - `title`, `description`, `created_by`, `scope`, `status`, `authority`, `source`, `entityType`.
- **Versioning**:
  - `schemaVersionMajor`, `schemaVersionMinor`, `schemaVersionPatch`.

### Workflow
- Input Data Preparation:
	- The input CSV file (well.csv) contains structured data required for schema generation.
	- You can customize this file to fit your specific data format.
- Configuration Setup:
	- Update config.json to define schema metadata such as title, description, entity type, and versioning details.
	- Adjust properties.json to specify schema attributes like ID patterns, legal tags, ACLs, etc.
- Execution:
  	- Run the main script (app.py) to process the input data, apply configurations, and generate the required schema.
	- The application interacts with OSDU APIs if configured, or it can run independently in a local environment.
- Output:
	- The output schemas and related artifacts are saved in the output directory for further use or validation.
