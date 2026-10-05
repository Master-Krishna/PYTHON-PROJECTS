from instabot import Bot

#store the function Bot 
bot = Bot()


class insta:


    def FOLLOW(username):
        try:
            #using the follow function to follow the user
            bot.follow(username)
            
        except Exception as err:
            print(f"An error occurred as {err}")

        else:
            print("Following successfully...")

    def PHOTO(upload_photo,caption = ''):
        try:
            #using the upload_photo function to upload the photo with caption
            bot.upload_photo(upload_photo,caption)
        except Exception as err:
            print(f"An error occurred as {err}")
        else:
            print("Uploading photo in your Account as successful")

    def UNFOLLOW(username):
        try:
            #using the unfollow function to unfollow the user
            bot.unfollow(username)
        except Exception as err:
            print(f"An error occurred as {err}")
        else:
            print("Successfully unfollow")

    def MESSAGE(message,username):
        try:
            #using the send_message function to send a message to the user
            bot.send_message(message,username)
        except Exception as err :
            print(f"An error occurred as {err}")
        else:
            print("Successfully send a message...")


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
    
    instagram = insta()

    try:
        option = int(input("Enter your choice:- "))

        if option == 1:
            username_to_follow = input("Enter the username of the user you want to follow:- ")
            instagram.FOLLOW(username_to_follow)

            
        elif option == 2:
            upload_photo = input("Enter the path of your photo:- ")
            options = int(input("If you want to write a caption press 1 and no press 2:- "))
            if option == 1:
                caption = input("Enter your caption here:- ")
                instagram.PHOTO(upload_photo,caption)
            else:
                instagram.PHOTO(upload_photo)

        elif option == 3:
            username_to_unfollow = input("Enter the username that you want to unfollow:- ")
            instagram.UNFOLLOW(username_to_unfollow)
        elif option == 4:
            username = input("Enter the username that you want to send a message:- ")
            Message = input("Write your message here:- ")
            instagram.MESSAGE()

    except Exception as err:
        print("An error occurred while processing your choice. Please make sure to enter a valid option.")
        print("Invalid option selected. Please try again.")

    else:
        print("Thank you for using the Instagram bot")
