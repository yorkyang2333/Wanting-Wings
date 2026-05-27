label a10_cou3_08:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    $ side_image = "hina 1 side school_scarf a"

    voice "2HI_1581"
    hina "\"Eheh, you really bought a lot. You're fully prepared, huh?\"" id a10_cou3_08_92bed41d

    $ side_image = "rin 1 side school_scarf a"

    voice "2RI_1619"
    rin "\"You're not laughing at me for being too hasty?\"" id a10_cou3_08_7152c4ca

    $ side_image = "hina 2 side school_scarf a"

    voice "2HI_1582"
    hina "\"Well, it's for Asou, isn't it?\"" id a10_cou3_08_30c2e865

    $ side_image = "rin 2 side school_scarf e"

    voice "2RI_1620"
    rin "\"Yeah... thanks.\"" id a10_cou3_08_aa3a4c89

    play sound se521
    pause 0.5

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    $ side_image = "hina 1 side school_scarf k"

    voice "2HI_1583"
    hina "\"We're back~ Huh?\"" id a10_cou3_08_7e1abde3

    $ side_image = "rin 1 side school_scarf e"

    voice "2RI_1621"
    rin "\"Oh...\"" id a10_cou3_08_686ee907

    "They opened the door to find Sachiko and..."

    show fumi 2 lg school i with dict_dissolve_50

    voice "2FU_1204"
    fumi "\"Welcome back.\"" id a10_cou3_08_6a41404e

    "...Fumi, with her usual carefree smile."

    $ side_image = "rin 2 side school_scarf e"

    voice "2RI_1622"
    rin "\"...Hey.\"" id a10_cou3_08_5c9b09c5

    "Rin kept herself from leaping into her arms."

    $ side_image = "rin 2 side school_scarf d"

    voice "2RI_1623"
    rin "\"...You're in your uniform.\"" id a10_cou3_08_e0e975d7

    hide fumi with Dissolve(0.5)

    show fumi z4 2 lg school g:
        xcenter 298
    show rin z4 2 lg school_scarf d:
        xcenter 726
    with Dissolve(0.5)

    voice "2FU_1205"
    fumi "\"Wait, what are those bags? Did you stop by somewhere on your way back?\"" id a10_cou3_08_d934d2ec

    "Rin's quiet voice didn't reach Fumi, her question drowning it out."

    show rin z4 2 lg school_scarf b with dict_dissolve_25

    voice "2RI_1624"
    rin "\"Yeah, we did.\"" id a10_cou3_08_fb39e542

    show fumi z4 2 lg school c with dict_dissolve_25

    voice "2FU_1206"
    fumi "\"Looks like you bought a lot. What'd you get?\"" id a10_cou3_08_0d04b9e7

    $ side_image = "hina 1 side school_scarf a"

    voice "2HI_1584"
    hina "\"Well, this one's a planner, and over here we have sunglasses, and masks...\"" id a10_cou3_08_29c0366c

    show fumi z4 2 lg school h with dict_dissolve_25

    voice "2FU_1207"
    fumi "\"Hm? That's an interesting collection.\"" id a10_cou3_08_5915f89a

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0873"
    sachiko "\"Ah...\"" id a10_cou3_08_b8df7137

    $ side_image = "hina 1 side school_scarf p"

    voice "2HI_1585"
    hina "\"Eeheehee.\"" id a10_cou3_08_563e8ba6

    "Sachiko shot a look to Hina, who returned it with an impish smile."

    show rin z4 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1625"
    rin "\"Listen, Fumi... I'm... gonna be your very first fan, okay?\"" id a10_cou3_08_0b6f757a

    "She did her very best, but still only managed to pull off an awkward smile."

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_1208RE"
    fumi "\"Huh...?\"" id a10_cou3_08_e98cf159

    voice "2RI_1626"
    rin "\"I'm not as cute as you are, so I can't stand in the same place as you, but I can cheer you on and help you.\"" id a10_cou3_08_95ff29d6

    show fumi z4 2 lg school d with dict_dissolve_25

    voice "2FU_1209RE"
    fumi "\"Huh? What?\"" id a10_cou3_08_f9270531

    "Rin just went on, leaving Fumi to her confusion."

    show rin z4 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1627"
    rin "\"Once we graduate, I'll join your agency, and I can support you as your manager. That's what I wrote on my career survey.\"" id a10_cou3_08_bfa69eab

    show rin z4 2 lg school_scarf d with dict_dissolve_25

    voice "2RI_1628"
    if persistent.dpatch:
        rin "\"Really I want to quit school right now and follow you, but then I wouldn't fulfill the hiring requirements of the agency—\"" id a10_cou3_08_a1c142a5
    else:
        rin "\"Really I want to quit studying right now and follow you, but then I wouldn't fulfill the hiring requirements of the agency—\"" id a10_cou3_08_7f3b98c6

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_1210RE"
    fumi "\"Wait... Wait a second, Rin.\"" id a10_cou3_08_4c951db9

    show rin z4 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1629"
    rin "\"Just wait. I'll be right behind you. And I'll do everything I can to be a good match for you. So you go ahead and go wherever you—\"" id a10_cou3_08_6a9b7771

    show fumi z4 2 lg school h with dict_dissolve_25

    voice "2FU_1211RE"
    fumi "\"...I'm not going anywhere.\"" id a10_cou3_08_61472d48

    "Her smile faded and she looked down, her voice trembling as if she was holding her emotions back."

    voice "2FU_1212RE"
    fumi "\"And I'm not joining the agency.\"" id a10_cou3_08_9a422a2a

    show rin z4 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1630"
    rin "\"What? But... didn't you go to the audition today?\"" id a10_cou3_08_b0cb72ab

    "Fumi shook her head."

    show rin z4 1 lg school_scarf i with dict_dissolve_25

    voice "2RI_1631"
    rin "\"But your dad said you were waiting to hear back about it...\"" id a10_cou3_08_740dd7ff

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_1213RE"
    fumi "\"Hear back? He must have been talking about the doctor... I was at the hospital. My mom collapsed with a fever this morning...\"" id a10_cou3_08_7c428506

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0874"
    sachiko "\"He must have thought she already knew. Foomin's dad strikes again.\"" id a10_cou3_08_1e917b0e

    $ side_image = "hina 2 side school_scarf b"

    voice "2HI_1586"
    hina "\"Yep...\"" id a10_cou3_08_3d5a1854

    show fumi z4 2 lg school h with dict_dissolve_25

    voice "2FU_1214RE"
    fumi "\"I had to take her to the hospital and arrange for all the people coming to the store, so I was really busy.\"" id a10_cou3_08_4e10e764

    show rin:
        "rin z4 1 lg school_scarf b" with Dissolve(0.25)
        3.5
        "rin z4 1 lg school_scarf h" with Dissolve(0.25)

    voice "2RI_1632"
    rin "\"So that's why you're in your uniform. But you never answered your phone...\"" id a10_cou3_08_dc3d29e3

    show rin z4 1 lg school_scarf h:
        pass
    with None
    show fumi:
        "fumi z4 1 lg school h" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1215RE"
    fumi "\"I'm sorry about that. The battery ran out...\"" id a10_cou3_08_2c0dd45d

    show fumi z4 1 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1633"
    rin "\"Umm... So then—huh?\"" id a10_cou3_08_3a9e92f2

    show fumi z4 1 lg school k with dict_dissolve_25

    stop music fadeout 1.0

    voice "2FU_1216RE"
    fumi "\"...!!\"" id a10_cou3_08_af92a6c9

    hide fumi
    hide rin
    with dict_dissolve_25

    show rin 1 lg school_scarf e as rin_1:
        xcenter 682
    show fumi 1 lg school k as fumi_1:
        xcenter 342
    camera:
        function LayerShake(5,5,0.3)
    with Dissolve(0.5)
    $ persistent.layer_shaken = False

    pause 0.5

    camera
    with None

    "Fumi embraced her with a soundless shout."

    voice "2FU_1217RE"
    fumi "\"I'm not going anywhere! I'm going to stay with you forever, Rin!\"" id a10_cou3_08_fe1135a3

    voice "2RI_1634"
    rin "\"Fumi...\"" id a10_cou3_08_c4b14848

    "This time, it was Rin who was taken aback."

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0875"
    sachiko "\"Yeah. It was really Foomin who was struggling with her loneliness this whole time.\"" id a10_cou3_08_58a2677f

    $ side_image = "hina 2 side school_scarf c"

    voice "2HI_1587"
    hina "\"Mhm, mhm, but she did a really good job~\"" id a10_cou3_08_6e602c26

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
