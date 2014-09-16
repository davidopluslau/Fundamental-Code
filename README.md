Fundamental-Code
================
I've got some helpful files here:

Lauiform.sh
---
A script that makes a few changes to your environment:<br>
  -It exposes a file publishing feature for UC Berkeley instructional accounts ONLY.<br>
  -It changes Vim settings and downloads a plugin to change colors, settings, and implement Nerdtree<br>
  -It appends the settings in LauAlieses.txt (described below) to your .bash_profile. If you instead need them in your .bashrc, append the file manually<br>

To run: paste/run the following command on a Unix command line:
`curl https://raw.githubusercontent.com/davidopluslau/Fundamental-Code/master/Lauiform.sh > ./Lauiform.sh && source Lauiform.sh && rm Lauiform.sh`
  
LauAliases.txt
---
Adds some really basic aliases to Unix systems:<br>
  -up: Equivalent to cd ..<br>
  -cl [directory]: equivalent to cd [directory] && ls<br>
  -post [file]: On UC Berkeley instructional accounts ONLY, put [file] in your ~/public_html directory and make it publicly accessible (but not writable) at inst.eecs.berkeley.edu/~cs<your course number>-<your account letters>/<br>
  -grab [course number] [account letters] [file]: On UC Berkeley instructional accounts ONLY, take a file from inst.eecs.berkeley.edu/~cs<course number>-<account letters>/<file> and put it into your ~/grabs directory<br>
