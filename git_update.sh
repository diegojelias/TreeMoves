#!/bin/bash

message="Changing file naming schemes"

echo $message

git add *
git commit -a -m "$message"
git push
