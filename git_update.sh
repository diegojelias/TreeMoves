#!/bin/bash

message="input formatted nexus files"

echo $message

git add *
git commit -a -m "$message"
git push
