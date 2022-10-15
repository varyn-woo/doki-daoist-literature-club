# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You", color="cccccc")
define g = Character("Guanzi", color="#5e88cc")
define l = Character("Laozi")

default seen_guanzi = 0
default seen_laozi = 0
default guanzi_score = 0
default laozi_score = 0

# The game starts here.

label start:

    play music main

    scene bg dojo

    "It’s your first day at a philosophy class. You enter the classroom, eager to learn."
    
    "Two instructors greet you."

    show guanzi

    g "Hi! I’m Guanzi! I specialize in inward training, a technique that helps you find The Way."

    g "It will help you center yourself and stay happy and healthy as you progress."

    hide guanzi

    show laozi

    l "I’m Laozi. Guanzi knows his stuff, but if you want the real deal, you should come to me."

    l "My trainings are longer and harder to understand, but if you learn them well,"
    
    l "you can not only fight to defend yourself, but rule the world as well."

    hide laozi

    y "Hmmm... it's so hard to choose!"
    
label mainchoice:
    
    if guanzi_score >= 0 or laozi_score >= 0:
        menu:

            "Train with Guanzi" if guanzi_score >= 0:
                if seen_guanzi == 0:
                    jump gday1start
                elif seen_guanzi == 1:
                    jump gday2start

            "Train with Laozi" if laozi_score >= 0:
                if seen_laozi == 0:
                    jump lday1start
                elif seen_laozi == 1:
                    jump lday2start

label end:

    if laozi_score < 0 and guanzi_score < 0:
        jump badending

    elif laozi_score > 0 and guanzi_score > 0:
        jump goodending

    elif laozi_score > 0:
        jump laoziending

    else guanzi_score > 0:
        jump guanziending

label badending:



    return
