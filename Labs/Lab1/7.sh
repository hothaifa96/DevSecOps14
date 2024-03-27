#!/bin/bash

x=5

if (( $x % 2 == 0 ));then
    echo "The number $x is even"
else
    echo "The number $x is odd"
fi