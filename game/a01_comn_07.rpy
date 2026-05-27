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
    hina "\"Gyaaaaa!\"" id a01_comn_07_25e52d3c

    show hina 1 sm school l at pos_r2:
        xoffset 0 yoffset 0
    with None

    "Pictures fluttered to the table alongside that scream."

    show fumi:
        ShakeJump

    voice "FUM_0101"
    fumi "\"Wah, that scared me.\"" id a01_comn_07_11039fc8

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0146"
    hina "\"There's something there!!\"" id a01_comn_07_1074c9f2

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None

    voice "RIN_0143"
    rin "\"Yeah, I'd hope so.\"" id a01_comn_07_b114a32e

    voice "HIN_0147"
    hina "\"No! I mean there's something I don't remember taking a picture of!\"" id a01_comn_07_2f01e340

    voice "HIN_0148"
    hina "\"This is all because of that stuff you said last night, Rin!\"" id a01_comn_07_052b5fc0

    "...The laws of cause and effect are all out of whack here."

    voice "FUM_0102"
    fumi "\"Umm, which picture is it?\"" id a01_comn_07_f771f84b

    voice "HIN_0149"
    hina "\"The one I took in front of the chapel...\"" id a01_comn_07_45a6ca91

    "Rin and Fumi peered down at the picture in question."

    "There definitely seemed to be a long, thin shadow in the picture, but it was too blurry to properly make out."

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0144"
    rin "\"It's not your finger?\"" id a01_comn_07_de6e7d62

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0150"
    hina "\"I wouldn't make a basic mistake like that.\"" id a01_comn_07_c5dd687d

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0145"
    rin "\"Then maybe there was a mistake developing it.\"" id a01_comn_07_2d295bd4

    show hina 1 sm school i with dict_dissolve_25

    voice "HIN_0151"
    hina "\"My dad's a pro.\"" id a01_comn_07_63975df3

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0146"
    rin "\"Hmm~ Well, then it can just be a ghost picture, can't it?\"" id a01_comn_07_1e166ea3

    show hina:
        "hina 1 sm school g" with Dissolve(0.25)
        function LayerShake(20,20,0.4)
    $ persistent.layer_shaken = False

    voice "HIN_0152"
    hina "\"Gyaaa!!\"" id a01_comn_07_13553ba2

    show hina 1 sm school g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0103"
    fumi "\"Hmm.\"" id a01_comn_07_313d6efe

    "Fumi was still looking carefully at the picture."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0104"
    fumi "\"...Do you suppose this could be a feather?\"" id a01_comn_07_2a79f910

    show hina 1 sm school k
    show rin 1 sm school e
    with dict_dissolve_25

    $ voice2("hina","HIN_0153","rin","RIN_0147")
    hina_rin "\"A feather?\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0105"
    fumi "\"Yes.\"" id a01_comn_07_d05e7f9c

    show hina 1 sm school d with dict_dissolve_25

    voice "HIN_0154"
    hina "\"But there weren't any birds around when I took this picture.\"" id a01_comn_07_c991f2db

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0106"
    fumi "\"Heheheh, it doesn't belong to a bird.\"" id a01_comn_07_f5a27a04

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0148"
    rin "\"Ah...\"" id a01_comn_07_df32aa95

    voice "FUM_0107"
    fumi "\"It's an angel!\"" id a01_comn_07_fa5ae4e3

    voice "HIN_0155"
    hina "\"U-Umm...\"" id a01_comn_07_03a03482

    "Hina glanced at Rin, who gave a small shrug."

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0108"
    if persistent.dpatch:
        fumi "\"There's a rumor that there's an angel at this school.\"" id a01_comn_07_c371c74a
    else:
        fumi "\"There's a rumor that there's an angel at this academy.\"" id a01_comn_07_7216a5bf

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0156"
    hina "\"Yeah, I know.\"" id a01_comn_07_e8117cc0

    voice "RIN_0149"
    rin "\"I heard, from you... several times.\"" id a01_comn_07_52b30aab

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0109"
    fumi "\"Most of the sightings have been at the chapel, and that's where you took this picture!\"" id a01_comn_07_df1d4a24

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0150"
    rin "\"She's real confident now.\"" id a01_comn_07_4d48bdd0

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0110"
    fumi "\"The angel was nearby when you took this picture, Natsume!\"" id a01_comn_07_446d18ef

    voice "HIN_0157"
    hina "\"Y-You think so?\"" id a01_comn_07_39fb6091

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0111"
    fumi "\"So you don't need to be scared. It's not a ghost. It's an angel feather.\"" id a01_comn_07_47021757

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0158"
    hina "\"You really believe the angel stuff, huh, Asou?\"" id a01_comn_07_87e54e6d

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0112"
    fumi "\"Yep. I've seen one before. It was when I was little, though.\"" id a01_comn_07_9cf00764

    voice "HIN_0159"
    hina "\"You said she found your shoe for you in the snow, right?\"" id a01_comn_07_a6f11c3d

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0113"
    fumi "\"Yep. I've believed in them ever since then.\"" id a01_comn_07_5d641ce4

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0160"
    hina "\"Huh...\"" id a01_comn_07_3d3fef77

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0151"
    rin "\"Umm~ I'm getting kinda hungry.\"" id a01_comn_07_7771129e

    "Rin raised a hand hesitantly."

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0114"
    fumi "\"Oh, I'm sorry! It's getting pretty late, isn't it?\"" id a01_comn_07_38845cb1

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0152"
    rin "\"No, I'm sorry for butting in.\"" id a01_comn_07_6ce3aa09

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0115"
    fumi "\"It's alright. I know I can get into it when I start talking about angels.\"" id a01_comn_07_75abd025

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_0153"
    rin "\"Ahaha, maybe so.\"" id a01_comn_07_62fcddb2

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0116"
    fumi "\"I'll get dinner ready right away!\"" id a01_comn_07_c38b8144

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
    rin "\"She's practically perfect aside from that...\"" id a01_comn_07_0d4f47c7

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_0161"
    hina "\"Well, it's not like she insists on it or anything.\"" id a01_comn_07_922c93a6

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_0162"
    hina "\"And she really seems to enjoy talking about angels whenever they come up.\"" id a01_comn_07_4df52e27

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
