label a09_comn_01:

    scene bg04aa
    show bg_obi
    with Dissolve(0.5)
    pause 1.5

    play music bgm01

    if routes_cleared < 2:
        jump a09_comn_01_a
    else:
        jump a09_comn_01_b

label a09_comn_01_a:

    "The air in the classroom was more strained than usual. They were in the middle of proficiency exams."

    "The sound of pencils scraping against answer sheets, of the teacher walking in between the desks."

    show fumi 1 lg school a with dict_dissolve_25

    voice "2FU_0574"
    fumi "\"......\""

    "Fumi was checking over her answers."

    hide fumi with Dissolve(0.25)

    show hina 1 lg school j with dict_dissolve_25

    voice "2HI_0732"
    hina "\"Nnh~\""

    "Hina was busy writing and erasing. She seemed to be having a tough time."

    hide hina with Dissolve(0.25)

    show rin 1 lg school b with dict_dissolve_25

    voice "2RI_0745"
    rin "\".........\""

    "Finishing quickly, Rin was absentmindedly spinning a pen."

    play sound se_2s_h035

    show rin 1 lg school e with dict_dissolve_25

    voice "2RI_0746"
    rin "\"Ah...!\""

    hide rin with dict_dissolve_25

    "The pen flew out of her hand, attracting a glare from the teacher."

    "As for Miyako..."

    show miyako 2 lg school i with dict_dissolve_25

    voice "2MI_0563a"
    miyako "\"......\""

    show miyako:
        "miyako 1 lg school_a f" with Dissolve(0.25)
        ShakeSide

    voice "2MI_0563"
    miyako "\"Ah!\""

    show miyako 1 lg school_a f:
        xoffset 0 yoffset 0
    with None

    "She'd been nodding off, but the sound of Rin's pen hitting the floor woke her up."

    show miyako 1 lg school_a i with dict_dissolve_25

    voice "2MI_0564"
    miyako "\"......\""

    "She hurriedly looked down at her exam."

    jump a09_comn_01_end

label a09_comn_01_b:

    "The air in the classroom was more strained than usual. They were in the middle of proficiency exams."

    "The sound of pencils scraping against answer sheets, of the teacher walking in between the desks."

    show fumi 1 lg school a with dict_dissolve_25

    voice "2FU_0574"
    fumi "\"......\""

    "Fumi was checking over her answers."

    show fumi 1 lg school e with dict_dissolve_25

    voice "2FU_0575"
    fumi "\"...Oh.\""

    "A careless mistake. She erased an answer with a small sound of recognition."

    hide fumi with Dissolve(0.25)

    show hina 1 lg school j with dict_dissolve_25

    voice "2HI_0732"
    hina "\"Nnh~\""

    "Hina was busy writing and erasing. "

    "She seemed to be struggling to fully pull out the answers from her brain."

    show hina 1 lg school c with dict_dissolve_25

    voice "2HI_0733"
    hina "\"Oh!\""

    "Her expression lit up. She must have remembered something. She nodded a few times as she wrote an answer down."

    hide hina with Dissolve(0.25)

    show rin 1 lg school b with dict_dissolve_25

    voice "2RI_0745"
    rin "\".........\""

    "Finishing quickly, Rin was absentmindedly spinning a pen."

    show rin 1 lg school g with dict_dissolve_25

    "The pen almost flew out of her hand, but she just managed to catch it."

    show rin:
        "rin 1 lg school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0747"
    rin "\"Whew...\""

    show rin 1 lg school k:
        xoffset 0 yoffset 0
    with None
    hide rin with dict_dissolve_25

    "As for Miyako..."

    show miyako 1 lg school_a l with dict_dissolve_25

    voice "2MI_0565"
    miyako "\"Zzz, zzz...\""

    "She was snoozing even though only half of her answer sheet was filled in."

    "Well, that's not good."

    show miyako:
        "miyako 1 lg school_a k" with Dissolve(0.25)
        ShakeJump

    voice "2MI_0566"
    miyako "\"—!!\""

    show miyako 1 lg school_a k:
        xoffset 0 yoffset 0
    with None

    "Miyako suddenly jolted awake."

    "All the students around her and the teacher looked at her."

    show miyako 2 lg school c with dict_dissolve_25

    voice "2MI_0567"
    miyako "\"Hahaha...\""

    "She looked awkwardly at her answer sheet."

    "—That scared me."

label a09_comn_01_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        scene expression "gui/kimikara/mainmenu_ground1.webp"
        show expression "gui/kimikara/title2.webp"
        with Dissolve(0.5)
        pause 1.5

        show chapter09a with Dissolve(1.5)
        pause 3.0

        scene black with Dissolve(0.5)
        pause 1.5
    elif route2 == 2:
        scene expression "gui/kimikara/mainmenu_ground1.webp"
        show expression "gui/kimikara/title2.webp"
        with Dissolve(0.5)
        pause 1.5

        show chapter09b with Dissolve(1.5)
        pause 3.0

        scene black with Dissolve(0.5)
        pause 1.5
    elif route2 == 3:

        scene expression "gui/kimikara/mainmenu_ground1.webp"
        show expression "gui/kimikara/title2.webp"
        with Dissolve(0.5)
        pause 1.5

        show chapter09c with Dissolve(1.5)
        pause 3.0

        scene black with Dissolve(0.5)
        pause 1.5


    if routes_cleared == 1:
        jump a09_comn_02

    elif routes_cleared != 0:
        jump a09_comn_04
    else:

        if route2 == 1:
            jump a09_cou1_01
        elif route2 == 2:
            jump a09_cou2_01
        elif route2 == 3:
            jump a09_cou3_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
