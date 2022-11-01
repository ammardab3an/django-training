1. poetry install
2. poetry shell
3. cd musicplatform
4. python manage.py migrate
5. python manage.py runserver

```
note:
if you got "CSRF Failed: CSRF token missing" response, then:
    if you have the knox token which is giving when POSTing to /auth/login/,
        add the token to the header of your request:
        key: Authentication
        value: token given_knox_token
    if you have csrf-token, 
        add it to the POST form-data body:
        key: csrfmiddlewaretoken
        value: given_csrf_token
    else,
        erase sessionid cookie
```

The problem is produced my the session middleware, if your request contains a session-id then the session middleware will make request.user reference the user which got that session-id, and if the request doesn't contains a knox-token then knox-token-authentication will fail, and django will run the second authentication option which is the session-authentication, which is going fail finding csrfmiddlewaretoken in the POST body and raise "CSRF token missing" exception.