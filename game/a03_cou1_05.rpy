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
    rin "\"Ugh... my neck hurts...\"" id a03_cou1_05_f4c16e7f

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0556"
    fumi "\"It's probably because you were reading in such a weird position. Do you want me to rub your shoulders?\"" id a03_cou1_05_9fc2cfa6

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0576"
    rin "\"Nah. But I think it'd help if I could rub your boobs.\"" id a03_cou1_05_3c4169fc

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0557"
    fumi "\"Oh~ I don't think that's going to happen.\"" id a03_cou1_05_8c110e55

    show rin:
        "rin z3 1 lg pyjama i" with Dissolve(0.25)
        ShakeNo

    voice "RIN_0577"
    rin "\"Stingy~\"" id a03_cou1_05_a2dbb93b

    show rin z3 1 lg pyjama i:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0740"
    hina "\"Hey, Fumi?\"" id a03_cou1_05_79ffa1d0

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0558"
    fumi "\"Yes?\"" id a03_cou1_05_166636b8

    show hina z3 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0741"
    hina "\"Can I borrow one of your stuffed animals?\"" id a03_cou1_05_0b1576b1

    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0559"
    fumi "\"One of my stuffed animals?\"" id a03_cou1_05_8ea240c6

    show hina:
        "hina z3 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0742"
    hina "\"Yeah...\"" id a03_cou1_05_0a8b4a5a

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
    rin "\"Oh, Hina, we're still your friends!\"" id a03_cou1_05_95af8257

    show hina z3 2 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0743"
    hina "\"Wh-What?\"" id a03_cou1_05_ceb1c354

    "Rin suddenly threw her arms around Hina, surprising her."

    show rin z3 2 lg pyjama e with dict_dissolve_25

    voice "RIN_0579"
    rin "\"You poor thing, you've been lonely, haven't you? We haven't been giving you enough attention lately...\"" id a03_cou1_05_2f2560fa

    show fumi z3 2 lg pyjama d
    show hina z3 1 lg pyjama f
    with Dissolve(0.25)

    show hina:
        ShakeJump

    voice "HIN_0744"
    hina "\"That's not it, stupid!\"" id a03_cou1_05_9a097f66

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 2 lg pyjama d with dict_dissolve_25

    voice "RIN_0580"
    rin "\"I promise we'll start taking you for walks—\"" id a03_cou1_05_0d8c8787

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
    rin "\"Ugh... you never hold back, do you?\"" id a03_cou1_05_502d3bf1

    show hina z3 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0745"
    hina "\"Shut up, Rin.\"" id a03_cou1_05_cb0f6ac0

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0560"
    fumi "\"Umm, which one would you like?\"" id a03_cou1_05_c86af205

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0746"
    hina "\"Which one's your favorite, Fumi?\"" id a03_cou1_05_b9c149f2

    show fumi z3 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0561"
    fumi "\"Hmm... I love all of them, but... I sleep with Rapha the most.\"" id a03_cou1_05_f926bfd5

    show hina z3 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0747"
    hina "\"Then that one, please.\"" id a03_cou1_05_aadbfe79

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0562"
    fumi "\"Here you go.\"" id a03_cou1_05_3d81e63a

    "Hina accepted Rapha gingerly."

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0582"
    rin "\"...Suddenly feels like a house of ill repute in here.\"" id a03_cou1_05_c2c80a21

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeSide
        ShakeSide

    voice "HIN_0748"
    hina "\"Gaaah!!\"" id a03_cou1_05_517a70f5

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0563"
    fumi "\"What did you want a stuffed animal for all of a sudden, though?\"" id a03_cou1_05_18f14cba

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0749"
    hina "\"W-Well, remember how you said you sleep better with one, Fumi?\"" id a03_cou1_05_ae083f43

    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0564"
    fumi "\"Oh? Are you having trouble sleeping?\"" id a03_cou1_05_e3afdddf

    show hina z3 1 lg pyjama d with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_0750"
    hina "\"N-No, not really, but... oh, yeah, my eyes are just wide open from the café au lait I had earlier.\"" id a03_cou1_05_498c0982

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0583"
    rin "\"Aww, poor widdle baby. Want me to sing you a lullaby, then?\"" id a03_cou1_05_91844f10

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0751"
    hina "\"No! And stop talking to me like I'm a baby!\"" id a03_cou1_05_c33c1a37

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0584"
    rin "\"If you can't sleep without a stuffed animal, you're a widdle baby.\"" id a03_cou1_05_eaa03140

    show fumi z3 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0565"
    fumi "\"But they say it reduces anxiety and stress when you sleep with a stuffed animal.\"" id a03_cou1_05_f9d31c44

    show fumi z3 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0566"
    fumi "\"The softness and warmth probably helps you relax.\"" id a03_cou1_05_4c358c58

    show rin z3 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0585"
    rin "\"Some people sleep with body pillows too, yeah.\"" id a03_cou1_05_fbaa8f42

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0567"
    fumi "\"Mhm, mhm.\"" id a03_cou1_05_09ef1109

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0752"
    hina "\"I'll borrow Rapha for the night, then.\"" id a03_cou1_05_76a18880

    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0586"
    rin "\"Don't get your drool on her.\"" id a03_cou1_05_08ed09b4

    show hina z3 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0753"
    hina "\"I won't!\"" id a03_cou1_05_cbdf2235

    show fumi z3 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0568"
    fumi "\"Heheh, it's okay, I'll just give her a bath if you do.\"" id a03_cou1_05_0d561067

    show hina z3 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0754"
    hina "\"I won't... probably.\"" id a03_cou1_05_a1dff67e

    "Hina took Rapha to her bed."

    show hina:
        "hina z3 1 lg pyjama d flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612
    pause 0.5

    hide hina with None
    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0569"
    fumi "\"Good night. Sweet dreams.\"" id a03_cou1_05_f9dac0c5

    show hina 3 lg light pyjama c with dict_dissolve_25

    voice "HIN_0755"
    hina "\"Night.\"" id a03_cou1_05_932045b9

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
    rin "\"If Hina's gonna sleep with Rapha, I'm gonna sleep with Fumi in my arms!\"" id a03_cou1_05_30908d8b

    show rin:
        "rin z3 1 lg pyjama c flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 412

    play sound se116a

    "Rin made to slip into Fumi's bed."

    hide rin with None

    $ side_image = "fumi 2 side pyjama d"

    voice "FUM_0570"
    fumi "\"Umm...\"" id a03_cou1_05_5d70d18e

    show hina 3 lg light pyjama h with dict_dissolve_25

    voice "HIN_0756"
    hina "\"No you don't!\"" id a03_cou1_05_9592aab4

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
    rin "\"Ugh...\"" id a03_cou1_05_d3027246

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
    fumi "\"Okay, I'm turning off the lights.\"" id a03_cou1_05_158aa71d

    play sound2 se025a

    stop music fadeout 5.0

    scene bg02da with Dissolve(0.25)
    pause 1.25

    "........."

    "......"

    show hina 3 lg dark pyjama i with Dissolve(0.25)

    voice "HIN_0757"
    hina "\"...So soft and warm...\"" id a03_cou1_05_c7243006

    voice "HIN_0758"
    hina "\"It smells... like Fumi...\"" id a03_cou1_05_22408c75

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
