import instaloader
while True:
    try:
        insta = instaloader.Instaloader()
        username = input("Enter instagram username: ")
        insta.download_profile(username, profile_pic_only=True)
        break
    except:
        print("No such user found!")