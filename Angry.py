def angry(num, op):
    if(num==-1):
        return ["I understand, people and circumstances can be frustrating sometimes.So how angry are you?"], 0, ['I can break a brick', 'I have it under control']   
    if(num==0):
        if(op == "I can break a brick"):
            return ["What happened? Maybe you can tell what or who has made you this angry?"], 1, []
        if(op == "I have it under control"):
            return ["Good to know that. Maybe a change of environment can help. Try staying away from what/who made you angry for some time. To take your mind off, you can attempt this quiz: <br> <a href='https://www.gracepointwellness.org/116-anger-management/article/3396-anger-quiz'>Take this quiz now</a> <br> I'm sure this'll help. Feel free to come back and chat if have any other trouble. Bye for now!"], -1, []
    if(num==1):
        return ["Well, that can definitely be a trigger. But often than not, you realize that a situation is only as powerful as you perceive it. The moment you change your perspective, things might not seem so bad. Try this", "Do you have access to actual ice ? It can be ice cubes , ice packs or some snowPut the ice in your handNow when you are ready place the ice on your forehead and eyelids and hold it for about 20-30 seconds.Notice the striking cooling sensation of ice!!Bring your attention gently to your breath and keep breathing at your regular pace while holding the ice.Over time you may notice that you feel cooler and that your heart rate has slowedI sometimes place it on my neck and wrists to help me stay cool. You can ever splash water on your face."], -1, []
