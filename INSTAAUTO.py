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

#using the unfollow function to unfollow the user
username_to_unfollow = input("Enter the username of the user you want to unfollow:- ")
bot.unfollow(username_to_unfollow)

#using the send_message function to send a message to the user
username_to_message = input("Enter the username of the user you want to send a message to:- ")
message = input("Enter the message you want to send:- ")
bot.send_message(message, username_to_message)

