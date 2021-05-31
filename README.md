# PB-Forum

This forum was made to help support the Black Lives Matter Movement. 
Here you will find a forum where anyone and everyone can share their experiences with police brutality. 
People can also share important resources they believe supporters should see.

[![IMAGE ALT TEXT](http://img.youtube.com/vi/kwU4P2t0dZs/0.jpg)](http://www.youtube.com/watch?v=kwU4P2t0dZs "Police Brutality Forum")

For more details on this project refer to: https://devpost.com/software/police-brutality-forum  

I made this website with aid from a tutorial by Miguel Grinberg. It is an amazing resource for learning how to use flask! I would highly reccomend it!
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Steps to test PB-Forum:
1. Download the zipfile for this repo from GitHub and unzip it
2. Open up a command line (for windows: click windows button and type cmd)
3. Navigate to the folder within the unzipped folder (windows example: cd Downloads/PB-Forum-Master/PB-Forum-Master)
4. if Windows: set FLASK_APP=microblog.py 
   if MAC: export FLASK_APP=microblog.py
5. Enter the following command within your command line: flask run
6. Open up a browser and go to http://localhost:5000/

Trouble shooting:

  Error: The CSRF tokens do not match.
  Soulution: Make sure you are not blocking cookies on http://localhost:5000/

