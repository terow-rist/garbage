#!/bin/bash

output='hardware_info.txt'
> $output

echo '-------------- CPU INFO ------------------' >> $output
lscpu >> $output
echo '' >> $output

echo '-------------- memory(RAM) INFO ------------------' >> $output
free -m >> $output 
echo '' >> $output


echo '-------------- Disk space usage INFO ------------------' >> $output
df -h >> $output
echo '' >> $output

echo '-------------- summary of hardware components INFO ------------------' >> $output
sudo lshw -short >> $output
echo '' >> $output

echo '-------------- PCI devices INFO ------------------' >> $output
lspci >> $output
echo '' >> $output
