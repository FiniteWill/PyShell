import time
import os
import math
import threading
import webbrowser

'''
Help functions and documentation
'''
num_help_pages = 4
help_intro = "PyShell Help:\n"
help_pgs = [help_intro,
            "Help 1/" + str(num_help_pages) + "\n"
            + "help - prints instructions for PyShell.\n"
            + "help (page: int) - prints the indicated help page.\n"
            + "help (command: str) - prints the description of given command.\n"
            + "time - prints current time.\n"
            + "quit - prompts the user to exit the terminal.\n"
            + "wc - (file path: str) - Returns the number of words in a file.\n",
            "Help 2/" + str(num_help_pages) + "\n"
            + "file (file path: str) - Creates a file at the given file path.\n"
            + "dir (dir path: str) - Create a folder at the given directory path.\n"
            + "write (file name: str) (\"data\") - Writes data to the given file. Using quotes around the\n"
            + "data will allow multiple words to be printed on one line. THIS WILL OVERWRITE EXISTING DATA\n"
            + "append (file name: str) (\"data\") - Appends data to the given file.)\n"
            + "cat (file name: str) (data : any) - Concatenates data to the given file and then prints the contents. of the file\n"
            + "history - Prints out the command history for the current session.",
            "Help 3/" + str(num_help_pages)
            + "",
            "Help 4/" + str(num_help_pages)
            + ""]

help_dict = {"help": "Usage: help\nPrints out a standard help introduction page to the PyShell terminal.\n" +
             "Usage: help (page)\nPrints out the help page with the number (page).",
             "quit": "Usage: quit\nPrompts the user if they would like to exit the PyShell terminal.",
             "time": "Usage: time\nPrints the current time.",
             "size": "Usage: size (file path)\nReturns the size of the file found at (file path).",
             "wc": "Usage: wc (file path)\nReturns the number of words in a file found at (file path).",
             "clear": "Usage: clear\nClears the PyShell terminal.",
             "typescript": "Usage: typescript (start/stop)\nStarts or stops the logging of terminal commands into a typescript.",
             "file": "Usage: file (file name)\nCreates a file with the given name.",
             "dir": "Usage: dir (dir name)\nCreates a folder with the given name.",
             "write": "Usage: write (file name) \"(data)\"\nWrites data to the given file. THIS WILL OVERWRITE EXISTING DATA."
             + "Using quotes around a data argument allows multiple words to be printed on one line.",
             "append": "Usage: append (file name) \"(data)\"\nAppends data the the given file.\n"
             + "Using quotes around a data argument allows multiple words to be printed on one line.",
             "cat": "Usage: cat (file name) (data)\nConcatenates data to the given file and then prints the contents of the file.",
             "history" : "Usage: history\nPrints the command history for the current session."
             }


def help(**args: list) -> None:
    fn_args = args.get("args")

    # Check that there are str arguments
    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            # Print description and information on a command if input is a str in help_dict
            if (help_dict.get(fn_args[0]) != None):
                print("-----------------------------------------------------------------------------")
                print(help_dict.get(fn_args[0]))
                print("-----------------------------------------------------------------------------\n")
            # Check if the input is a valid help page number
            else:
                pg_num = None
                try:
                    pg_num = int(fn_args[0])
                    # The given argument is not a valid page number or known command and is invalid (notify user)
                except:
                    pg_num = None

                if pg_num != None:
                    if (pg_num >= 0 and pg_num <= num_help_pages):
                        print(help_pgs[pg_num])
                        # The page number argument is out of range (notify user)
                    else:
                        print(str(pg_num))+" is not a valid help page number. Please select a help page " + \
                            "0"+"-"+str(num_help_pages)
                else:
                    print("help only takes numbers 0-"+str(num_help_pages) +
                          " or the name of a command as an argument.")
    # There are no arguments (print the default help page)
    else:
        print(help_intro)


'''
Utility functions
'''
command_history = []

def history(**args: None) -> None:
    print("======session command history====")
    for command in command_history:
        print(command_history.index(command),": ",command)
    print("=================================")

def clear(**args: None) -> None:
    os.system("cls")


def set_console_color(**args: None) -> None:
    fn_args = args.get("args")

    # color bg fg
    '''
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
    '''
    if (fn_args != None and isinstance(fn_args, list)):
        if (isinstance(fn_args, list)):
            if (len(fn_args) >= 2):
                try:
                    os.system("color "+fn_args[0]+""+fn_args[1])
                except:
                    pass
            elif (len(fn_args) >= 1):
                try:
                    os.system("color "+fn_args[0])
                except:
                    pass
            # No arguments given, return to default console colors
            else:
                os.system("color 07")


def quit(**args: None) -> None:
    user_input = input("Are you sure you want to quit? Y/N. \n")
    if (str(user_input).lower()[0] == "y"):
        print("Exiting PyShell.")
        os._exit(0)


def get_time(**args: any) -> None:
    print(time.ctime())


def word_count(**args: any) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            # look for given file and try to read it
            try:
                file = open(fn_args[0])
                count = 0
                for x in file:
                    count += 1
                    # print(x)
                file.close()
                print(count)
            except:
                print("Unable to open "+str(fn_args))


'''
Prints out contents of document after appending
'''
def concatenate(**args: any) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if (len(fn_args) > 0):
            append_args = [fn_args[0]]
            for i in range(1, len(fn_args)):
                append_args.append(fn_args[i])
            append(args=append_args)
            print("----------------Contents of "+str(fn_args[0])+"------------")
            contents = read_from_file(args=[fn_args[0]])
            print(contents)
            print("----------------End of contents of "+str(fn_args[0])+"------------")


