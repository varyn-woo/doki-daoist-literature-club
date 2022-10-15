default look = False
default leave = False
default dictator = False
default knowledge = False
default breakin = False

label lday1start:

    $ seen_laozi += 1

    y "I think I'll train with Laozi."

    show laozi

    l "A wise choice."

    l "Let me show you something."

    y "What is it?"

    l "Just follow me."

    "You follow Laozi."

    scene bg empty
    with fade

    show laozi

    l "Welcome to the plane of emptiness."

    l "We will start here."

    menu:
        "HELP!!! Get me out of here!":
            show laozi disappointed
            $ laozi_score -= 0.5
            l "Please keep your calm."
            show laozi -disappointed
        
        "Wow. This place is so empty!":
            $laozi_score += 1
            l "Well, what did you expect?"
            l "It is the plane of emptiness, after all."

        "Is this your bedroom? *wink wink*":
            show laozi disappointed
            l "Please show some restraint."
            $ laozi_score -= 1
            show laozi -disappointed
    
    l "Let us begin."

    l "We're here because, in the Dao De Jing chapter 11 (Varyn's Dad's annotated translation), it says..."

    l "Thirty spokes converge on a hub,"

    l "but it's the emptiness that makes a wheel work."

    l "Pots are fashioned from clay,"

    l "but it's the emptiness that makes a pot work."

    l "Windows and doors are carved for a house,"

    l "but it's the emptiness that makes a house work."

    l "Existence makes something useful,"

    l "but emptiness makes it work."

    l "And that's why I took you here to this empty space."

    l "In order to learn, you must first embrace the emptiness of your mind."

    y "So you're calling me stupid?"

    l "Only for now."

    y "That's only very mildly reassuring."
    
    "With that, Laozi mysteriously disappears."

    hide laozi with fade

    stop music fadeout 1.0

    y "..."

    y "Hello?"

    "You receive no response."

label blankchoice:

    y "What now?"

    menu:
        "Meditate":
            jump meditate

        "Look for Laozi" if not look:
            jump look

        "Try to leave" if not leave:
            jump leave

label meditate:

    play music meditation

    "You close your eyes and meditate."

    "After some time..."
    
    "...you hear a voice speaking to you."

    "It feels grand and godlike."

    "(DDJ Chapter 1)"

    "The way that becomes a way is not the Immortal Way."

    "The name that becomes a name is not the Immortal Name."

    "The maiden of Heaven and Earth has no name."

    "The mother of all things has a name."

    "Thus in innocence we see the beginning,"

    "in passion we see the end;"
    
    "two different names, for one and the same"

    "the one we call dark, the dark beyond dark"

    "the door to all beginnings."
    
    "..."

    jump door

label look:

    $ look = True

    "You wander around the premises, looking for Laozi."

    "He is nowhere to be found."

    "After a while, you give up."
    
    jump oof

label leave:

    $ leave = True

    "You run as fast as you can in a single direction."

    "You run and you run and you run..."

    "...and you run and you run and you run..."

    "Until your legs give out."

label oof:

    "You're back exactly where you started."

    jump blankchoice

label door:

    scene bg door with dissolve

    "After meditating for a while, you see a door."

    menu:
        "Go through the door":
            pass 

        "Go Through The Door":
            pass 

        "GO THROUGH THE DOOR!":
            pass 

label palace:

    play music main fadein 0.5 fadeout 0.5

    scene bg palace with fade

    if leave and look:
        $laozi_score -= 1
        show laozi disappointed
        l "Took you long enough."
    
    elif leave or look:
        show laozi
        l "It took you a bit, but you figured it out."

    else:
        $ laozi_score += 1
        show laozi smiling
        l "There you are!"

    show laozi -smiling -disappointed

    l "I hope your meditation went well."
    
    y "It did. I think I might have found the Way."

    show laozi smiling

    l "Haha, you're funny."

    show laozi -smiling

    l "As chapter 21 of the Dao De Jing says..."

    l "the Way is a thing waxes and wanes."

    show laozi

    l "So really, you must lose the way after you find it."

    l "And you must find it again once it is lost."

    y "I see..."

    y "So where exactly are we?"

    l "We're in my palace."

    y "You're a king?!"

    l "I'm no king. I'm just a sage. The palace is more of a metaphor."

