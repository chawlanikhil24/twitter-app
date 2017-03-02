The app uses Twitter API to fetch tweets from Twitter. The tweets can be filtered on the basis of #HASHTAG and RE-TWEET counts.

**HOW TO USE THIS APP:**

The very first thing you be requiring is Twitter Access tokens and secrets.
Go to this [link](https://apps.twitter.com/) and create your app.

When your app is created,then: 

 - Click on "Keys and Access Tokens"
 - Create your OAuth tokens and secrets

Copy:

 1. Consumer Key (API Key)
 2. Consumer Secret (API Secret)
 3. Access Token
 4. Access Token Secret
 
in **"config.sample.ini"** to the corresponding Keys and **rename the "config.sample.ini"  to  "config.ini"** .

Before running this app you must ensure that you have 
python2.7.x ,
python-dev ,
python-virtualenv , installed on your system. 

If not, then follow these steps: (for Ubuntu 14.04 and above) 

    sudo apt-get install python-dev python-virtualenv


Steps to run the app:

 1. git clone https://github.com/chawlanikhil24/twitter-app
 2. cd twitter-app
 3. virtualenv venv
 4. source venv/bin/activate
 5. pip install -r req.txt
 6. python twi.py "hashtag" "retweet-count" 

EXAMPLE: 

    python twi.py custserv 1 


