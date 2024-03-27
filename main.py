import argparse
from data_generator import generate_data_csv
from schema import set_end_id_range, set_start_id_range, set_id_random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--total-rows', required=True, help='total number of rows need to generate', type=int)
    parser.add_argument('--schema', required=True, help='schema name to generate')
    parser.add_argument('--batch-size', required=False, help='batch size', type=int)
    parser.add_argument('--output', required=False, help='output folder')
    parser.add_argument('--start-id', required=False, help='', default=1, type=int)
    parser.add_argument('--end-id', required=False, help='', default=1000000000, type=int)
    parser.add_argument('--random-id', required=False, help='',action=argparse.BooleanOptionalAction)
    parser.add_argument('--shuffle', required=False, help='',action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    try:
        set_start_id_range(args.start_id)
        set_end_id_range(args.end_id)
        set_id_random(args.random_id)
        file = generate_data_csv(args.schema, args.total_rows, args.batch_size, args.output, args.shuffle)
    except Exception as e:
        print(e)
        print("There seem to be some problem with data generation. Please check the input and try again.")
