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
n = int(input("Enter number of days u want to make a commit: "))

for i in range(1,n + 1):
    d = str(i) + ' day ago'
    try:
        quote,author = get_Quote()
        text = quote+" -"+author+"\n"
    except:
        text = "Sorry!! No quote found\n" 

    ## Open a text file and modify it (append mode)
    with open('bot.txt', 'a') as file:
        file.write(text)

    ## Add bot.txt to staging area
    os.system('git add bot.txt')

    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')
