label a10_cou3_11:

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01 fadein 1.0

    show fumi z4 1 lg pyjama k:
        xcenter 118
    show miyako z4 1 lg pyjama_a a behind fumi, hina:
        xcenter 383
    show hina z4 2 lg pyjama_pjm a:
        xcenter 641
    show rin z4 2 lg pyjama glasses a:
        xcenter 906
    with Dissolve(0.5)

    voice "2FU_1281"
    fumi "\"I sorta made you into a bad guy. I'm sorry about that.\""

    "Fumi apologized to Hina."

    "Now that it was all over, they could look back on it and laugh, but it's true that Hina had to be a sort of villain this last week."

    "That seemed to be bothering Fumi, since she'd apologized a few times for it."

    show hina z4 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_1600"
    hina "\"I told you, it's fine. I had fun tormenting Rin.\""

    show rin:
        "rin z4 2 lg pyjama glasses f" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1687"
    rin "\"Ugh...\""

    show rin z4 2 lg pyjama glasses f:
        xoffset 0 yoffset 0
    with None
    show hina z4 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_1601"
    hina "\"And you did good holding back as much as you did.\""

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_1282"
    fumi "\"...It was really hard.\""

    "She admits it easily now."

    show rin z4 2 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1688"
    rin "\"What~? Fumi had it better than me. I was the only one who didn't know anything about this!\""

    show fumi z4 1 lg pyjama h with dict_dissolve_25

    voice "2FU_1283"
    fumi "\"I'm... sorry about that, too.\""

    show hina z4 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_1602"
    hina "\"Well, if we didn't do something like that, you wouldn't learn anything, Rin.\""

    show rin z4 2 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1689"
    rin "\"I'm learning!\""

    show miyako z4 1 lg pyjama_b g with dict_dissolve_25

    voice "2MI_1066"
    miyako "\"How so?\""

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_1690"
    rin "\"Because I'm fine in groups now!\""

    show fumi z4 1 lg pyjama d
    show miyako z4 1 lg pyjama_b e
    show hina z4 1 lg pyjama_pjm j
    with dict_dissolve_25

    voice "2HI_1603"
    hina "\"......\""

    voice "2FU_1284"
    fumi "\".........\""

    voice "2MI_1067"
    miyako "\"......\""

    "Well, she's done it now."

    show hina z4 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_1604"
    hina "\"Hey, Asou, I'm kind of interested in a model photo shoot. The picture-taking part, I mean. Do you mind asking the president of the agency if I can come and observe?\""

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_1285"
    fumi "\"Sure thing♪\""

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1691"
    rin "\"Mmmmmh!!\""

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_1068"
    miyako "\"Ahahahahaha!\""

    "Miyako was absolutely tickled at the gag's nonexistent landing."

    show rin:
        "rin z4 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeJump

    voice "2RI_1692"
    rin "\"Fine! You know what? I {i}will{/i} go to the audition! And I'll ask them if they have any kids' modeling jobs for Hina!\""

    show rin z4 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None

    voice "2FU_1286"
    fumi "\"Ahaha. Let's go, let's go. We should all go♪\""

    show hina z4 1 lg pyjama_pjm f with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "2HI_1605"
    hina "\"Hey, who are you calling a kid model?!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin:
        ShakeJump

    voice "2RI_1693"
    rin "\"I'm gonna make sure you star in a junior idol promo vid eventually!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1606"
    hina "\"What? I dunno what that is, but I bet it's dirty!\""

    "And they went right back to their everyday lives like nothing had happened."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    call staff_02 from _call_staff_02_2

    jump a10_cou3_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
