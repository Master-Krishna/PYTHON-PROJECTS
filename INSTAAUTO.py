from instabot import Bot

#store the function Bot 
bot = Bot()

def FOLLOW(username):
    try:
        #using the follow function to follow the user
        bot.follow(username)
        
    except Exception as err:
        print(f"An error occurred as {err}")

    else:
        print("Following successfully...")

def PHOTO(upload_photo,caption):
    try:
        bot.upload_photo(upload_photo,caption)
    except Exception as err:
        print(f"An error occurred as {err}")
    else:
        print("Uploading photo in your Account as successful")


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
            username_to_follow = input("Enter the username of the user you want to follow:- ")
            FOLLOW(username_to_follow)

            
        elif option == 2:
            upload_photo = input("Enter the path of your photo:- ")
            options = int(input("If you want to write a caption press 1 and no press 2:- "))
            if option == 1:
                caption = input("Enter your caption here:- ")
                PHOTO(upload_photo,caption)

        elif option == 3:
            pass
        elif option == 4:
            pass

    except Exception as err:
        print("An error occurred while processing your choice. Please make sure to enter a valid option.")
        print("Invalid option selected. Please try again.")

    else:
        print("Thank you for using the Instagram bot")
