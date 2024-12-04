from dateutil.parser import parse
import numpy as np
import json
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

def infer_column_type(data):
    """
    Infers the JSON schema type based on column data.
    Checks the first 10 rows for type consistency.

    :param data: Pandas Series containing column data
    :return: string, inferred JSON schema type
    """
    data = data.dropna()

    if data.empty:
        return "string"

    if np.issubdtype(data.dtype, np.number):
        return "number"

    if all(data.astype(str).apply(is_date)):
        return "string"

    return "string"

def save_schema_to_file(schema, filename):
    """
    Save the generated schema to a JSON file.

    :param schema: JSON object representing the schema.
    :param filename: Name of the file to save the schema.
    """
    with open(filename, 'w') as file:
        json.dump(schema, file, indent=4)
    print(f"Schema saved to {filename}")