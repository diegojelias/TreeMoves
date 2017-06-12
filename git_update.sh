#!/bin/bash

message="Add printed output of cloud stats"

echo $message

git add *
git commit -a -m "$message"
git push
