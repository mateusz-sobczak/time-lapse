#!/usr/bin/bash

mkdir -p ./archive
cp -r ./camera_* ./archive/
rm -rf ./camera_*

cd archive

tar -czf ./"$(date +%F-%T).tar.gz" ./camera_*
zip -rq ./"$(date +%F-%T).zip" ./camera_*

rm -rf ./camera_*
