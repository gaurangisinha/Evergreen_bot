---
# Evergreen Bot
It's a Python bot capable of generating a single quote (times the number of days given) and store it in bot.txt ....Everything is done in past :P XD

---

#### Disclaimer : This has been made available for informational and educational purposes only and solely as a self-help tool for your own use.
### Steps to make your github timeline evergreen again: 

1. Make a new repo (public / private). 
2. Clone the repo to your local machine using SSH or HTTPS,for example SSH key using <br>
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
3. Copy the output of cat id_rsa.pub<br>
4. Paste the above copied outpur into your Github profile -> Settings -> SSH and GPG Keys -> Add new SSH key.


5. Download bot.py only and paste it in your cloned repo(which was empty or had readme.md).
6. Run the script .
```
python bot.py
```

---
### The way it works: 
1. Lets assume today's date is 12th June.
2. You enter a number n : 5 (say).
3. Basically then from 12th june it goes back 5 days and each day it starts to commit(puts a random quote in bot.txt).
4. Now you know how to make your timeline evergreen, if you miss to upload one day :P .

---
### So u want proof XD ....??
![](https://github.com/Sayantan-world/Quote_bot/blob/master/Images/commits.png?raw=true)
