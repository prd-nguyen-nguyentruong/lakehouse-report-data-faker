import os
import pandas as pd
import numpy as np
from mimesis.schema import Schema
from tqdm import tqdm
from schema import get_schema

def generate_data_sample(schema_name, total_rows):
    """
    Generates data based on the given schema.

    Args:
        schema_name (str): Name of the schema.
        total_rows (int): Total number of rows to generate.

    Returns:
        list: List of dictionaries representing the generated data.
    """
    print("Generating sample data...")
    schema = Schema(schema=get_schema(schema_name), iterations=total_rows)
    sample_data = schema.create()
    print("Finish generating sample data...")
    return sample_data

def generate_data_csv(schema_name, total_rows, batch_size, output_folder, shuffle):
    """
    Generates a CSV file containing data based on the given schema.

    Args:
        schema_name (str): Name of the schema.
        total_rows (int): Total number of rows to generate.
        sample_data (list): Pre-generated sample data.
        batch_size (int): Batch size.
        output_folder (str): Folder to save the output CSV file.
        shuffle (bool): Whether to shuffle the data or not.

    Returns:
        str: Path to the generated CSV file.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    file_name = f"{total_rows}_{schema_name}.csv"
    output_path = os.path.join(output_folder, file_name)

    print("Generating data csv...")
    iterations = total_rows // batch_size
    modulo = total_rows % batch_size
    with tqdm(total=total_rows, desc="Progress", unit="rows") as pbar, open(output_path, 'w', encoding="utf-8") as file:
        for i in range(iterations):
            process_batch(schema_name, batch_size, shuffle, file, f"{'w' if i == 0 else 'a'}", pbar)
        if modulo > 0:
            process_batch(schema_name, modulo, shuffle, file, f"{'w' if total_rows == modulo else 'a'}", pbar)

    print("Complete generating data csv...")

    return output_path

def process_batch(schema_name, batch_size, shuffle, file, mode, pbar):
    """Generating data by batch and write to file. Then upgrade progress bar."""
    batch_data = generate_data_sample(schema_name, total_rows=batch_size)
    df_sample = pd.DataFrame(batch_data)
    if shuffle:
        df_sample = df_sample.apply(np.random.permutation, axis=0)
    df_sample.to_csv(file, sep=",", encoding="utf-8", index=False, header=None, mode=mode)
    pbar.update(batch_size)
