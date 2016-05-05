#!/bin/bash

echo "Hello"
repos="$(find `pwd` -mindepth 1 -maxdepth 1 -type d)"
for r in $repos;
do
  echo $r
  /Users/user/pmd-bin-5.4.1/bin/run.sh cpd --minimum-tokens 150 --files $r --language pp --format xml >> $r/cpd.xml
done
