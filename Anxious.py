def anxious(num, op):
    if(num==-1):
        return ["Calm down, and take a deep breath...Could you briefly describe what happened today?"], 0, []
    if(num==0):
        return ["I see, How are things going on with your friends and family? Is everything alright?"], 1, ["all fine", "not great"]
    if(num==1):
        if(op == "all fine"):
            return ["I see, How are things at work? Is there anything that concerns you?"], 2, ["yes", "no"]
        if(op == "not great"):
            return ["We often tend to expect too much of others, their family their friends or even just acquaintances. It's a usual mistake people don't think exactly the way you do Don't let the opinions of others make you forget what you deserve. So tell me what happened"], 3, []
    if(num==2):
        if(op == "yes"):
            return ["You should have clear boundaries between your work or academic life and home life so you make sure that you don't mix them. So tell me what's bothering you..."], 4, []   
        if(op == "no"):
                return ["That's great! It was really nice talking to you! Feel free to come back if you're feeling anxious. I could lend my huge ears :) Bye for now!"], -1, []
    if(num==3):
        return ["I understand. But you know, you are not in this world to live up to the expectations of others nor should you feel that others are here to live up to yours. The first step you should take if you want to learn how to stop expecting too much from people is to simply realize and accept the fact that nobody is perfect and that everyone makes mistakes every now and then.", "Don't take too much stress. I can list some really cool ways to handle it. Techniques such as meditation and deep breathing exercises can be really helping in relieving stress. We need time to replenish and return to our pre- stress level of functioning <br> <img src='https://i.pinimg.com/originals/b2/6a/e4/b26ae4728f6dda2de6c9a98f60a908a5.jpg' width='100px' height='100px' > <br> "], -1, []
    if(num==4):
        return ["Lets try some activity to reduce your stress", "Don't take too much stress. I can list some really cool ways to handle it. You should develop healthy responses which include doing regular exercise and taking good quality sleep. Techniques such as meditation and deep breathing exercises can be really helping in relieving stress. Always take time to recharge so as to avoid the negative effects of chronic stress and burnout. We need time to replenish and return to our pre- stress level of functioning <br> <img src='https://i.pinimg.com/originals/b2/6a/e4/b26ae4728f6dda2de6c9a98f60a908a5.jpg' width='100px' height='100px' >  <br> "], -1, []

