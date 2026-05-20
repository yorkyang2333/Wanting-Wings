label a04_cou2_10:

    scene white with Dissolve(0.5)
    pause 1.5

    scene bg06ca with Dissolve(0.375)
    pause 1.125

    play music bgm02

    play sound woodendoor

    show fumi:
        "fumi 1 sm school a flat"
        alpha 0.0 xcenter 152
        easein 0.5 alpha 1.0 xcenter 252
    pause 0.5

    show fumi 1 sm school a:
        alpha 1.0 xcenter 252
    with None

    voice "FUM_1087"
    fumi "\"May I come in?\""

    show rin 1 sm school e:
        xcenter 632
    show hina 1 sm school k at pos_r
    with Dissolve(0.25)

    voice "HIN_1474"
    hina "\"Oh, Asou.\""

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_1253"
    rin "\"I've cleared things up with the idiot.\""

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_1475"
    hina "\"I'm not an idiot!\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_1088"
    fumi "\"Ahaha, you're back to normal.\""

    "Fumi smiled, relieved to see them acting the same as always."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_1089"
    fumi "\"That's right. Sachiko gave me this.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_1476"
    hina "\"What is it, what is it?\""

    show rin:
        "rin 1 sm school b" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_1254"
    rin "\"Haah... It's your present.\""

    show rin 1 sm school b:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm school c" with Dissolve(0.25)
        ShakeJump

    voice "HIN_1477"
    hina "\"Woof!\""

    show hina 1 sm school c:
        xoffset 0 yoffset 0
    with None

    "Hina looked up at Rin and ran around her."

    show hina 1 sm school c with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_1255"
    rin "\"No! You have to wait until morning!\""

    show hina 1 sm school d with dict_dissolve_25

    voice "HIN_1478"
    hina "\"Nooo! I want it now! I want it now!\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_1090"
    fumi "\"Ogata?\""

    show rin:
        "rin 1 sm school i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1256"
    rin "\"Ah, fine, whatever!\""

    show rin 1 sm school i:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school c with dict_dissolve_25

    voice "HIN_1479"
    hina "\"Yay!\""

    scene white with Dissolve(0.5)
    pause 2.0

    scene ev14a with Dissolve(0.375)
    pause 1.625

    voice "RIN_1257"
    rin "\"Here.\""

    "What emerged from the package was—"

    voice "HIN_1480"
    hina "\"Huh? It's...\""

    voice "RIN_1258"
    rin "\"I got it specially made at an accessory store. They just finished it today, so I had Sachiko go and pick it up for me.\""

    voice "HIN_1481"
    hina "\"Is this a collar?!\""

    voice "RIN_1259"
    rin "\"It's a choker, you stupid pervert!\""

    voice "HIN_1482"
    hina "\"Put it on, put it on, Rin!\""

    voice "RIN_1260"
    rin "\"Yeah, yeah.\""

    play sound se116a

    "Rin fastened the choker on Hina's neck."

    voice "HIN_1483"
    hina "\"Now I belong to you, Rin!\""

    voice "RIN_1261"
    rin "\"Maybe if you run away again, I'll put a leash on it.\""

    voice "HIN_1484"
    hina "\"Can't breathe...\""

    window hide



    $ persistent.rin_hina_clear1 = True
    $ renpy.block_rollback()

    pause 1.0
    scene ed_b00 with Dissolve(0.75)
    pause 2.25
    show ed_b01 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 3.0

    scene white with Dissolve(0.75)
    pause 2.25

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
