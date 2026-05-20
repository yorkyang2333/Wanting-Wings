label a09_cou2_05:

    scene bg06aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show bg_obi
    show hina 1 lg school k
    with dict_dissolve_50

    voice "2HI_1019"
    hina "\"What were you talking about just now?\""

    "The chapel at lunchtime."

    "Hina asked Rin a question just as she was about to start eating."

    show hina:
        xcenter 512
        easein 0.5 xcenter 252
    pause 0.5

    show rin 1 lg school e at pos_r with dict_dissolve_25

    voice "2RI_1001"
    rin "\"Hunh? Me? Just when?\""

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_1020"
    hina "\"Just now with Honjou.\""

    "Honjou was a classmate of theirs. Hina had seen her stop Rin and say something to her when they were leaving the classroom."

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_1002"
    rin "\"She didn't understand something during class.\""

    show hina 1 lg school k with dict_dissolve_25

    voice "2HI_1021"
    hina "\"Oh yeah?\""

    show rin:
        "rin 1 lg school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1003"
    rin "\"I dunno why she asked me about it.\""

    show rin 1 lg school k:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_1022"
    hina "\"'Cause you're smart.\""

    $ side_image = "fumi 2 side school a"

    voice "2FU_0810"
    fumi "\"......\""

    "I get the feeling Fumi's the only one noticing the slight awkwardness in Hina's smile."

    show rin 1 lg school b with dict_dissolve_25

    voice "2RI_1004"
    rin "\"She should just ask the teacher.\""

    $ side_image = "fumi 1 side school d"

    voice "2FU_0811"
    fumi "\"Well, you're a good instructor, Ogata!\""

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_1005"
    rin "\"Am I?\""

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_1023"
    hina "\"You're strict with me...\""

    show rin 2 lg school a with dict_dissolve_25

    voice "2RI_1006"
    rin "\"Well, my selling point's my individual lessons tailored to your learning level. Your grades are up, right?\""

    show hina 2 lg school b with dict_dissolve_25

    voice "2HI_1024"
    hina "\"Yeah... a little. Thanks.\""

    show rin 1 lg school k with dict_dissolve_25

    voice "2RI_1007"
    rin "\"You're welcome.\""

    hide rin
    hide hina
    with Dissolve(0.5)

    show miyako 1 lg school_a j with dict_dissolve_25

    voice "2MI_0866"
    miyako "\"Rin's smart, Hina's super athletic, and Fumi's really good at cooking. And everybody in your class knows all that. That's pretty impressive, isn't it?\""

    "The three girls looked at each other."

    show miyako 1 lg school_b k with dict_dissolve_25

    voice "2MI_0867"
    miyako "\"I want some kind of special skill I can brag about, too!\""

    "She said eagerly."

    $ side_image = "side/hina_fumi_rin_school_sozai01.webp"

    $ voice3("hina","2HI_1025","rin","2RI_1008","fumi","2FU_0812")
    hina_rin_fumi "\"Sleeping a lot?\""

    show miyako 2 lg school e with dict_dissolve_25

    voice "2MI_0868"
    miyako "\"What...?\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg06aa with bg_effect_05
    pause 0.5

    "......"

    "Hina and Rin were talking and fooling around after eating, looking up at the stained glass."

    "Fumi and Miyako were still eating, meanwhile, watching the other two as they did."

    show bg_obi
    show fumi 1 lg school a at pos_l
    show miyako 1 lg school_a e at pos_r
    with dict_dissolve_25

    voice "2MI_0869"
    miyako "\"Lately, she's always right next to her during breaks.\""

    show fumi 2 lg school g with dict_dissolve_25

    voice "2FU_0813"
    fumi "\"Natsume? Yeah. Valentine's is coming up, so maybe she's trying to guard Ogata.\""

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_0870"
    miyako "\"Guard her?\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "2FU_0814"
    fumi "\"You know, since she said she was always popular... Maybe she's worried someone will try to steal her.\""

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_0871"
    miyako "\"I see. Like Honjou?\""

    "Oho."

    show fumi 1 lg school a with dict_dissolve_25

    voice "2FU_0815"
    fumi "\"Could be. Natsume's the one who wants us to have lunch in the chapel instead of the classroom.\""

    show miyako:
        "miyako 1 lg school_a b" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0872"
    miyako "\"She's like a guard dog. Bow wow.\""

    show miyako 1 lg school_a b:
        xoffset 0 yoffset 0
    with None

    "She squeezed her hands in front of her. Probably a dog imitation."

    show fumi:
        "fumi 1 lg school c" with Dissolve(0.25)
        2.1
        "fumi 1 lg school i" with Dissolve(0.25)

    voice "2FU_0816"
    fumi "\"Beware of dog, right? I don't think she's doing it consciously, though. At least, that's the sense I get.\""

    show fumi 1 lg school i:
        pass
    with None
    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_0873"
    miyako "\"What about Rin?\""

    show fumi 1 lg school a with dict_dissolve_25

    voice "2FU_0817"
    fumi "\"Oh, Ogata has no idea.\""

    "No hesitation."

    show fumi 1 lg school c
    show miyako 1 lg school_a d
    with dict_dissolve_25

    $ voice2("fumi","2FU_0818","miyako","2MI_0874")
    fumi_miyako "\"Ahahahaha.\""

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_0875"
    miyako "\"Everything is a first experience for them right now.\""

    show fumi 1 lg school b with dict_dissolve_25

    voice "2FU_0819"
    fumi "\"Huh? You wouldn't happen to be experienced yourself, would you, Miyako?\""

    show miyako 1 lg school_b h with dict_dissolve_25

    voice "2MI_0876"
    miyako "\"Only observing.\""

    show fumi 2 lg school g with dict_dissolve_25

    voice "2FU_0820"
    fumi "\"Observing?\""

    show miyako 1 lg school_b g with dict_dissolve_25

    voice "2MI_0877"
    miyako "\"Oh, umm... like on TV.\""

    show fumi 2 lg school b with dict_dissolve_25

    voice "2FU_0821"
    fumi "\"Ah, I get it.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared == 1:
        jump a09_comn_07
    elif routes_cleared >= 2:
        jump a09_cou4_02
    else:
        jump a09_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
