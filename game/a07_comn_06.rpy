label a07_comn_06:

    if route2 == 1:
        scene bg01cg with Dissolve(0.5)
    else:
        scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Lounging around after dinner."

    "The table had gotten busier, but time passed just as idly after Miyako joined the three girls."

    play sound se_2s_j004

    scene white with Dissolve(0.1875)
    pause 1.0625

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_aa with Dissolve(0.25)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_ba with Dissolve(0.25)
    pause 0.75

    voice "2FU_0073"
    fumi "\"Here we go...\""

    "Setting down four mugs, Fumi took a seat."

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_ae with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_be with Dissolve(0.2)
    pause 0.6

    voice "2MI_0053"
    miyako "\"...What's this?\""

    "Miyako sniffed the steam coming from the mug."

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_ab with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bb with Dissolve(0.2)
    pause 0.6

    voice "2FU_0074"
    fumi "\"I made apple tea tonight. By boiling apple peels, not with tea bags.\""

    voice "2MI_0054"
    miyako "\"So this is apple tea. It's a beautiful color, too.\""

    "Her curious gaze was reflected in the liquid inside the mug."

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_af with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bf with Dissolve(0.2)
    pause 0.6

    voice "2RI_0096"
    rin "\"Takaoka, is this your first time having apple tea?\""

    voice "2MI_0055"
    miyako "\"Yes.\""

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_ai with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bi with Dissolve(0.2)
    pause 0.6

    voice "2FU_0075"
    fumi "\"Try it. It's really good♪\""

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_ag with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bg with Dissolve(0.2)
    pause 0.6

    voice "2HI_0100"
    hina "\"Apple tea's always kinda rubbed me the wrong way.\""

    "Hina piped up from under the table."

    voice "2HI_0101"
    hina "\"I mean, apple tea doesn't taste like apples at all. It smells like them, though.\""

    voice "2RI_0097"
    rin "\"Aha.\""

    voice "2HI_0102"
    hina "\"The first sip always fools me.\""

    voice "2FU_0076"
    fumi "\"It does just taste like tea if you don't put sugar in it.\""

    voice "2RI_0098"
    rin "\"Widdle baby Hina can have some apple juice.\""

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_ah with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bh with Dissolve(0.2)
    pause 0.6

    voice "2HI_0103"
    hina "\"I'll drink it, okay?!\""

    if route2 == 1:
        voice "2FU_0077"
        fumi "\"I have this for you, Hina.\""
    else:
        voice "2FU_0078"
        fumi "\"I have this for you, Natsume.\""

    "Fumi held out..."

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_ag with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bg with Dissolve(0.2)
    pause 0.6

    voice "2HI_0104"
    hina "\"An apple!\""

    voice "2FU_0079"
    fumi "\"Since I only used the peel.\""

    voice "2HI_0105"
    hina "\"I'll eat it~\""

    "This, Hina was happy to receive."

    play sound se_2s_h019
    pause 0.5

    voice "2HI_0106"
    hina "\"Apples smell like apples and taste like apples!\""

    voice "2RI_0099"
    rin "\"I'll alert the media.\""

    voice "2MI_0056"
    miyako "\"......\""

    "Miyako looked curiously at Hina."

    "Hina associated apples with a taste and smell from her previous experiences, which was why apple tea offended her."

    "But Miyako, tasting both apples and apple tea for the first time, had no such associations, so it {i}was{/i} news to her, in a way."

    voice "2FU_0080"
    fumi "\"Would you like some apple too, Miyako?\""

    "Fumi offered, noticing her staring."

    if rin_pyjama == "pyjama_a":
        scene kimikara_01_aj with Dissolve(0.2)
    elif rin_pyjama == "pyjama_b":
        scene kimikara_01_bj with Dissolve(0.2)
    pause 0.6

    voice "2MI_0057"
    miyako "\"Yes, please.\""

    "Miyako {i}knew{/i} that apple tea smelled like apples and that apples tasted like apples."

    "But she had never {i}experienced{/i} that smell or taste."

    "For her, experience came after knowledge, not the other way around."

    "Having a sense of color now, she could distinguish between green and red apples, but learning the difference in their flavors would be a future experience for her."

    voice "2MI_0058"
    miyako "\"I'll try the apple tea first.\""

    voice "2FU_0081"
    fumi "\"It's still hot, so be—\""

    "Miyako put the mug to her lips before Fumi could warn her."

    voice "2MI_0059"
    miyako "\"Augh?!\""

    "Ah, yes, that heat, too."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    if route2 == 1:
        jump a07_cou1_01
    elif route2 == 2:
        jump a07_cou2_01
    elif route2 == 3:
        jump a07_cou3_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
