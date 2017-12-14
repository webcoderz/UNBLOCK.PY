#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jeremy Low
# License: MIT

import twitter
import json

CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'
ACCESS_KEY = 'xxxx'
ACCESS_SECRET = 'xxxx'

api = twitter.Api(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_KEY,
                  ACCESS_SECRET,
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
