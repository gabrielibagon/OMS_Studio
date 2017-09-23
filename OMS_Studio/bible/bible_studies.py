import tweepy
import datetime


# -- Import Bible --
bible = []
with open('bible.txt') as f:
	for line in f:
		line = ''.join(line.split(' ')[1:]).strip()
		for ch in list(line.strip().replace(' ','')):
			bible.append(ch)

# -- Setup credentials -- 
credentials = {}
with open('credentials.txt') as inputfile:
    for line in inputfile:
    	if len(line)>1:
	    	key, value = line.strip().split('=')
	    	credentials[key] = value
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
api = tweepy.API(auth)

# -- Main Loop --
idx=0
length = len(bible)
wait = True

While True:
	minute = datetime.datetime.now().minute
	if (minute == 0 or minute == 30):
		if wait:
			wait = False
			num_spaces = idx % 10 + 5
			api.update_status("%s%s" % (bible[idx], ' '*num_spaces + '.'))
			idx+=1
			with open('current_index.txt', 'w') as fp:
				fp.write(str(idx))
	else:
		wait = True
