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

def generate_data_csv(schema_name, total_rows, sample_rows, output_folder, shuffle):
    """
    Generates a CSV file containing data based on the given schema.

    Args:
        schema_name (str): Name of the schema.
        total_rows (int): Total number of rows to generate.
        sample_data (list): Pre-generated sample data.
        sample_rows (int): Number of rows in each sample.
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
    sample_data = generate_data_sample(schema_name, total_rows=sample_rows)

    with tqdm(total=total_rows, desc="Progress", unit="rows") as pbar, open(output_path, 'w', encoding="utf-8") as file:
        header_written = False
        sample_data_length = len(sample_data)
        while total_rows > 0:
            current_sample_rows = min(total_rows, sample_rows)
            if current_sample_rows > sample_data_length:
                # If the required sample size exceeds the length of the sample data, duplicate and concatenate the sample data
                iterations = current_sample_rows // sample_data_length
                remainder = current_sample_rows % sample_data_length
                sample_data_chunk = sample_data * iterations + sample_data[:remainder]
            else:
                sample_data_chunk = sample_data[:current_sample_rows]
            df_sample = pd.DataFrame(sample_data_chunk)

            if shuffle:
                df_sample = df_sample.apply(np.random.permutation, axis=0)
            
            if not header_written:
                df_sample.to_csv(file, sep=",", encoding="utf-8", index=False)
                header_written = True
            else:
                df_sample.to_csv(file, sep=",", encoding="utf-8", index=False, header=None, mode="a")
            
            total_rows -= current_sample_rows
            pbar.update(current_sample_rows)

    print("Complete generating data csv...")
    return output_path