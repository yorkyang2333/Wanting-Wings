label a10_cou2_02:

    scene expression "gui/kimikara/mainmenu_ground1.webp"
    show expression "gui/kimikara/title2.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter10b with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    "A break between classes."

    $ side_image = "hina 2 side school e"

    voice "2HI_1377"
    hina "\"I'm going to the bathroom.\""

    "Hina told Fumi and stood."

    "Fumi watched her leave the classroom and then stood herself and headed to Rin's desk."

    show rin z4 2 lg school b:
        xcenter 298
    with dict_dissolve_25

    voice "2RI_1314"
    rin "\"......\""

    "Rin was staring absentmindedly out the window."

    show fumi z4 1 lg school h:
        xcenter 726
    with dict_dissolve_25

    voice "2FU_1110"
    fumi "\"Ogata.\""

    show rin z4 2 lg school g with dict_dissolve_25

    voice "2RI_1315"
    rin "\"Hm? Yeah?\""

    show fumi z4 1 lg school k with dict_dissolve_25

    voice "2FU_1111"
    fumi "\"Something really did happen between you two last night, didn't it?\""

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1316"
    rin "\"Geez, how many times have you asked me that now? I keep telling you you're worrying over nothing.\""

    "Yes. Fumi had asked several times."

    "She'd realized instantly when the two had returned to the room. They'd looked the same as always at a glance, but something was off between them."

    "When she'd asked about it, they'd both said nothing had happened, and when she took them aside separately, they both still denied it."

    show rin z4 1 lg school f with dict_dissolve_25

    voice "2RI_1317"
    rin "\"Do we really look that weird~?\""

    "Rin was laughing it off as usual."

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_1112"
    fumi "\"I'm sorry, but you do.\""

    "But Fumi wasn't buying it."

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_1318"
    rin "\"I'm telling you, nothing happened...\""

    "She denied it again. Averting her eyes this time."

    show fumi z4 1 lg school k with dict_dissolve_25

    voice "2FU_1113"
    fumi "\"......\""

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1319"
    rin "\"We just had a little tiny misunderstanding. But it's fine. We'll make up in no time.\""

    "Rin confessed, succumbing to Fumi's silent stare."

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_1114B"
    fumi "\"Do you have an idea of how to?\""

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1320"
    rin "\"Uhh, you know, a little fooling around and we'll be good as new. Hina's not complicated, you know?\""

    show fumi z4 2 lg school h with dict_dissolve_25

    voice "2FU_1115"
    fumi "\"Ah...\""

    "Fumi caught on, as usual."

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1321"
    rin "\"So, sorry to spring this on you, but, you know, could you give us some time today?\""

    "Rin put her hands together, pleading."

    show fumi z4 2 lg school a with dict_dissolve_25

    voice "2FU_1116"
    fumi "\"Alright. Miya—\""

    $ side_image = "miyako 1 side school_a b"

    voice "2MI_1032"
    miyako "\"Yes, I'd like to have some tea with you on the way home, Fumi.\""

    "With just a look from Fumi, Miyako instantly picked up on the implication."

    voice "2RI_1322"
    rin "\"Thanks for doing this all the time, guys... I'm kinda embarrassed about it~\""

    "Rin laughed, but it was a little strained."

    voice "2FU_1117"
    fumi "\"......\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
