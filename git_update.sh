#!/bin/bash

message="Adding note that these scripts are currently only compatible with Dendropy 4"

echo $message

git add *
git commit -a -m "$message"
git push
