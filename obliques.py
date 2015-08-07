#!/usr/bin/env python

import time
import ConfigParser
from random import random, randint, seed
from twilio.rest import TwilioRestClient

def random_line(file):
	'''Selects a random line from a file.'''
	# sort of oblique but works without reading whole files into memory 
	# yoinked from @smammy's fix to my computers-will-never script

        seed()
        selected = next(file)
        for n, line in enumerate(file, start=1):
            if random() * n < 1:
                selected = line
        return selected.rstrip()

def send(number, sender, sid, token):
        '''Sends an SMS to a number.'''

        ACCOUNT_SID = sid
        AUTH_TOKEN = token

        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        strategy=random_line(open('obliques.txt','r'))

	# twilio is a tad weird and this actually sends the message instead of just creating the object
        msg = client.messages.create(
            to=number,
            from_=sender, # not a typo, don't remove the _
            body=strategy,
            )

        print msg.sid

if __name__=='__main__':
        time.sleep(randint(36000,72000)) # sleep until somewhere between 10:00 and 20:00
	# remove or modify the line above for your own purposes
	
	config = ConfigParser.RawConfigParser()
	config.read(os.realpath(os.dirname('obliques.conf'))) # testing a fix for possible issue with cron working directory

	recipient = config.get('numbers', 'recipient')
	sender = config.get('numbers', 'sender')
	sid = config.get('auth', 'sid')
	token = config.get('auth', 'token')

	send(recipient, sender, sid, token)
