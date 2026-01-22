#!/bin/bash
# Before: Inefficient bash script that spawns a new process for each file
#
# This script finds all .txt files and counts lines in each.
# The problem: Using a for loop with $(find ...) spawns a subshell for each file,
# which is inefficient for large directory trees.

for file in $(find . -type f -name "*.txt"); do
    wc -l "$file"
done
