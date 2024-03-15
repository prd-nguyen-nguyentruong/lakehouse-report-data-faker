#!/bin/bash

TOTAL_ROWS=10000000
SAMPLE_ROWS=1000000
START=1
END=10000000

ID_MAX=500000

SCHEMA="ai_messages"
OUTPUT_FOLDER_NAME="many_to_many"
DESTINATION="/home/nguyenkhoa/workspace/lakehouse_reporting_prototype/fakedata"

python main.py --total-rows $TOTAL_ROWS --sample-rows $SAMPLE_ROWS \
        --output $DESTINATION/$OUTPUT_FOLDER_NAME \
        --schema $SCHEMA \
        --start $START --end $END \
        --max-id $ID_MAX