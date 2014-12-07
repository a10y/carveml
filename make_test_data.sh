#!/bin/bash

for f in $(find corpora-test -type f); do
    python make_data_test.py $f
done
