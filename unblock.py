#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jeremy Low
# License: MIT
try:
  import turtle
  import twitter
  import json
  import sys
  from time import sleep
except ImportError as whoops:
  print("Sorry, one of the required packages did not import properly. try running pip install with the package name", str(whoops))
  sleep(8) # display error message so they can gather the needed info, can add in logging, and log it to a file.
  sys.exit(1) # because of error with importing, set exit status as 1 because of an error.

screen = turtle.Screen() # setting up screen ratio's
screen.setup(1000,1000)
screen.background('White') # can be changed to a background picture with screen.bgpic('')

disclaimer = ('Please be aware, none of this information will be shared with anyone, '
              'this is to help you unblock your access to twitter.'
              'AND WILL ONLY BE USED FOR THAT PURPOSE.'
              'this message will display for 15 seconds.') # for the non tech savy.
turtle.write(disclaimer, False, align='center', font=('Arial', 12, 'bold')) # disclaimer text, alignement, and text def.
sleep(15) # display the message for 15 seconds.

# the reason for string, is because turtle's primary input's is for float, which makes API keys difficult to handle, because of the
# following .0
CONSUMER_KEY = turtle.numinput("CONSUMER KEY", "Enter or copy your Consumer key please!","0000")
CONSUMER_SECRET = turtle.numinput("CONSUMER SECRET", "Enter your consumer secret key please!","0000000")
ACCESS_KEY = turtle.numinput("ACCESS KEY","Enter your access key please!","0000")
ACCESS_SECRET = turtle.numinput("ACCESS SECRET","Please enter your Access Secret Key please!","0000")

# inside this call, im not exactly sure if they can be passed as a string, or as an int, so i figured for ease of use, set as string.
# and if it fails handle as neccessary.
api = twitter.Api(str(CONSUMER_KEY),
                  str(CONSUMER_SECRET),
                  str(ACCESS_KEY),
                  str(ACCESS_SECRET),
                  tweet_mode='extended',
                  sleep_on_rate_limit=True)


def get_blocks(filename):
    with open(filename, 'w+') as f:
        blocks = api.GetBlocksIDs()
        f.write(json.dumps(blocks))
    return True


def unblock(blocklist):
    with open(blocklist, 'r') as f:
        blocks = json.loads(f.read())
    while blocks:
        block = str(blocks.pop())
        try:
            result = api.DestroyBlock(user_id=block)
            if result:
                with open('successfully_unblocked.txt', 'a+') as unblocked_list:
                    unblocked_list.write(block + '\n')
        except Exception as e:
            with open('errors.txt', 'a+') as error_log:
                error_log.write(repr(e) + '\n')
            with open('faied_to_unblock.txt', 'a+') as fail_list:
                fail_list.write(block + '\n')
            continue
        with open(blocklist, 'w+') as f:
            f.write(json.dumps(blocks))


if __name__ == '__main__':
    if get_blocks('blocklist.json'):
        unblock('blocklist.json')
