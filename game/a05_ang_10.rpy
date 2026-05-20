label a05_ang_10:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_10:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg05ba_grayscale with Dissolve(0.375)
    pause 1.125

    play music bgm05

    show sachiko 1 grayscale lg outfit b with Dissolve(0.25)

    play sound se558b_100

    show sachiko:
        "sachiko 1 grayscale lg outfit cigarette i" with Dissolve(0.25)
        ycenter 1036
        ShakeYes

    voice "SYO_0214"
    sachiko "\"I'm guessing you've figured this out by now, but...\""

    show sachiko 1 grayscale lg outfit cigarette i:
        xoffset 0 yoffset 0
    with None

    "She took a cigarette out slowly."

    show sachiko 1 grayscale lg outfit cigarette a with dict_dissolve_25

    voice "SYO_0215"
    sachiko "\"I was an angel, too.\""

    "She confessed to me flatly, like it was the most obvious thing in the world."

    "...Yeah."

    "I accepted the information in much the same way."

    "Actually, I'd been waiting to hear those words, and was relieved to have my answer."

    voice "SYO_0216"
    sachiko "\"The angel they saw as kids was me.\""

    "I still wasn't surprised. I had begun to suspect. The way Sachiko looked at those girls was special."

    show sachiko 1 grayscale lg outfit cigarette g with dict_dissolve_25

    voice "SYO_0217"
    sachiko "\"I guess I've known them for a long time, come to think of it. It's just an instant for an angel, though.\""

    "Supposedly, innocent children can see angels. They usually forget about them by the time they grow up, though."

    "But very rarely, they'll be able to hold onto those memories."

    "They must be the reason images of angels exist."

    show sachiko 1 grayscale lg outfit cigarette a with dict_dissolve_25

    voice "SYO_0218"
    sachiko "\"They grew into good girls.\""

    "I nodded."

    show sachiko 1 grayscale lg outfit cigarette i with dict_dissolve_25

    voice "SYO_0219"
    sachiko "\"I wanted to see the things those girls saw, feel what they felt... so I got rid of my wings.\""

    show sachiko:
        "sachiko 1 grayscale lg outfit cigarette g" with Dissolve(0.25)
        ShakeYes

    voice "SYO_0220"
    sachiko "\"Though that wasn't the only reason... But that's another story.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a05_ang_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
