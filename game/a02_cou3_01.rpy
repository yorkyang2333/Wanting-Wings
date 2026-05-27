label a02_cou3_01:

    scene bg01ba with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show rin 1 lg school a at pos_r
    show fumi 1 lg school d at pos_l
    with Dissolve(0.25)

    show fumi:
        ShakeTameiki

    voice "FUM_0425"
    fumi "\"Whew, it's later than I thought it'd be.\"" id a02_cou3_01_d78609a0

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi put her bag down and sighed."

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0474"
    rin "\"Hina's not back yet, though. We made it.\"" id a02_cou3_01_6a751922

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0426"
    fumi "\"Oh, we should go ask Sachiko for her help on the day of the party.\"" id a02_cou3_01_1591c116

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0475"
    rin "\"We've gotta borrow her computer, too. Though there's no rush on that, I guess.\"" id a02_cou3_01_2e41f997

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0427"
    fumi "\"So I guess we can take a break now.\"" id a02_cou3_01_a275ff2a

    show rin:
        "rin 1 lg school d" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0476"
    rin "\"Alright, that marks the end of Operation Present-Shopping for Hina Natsume's Birthday!\"" id a02_cou3_01_b89fd734

    show rin 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0428"
    fumi "\"Ahaha, this is a rare display of energy from you.\"" id a02_cou3_01_1471567b

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0477"
    rin "\"It's just the first time I've done something like this, with the party and the presents and stuff. I know I'm acting kinda weird about it.\"" id a02_cou3_01_69342502

    show fumi 1 lg school c with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "FUM_0429"
    fumi "\"I understand! It's a lot of fun, isn't it?!\"" id a02_cou3_01_4a0a79a7

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg school e with dict_dissolve_25

    voice "RIN_0478"
    rin "\"I wonder if it's okay for me to be so excited when it isn't even my party.\"" id a02_cou3_01_8601c930

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0430"
    fumi "\"It's perfectly fine. We should all enjoy it.\"" id a02_cou3_01_73b66fff

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0479"
    rin "\"Do you think she'll like the present?\"" id a02_cou3_01_40ea8112

    "Rin looked worriedly at the bag in her hand."

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0431"
    fumi "\"Yes, I'm sure she will!\"" id a02_cou3_01_1c3aa44d

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0480"
    rin "\"I hope so...\"" id a02_cou3_01_56d1693e

    "They heard Hina's voice from the hallway."

    show fumi:
        "fumi 2 lg school d" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0432"
    fumi "\"Oh, she's home. Hide the present, hide the present!\"" id a02_cou3_01_3b0f0656

    show fumi 2 lg school d:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0481"
    rin "\"Right.\"" id a02_cou3_01_fc9fbc0d

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
