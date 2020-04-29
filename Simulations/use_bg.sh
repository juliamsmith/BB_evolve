#!/bin/bash
printf "BACKGROUND RUNS STARTED\n"


function max2 {
   while [ `jobs | wc -l` -ge 45 ]
   do
      sleep 5
   done
}

cd to_run
for f in *.sh; do
    max2; ./$f &
done
wait
echo "All done!!!"
