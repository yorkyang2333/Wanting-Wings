label a04_cou3_01:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 lg pyjama d with Dissolve(0.25)

    voice "HIN_1485"
    hina "\"Are you fighting?\"" id a04_cou3_01_0b41e909

    show hina:
        xcenter 512
        easein 0.25 xcenter 172
    show rin:
        "rin 1 lg pyjama e flat"
        alpha 0.0 xcenter 852
        linear 0.25 alpha 1.0
    show fumi 1 lg pyjama e:
        "fumi 1 lg pyjama e flat"
        alpha 0.0 xcenter 512
        linear 0.25 alpha 1.0

    $ voice2("rin","RIN_1262","fumi","FUM_1091")
    rin_fumi "\"Huh?\""

    show hina 1 lg pyjama d:
        xcenter 172
    show rin 1 lg pyjama e:
        alpha 1.0 xcenter 852
    show fumi 1 lg pyjama e:
        alpha 1.0 xcenter 512
    with None

    "The two of them both exclaimed at Hina's unexpected question."

    show rin:
        "rin 1 lg pyjama g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1263"
    rin "\"Wh-Why do you say that?\"" id a04_cou3_01_1ed15410

    show rin 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_1486"
    hina "\"I'm not sure what it is exactly, but the two of you seem kind of distant lately.\"" id a04_cou3_01_a17341e1

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_1092"
    fumi "\"That's not true... right?\"" id a04_cou3_01_c8c48f45

    voice "RIN_1264"
    rin "\"Y-Yeah, of course it isn't... right?\"" id a04_cou3_01_99cba650

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_1487"
    hina "\".........\"" id a04_cou3_01_05864c2f

    show rin 1 lg pyjama d with dict_dissolve_25

    voice "RIN_1265"
    rin "\"S-See, we get along perfectly fine!\"" id a04_cou3_01_8904cc3e

    play sound se118a

    show fumi:
        "fumi 1 lg pyjama e" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 542

    voice "FUM_1093"
    fumi "\"Aah!\"" id a04_cou3_01_7b43ff12

    "Rin put a hand around Fumi's shoulder in an exaggerated manner."

    show hina 1 lg pyjama e with dict_dissolve_25

    voice "HIN_1488"
    hina "\"...Yeah, something's weird.\"" id a04_cou3_01_2ec1095c

    show rin 1 lg pyjama e with dict_dissolve_25

    voice "RIN_1266"
    rin "\"Wh-Why?\"" id a04_cou3_01_5b4f9def

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_1489"
    hina "\"Well, before, you would've pushed Asou down and been all like, 'Shouldn't you be in bed by now, kiddo?' or something like that.\"" id a04_cou3_01_5d55fea7

    show rin:
        "rin 1 lg pyjama i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1267"
    rin "\"Ugh...\"" id a04_cou3_01_5c6ea42d

    show rin 1 lg pyjama i:
        xoffset 0 yoffset 0
    with None

    "Her past actions were catching up to her."

    "Now that they'd crossed a line, maybe it was somehow harder to do such things in jest."

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1268"
    rin "\"Umm... aren't you tired?\"" id a04_cou3_01_61f8fc2b

    show hina 1 lg pyjama e with dict_dissolve_25

    voice "HIN_1490"
    hina "\"Nope. It's only 8.\"" id a04_cou3_01_1a65ae02

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_1269"
    rin "\"...Right.\"" id a04_cou3_01_f3fd0405

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_1094"
    fumi "\"A-Anyway, we're not fighting~\"" id a04_cou3_01_2c7c99e5

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_1491"
    hina "\"Well, alright...\"" id a04_cou3_01_d2e5bb5d

    play sound se555

    show hina:
        "hina 2 lg pyjama headphones e" with Dissolve(0.25)
        ShakeYes

    "Hina said, putting her headphones on and sinking into her music."

    show hina 2 lg pyjama headphones e:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama h
    show rin 2 lg pyjama b
    with Dissolve(0.25)

    $ voice2("rin","RIN_1270","fumi","FUM_1095")
    rin_fumi "\".........\""

    "Rin and Fumi exchanged a glance."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
