import argparse
from data_generator import generate_data_csv
from schema import set_end_id_range, set_start_id_range



def data_checker():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--total-rows', required=True, help='total number of rows need to generate', type=int)
    parser.add_argument('--schema', required=True, help='schema name to generate')
    parser.add_argument('--sample-rows', required=False, help='number of rows need to generate for the dataset', type=int)
    parser.add_argument('--output', required=False, help='output folder')
    parser.add_argument('--start-id', required=False, help='', default=1, type=int)
    parser.add_argument('--end-id', required=False, help='', default=1000000000, type=int)
    parser.add_argument('--max-id', required=False, help='', default=1000000000, type=int)
    args = parser.parse_args()

    try:
        set_start_id_range(args.start_id)
        set_end_id_range(args.end_id)
        file = generate_data_csv(args.schema, args.total_rows, args.sample_rows, args.output, args.max_id)
    except Exception as e:
        print(e)
        print("There seem to be some problem with data generation. Please check the input and try again.")
