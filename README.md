PRAW 4 reddit bot that replies to mentions with a random integer within the limits defined by the comment that calls the bot. 

If the bot is mentioned like this: /u/botname 30 it will reply with a number between 1 and 30. 
  By default that text is: "The winner is: N"
  
If the bot is mentioned like this: /u/botname blah it will reply with the contents of error_reply.
  By default that text is: "Call the bot like this: /u/botname 20"


To set up:
Install python (I used 2.75)
Install PRAW 4 via pip
Create reddit app here: https://www.reddit.com/prefs/apps/
Write down client_id, client_secret
Input client_id, client_secret, username and password within raffle_rng.py 
Modify user_agent line to be unique
Modify error_reply text as necessary
Modify raffle_reply text as necessary

Create a scheduled task to run the raffle_rng.py script as necessary. Be mindful of Reddit's 10 minute throttle for low-karma accounts.
