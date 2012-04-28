from sys import argv

script, filename = argv

with open(filename, 'r') as f:
   for line in f:
         d = eval(line)
         tweet_text = unicode(d['text']).encode('utf8')
         user_details = d['user']
         user_description = unicode(user_details['description']).encode('utf8')
         user_name = unicode(user_details['name']).encode('utf8')
         screen_name = unicode(user_details['screen_name']).encode('utf8')
         print screen_name + ', ' + user_name + ', ' + user_description + ', ' + tweet_text
