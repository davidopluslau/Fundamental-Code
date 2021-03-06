#!/bin/bash
here=$PWD
mkdir $HOME/grabs
cd
curl -k https://dl.dropboxusercontent.com/u/59596352/LauAliases.txt >> ~/.bash_profile
mkdir public_html
chmod 755 public_html
chmod 755 ~
if [ ! -d .vim/colors ]; then mkdir -p .vim/colors; fi
curl -k https://dl.dropboxusercontent.com/u/59596352/.vimrc > ~/.vimrc
curl -k https://dl.dropboxusercontent.com/u/59596352/LauIdleX.vim > ~/.vim/colors/LauIdleX.vim
curl -k https://dl.dropboxusercontent.com/u/59596352/nerdtree.zip > ~/.vim/nerdtree.zip
cd ~/.vim
unzip ~/.vim/nerdtree.zip
cd $here
