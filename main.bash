#!/bin/bash

(parallel python ::: ./spam_a_random.py ./who_wins.py) > out; echo done; tail -n2 out
