Fundamental-Code
================
I've got some helpful files here:

Lauiform.sh
---
A script that makes a few changes to your environment:
  -It exposes a file publishing feature for UC Berkeley instructional accounts ONLY.
  -It changes Vim settings and downloads a plugin to change colors, settings, and implement Nerdtree
  -It appends the settings in LauAlieses.txt (described below) to your .bash_profile. If you instead need them in your .bashrc, append the file manually

To run: paste/run the following command on a Unix command line:
`curl https://raw.github.com/davidopluslau/Fundamental-Code/master/Lauiform.sh > ./Lauiform.sh && source Lauiform.sh && rm Lauiform.sh`
  
LauAliases.txt
---
Adds some really basic aliases to Unix systems:
  -up: Equivalent to cd ..
  -cl [directory]: equivalent to cd [directory] && ls
  -post [file]: On UC Berkeley instructional accounts ONLY, put [file] in your ~/public_html directory and make it publicly accessible (but not writable) at inst.eecs.berkeley.edu/~cs<your course number>-<your account letters>/
  -grab [course number] [account letters] [file]: On UC Berkeley instructional accounts ONLY, take a file from inst.eecs.berkeley.edu/~cs<course number>-<account letters>/<file> and put it into your ~/grabs directory
