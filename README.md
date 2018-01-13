# UNBLOCK.PY
TWITTER UNBLOCK SCRIPT I FOUND THAT UNBLOCKS USERS by JEREMY LOW

requires python 3 and python twitter

instructions to download python 3 are here : https://www.python.org/

open terminal or shell and type: pip3 install python-twitter


ONCE YOU GET EVERYTHING SITUATED TO RUN, LOCATE/ GENERATE NEW API KEYS HERE https://apps.twitter.com/


: Create your Twitter App

a. After you sign in, you’ll be taken to your application creation page. Be sure to fill in your application’s name, a description about your application and your applications URL in the WebSite field. In the Callback URL field, enter your application's URL again. This tells your app to return to this location after authenticating.

b. Read and agree to Twitter’s “Developer Rules Of The Road”. Check the box next to “Yes, I agree”.

c. In the space below, enter the characters you see in the CAPTCHA and click on the “Create your Twitter application” button.

Name: Enter the name of yourapp

Description: Give a description of your app

WebSite: Enter in the website for example, http://yournetworkname.com  (IF YOU DONT KNOW WHAT THIS MEANS JUST PUT ANYTHING)

Callback URL: Enter in the web address of your callback, for example http://yournetworkname.com  (IF YOU DONT KNOW WHAT THIS MEANS YOU CAN LEAVE BLANK)

d. Doing this will take you to your Twitter app’s detail page. Under the OAuth settings, you’ll see that your app’s Access level is set to “Read-only” by default. To enable members to post to Twitter, click on the Settings tab at the top to change the Access level from “Read-only” to “Read and Write”.  Also check the box next to where it reads, “Allow this application to be used to Sign In with Twitter.”

The Application Icon and Organization fields are optional and can be left blank.

Click on the “Update this Twitter application’s settings” button at the bottom.

e. Go back to your Twitter app’s detail page. You’ll need your Consumer key and Consumer secret, found here, to paste into the unblock.py script deleting the X's and entering each required key after the name 

CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'
ACCESS_KEY = 'xxxx'
ACCESS_SECRET = 'xxxx'

~~just remove the X's and place the correspoding code within the quotes.~~~~~~~~~~~~~~~~



ONCE THE KEYS ARE ADDED, RUN THIS INSIDE A FOLDER, A FILE SHOULD BE GENERATED, ONE THAT IS ALL OF THE JSON USER ID OF ALL THE USERS IN YOUR BLOCK LIST, WHEN THE  FILE AUTOMATICALLY RUNS BACK THROUGH THE SCRIPT AND IS FED INTO TWITTER API AND IT PRINTS THE USER ID OF THE SUCCESSFULLY UNBLOCKED USER.







Update 12/16/17


GUI FULLY FUNCTIONAL NOW JUST DOWNLOAD PYTHON 3 ON YOUR MACHINE , THEN IN A TERMINAL OR COMMAND PROMPT PIP INSTALL PYTHON-TWITTER
AND THEN JUST python3 unblock.py in a terminal or window inside the extracted folder.

YOU PUT YOU API KEYS IN THE GRAPHICAL INTERFACE AS IT ASK FOR THEM IN THE SAME ORDER AS BEFORE :)

FOR LARGE BLOCKLIST JUST LET IT RUN IT WILL CLOSE AND END WHEN ITS DONE SUCCESSFULLY :)

