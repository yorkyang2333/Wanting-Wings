label a05_ang_12:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_12:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    play music bgm05

    scene ev02b_grayscale with bg_effect_08_1000

    voice "FUM_0605"
    fumi "\"...The truth is, I didn't need the feather anymore.\""

    voice "FUM_0606"
    fumi "\"Since you said you'd believe with me.\""

    voice "FUM_0607"
    fumi "\"I still believe in angels. But not the ones I can't see or touch... I believe because of what's in front of me.\""

    voice "FUM_0608"
    fumi "\"I think this feather really must be yours, Hina. To me, you're—\""

    voice "HIN_0799"
    hina "\"Nnh...\""

    voice "FUM_0609"
    fumi "\"...I'll go change your towel.\""

    voice "FUM_0610"
    fumi "\"......\""

    voice "FUM_0612"
    fumi "\"...She's burning up.\""

    voice "HIN_0801"
    hina "\"...You'll catch my cold...\""

    play sound se_bati

    show batim at truecenter
    pause 0.5

    scene white with bg_effect_07_1000

    scene bg01ca_grayscale with bg_effect_08_1000
    pause 0.5

    play sound se220c_100

    show rin 2 lg pyjama glasses a grayscale with Dissolve(0.25)

    voice "RIN_0741"
    rin "\"...Hina, do you...\""

    show rin 1 lg pyjama glasses h grayscale with dict_dissolve_25

    voice "RIN_0742"
    rin "\"Like me?\""

    play sound se115a

    $ side_image = "side/hina_2_side_pyjama_headphones_j_grayscale.webp"

    voice "HIN_0920"
    hina "\"I do!!\""

    show rin:
        "rin 1 lg pyjama glasses j grayscale" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_0743"
    rin "\"Wah?!\""

    show rin 1 lg pyjama glasses j grayscale:
        xoffset 0 yoffset 0
    with None

    play sound se_bati

    show batim at truecenter
    pause 0.5

    scene white with bg_effect_07_1000

    scene bg02ca_grayscale with bg_effect_08_1000
    pause 0.5

    show rin 1 lg pyjama glasses h grayscale at pos_r
    show fumi 2 lg pyjama h grayscale at pos_l
    with Dissolve(0.25)

    voice "RIN_0837"
    rin "\"Do you actually want to keep going from where we stopped yesterday?\""

    voice "FUM_0744"
    fumi "\"......\""

    show rin:
        "rin 1 lg pyjama glasses j grayscale" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0838"
    rin "\"I-If you don't... you can tell me. I know I can get carried away...\""

    show rin 1 lg pyjama glasses j grayscale:
        xoffset 0 yoffset 0
    with None

    voice "FUM_0745"
    fumi "\"I do... want to keep going.\""

    show rin 1 lg pyjama glasses c grayscale with dict_dissolve_25

    voice "RIN_0839"
    rin "\"...Okay.\""

    show fumi 2 lg pyjama b grayscale with dict_dissolve_25

    voice "FUM_0746"
    fumi "\"If we get the chance...\""

    show rin 1 lg pyjama glasses b grayscale with dict_dissolve_25

    voice "RIN_0840"
    rin "\"Right... if we get the chance.\""

    play sound se_bati

    show batim at truecenter
    pause 0.5

    scene black with Dissolve(0.5)
    pause 1.5

    "Through each door I opened, the girls fell in love—"

    scene bg01aa_grayscale with Dissolve(0.375)
    pause 1.125

    play music bgm05

    "The room was full of possibilities when I first peeked in."

    "But when I looked at one of them, a story was chosen."

    scene black with bg_effect_01_1000

    scene bg02aa_grayscale with bg_effect_01_1000
    pause 0.5

    "The reason angels exist..."

    "It's to observe one of countless possibilities, and through doing so, form the shape of the world."

    scene black with bg_effect_01_1000

    scene bg05aa_grayscale with bg_effect_01_1000
    pause 0.5

    "I thought to myself."

    "Was this story what the girls themselves chose?"

    "Or did they fall in love {i}because I saw it{/i}?"

    "If I hadn't seen it, would {i}her{/i} and {i}her{/i} romance have happened?"

    scene black with bg_effect_01_1000

    scene bg07aa_grayscale with bg_effect_01_1000
    pause 0.5

    "Of course, according to Sachiko..."

    "The angel's will has nothing to do with where probability lands."

    "All the angel does is throw the ball into the spinning roulette."

    scene white with Dissolve(0.375)
    pause 1.625

    voice "2SA_0038"
    sachiko "\"We're not the type of angel with a little bow and arrow, unfortunately. We have no power to begin or end a romance.\""

    voice "SYO_0221"
    sachiko "\"It's all chance. Change the world? Observers can't do that. It's rude to human will to even think it.\""

    voice "SYO_0222"
    sachiko "\"No matter what box you open, the cats inside are living happily.\""

    scene bg08aa_grayscale with Dissolve(0.375)
    pause 1.625

    play sound se118b

    "I spread my wings."

    "—I'm off to see the conclusion."

    pause 0.5

    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene black with Dissolve(0.75)
    pause 2.25

    jump a05_ang_13
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
