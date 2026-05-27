label a03_comn_06:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg02aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    "Sunday morning."

    show hina 1 sm pyjama a
    show rin 1 sm pyjama c at pos_r2
    show fumi 1 sm school_scarf b at pos_l2
    with Dissolve(0.25)

    voice "FUM_0500"
    fumi "\"Okay, I'm going home. I should be back by dinnertime.\"" id a03_comn_06_a348112b

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0679"
    hina "\"Seems like a lot of work to go back every other week.\"" id a03_comn_06_d19b72ce

    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "FUM_0501"
    fumi "\"Well, it's not far, and this way, my mom won't worry.\"" id a03_comn_06_11e0d876

    "Fumi gave a bit of a strained smile."

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "FUM_0502"
    fumi "\"I'll order a Christmas cake, too.\"" id a03_comn_06_b7e9d6ff

    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0680"
    hina "\"Sounds good.\"" id a03_comn_06_304ec16c

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0503"
    fumi "\"And this time, I'll make sure my dad doesn't mess it up.\"" id a03_comn_06_be1d4587

    show rin 1 sm pyjama d with dict_dissolve_25

    voice "RIN_0554"
    rin "\"Ahaha. What if we get a wedding cake this time?\"" id a03_comn_06_d73baecd

    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "FUM_0504"
    fumi "\"Even he wouldn't make that mistake! ...I wish I could be 100%% sure about that~\"" id a03_comn_06_fc221fe6

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0505"
    fumi "\"Anyway, I'll be back later.\"" id a03_comn_06_bdd8f4d5

    show hina 1 sm pyjama c
    show rin 1 sm pyjama c
    with dict_dissolve_25

    $ voice2("hina","HIN_0681","rin","RIN_0555")
    hina_rin "\"See you.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if (route1 == 1 or route1 == 2) and rin_hina_score > hina_fumi_score:
        jump a03_cou2_05
    else:
        jump a03_cou1_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
