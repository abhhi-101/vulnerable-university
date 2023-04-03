## How to access Vulnerable DJango application

## Installation
1. Clone GitHub repository

``git clone https://github.com/abhhi-101/vulnerable_university.git``

2. Move in the application

``cd vulnerable_university/vunlnerableuni``

3. Run the server 

``python manage.py runserver``

4. Access the application by visitin - http://127.0.0.1:8000

### Thanks

## Vulnerabilities
Done 1. Login bruteforce 
Done 2. Insecure Password policy - removing AUTH_PASSWORD_VALIDATORS from setting.py file
    - no password security policy
Done 3. Reflected XSS - Search functionality
Done 4. Debug message to unauthenticated user - by visiting non-exsisting page
Done 5. CSRF - removing 'django.middleware.csrf.CsrfViewMiddleware', from setting.py file
    - add a feedback page for POC - make it authenticated only
6. Clickjacking - removing 'django.middleware.clickjacking.XFrameOptionsMiddleware', from setting.py file
    POC http://web.clickjacker.io/test?url=127.0.0.1:8000
7. Insecure access control - visit authenticate pages without authentication
8. 