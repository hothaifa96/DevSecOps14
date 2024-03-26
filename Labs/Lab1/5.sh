#!/bin/bash

file_path='test.txt'

ls -al

# Check if file exists
if [ -f "$file_path" ];
then
    echo "File $file_path exists ."
    if [ -w "$file_path" ];
    then
        echo "the $file_path is writable ."
    else
        echo "the file isn't writable "
        echo "granting the permissions "
        chmod u+w "$file_path"
        ls -al
        
    fi
fi
