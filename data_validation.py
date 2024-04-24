import csv
import hashlib
from tqdm import tqdm
import pandas as pd
import re
import ast
import json

def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def generate_hashes(data, selected_cols):
    hash_set = set()
    for row in tqdm(data):
        concat_value = ''
        sorted_cols = sorted(selected_cols)
        for col in sorted_cols:
            concat_value += row[col.strip()]
        hash_value = hashlib.sha256(concat_value.encode()).hexdigest()
        hash_set.add(hash_value)
    return hash_set

def convert_to_hash(file_path, selected_cols):
    data = read_csv(file_path)
    hash_set = generate_hashes(data, selected_cols)
    return hash_set


def sort_json(json_string):
    my_dict = ast.literal_eval(json_string)
    def sort_keys(d):
        if isinstance(d, dict):
            return {k: sort_keys(v) for k, v in sorted(d.items())}
        else:
            return d
    sorted_dict = sort_keys(my_dict)
    
    return json.dumps(sorted_dict)
    
def sort_array(array_string):
    try:
        words = re.findall(r'\w+', array_string)
        words.sort()
        result_string = ", ".join(words)
        return result_string
    except ValueError:
        return False

def list_not_common(hash1, hash2):
    not_common_hashes = hash1.symmetric_difference(hash2)
    unique_to_hash1 = not_common_hashes.intersection(hash1)
    unique_to_hash2 = not_common_hashes.intersection(hash2)
    return unique_to_hash1, unique_to_hash2

def preprocess_data(file_path, column_conversions):
    updated_data = []

    with open(file_path, 'r', newline='') as infile:
        reader = csv.reader(infile)
        
        header = next(reader)
        updated_header = [column_conversions.get(column, lambda x: x)(column) for column in header]
        updated_data.append(updated_header)
        
        for row in reader:
            updated_row = [column_conversions.get(header[i], lambda x: x)(row[i]) for i in range(len(header))]
            updated_data.append(updated_row)

    with open(file_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(updated_data)

def main():
    header_list = [
    "Candidate Full Name",
    "Candidate ID",
    "Travel Required",
    "Associated Req/Job ID's",
    "Interview ID",
    "Candidate External ID 1",
    "Candidate External ID 2",
    "Candidate External ID 3",
    "Candidate Phone Number",
    "Candidate Email",
    "1st reminder for interviewer to add availability",
    "2nd reminder for interviewer to add availability",
    "3rd reminder for interviewer to add availability",
    "Interview Reminders Preference  (opt-in to SMS/Email)",
    "Interview Communication Source",
    "Advanced Scheduling Action",
    "Interview Scheduled by User Type",
    "Interview Prep Title",
    "External Group ID",
    "Location Calendar Name",
    "Interview Scheduled by EID",
    "Interview Scheduled By Phone",
    "Scheduled By User's Time Zone",
    "Interview Scheduled By User's Job Title",
    "Interview Prep Title",
    "Candidate Current Journey Status",
    "Round Robin Group Name",
    "Conversation Name",
    "Travel Required",
    "Job Application ID",
    "Primary Recruiter (Custom)",
    "Interview Scheduled by Name",
    "Interview Scheduled By Email",
    "Interview Method",
    "Group/ Job Name",
    "Interview Duration (in minutes)",
    "Candidate Associated To - User's Full Name",
    "Candidate Associated To - User's Email",
    "Candidate Associated To - User's Phone Number",
    "Candidate Current Interview Status",
    "Primary Manager (Custom)",
    "Rescheduled",
    "Interview Type",
    "Conversation Type",
    "Candidate Interview Request Currently Pending",
    "Queued Interview Request Sent to Candidate Date (SMS)" # this field is wrong should be omited, follow the doc https://docs.google.com/spreadsheets/d/1jmuspCVLLStL4m5UmGHJr-b6uDHyl8cJRzjMoI0_HFM/edit#gid=0,
    # "Time from interview accepted to selected interview date/time" # date,
    # "Selected Interview Date and Time", # date
    # "Interview Canceled by User", # date
    # "Interview Canceled by Candidate", # date
]

    column_conversions = {"Interview Communication Channels": sort_array}
    preprocess_data("./data/origin.csv", column_conversions)
    preprocess_data("./data/generate.csv", column_conversions)
    hash1 = convert_to_hash('./data/origin.csv', header_list)
    hash2 = convert_to_hash('./data/generate.csv', header_list)
    unique_hash1, unique_hash2 = list_not_common(hash1, hash2)

    print("number of rows in original file compare to new report file: ", len(unique_hash1))
    print("number of rows in new report file compare to original file: ", len(unique_hash2))


if __name__ == "__main__":
    main()