#!/bin/sh
DELIM=" | "

while true; do
    bl=$(acpi | awk -F, '{print $2}')

    datetime=$(date '+%b %d (%a) %I:%M%p')

    xsetroot -name "[BL: $bl$DELIM$datetime]"

    sleep 20
    
    xsetroot -name "ToTa TatO!"
    
    sleep 10

done

