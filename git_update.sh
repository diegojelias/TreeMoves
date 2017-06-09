#!/bin/bash

message="squashing int ants"

echo $message

git add *
git commit -a -m "$message"
git push
