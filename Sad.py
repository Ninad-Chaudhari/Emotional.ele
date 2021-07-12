def sad(num, op):
    if(num==-1):
        return ["I understand. Seems like something's bothering you.  'Could you further describe it, in short?Feel free to share your feelings , think of me as your friend."], 0, []
    if(num==0):
        return ["I see. Among the thoughts occuring in your mind,  which one upsets you the most?"], 1, []
    if(num==1):
        return ["Why do you think it upsets you?"], 2, []
    if(num==2):
        return ["Okay. You just identified what we call an automatic thought. Everyone has them. They are thoughts that immediately pop to mind without any effort on your part. Most of the time the thought occurs so quickly you don't notice it, but it has an impact on your emotions. It's usually the emotion that you notice, rather than the thought. Often these automatic thoughts are distorted in some way but we usually don't stop to question the validity of the thought.The reason these are called 'false beliefs' is because they are extreme ways of perceiving the world. They are black or white and ignore the shades of grey in between.", "When I am sad, I listen to these songs. <br> <a href='https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC'>Check this out!</a> <br> Tell me if it helped..."], 3, ["yes", "no"]
    if(num==3):
        if(op =="yes"):
            return ["Awesome! Glad to help. I'm always here if you need me"], -1, []
        if(op == "no"):
            return ["I see that this thing has really made you low. Well, try going for a walk, get some fresh air. When I am sad, I treat myself with good food, water my plants, try being close to nature. Maybe that will help. But the thing that helps me the most is knowing that someone understands my pain. So, I am here for you whenever you need me."], -1, []

