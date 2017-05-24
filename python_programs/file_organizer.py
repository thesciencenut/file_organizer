# these are the two libraries I know that we're gonna need -bj
import os
import datetime

# i always like to define a variable to clear the screen when writing command
# line programs. I'm not sure if the command is different for windows though -bj
clear_screen = os.system("clear")
# i like to define a prompt for command line programs as well -bj
prompt = ":>"

# this is the main function in python, it allows you to define functions
# and variables before running anything at all. Only what comes after this
# statement will be run upon execution of the program -bj
if __name__ == "__main__":
    current_directory = os.getcwd()
    clear_screen
    print ("Welcome to  'File organizer'\n")
    # this will print the current working directory -bj
    print ("The current working directory is: %s\n" % current_directory)
    print ("Please enter the absolute path of the target directory to organize"),
    # for now you must enter the absolute path
    # but this will change in the future -bj
    target_directory = raw_input(prompt)

    # so this gets a list of all items in the entered target_directory -bj
    dirs = os.listdir(target_directory)
    # this prints the files and dirs and tells you the different.
    # its a start -bj
    print "Files: "
    for f in dirs:
        if os.path.isdir(target_directory + f):
            print "\t**%s is a directory.\n" % f
        else:
            print f + "\n"
