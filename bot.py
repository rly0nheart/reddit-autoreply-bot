#!/usr/bin/env python3

import praw
import time
from config.credentials import client_secret, client_id, username, password


class Bot:
	def __init__(self):
		self.reddit = self.authenticate()
		# subreddit to monitor
		self.subreddit = " " 
		# phrase or word that will trigger the bot
		self.phrase = " "
		
	"""
	Creating an authorized reddit instance
	"""
	def authenticate(self):
	 	reddit = praw.Reddit(client_id = client_id,
	 	                  client_secret = client_secret,
	 	                  username = username,
	 	                  password = password,
	 	                  user_agent = user_agent)
	 	                  
	 	return reddit	 	
	 	
	def main(self):
	    print("Connecting to reddit...")
	    while True:
	    	try:
	    		"""
	    		bot goes live on the specified subreddit
	    		"""
	    		subreddit = self.reddit.subreddit(self.subreddit)
	    		"""
	    		check every comment in the subreddit
	    		"""
	    		for comment in subreddit.stream.comments():
	    		  comm = self.reddit.comment(comment.id)
	    		  """
	    		  check the phrase in each comment
	    		  """
	    		  if self.phrase in comment.body:
	    		  	print(f"{comment.author}:\n{comment.body}\n", end="_"*90);time.sleep(2)
	    		  	"""
	    		  	automated reply to comments containing the trigger phrase
	    		  	"""
	    		  	comment.reply("I am an automated bot") # you can write whatever you want your bot to reply 
	    		  	print("\nAutomated reply sent.\n\n")
	    		  	
	    	except KeyboardInterrupt:
	    	    exit()
	    	   
	    	except Exception as e:
	    	    print(f"An erro occured: {e}")
	    	    print("Reconnecting...")
	 	    	
	 	    	
if __name__=="__main__":
	Bot().main()