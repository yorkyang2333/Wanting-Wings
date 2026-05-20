label a05_ang_06:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_06:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg05ba_grayscale with Dissolve(0.375)
    pause 1.125

    show hina 1 sm school_scarf f grayscale at pos_l
    show rin 1 sm school_scarf a grayscale
    show fumi 1 sm school_scarf a grayscale at pos_r
    with Dissolve(0.25)

    voice "RIN_0182"
    if persistent.dpatch:
        rin "\"Every school has stupid rumors like that. There's no such thing as angels.\"" id a05_ang_06_b2caa84c
    else:
        rin "\"Every campus has stupid rumors like that. There's no such thing as angels.\""

    voice "RIN_0186"
    rin "\"Okay, let's get out of here. Come on, Asou.\""

    $ side_image = "side/sachiko_1_side_outfit_j_grayscale.webp"

    voice "SYO_0047"
    sachiko "\"T-Twelve thousand!\""

    show hina 1 sm school_scarf j grayscale with dict_dissolve_25

    voice "HIN_0205"
    hina "\"Shoo, shoo! Back to hell with you, demon!\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    "........."

    "The lobby regained its quiet after the three left."

    play music bgm05

    show sachiko 1 grayscale lg outfit b with dict_dissolve_25

    voice "SYO_0202"

    sachiko "\"No such thing, she says.\""

    "Sachiko turned around pointedly. She was as shrewd as always."

    "I would claim that I do exist."

    "However, if she's unable to see me or sense my presence, to Rin, I may as well not."

    show sachiko 1 grayscale lg outfit a with dict_dissolve_25

    voice "SYO_0203"

    sachiko "\"So, was that you?\""

    "—It was not."

    "I shook my head without thinking. Though she couldn't see me."

    show sachiko 1 grayscale lg outfit b with dict_dissolve_25

    voice "SYO_0204"

    if persistent.dpatch:
        sachiko "\"No, it was at the school festival, which was before you came. Well, they do tend to pass through here pretty often.\"" id a05_ang_06_f067e3a4
    else:
        sachiko "\"No, it was at the class festival, which was before you came. Well, they do tend to pass through here pretty often.\""

    "Now that she mentioned it, I realized she was right. In just these few weeks, I'd seen several of my kind."

    if persistent.dpatch:
        "This school was founded because of an angel, too. Maybe there's something near here that draws us to it." id a05_ang_06_d9e33fe1
    else:
        "This academy was founded because of an angel, too. Maybe there's something near here that draws us to it."

    if persistent.dpatch:
        "There might just be something to these school rumors." id a05_ang_06_6779fab8
    else:
        "There might just be something to these campus rumors."

    show sachiko 1 grayscale lg outfit a with dict_dissolve_25

    voice "SYO_0205"

    sachiko "\"It's rare they'd show up on film, though.\""

    "Sachiko mimed taking a picture."

    "She might be right."

    "There are sometimes people who can sense us, like Sachiko."

    "But it's incredibly rare to catch sight of one so clearly."

    "And for them to appear on film, too..."

    voice "2SA_0015"
    sachiko "\"Oh, it's not your fault. That girl's camera is special.\""

    "Special? What does that mean?"

    show sachiko 1 grayscale lg outfit i with dict_dissolve_25

    voice "2SA_0016"
    sachiko "\"It's a Device.\""

    "—I'm surprised."

    "I've heard of them before, but it's my first time seeing one for real."

    "Very rarely, there exist certain items called \"Devices\" that bridge the gap between humans and angels."

    "Not even we know why they exist, how they work, or who makes them."

    show sachiko 1 grayscale lg outfit g with dict_dissolve_25

    voice "2SA_0017"
    sachiko "\"Are you surprised? I bet you thought all Devices are displayed in cathedrals or something.\""

    "She's right. I never thought I'd see one here. And being used so regularly..."

    "Most known Devices are used in name only by various religions to whatever purpose they deem convenient."

    voice "2SA_0018"
    sachiko "\"Devices don't have to be holy relics or anything.\""

    "I suppose not. It's not as if we angels are \"holy\" beings, either."

    "If we're not able to intervene in anything, we're agents of no force, holy or otherwise."

    show sachiko 1 grayscale lg outfit a with dict_dissolve_25

    voice "2SA_0019"
    sachiko "\"It's not just Hina's camera. There's plenty of Devices in this world.\""

    "It sounds as if she knows of at least one other."

    "But how does she know so much about angels and Devices?"

    "Sachiko had a mysterious smile on her face."

    "........."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a05_ang_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
