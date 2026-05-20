label a04_comn_01:





    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm school a
    show fumi 1 sm school a at pos_l2
    show rin 1 sm school a at pos_r2
    with Dissolve(0.25)

    voice "RIN_0910"
    rin "\"Ehm~ I have an announcement to make.\""

    "Rin returned to the classroom as Hina and Fumi were locking it up."

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0967"
    hina "\"Wait, when'd you leave?\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0807"
    fumi "\"We were just about to lock the doors.\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0911"
    rin "\"You didn't notice me leave?\""

    show hina 1 sm school e with dict_dissolve_25

    voice "HIN_0968"
    hina "\"Well, it's pretty rare for you to not be here.\""

    show fumi 1 sm school b with dict_dissolve_25

    if hina_fumi_score != 999:

        voice "FUM_0808"
        fumi "\"We're usually waiting for Natsume. So what's your announcement?\""
    else:


        voice "FUM_0809"
        fumi "\"We're usually waiting for Hina. So what's your announcement?\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0912"
    rin "\"Well, I just talked to the biology teacher.\""

    show fumi 1 sm school a
    show hina 1 sm school k
    with dict_dissolve_25

    "She was met with blank faces in response."

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0913"
    rin "\"The feather from the other day has been identified.\""

    play sound se558b

    show rin:
        ShakeYes

    if persistent.dpatch:
        "Rin pulled a small plastic bag out of her school bag. Inside was the feather in question." id a04_comn_01_a9350ede
    else:
        "Rin pulled a small plastic bag out of her backpack. Inside was the feather in question."

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school e with dict_dissolve_25

    "Recognition dawned on the other two's faces."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_0914"
    rin "\"This feather...\""

    "Hina and Fumi held their breath, awaiting Rin's next words."

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_0915"
    rin "\"...Belongs to a goose. Is there perhaps a down comforter, or... {i}jacket{/i}... in our room?\""

    voice "FUM_0810"
    fumi "\"Ah...\""

    "Their eyes settled on Hina."

    show hina 1 sm school d with dict_dissolve_25

    voice "HIN_0969"
    hina "\"Huh? Me?\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0811"
    fumi "\"It {i}is{/i} getting a little worn.\""

    show hina 1 sm school l with dict_dissolve_25

    voice "HIN_0970"
    hina "\"Wait a second, down jackets don't have feathers that big in them, do they?\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0916"
    rin "\"I guess cheap ones sometimes do.\""

    show hina 1 sm school i with dict_dissolve_25

    voice "HIN_0971"
    hina "\"Stop giving me that pitying look.\""

    voice "FUM_0812"
    fumi "\"Be nice.\""

    show rin 1 sm school d with dict_dissolve_25

    voice "RIN_0917"
    rin "\"...In other words, the culprit was Hina.\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0972"
    hina "\"Hey, don't call me that!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school h with dict_dissolve_25

    voice "FUM_0813"
    fumi "\"Mmh...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_01
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_01
    else:
        jump a04_cou1_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
