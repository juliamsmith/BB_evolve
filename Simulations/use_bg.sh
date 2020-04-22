#!/bin/bash
printf "BACKGROUND RUNS STARTED\n"
cd to_run
for f in *.sh; do
    ./$f &
    printf "."
done
printf "/n"
printf "BACKGROUND RUNS COMPLETE!"