# Working with CogStack
This repository contains all tools relevant to interacting with an NHS deployment of CogStack


It contains easy to follow templates and instructions to interact and search CogStack

## Setup
__Windows__

1. Create a new virtual env: `python -m venv venv`
2. Load the virtual environment: `.\venv\Scripts\activate`
3. Install relevant packages and libraries: `pip install -r requirements.txt`


__Linux/MAC OS__
1. Create a new virtual env: `python -m venv venv`
2. Load the virtual environment: `source venv/bin/activate`
3. Install relevant packages and libraries: `pip install -r requirements.txt`

### Login details
In this directory you must create a __credentials.py__ file.

Contents:
```
hosts = []  # This is a list of your cogstack elasticsearch instances.

# These are your login details (either via http_auth or API)
username = ""
password = ""
api_username = ''
api_password = ''
```

## Contents

## [How to search](search)
This directory contains the basics search templates

## [How to create a watcher](watcher)
This directory contains the basics watcher job templates.

__NOTE__ this section is currently in progress. Let me know if there is anything 
else to add.


