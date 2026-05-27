label a04_cou3_04:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 1 lg school k
    show fumi 2 lg school j:
        xcenter 272
    with Dissolve(0.25)

    voice "RIN_1330"
    rin "\"Mmh... chp.\"" id a04_cou3_04_317161a6

    show fumi:
        "fumi 1 lg school k" with Dissolve(0.25)
    show rin:
        "rin 2 lg school g" with Dissolve(0.25)
        xcenter 512
        easein 1.0 xcenter 772

    voice "FUM_1164"
    fumi "\"Ahh...\"" id a04_cou3_04_fc19e7e4

    show rin 2 lg school g:
        xcenter 772
    with None

    "Sweet sighs escaped from their parted lips."

    show fumi 1 lg school i behind rin with dict_dissolve_25

    voice "FUM_1165"
    fumi "\"Haahh... You get better at kissing every time.\"" id a04_cou3_04_2b4b7285

    show rin 2 lg school e with dict_dissolve_25

    voice "RIN_1331"
    rin "\"I-I do?\"" id a04_cou3_04_5d60f998

    "........."

    "Today, once again, they were having a short tryst as they waited for Hina to return from the faculty room."

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_1332"
    rin "\"Hey, Fumi? Can I ask you something I've been wanting to know for a while?\"" id a04_cou3_04_eb4cae03

    show fumi 1 lg school e with dict_dissolve_25

    voice "FUM_1166"
    fumi "\"Sure, what is it?\"" id a04_cou3_04_8b50fdbb

    show rin 2 lg school e with dict_dissolve_25

    voice "RIN_1333"
    rin "\"Would you rather be a top or a bottom?\"" id a04_cou3_04_7bbaed07

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_1167"
    fumi "\"Huh?\"" id a04_cou3_04_a98382b7

    "Fumi's face was blank."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_1168"
    fumi "\"Well, I like having a bottom bunk right now.\"" id a04_cou3_04_dc2add90

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1334"
    rin "\"Ah, that's not what I mean.\"" id a04_cou3_04_ba23b941

    "Rin found herself embarrassed by Fumi's innocent answer."

    show rin 2 lg school c with dict_dissolve_25

    voice "RIN_1335"
    rin "\"It's like, about... whether you enjoy being in charge during... you know.\"" id a04_cou3_04_aef4ae92

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_1169"
    fumi "\"Oh, I see.\"" id a04_cou3_04_b8b4b27e

    "Comprehension."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_1170"
    fumi "\"Hmm~\"" id a04_cou3_04_f4345351

    "Fumi gave it some thought, and..."

    show fumi:
        "fumi 2 lg school b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_1171"
    fumi "\"Whatever you prefer, Rin.\"" id a04_cou3_04_caf98a32

    show fumi 2 lg school b:
        xoffset 0 yoffset 0
    with None

    "She lifted her skirt in a curtsy."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_1172"
    fumi "\"Do you want to be in charge, Rin?\"" id a04_cou3_04_349458d8

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1336"
    rin "\"Me? I... I guess so.\"" id a04_cou3_04_60e94756

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_1173"
    fumi "\"I see...\"" id a04_cou3_04_0cf20355

    show rin 2 lg school e with dict_dissolve_25

    voice "RIN_1337"
    rin "\"I just feel like you're so much more of a girl than me, so I have to do that.\"" id a04_cou3_04_2991366a

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_1174"
    fumi "Oh? I think you're plenty feminine. Much more so than me.\"" id a04_cou3_04_46e43321

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1338"
    rin "\"You think so...?\"" id a04_cou3_04_04db1a28

    "Rin's face said she didn't agree."

    show fumi 1 lg school f with dict_dissolve_25

    voice "FUM_1175"
    fumi "\"You were pretty incredible that night.\"" id a04_cou3_04_8b919d48

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1339"
    rin "\"Inc—?!\"" id a04_cou3_04_9634909f

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None

    "Rin went speechless with shame at the memory."

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1176"
    fumi "\"When I tried to sleep after that, my sheets were soaked—\"" id a04_cou3_04_1eec8d7d

    show rin:
        ShakeSide
        0.5
        ShakeSide

    voice "RIN_1340"
    rin "\"Wah, waaah...\"" id a04_cou3_04_b4acbfd3

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin covered her face."

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_1177"
    fumi "\"I had to put a towel down—\"" id a04_cou3_04_4c79ebcd

    show rin:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_1341"
    rin "\"Waaah, I'm sorry, I'm sorry!!\"" id a04_cou3_04_757773f9

    show rin:
        "rin 1 lg school j flat"
        alpha 1.0 xcenter 772 xoffset 0 yoffset 0
        easeout 0.25 alpha 0.0 xcenter 872

    play sound se137a

    "Rin yelled and ran off."

    hide rin with None
    show fumi 1 lg school e with dict_dissolve_25

    voice "FUM_1178"
    fumi "\"Ah, Rin?\"" id a04_cou3_04_6efc59bb

    play sound2 se000c

    "Rin ran straight out of the classroom."

    show hina:
        "hina 1 lg school k flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772
    pause 0.5

    voice "HIN_1499"
    hina "\"What was that?\"" id a04_cou3_04_8febbf70

    "Hina came in in her place, looking rather bewildered."

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1179"
    fumi "\"Ahaha, hahaha.\"" id a04_cou3_04_c542662b

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_cou3_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
