#!/bin/bash

TOTAL_ROWS=1000000
SAMPLE_ROWS=1000000
START=1
END=1000000

SCHEMA="ai_messages"
DESTINATION="/home/nguyenkhoa/workspace/lakehouse_reporting_prototype/fakedata/many_to_many"
RAND="random-id" # set this to random-id or no-random-id

python main.py --total-rows $TOTAL_ROWS --sample-rows $SAMPLE_ROWS \
        --output $DESTINATION \
        --schema $SCHEMA \
        --start $START --end $END \
        --$RAND