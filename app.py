import json
from utils.utils import is_date, infer_column_type, save_schema_to_file
import pandas as pd
from utils.osdu_client import OSDUClient


def generate_osdu_schema(config_file,properties_file):
    """
    Generates a complete OSDU schema based on the CSV file, with placeholders for non-inferred parts.
    """
    # Load configuration from the provided config file
    with open(config_file, 'r') as file:
        config = json.load(file)

    # Load properties from the provided properties config file
    with open(properties_file, 'r') as file:
        properties = json.load(file)

    # Read the CSV file specified in the configuration
    csv_file = config["csv_file"]
    df = pd.read_csv(csv_file)

    # Initialize definitions dictionary to store column definitions
    definitions = {}

    # Infer schema for each column in the CSV file
    for col in df.columns:
        col_data = df[col]
        col_type = infer_column_type(col_data)

        # Build the definition for each column
        definition_entry = {
            "title": col,
            "type": col_type,
            "description": ""  # Placeholder description
        }

        # Add x-osdu-frame-of-reference for specific types
        if col_type == "number":
            definition_entry["x-osdu-frame-of-reference"] = "UOM:length"
        elif col_type == "string" and all(col_data.astype(str).apply(is_date)):
            definition_entry["x-osdu-frame-of-reference"] = "DateTime"

        # Add definition entry to definitions
        definitions[col] = definition_entry

    # Construct the schema name using the identity components from the configuration
    schema_name = f"{config['authority']}:{config['source']}:{config['entityType']}:{config['schemaVersionMajor']}.{config['schemaVersionMinor']}.{config['schemaVersionPatch']}"

    # Add a reference to the definitions within properties
    properties['data']['allOf'].append({
        "$ref": "#/definitions/" + schema_name
    })

    # Build the final schema structure
    schema = {

        "schemaInfo": {
            "schemaIdentity": {
                "authority": config["authority"],
                "source": config["source"],
                "entityType": config["entityType"],
                "schemaVersionMajor": 1,
                "schemaVersionMinor": 0,
                "schemaVersionPatch": 0,
                "id": schema_name
            },
            "createdBy": config["created_by"],
            "scope": config["scope"],
            "status": config["status"]
        },
        "schema": {
            "x-osdu-license": "Copyright 2024, The Open Group \\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0. Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.",

            "id": schema_name,
            "$schema": "http://json-schema.org/draft-07/schema#",
            "x-osdu-schema-source": config['source'],
            "title": config["title"],
            "description": config["description"],
            "type": "object",
            "definitions": {
                schema_name: {
                    "type": "object",
                    "properties": definitions
                }
            },
            "properties": properties,
            "required": ["kind", "acl", "legal", "data"],
            "additionalProperties": False,
            "x-osdu-review-status": "Accepted",
            "x-osdu-virtual-properties": {},
            "x-osdu-inheriting-from-kind": [],
        }
    }
    # client = OSDUClient(config['osdu'])
    # res = client.create_schema_in_osdu(schema)
    # print(res)
    return schema


# Example usage
config_file = "config\config.json"  # Path to your configuration file
properties_file = "config\properties.json" # Path to your properties file
schema = generate_osdu_schema(config_file,properties_file)
save_schema_to_file(schema, "output\wellbore_schema.json")


