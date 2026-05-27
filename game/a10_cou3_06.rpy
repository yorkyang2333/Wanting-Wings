label a10_cou3_06:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    if persistent.dpatch:
        "—After school." id a10_cou3_06_fe776d95
    else:
        "—After class."

    "Rin and Fumi were alone in the classroom."

    "This is usually when they would be waiting for Hina and Miyako to come back so they could all go to the grocery store on their way home. But since Fumi had been going back to her house this week, she had to part with them here."

    show rin z4 1 lg school e:
        xcenter 662
    with dict_dissolve_25

    voice "2RI_1591"
    rin "\"Ah...\"" id a10_cou3_06_4d5c4479

    "She was supposed to be saying goodbye, but Rin had grabbed Fumi's hand instead. She made a little noise, as if her own action had startled her."

    show fumi z4 1 lg school_scarf e:
        xcenter 362
    with dict_dissolve_25

    voice "2FU_1186"
    fumi "\"!\"" id a10_cou3_06_7a5c718f

    "Fumi turned around, also surprised. She glanced at the clock and then gave Rin a smile."

    show fumi z4 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_1187"
    fumi "\"We still have a little time...\"" id a10_cou3_06_a711f36a

    show rin z4 1 lg school d with dict_dissolve_25

    voice "2RI_1592"
    rin "\"Yeah!\"" id a10_cou3_06_24c95265

    "Her face lit up at that."

    show fumi z4 2 lg school_scarf c with dict_dissolve_25

    voice "2FU_1188"
    fumi "\"Are you getting up on time in the morning?\"" id a10_cou3_06_6b2d38d5

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1593"
    rin "\"Well, I'm in class every day, aren't I?\"" id a10_cou3_06_a2f5f6b4

    show fumi z4 1 lg school_scarf c with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_1189"
    fumi "\"Yes, you are. Good job.\"" id a10_cou3_06_4baa65fb

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi stretched up a bit and gave Rin a pat on the head."

    show fumi z4 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_1190"
    fumi "\"What about dinner? You're not being too picky, are you?\"" id a10_cou3_06_05b248ec

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1594"
    rin "\"I'm not. Hina gets mad if I leave anything.\"" id a10_cou3_06_486b2a21

    show fumi:
        "fumi z4 2 lg school_scarf i" with Dissolve(0.25)
        3.0
        "fumi z4 2 lg school_scarf c" with Dissolve(0.25)

    voice "2FU_1191"
    fumi "\"Ahaha. I left you in capable hands, it seems. Are you ironing your—\"" id a10_cou3_06_f5dcb73a

    show fumi z4 2 lg school_scarf c:
        pass
    with None
    hide rin
    hide fumi
    with dict_dissolve_25

    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False
    show rin 1 lg school k as rin_1:
        xcenter 682
    show fumi 2 lg school_scarf d as fumi_1:
        xcenter 342
    with Dissolve(0.5)

    pause 0.5

    camera
    with None

    "Rin cut Fumi off with an embrace, stealing her lips in the process."

    show fumi 2 lg school_scarf j as fumi_1 with dict_dissolve_50

    "Fumi was startled at first, but quickly put her hands behind Rin's back."

    hide rin_1
    hide fumi_1
    with dict_dissolve_50

    "........."

    "......"

    $ side_image = "rin 1 side school g"

    voice "2RI_1595"
    rin "\"Yah!\"" id a10_cou3_06_05416423

    show rin:
        "rin z4 2 lg school d flat"
        alpha 0.0 xcenter 526
        easein 0.25 alpha 1.0 xcenter 726
    show fumi:
        "fumi z4 2 lg school_scarf d flat"
        alpha 0.0 xcenter 498
        easein 0.25 alpha 1.0 xcenter 298

    play sound se_2s_g002

    "After a long kiss, Rin swiftly pulled away."

    show rin z4 2 lg school d:
        alpha 1.0 xcenter 726
    show fumi z4 2 lg school_scarf d:
        alpha 1.0 xcenter 298
    with None
    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1596"
    rin "\"I'm fine on my own! And I'm ironing my shirts, too.\"" id a10_cou3_06_c95ddbc7

    "She boasted."

    show fumi z4 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_1192"
    fumi "\"...Good.\"" id a10_cou3_06_0db8dffb

    "Fumi could easily see through Rin's brave front, of course. But she smiled nonetheless."

    voice "2RI_1597"
    rin "\"I also washed the dishes. And did my laundry. And hung my clothes out to dry, and folded them, too. And I vacuumed and changed my sheets.\"" id a10_cou3_06_8c53e716

    "Rin listed off all the household chores she'd done in Fumi's absence. She was like a child looking for praise."

    show fumi z4 1 lg school_scarf b with dict_dissolve_25

    voice "2FU_1193"
    fumi "\"That's incredible, Rin.\"" id a10_cou3_06_e3fc7f0c

    "And Fumi, being Fumi, was predictably impressed."

    show rin:
        ShakeYes

    voice "2RI_1598"
    rin "\"Oh, and I brushed all your stuffed animals, too.\"" id a10_cou3_06_8261e69f

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_1194"
    fumi "\"What? You're even taking care of them?\"" id a10_cou3_06_805da85f

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_1599"
    rin "\"I don't think I'm as good at it as you, though.\"" id a10_cou3_06_4fb3e84d

    show fumi z4 2 lg school_scarf i with dict_dissolve_25

    voice "2FU_1195"
    fumi "\"That's alright. It's enough that you're taking care of them. I'm sure they're also happy about it.\"" id a10_cou3_06_382bab2f

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1600"
    rin "\"And I turned in my course plan.\"" id a10_cou3_06_9fd86462

    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_1196"
    fumi "\"Which one did you pick?\"" id a10_cou3_06_0b850bee

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1601"
    rin "\"Arts, for now.\"" id a10_cou3_06_3376ecca

    show fumi z4 2 lg school_scarf a with dict_dissolve_25

    voice "2FU_1197"
    fumi "\"Did you pick that to match with me?\"" id a10_cou3_06_4841d18f

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_1602"
    rin "\"Well, partly. But my scores for our practical tests were a little bit higher in those subjects.\"" id a10_cou3_06_dc909855

    show fumi z4 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_1198"
    fumi "\"Ah. What about your career survey?\"" id a10_cou3_06_6a4b387f

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1603"
    rin "\"I turned that in, too.\"" id a10_cou3_06_fe868fb1

    voice "2FU_1199"
    fumi "\"What did you say?\"" id a10_cou3_06_97cd16cf

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_1604"
    rin "\"...I won't tell you yet.\"" id a10_cou3_06_aaa637c5

    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_1200"
    fumi "\"Huh? You won't?\"" id a10_cou3_06_5498a95b

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1605"
    rin "\"Yeah.\"" id a10_cou3_06_ff64b3b1

    "Rin nodded, her face hesitant."

    show fumi z4 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_1201"
    fumi "\"I'll be looking forward to hearing it, then. I'm happy you thought about your career plans.\"" id a10_cou3_06_2a6229f8

    show fumi z4 2 lg school_scarf h with dict_dissolve_25

    voice "2FU_1202"
    fumi "\"Listen, I'm—\"" id a10_cou3_06_ed85f8d0

    play sound se030a

    show fumi z4 2 lg school_scarf g
    show rin z4 2 lg school g
    with dict_dissolve_25

    "The bell rang, and the two of them looked up at the clock."

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1606"
    rin "\"Oh, sorry. I kinda kept you, huh? You should go.\"" id a10_cou3_06_40a39a12

    "She put her best smile on."

    show fumi z4 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_1203"
    fumi "\"No, it's fine. I should, though...\"" id a10_cou3_06_c1b0a6ae

    hide rin
    hide fumi
    with dict_dissolve_50

    "Fumi shouldered her bag and left the classroom, turning around and waving a couple times as she went."

    $ side_image = "rin 2 side school d"

    voice "2RI_1607"
    rin "\"Don't go too—\"" id a10_cou3_06_a32a4624

    "Rin swallowed the words she was about to say to Fumi."

    "Good job. I'll pat your head in Fumi's place."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared >= 2:
        jump a10_cou4_01
    else:
        jump a10_cou3_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
