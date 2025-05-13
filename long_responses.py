#Name: TORRENO, Lerrica Jeremy S. 
#Course/Year: 1st year/BSCS-DS
#Work title: Midterm Exam: IoT Device Controller
#Date: December 5, 2023 

import random

R_IOT = "Hey there, so Internet of Things device controller, from the word itself. It is a device that allows people to control and monitor their IoT devices, it can be your smartphone, laptops, smart TVs, smart home, and many more. I hope you understood that, my friend."
R_WHERE = "You might be shocked with what I'm about to say, so ready yourself, my friend. You can use this anywhere! I mean anywhere at all! From the lights in your home, cameras, thermostat, garage doors you can even command it. IoT is you assistance in life, buddy."
R_BENEFIT = "This IoT Device Controller will be a huge helping hand in your life, buds! I'm telling you, it can help you by saving time, but doing more. Was it quite misleading? Sorry, basically you can monitor the connected IoT devices in it from the battery percentage, screen time, and notifications that is sent from that device. You can also give commands. Works like magic, right?"
R_DEVICES = "You know, you might think that this is some sort of black magic, but its not. It can actually control anything from smartphones to garage doors to the temperature of the room. It's basically like a human being already, but it doesn't have an appearance, but it's not a ghost.. so don't be scared."
R_STUDENT = "Wow, being a student is stressful that's for sure. Iot Device Controller can be your study buddy when you need one, although it may not really answer your homeworks. But, it sure can help you relieve stress with just one command you can feel like you're in a coffee shop studying and it can actually improve your productivity, and it can also enhance your 21st century skills, which is being technology literate. Oh, before I forget it can also help you with multi-tasking."
R_WORKING = "Most definitely! Especially if you work at home and you need to do some chores, but can't leave your desk. Just one command and the IoT Device Controller is at your service, my dear friend. Having this device will make you feel that you are not alone at home.. not to sound creepy or anything, but this device will surely help you in more ways than one."
R_NOT = "Pal.. of course you can! This device has a user-friendly design that will allow anyone, even if you are not really a techy-kinda person. It has a single interface and it uses human-like language that makes it even more easier to use. You should give it a try first and let's see the results."
R_PRIORITIES = "If you are a student, housewife, or just any adult that needs help about prioritizing or managing things. This is for you, bestie. This device can take down notes for you, and if you forgot it with just one voice command, the device can help you remember it and it can even send you notifications and update you with real-time news or weather updates."
R_COMMUNICATION = "That is something that I can assure you of myself, Champ. This device prioritizes data security and privacy, which means any data or information that will be exchanged through this device will only remain in this device. To sum it up, just like in the ROTC, what you see, what you hear, what you feel, when you leave, leave it here. That is something that IoT Device Controller upholds."
R_CUSTOMIZE = "Most definitely! It's like a build your own lego, but instead of lego bricks you can customize your own device by setting up your personalized voice commands that will do a specific action and it can even respond to you in natural language."
R_BILL = "Did you know that one of the functions of IoT Device Controller is to take care of things that you might forget. One is when turning off lights, we usually forget that right? Another is turning of the aircon, since we're sleeping soundly we forget to turn it off to conserve electricity, this device can do that for you! It likes to conserve electricity."
R_EYES = "My buddy, this device will actually remind you to take a rest by showing you the report of how long you are using a specific device and it can even provide you the summary of your entire time of usage of each device! It's like a mother scolding you, but in a more calm manner."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response