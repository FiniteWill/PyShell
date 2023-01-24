import PyShellCommands as ps

running = True

if __name__ == "__main__":
    print("Starting PyShell.")
    while running:
        command = input("Enter a command or type 'help' for help. \n")
        ps.parse(command)
    