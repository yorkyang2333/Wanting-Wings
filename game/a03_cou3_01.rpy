label a03_cou3_01:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg04aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm school headphones c
    show rin 1 sm school c at pos_r2
    show fumi 1 sm school a at pos_l2
    with Dissolve(0.25)

    voice "HIN_0935"
    hina "\"Ah, I know this song! ♪Hnn, nya nya nyaaa!\"" id a03_cou3_01_490258d8

    "She'd been like this every break period today."

    play sound se555

    show hina:
        "hina 1 sm school c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0936"
    hina "\"Thank you sooo much, guys!\"" id a03_cou3_01_135a73a9

    show hina 1 sm school -headphones c:
        xoffset 0 yoffset 0
    with None

    "Hina took her headphones off and turned to face the other two, smiling from ear to ear."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0673"
    fumi "\"You're very welcome. We're just happy to see you happy.\"" id a03_cou3_01_5563c1bc

    show rin 1 sm school d with dict_dissolve_25

    voice "RIN_0758"
    rin "\"Hah hah hah! Hina seems very happy with her present from Mom and Dad.\"" id a03_cou3_01_5a6c168b

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0937"
    hina "\"Mom and Dad who—speaking of which!\"" id a03_cou3_01_0a45a440

    play sound se105b_120

    show hina 1 sm school f:
        xoffset 0 yoffset 0
        ShakeYes

    "Hina slammed her hands down on her desk and pointed straight at Rin."

    show hina 1 sm school j:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "HIN_0938"
    hina "\"I will not allow it!\"" id a03_cou3_01_b3705873

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0759"
    rin "\"Wh-What's this about?\"" id a03_cou3_01_7e98f977

    show hina 1 sm school e with dict_dissolve_25

    voice "HIN_0939"
    hina "\"I won't allow any deviancy in that room as long as I live!\"" id a03_cou3_01_27499fae

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0760"
    rin "\"Deviancy? There was nothing of the sort... What, were you jealous?\"" id a03_cou3_01_b41679cf

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0940"
    hina "\"No! I'm worried about Asou!\"" id a03_cou3_01_5e1c3dbc

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0674"
    fumi "\"Umm... what are we talking about?\"" id a03_cou3_01_8f9cdee9

    "Fumi slowly raised a hand when her name came up in the conversation."

    show hina 1 sm school l
    show rin 1 sm school e
    with dict_dissolve_25

    $ voice2("hina","HIN_0941","rin","RIN_0761")
    hina_rin "\"Huh?\""

    "The two of them both turned to her."

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0942"
    hina "\"Last night! In our room! Rin...!\"" id a03_cou3_01_63701358

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0675"
    fumi "\"Last night? In our room? Ogata...?\"" id a03_cou3_01_247465b8

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0762"
    rin "\"Do you... not remember?\"" id a03_cou3_01_16d96862

    voice "FUM_0676"
    fumi "\"What happened?\"" id a03_cou3_01_7c506750

    "Fumi cocked her head, a blank look on her face."

    show rin 1 sm school d with dict_dissolve_25

    voice "RIN_0763"
    rin "\"Who knows? I sure couldn't tell you!\"" id a03_cou3_01_9f1c3992

    show hina:
        "hina 1 sm school l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0943"
    hina "\"Ah, Rin! Don't play dumb!\"" id a03_cou3_01_fd6bdca3

    show hina 1 sm school l:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0764"
    rin "\"Don't you feel bad for Asou, harping on and on about mistakes made under the influence?\"" id a03_cou3_01_70e083ae

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0944"
    hina "\"I'm 'harping' about you, not Asou!\"" id a03_cou3_01_914c4657

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school g with dict_dissolve_25

    voice "FUM_0677"
    fumi "\"Hmm?\"" id a03_cou3_01_b37019f1

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
