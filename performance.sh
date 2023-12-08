#!/bin/bash

for day in $(ls -d -- */) 
do 
    cd $day
    TIMEFORMAT="${day%/}: time: %E s"
    # uses fishshell implementation of time
    time python3 "${day%/}.py" &>/dev/null
    cd ../
done
