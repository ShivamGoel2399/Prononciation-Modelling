import speech_recognition as sr 
import pyttsx3 
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      
      
# Loop infinitely for user to 
# speak 
flag=True
while(flag):     
    #print("x")
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
            #print("x")
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            print("speak now you have 6 seconds")
              
            #listens for the user's input  
            audio2 = r.listen(source2, phrase_time_limit=6)
            #print("x")
              
            # Using google to recognize audio 
            MyText = r.recognize_google(audio2, language='en-US', show_all=True)
            MyText1 = r.recognize_google(audio2, language='en-US')
            MyText1 = MyText1.lower()
            print(MyText)
            assumed_words=[]
            for i in range(len(MyText['alternative'])):
                assumed_words.append(MyText['alternative'][i]['transcript'])
            print(assumed_words)
  
            print("Did you say ", assumed_words) 
            print("Did you say ", MyText1) 
            #SpeakText(MyText1) 
            
            #--------------------
            """r.adjust_for_ambient_noise(source2, duration=0.2) 
            print("do you wish to say something? say yes or no")
              
            #listens for the user's input  
            audio2 = r.listen(source2, phrase_time_limit=4)
            #print("x")
              
            # Using ggogle to recognize audio 
            Choice = r.recognize_google(audio2) 
            Choice = Choice.lower() """
            """print("Did you say "+MyText) 
            SpeakText(MyText)""" 
    
            """if Choice=='no':
                break"""
            flag=False
            
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("I am exiting!!!!! you didn't speak anything")
        flag=False

import pandas as pd
df=pd.read_csv("contacts.csv",usecols=['Name'])

a=len(df)
print(a)
contact_list=[]
for i in range(0,a):
    contact_list.append(df.Name[i].lower())
print(contact_list)

b=len(MyText1)
print(b)
asked_list=[]
for i in range(0,a):
    #print(contact_list[i][0:b])
    if MyText1==contact_list[i][0:b]:
        asked_list.append(contact_list[i])
asked_list1=[x.lower() for x in asked_list]
print(asked_list1)
     
print("which one u want to call",asked_list)

flag=True
while(flag):     
    #print("x")
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
            #print("x")
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            print("speak now you have 4 seconds")
              
            #listens for the user's input  
            audio2 = r.listen(source2, phrase_time_limit=4)
            print(audio2)
              
            # Using ggogle to recognize audio 
            MyText2 = r.recognize_google(audio2, language='en-US')
            MyText2 = MyText2.lower()
            print(MyText2)
            flag=False
            
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("I am exiting!!!!! you didn't speak anything")
        flag=False
        
"""for i in asked_list:
    if MyText2==i:
        print(i)"""

"""with open("names.txt","r+") as f:
    x=f.readlines()
    original_words=[]
    for i in x:
        original_words.append(i.strip())
for a in assumed_words:
    #print(a)
    #print(original_words)
    if a in original_words:
        print(a)
        break;
else:
    print("Not Found")"""

for i in asked_list1:
    if MyText2==i:
        print(i)
        
