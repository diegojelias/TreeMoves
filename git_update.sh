#!/bin/bash

message="Adding another script that just calculates stats for clouds"

echo $message

git add *
git commit -a -m "$message"
git push
