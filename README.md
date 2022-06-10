# AWS EC2 Excercise

This cmd-line application has two features that displays ec2 instance information to the user.

# How to use
## Backend Requirements

* [Python 3](https://www.python.org/downloads/) on your host machine
* Clone/download this repo locally, then open the folder with VSCode (or any other IDE of your choice). 
* Alternatively, you can run the application using Powershell (windows) or bash (in the Linux distro of your choice).

## Setup Virtual Environment

* Create virtual env:
```bash
python3 -m venv venv
```

* Activate virtual env:
```bash
venv/Scripts/activate (May need Admin Powershell: Set-ExecutionPolicy RemoteSigned)
```

* Install requirements into virtual env:
```bash
pip install -r requirements.txt
```

## Configure AWS credentials

* On the CLI, configure AWS settings by typing:
```bash
aws configure
```
* Paste in your AWS Access Key, Secret, and Region. Output format can be left as "None".

