label a04_cou2_04:

    if persistent.dpatch:
        jump a04_cou2_04_d
    else:
        pause 2.0
        "........."
        "......"
        window hide
        pause 2.0
        window auto

label a04_cou2_04_d_end:

    scene black with bg_effect_05
    pause 0.5

    scene bg02ba with bg_effect_05
    pause 0.5

    "Having changed their clothes, the two sat on the edge of the bed, each with a bottle of mineral water."

    show rin 1 lg pyjama a at pos_l
    show hina 2 lg pyjama g at pos_r
    with Dissolve(0.25)

    voice "HIN_1399"
    hina "\"I want to be your dog, Rin.\"" id a04_cou2_04_d_end_f5a466be

    show rin:
        "rin 1 lg pyjama j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1165"
    rin "\"Pfft... What?\"" id a04_cou2_04_d_end_fcfd3bbe

    show rin 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_1400"
    hina "\"You know, the author of that book. Their other story.\"" id a04_cou2_04_d_end_63aa345c

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_1166"
    rin "\"O-Oh... that. 'Cause of what we just did, I thought...\"" id a04_cou2_04_d_end_a044c7dd

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1401"
    hina "\"You thought what?\"" id a04_cou2_04_d_end_1e9a62cd

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1167"
    rin "\"Umm... you know—\"" id a04_cou2_04_d_end_c17cb0de

    "Rin whispered to Hina."

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1402"
    hina "\"I don't need butter or jam, I'll still—mggh!\"" id a04_cou2_04_d_end_86a493b5

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_1168"
    rin "\"I get it already!\"" id a04_cou2_04_d_end_4f06bcfa

    "Rin covered Hina's mouth."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1403"
    hina "\"It was about how they wanted to become a dog and serve the person they love forever in return for their affection, right?\"" id a04_cou2_04_d_end_01c7ec5d

    show rin 1 lg pyjama e with dict_dissolve_25

    voice "RIN_1169"
    rin "\"Hm? How far into that book did you get, Hina?\"" id a04_cou2_04_d_end_0b5f9b55

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_1404"
    hina "\"Umm, up to where the bartender turned Fusae into a dog.\"" id a04_cou2_04_d_end_eff305d8

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_1170"
    rin "\"Ah, I see... I think maybe you should stop there.\"" id a04_cou2_04_d_end_0ce6547e

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1405"
    hina "\"What? Why?\"" id a04_cou2_04_d_end_abf84ba0

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_1171"
    rin "\"I think the rest might be a bit beyond you. But I'll lend you another one.\"" id a04_cou2_04_d_end_237935a5

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1406"
    hina "\"O-Okay.\"" id a04_cou2_04_d_end_adf41836

    "Apparently she didn't want Hina reading the rest of that book."

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_1172"
    rin "\"Honestly, though... how many steps on the stairs to perversion are you planning on skipping?\"" id a04_cou2_04_d_end_6a0a2642

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_1407"
    hina "\"Am I... perverted? I just want to make you happy, Rin.\"" id a04_cou2_04_d_end_78b8798d

    show rin 1 lg pyjama h with dict_dissolve_25

    voice "RIN_1173"
    rin "\"I think there's a misunderstanding here. I'm not a pervert.\"" id a04_cou2_04_d_end_d6ef1bbb

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1408"
    hina "\"You're not?\"" id a04_cou2_04_d_end_54c077e9

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_1174"
    rin "\"I'm not.\"" id a04_cou2_04_d_end_9888401b

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1409"
    hina "\"I thought if I did the stuff in the books you like, you'd be happy.\"" id a04_cou2_04_d_end_c72dbfe5

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1175"
    rin "\"How simplistic. That's very like you, though.\"" id a04_cou2_04_d_end_1ddeb907

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1410"
    hina "\"I really do want to be your dog though, Rin.\"" id a04_cou2_04_d_end_949d3056

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_1176"
    rin "\"Do you really know what that means?\"" id a04_cou2_04_d_end_88cfa766

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_1411"
    hina "\"I don't, but... I want all of me to belong to you, Rin.\"" id a04_cou2_04_d_end_3d9824f6

    "Her face was utterly serious."

    show rin 1 lg pyjama e with dict_dissolve_25

    voice "RIN_1177"
    rin "\".........\"" id a04_cou2_04_d_end_4c75d2a1

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1412"
    hina "\"...Can I?\"" id a04_cou2_04_d_end_58848224

    show rin:
        "rin 1 lg pyjama g" with Dissolve(0.25)
        ShakeTameiki

    "Rin sighed, then poured some water into her hand and held it out to Hina."

    show rin 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None

    "Hina innocently lapped it up."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1413"
    hina "\"Eheheh♪\"" id a04_cou2_04_d_end_1e740c8d

    show rin 1 lg pyjama h with dict_dissolve_25

    voice "RIN_1178"
    rin "\".........\"" id a04_cou2_04_d_end_6dbaee0c

    "Patting Hina's head, Rin fell into thought."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
