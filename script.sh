#!/bin/bash

for n in {1..15};
do
    python run_instrumented.py $n $1 testL >$n.out 2> $n.err &
done