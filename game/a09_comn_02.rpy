label a09_comn_02:

    scene bg06aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    if persistent.dpatch:
        "The chapel, after school." id a09_comn_02_928ecf02
    else:
        "The chapel, after class."

    "The four girls were on cleaning duty, but they were chatting now, their work almost done."

    show fumi z4 2 lg school_scarf c:
        xcenter 118
    show miyako z4 1 lg school_a_sei e behind fumi, hina:
        xcenter 383
    show hina z4 2 lg school_scarf a:
        xcenter 641
    show rin z4 2 lg school_scarf a:
        xcenter 906
    with dict_dissolve_25

    voice "2FU_0576"
    fumi "\"That scarf looks good on you.\"" id a09_comn_02_f88fe614

    show miyako:
        "miyako z4 1 lg school_a_sei c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0568"
    miyako "\"Thank you. I like it, too.\"" id a09_comn_02_441026d5

    show miyako z4 1 lg school_a_sei c:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_0748"
    rin "\"Oh yeah, you just started wearing that, didn't you? Where'd you get it?\"" id a09_comn_02_68d6cac1

    show miyako z4 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_0569"
    miyako "\"Sachiko gave it to me.\"" id a09_comn_02_5e60c7ef

    show fumi z4 2 lg school_scarf h
    show hina z4 2 lg school_scarf e
    show rin z4 1 lg school_scarf i
    with dict_dissolve_25

    "At Sachiko's name, a strange air settled between the other three girls."

    show miyako z4 2 lg school_sei a with dict_dissolve_25

    voice "2MI_0570"
    miyako "\"...?\"" id a09_comn_02_2645870b

    show fumi z4 2 lg school_scarf a with dict_dissolve_25

    voice "2FU_0577"
    fumi "\"Speaking of Sachiko...\"" id a09_comn_02_7fdd0679

    voice "2MI_0571"
    miyako "\"Yes?\"" id a09_comn_02_e8b7a6ae

    "Miyako cocked her head to the right."

    show rin z4 1 lg school_scarf g with dict_dissolve_25

    voice "2RI_0749"
    rin "\"About the night of the hotpot party...\"" id a09_comn_02_90aa5303

    voice "2MI_0572"
    miyako "\"Yes?\"" id a09_comn_02_129bf9d8

    "She cocked her head to the left this time."

    show hina z4 1 lg school_scarf n with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_0734"
    hina "\"That really surprised me. You were right on top of her when we opened the door.\"" id a09_comn_02_d06ccb49

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina gets straight to the point."

    show miyako:
        "miyako z4 2 lg school_sei d" with Dissolve(0.25)
        ShakeNo

    voice "2MI_0573"
    miyako "\"That was...\"" id a09_comn_02_8e5ea8f2

    show miyako z4 2 lg school_sei d:
        xoffset 0 yoffset 0
    with None
    show hina z4 2 lg school_scarf f with dict_dissolve_25

    voice "2HI_0735"
    hina "\"Were you half-asleep? Dreaming about being a lion?\"" id a09_comn_02_2b1cbe48

    show miyako z4 2 lg school_sei f with dict_dissolve_25

    voice "2MI_0574"
    miyako "\"I just wanted to tease her a little.\"" id a09_comn_02_4c5f6e43

    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_0578"
    fumi "\"Not the other way around?\"" id a09_comn_02_10172d87

    show miyako z4 2 lg school_sei b with dict_dissolve_25

    voice "2MI_0575"
    miyako "\"No.\"" id a09_comn_02_0f39b6d1

    show rin z4 1 lg school_scarf i with dict_dissolve_25

    voice "2RI_0750"
    rin "\"She didn't just tell you to say that?\"" id a09_comn_02_5bd6bc92

    show miyako z4 2 lg school_sei c with dict_dissolve_25

    voice "2MI_0576"
    miyako "\"No.\"" id a09_comn_02_926e46a1

    show hina z4 2 lg school_scarf e with dict_dissolve_25

    voice "2HI_0736"
    hina "\"Sachiko's being a bad influence on her!\"" id a09_comn_02_911ab078

    "That's not very nice, you three."

    show miyako z4 2 lg school_sei e with dict_dissolve_25

    voice "2MI_0577"
    miyako "\"I... think I love her.\"" id a09_comn_02_6e2e6e27

    show hina z4 1 lg school_scarf k with dict_dissolve_25

    voice "2HI_0737"
    hina "\"Hwha?\"" id a09_comn_02_903850c8

    show miyako z4 2 lg school_sei f with dict_dissolve_25

    voice "2MI_0578"
    miyako "\"Sachiko.\"" id a09_comn_02_03ebbdc9

    show rin:
        "rin z4 1 lg school_scarf d" with Dissolve(0.25)
        2.5
        "rin z4 1 lg school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0751"
    rin "\"There you go joking aga... Wait, you're serious?!\"" id a09_comn_02_d1a50edf

    show rin z4 1 lg school_scarf j:
        xoffset 0 yoffset 0
    with None
    show miyako:
        ShakeYes

    "Miyako nodded."

    show miyako:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school_scarf b with dict_dissolve_25

    voice "2FU_0579"
    fumi "\"Ahh...\"" id a09_comn_02_705099d8

    "Fumi was quick to catch on as always."

    voice "2HI_0738"
    hina "\"You mean you love her as family? Or you want to kiss her?\"" id a09_comn_02_e613e45b

    show miyako z4 2 lg school_sei c with dict_dissolve_25

    voice "2MI_0579"
    miyako "\"I would say I want to kiss her, yes.\"" id a09_comn_02_5b21536a

    show hina:
        "hina z4 1 lg school_scarf d" with Dissolve(0.25)
        ShakeSide

    voice "2HI_0739"
    hina "\"Ugh...\"" id a09_comn_02_90029f28

    show hina z4 1 lg school_scarf d:
        xoffset 0 yoffset 0
    with None
    show rin z4 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_0752"
    rin "\"Haha, wait a second. Let's be rational about this. In some Western societies, family members kiss—\"" id a09_comn_02_85a9f66e

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0580"
    miyako "\"Like you two do.\"" id a09_comn_02_11686cf0

    "Miyako indicated the lovers."

    if route2 == 1:
        show fumi z4 2 lg school_scarf h
        show hina z4 2 lg school_scarf f
    elif route2 == 2:
        show hina z4 2 lg school_scarf f
        show rin z4 2 lg school_scarf g
    elif route2 == 3:
        show fumi z4 2 lg school_scarf h
        show rin z4 2 lg school_scarf g
    with dict_dissolve_25

    "They exchanged a glance."

    if route2 == 1:
        $ voice2("hina","2HI_0740","fumi","2FU_0580")
        hina_fumi "\"Oh...\""
    elif route2 == 2:
        $ voice2("hina","2HI_0740","rin","2RI_0753")
        hina_rin "\"Oh...\""
    elif route2 == 3:
        $ voice2("rin","2RI_0753","fumi","2FU_0580")
        rin_fumi "\"Oh...\""

    show rin z4 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_0754"
    rin "\"You're surprisingly assertive, Mikoyan.\"" id a09_comn_02_c720319b

    "Rin scratched her head."

    show hina z4 1 lg school_scarf m with dict_dissolve_25

    voice "2HI_0741"
    hina "\"Well, the peach doesn't fall far from the tree.\"" id a09_comn_02_4fa880ba

    show rin z4 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_0755"
    rin "\"Huh?\"" id a09_comn_02_92324de9

    show hina z4 1 lg school_scarf e with dict_dissolve_25

    voice "2HI_0742"
    hina "\"Or is it pear?\"" id a09_comn_02_159f00ca

    show rin z4 1 lg school_scarf d with dict_dissolve_25

    voice "2RI_0756"
    rin "\"Pfft.\"" id a09_comn_02_2ebecfb4

    "That's Hina."

    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_0581"
    fumi "\"But you two aren't blood relatives, right?\"" id a09_comn_02_7f6420d1

    show miyako z4 1 lg school_a_sei e with Dissolve(0.25)
    show miyako:
        ShakeYes

    voice "2MI_0581"
    miyako "\"Oh, yes.\"" id a09_comn_02_2ff263ce

    show miyako:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg school_scarf m with dict_dissolve_25

    voice "2HI_0743"
    hina "\"I guess there's no problem, then.\"" id a09_comn_02_d6674b2a

    show rin z4 1 lg school_scarf b with dict_dissolve_25

    voice "2RI_0757"
    rin "\"There... isn't?\"" id a09_comn_02_8ee73d76

    "I wonder."

    show rin z4 2 lg school_scarf a with dict_dissolve_25

    voice "2RI_0758"
    rin "\"There's a pretty big age difference between you two, Mikoyan.\"" id a09_comn_02_453034c0

    show miyako z4 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_0582"
    miyako "\"That's alright.\"" id a09_comn_02_4019be15

    "It's only their appearances that differ in age, after all."

    show fumi z4 2 lg school_scarf a with dict_dissolve_25

    voice "2FU_0582"
    fumi "\"Do you think your relatives will allow it?\"" id a09_comn_02_4ae1a258

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0583"
    miyako "\"I'm not worried about that.\"" id a09_comn_02_25ec7d9b

    "They don't have any, after all."

    show hina z4 2 lg school_scarf f with dict_dissolve_25

    voice "2HI_0744"
    hina "\"She's a pervert, you know?\"" id a09_comn_02_c2a35e02

    show miyako z4 1 lg school_a_sei d with dict_dissolve_25

    voice "2MI_0584"
    miyako "\"Ahaha, that's fine.\"" id a09_comn_02_f78371db

    show hina z4 2 lg school_scarf e with dict_dissolve_25

    voice "2HI_0745"
    hina "\"Hmm.\"" id a09_comn_02_e6463e07

    "Well, that's how humans are."

    show miyako z4 2 lg school_sei c with dict_dissolve_25

    voice "2MI_0585"
    miyako "\"I feel all tingly when I touch her.\"" id a09_comn_02_22c3c586

    if route2 == 1:
        show fumi z4 2 lg school_scarf b
        show hina z4 2 lg school_scarf f
        show rin z4 2 lg school_scarf g
    if route2 == 2:
        show fumi z4 2 lg school_scarf h
        show hina z4 2 lg school_scarf f
        show rin z4 2 lg school_scarf e
    elif route2 == 3:
        show fumi z4 2 lg school_scarf b
        show hina z4 2 lg school_scarf b
        show rin z4 2 lg school_scarf e
    with dict_dissolve_25

    "The lovers looked at each other in understanding, while the third wheel looked on blankly."

    show hina z4 1 lg school_scarf n with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_0746"
    hina "\"Haah, well, you seem serious. What do you like about Sachiko, though?\"" id a09_comn_02_781c2c0a

    show hina:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg school_a_sei g with dict_dissolve_25

    voice "2MI_0586"
    miyako "\"Hmm~\"" id a09_comn_02_d49596ac

    "She tilted her head again."

    show hina:
        "hina z4 1 lg school_scarf d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0747"
    hina "\"You have to think about it?!\"" id a09_comn_02_13b6a37b

    show hina z4 1 lg school_scarf d:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school_scarf c with dict_dissolve_25

    voice "2FU_0583"
    fumi "\"Ahaha, well, she's nice. She is a little perverted, though.\"" id a09_comn_02_dd7e49df

    show rin z4 1 lg school_scarf k with dict_dissolve_25

    voice "2RI_0759"
    rin "\"She is pretty good-looking if you look close enough. Though she's a dirty old man on the inside.\"" id a09_comn_02_21d0f14c

    show hina z4 2 lg school_scarf e with dict_dissolve_25

    voice "2HI_0748"
    hina "\"I guess she's pretty reliable. Reliable but dirty.\"" id a09_comn_02_f9ce999a

    show miyako z4 1 lg school_a_sei h with dict_dissolve_25

    voice "2MI_0587"
    miyako "\"Ahaha. I love all of that.\"" id a09_comn_02_50820341

    show fumi z4 2 lg school_scarf b
    show miyako z4 1 lg school_a_sei g
    show hina z4 2 lg school_scarf a
    show rin z4 1 lg school_scarf a
    with dict_dissolve_25

    "The three all took Miyako by the hand."

    show fumi z4 2 lg school_scarf i
    show hina z4 2 lg school_scarf g
    show rin z4 1 lg school_scarf c
    with dict_dissolve_25

    $ voice3("hina","2HI_0749","rin","2RI_0760","fumi","2FU_0584")
    hina_rin_fumi "\"Good luck.\""

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0588"
    miyako "\"Thank you.\"" id a09_comn_02_0d919596

    "They had plenty of commentary, but they were rooting for her in the end."

    "—Well, Sachiko's pretty popular, isn't she?"

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
