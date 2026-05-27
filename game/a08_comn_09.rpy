label a08_comn_09:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    if persistent.dpatch:
        "After school. The three were returning from the store." id a08_comn_09_69631eb7
    else:
        "After class. The three were returning from the store."

    show fumi 1 sm school_scarf a at pos_ls
    show rin 1 sm school_scarf a at pos_rs
    with dict_dissolve_25

    voice "2RI_0556"
    rin "\"It's been snowing on and off all day.\"" id a08_comn_09_08b5fbf8

    "It was snowing now, too. Lightly, though."

    voice "2FU_0471"
    fumi "\"It's not likely to stay on the ground at this rate.\"" id a08_comn_09_61833473

    "In fact, most of the snow from the morning was gone."

    "People were walking and driving over it in town, and it melted faster on asphalt and concrete than on dirt."

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "2RI_0557"
    rin "\"Good. If there's snow on the ground, people are likely to slip like a certain someone.\"" id a08_comn_09_d8d3150d

    show fumi:
        "fumi 1 sm school_scarf d" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_0472"
    fumi "\"Ahaha, that was dangerous this morning.\"" id a08_comn_09_11a1a4d9

    show fumi 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None

    "Hina had run off into the snow and almost tripped this morning."

    "But with her superior reflexes, she'd managed to regain her balance with a bit of a dance."

    show rin 1 sm school_scarf f with dict_dissolve_25

    voice "2RI_0558"
    rin "\"Hey, someone.\" " id a08_comn_09_eb1bf2e9

    "She called out to Hina, who was ahead of them, staying out of the conversation."

    $ side_image = "hina 2 side school_scarf g"

    voice "2HI_0540"
    hina "\"I wanna go to the beach.\"" id a08_comn_09_92941509

    show fumi 1 sm school_scarf e
    show rin 1 sm school_scarf e
    with dict_dissolve_25

    voice "2RI_0559"
    rin "\"Huh?\"" id a08_comn_09_fac1d5cb

    "Rin was taken aback by Hina's words when she turned around."

    $ side_image = "hina 2 side school_scarf d"

    voice "2HI_0541"
    hina "\"The beach.\"" id a08_comn_09_e8a87c82

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0560"
    rin "\"Uh, I heard you. But that's kinda out of the blue in this chill, don't you think? You wanna do a polar bear plunge or something?\"" id a08_comn_09_e67c1e30

    show fumi:
        "fumi 1 sm school_scarf d" with Dissolve(0.25)
        ShakeNo

    voice "2FU_0473"
    fumi "\"Ugh, that sounds cold~\"" id a08_comn_09_828b3860

    show fumi 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None

    "Fumi clutched herself and shivered just hearing the phrase."

    "\"A winter beach\" sounds like lyrics from some kind of ballad."

    $ side_image = "hina 1 side school_scarf a"

    voice "2HI_0542"
    hina "\"No, not now. I mean in the summer.\"" id a08_comn_09_0be948a9

    show fumi 1 sm school_scarf b
    show rin 1 sm school_scarf a
    with dict_dissolve_25

    $ voice2("rin","2RI_0561","fumi","2FU_0474")
    rin_fumi "\"Ah.\""

    "Rin and Fumi understood."

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0562"
    rin "\"Getting a little ahead of yourself there, aren't you? What made you think of the beach in the middle of this cold?\"" id a08_comn_09_0070e04b

    $ side_image = "hina 1 side school_scarf p"

    voice "2HI_0543"
    hina "\"We bought some gas for a portable stove at the store, right? So then I was thinking about gas, and went from gas to bus, and then to bus stop...\"" id a08_comn_09_3f68c448

    $ side_image = "hina 1 side school_scarf c"

    voice "2HI_0543a"
    hina "\"And then when we left the store it was snowing, and I thought of, you know, marine snow—which is in the ocean. See!\"" id a08_comn_09_975b2590

    show rin:
        "rin 1 sm school_scarf j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_0563"
    rin "\"What do you mean, 'See!'? What was the point of the first half?!\"" id a08_comn_09_f683c531

    show rin 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side school_scarf l"

    voice "2HI_0544"
    hina "\"Oh, you're right!\"" id a08_comn_09_97993f63

    show fumi 2 sm school_scarf i with dict_dissolve_25

    voice "2FU_0475"
    fumi "\"Ahaha. It'd be fun to go swimming with everyone, though.\"" id a08_comn_09_2b78711e

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0564"
    rin "\"We'd have to travel to get to the beach from here. You don't just want to go to the pool?\"" id a08_comn_09_f1806b5b

    show fumi 2 sm school_scarf f with dict_dissolve_25
    $ side_image = "hina 1 side school_scarf f"

    $ voice2("hina","2HI_0545","fumi","2FU_0476N")
    hina_fumi "\"No way.\"\n\"I don't think so.\"" (what_rest_indent=0)

    show rin:
        "rin 1 sm school_scarf g" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0565"
    rin "\"Oh yeah? Trips take time and money, you know.\"" id a08_comn_09_d75bb438

    show rin 1 sm school_scarf g:
        xoffset 0 yoffset 0
    with None
    show fumi 2 sm school_scarf i with dict_dissolve_25

    voice "2FU_0477"
    fumi "\"Let's save up for summer♪\"" id a08_comn_09_92fd6b5b

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0566"
    rin "\"O-Okay...\"" id a08_comn_09_c99c6674

    show fumi 2 sm school_scarf e with dict_dissolve_25

    voice "2FU_0478"
    fumi "\"We'll decide on a rule and put in 100 yen every time we break it.\"" id a08_comn_09_c13ce4c9

    hide rin with Dissolve(0.25)

    show hina 2 sm school_scarf f at pos_rs with dict_dissolve_25

    if route2 == 1:
        voice "2HI_0546"
        hina "\"You mean like your 'no eating after 9' rule?\"" id a08_comn_09_b85ac83f
    else:
        voice "2HI_0547"
        hina "\"You mean like your 'no eating after 9' rule?\"" id a08_comn_09_74c4365e

    show fumi:
        "fumi 2 sm school_scarf c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0479"
    fumi "\"Yes, like that. You two should do it, too.\"" id a08_comn_09_cec97ff5

    show fumi 2 sm school_scarf c:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side school_scarf k"

    voice "2RI_0567"
    rin "\"Sure. I won't eat after 9 either.\"" id a08_comn_09_fd867819

    show hina 1 sm school_scarf p with dict_dissolve_25

    voice "2HI_0548"
    hina "\"Same here.\"" id a08_comn_09_e30e55f3

    show fumi 2 sm school_scarf f with dict_dissolve_25

    voice "2FU_0480"
    fumi "\"No! Neither of you eat at night anyway! I'd be the only one paying!\"" id a08_comn_09_d9850783

    "So she's assuming she'll be eating, then."

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0481"
    fumi "\"You two have to pick something that will take effort or self-control.\"" id a08_comn_09_a97fa0b3

    show hina 1 sm school_scarf k with dict_dissolve_25

    $ side_image = "rin 1 side school_scarf b"

    "Hina and Rin exchanged a look."

    show hina 1 sm school_scarf b with dict_dissolve_25

    voice "2HI_0549"
    hina "\"Then you should pay 100 yen every time you forget something, Rin.\"" id a08_comn_09_96f6f408

    $ side_image = "rin 1 side school_scarf g"

    voice "2RI_0568"
    rin "\"What~? Where do you want to go, Hawaii?\"" id a08_comn_09_745a5ee3

    show hina:
        "hina 1 sm school_scarf g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0550"
    hina "\"You're not supposed to plan to pay! Try being more careful!\"" id a08_comn_09_92a45e85

    show hina 1 sm school_scarf g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf a with dict_dissolve_25

    if route2 == 1:
        voice "2FU_0482"
        fumi "\"What will you do, Hina?\"" id a08_comn_09_d3cd6658
    else:
        voice "2FU_0483"
        fumi "\"What will you do, Natsume?\"" id a08_comn_09_48a7b0de

    show hina 2 sm school_scarf e with dict_dissolve_25

    voice "2HI_0551"
    hina "\"Hmm. I can't think of anything...\"" id a08_comn_09_0171e46e

    $ side_image = "rin 1 side school_scarf k"

    voice "2RI_0569"
    rin "\"You can pay 100 yen every time you sing.\"" id a08_comn_09_0c30f555

    show hina 1 sm school_scarf g with Dissolve(0.25)
    show hina:
        ShakeJump
        ShakeJump

    voice "2HI_0552"
    hina "\"Don't limit my right to express myself!\"" id a08_comn_09_2e256c5a

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 0:
        jump a08_comn_10
    else:
        jump a08_comn_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
