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
    hina "\"Ah, I know this song! ♪Hnn, nya nya nyaaa!\""

    "She'd been like this every break period today."

    play sound se555

    show hina:
        "hina 1 sm school c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0936"
    hina "\"Thank you sooo much, guys!\""

    show hina 1 sm school -headphones c:
        xoffset 0 yoffset 0
    with None

    "Hina took her headphones off and turned to face the other two, smiling from ear to ear."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0673"
    fumi "\"You're very welcome. We're just happy to see you happy.\""

    show rin 1 sm school d with dict_dissolve_25

    voice "RIN_0758"
    rin "\"Hah hah hah! Hina seems very happy with her present from Mom and Dad.\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0937"
    hina "\"Mom and Dad who—speaking of which!\""

    play sound se105b_120

    show hina 1 sm school f:
        xoffset 0 yoffset 0
        ShakeYes

    "Hina slammed her hands down on her desk and pointed straight at Rin."

    show hina 1 sm school j:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "HIN_0938"
    hina "\"I will not allow it!\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0759"
    rin "\"Wh-What's this about?\""

    show hina 1 sm school e with dict_dissolve_25

    voice "HIN_0939"
    hina "\"I won't allow any deviancy in that room as long as I live!\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0760"
    rin "\"Deviancy? There was nothing of the sort... What, were you jealous?\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0940"
    hina "\"No! I'm worried about Asou!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0674"
    fumi "\"Umm... what are we talking about?\""

    "Fumi slowly raised a hand when her name came up in the conversation."

    show hina 1 sm school l
    show rin 1 sm school e
    with dict_dissolve_25

    $ voice2("hina","HIN_0941","rin","RIN_0761")
    hina_rin "\"Huh?\""

    "The two of them both turned to her."

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0942"
    hina "\"Last night! In our room! Rin...!\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0675"
    fumi "\"Last night? In our room? Ogata...?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0762"
    rin "\"Do you... not remember?\""

    voice "FUM_0676"
    fumi "\"What happened?\""

    "Fumi cocked her head, a blank look on her face."

    show rin 1 sm school d with dict_dissolve_25

    voice "RIN_0763"
    rin "\"Who knows? I sure couldn't tell you!\""

    show hina:
        "hina 1 sm school l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0943"
    hina "\"Ah, Rin! Don't play dumb!\""

    show hina 1 sm school l:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0764"
    rin "\"Don't you feel bad for Asou, harping on and on about mistakes made under the influence?\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0944"
    hina "\"I'm 'harping' about you, not Asou!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school g with dict_dissolve_25

    voice "FUM_0677"
    fumi "\"Hmm?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
