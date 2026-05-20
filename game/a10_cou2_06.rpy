label a10_cou2_06:

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01 fadein 1.0

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_1133"
    fumi "\"—So I'll be taking tomorrow off. I'm sorry.\""

    "Fumi said, bowing her head to the other three girls."

    if persistent.dpatch:
        "She'd gotten a LIME message from her parents that her mother had collapsed with a fever, so she'd decided to take time off school to help out at the store." id a10_cou2_06_74566c92
    else:
        "She'd gotten a LIME message from her parents that her mother had collapsed with a fever, so she'd decided to take time off class to help out at the store."

    hide fumi with Dissolve(0.25)

    show miyako z4 2 lg pyjama a
    show fumi z4 1 lg pyjama h:
        xcenter 172
    show hina z4 1 lg pyjama d:
        xcenter 852
    with Dissolve(0.25)

    voice "2HI_1392"
    hina "\"Your store's been really busy lately, huh?\""

    voice "2FU_1134"
    if persistent.dpatch:
        fumi "\"I know I shouldn't be skipping school for this, but...\"" id a10_cou2_06_ffcb336b
    else:
        fumi "\"I know I shouldn't be skipping class for this, but...\""

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_1036"
    miyako "\"You don't have a choice. It's Valentine's Day.\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_1135"
    fumi "\"It is. Of all times, right?\""

    show hina z4 2 lg pyjama a with dict_dissolve_25

    voice "2HI_1393"
    hina "\"I'll take notes for you.\""

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_1136"
    fumi "\"Thank you. That'll help.\""

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_1137"
    fumi "\"I can prepare your lunches tonigh—\""

    show hina z4 1 lg pyjama a with dict_dissolve_25

    voice "2HI_1394"
    hina "\"You don't need to worry about that. We can always buy our lunches. Oh, I'll wash the lunchboxes.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_1037"
    miyako "\"I'll help.\""

    hide hina
    hide miyako
    with dict_dissolve_25

    "Hina and Miyako went to the kitchen without letting Fumi finish."

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_1138"
    fumi "\"Oh...\""

    "Fumi put her hands together in thanks."

    show rin z4 2 lg pyjama glasses e:
        xcenter 726
    with dict_dissolve_25

    voice "2RI_1360"
    rin "\"Is there anything I can do?\""

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_1139"
    fumi "\"It's only one day. Your concern is enough.\""

    show rin z4 2 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_1361"
    rin "\"Okay...\""

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_1140"
    fumi "\"More importantly...\""

    show rin z4 2 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1362"
    rin "\"Oh... yeah.\""

    "Rin had been trying to talk to Hina, but hadn't been able to get the timing right."

    "Hina seemed to have noticed, but was waiting on Rin."

    "Noticing this, Fumi gave Rin some encouragement."

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_1363"
    if persistent.dpatch:
        rin "\"Hina, after school tomorrow, can we talk?\"" id a10_cou2_06_7e63456c
    else:
        rin "\"Hina, after class tomorrow, can we talk?\""

    $ side_image = "hina 2 side pyjama d"

    voice "2HI_1395"
    hina "\"Okay... sure.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
