label a03_cou3_02:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    play sound se056b_100

    $ side_image = "fumi 2 side pyjama i"

    voice "FUM_0678"
    fumi "\"♪If the day's got a 0, it's 5 times the points, a super special point day!\"" id a03_cou3_02_9d8768e7

    stop sound fadeout 5.0

    "Fumi was doing the dishes, in a good mood."

    "Incidentally, the song she was (likely subconsciously) singing was the point day song often played at the supermarket she frequented."

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0765"
    rin "\".........\"" id a03_cou3_02_0ee7159b

    "Rin was stealing glances at her from the other room, pretending to read a book."

    $ side_image = "fumi 1 side pyjama e"

    voice "FUM_0679"
    fumi "\"Ah...!\"" id a03_cou3_02_abe3ce04

    stop music fadeout 1.0

    play sound se010a

    $ side_image = "fumi 1 side pyjama h"

    voice "FUM_0680"
    fumi "\"Ow...\"" id a03_cou3_02_c1f3111a

    "There was the sound of breaking glass and a small shout from Fumi."

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0766"
    rin "\"A-Asou?!\"" id a03_cou3_02_f1d85af9

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin jumped up."

    scene black with bg_effect_11
    pause 0.25

    scene bg02ca with bg_effect_11
    pause 0.5

    play music bgm02

    show fumi 1 lg pyjama h at pos_l
    show rin 2 lg pyjama glasses e at pos_r
    with Dissolve(0.25)

    show rin:
        ShakeYes

    voice "RIN_0767"
    rin "\"Don't worry about it, I'll clean it up.\"" id a03_cou3_02_60d7fa2d

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin said, picking up the shards of glass in the sink."

    voice "FUM_0681"
    fumi "\"Thank you. My hands slipped on the soap...\"" id a03_cou3_02_efa9c765

    "Fumi stood apologetically beside her."

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0768"
    rin "\"It's fine, it's fine. You're not hurt, are you?\"" id a03_cou3_02_b86bf566

    show fumi:
        "fumi 1 lg pyjama d" with Dissolve(0.25)
        ShakeTameiki

    voice "FUM_0682"
    fumi "\"I just cut myself a little.\"" id a03_cou3_02_bcfa11ea

    show fumi 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0769"
    rin "\"Whoa! A-Are you okay? Do we need to stop the bleeding?\"" id a03_cou3_02_19fd3d5f

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    voice "FUM_0683"
    fumi "\"Oh, it's just a little nick. Doesn't even need a band-aid.\"" id a03_cou3_02_5c5584b0

    "She showed Rin the little bead of blood on her finger."

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0770"
    rin "\"...Good.\"" id a03_cou3_02_7aca4c1c

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "FUM_0684"
    fumi "\"Sorry for worrying you.\"" id a03_cou3_02_8f996ff6

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0771"
    rin "\"Nah. I just didn't want your pretty little fingers getting scarred.\"" id a03_cou3_02_1ff41d97

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0685"
    fumi "\"It looks like I'm not the angel.\"" id a03_cou3_02_96f373e0

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0772"
    rin "\"Huh? What do you mean?\"" id a03_cou3_02_76f4fea9

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "FUM_0686"
    fumi "\"Your way to find out. You said our blood would try to get away if it sensed danger, right?\"" id a03_cou3_02_0f409d61

    show rin 2 lg pyjama glasses e with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0773"
    rin "\"Oh! That was actually how to spot an alien, not an angel.\"" id a03_cou3_02_eeec4bf1

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0687"
    fumi "\"Really?\"" id a03_cou3_02_538ccfe2

    voice "RIN_0774"
    rin "\"There's a scene like that in this old science fiction movie.\"" id a03_cou3_02_e990bda1

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0688"
    fumi "\"I see. You're full of trivia, aren't you, Ogata?\"" id a03_cou3_02_c580224d

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0775"
    rin "\"You don't need to be all impressed. I'm sorry for talking nonsense... Anyway, gimme your finger.\"" id a03_cou3_02_5a40279b

    hide rin with Dissolve(0.25)

    show fumi:
        "fumi 1 lg pyjama e" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 512
    pause 0.25

    show fumi 1 lg pyjama e:
        xcenter 512
    with None

    voice "FUM_0689"
    fumi "\"Oh...\"" id a03_cou3_02_45228cf2

    "Rin took Fumi's finger and put it in her mouth."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "RIN_0776"
    rin "\"Mmh... does that sting?\"" id a03_cou3_02_a8e5245e

    show fumi 1 lg pyjama h with Dissolve(0.25)
    show fumi:
        ShakeNo

    voice "FUM_0690"
    fumi "\"......\"" id a03_cou3_02_936f9e2b

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi shook her head."

    $ side_image = "rin 2 side pyjama glasses e"

    voice "RIN_0777"
    rin "\"Your fingers are so soft...\"" id a03_cou3_02_04de3102

    show fumi:
        "fumi 1 lg pyjama k" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0691"
    fumi "\"...Ah...\"" id a03_cou3_02_0286b2f6

    show fumi 1 lg pyjama k:
        xoffset 0 yoffset 0
    with None

    $ side_image = "rin 1 side pyjama glasses k"

    voice "RIN_0778"
    rin "\"They're so pretty, too... You should... be more careful... mh...\"" id a03_cou3_02_e760e0a3

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0692"
    fumi "\"...Th-Thank you...\"" id a03_cou3_02_50b3de5a

    "Rin drew back, a thread of saliva connecting her to Fumi's finger."

    show fumi:
        "fumi 2 lg pyjama h" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 252
    show rin 2 lg pyjama glasses b at pos_r with dict_dissolve_25
    pause 0.25

    show fumi 2 lg pyjama h:
        xcenter 252
    with None

    voice "RIN_0779"
    rin "\"...Asou...\"" id a03_cou3_02_03497a52

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "FUM_0693"
    fumi "\"...Y...Yes?\"" id a03_cou3_02_2465c13a

    "Their eyes were locked on each other's lips, and—"

    stop music fadeout 0.1

    play sound se001c

    show fumi 1 lg pyjama j
    show rin 1 lg pyjama glasses j
    with dict_dissolve_25

    camera:
        function LayerShake(20,20,0.25)
    $ persistent.layer_shaken = False

    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0945"
    hina "\"NO DEVIANCYYY!\"" id a03_cou3_02_be1302e0

    camera
    with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
