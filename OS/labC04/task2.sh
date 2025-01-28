#!/usr/bin/bash
read filename
cat $filename

symbols=`wc -m $filename`
bytes=`wc -c $filename`
words=`wc -w $filename`
lines=`wc -l $filename`

echo
echo '--------------------------'
echo 'Number of symbols' $symbols
echo 'Number of bytes' $bytes
echo 'NUmber of words' $words
echo 'Number of lines' $lines
