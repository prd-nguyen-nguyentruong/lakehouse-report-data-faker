#!/bin/bash

TOTAL_ROWS=10000
BATCH_SIZE=1000
START=1
END=1000

SCHEMA="ai_messages"
DESTINATION="./"
RAND="no-random-id" # set this to random-id or no-random-id
SHUFFLE="no-shuffle" # set this to shuffle or no-shuffle

python main.py --total-rows $TOTAL_ROWS --batch-size $BATCH_SIZE \
        --output $DESTINATION \
        --schema $SCHEMA \
        --start $START --end $END \
        --$RAND --$SHUFFLE
