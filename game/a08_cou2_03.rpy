label a08_cou2_03:

    scene bg02dh with Dissolve(0.5)
    pause 1.5

    play music bgm02

    "After they'd all gotten into their beds, Miyako fell asleep right away, but..."

    show rin 3 lg nightlight pyjama glasses_g with dict_dissolve_25

    voice "2RI_0672"
    rin "\"Ngh...\"" id a08_cou2_03_9501c735

    "Rin groaned when she turned the page of her book."

    show hina 3 lg dark pyjama_pjm b with dict_dissolve_25

    voice "2HI_0660"
    hina "\"Rin?\"" id a08_cou2_03_63ea1809

    "Hina heard it from the bed underneath her."

    show rin 3 lg nightlight pyjama glasses_b with dict_dissolve_25

    voice "2RI_0673"
    rin "\"Oh, you're still up? That's unusual.\"" id a08_cou2_03_eb62dbab

    show hina 3 lg dark pyjama_pjm d with dict_dissolve_25

    voice "2HI_0661"
    hina "\"Yeah. What was that sound? You okay?\"" id a08_cou2_03_d3617db8

    show rin 3 lg nightlight pyjama glasses_c with dict_dissolve_25

    voice "2RI_0674"
    rin "\"Oh, my finger just hurt a bit. Caught my cut on the edge of the page.\"" id a08_cou2_03_115b4958

    voice "2HI_0662"
    hina "\"The cut from when I bit you?\"" id a08_cou2_03_6e682733

    show rin 3 lg nightlight pyjama glasses_b with dict_dissolve_25

    voice "2RI_0675"
    rin "\"Yeah. It might be a little swollen.\"" id a08_cou2_03_6ed5eb2c

    show hina 3 lg dark pyjama_pjm f with dict_dissolve_25

    voice "2HI_0663"
    hina "\"...I'm sorry.\"" id a08_cou2_03_2e49f4cb

    "Hina curled up in her bed, remorseful."

    voice "2RI_0676"
    rin "\"Well, I didn't really clean it or anything. I just left it alone.\"" id a08_cou2_03_6ae1631c

    voice "2HI_0664"
    hina "\"......\"" id a08_cou2_03_75fa44d4

    show rin 3 lg nightlight pyjama glasses_h with dict_dissolve_25

    voice "2RI_0677"
    rin "\"Ugh... It hurts. What if I get rabies~?\"" id a08_cou2_03_6fa5ff5a

    show hina 3 lg dark pyjama_pjm h with dict_dissolve_25

    voice "2HI_0665"
    hina "\"Awawa...\"" id a08_cou2_03_1223f2ca

    "Rin was exaggerating her pain, but Hina was almost crying, taking her seriously."

    show hina 3 lg dark pyjama_pjm k with dict_dissolve_25

    voice "2HI_0666"
    hina "\"What if you lose your finger... because of me...?\"" id a08_cou2_03_74e2315f

    "Her voice was thick now. Rin realized she'd overdone it."

    show rin:
        "rin 3 lg nightlight pyjama glasses_f" with Dissolve(0.25)
        6.5
        "rin 3 lg nightlight pyjama glasses_h" with Dissolve(0.25)

    voice "2RI_0678"
    rin "\"No, hey... I was joking. It'll get better in no time if I just lick it... mmn... Ow!\"" id a08_cou2_03_f46c8271

    show rin 3 lg nightlight pyjama glasses_h:
        pass
    with None

    "I guess that stung."

    show hina 3 lg dark pyjama_pjm g with dict_dissolve_25

    voice "2HI_0667"
    hina "\"Aaah!\"" id a08_cou2_03_fa492bc8

    show rin 3 lg nightlight pyjama glasses_c with dict_dissolve_25

    voice "2RI_0679"
    rin "\"It's fine! I'll go get some antiseptic and a band-aid from Sachiko—\"" id a08_cou2_03_a717b07c

    "Rin sat up and made to get off her bed, but..."

    hide rin
    hide hina
    with Dissolve(0.25)

    show hina 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0668"
    hina "\"I'll go!\"" id a08_cou2_03_45cbe81d

    hide hina with dict_dissolve_25

    "Hina leapt out of bed quicker, and was out the door in the next moment."

    show rin 3 sm nightlight pyjama glasses_f with dict_dissolve_25

    voice "2RI_0680"
    rin "\"Okay...\"" id a08_cou2_03_86a35eda

    show fumi 3 sm dark pyjama b with dict_dissolve_25

    voice "2FU_0537"
    fumi "\"Ogata?\"" id a08_cou2_03_5b8bb220

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "2RI_0681"
    rin "\"Ah, yeah?\"" id a08_cou2_03_49760665

    show fumi 3 sm dark pyjama d with dict_dissolve_25

    voice "2FU_0538"
    fumi "\"You shouldn't do that. You know Natsume takes everything to heart.\"" id a08_cou2_03_7d711ad1

    show rin 3 sm nightlight pyjama glasses_c with dict_dissolve_25

    voice "2RI_0682"
    rin "\"Er, I mean, I was just teasing her a little...\"" id a08_cou2_03_2ac0f229

    voice "2FU_0539"
    fumi "\"......\"" id a08_cou2_03_03a72435

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "2RI_0683"
    rin "\"...I'm sorry.\"" id a08_cou2_03_1ec86bc8

    show fumi 3 sm dark pyjama c with dict_dissolve_25

    voice "2FU_0540"
    fumi "\"Please tell Natsume that.\"" id a08_cou2_03_d7f8dbe8

    voice "2RI_0684"
    rin "\"...Right.\"" id a08_cou2_03_3379b102

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
