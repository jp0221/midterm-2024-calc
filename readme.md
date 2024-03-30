Calculator Midterm Application
Jimit Patel
APP DEMO: https://vimeo.com/928927285/fbd8aa7548?share=copy

Design Patterns:
I have used Strategy design pattern where I have created multiple methods that can be encapsualted by another method to create this calculator program. For example I have started with creating basic operations file that has the basic add, subtract, multiply, divide functionalities. This file can be execueted on its own or call the methods in another file like I did in the calculator __init__.py file. Similarly I used the calculator file to create four plugins which use the functionalty of the operations file. Another design pattern I have implemented in my app is prototype design pattern. I have a commands file which sets up a blueprint to register plugins as commands. Through this blueprint I am able to simply create plugins for add, divide, subtract, and multiply and my app __init__.py file takes those plugins and uses the Command class to turn them into commands. I have also used the Observer design pattern with CommandHandler class. For example when a user enters a command, the CommandHandler notifies the corresponding command object to execuete the requested operation. 

Enviornment Variables:
I have a .env file for my enviornment variables where I can set the variables such as what enviornment I am working in, or make a connection to a database if I am using one. In my app __init__ file, I have set the default enviornment variable to production for users that clone this repository to use the app and they don't have a .env file. With addign enviornment variables, it is easier for this application to be more portable through different enviorments without modifying any of the codebase.

Logging:
I currently use logging to display how the repl interface handles everything. For example, when a user starts the app, the logs display all the commands that are registered for the app, and once the user types in a command for a calculation, the logging displays the calculation that was completed. Logs are also used to show that the user has exited the app and the system has shutdown. At some instances, I have used logging as mechanism for error handling, so when I run something through the terminal I get logs for errors or if it ran successfully. 

LBYL and EAFP:
In my save.py, I have demonstrated clearly with this bottom part of my code how I used LBYL. I am checking if the filename provided by user is a .csv file before I proceed with save the history on the file. 

filename = input("Please enter a filename to save as (include '.csv'): ")
if not filename.endswith('.csv'):
    print("Error: Filename must end with '.csv'.")
    return

I am also demonstrating "easier to ask for forgiveness than permission" in the same file when I save the calculation history to the sepcified file. If any exceptions occur during the process, then I am catching the exception and printing a appropriate message.

try:
    self.calculation_history.history.to_csv(filename, index=False, header=False)
    print(f"Calculation history saved to {filename}.")
except Exception as e:
    print(f"Failed to save file: {e}")
