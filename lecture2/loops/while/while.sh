#!/bin/bash

# while condition
# do
#  command 
#  command

# done

while [ ! -e test.txt ]
do 
    echo " at $(date) test.txt file doesnt exists"
    sleep 5
done

