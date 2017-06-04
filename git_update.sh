#!/bin/bash

message="Adding folder with example scripts"

echo $message

git add *
git commit -a -m "$message"
git push
