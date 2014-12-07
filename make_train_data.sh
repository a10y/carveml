#!/bin/bash

for f in $(find corpora-train -type f); do
    python make_data_train.py $f
done
