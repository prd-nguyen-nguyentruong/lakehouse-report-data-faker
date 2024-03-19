#!/bin/bash

TOTAL_ROWS=1000
SAMPLE_ROWS=1000
START=1
END=500

SCHEMA="ai_message_note"
DESTINATION="/home/nguyenkhoa/workspace/lakehouse_reporting_prototype/fakedata/many_to_many"
RAND="random-id" # set this to random-id or no-random-id
SHUFFLE="shuffle" # set this to shuffle or no-shuffle

python main.py --total-rows $TOTAL_ROWS --sample-rows $SAMPLE_ROWS \
        --output $DESTINATION \
        --schema $SCHEMA \
        --start $START --end $END \
        --$RAND --$SHUFFLE