#!/bin/bash

file=$1 

if [ -e "$file" ];then
    echo "File exists."
    echo > "$file"
fi

for f in *
do
    if [ "./$f" !=  $0 ]; then
    echo "coping  $f to $file..."
    echo "$f\n" >> "$file" 
    cat "$f" >> "$file"
    sleep 3
    fi
done

