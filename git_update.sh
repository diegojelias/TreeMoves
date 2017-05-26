#!/bin/bash

message="Typo"

echo $message

git add *
git commit -a -m "$message"
git push
