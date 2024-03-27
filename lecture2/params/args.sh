#!/bin/bash

echo $0 " > echo $0" $ script file name

echo $1 "This is the first argument."
echo $2 "This is the second argument."
echo $3 "This is the third argument."
echo $4 "This is the 4 argument."
echo $5 "This is the 5 argument."
echo $6 "This is the 6 argument."

echo $# "the number of args were passing"
echo $* "joined all arguments into one string"
echo $? "exit code as string" 
echo $$ "proccess"
echo $! "background proccess id"
echo $@ "array"

args=("$@")
echo "the second arg is ${args[1]}"