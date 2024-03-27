#!/bin/bash

# for n in $@ ;  ## iterate over all the user arg's
# do
#     echo "making dir with this name $n"
#     mkdir "$n"
# done


for f in  *;
do
    tar -czvf "$f.gz.tar" $f
done