label gday2start:
    
    $ seen_guanzi += 1

    show guanzi

    g "Welcome back to Inward Training."

    g "Today, we're going to do something a little different."

    g "I could just tell you more about my philosophy and lead you through some nice meditations,"

    g "but that wouldn't be much different than just giving you my book to read."

    g "Instead, want to go somewhere?"

    menu:
        "Sure!":
            $ guanzi_score += 1
            jump go

        "I don't think I'm ready for that."
            $ guanzi_score -= 1
            jump nvm

