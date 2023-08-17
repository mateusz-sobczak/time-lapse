#!/usr/bin/bash

mkdir -p ./cameras/archive
cp -r ./cameras/camera_* ./cameras/archive/
rm -rf ./cameras/camera_*

cd ./cameras/archive

tar -czf ./"$(date +%F-%T).tar.gz" ./camera_*

rm -rf ./camera_*
