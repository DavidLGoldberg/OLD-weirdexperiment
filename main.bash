#!/bin/bash

parallel python ::: ./spam_a_random.py > spam_out ./who_wins.py > victor; echo done
