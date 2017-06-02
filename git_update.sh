#!/bin/bash

message="Adding dendropy3 compatibility"

echo $message

git add *
git commit -a -m "$message"
git push
