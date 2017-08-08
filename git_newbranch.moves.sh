#!/bin/bash

mv git_newbranch.moves.sh ../

#cd ./TreeMoves


new_branch='Aug1_ggm'
old_branch='July1_ggm'

git checkout master
git branch -d $old_branch
git pull
git branch $new_branch
git checkout $new_branch
git push -u origin $new_branch

mv ../git_newbranch.moves.sh .