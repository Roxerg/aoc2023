#!/bin/bash

for day in $(ls -d -- */) 
do 
    cd $day
    TIMEFORMAT="${day%/}: %R s"
    time python3 "${day%/}.py" &>/dev/null
    cd ../
done
