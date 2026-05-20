label a03_cou1_05:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg02ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina z3 1 lg pyjama k
    show rin z3 1 lg pyjama g behind hina at pos_r2_z3
    show fumi z3 1 lg pyjama e behind hina at pos_l2_z3
    with Dissolve(0.25)

    show rin:
        ShakeSide

    voice "RIN_0575"
    rin "\"Ugh... my neck hurts...\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0556"
    fumi "\"It's probably because you were reading in such a weird position. Do you want me to rub your shoulders?\""

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0576"
    rin "\"Nah. But I think it'd help if I could rub your boobs.\""

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0557"
    fumi "\"Oh~ I don't think that's going to happen.\""

    show rin:
        "rin z3 1 lg pyjama i" with Dissolve(0.25)
        ShakeNo

    voice "RIN_0577"
    rin "\"Stingy~\""

    show rin z3 1 lg pyjama i:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0740"
    hina "\"Hey, Fumi?\""

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0558"
    fumi "\"Yes?\""

    show hina z3 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0741"
    hina "\"Can I borrow one of your stuffed animals?\""

    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0559"
    fumi "\"One of my stuffed animals?\""

    show hina:
        "hina z3 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0742"
    hina "\"Yeah...\""

    show hina z3 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None

    "Hina nodded bashfully."

    show rin behind hina, fumi:
        "rin z3 2 lg pyjama c" with Dissolve(0.25)
        xcenter 842
        easein 0.25 xcenter 756
    pause 0.25

    play sound se118a

    show hina:
        "hina z3 2 lg pyjama f" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0578"
    rin "\"Oh, Hina, we're still your friends!\""

    show hina z3 2 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0743"
    hina "\"Wh-What?\""

    "Rin suddenly threw her arms around Hina, surprising her."

    show rin z3 2 lg pyjama e with dict_dissolve_25

    voice "RIN_0579"
    rin "\"You poor thing, you've been lonely, haven't you? We haven't been giving you enough attention lately...\""

    show fumi z3 2 lg pyjama d
    show hina z3 1 lg pyjama f
    with Dissolve(0.25)

    show hina:
        ShakeJump

    voice "HIN_0744"
    hina "\"That's not it, stupid!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 2 lg pyjama d with dict_dissolve_25

    voice "RIN_0580"
    rin "\"I promise we'll start taking you for walks—\""

    play sound se103a

    show rin:
        "rin z3 1 lg pyjama j" with Dissolve(0.25)
        xcenter 756
        parallel:
            function LayerShake(20,20,0.5)
        parallel:
            easein 0.25 xcenter 842
    $ persistent.layer_shaken = False
    pause 0.5

    show rin z3 1 lg pyjama i:
        xcenter 842 xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "RIN_0581"
    rin "\"Ugh... you never hold back, do you?\""

    show hina z3 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0745"
    hina "\"Shut up, Rin.\""

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0560"
    fumi "\"Umm, which one would you like?\""

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0746"
    hina "\"Which one's your favorite, Fumi?\""

    show fumi z3 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0561"
    fumi "\"Hmm... I love all of them, but... I sleep with Rapha the most.\""

    show hina z3 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0747"
    hina "\"Then that one, please.\""

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0562"
    fumi "\"Here you go.\""

    "Hina accepted Rapha gingerly."

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0582"
    rin "\"...Suddenly feels like a house of ill repute in here.\""

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeSide
        ShakeSide

    voice "HIN_0748"
    hina "\"Gaaah!!\""

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0563"
    fumi "\"What did you want a stuffed animal for all of a sudden, though?\""

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0749"
    hina "\"W-Well, remember how you said you sleep better with one, Fumi?\""

    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0564"
    fumi "\"Oh? Are you having trouble sleeping?\""

    show hina z3 1 lg pyjama d with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_0750"
    hina "\"N-No, not really, but... oh, yeah, my eyes are just wide open from the café au lait I had earlier.\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0583"
    rin "\"Aww, poor widdle baby. Want me to sing you a lullaby, then?\""

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0751"
    hina "\"No! And stop talking to me like I'm a baby!\""

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0584"
    rin "\"If you can't sleep without a stuffed animal, you're a widdle baby.\""

    show fumi z3 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0565"
    fumi "\"But they say it reduces anxiety and stress when you sleep with a stuffed animal.\""

    show fumi z3 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0566"
    fumi "\"The softness and warmth probably helps you relax.\""

    show rin z3 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0585"
    rin "\"Some people sleep with body pillows too, yeah.\""

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0567"
    fumi "\"Mhm, mhm.\""

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0752"
    hina "\"I'll borrow Rapha for the night, then.\""

    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0586"
    rin "\"Don't get your drool on her.\""

    show hina z3 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0753"
    hina "\"I won't!\""

    show fumi z3 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0568"
    fumi "\"Heheh, it's okay, I'll just give her a bath if you do.\""

    show hina z3 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0754"
    hina "\"I won't... probably.\""

    "Hina took Rapha to her bed."

    show hina:
        "hina z3 1 lg pyjama d flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612
    pause 0.5

    hide hina with None
    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0569"
    fumi "\"Good night. Sweet dreams.\""

    show hina 3 lg light pyjama c with dict_dissolve_25

    voice "HIN_0755"
    hina "\"Night.\""

    show fumi:
        "fumi z3 1 lg pyjama c flat"
        alpha 1.0 xcenter 182
        easeout 0.5 alpha 0.0 xcenter 82

    hide hina with Dissolve(0.25)

    pause 0.25
    hide fumi with None

    show rin:
        "rin z3 1 lg pyjama c" with Dissolve(0.25)
        xcenter 842
        easein 0.25 xcenter 512

    voice "RIN_0587"
    rin "\"If Hina's gonna sleep with Rapha, I'm gonna sleep with Fumi in my arms!\""

    show rin:
        "rin z3 1 lg pyjama c flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 412

    play sound se116a

    "Rin made to slip into Fumi's bed."

    hide rin with None

    $ side_image = "fumi 2 side pyjama d"

    voice "FUM_0570"
    fumi "\"Umm...\""

    show hina 3 lg light pyjama h with dict_dissolve_25

    voice "HIN_0756"
    hina "\"No you don't!\""

    play sound se118c

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    "Hina threw a pillow right at Rin."

    camera
    with None

    show rin z3 1 lg pyjama j behind hina with Dissolve(0.25)
    show rin:
        ShakeNo

    voice "RIN_0588"
    rin "\"Ugh...\""

    show rin:
        "rin z3 1 lg pyjama j flat"
        alpha 1.0 ycenter 994 xoffset 0 yoffset 0
        easeout 0.5 alpha 0.0 ycenter 1094
    pause 0.5

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    $ side_image = "fumi 1 side pyjama b"

    voice "FUM_0571"
    fumi "\"Okay, I'm turning off the lights.\""

    play sound2 se025a

    stop music fadeout 5.0

    scene bg02da with Dissolve(0.25)
    pause 1.25

    "........."

    "......"

    show hina 3 lg dark pyjama i with Dissolve(0.25)

    voice "HIN_0757"
    hina "\"...So soft and warm...\""

    voice "HIN_0758"
    hina "\"It smells... like Fumi...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
