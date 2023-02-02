import PyShellCommands as ps

running = True

if __name__ == "__main__":
    print("Starting PyShell.")
    print("       ________\n"
          +"      |o       |\n"
          +"    >-|____    |___\n"
          +"    _______|   |   |\n"
          +"   |    _______|   |\n"
          +"   |   |    _______|\n"
          +"   |___|   |_____\n"
          +"       |        o|-<   \n"
          +"       |_________|\n")
    while running:
        command = input("Enter a command or type 'help' for help. \n")
        ps.parse(command)
    