label a09_cou2_06:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    if persistent.dpatch:
        "—After school." id a09_cou2_06_fe776d95
    else:
        "—After class."

    $ side_image = "hina 2 side school f"

    voice "2HI_1026"
    hina "\"...?\""

    "The hallway in front of the classroom. Hina passed by a girl on her way back from the faculty room."

    "The girl bounded away while Hina watched."

    "It was the girl who'd asked Rin a question about class. I think her name was Honjou."

    $ side_image = "hina 2 side school d"

    voice "2HI_1027"
    hina "\"......\""

    pause 0.5

    play sound se000c

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    show rin 2 sm school a at pos_ls with dict_dissolve_50
    show hina:
        "hina 2 sm school d flat"
        alpha 0.0 xcenter 832
        easein 0.75 alpha 1.0 xcenter 732

    "Hina entered the classroom to find Rin standing at the window. No one else was there."

    show hina 2 sm school d:
        alpha 1.0 xcenter 732
    with None
    show rin 1 sm school b with dict_dissolve_25

    voice "2RI_1009"
    rin "\"Y-You're back. Asou and Mikoyan went to the bathroom—\""

    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_1028"
    hina "\"Honjou was just here. Were you talking about something?\""

    show rin 2 sm school e with dict_dissolve_25

    voice "2RI_1010"
    rin "\"No... yeah. But it wasn't important.\""

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_1029"
    hina "\"......\""

    "Rin tried to brush it off, but Hina merely waited for elaboration."

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_1011"
    rin "\"Uhh... she said she was gonna give me chocolates for Valentine's.\""

    voice "2HI_1030"
    hina "\"And what did you say?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_1012"
    rin "\"Well... I said, 'Thanks.'\""

    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_1031"
    hina "\"You're gonna accept them?\""

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1013"
    rin "\"No, I wanted to turn them down...! But I couldn't think of a good excuse off the top of my head.\""

    "Rin was panicking just from Hina's continued eye contact."

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_1014"
    rin "\"I-I told her I don't like sweets...!\""

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_1032"
    hina "\"......\""

    "Hina thought for a moment, then slowly started..."

    show hina 2 sm school h with dict_dissolve_25

    voice "2HI_1033"
    hina "\"Listen—\""

    play sound se000c

    $ side_image = "miyako 1 side school_a b"

    voice "2MI_0878"
    miyako "\"Sorry that took so long~\""

    $ side_image = "fumi 1 side school b"

    voice "2FU_0822"
    fumi "\"Oh, Natsume's back.\""

    "Fumi and Miyako had returned."

    show hina 1 sm school a with dict_dissolve_25

    voice "2HI_1034"
    hina "\"Hey, guys.\""

    "Letting her gaze drop for just a second, Hina turned to them. Her voice and her expression were those of the usual Hina."

    show hina 1 sm school p with dict_dissolve_25

    voice "2HI_1035"
    hina "\"I'll get ready to go right away~\""

    hide hina with dict_dissolve_25

    "She went to her desk and swiftly prepared to head home."

    show rin 1 sm school h with dict_dissolve_25

    voice "2RI_1015"
    rin "\"Umm, Hina—\""

    $ side_image = "hina 2 side school a"

    voice "2HI_1036"
    hina "\"Oh, I'm gonna check the locks on the windows, so you can leave first~\""

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_1016"
    rin "\"Uhh... right.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared >= 2:
        jump a09_cou4_03
    elif routes_cleared == 1:
        jump a09_comn_12
    else:
        jump a09_cou2_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
