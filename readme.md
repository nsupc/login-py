# Login-py
A very basic login script for maintaining nations on [NationStates](https://www.nationstates.net)
## Features
- Easy to use
- Keeps nations alive
- Doesn't get you API banned*
## Instructions
1. Install Python3 on your system and download the script
2. Modify the nations.txt file the same folder as the application, and add your nations and their passwords to the file in the following format:
    ```
       Nation 1,Password 1
       nation_2,Password 2
       etc
       etc
    ```
3. Run the file from the terminal or with batch/shell/cron/etc. Your user-agent (-u or --user) is a required argument, and the script will not run without it. You can optionally pass a ratelimit argument between 1 and 45 as well, the default is 30. 
4. That's it. Don't close the window until the script is done. 


\*This script will not exceed the NationStates rate limit on its own, but use caution when running multiple scripts concurrently. You can lower this script's rate limit via the -r/--ratelimit flag. 
