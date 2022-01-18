
# userInteract: Runs user interactions and returns info in array.
def userInteract():
    name = input("What's your name? ")
    favNum = input("What's your favorite number? ")
    info = []
    info.append(name)
    info.append(favNum)
    return info

# replyToUser: Takes in array of user inputs and prints out responses with user information.
#               If user's number is 42, adds a special series of messages for them.
def replyToUser(nameNum):
    userName = nameNum[0]
    userNum = nameNum[1]
    if int(userNum) != 42:
        print("Hi there " + userName + "!")
        print("I see that your favorite number is " + userNum + "!")
        print("That's pretty neat, especially because my favorite number is " + str(int(userNum)+3) + "!")
        print("Well, that's all I've got, so I suppose I'll see you later!")
    else:
        print("So " + userName + ", you're a fan of Douglas Adams?")
        print("I guess I'll have to get you a drink at the restaurant at the end of the universe!")
        print("Until we meet again " + userName + ", keep doing what you do!")


if __name__ == '__main__':
    replyToUser(userInteract())


