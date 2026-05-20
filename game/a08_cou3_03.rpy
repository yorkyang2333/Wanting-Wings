label a08_cou3_03:

    scene bg09cb with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_boiling1
    pause 0.5

    show bg_obi
    show miyako 1 lg pyjama_a i
    with Dissolve(0.5)

    show miyako:
        ShakeYes
        1.5
        ShakeYes

    voice "2MI_0558"
    miyako "\"Nn... mmh... rgh!\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "The crab-eating lion was really struggling to get the meat out of the shells."

    "They'd taken part of the shells off before cooking, and they had crab spoons, so the difficulty should have been rather low."

    "But Miyako was trying this for the first time in her life."

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_0722"
    hina "\"Miyako, it's easier if you move the crab instead of the spoon. Be careful of the spikes on the shell, though.\""

    show miyako:
        "miyako 1 lg pyjama_a b" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0559"
    miyako "\"Okay! Oh, you're right!\""

    show miyako 1 lg pyjama_a b:
        xoffset 0 yoffset 0
    with None

    "Miyako dutifully followed Hina's advice, eyes sparkling when the meat came out smoothly."

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0432"
    sachiko "\"Sorry. Maybe we should have taken the shells off first.\""

    show miyako 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0560"
    miyako "\"No, this is fun! And it's delicious!\""

    "She said, bringing the fruit of her effort to her mouth and starting in on another leg."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0433"
    sachiko "\"Oh yeah? Well, good.\""

    "Seeing Miyako innocently enjoying the process, Sachiko couldn't help smiling."

    hide miyako with Dissolve(0.5)

    show sachiko z4 2 lg outfit f:
        xcenter 298
    show hina z4 1 lg pyjama_pjm a:
        xcenter 726
    with Dissolve(0.25)

    voice "2HI_0723"
    hina "\"Miyako really gives everything her all, doesn't she?\""

    voice "2SA_0434"
    sachiko "\"Yeah. She's a good girl...\""

    show hina:
        "hina z4 1 lg pyjama_pjm h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0724"
    hina "\"On the other hand...\""

    show hina z4 1 lg pyjama_pjm h:
        xoffset 0 yoffset 0
    with None

    "Hina looked past Miyako with a sigh."

    hide hina
    hide sachiko
    with Dissolve(0.5)

    show fumi 2 lg pyjama i at pos_l
    show rin 1 lg pyjama glasses c at pos_r
    with Dissolve(0.25)

    voice "2FU_0566"
    fumi "\"Here, I got this crab meat out for you.\""

    show rin:
        "rin 1 lg pyjama glasses d" with Dissolve(0.25)
        ShakeYes

    voice "2RI_0737"
    rin "\"Yay~, nice and easy~\""

    show rin 1 lg pyjama glasses d:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0567"
    fumi "\"What would you like next?\""

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0738"
    rin "\"More crab~\""

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0568"
    fumi "\"You need to eat your vegetables too, you know.\""

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0739"
    rin "\"I'll eat a vegetable after the next crab~\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0569"
    fumi "\"Really?\""

    show rin:
        "rin 1 lg pyjama glasses d" with Dissolve(0.25)
        ShakeYes

    voice "2RI_0740"
    rin "\"Really~♪\""

    show rin 1 lg pyjama glasses d:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 2 lg pyjama i" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_0570"
    fumi "\"Well, alright...\""

    show fumi 2 lg pyjama i:
        xoffset 0 yoffset 0
    with None

    "Fumi said, plucking some more crab from the pot and smiling as she worked the meat out."

    hide rin
    hide fumi
    with Dissolve(0.5)

    show sachiko z4 1 lg outfit a:
        xcenter 298
    show hina z4 1 lg pyjama_pjm d:
        xcenter 726
    with Dissolve(0.25)

    show hina:
        ShakeJump

    voice "2HI_0725"
    hina "\"What is this?! Seriously?!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0435"
    sachiko "\"Couldn't tell ya~\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0741"
    rin "\"Fumi, my glasses are all foggy.\""

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0571"
    fumi "\"They are! You must have gotten steam on them. Here, let me wipe them off.\""

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_0742"
    rin "\"I can't see~\""

    show hina:
        "hina z4 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0726"
    hina "\"Is this dorm a preschool?! Is Asou Rin's mother?!\""

    show hina z4 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeNo_4_500

    voice "2SA_0436"
    sachiko "\"I told you, don't ask me!\""

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None

    "Sachiko's voice shook as Hina shook her shoulders."

    "All throughout the hotpot, Rin was being a total baby and Fumi was taking care of her."

    "She picked pieces of food out of the pot for her and cleaned it up when Rin spilled. And—"

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0743"
    rin "\"Hot!\""

    $ side_image = "fumi 1 side pyjama k"

    voice "2FU_0572"
    fumi "\"Oh, is it too hot? I'll blow on it for you.\""

    "Fumi took the bowl from Rin and blew on the soup."

    show hina z4 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_0727"
    hina "\"...I'm gonna take that hot soup and...\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0437"
    sachiko "\"Settle down.\""

    $ side_image = "fumi 2 side pyjama c"

    voice "2FU_0573"
    fumi "\"Phoo... phoo... how's that? Say, 'ahh'~\""

    $ side_image = "rin 1 side pyjama glasses d"

    voice "2RI_0744"
    rin "\"Ahh~\""

    voice "2HI_0728"
    hina "\".........\""

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0438"
    sachiko "\"She got quiet.\""

    show hina z4 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0729"
    hina "\"This isn't just Rin being selfish. Asou's having fun babying her, too.\""

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0439"
    sachiko "\"This that codependence thing?\""

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0730"
    hina "\"You think this is okay?\""

    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0440"
    sachiko "\"Want me to blow on yours, Hinacchi? Say, 'ahh'!\""

    "Sachiko brought her chopsticks to Hina's mouth."

    show hina z4 1 lg pyjama_pjm g with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "2HI_0731"
    hina "\"No!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0441"
    sachiko "\"Feh. You're no fun. What about you, Mikoyan?\""

    hide hina with Dissolve(0.25)

    show miyako z4 1 lg pyjama_a e:
        xcenter 726
    with Dissolve(0.25)

    voice "2MI_0561"
    miyako "\"Yes?\""

    show sachiko:
        "sachiko z4 1 lg outfit g" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0442"
    sachiko "\"'Ahh'~\""

    show sachiko z4 1 lg outfit g:
        xoffset 0 yoffset 0
    with None
    show miyako:
        "miyako z4 1 lg pyjama_a d" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0562"
    miyako "\"Ahh.\""

    show miyako z4 1 lg pyjama_a d:
        xoffset 0 yoffset 0
    with None

    "She's easy."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 0:
        jump a08_comn_13
    else:
        jump a08_comn_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
