def joy(num, op):
    if(num==-1):
        return ["I'm glad to know that :) Looks like you're content. Is there any thing else you would like to share?"], 0, ["yes", "no"]
    if(num==0):
        if(op == "yes"):
            print("Hello")
            return ["What would you like to share?"], -1, []
        else:
            return ["It was really nice talking to you! Feel free to come back if you're feeling low. I could lend my huge ears :) Bye for now!"], -1, []
