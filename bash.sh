#  Print out the contents of the current directory
# ls

# Lists all contents of the present working directory including hiddne files and directories
# ls -a

# Lists all contents of a directory in long format as well as the file permissions
# ls -l

# Lists files and directories by the time the were last modified
# ls -t

# Print out the present working directory
# pwd

# Change directory to a directory inside your pwd
# cd <directory name>
# cd 2015

# Change directories into a directory two levels deep
# cd <direcotry name>/<direcctory name>
# cd jan/memory

# Move one directory up
# cd ..

# Make a directory inside the current directory
# mkdir <directory name>
# mkdir media

# Make a directory two levels deep
# mkdir <directory name>/<directory name>
# mkdir media/tv

# Create an empty file
# touch keyboard.txt

# Output the contents of a command to the console or terminal
# cat <filename>
# cat terminator.txt

# Copy the contents of a source file into a destination file
# cp <source> <destination>
# cp frida.txt lincoln.txt

# Copy a source file into a destination directory
# cp <source> <destination>
# cp biopic/cleopatra.txt historical/

# Copy multiple files into a destination directory
# cp <file1> <file2> <destination directory>
# cp drama/biopic/ray.txt drama/biopic/notorious.txt drama/historical

# Copy all files in the current directory to a destination directory
# cp * <destination directory>
# cp *.txt satire/ 

# Move a file and its contents to a destination directory
# mv <file> <directory>
# mv supername.txt superhero/

# Move mutliple files to a destination directory
# mv <file1> <file2> <directory>
# mv wonderwoman.txt batman.txt superhero/

# Rename a file by moving it into a file with a new name
# mv <file1> <file2>
# mv superhero/batman.txt superhero/spiderman.txt

# Remove a single file
# rm <filename>
# rm waterboy.txt

# Remove a directory and all of its contents recursively
# rm -r <directory name>
# rm -r slapstick/

# Print a message to terminal
# echo <message>
# echo "Hello World"

# Print a message to a file
# echo <message> > <file name>
# echo "Hello World" > hello.txt

# Append a message to a file
# echo <message> >> <file name>
# echo "Hello World" >> hello.txt

# Print the output of a command to a file
# ex: cat deserts.txt > forests.txt

# Send the standard input of the file on the left to the command on the left
# <command> < <file name>
# sort < lakes.txt

# Redirect standard output of a command to another command
# <command> | <command>
# cat volcanoes.txt | wc | cat > islands.txt 

# Sort lines of text alphabetically
# sort <file name>
# sort rivers.txt

# Filter duplicate, adjacent lines of text
# uniq <file name>
# uniq rivers.txt

# Search for a text pattern and output git, adding the -i flag makes it case insensitive
# grep <-i> <pattern> <filename>
# grep -i Mount mountains.txt

# Additional grep flags
# R - Search an entire directory and print out all files and lines within those files that match
# Rl - Search an entire directory and printout only the file names that have a match

# Modify a standard input based on an expression
# In this example, replace all instances of "snow" in the file with "rain"
# sed "s/snow/rain/g" forests.txt

###### Helper Commands ######
# To clear the screen but remain in your current pwd
# clear

# To complete the current directory in the path you are entering (as long as it exists)
# Tab

# To see your previously run command (this can be repeated to go further back in history)
# Up arrow