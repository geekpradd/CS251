#! /bin/bash

mkdir -p albums
mkdir -p playlists

for f in songs/*
do
    IFS=$'\n' line=($(<$f))
    mkdir -p "albums/${line[0]}"
    ln -sf ../../$f "albums/${line[0]}/$(basename $f)"
    for i in "${line[@]:2}"
    do
        mkdir -p "playlists/$i"
        ln -sf ../../$f "playlists/$i/$(basename $f)"
    done
done
