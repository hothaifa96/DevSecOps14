#!/bin/bash

# this file change the permissions for the files with .sh extention

file=$1

if [ ! -x "$file" ];then
    echo "granting permissions"
    sleep 3 
    chmod +x "$file"
    if [ $? != 0 ];then
        echo "we need a file"
        exit 199
    fi
    echo "this file is executable now ! Go Crazy !"
else  
    echo "This file already has execute permission. You can run it directly."
fi
