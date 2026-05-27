label a03_cou1_01:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg04aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm school g at pos_r
    show fumi 1 sm school e
    show rin 1 sm school b at pos_l
    with Dissolve(0.25)

    show hina:
        ShakeYes

    voice "HIN_0682"
    hina "\"Achoo!\"" id a03_cou1_01_912419fc

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school h with dict_dissolve_25

    voice "FUM_0506"
    fumi "\"Are you okay? You didn't catch a cold, did you...?\"" id a03_cou1_01_0a369f0c

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0683"
    hina "\"Mmm~ I dunno.\"" id a03_cou1_01_97f69e8b

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0556"
    rin "\"......\"" id a03_cou1_01_d3cde3a2

    show hina 1 sm school j with dict_dissolve_25

    voice "HIN_0684"
    hina "\"I'm not an idiot!\"" id a03_cou1_01_84092e16

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0557"
    rin "\"I didn't say anything.\"" id a03_cou1_01_11a5b2c0

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0685"
    hina "\"You were saying it with your eyes.\"" id a03_cou1_01_cbb38afc

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0558"
    rin "\"Maybe you caught a chill 'cause you're always sleeping with your stomach exposed.\"" id a03_cou1_01_5c4aed75

    show hina 1 sm school j with dict_dissolve_25

    voice "HIN_0686"
    hina "\"I am not.\"" id a03_cou1_01_30edfbab

    show fumi 1 sm school k with dict_dissolve_25

    voice "FUM_0507"
    fumi "\"Is it because we took too long last night...?\"" id a03_cou1_01_d0324267

    show rin 1 sm school e with dict_dissolve_25

    "\"Last night?\" said Rin's face."

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0687"
    hina "\"I-It's noth... achoo!\"" id a03_cou1_01_d1d0f040

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school h with dict_dissolve_25

    voice "FUM_0508"
    fumi "\"Well, we're done with exams, so you should get to bed early tonight.\"" id a03_cou1_01_7d4279b4

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0688"
    hina "\"Yeah. Thanks.\"" id a03_cou1_01_8827fe91

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0560"
    rin "\"Wanna go to the Firtree Clinic before it gets too bad?\"" id a03_cou1_01_295bf34c

    show hina:
        "hina 1 sm school k" with Dissolve(0.25)
        ShakeNo
        1.0
        "hina 1 sm school g" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0689"
    hina "\"No, it's not that—Wait, the Firtree Clinic is an animal hospital!\"" id a03_cou1_01_65a5ab1d

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
