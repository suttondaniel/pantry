
### Heroku apps need the following things: 

1. A requirements.txt file: 
    
    ``` 
    pip freeze > requirements.txt 
    ```
2. A Procfile to tell Heroku what to run:
    
    ```
    echo "web: gunicorn app:app" > Procfile
    ```

3. A github repo from which to work: 
    ``` 
    git remote add origin https://github.com/suttondaniel/pantry.git
     ```

From here, you can create the app via your Heroku account, and then issue the following commands: 

```
heroku git:remote -a pantry5024
git add .
git commit -am "V1 deployment in 3...2..1.."
git push heroku master
```

Then, you'll want to add the database to your project: 
``` 
heroku addons:create heroku-postgresql:hobby-dev 
```

And if you want to play around with the db at any time, you can do so via psql
```
heroku pg:psql
```

***NOTES***
 - You can monitor the app logs from your Heroku account in order to debug.  so far, it seems like 9 times out of 10 there is an issue in the code, not some issue with the "Internal Server" or whatever
 - psql commands can be found here: 
   - https://www.postgresqltutorial.com/psql-commands/
 - The tutorial that finally got something up onto the internet for me: 
   - https://dev.to/paultopia/the-easiest-possible-way-to-throw-a-webapp-online-flask--heroku--postgres-185o
 - 
