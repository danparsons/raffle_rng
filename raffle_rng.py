#!/usr/bin/python
import time
import praw
import re
import random
import datetime

print "STARTING RAFFLE-BOT..."

#authenticate
user_agent='raffle_rng bot 1.0 by diversionmary make this unique'
reddit = praw.Reddit('raffle_rng', user_agent=user_agent, client_id='put client_id here', client_secret='put client_secret here', username='put reddit username here', password='put password here')

#reply if error
error_reply = "Call the bot like this: /u/botname 20"

#parse_to_integer turns strings into integers
def parse_to_integer(string):
    num_slots = 0
    try:
        int(string)
        num_slots = int(string)
    except ValueError:
        pass
    return num_slots


from praw.models import Comment
#get unread mentions
for mention in reddit.inbox.unread(limit=None):
	comment_word_list = mention.body.split(" ")
	if len(comment_word_list) !=2:
		mention.reply(error_reply)
		mention.mark_read()
		break
	total_slots = 0
	for word in comment_word_list:
	# parses any number strings in the comment to integers
		slots = parse_to_integer(word)
		if slots != 0 and total_slots == 0:
			total_slots = slots
		else:
			pass
	# if a slot total was included, randomly determines a winner from the slot range
		if total_slots != 0:
			winner = random.randint(0, total_slots)
			raffle_reply = "The winner is: " + str(winner)
			mention.reply(raffle_reply)
			print(raffle_reply)
			mention.mark_read()
