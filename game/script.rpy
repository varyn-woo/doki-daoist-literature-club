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
default horny_score = 0

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

    scene bg dojo with fade
    
    if seen_guanzi == 0 or seen_laozi == 0:

        "Pick which philosopher you would like to train with today."

        menu:

            "Train with Guanzi" if seen_guanzi == 0:
                jump gday1start

            "Train with Laozi" if seen_laozi == 0:
                jump lday1start

label end:

    "You got to know two philosophers today."

    show guanzi at left with fade

    "Guanzi"

    show laozi at right with fade

    "and Laozi."

    if horny_score == 5:
        jump hornyending

    elif laozi_score < 0 and guanzi_score < 0:
        jump badending

    elif laozi_score > 0 and guanzi_score > 0:
        jump goodending

    elif laozi_score > 0:
        jump laoziending

    else:
        jump guanziending

label hornyending:

    show guanzi angry at left

    g "You really need to detach yourself from worldly desires."

    show laozi disappointed at right

    l "Agreed. This attitude of yours is not as attractive as you seem to think it is."

    "BONK! Go to horny jail."

    "THE END."

    return    

label badending:

    show guanzi angry at left

    g "I have to say, you have much to improve on."

    show laozi disappointed at right

    l "You really didn't absorb anything we told you, did you?"

    hide laozi with dissolve
    hide guanzi with dissolve

    "The two philosophers go on a date without you, leaving you behind to stew in your own mistakes."

    "THE END."

    return

label goodending:

    g "You were a very good student!"

    if not chaotic:
        g "You also managed to avoid chaos."

    l "I think you have potential, sage in training."

    g "We'd love to..."

    l "...invite you on a date with both of us."

    "The two philosophers take you on a date, and you all take over the world together."

    "THE END."

    return

label laoziending:

    show guanzi angry at left

    g "I have to say, you have much to improve on."

    show laozi smiling at right
    
    l "Perhaps the Inward Training was not to your taste, but no matter."

    l "You understood the Dao De Jing well."

    l "I'd be happy to follow the path of the sage with you at my side."

    hide guanzi with dissolve

    "You go on a date with Laozi and rule the world through the teachings of the Way."

    "THE END."

    return

label guanziending:

    show laozi disappointed at right

    l "You really didn't absorb anything we told you, did you?"

    g "No, they may not have understood your confusing and manipulative teachings,"

    g "but they understood my inward training perfectly."

    g "Don't listen to Laozi. I'm happy to guide you on your journey through the Way."

    hide laozi with dissolve

    "You go on a date with Guanzi and learn to center yourself with him by your side."

    "THE END."
    
    return
