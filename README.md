# Working with CogStack
This repository contains all tools relevant to interacting with an NHS deployment of CogStack.

It contains easy to follow templates and instructions to interact and search CogStack.

__NOTE__ this section is currently in progress. Let me know if there is anything 
else to add.

## Setup

### Step 1: Clone this repository locally.
1) Enter the directory where you would like to store these files.

2) `git clone https://github.com/antsh3k/working_with_cogstack.git`

Further instructions and self-help with git and git clone. Please visit this [link.](https://github.com/git-guides/git-clone)

If you choose to use github desktop rather than the terminal please refer to the [official github desktop guides.](https://docs.github.com/en/desktop)



### Step 2: Creating a virtual environment and required packages (Terminal)
__Windows__
1. `cd path/to/where/you/want/your/environment`
2. Create a new virtual env: `python3 -m venv venv`
3. Load the virtual environment: `.\venv\Scripts\activate`
4. Install relevant packages and libraries: `pip install -r requirements.txt`


__Linux/MAC OS__
1. `cd path/to/where/you/want/your/environment`
2. Create a new virtual env: `python3 -m venv venv`
3. Load the virtual environment: `source venv/bin/activate`
4. Install relevant packages and libraries: `pip install -r requirements.txt`

Optional: If no jupyter instance is installed. In terminal enter
1. In the main folder of this repository. Activate your virtual environment, using the command from your respective OS. (Step 3)
2. Start jupyter notebook: `jupyter notebook`


### Step 3: Enter credentials and Login details
In the main folder of this repository you must populate the [credentials.py](credentials.py) file with your own CogStack hostnames, username and passwords.

If you have any questions or issues obtaining these details please contact your local CogStack administrator.


The credentials.py contents:
```
hosts = []  # This is a list of your cogstack elasticsearch instances.

# These are your login details (either via http_auth or API)
username = ''
password = ''
api_username = ''
api_password = ''
```

## Contents

## [How to search](search)
This directory contains the basics search templates

## [How to create a watcher](watcher)
This directory contains the basics watcher job templates.

## [MedCAT](medcat)
This directory contains the all scripts required to run a MedCAT project. 

