# Nodejs Vulnerable Application

## System Information

- **Server environment**: Node.js
- **Web Framework**: Express
- **Database**: MongoDB
- **Platform (developed on)**: Ubuntu 20.04

### System Requirements
1. Docker
2. NodeJs

## Run in Docker [commands]
1. Clone the code locally

```bash
git clone https://github.com/abhhi-101/vulnerable-university.git
```
2. Move to the directory

```bash
cd vulnerable-university/vul_nodejs
```

3. Run the application in a docker container:
```bash
docker-compose up -d
```

4. Stop the running container:
```bash
docker-compose down
```

## Features

1. User login
2. User Registration
3. Search Users
4. Download images via URL

## Vulnerabilities

1. Authentication bypass via NoSQL injection in the login form
2. Reflected cross-site scripting (XSS) in the user search form
3. Server-side request forgery (SSRF) in image download feature
4. Account takeover by changing the password of any arbitrary user
5. User information diclosure via direct endpoint

## Steps to Reproduce

1. **NoSQL Injection**
- Go to the login page.
- Enter any valid username and an arbitrary password while intercepting the request in Burp.
- Replace the value of the Content-Type header with the below data to change it to JSON.
```
application/json;charset=UTF-8
```
- Replace the request body with the below JSON data containing the payload.
```
{"username":"admin","password":{"$ne": 1}}
```
- Send the request to get authenticated.
	
2. **Reflected XSS**
- Get authenticated and go to the user search page.
- Enter the below XSS payload in the search bar and submit to execute it.
```
<script>alert(document.domain)</script>
```
		
3. **Server-side request forgery (SSRF)**
- Get authenticated and go to the image download page.
- Enter the given URL in the input field and submit to induce a request on behalf of the server to reset the database.
http://localhost:3000/reset
		
4. **Account takeover via Improper Input Validation**
- Get authenticated and go to the change password page.
- Enter a password in the input field and submit while intercepting the request in Burp.
- Replace the username with target's username in the POST data.
- Send the request to change the password of the target user and login with the new credentials.
	
5. **Information disclosure via direct endpoint**
- Send a POST request to the given endpoint to fetch the data of all the users.
http://localhost:3000/admin/users
