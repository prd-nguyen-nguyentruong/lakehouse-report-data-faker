#!/bin/bash

FILE_1_PATH="/home/nguyenkhoa/workspace/lakehouse_reporting_prototype/fakedata/many_to_many/1000000_ai_message_note.csv"
FILE_1_COL="x_id"
FILE_2_PATH="/home/nguyenkhoa/workspace/lakehouse_reporting_prototype/fakedata/many_to_many/1000000_ai_messages.csv"
FILE_2_COL="id"


python data_checker.py --file-1-path $FILE_1_PATH --file-2-path $FILE_2_PATH \
        --file-1-col $FILE_1_COL \
        --file-2-col $FILE_2_COL