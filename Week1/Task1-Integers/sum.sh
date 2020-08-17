#! /bin/bash

if(($# < 2 || $# > 2))
then 
    echo "Wrong number of arguements, expected 2" >&2
    exit 1
else
    echo "$(($1 + $2))"
fi