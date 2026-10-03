from instabot import Bot

#store the function Bot 
bot = Bot()

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

openinsta = input("Do you want to open Instagram? (yes/no):- ")

if openinsta.lower() == "yes":
    #using the login function to login to the account
    print("Opening Instagram...")
    print("Please enter your login details to open your Account:")
    username = input("Enter your username:- ")
    Password = input("Enter your Password:- ")
    try:
        bot.login(username=username, password=Password)

    except Exception as err:
        print(f"An error occurred {err}")

    else:
        print("your Account is opened successfully")

    print("You can now use the bot to perform various actions on Instagram.")
    print("Please choose an action from the following options:")
    print("1. Follow a user press 1:- ")
    print("2. Upload a photo press 2:- ")
    print("3. Unfollow a user press 3:- ")
    print("4. Send a message press 4:- ")

    try:
        option = int(input("Enter your choice:- "))

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass

    except Exception as err:
        print("An error occurred while processing your choice. Please make sure to enter a valid option.")
        print("Invalid option selected. Please try again.")

    else:
        print("Thank you for using the Instagram bot")