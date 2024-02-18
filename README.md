# Chat app

In this application users can create chat groups that can have different threads where they can post messages.


## Functionalities

As a user I want to:

* Register/create an account.
* Login with my username and password.
* See groups.
* See threads in the group. (Not done yet)
* See messages in the different threads. (Not done yet)

As a user that has logged in I want to:

* Create group.
* Create a thread to the group.
* Add message to the thread. (Not done yet)
* Join groups. (Not done yet)
* Like threads. (Not done yet)
* Like messages. (Not done yet)

## Tables

* Users
* Groups
* Threads
* Messages (Not done yet)
* Likes (Not done yet)

## Get started

This application will only work locally. 

What you need to do to get application running:

1. Clone project to your computer.
1. Open the cloned project with your terminal.
1. Run `python3 -m venv venv` to create Python virtual environment.
1. Activate your venv by running `source venv/bin/activate`
1. Run `pip install -r requirements.txt` to install the dependencies.
1. Start psql server in other terminal.
1. Run `psql < schema.sql`, to get tables that are needed.
1. Run `flask run`
1. Open browser and navigate to your localhost.

## Known improvement ideas

* Validation for username length.
* Validation for input lengths.
    * Empty inputs not allowed.
* Forms that require user to be logged in should not be accessible, if user is not logged in.

## Known bugs


## Links

Important links will be here

## Other

Maybe something else here?