label govchoice:

    menu:
        "So you're a dictator?" if not dictator:
            jump dictator

        "So you're just a holder of knowledge?" if not knowledge:
            jump knowledge

        "So you broke into this palace?" if not breakin:
            jump breakin

        "None of this makes sense.":
            jump huh

label dictator:
    
    $ dictator = True

    show laozi smiling

    l "You would think that makes ruling the world easy, wouldn't you?"

    show laozi -smiling

    l "Well, as the Dao De Jing says in chapter 29..."

    l "Trying to govern the world with force, I see this not succeeding."

    l "The world is a spiritual thing. It can't be forced."

    l "To force it is to harm it; to control it is to lose it."

    l "I also explain in chapter 53 that..."

    l "Were I sufficiently wise, I would follow the Great Way"

    l "and only fear going astray,"

    l "but, and I'm paraphrasing a bit here:"

    l "people are imperfect and do not all share the same goals as me."

    l "They lavish in excess and tire of their material possessions quickly."

    show laozi smiling

    l "It would be foolish to assume everyone can simply follow one Way and be happy with it."

    show laozi disappointed

    l "That's why I am not a dictator."

    show laozi -disappointed

    jump govchoice

label knowledge:

    $ knowledge = True

    l "It's not that simple."

    l "In chapter 49 of the Dao De Jing, it states..."

    l "The sage has no mind of his own."

    l "His mind is the mind of the people."

    l "I am not the holder of some secret wisdom, but rather a representative of the people."

    l "I help synthesize the goals, lives, and wisdom of all people over which I have power."

    l "I only facilitate communication and decide what nees to be said."

    l "I do not have anything special that others don't."

    jump govchoice

label breakin:

    $ breakin = True

    l "I guess you could say that."

    l "I'm no king, after all."

    show laozi smiling

    l "But who's going to kick me out? The people love me."

    show laozi -smiling

    l "The real goal of the sage is to help everyone while remaining good,"

    l "not only in the objective moral sense, but also in the eyes of his people."

    l "Being diplomatic isn't just about being nice. It's about protecting yourself."

    l "That is but a small part of what it means to be a sage."

    y "I see."

    jump govchoice

label huh:

    l "It's not supposed to make sense."

    l "The world doesn't make sense. You'll never agree with everyone."

    l "You can never make a perfect choice, or be a perfect ruler."

    l "You should simply try to reduce complexity and struggle,"

    l "strive toward order,"

    l "and follow the Way without becoming too obsessed with it."

    l "Being a sage isn't about following a clear set of instructions."

    l "If it were that easy, everyone would do it."

    menu:
        "So what do you want me to do then?":
            $ laozi_score -= 1
            show laozi disappointed
            l "You really don't get it, do you?"
            show laozi -disappointed

        "It's not easy, but I'll do my best to listen to the Way.":
            $ laozi_score += 1
            show laozi smiling
            l "Good. Maybe you've got some brains after all."
            show laozi -smiling

        "God, you're so hot.":
            show laozi disappointed
            l "I've been told I'm rather cold, actually."
            l "And I'm definitely not a god."
            if laozi_score < 0:
                l "Regardless, you have little chance of winning my affections."
            show laozi -disappointed

label lday1end:

    if laozi_score >= 3:
        show laozi smiling
        l "You seem very level-headed and wise."
        l "I wouldn't quite go so far as to say I'd trust you with the entire nation of China today,"
        l "but I might say it at some point in the future."
        show laozi -smiling
    
    elif laozi_score > 0:
        l "You did well today."
        l "Remember to always keep yourself in check,"
        l "and follow the Way without becoming overzealous about it."

    elif laozi_score == 0:
        l "I'm not sure what you got out of our conversation,"
        l "but hopefully you learned something?"

    else:
        show laozi disappointed

        l "Well, that was... an experience."

        l "Maybe you'd do better with Guanzi's softer teaching style."

        show laozi smiling

        l "If you come back, I will make you my tax collector,"

        l "a scapegoat for the people to hate whenever times get tough."

        hide laozi

        jump mainchoice

    l "You're welcome to come back and learn more tomorrow."

    l "I enjoyed your company, so I hope to see you again!"

    hide laozi

    scene bg dojo with dissolve

    jump mainchoice