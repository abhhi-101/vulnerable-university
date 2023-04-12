# Vulnerable Application in Django - vul_django
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Intentionally vuln web Application Security in django.
Our roadmap build intentionally vuln web Application in django. The Vulnerability can based on OWASP top ten
<br>

Table of Contents
=================

* [Vul_django](#Vulnerable-Application-in-Django---vul_django)
   * [Installation](#installation)
      * [From Sources](#from-sources)
      * [Docker Container](#from-docker-compose)

## Installation

### From Sources

To setup the project on your local machine:
<br>

First, Clone the repository using GitHub website or git in Terminal
```
  git clone https://github.com/abhhi-101/vulnerable-university.git
 ### Change the directory
  cd vul_django
```
### Method 1
1. Install all app and python requirements using installer file - `python -m pip install -r requirements.txt`
2. Apply the migrations `python3 manage.py migrate`.<br>
3. Finally, run the development server `python3 manage.py runserver`.<br>
4. The project will be available at <http://127.0.0.1:8000> 

### From Docker-Compose 
1. Install [Docker](https://www.docker.com)
2. Run `docker-compose up` or `docker-compose up -d`

### Build Docker Image and Run
1. Clone the repository  &ensp; `git clone https://github.com/abhhi-101/vulnerable-university.git` 
2. Change the Directory `cd vul_django`
2. Build the docker image from Dockerfile using &ensp; `docker build -f Dockerfile -t vul_django .`
3. Run the docker image &ensp;`docker run --rm -p 8000:8000 vul_django:latest`
4. Browse to <http://127.0.0.1:8000> or <http://0.0.0.0:8000> 