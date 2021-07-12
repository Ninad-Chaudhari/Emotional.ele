def joy():
    print("I'm glad to know that :) Looks like you're content.")
    print("Is there any thing else you would like to share?")
    response = input()
    if(response == "yes"):
        print("What would you like to share?")
        #back to tree
    else:
        print("It was really nice talking to you! Feel free to come back if you're feeling low. I could lend my huge ears :) Bye for now!")

def sad():
    print("I understand. Seems like something's bothering you.  'Could you further describe it, in short?Feel free to share your feelings , think of me as your friend.")
    response = input()
    print("I see. Among the thoughts occuring in your mind,  which one upsets you the most?")
    response = input()
    print("Why do you think it upsets you?")
    response=input()
    print("Okay. You just identified what we call an automatic thought. Everyone has them. They are thoughts that immediately pop to mind without any effort on your part. Most of the time the thought occurs so quickly you don't notice it, but it has an impact on your emotions. It's usually the emotion that you notice, rather than the thought. Often these automatic thoughts are distorted in some way but we usually don't stop to question the validity of the thought.The reason these are called 'false beliefs' is because they are extreme ways of perceiving the world. They are black or white and ignore the shades of grey in  between.")
    activities("sad")

def anxious():
    print("Calm down, and take a deep breath...Could you briefly describe what happened today?")
    response=input()
    print("How are things going on with your friends and family? Is everything alright?")
    response = input()
    if(response == "all fine"):
        print("How are things at work? Is there anything that concerns you?")
        response = input()
        if(response == "yes"):
            print("You should have clear boundaries between your work or academic life and home life so you make sure that you don't mix them. So tell me what's bothering you...")
            response = input()
            print("Lets try some activity to reduce your stress")
            
        if(response == "no"):
            print("That's great! It was really nice talking to you! Feel free to come back if you're feeling anxious. I could lend my huge ears :) Bye for now!")
        
    if(response=="not great"):
        print("We often tend to expect too much of others, their family their friends or even just acquaintances. It's a usual mistake people don't think exactly the way you do Don't let the opinions of others make you forget what you deserve. So tell me what happened")
        response= input()
        print("I understand. But you know, you are not in this world to live up to the expectations of others nor should you feel that others are here to live up to yours. The first step you should take if you want to learn how to stop expecting too much from people is to simply realize and accept the fact that nobody is perfect and that everyone makes mistakes every now and then.")
        activities("anxious")
        
def angry():
    print("I understand, people and circumstances can be frustrating sometimes.So how angry are you?")
    response = input()
    
    if(response=="I can break a brick"):
        print("What happened? Maybe you can tell what or who has made you this angry?")
        
        response = input()
        print("Well, that can definitely be a trigger. But often than not, you realize that a situation is only as powerful as you perceive it. The moment you change your perspective, things might not seem so bad. Try this")
        activities("angry")
    if(response =="I have it under control"):
        print("Good to know that. Maybe a change of environment can help. Try staying away from what/who made you angry for some time. To take your mind off, you can attempt this quiz: https://www.mindtools.com/pages/article/newTCS_88.htm I'm sure this'll help. Feel free to come back and chat if have any other trouble. Bye for now!")
        
    
def activities(emotion):
    activity_conclusion="Now that you have learned about this cool technique to deal with your emotions, you can apply it on most of the problems that you will face. If you still feel stuck at any point, you can always chat with me. Best of luck for your future endeavours. Bye!"
    if(emotion == "sad"):
        print("When I am sad, I listen to these songs (maybe you can try my playlist)")
        print("Did it help?")
        response = input()
        if(response =="yes"):
            print("")
        if(response == "no"):
            print("I see that this thing has really made you low. Well, try going for a walk, get some fresh air. When I am sad, I treat myself with good food, water my plants, try being close to nature. Maybe that will help. But the thing that helps me the most is knowing that someone understands my pain. So, I am here for you whenever you need me.")

    if(emotion == "angry"):
        print("Do you have access to actual ice ? It can be ice cubes , ice packs or some snowPut the ice in your handNow when you are ready place the ice on your forehead and eyelids and hold it for about 20-30 seconds.Notice the striking cooling sensation of ice!!Bring your attention gently to your breath and keep breathing at your regular pace while holding the ice.Over time you may notice that you feel cooler and that your heart rate has slowedI sometimes place it on my neck and wrists to help me stay cool. You can ever splash water on your face.")
    if(emotion == "anxious"):
        print("don't take too much stress. I can list some really cool ways to handle it. You should develop healthy responses which include doing regular exercise and taking good quality sleep. Techniques such as meditation and deep breathing exercises can be really helping in relieving stress. Always take time to recharge so as to avoid the negative effects of chronic stress and burnout. We need time to replenish and return to our pre- stress level of functioning")
    print(activity_conclusion)

def introduction():
    print("Hi, I am emotion-ele! People say that I'm approachable :)And you are?")
    response = input()
    print("Hi ___! How are you feeling today?")
    response = input()
    sad()

introduction()


    