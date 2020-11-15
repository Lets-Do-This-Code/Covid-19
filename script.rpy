# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lucy")


# The game starts here.

label start:
    scene room1
    show lucy
    l "Hello, my name is Lucy and today I will tell you about the Cov-19 virus.  To move on press the enter button or click."
    l " Press the button on the next screen to learn Cov-19"
    jump let_go

label let_go:
    hide room1
    hide lucy
    show room1
    show lucy_1
    menu:
        "What is Cov-19":
            scene room2
            show lucy_1
            l "COVID-19 is an infectious disease that is now considered a pandemic."
            menu:
                "What is a pandemic":
                    "The Covi-19 or Coronavirus is a pandemic because is it the worldwide spread of a new disease."
                    jump let_go
                "Ok":
                    jump let_go
        "What can I do?":
            show lucy_1
            l "People all over the world are trying to find a cure for the virus."
            scene room3
            l "The best thing you can do is wash and sanitise your hands, regularly."
            scene room5
            l "Cough in your shirt."
            l "If your state needs to wear a mask wear one."
            scene room4
            l "And lastly, if you feel sick ask your, parent, to see a doctor as soon as possible."
            jump let_go

        "Where else can I find information?":
            show lucy_1
            l "You can find information at this link https://kidshealth.org/en/parents/coronavirus.html"
            l "Or from a trusted adult"
            jump let_go

    return
