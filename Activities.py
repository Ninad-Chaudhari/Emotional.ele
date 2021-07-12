def activities(emotion):
    activity_conclusion="Now that you have learned about this cool technique to deal with your emotions, you can apply it on most of the problems that you will face. If you still feel stuck at any point, you can always chat with me. Best of luck for your future endeavours. Bye!"
    if(emotion == "sad"):
        print()
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