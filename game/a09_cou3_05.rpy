label a09_cou3_05:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "The weekend ended, and Monday arrived."

    "First thing in the morning, there was a crowd around Fumi. All because of that magazine."

    "Some among the throng even had the offending magazine in hand."

    "The other three watched the spectacle from Rin's desk."

    show hina z4 2 lg school f
    show miyako z4 2 lg school a:
        xcenter 172
    show rin z4 2 lg school a:
        xcenter 852
    with dict_dissolve_25

    voice "2MI_0927"
    miyako "\"Lots of people saw it, I guess.\"" id a09_cou3_05_5cbc2614

    voice "2HI_1140"
    hina "\"Well, most Seiyou students go past the station. Mm, this magazine is probably pretty effective advertisement for the girls here, huh?\"" id a09_cou3_05_f1c3710c

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_0928"
    miyako "\"Is Asou's family's store really thriving?\"" id a09_cou3_05_6837648c

    show hina:
        "hina z4 2 lg school a" with Dissolve(0.25)
        4.0
        "hina z4 1 lg school k" with Dissolve(0.25)

    voice "2HI_1141"
    hina "\"Well, it is Valentine's season, so they'll probably be busy... Oh, they're asking for her autograph.\"" id a09_cou3_05_5e347282

    show hina z4 1 lg school k:
        pass
    with None

    "One of the crowd wanted Fumi to sign her magazine. Fumi said no, of course."

    show rin z4 1 lg school f with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2RI_1183"
    rin "\"We can't have this... They gotta go through me for that stuff. I get where they're coming from, though.\"" id a09_cou3_05_a9f2e702

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin slowly took a magazine out of her bag."

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_1142"
    hina "\"...You made her sign yours?\"" id a09_cou3_05_77559ca1

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1184"
    rin "\"Well, this is, in essence, Fumi Asou's first photo collection, 'Le Chocolat Chocolat.'\"" id a09_cou3_05_70f25d08

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0929"
    miyako "\"That's the name of the shop.\"" id a09_cou3_05_119fe758

    show rin z4 1 lg school f with dict_dissolve_25

    voice "2RI_1185"
    rin "\"Heheh.\"" id a09_cou3_05_4fe951f2

    "All the while, the girls were asking Fumi things, and she was shrinking back from them. And Rin just watched this smugly."

    voice "2HI_1143"
    hina "\"Why are you so smug?\"" id a09_cou3_05_6c559684

    show rin:
        "rin z4 2 lg school c" with Dissolve(0.25)
        3.5
        "rin z4 1 lg school d" with Dissolve(0.25)

    voice "2RI_1186"
    rin "\"Man, that Asou's so cute~ Wonder if she's going out with anyone~? Oh, she's going out with me~♪\"" id a09_cou3_05_c85b39ac

    show rin z4 1 lg school d:
        pass
    with None

    "Rin poked her head and stuck her tongue out."

    show hina:
        "hina z4 1 lg school h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_1144"
    hina "\"Hahh... whatever.\"" id a09_cou3_05_f04d364e

    show hina z4 1 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school f with dict_dissolve_25

    voice "2RI_1187"
    if persistent.dpatch:
        rin "\"I wanna announce it at an assembly to the whole school!\"" id a09_cou3_05_f80a168d
    else:
        rin "\"I wanna announce it at an assembly to the whole campus!\"" id a09_cou3_05_fa735af6

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_1145"
    hina "\"Don't.\"" id a09_cou3_05_575f644a

    voice "2RI_1188"
    rin "\"No, maybe I'll put it on the side of a truck and drive around town!\"" id a09_cou3_05_a571aa00

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1146"
    hina "\"Seriously, don't.\"" id a09_cou3_05_fc849e6f

    show hina z4 1 lg school f:
        xoffset 0 yoffset 0
    with None

    "I wouldn't be surprised if she paid someone to do it."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared == 1:
        jump a09_comn_07
    elif routes_cleared >= 2:
        jump a09_cou4_02
    else:
        jump a09_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
