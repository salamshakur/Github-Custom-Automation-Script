# Github Custom Automation Script 

This project was created using Python to help automate the tedious process of creating a local and Github repository.

By running this script, any user can simultaneously create a Github repository, a new local folder for their project containing a README.md, an initial commit, stage, and push online into their newly created repository, as well as, open visual studio code to continue working! Woah!

prerequisites:
1. PyGitHub - Do not worry, this script will download this package for you if it is not currently installed
2. Visual Studio Code - But I mean... who doesn't already have this though, amirite?

To run:
1. Edit the config.json file to include your username, password, and local path to where you want to create your new project
2. run the following code -> `python create.py {name of your project here}`

For Example:
* In Config.json file
    * ```
        "username"  :  "salamshakur",
        "password"  :  "p@$$w0rd",
        "folderPath":  "C:\\Users\\salamshakur\\Desktop\\myProjects"

* In Terminal/Command Prompt
    * `python create.py Hello World`

Thank you and enjoy!