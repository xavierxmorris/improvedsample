#!/bin/bash
# After: Optimized bash script using find's -exec with + terminator
#
# This version passes multiple files to wc at once rather than calling wc
# once for each .txt file found, significantly improving performance.

find . -type f -name "*.txt" -exec wc -l {} +
