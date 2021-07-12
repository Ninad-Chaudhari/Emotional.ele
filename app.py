#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os
import pandas as pd
import numpy as np
import librosa
import soundfile
import joblib
from pydub import AudioSegment
import pickle

from keras.utils.np_utils import to_categorical
from  keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import classification_report
from tensorflow import keras

import speech_recognition as sr

from Joy import joy
from Sad import sad
from Angry import angry
from Anxious import anxious

app = Flask(__name__)
emotion_state = -1
inpnum = -1

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def extract_feature(file_name, mfcc, chroma, mel):
    sound = AudioSegment.from_file(file_name)
    sound = sound.set_channels(1)
    sound.export(file_name, format="wav")
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result


# MAIN FUNCTION FOR POST
# emotion, inp num

@app.route("/", methods=['POST', 'GET'])
def index():
    global emotion_state
    global inpnum
    y = []
    temp = []
    options = []
    responses = []
    sentence = ""
    r = sr.Recognizer()
    emotions = ['Angry', 'Anxious', 'Happy', 'Sad']

    speech_model = keras.models.load_model('cnn_emotion_model1.h5')
    text_model = keras.models.load_model('model.h5')

    tokenizer = ""
    with open('tokenizer.pickle', 'rb') as handle: 
        tokenizer = pickle.load(handle)

    if request.method == "POST":
        if(inpnum==-1 and emotion_state!=-1):
            emotion_state = -1
            return "Now that you have learned about this cool technique to deal with your emotions, you can apply it on most of the problems that you will face. If you still feel stuck at any point, you can always chat with me. Best of luck for your future endeavours. Bye!"

        if(emotion_state==-1):
            inpnum = -1
            f = request.files['audio_data']
            with open('audio.wav', 'wb') as audio:
                f.save(audio)
                x = []
                feature=extract_feature('audio.wav', mfcc=True, chroma=False, mel=False)
                feature.reshape(-1,1)
                x_arr = []
                x_arr.append(feature)
                x = np.expand_dims(x_arr, axis=2)
                y = speech_model.predict(x)[0]
                print("YYY : ", y)
                # print(y[0])

            with sr.AudioFile('audio.wav') as source:
                try:
                    audio_data = r.record(source)
                    sentence = r.recognize_google(audio_data)
                    #print(text)
                except:
                    text = "Sorry, I was unable to recognize it. Can you repeat?"

            sentence_lst=[]
            sentence_lst.append(sentence)
            sentence_seq=tokenizer.texts_to_sequences(sentence_lst)
            sentence_padded=pad_sequences(sentence_seq,maxlen=80,padding='post')
            temp = text_model.predict(sentence_padded)[0]
            print("TEMP : ", temp)

            final_list = []
            avg1 = max(y[0], temp[1])
            avg2 = max(y[1], max(temp[4],temp[5]))
            avg3 = max(y[2], max(temp[0],temp[2]))
            avg4 = max(y[3], temp[3])
            final_list.extend([avg1, avg2, avg3, avg4])

            prediction = final_list.index(max(final_list))
            emotion_state = prediction
            # print(final_list)

        if(emotion_state!=-1):
            print("emo: ",emotion_state)
            print("inp: ",inpnum)
            op = request.args.get("answer")
            print("OP: ", op)
            if(emotion_state==0):
                # Angry
                responses, inpnum, options = angry(inpnum, op)
                if(inpnum==-1):
                    emotion_state = -1
            elif(emotion_state==1):
                #Anxious
                responses, inpnum, options = anxious(inpnum, op)
                if(inpnum==-1):
                    emotion_state = -1
            elif(emotion_state==2):
                # Happy
                responses, inpnum, options = joy(inpnum, op)
                if(inpnum==-1):
                    emotion_state = -1
            elif(emotion_state==3):
                # Sad
                responses, inpnum, options = sad(inpnum, op)
                if(inpnum==-1):
                    emotion_state = -1


        print("RR : ", responses)
        print("OP: ", options)
        option = '-'.join(options)
        response = '_'.join(responses)
        return response+"#"+option
    else:
        if request.method == "GET":
            greet = "Hi, I am emotion-ele! People say that I'm approachable :) How are you feeling today?"
            return render_template("index.html", greet=greet)


if __name__ == "__main__":
    app.run(debug=True)