def sizeof_file(**args: any) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            try:
                file_size = os.path.getsize(fn_args[0])
                if (file_size > 1000):
                    print(str(file_size/1000)+" KB")
                elif (file_size > 1000000):
                    print(str(file_size/1000000)+" GB")
                else:
                    print(str(file_size)+" B")
            except:
                try:
                    print(default_path+str(fn_args[0]))
                    file_size = os.path.getsize(default_path+str(fn_args[0]))
                    if (file_size > 1000):
                        print(str(file_size/1000)+" KB")
                    elif (file_size > 1000000):
                        print(str(file_size/1000000)+" GB")
                    else:
                        print(str(file_size)+" B")
                except:
                    print("Unable to open file with path: "+str(fn_args[0]))


'''
File manipulation commands
'''


def create_dir(**args) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            try:
                os.mkdir(fn_args[0])
            except:
                print("Unable to create directory: "+str(fn_args[0]))


def create_file(**args) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            if (isinstance(fn_args[0]), str):
                try:
                    file = open(fn_args[0], "x")
                    print(str(fn_args[0])+" was created successfully.")
                except:
                    print(str(fn_args[0])+" could not be created.")


def read_from_file(**args) -> any:
    fn_args = args.get("args")
    if (fn_args != None and isinstance(fn_args, list)):
        file = None
        # Open file with write argument
        file = open(fn_args[0], "r")
        if file != None:
            file_str = ""
            for x in file:
                file_str+=str(x)
            return file_str
        else:
            return None


def write_to_file(**args) -> None:
    fn_args = args.get("args")
    if (fn_args != None and isinstance(fn_args, list)):
        if (len(fn_args) > 2):
            file = None
            # Open file with write argument
            file = open(fn_args[0], "w")
            if file != None:
                for i in range(1, len(fn_args)):
                    file.write(fn_args[i])
                    file.write(" ")
                file.write("\n")
                file.close()


def append(**args) -> None:
    fn_args = args.get("args")
    if (fn_args != None and isinstance(fn_args, list)):
        if (len(fn_args) > 2):
            file = None
            # Open file with append argument
            file = open(fn_args[0], "a")
            if file != None:
                for i in range(1, len(fn_args)):
                    file.write(fn_args[i])
                    file.write(" ")
                file.write("\n")
                file.close()


def redirect(**args) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
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
Functions and vars related to typescript for logging shell commands
'''
default_typescript_dir = "C:/PyShell-Typescript"
cur_typescript_dir = default_typescript_dir
cur_typescript_file = cur_typescript_dir+"/"+"DefaultTS"+".txt"
typescript_running = False


def typescript(**args: str) -> None:
    global typescript_running
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            if (fn_args[0].lower() == "on"):
                typescript_running = True
            elif (fn_args[0].lower() == "off"):
                typescript_running = False
    else:
        typescript_running = not (typescript_running)
    print("Typescript logging: "+str(typescript_running) +
          " "+str(cur_typescript_file))

# Used by shell when typescript_running is True to write user input to cur_typescript_file


def typescript_log(**args: str) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            # Add all args to end of list with arg using current typescript file (so the file will always be correct)
            append_args = [cur_typescript_file]
            for arg in fn_args:
                append_args.append(arg)
            # Add time stamp at the end of the command log
            append_args.append(str(time.ctime()))
            append(args=append_args)


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
    global cur_path
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            new_path = str(fn_args[0])
            try:
                os.path.exists(new_path)
                cur_path = str(new_path)
            except:
                print("Unable to change current path to "+str(new_path))


global user_vars
user_vars = {}
'''Variables that the user has declared and assigned.'''

'''
Adds or updates variable in user-defined variables
'''


def set_var(**args) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            if (not fn_args[0] in user_vars):
                user_vars.update({fn_args[0]: fn_args[1]})


'''
Removes variable in user-defined variables
'''


def del_var(**args) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            user_vars.__delitem__(fn_args[0])


'''
Prints variable value in user-defined variables
'''


def print_var(**args) -> None:
    fn_args = args.get("args")

    if (fn_args != None and isinstance(fn_args, list)):
        if len(fn_args) > 0:
            for arg in fn_args:
                print(user_vars.get(arg))
    else:
        for var in user_vars:
            print(var)

def browse(**args):
    fn_args = args.get("args")
    url = fn_args[0]
    if(isinstance(url, str)):
        webbrowser.open_new_tab(url)


command_dict = {"append": "append", "help": "help", "time": "get_time",
                "wc": "word_count",  "size": "sizeof_file", "clear": "clear",
                "color": "set_console_color", "ts": "typescript", "typescript": "typescript",
                "quit": "quit", "write": "write_to_file", "file": "file", "dir": "dir", "cat": "concatenate",
                "history": "history", "browse" : "browse"}

'''
Main function for parsing commands
'''
def parse(input_str: str) -> None:
    global typescript_running
    global command_history

    if (isinstance(input_str, str)):
        # Add input to command history 
        command_history.append(input_str)
        # Tokenize input
        tokens = input_str.split()
        fn_args = []
    
        if typescript_running:
            typescript_log(args=tokens)

        # Sends dictionary with 1 item 'args' mapping to the list of arguments provided after the first command in tokens
        # This will be None if input_str does not have any spaces (len of tokens < 2)
        if (len(tokens) > 0 and tokens[0] in command_dict):
            command = command_dict.get(tokens[0])
            if (len(tokens) > 1):
                fn_args = tokens[1:len(tokens)]
                #print("INPUT: "+tokens[0]+"("+tokens[-1]+")")
                globals()[command](args=fn_args)
            else:
                globals()[command]()
        else:
            pass
            # print("whats in the dictionary")
            # for x in command_dict:
            #     print(x)
