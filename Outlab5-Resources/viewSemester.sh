#! /bin/bash
sed -n "1,3p" $1
sed -n "/$2/p" $1| sed -n "/$3/p"|sort -k3