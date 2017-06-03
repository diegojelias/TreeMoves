#!/bin/bash

message="Make sure NNI moves != 0"

echo $message

git add *
git commit -a -m "$message"
git push
