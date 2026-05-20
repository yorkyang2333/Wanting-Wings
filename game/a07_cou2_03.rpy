label a07_cou2_03:

    scene bg02ag with Dissolve(0.5)
    pause 1.5

    play sound se521
    pause 1.0

    play music bgm01

    $ side_image = "hina 1 side casual_scarf j"

    voice "2HI_0256"
    hina "\"......\""

    "Hina had returned."

    "But she was clearly displeased, a pout on her face."

    play sound se521
    pause 1.5

    "Rin followed close behind her, a little out of breath."

    show rin z4 1 lg casual g with dict_dissolve_25

    voice "2RI_0240"
    rin "\"Don't run off like that... You expect me to keep up with you?\""

    "Hina didn't turn to face her."

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0241"
    rin "\"Hina—\""

    $ side_image = "hina 1 side casual_scarf h"

    voice "2HI_0257"
    hina "\"I don't care!\""

    "Hina shouted."

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0242"
    rin "\"Huh? Hey... what are you mad about?\""

    "Rin finally noticed her mood."

    "She went around to Hina's front and put her hands on her shoulders, but Hina wouldn't meet her gaze."

    show rin:
        xcenter 512
        easein 0.5 xcenter 668
    pause 0.5

    show rin z4 2 lg casual d
    show hina z4 2 lg casual_scarf e:
        xcenter 356
    with dict_dissolve_25

    voice "2RI_0243"
    rin "\"...Did I do something?\""

    voice "2HI_0258"
    hina "\".........\""

    show rin z4 2 lg casual b with dict_dissolve_25

    voice "2RI_0244"
    rin "\"...I won't know what I did unless you tell me.\""

    show hina z4 2 lg casual_scarf d with dict_dissolve_25

    voice "2HI_0259"
    hina "\"...You really don't know?\""

    "Rin nodded helplessly."

    show hina z4 1 lg casual_scarf h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_0260"
    hina "\"...Haahh...\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "The tension went out of Hina with her sigh."

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0245"
    rin "\"Huh? What is it...?\""

    show hina z4 1 lg casual_scarf j with dict_dissolve_25

    voice "2HI_0261"
    hina "\"When I clung to you, you pushed me away.\""

    "That rang a bell for her."

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0246"
    rin "\"Th-That's kind of an exaggeration, isn't it? I just pulled away a little.\""

    show hina z4 1 lg casual_scarf e with dict_dissolve_25

    voice "2HI_0262"
    hina "\"Why?\""

    show rin:
        "rin z4 1 lg casual g" with Dissolve(0.25)
        ShakeNo

    voice "2RI_0247"
    rin "\"W-Well... I saw some girls from our class coming our way.\""

    show rin z4 1 lg casual g:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg casual_scarf j with dict_dissolve_25

    voice "2HI_0263"
    hina "\"I know. I saw them too. Is that why?\""

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0248"
    rin "\"Well... it'd be embarrassing if they started spreading rumors, right?\""

    show hina z4 2 lg casual_scarf h with dict_dissolve_25

    voice "2HI_0264"
    hina "\"...Are you embarrassed to be with me?\""

    show rin z4 2 lg casual d with dict_dissolve_25

    voice "2RI_0249"
    rin "\"...Sorry.\""

    "Realizing what she'd stepped in, Rin elected to simply apologize instead."

    show hina z4 2 lg casual_scarf e with dict_dissolve_25

    voice "2HI_0265"
    hina "\"Fine, whatever. You didn't mean anything by it, you were just being insensitive. I should have known you're just like this.\""

    show rin z4 2 lg casual f with dict_dissolve_25

    voice "2RI_0250"
    rin "\"Ugh...\""

    "She swallowed whatever retort she was thinking of making, sensing that now would be a bad time."

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0251"
    rin "\"...What do you want to do now?\""

    show hina z4 1 lg casual_scarf m with dict_dissolve_25

    voice "2HI_0266"
    hina "\"Organize my pictures.\""

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0252"
    rin "\"Huh? What am I supposed to do, then?\""

    voice "2HI_0267"
    hina "\"Why don't you read one of your sex books?\""

    "Cold as ice."

    show rin:
        "rin z4 1 lg casual j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0253"
    rin "\"Asou was nice enough to give us time to be alone together! You're just going to waste it?!\""

    show rin z4 1 lg casual j:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z4 1 lg casual_scarf i" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0268"
    hina "\"I don't care! I'm not in the mood!\""

    hide hina with Dissolve(0.5)

    show rin z4 1 lg casual g with dict_dissolve_25

    voice "2RI_0254"
    rin "\"......\""

    "Hina turned her back, leaving Rin to flounder behind her."


    hide rin with dict_dissolve_25
    show rin 1 lg casual i as rin_1:
        "rin 1 lg casual i flat" with Dissolve(0.25)
        xcenter 682 ycenter 1016
        ShakeSide

    voice "2RI_0255"
    rin "\"Hiiinaaa!\""


    hide rin_1
    show rin 1 lg casual i:
        xcenter 682
    with None
    show hina 1 lg casual_scarf l:
        xcenter 342
        function LayerShake(20,20,0.3)
    with dict_dissolve_25
    $ persistent.layer_shaken = False

    voice "2HI_0269"
    hina "\"Wah?!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Rin leapt on Hina."

    show rin:
        ShakeNo_3_500

    voice "2RI_0256"
    rin "\"Let's make up! I was looking forward to this!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg casual_scarf f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0270"
    hina "\"I was too! But then you...!\""

    show hina 1 lg casual_scarf f:
        xoffset 0 yoffset 0
    with None
    show rin:
        ShakeNo_3_500

    voice "2RI_0257"
    rin "\"But I apologized! And I'll apologize more if that wasn't enough! I'm sorry, I'm sorry!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg casual_scarf g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0271"
    hina "\"L-Let me go! I hate this part of you, Rin!\""

    show hina 1 lg casual_scarf g:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0258"
    rin "\"Don't tell me you hate me! You'll really hurt me!\""

    "Hina struggled as Rin held her down."

    "They fought for control. With her height, Rin should have had the advantage, but Hina's physical abilities were no joke."

    show rin 2 lg casual a with Dissolve(0.25)
    show rin:
        ShakeNo_3_500

    voice "2RI_0259B2"
    rin "\"Urrrgh... h-how 'bout this?!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin blew on Hina's ear."

    show hina 2 lg casual_scarf i with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "2HI_0272"
    hina "\"Nnh?!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "All of Hina's strength left her."

    if persistent.dpatch:
        jump a07_cou2_03_d
    else:
        stop music fadeout 1.0
        stop sound fadeout 1.0
        scene black with Dissolve(0.5)
        pause 3.5
        "........."
        "......"
        window hide
        pause 1.0
        window auto

label rp_c_scene03_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    $ renpy.end_replay()

    jump a07_comn_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
