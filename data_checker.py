import pandas as pd
import argparse

def count_occurences(path_file_1, path_file_2, field_file_1, field_file_2):
    df_first = pd.read_csv(path_file_1)
    df_second = pd.read_csv(path_file_2)

    counts_1 = df_first[field_file_1].value_counts(ascending=True)
    counts_2 = df_second[field_file_2].value_counts(ascending=True)

    print(counts_1)
    print(counts_2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-1-path', required=True, help='path to first file')
    parser.add_argument('--file-2-path', required=True, help='path to second file')
    parser.add_argument('--file-1-col', required=True, help='col of first file')
    parser.add_argument('--file-2-col', required=True, help='col of second file')
    args = parser.parse_args()

    try:
        count_occurences(args.file_1_path, args.file_2_path, args.file_1_col, args.file_2_col)
    except Exception as e:
        print(e)
        print("There seem to be some problem with data generation. Please check the input and try again.")