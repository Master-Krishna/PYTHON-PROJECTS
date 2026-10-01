from instabot import Bot

#store the function Bot 
bot = Bot()

#using the login function to login to the account
username = input("Enter your username:- ")
Password = input("Enter your Password:- ")
bot.login(username=username, password=Password)

#using the follow function to follow the user
follow_user = input("Enter the username of the user you want to follow:- ")
bot.follow(follow_user)

#using the upload_photo function to upload the photo with caption
upload_photo = input("Enter the path of the photo you want to upload:- ")
caption = input("Enter the caption for the photo:- ")
bot.upload_photo(upload_photo, caption=caption)