from termcolor import colored
print(colored("Available commands:", 'cyan'))
print(colored("  help, h                : Show this help message", 'green'))
print(colored("  cd <directory>         : Change the current directory", 'green'))
print(colored("  peek <directory>       : List files in the specified directory", 'green'))
print(colored("  branch <directory>     : List files in the specified directory", 'green'))
print(colored("  tree                   : List files in the current directory", 'green'))
print(colored("  task --show <process>  : Show running processes matching the name", 'green'))
print(colored("  admin install <pkg>    : Install a package", 'green'))
print(colored("  admin update           : Update the package installer", 'green'))
print(colored("  admin ubuntu <cmd>     : Run a command with sudo", 'green'))
print(colored("  admin uninstall <pkg>  : Uninstall a package", 'green'))
print(colored("  admin pkgs             : List installed packages", 'green'))
print(colored("  admin pkgs --filter <filter> : List installed packages with a filter", 'green'))
print(colored("  lib.use <command>      : Execute a library command", 'green'))
print(colored("  create --directory <name> : Create a new directory", 'green'))
print(colored("  create --file <name>   : Create a new file and open it in nano", 'green'))
print(colored("  remove --directory <name> : Remove a directory", 'green'))
print(colored("  remove --file <name>   : Remove a file", 'green'))
print(colored("  read <file>            : Read the contents of a file", 'green'))
print(colored("  modify --editfile <file> : Edit a file with nano", 'green'))
print(colored("  modify --copyfile <src> <dest> : Copy a file", 'green'))
print(colored("  modify --movedir <src> <dest> : Move a directory", 'green'))
print(colored("  modify --movefile <src> <dest> : Move a file", 'green'))
print(colored("  python, py             : Start a Python interpreter", 'green'))
print(colored("  bash <script>          : Run a shell script", 'green'))
print(colored("  output <string>        : Print a string to the console", 'green'))
print(colored("  kill --all <process>   : Kill all processes matching the name", 'green'))
print(colored("  kill --specific <pid>  : Kill a specific process by PID", 'green'))
print(colored("  get.cwd                : Get the current working directory", 'green'))
print(colored("  get.rds                : Get disk usage", 'green'))
print(colored("  get.cpu                : Get CPU information", 'green'))
print(colored("  get.ram                : Get RAM usage", 'green'))
print(colored("  get.gpu                : Get GPU usage", 'green'))
print(colored("  get.usr.current        : Get the current user", 'green'))
print(colored("  get.usr.all            : List all users", 'green'))
print(colored("  get.stat               : Show system status", 'green'))
print(colored("  sys.upgrade            : Upgrade the system", 'green'))
print(colored("  sys.perms <args> <file> : Change file permissions", 'green'))
print(colored("  netssh <url>           : Download a file from the specified URL", 'green'))
print(colored("  pinecone --version     : View installed Pinecone version", 'green'))
print(colored("  pinecone --update      : Update Pinecone to the latest version", 'green'))
print(colored("  pinecone install <pkg> : Install a pinecone package", 'green'))
print(colored("  pinecone uninstall <pkg> : Uninstall a pinecone package", 'green'))
print(colored("  pinecone list          : List all pinecone packages", 'green'))
print(colored("  compile python <args> <file.py> : Compile python files", 'green'))
print(colored("  compile cpp <file.cpp> <args> : Compile C++ files", 'green'))
print(colored("  compile c <file.c> <args> : Compile C files", 'green'))
print(colored("  restart                : Restarts Pinecone", 'green'))
print(colored("  exit                   : Exit the program", 'green'))
