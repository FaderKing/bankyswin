"""
Copyright [2020] [Zikora Ogbuagu]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
__author__ = 'Zikora Ogbuagu-<ziebroog@gmail.com>'
__copyright__ = 'Copyright (c) 2020, Sporadica Inc.'
__license__ = 'Apache License, Version 2.0'


#Check for Microphone
#GTTS Speak function as gtts.speak()
#Start Up Window

import androidhelper
import time
import random

droid = androidhelper.Android()

#Probable solution to the random-
#dynamic error handling
#import random

protocol = ["Operator", "Family", "Affiliate",]
commands = ["say", "call", "what's my", "what",]
err_prompts = ["Sorry, it looks like i can't perform that command yet. ", "Sorry, i can't perform this task right now, after all, I'm just an AI!",]

Family = ["keta", "kosi", "ifechi", "jachie",]
Affiliate = ["Hardcore Levelling Warrior", "HLW", "hardcore levelling warrior", "hlw",]

Fam = Family

Current_User = ""

#Meta system for the AIDEN API (Android Based)
class Base:
    #Specifically for android
    
    #def talk(msg):
       # droid.ttsSpeak(msg)
    
    def send_msg(msg):
        droid.makeToast(msg)
        droid.ttsSpeak(msg)
        #Base.talk(msg)
        
    #Function For handling master Operations
    def zik_handle():
        print("Welcome Master Zik!: " + "Access Granted: Protocol: " + protocol[0])
        Base.send_msg("Welcome Master Zik!: " + "Access Granted: Protocol: " + protocol[0])
        #To continuously await instructions
        while True:
            Base.recieve(input("What would you like me to do Zik? "))
    
    #Function for handling family operations
    def fam_handle(User):
        print("Welcome Master " + User + "! :" + "Access Granted: Protocol: " + protocol[1])
        Base.send_msg("Welcome Master " + User + "! :" + "Access Granted: Protocol: " + protocol[1] + " ")
        Base.recieve(input("What would you like me to do " + User + "?"))
        
    def start_up(User):
        droid.notify('A.I.D.E.N', "I'm here if you need me. (σˋ▽ˊ)σ")

        if User == "zik":
            Base.zik_handle()
            Current_User = User
            #Add recognition for DTK and Julius
            """print("Welcome Master Zik!: " + "Access Granted: Protocol: " + protocol[0])
            Base.send_msg("Welcome Master Zik!: " + "Access Granted: Protocol: " + protocol[0])
            Base.recieve(input("What would you like me to do Zik? "))
            """
            
        elif User in Fam:
            Base.fam_handle(User)
            Current_User = User
            """
            print("Welcome Master " + User + "! :" + "Access Granted: Protocol: " + protocol[1])
            Base.send_msg("Welcome Master " + User + "! :" + "Access Granted: Protocol: " + protocol[1])
            Base.recieve(input("What would you like me to do " + User + "?"))
            """
            
        elif User in Affiliate:
            Current_User = User
            print("Welcome " + User + "! :" + "Access Granted: Protocol: " + protocol[2])
            Base.send_msg("Welcome " + User + "! :" + "Access Granted: Protocol: " + protocol[1])
            Base.recieve(input("What would you like me to do " + User + "?"))
                    
        else:
            droid.ttsSpeak("Sorry! This Username is not recognized.")
            print("Sorry! This Username is not recognized.")
    
    def raise_error():
        err_prompt = err_prompts[random.randint(0, 1)]
        print(err_prompt)
        droid.ttsSpeak(err_prompt)
          
    def recieve(user_input):
            arg_query = "who are you"
            if user_input.startswith(commands[0]):
                curr_command = user_input.replace(commands[0], "")
                #Base.talk(curr_command)
                droid.ttsSpeak(curr_command)
                print(curr_command)
                
                
            elif user_input.startswith(commands[1]):
                curr_command = user_input.replace(commands[1], "")
                target = curr_command
                prompt = "Calling... " + target
                print(prompt)
                #Base.talk(prompt)
                #droid.phoneCallNumber(target)
                #droid.phoneDial(target)
                #
                droid.ttsSpeak(prompt)
                #Call the target
            
            #The "What's my" Command Function
            elif user_input.startswith(commands[2]):
                droid.batteryStartMonitoring()
                arg1 = "battery"
                curr_command = user_input.replace(commands[2], "")
                if arg1 in curr_command:
                    #Fix the Battery Reading
                    prompt = "Your current battery level is " + str(droid.batteryGetVoltage()) + "!"
                    print(prompt)
                    droid.ttsSpeak(prompt)
                    
            #The "What" Command Function
            elif user_input.startswith(commands[3]):
                arg2 = "time"
                curr_command = user_input.replace(commands[3], "")
                if arg2 in curr_command:
                    prompt = "The time is " + str(time.strftime("%I %M %p on %A, %B %e, %Y"))
                    print(prompt)
                    droid.ttsSpeak(prompt)
                else:
                    Base.raise_error()
        
            #Make all user inputs non case sensitive   
            elif arg_query in user_input:
                prompt = "I am an Artificial Intelligence construct, made by Robert Junior"
                print(prompt)
                droid.ttsSpeak(prompt)
            
            else:
                #print(err_prompt)
                #droid.ttsSpeak(err_prompt)
                Base.raise_error()

droid.ttsSpeak("Declare your Username")         
Base.start_up(input("Declare your Username: "))