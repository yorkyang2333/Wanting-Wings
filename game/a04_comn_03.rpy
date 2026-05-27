label a04_comn_03:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg05ba with Dissolve(0.25)
    pause 0.75

    play music bgm01

    play sound2 se585

    show sachiko 1 sm outfit e:
        xcenter 128
    with dict_dissolve_25

    show hina:
        "hina 1 sm school_scarf l flat"
        alpha 0.0 xcenter 732
        easein 0.5 alpha 1.0 xcenter 632
    show rin behind hina:
        "rin 1 sm school_scarf e flat"
        alpha 0.0 xcenter 876
        easein 0.5 alpha 1.0 xcenter 776
    show fumi behind hina:
        "fumi 1 sm school_scarf j flat"
        alpha 0.0 xcenter 1040
        easein 0.5 alpha 1.0 xcenter 940

    voice "FUM_0831"
    fumi "\"Aaah?!\"" id a04_comn_03_5f0f5b63

    show hina 1 sm school_scarf l:
        alpha 1.0 xcenter 632
    show rin 1 sm school_scarf e:
        alpha 1.0 xcenter 776
    show fumi 1 sm school_scarf j:
        alpha 1.0 xcenter 940
    with None

    "An obnoxious popping sound greeted the three girls as they came through the door."

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "SYO_0137"
    sachiko "\"It's Christmas Eve Eve Eve Eve... Four sleeps 'til Christmas♪\"" id a04_comn_03_945a5609

    show fumi 1 sm school_scarf h
    show hina 1 sm school_scarf l
    with dict_dissolve_25

    voice "HIN_0989"
    hina "\"You're excited!\"" id a04_comn_03_9bdafc1f

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "RIN_0933"
    rin "\"It's a little early for party poppers, isn't it?\"" id a04_comn_03_2ad94494

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0138"
    sachiko "\"I just can't wait, you know?\"" id a04_comn_03_c57ac753

    "Sachiko plucked ribbons from the party popper out of the girls' hair."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0139"
    sachiko "\"By the way, do you guys have plans for Christmas yet?!\"" id a04_comn_03_832eda4b

    show hina 1 sm school_scarf k
    show rin 1 sm school_scarf i
    show fumi 1 sm school_scarf d
    with dict_dissolve_25

    $ voice3("hina","HIN_0990","rin","RIN_0934","fumi","FUM_0832")
    hina_rin_fumi "\"Umm...\""

    "The three exchanged a glance."

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0140"
    sachiko "\"What is it? You're not gonna be all alone, are you?\"" id a04_comn_03_c9dae0e2

    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "HIN_0991"
    hina "\"No, I don't think so.\"" id a04_comn_03_5dfdecd6

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0833"
    fumi "\"We're throwing a party in our room.\"" id a04_comn_03_d572263d

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "RIN_0935"
    rin "\"And what are your plans?\"" id a04_comn_03_8f79e0ed

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "SYO_0141"
    sachiko "\"Hey, that's not the sort of question you ask a woman who's my age.\"" id a04_comn_03_454f96f6

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "RIN_0936"
    rin "\"You asked us.\"" id a04_comn_03_1e24b87c

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0142"
    sachiko "\"I do have plans! ......Probably.\"" id a04_comn_03_16890ac0

    show hina 1 sm school_scarf l with dict_dissolve_25

    voice "HIN_0992"
    hina "\"Probably? What's that supposed to mean?\"" id a04_comn_03_b9a8ea40

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0143"
    sachiko "\"Well, if they fall through, I'll just crash your guys' party.\"" id a04_comn_03_45f0150b

    show hina 1 sm school_scarf d
    show rin 1 sm school_scarf g
    show fumi 1 sm school_scarf e
    with dict_dissolve_25

    $ voice3("hina","HIN_0993","rin","RIN_0937","fumi","FUM_0834")
    hina_rin_fumi "\"What?!\""

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "SYO_0144"
    sachiko "\"Well, you don't have to harmonize about it.\"" id a04_comn_03_7136b97c

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_03
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_04
    else:
        jump a04_cou1_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
