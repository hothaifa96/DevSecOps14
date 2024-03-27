#!/bin/bash

echo "whats your fav pizza toppings "
echo ""
echo "1 - Tuna"
echo "2 - Corn"
echo "3 - olive"
echo "4 - pineapple"

echo "enter the number : "
read x

case $x in
    1)
    echo "Tuna is a good choice, mama maglione pizza on the way"
    ;;
    2) echo "Corn is a Classic choice , mama maglione pizza on the way";;
    3) echo "Olive is a fantastic choice , mama maglione pizza on the way";;
    4) echo "vafancolo ";;
    *)  echo "Invalid Entry"
esac


# echo "you choose $x nice topping you italian friend"

# if [ $x -eq 1 ];then
#     echo "Tuna is a good choice, mama maglione pizza on the way"
# fi

# if [ $x -eq 2 ]; then
#     echo "Corn is a Classic choice , mama maglione pizza on the way"
# fi

# if [ $x -eq 3 ]; then
#     echo "Olive is a fantastic choice , mama maglione pizza on the way"
# fi

# if [ $x -eq 4 ]; then
#     echo "vafancolo "
# fi