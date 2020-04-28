#!/bin/bash
printf "BACKGROUND RUNS STARTED\n"
cd to_run
for f in *.sh; do
    ./$f &
done
