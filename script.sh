#!/bin/bash
echo $PATH
for n in {1..15}
do
    echo "python3 run_instrumented.py $n $1 $2 >$n.out 2> $n.err &"
done
