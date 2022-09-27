# The top of every bash script must start with this
# #!/bin/bash

# To allow a script to execite you must run this in the command line
# chmod +x <script name>
# chmod +x script.sh

# Variables are declared by setting the variable name equal to a value
# greeting="Hello"

# To access the value of a variable use the variable name prepended with a dollar sign
# $<variable name>
# $greeting

# Format for an if conditional
# if [ condition ]
# then
#   <statement to execute>
# else
#   <statement to execute>
# fi

# Bash comparison operators
# Equal: -eq
# Not equal: -ne
# Less than or equal: -le
# Greater than or equal: -ge
# Greater than: -gt
# Is null: -z

# Bash comparison operators for strings
# Equal: ==
# Not equal: !=

# Format of a for loop
# for <counter> in <variable>
# do
#   <statement to execute>
# done

# Format of a while loop
# while [ condition ]
# do
#   <statement to execute>
#   <iterator of the counter>
# done

# Format of an until loop
# until [ condition ]
# do
#   <statement to execute>
#   <iterator of the counter>
# done

# To ask the user for an input and save it to a value
# read <variable>
# read number

# To have a user enter input arguments on a script
# <script name> <argument1> <argument2>
# saycolors red green blue

# To iterate over an indefinite number of input arguments use $@
# for color in "$@"

# To assign a file or set of files to a variable use the path regular expression
# <variable name>=<path>
# files=/some/directory/*

# Assign an alias to a script name
# alias <alias name>='<./script name>'
# alias saycolors='./saycolors.sh'

# Assign an alias to a script name with parameters
# alias <alias name>='<./script name> parameters'
# alias saycolors='./saycolors.sh "green"'