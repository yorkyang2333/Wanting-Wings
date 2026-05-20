label a11_cou4_14:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_14:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg02dd with Dissolve(0.25)
    pause 0.75

    play music bgm02 fadein 1.0

    "It was late at night, and everyone was in bed."

    "Well, everyone except one person..."

    show fumi 3 sm nightlight pyjama h with dict_dissolve_25

    voice "2FU_1315"
    fumi "\"'It was another great day today.'\""

    "Fumi quietly closed her diary in her bed."

    show rin 3 sm light pyjama glasses b with dict_dissolve_25

    voice "2RI_1722"
    rin "\"Especially for a certain pair.\""

    "Rin closed her book as well, eyeing the bed beside hers."

    show hina 3 sm light pyjama_pjm e with dict_dissolve_25

    voice "2HI_1624"
    hina "\"Think she's gonna stay over there tonight?\""

    "Miyako's bed was empty, but they all had an idea where she was sleeping."

    "The three chatted for a bit in bed, all celebrating Miyako's and Sachiko's happy ending."

    show rin 3 sm light pyjama glasses c with dict_dissolve_25

    voice "2RI_1723"
    rin "\"You think Mikoyan will be able to get up tomorrow morning~?\""

    show hina 3 sm light pyjama_pjm h with dict_dissolve_25

    voice "2HI_1625"
    hina "\"Hey.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_15
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
