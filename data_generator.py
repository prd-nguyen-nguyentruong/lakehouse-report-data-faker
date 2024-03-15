import pandas
import numpy as np
from mimesis.schema import Schema
from tqdm import tqdm
import os

from schema import get_schema
from tqdm import tqdm

def generate_data_sample(schema_name, sample_data_rows):
    print("Generating sample data...........................")
    test = get_schema(schema_name)
    schema = Schema(schema=test, iterations=sample_data_rows)
    schema.create()
    print("Finish sample data...........................")

    return schema


def generate_data_csv(schema_name, total_rows, sample_rows, output_folder, max_id):
    if not sample_rows:
        sample_rows = total_rows
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    file_name = f"{total_rows}_{schema_name}.csv"

    sample_data = generate_data_sample(schema_name, sample_rows)

    print("Converting to dataframe...........................")
    df_sample = pandas.DataFrame(sample_data)
    header_df = pandas.DataFrame(columns=df_sample.columns)
    print("Finish converting to dataframe...........................")

    print("generate data csv...........................")
    output_path = os.path.join(output_folder, file_name)
    header_df.to_csv(output_path, sep=",", encoding="utf-8", index=False)
    random_id = np.random.randint(1, max_id, size=total_rows)
    for batch_count in tqdm(range(0, total_rows, sample_rows)):
        df_sample.iloc[:,0] = random_id[batch_count:sample_rows + batch_count]
        df_shuffle = df_sample.apply(np.random.permutation, axis=0)
        df_shuffle.to_csv(output_path, sep=",", encoding="utf-8", index=False, mode="a", header=None)
    print("generate data csv...........................")

    return output_path