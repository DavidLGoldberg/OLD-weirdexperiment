#!/bin/bash

for i in {1..20}
do
    (parallel python ::: ./spam_a_random.py ./who_wins.py) > out;
    read spam <<< `head -n1 out`;
    read victor <<< `tail -n1 out`;

    if [ $spam == $victor ]; then
        ((same++))
    else
        ((different++))
    fi
done

echo "Same: $same"
echo "Different: $different"
