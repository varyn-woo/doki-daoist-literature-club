default mind = False
default body = False
default sex = False
default chaotic = False

label gday1start:

    $ seen_guanzi += 1

    y "I think I'll train with Guanzi."

    show guanzi

    g "I'm glad! Let's get started."

    g "Inward training is the combination of multiple practices."

    g "The main three I'll start with are the mind, the body, and the way bodies interact."

label threepractices:

    if body and mind and sex:
        
        jump gday1end

    g "Now, which of the main practices would you like to learn about?"

    menu:
        "Mind" if not mind:
            jump mind
    
        "Body" if not body:
            jump body
    
        "...Interaction?" if not sex:
            jump sex

        "I'm not interested in any of these":
            jump gday1end

label mind:

    $ mind = True
    
    g "To understand the mind, we must first understand the Way."

    g "From Inward Training, Passage V..."

    g "The Way has no fixed position;"

    g "It abides within the excellent mind."

    g "When the mind is tranquil and the vital breath is regular,"

    g "The Way can thereby be halted..."

    g "...Cultivate your mind, make your thoughts tranquil,"
    
    g "And the Way can thereby be attained."

    y "Oh, I see!"
    
    y "The way is ever changing,"

    y "but my mind needs to be tranquil to find it."

    y "It makes sense, in a weird paradoxical kind of way."

    g "Exactly! So answer me this:"

label chaosquestion:

    g "Should you seek to be orderly or chaotic?"

    menu:
        "Orderly":
            $ guanzi_score += 0.5
            jump order

        "Chaotic":
            jump chaos

label order:

    g "Correct!"

    g "From passage XIV in Inward Training..."

    g "When your mind is well ordered, your senses are well ordered..."

    g "...Without order, you will always be chaotic."

    g "If chaotic, you die."

    if not chaotic:
        y "I die?! I had no idea!"

    else:
        y "I know! I'll never have a messy room again, I promise!!"

    g "So now you know the key to how the mind relates to the Way."

    menu:
        "Thank you so much! I learned a lot.":
            g "No problem! Happy to help."
            $ guanzi_score += 1
        
        "That explanation was sooo sexy!":
            show guanzi blush
            g "Uhhh... ok?"
            show guanzi -blush

        "Wow that was super dumb and unhelpful.":
            show guanzi angry
            g "I suppose my teachings aren't for everyone."
            $ guanzi_score -= 1
            show guanzi -angry


    jump threepractices

label chaos:

    stop music fadeout 1.0

    play sound death

    if not chaotic:
        $ guanzi_score -= 1

    $ chaotic = True

    show guanzi

    scene you died
    with dissolve

    pause(1.0)

    show guanzi glitch

    g "IF CHAOTIC, YOU DIE."

    menu:
        
        "Try again":
            scene bg dojo
            with dissolve
            show guanzi -glitch
            play music main
            jump chaosquestion

label body:

    $ body = True

    g "The body is an important part of Inward Training."

    g "You need to make sure to take good care of your body by feeding it properly."

    g "As the Inward Training states in passage XXIII..."

    g "The mean between overfilling and overrestricting"

    g "This is called \"harmonious completion.\""

    g "It is where the vital essence lodges"

    g "And knowledge is generated..."

    g "...When full, move quickly..."

    g "...If when full you don't move quickly,"

    g "Vital energy will not circulate to your limbs."

    g "How would you interpret this passage?"

    menu:

        "I should run 3 miles after every meal.":
            show guanzi angry
            g "What?! No! That's not what I meant at all!"
            g "Anyway..."
            $ guanzi_score -= 1
            show guanzi -angry

        "I should make sure to eat regularly and in moderate amounts.":
            g "Exactly! Listen to your body and practice moderation."
            $ guanzi_score += 1

        "Why would I eat food when I could simply kiss you?":
            show guanzi blush
            g "Uhhh..."
            show guanzi -blush

    jump threepractices

label sex:

    $ sex = True

    g "Ahem, well, yes... interactions."

    menu:

        "You don't have to be shy around me.":
            $ guanzi_score += 1

        "I want to have *interactions* with you ;)":
            show guanzi blush
            g "I don't really know what to say to that..."
            show guanzi -blush

        "Ugh, just say it.":
            show guanzi angry
            g "Your reaction isn't aligned with the Way."
            g "Settle your mind and let me take my time."
            $ guanzi_score -= 1
            show guanzi -angry

    g "..."

    g "Well, by interactions, I really meant interpersonal interactions."

    y "Like sex?"

    show guanzi blush

    g "Yeah. That."

    g "Anyway..."

    show guanzi -blush

    if guanzi_score <= 0:

        g "Actually, I don't want to talk about this anymore."

        g "Let's move on."

    else:

        g "If you enjoy sex, you should practice it in moderation."

        g "The text skirts around it a bit..."

        y "Like you do?"

        show guanzi blush

        g "Yeah, I guess."

        show guanzi -blush

        g "But the point is to trust yourself"

        g "and not lose the Way."

        y "Makes sense! Thanks!"

    jump threepractices

label gday1end:

    if guanzi_score >= 3:
        g "I thoroughly enjoyed my day with you!"
    
    elif guanzi_score > 0:
        g "I'm glad you learned a bit about Inward Training."

    elif guanzi_score == 0:
        g "I'm not sure what you got out of our conversation,"

        g "but hopefully you learned something?"

    else:
        show guanzi angry

        g "Well, that was... an experience."

        g "Maybe you're better suited to Laozi's teachings,"

        g "but do bear in mind that he has even higher standards than me."

        show guanzi -angry

        g "Good luck in your philosophical ventures, I guess."

        hide guanzi

        jump end

    g "Feel free to find me again to go more in depth about inward training."

    hide guanzi

    jump end