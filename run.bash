#!/bin/bash

for i in {1..10}
do
    nice ./main.bash >> results;
done
