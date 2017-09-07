#!/bin/bash

mv git_newbranch.moves.sh ../

#cd ./TreeMoves


new_branch='Sept7_ggm'
old_branch='Aug8_ggm'

git checkout master
git branch -d $old_branch
git pull
git branch $new_branch
git checkout $new_branch
git push -u origin $new_branch

mv ../git_newbranch.moves.sh .
