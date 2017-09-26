import tweepy
import datetime


# -- Import Bible --
paradise = []
with open('paradise_lost.txt') as f:
	for line in f:
		line = ''.join(line.split(' ')[1:]).strip()
		for ch in list(line.strip().replace(' ','')):
			paradise.append(ch)

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
wait = True

while True:
	minute = datetime.datetime.now().minute
	if (minute == 0 or minute == 30):
		if wait:
			wait = False
			num_spaces = idx % 10 + 5
			try:
				api.update_status("%s%s" % (paradise[idx], ' '*num_spaces + '.'))
				idx+=1
			except:
				pass
			with open('current_index.txt', 'w') as fp:
				fp.write(str(idx))
	else:
		wait = True	