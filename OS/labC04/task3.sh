#!/usr/bin/bash
read filename

while read p; do
  echo "$p"
done <$filename
