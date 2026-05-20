label a04_cou1_07:

    scene bg05bb with Dissolve(0.5)
    pause 1.5

    scene bg02ba with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 1 sm school_scarf b with Dissolve(0.25)

    $ side_image = "hina 2 side school f"

    voice "HIN_1204"
    hina "\"Rin, can you sit down a sec?\""

    "Hina sat down at the table and beckoned Rin over."

    show rin:
        "rin 1 sm school a" with Dissolve(0.25)
        ShakeYes

    play sound se116a

    voice "RIN_0974"
    rin "\"Can I change first?\""

    show rin 1 sm school -school_scarf a:
        xoffset 0 yoffset 0
    with None

    "Rin called back to the living room, removing her scarf."

    $ side_image = "fumi 2 side school a"

    voice "FUM_1022"
    fumi "\"We need to tell you something important.\""

    "Fumi was seated next to Hina."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_0975"
    rin "\".........\""

    "Seeing their solemn faces, Rin sighed, hooked her scarf on a bedpost, and headed to the living room."

    stop music fadeout 1.0

    scene black with bg_effect_02
    pause 0.25

    scene bg01ac with bg_effect_02
    pause 0.5

    play music bgm05

    show rin z3 1 lg school b:
        xcenter 918
    show fumi z3 2 lg school a:
        xcenter 124
    show hina z3 1 lg school e behind rin, fumi:
        xcenter 440
    with Dissolve(0.25)

    voice "RIN_0976"
    rin "\"So, why the formality?\""

    voice "HIN_1205"
    hina "\"We thought we should tell you...\""

    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_1023"
    fumi "\"Please don't be surprised.\""

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0977"
    rin "\"Uh huh...\""

    stop music fadeout 3.0

    show hina z3 2 lg school d with dict_dissolve_25

    voice "HIN_1206"
    hina "\"The truth is... the two of us are—\""

    "Hina turned and met Fumi's eye before facing Rin again, her face serious."

    show hina z3 1 lg school f with dict_dissolve_25

    voice "HIN_1207"
    hina "\"We're dating.\""

    show fumi z3 1 lg school h with dict_dissolve_25

    voice "FUM_1024"
    fumi "\"We're sorry for hiding it all this time! You're surprised, aren't you?\""

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0978"
    rin "\"...No, I was aware.\""

    show hina 1 lg school l
    show fumi 1 lg school j
    with None

    camera:
        function LayerShake(40,40,0.5)
    $ persistent.layer_shaken = False

    $ voice2("hina","HIN_1208","fumi","FUM_1025")
    hina_fumi "\"Whaaat?!\""

    camera
    with None

    play music bgm01

    "The two jumped up in shock."

    show hina:
        "hina z3 1 lg school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1209"
    hina "\"H-How did you know...?\""

    show hina z3 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0979"
    rin "\"Hahh... What I want to know is how did you think you were hiding it?\""

    show fumi z3 1 lg school h with Dissolve(0.25)
    show fumi:
        ShakeNo

    voice "FUM_1026"
    fumi "\"But... we were being careful not to show any signs of it...\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg school f with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "HIN_1210"
    hina "\"Yeah, we were being totally normal, weren't we?\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 2 lg school c with dict_dissolve_25

    voice "RIN_0980"
    rin "\"You were not.\""

    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_1027"
    fumi "\"Umm, how long have you known?\""

    show rin z3 2 lg school a with dict_dissolve_25

    voice "RIN_0981"
    rin "\"Since Hina had that fever.\""

    show fumi z3 2 lg school d with dict_dissolve_25

    voice "FUM_1028"
    fumi "\"What?! Since the very beginning?\""

    show rin z3 2 lg school c with dict_dissolve_25

    voice "RIN_0982"
    rin "\"I was right outside the door then.\""

    show hina z3 1 lg school j with dict_dissolve_25

    voice "HIN_1211"
    hina "\"...Eavesdropping?\""

    show rin z3 1 lg school g with dict_dissolve_25

    voice "RIN_0983"
    rin "\"That's rude! You two were making out, so I couldn't come in!\""

    show fumi z3 1 lg school h with dict_dissolve_25

    voice "FUM_1029"
    fumi "\"S-Sorry...\""

    show rin z3 2 lg school c with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0984"
    rin "\"Try not leaving hickeys if you want to keep it a secret.\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z3 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1212"
    hina "\"Huh?\""

    show hina z3 1 lg school l:
        xoffset 0 yoffset 0
    with None

    "Hina brought a hand to her neck."

    show rin z3 2 lg school e with dict_dissolve_25

    voice "RIN_0985"
    rin "\"And you were doing something dirty in the chapel, right?\""

    show hina:
        "hina z3 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_1213"
    hina "\"You were watching?! Pervert!\""

    show hina z3 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0986"
    rin "\"I didn't have to watch, I could just tell!\""

    show hina z3 1 lg school d with dict_dissolve_25

    voice "HIN_1214"
    hina "\"...Are you psychic?\""

    show rin z3 1 lg school i with dict_dissolve_25

    voice "RIN_0987"
    rin "\"It was written all over your faces.\""

    show hina:
        "hina z3 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1215"
    hina "\"Huh?\""

    show hina z3 1 lg school l:
        xoffset 0 yoffset 0
    with None

    "This time she touched her face."

    show rin z3 2 lg school c with dict_dissolve_25

    voice "RIN_0988"
    rin "\"It's a figure of speech!\""

    show fumi z3 1 lg school e with dict_dissolve_25

    voice "FUM_1030"
    fumi "\"But if you knew, why didn't you say anything?\""

    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0989"
    rin "\"I'm not gonna talk about it if you two don't want to bring it up.\""

    show fumi z3 2 lg school h with dict_dissolve_25

    voice "FUM_1031"
    fumi "\"It wasn't that we didn't want to bring it up...\""

    show hina z3 2 lg school h with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_1216"
    hina "\"...It's embarrassing.\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school g with dict_dissolve_25

    voice "RIN_0990"
    rin "\"Well, whatever. I've been having a pretty hard time of it, though.\""

    show fumi z3 2 lg school d with dict_dissolve_25

    voice "FUM_1032"
    fumi "\"A hard time?\""

    show rin z3 1 lg school i with dict_dissolve_25

    voice "RIN_0991"
    rin "\"I've had to keep Sachiko away from the room while you two were flirting. She's weirdly sharp about stuff like this.\""

    show hina z3 1 lg school d with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "HIN_1217"
    hina "\"What, really?!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_1033"
    fumi "\"Ah, is that why you suddenly decided to model for her...?!\""

    show hina z3 1 lg school c with dict_dissolve_25

    voice "HIN_1218"
    hina "\"You're like our Cupid, Rin.\""

    show rin:
        "rin z3 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0992"
    rin "\"That's right. You'd better appreciate me.\""

    show rin z3 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi z3 2 lg school i" with Dissolve(0.25)
        ShakeYes

    voice "FUM_1034"
    fumi "\"Of course we do!\""

    show fumi z3 2 lg school i:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg school f
    show fumi z3 2 lg school h
    with dict_dissolve_25

    voice "HIN_1219"
    hina "\"So, Rin? While we're appreciating you, is there one more thing we can ask you...?\""

    show rin z3 1 lg school e with dict_dissolve_25

    voice "RIN_0993"
    rin "\"Like what...?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
