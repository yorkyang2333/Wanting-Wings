label a10_comn_03:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play sound se521
    pause 0.5

    show namahage sm:
        alpha 0.0 xcenter 412
        easein 0.5 alpha 1.0 xcenter 512

    voice "2SA_0816"
    sachiko "\"Trick or chocolate!\""

    show namahage sm:
        alpha 1.0 xcenter 512
    with None

    "Before they could even knock and open the door, a namahage flew out of the dorm manager's room."

    play music bgm01 fadein 1.0

    $ side_image = "hina 1 side pyjama_pjm d"

    voice "2HI_1187"
    hina "\"Geez, not again...\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1230"
    rin "\"She's mixing things again. And just like setsubun, why's the demon the one waiting?\""

    show namahage:
        ShakeJump

    voice "2SA_0817"
    sachiko "\"I'll play a trick on you if you don't give me chocolate!\""

    show namahage:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_1188"
    hina "\"You're always playing tricks on us anyway!\""

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0937"
    fumi "\"Is White Day too late?\""

    show namahage:
        ShakeNo

    voice "2SA_0818"
    sachiko "\"Nnnnnnngh!\""

    show namahage:
        xoffset 0 yoffset 0
    with None
    $ side_image = "side/fumi_rin_[rin_pyjama]_sozai01.webp"

    $ voice2("rin","2RI_1231N","fumi","2FU_0938")
    rin_fumi "\"She's just whining now.\""

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1189"
    hina "\"Hm?\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1232"
    rin "\"Whatever, just take that off. Or do you want us to throw chocolate at you?\""

    show namahage:
        ShakeNo

    voice "2SA_0819"
    sachiko "\"Uuugh...\""

    play sound se_2s_g004
    hide namahage with Dissolve(0.25)
    pause 1.0

    show sachiko 1 sm outfit c with Dissolve(0.25)

    $ side_image = "fumi 1 side pyjama a"

    voice "2FU_0939"
    fumi "\"Don't worry, we made some for you. We just came over to give it to you.\""

    "Fumi handed over the bag containing the chocolate from the four of them."

    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "2SA_0820"
    sachiko "\"Paaah!\""

    "Sachiko lifted the bag up like it was a rare item she'd just obtained."

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1233"
    rin "\"...What a joke.\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0821"
    sachiko "\"It's my aesthetic.\""

    if routes_cleared != 1:
        jump a10_comn_03_a
    else:
        jump a10_comn_03_b

label a10_comn_03_a:

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg05ba with bg_effect_05
    pause 0.5

    "After some pestering, the four went on their way."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0822"
    sachiko "\"Thanks~\""

    $ side_image = "miyako 1 sm pyjama_a g"

    voice "2MI_0985"
    miyako "\"Oh, right!\""

    "Miyako turned around before they left."

    show miyako 1 sm pyjama_a e with dict_dissolve_25
    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0823"
    sachiko "\"Hm? What's up?\""

    show miyako 1 sm pyjama_a i with dict_dissolve_25

    voice "2MI_0986"
    miyako "\"Umm, do you have someone you have feelings for?\""

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0824"
    sachiko "\"'Course I do.\""

    "She answered unexpectedly quickly."

    show miyako 2 sm pyjama f with dict_dissolve_25

    voice "2MI_0987"
    miyako "\"...Huh?\""

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0825"
    sachiko "\"All cute girls are my sweethearts♪\""

    show miyako 2 sm pyjama c with dict_dissolve_25

    voice "2MI_0988"
    miyako "\"Haha, I see...\""

    hide miyako with dict_dissolve_50

    "Miyako smiled awkwardly and went after the other three."

    "......"

    "Sachiko muttered to herself as she watched her leave."

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0826"
    sachiko "\"...I do. And she looks just like you.\""

    jump a10_comn_03_end

label a10_comn_03_b:

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0827"
    sachiko "\"...?\""

    hide sachiko with dict_dissolve_50

    "Sachiko noticed Miyako standing separately from the cheerful group of the other three girls."

    show miyako 2 sm pyjama c with dict_dissolve_25

    voice "2MI_0989"
    miyako "\"......\""

    "As their eyes met awkwardly, Miyako shook her head and smiled."

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0940"
    fumi "\"......\""

    "Fumi noticed and placed a hand on Miyako's back."

label a10_comn_03_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a10_cou1_09
    elif route2 == 2:
        jump a10_cou2_11
    elif route2 == 3:
        jump a10_cou3_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
