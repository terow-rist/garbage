#!/bin/bash

OUTPUT_FILE="syslog_report.txt"
> OUTPUT_FILE
# 1. Total number of lines in journalctl logs
TOTAL_LINES=$(journalctl | wc -l)

# 2. Last 10 lines of logs
LAST_10_LINES=$(journalctl -n 10)

# 3. Search for "error" (case-insensitive) and count occurrences
ERROR_COUNT=$(journalctl | grep -i "error" | wc -l)

# 4. Date and time of the first occurrence of "error"
FIRST_ERROR=$(journalctl | grep -i "error" | head -n 1 | awk '{print $1, $2, $3}')

# Create the summary report
echo "----Syslog Summary Report----" > $OUTPUT_FILE

echo "Total number of lines: $TOTAL_LINES" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

echo "---- Last 10 Lines of Logs ----" >> $OUTPUT_FILE
echo "$LAST_10_LINES" >> $OUTPUT_FILE
echo "" >> $OUTPUT_FILE

echo "Total number of 'error' occurrences: $ERROR_COUNT" >> $OUTPUT_FILE
if [ "$ERROR_COUNT" -gt 0 ]; then
  echo "Date and time of first 'error': $FIRST_ERROR" >> $OUTPUT_FILE
else
  echo "No 'error' occurrences found." >> $OUTPUT_FILE
fi

echo "Syslog analysis complete. Report saved to $OUTPUT_FILE."
