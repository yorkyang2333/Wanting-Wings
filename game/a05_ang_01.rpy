label a05_ang_01:

    scene white with Dissolve(0.5)
    pause 1.5

    scene bg08cb_grayscale with Dissolve(0.375)
    pause 1.125

    play music bgm02

    play sound [se585,se585]
    pause 0.5
    play sound2 se585

    $ voice3("hina","HIN_1538","rin","RIN_1478","fumi","FUM_1300")
    hina_rin_fumi "\"Merry Christmas!\""

    scene ev03a with bg_effect_25_1000

    voice "SYO_0184"
    sachiko "\"Phew...\""

    scene ev03b with bg_effect_25_1000

    voice "SYO_0185"
    sachiko "\"...?\""

    voice "SYO_0186"
    sachiko "\"Welcome back. It's a nice Eve, isn't it?\""

    scene ev03c with Dissolve(0.75)
    pause 3.75

    scene white with Dissolve(0.75)
    pause 2.25

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a05_ang_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
