import time
import os
import math
import threading

num_help_pages = 4
help_intro = "PyShell Help:\n"
help_pgs = [help_intro, 
    "Help 1/" + str(num_help_pages) 
    + "\nhelp - prints instructions for PyShell.\n"
    + "help (page: int) - prints the indicated help page\n."
    + "help (command: str) - prints the description of given command.\n"
    + "time - prints current time.\n"
    ,"Help 2/" + str(num_help_pages)
    ,"Help 3/" + str(num_help_pages)
    ,"Help 4/" + str(num_help_pages)]

command_dict = {"help" : help, "time" : time}

'''
Main function for parsing commands
'''

def parse(input_str : str) -> None:
    if(isinstance(input_str, str)):
        # tokenize input
        tokens = input_str.split()

        if(len(tokens) > 0 and tokens[0] in command_dict):
            if(len(tokens) > 1):
                help(pg_num = tokens[-1])
            else:
                help(pg_num = tokens[-1])
        else:
            print("whats in the dictionary")
            for x in command_dict:
                print(x)
            
def help(pg_num : int, **kwargs) -> None:
    if(isinstance(int(pg_num), int)):
        print(help_pgs[eval(pg_num)])
    else:
        print(help_intro)
        
def quit():
    input = input("Are you sure you want to quit? Y/N. \n")
    if(str(input).lower()[0] == "Y"):
        running = False
            
def get_time():
    print(time.time())
    
'''
File manipulation commands
'''
def create_file(file_name, file_dir):
    pass

def write_to_file(fd, data):
    if os.write(fd, data) != 0:
        print("Failed to write to ", fd)
    else:
        print("Write successful!")
        
'''
Processes
'''
def create_process(pid, delay):
    pass
def suspend_process(pid, duration):
    pass
def kill_process(pid):
    os.kill(pid)

'''
Modes (PyShell context management)
'''
default_mode_name = "default"
modes = [default_mode_name]
cur_mode = modes[0]

def create_mode(mode_name):
    if(not str(mode_name) in modes):
        modes.append(mode_name)
        
def del_mode(mode_name):
    if(str(mode_name) in modes and str(mode_name) != default_mode_name):
        modes.remove(mode_name)
        
def set_mode(mode_name):
    if(str(mode_name) in cur_mode):
        cur_mode = modes[len(modes.index(str(mode_name)))]