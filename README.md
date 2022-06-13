# AWS EC2 Excercise

This cmd-line application has two features that displays ec2 instance/ingress rules information to the user.

# How to use

* The application can be launched using Windows Powershell/Command Prompt, or Bash (Linux). 
* Clone the repository into your local directory (requires git), or download the zip & extract
* Using your terminal, cd to the application directory

## Requirements

* [Python 3](https://www.python.org/downloads/) installed on your host machine
* git (optional, for cloning this repo)

## Setup Virtual Environment

* Create Virtual Environment:
```bash
python3 -m venv venv
```

* Activate Virtual Environment:
```bash
(Windows Command Prompt) venv\Scripts\activate
```
```bash
(Windows Powershell) venv/Scripts/activate (May need to run: Set-ExecutionPolicy RemoteSigned)
```
```bash
(Linux) source venv/bin/activate
```

* Install requirements into virtual env:
```bash
pip3 install -r requirements.txt
```

## Configure AWS credentials

* On the CLI, configure AWS settings by typing:
```bash
aws configure
```
* Paste in your AWS Access Key, Secret, and Region. Output format can be left as "None"

## Run the Application

```bash
python ec2_main.py
```

## Run Unit Tests
```bash
python -m unittest test_ec2.py
```

