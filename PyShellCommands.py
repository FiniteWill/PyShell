import time
import os
import math
import threading

'''
Help functions and documentation
'''
num_help_pages = 4
help_intro = "PyShell Help:\n"
help_pgs = [help_intro,
            "Help 1/" + str(num_help_pages)
            + "\nhelp - prints instructions for PyShell.\n"
            + "help (page: int) - prints the indicated help page\n."
            + "help (command: str) - prints the description of given command.\n"
            + "time - prints current time.\n", "Help 2/" + str(num_help_pages), "Help 3/" + str(num_help_pages), "Help 4/" + str(num_help_pages)]


def help(**args: list) -> None:
    fn_args = args.get("args")
    
    if (fn_args != None and isinstance(fn_args, list)):
        if (isinstance(fn_args, list) and len(fn_args) > 0):
            try:
                pg_num = int(fn_args[0])
            except TypeError:
                pg_num = 0
            except ValueError:
                pg_num = 0
                
            if (pg_num >= 0 and pg_num <= num_help_pages):
                    print(help_pgs[pg_num])
            else:
                # The page number argument is out of range
                print(str(pg_num)+" is not a valid help page number. Please select a help page "+"0"+"-"+str(num_help_pages))
        else:
            # The arguments are invalid
            print("Invalid args: help only takes values 0-"+str(num_help_pages)+" as an argument. Usage: help (page number) without parenthesis")
            print(help_intro)
    else:
        # There are no arguments
        print(help_intro)


'''
Utility functions
'''
def quit(**args: None) -> None:
    input = input("Are you sure you want to quit? Y/N. \n")
    if (str(input).lower()[0] == "Y"):
        running = False


def get_time(**args: any) -> None:
    print(time.ctime())

def word_count(**args: any) -> None:
    fn_args = args.get("args")
    
    if (fn_args != None and isinstance(fn_args, list)):
        if (isinstance(fn_args, list) and len(fn_args) > 0):
            #look for given file and try to read it
            try:
                file = open(fn_args[0])
                count = 0
                for x in file:
                    count+=1
                    #print(x)
                file.close()
                print(count)
            except:
                print("Unable to open "+str(fn_args))
                
def sizeof_file(**args: any) -> None:
    fn_args = args.get("args")
    
    if (fn_args != None and isinstance(fn_args, list)):
        if (isinstance(fn_args, list) and len(fn_args) > 0):
           try:
                file_size = os.path.getsize(fn_args[0])
                if(file_size > 1000):
                    print(str(file_size/1000)+" KB")
                elif(file_size > 1000000):
                    print(str(file_size/1000000)+" GB")
                else:
                    print(str(file_size)+" B")
           except:
               try:
                print(default_path+str(fn_args[0]))
                file_size = os.path.getsize(default_path+str(fn_args[0]))
                if(file_size > 1000):
                    print(str(file_size/1000)+" KB")
                elif(file_size > 1000000):
                    print(str(file_size/1000000)+" GB")
                else:
                    print(str(file_size)+" B")
               except:
                print("Unable to open file with path: "+str(fn_args[0]))

                
'''
File manipulation commands
'''


def create_file(file_name: str, file_dir: str) -> None:
    print("Create file")


def write_to_file(fd, data):
    if os.write(fd, data) != 0:
        print("Failed to write to ", fd)
    else:
        print("Write successful!")


def redirect(**args) -> None:
    fn_args = args.get("args")
    
    if (fn_args != None and isinstance(fn_args, list)):
        if (isinstance(fn_args, list) and len(fn_args) > 0):
            # (process 1) >> (process 2)
            pass

'''
Processes
'''


def create_process(**args):
    pass


def suspend_process(**args):
    pass


def kill_process(**args):
    os.kill(args[0])


'''
Modes (PyShell context management)
'''
default_mode_name = "default"
modes = [default_mode_name]
cur_mode = modes[0]


def create_mode(**args):
    if (not str(args[0]) in modes):
        modes.append(args[0])


def del_mode(**args):
    if (str(args[0]) in modes and str(args[0]) != default_mode_name):
        modes.remove(args[0])


def set_mode(**args):
    if (str(args[0]) in cur_mode):
        cur_mode = modes[len(modes.index(str(args)))]


'''
Paths, vars, and settings
'''
default_path = "C:/"
cur_path = default_path

def set_cur_path(**args) -> None:
    fn_args = args.get("args")
    
    if (fn_args != None and isinstance(fn_args, list)):
        if (isinstance(fn_args, list) and len(fn_args) > 0):
            new_path = str(fn_args[0])
            try:
                os.path.exists(new_path)
                cur_path = str(new_path)
            except:
                print("Unable to change current path to "+new_path)
                
command_dict = {"help": "help", "time": "get_time", "wc" : "word_count",  "size" : "sizeof_file", "quit" : "quit"}

'''
Main function for parsing commands
'''


def parse(input_str: str) -> None:
    if (isinstance(input_str, str)):
        # tokenize input
        tokens = input_str.split()
        fn_args = []

        # Sends dictionary with 1 item 'args' mapping to the list of arguments provided after the first command in tokens
        # This will be None if input_str does not have any spaces (len of tokens < 2)
        if (len(tokens) > 0 and tokens[0] in command_dict):
            command = command_dict.get(tokens[0])
            if (len(tokens) > 1):
                fn_args = tokens[1:len(tokens)]
                print("INPUT: "+tokens[0]+"("+tokens[-1]+")")
                globals()[command](args=fn_args)
            else:
                globals()[command]()
        else:
            pass
            # print("whats in the dictionary")
            # for x in command_dict:
            #     print(x)
