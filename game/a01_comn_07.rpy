label a01_comn_07:

    scene bg01ba with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 1 sm school l at pos_r2
    show fumi 1 sm school e
    show rin 1 sm school a at pos_l2
    with Dissolve(0.25)

    show hina:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "HIN_0145"
    hina "\"Gyaaaaa!\""

    show hina 1 sm school l at pos_r2:
        xoffset 0 yoffset 0
    with None

    "Pictures fluttered to the table alongside that scream."

    show fumi:
        ShakeJump

    voice "FUM_0101"
    fumi "\"Wah, that scared me.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0146"
    hina "\"There's something there!!\""

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None

    voice "RIN_0143"
    rin "\"Yeah, I'd hope so.\""

    voice "HIN_0147"
    hina "\"No! I mean there's something I don't remember taking a picture of!\""

    voice "HIN_0148"
    hina "\"This is all because of that stuff you said last night, Rin!\""

    "...The laws of cause and effect are all out of whack here."

    voice "FUM_0102"
    fumi "\"Umm, which picture is it?\""

    voice "HIN_0149"
    hina "\"The one I took in front of the chapel...\""

    "Rin and Fumi peered down at the picture in question."

    "There definitely seemed to be a long, thin shadow in the picture, but it was too blurry to properly make out."

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0144"
    rin "\"It's not your finger?\""

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0150"
    hina "\"I wouldn't make a basic mistake like that.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0145"
    rin "\"Then maybe there was a mistake developing it.\""

    show hina 1 sm school i with dict_dissolve_25

    voice "HIN_0151"
    hina "\"My dad's a pro.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0146"
    rin "\"Hmm~ Well, then it can just be a ghost picture, can't it?\""

    show hina:
        "hina 1 sm school g" with Dissolve(0.25)
        function LayerShake(20,20,0.4)
    $ persistent.layer_shaken = False

    voice "HIN_0152"
    hina "\"Gyaaa!!\""

    show hina 1 sm school g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0103"
    fumi "\"Hmm.\""

    "Fumi was still looking carefully at the picture."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0104"
    fumi "\"...Do you suppose this could be a feather?\""

    show hina 1 sm school k
    show rin 1 sm school e
    with dict_dissolve_25

    $ voice2("hina","HIN_0153","rin","RIN_0147")
    hina_rin "\"A feather?\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0105"
    fumi "\"Yes.\""

    show hina 1 sm school d with dict_dissolve_25

    voice "HIN_0154"
    hina "\"But there weren't any birds around when I took this picture.\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0106"
    fumi "\"Heheheh, it doesn't belong to a bird.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0148"
    rin "\"Ah...\""

    voice "FUM_0107"
    fumi "\"It's an angel!\""

    voice "HIN_0155"
    hina "\"U-Umm...\""

    "Hina glanced at Rin, who gave a small shrug."

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0108"
    if persistent.dpatch:
        fumi "\"There's a rumor that there's an angel at this school.\"" id a01_comn_07_c371c74a
    else:
        fumi "\"There's a rumor that there's an angel at this academy.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0156"
    hina "\"Yeah, I know.\""

    voice "RIN_0149"
    rin "\"I heard, from you... several times.\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0109"
    fumi "\"Most of the sightings have been at the chapel, and that's where you took this picture!\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0150"
    rin "\"She's real confident now.\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0110"
    fumi "\"The angel was nearby when you took this picture, Natsume!\""

    voice "HIN_0157"
    hina "\"Y-You think so?\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0111"
    fumi "\"So you don't need to be scared. It's not a ghost. It's an angel feather.\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0158"
    hina "\"You really believe the angel stuff, huh, Asou?\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0112"
    fumi "\"Yep. I've seen one before. It was when I was little, though.\""

    voice "HIN_0159"
    hina "\"You said she found your shoe for you in the snow, right?\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0113"
    fumi "\"Yep. I've believed in them ever since then.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0160"
    hina "\"Huh...\""

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0151"
    rin "\"Umm~ I'm getting kinda hungry.\""

    "Rin raised a hand hesitantly."

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0114"
    fumi "\"Oh, I'm sorry! It's getting pretty late, isn't it?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0152"
    rin "\"No, I'm sorry for butting in.\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0115"
    fumi "\"It's alright. I know I can get into it when I start talking about angels.\""

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_0153"
    rin "\"Ahaha, maybe so.\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0116"
    fumi "\"I'll get dinner ready right away!\""

    show fumi:
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612

    pause 1.0
    hide fumi with None

    "Fumi hurried into the kitchen."

    hide rin
    hide hina
    with Dissolve(0.05)
    pause 0.2


    show hina 1 lg school k at pos_r
    show rin 1 lg school a at pos_l
    with Dissolve(0.25)

    voice "RIN_0154"
    rin "\"She's practically perfect aside from that...\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_0161"
    hina "\"Well, it's not like she insists on it or anything.\""

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_0162"
    hina "\"And she really seems to enjoy talking about angels whenever they come up.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
