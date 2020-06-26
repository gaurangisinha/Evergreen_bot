import os
import random
import json
import requests

# Fetch Json
def get_Quote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    response = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return jsonText["quoteText"],jsonText["quoteAuthor"]


## Number of days you want to make commits
print("\nWelcome to Github commit in the past !! XD\n")
n = int(input("Enter number of days u want to go back: "))
maxm = int(input("Enter limit of max commit each day: "))

# Erase contents of the file
file = open("bot.txt","w")
file.close()

for i in range(1,n + 1):
	end = random.randint(0,maxm)
	for j in range(0,end):
		d = str(i) + ' day ago'
		try:
		    quote,author = get_Quote()
		    text = str(j) +" " + quote+" -"+author+"\n"
		except:
		    text = "Sorry!! No quote found -- " + str(j) + "\n"

		## Open a text file and modify it (append mode)
		with open('bot.txt', 'a') as file:
		    file.write(text)

		## Add bot.txt to staging area
		os.system('git add bot.txt')

		## Commit it
		os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')
