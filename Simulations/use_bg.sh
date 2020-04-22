#!/bin/bash
print("BACKGROUND RUNS STARTED")
cd to_run
for f in *.sh; do
    ./$f &
    print(".")
done
print("BACKGROUND RUNS COMPLETE!")