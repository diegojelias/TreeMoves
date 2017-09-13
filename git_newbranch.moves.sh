#!/bin/bash

mv git_newbranch.moves.sh ../

new_branch='Sept13_ggm'
old_branch='Sept7_ggm'

git checkout master
git branch -d $old_branch
git pull
git branch $new_branch
git checkout $new_branch
git push -u origin $new_branch

mv ../git_newbranch.moves.sh .
