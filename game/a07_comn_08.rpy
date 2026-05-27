label a07_comn_08:

    scene bg02di with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "By the time Miyako left Sachiko's room, these three were already in bed."

    show hina 3 sm light pyjama_headphones_pjm i with dict_dissolve_25

    voice "2HI_0107"
    hina "\"♪Nyaga nyanyaaa ganyaaa, nyaga nyagaaa, nyaaa, nyaaa. nyaaa!\"" id a07_comn_08_9c245bff

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "2RI_0100"
    rin "\"...Shut up.\"" id a07_comn_08_6e070b53

    show fumi 3 sm nightlight pyjama b with dict_dissolve_25

    voice "2FU_0082"
    fumi "\"...Ah, ah...\"" id a07_comn_08_3fe2e795

    show hina 3 sm light pyjama_headphones_pjm j with dict_dissolve_25

    voice "2HI_0108"
    hina "\"♪Nyaga nyaga! Nyagaaa!!\"" id a07_comn_08_b47e3206

    play sound se_2s_h014

    show fumi 3 sm nightlight pyjama e with dict_dissolve_25

    voice "2FU_0083"
    fumi "\"Ah...!\"" id a07_comn_08_1be91282

    hide rin
    hide fumi
    with Dissolve(0.25)

    window hide

    show rin 1 lg pyjama glasses i
    show white:
        alpha 1.0 additive 1.0
        linear 0.3 alpha 0.0
    pause 0.3
    window auto

    show rin:
        ShakeJump

    voice "2RI_0101"
    rin "\"200 candelas!!\"" id a07_comn_08_069bc5c1

    hide white with None
    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 3 sm light pyjama_headphones_pjm k" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2HI_0109"
    hina "\"Gwah, that's bright!\"" id a07_comn_08_4443be1a

    show hina 3 sm light pyjama_headphones_pjm k:
        xoffset 0 yoffset 0
    with None

    "Rin grabbed her bedside reading light and shone it in Hina's face."

    hide hina
    with Dissolve(0.25)

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0110"
    hina "\"What was that for?!\"" id a07_comn_08_589b4dc2

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0102"
    rin "\"What do you think?! You're! Being! Loud!\"" id a07_comn_08_23bcff60

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0111"
    hina "\"Oh, you can hear my music?\"" id a07_comn_08_496a1ef0

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0103"
    rin "\"This is way beyond that!\"" id a07_comn_08_e4ed94cc

    $ side_image = "hina 1 side pyjama_pjm c"

    voice "2HI_0112"
    hina "\"I love this song, so I just can't help humming it~ I have no idea what they're saying, though.\"" id a07_comn_08_1915e91a

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0104"
    rin "\"Your singing is an environmental issue.\"" id a07_comn_08_15e15ce2

    $ side_image = "hina 1 side pyjama_pjm d"

    voice "2HI_0113"
    hina "\"That's mean!\"" id a07_comn_08_d2c4e00e

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0105"
    rin "\"It's honest!\"" id a07_comn_08_dadd3a59

    hide rin
    with Dissolve(0.25)

    pause 0.3

    play sound se521

    pause 1.0

    show miyako 2 sm pyjama_hood a with dict_dissolve_25

    voice "2MI_0095"
    miyako "\"I'm back... Oh, you're all still up?\"" id a07_comn_08_c07a61c7

    "Miyako had opened the door quietly in case they were sleeping."

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0106"
    rin "\"Can't sleep while Hina's singing.\"" id a07_comn_08_016a8c61

    show miyako 2 sm pyjama_hood c with dict_dissolve_25

    voice "2MI_0096"
    miyako "\"That's mean.\"" id a07_comn_08_0e06a69c

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0107"
    rin "\"It's not mean!\"" id a07_comn_08_d83942ac

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0084"
    fumi "\"Did she fill out the printout for you?\"" id a07_comn_08_e03fe650

    show miyako 1 sm pyjama_hood_a b with dict_dissolve_25

    voice "2MI_0097"
    miyako "\"Yes.\"" id a07_comn_08_49b8aa4f

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_0114"
    hina "\"You should put it in your bag now so you don't forget it.\"" id a07_comn_08_23c1dc77

    show miyako 1 sm pyjama_hood_a c with dict_dissolve_25

    voice "2MI_0098"
    miyako "\"Yes, I'll do that.\"" id a07_comn_08_aed873ad

    hide miyako with dict_dissolve_25

    "Miyako slipped through the bedroom into the living room."

    $ side_image = "hina 1 side pyjama_pjm p"

    voice "2HI_0115"
    hina "\"She's such a good girl! The complete opposite of Rin.\"" id a07_comn_08_8cb1e0f7

    show rin 1 lg pyjama glasses j with dict_dissolve_25

    voice "2RI_0108"
    rin "\"Huh? Me?!\"" id a07_comn_08_29780b49

    $ side_image = "hina 1 side pyjama_pjm d"

    voice "2HI_0116"
    hina "\"You really need to be more careful. You even forgot something at my house the other day when you slept over.\"" id a07_comn_08_2016a0c2

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0109RE"
    rin "\"Ugh, we don't need to air our dirty laundry like this, do we?\"" id a07_comn_08_e2c458d7

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_0117"
    hina "\"Why are we talking about laundry all of a sudden? Don't change the subject just because you don't want to listen to what I'm saying.\"" id a07_comn_08_04c1fcad

    "She didn't get it."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0118"
    hina "\"It wasn't dirty laundry, anyway! It was a dirty book of all things!\"" id a07_comn_08_f5b1c086

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0110"
    rin "\"With a cover over it, luckily...\"" id a07_comn_08_6c186435

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0119"
    hina "\"I had to run back there to get it! What do you think would have happened if my family had opened it before that?! Who brings dirty books to a sleepover, anyway?!\"" id a07_comn_08_c7cc2ddb

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0111"
    rin "\"I apologize for the trouble...\"" id a07_comn_08_e19360f3

    hide rin
    with Dissolve(0.25)

    show miyako 1 lg pyjama_hood_a b with dict_dissolve_25

    voice "2MI_0099"
    miyako "\"I put it in my bag. What are we talking about?\"" id a07_comn_08_157c39f4

    "Miyako returned with perfect timing again."

    $ side_image = "hina 1 side pyjama_pjm e"

    voice "2HI_0120"
    hina "\"How Rin forgets things too often!\"" id a07_comn_08_0ca312bc

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0112"
    rin "\"How did we get on that subject anyway?! I thought we were talking about how bad your singing is!\"" id a07_comn_08_d25c251f

    $ side_image = "hina 1 side pyjama_pjm n"

    voice "2HI_0121"
    hina "\"Sorry for leaving you alone here on New Year's.\"" id a07_comn_08_de8c8481

    show miyako 1 lg pyjama_hood_a c with dict_dissolve_25

    voice "2MI_0100"
    miyako "\"Oh, it's fine, I had to unpack my things. And Sachiko was here.\"" id a07_comn_08_3da6c0d4

    $ side_image = "hina 1 side pyjama_pjm n"

    voice "2HI_0122"
    hina "\"Yeah, that's what I was most worried about...\"" id a07_comn_08_8bc64ac9

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0113"
    rin "\"Now the subject's changed again!\"" id a07_comn_08_271b1b47

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0085"
    fumi "\"Alright, alright, it's getting late, so let's get to sleep.\"" id a07_comn_08_10d6c36e

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0114"
    rin "\"Mean!\"" id a07_comn_08_450b5393

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0123"
    hina "\"Not mean!\"" id a07_comn_08_6a7bae73

    show miyako 1 lg pyjama_hood_a i with dict_dissolve_25

    voice "2MI_0101"
    miyako "\"I'll wake up on time tomorrow!\"" id a07_comn_08_afb82789

    $ side_image = "rin 1 side pyjama glasses d"

    voice "2RI_0115"
    rin "\"Good! You do that!\"" id a07_comn_08_d8a17b67

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0124"
    hina "\"You do it, too!\"" id a07_comn_08_98b6d024

    $ side_image = "fumi 2 side pyjama i"

    voice "2FU_0086"
    fumi "\"Ahaha.\"" id a07_comn_08_feb3e51b

    hide miyako
    with Dissolve(0.25)

    pause 0.5

    play sound se_bati
    window hide
    show white:
        alpha 1.0 additive 1.0
        linear 0.5 alpha 0.0
    pause 0.5
    window auto

    $ side_image = "miyako 1 side pyjama_hood_a k"

    voice "2MI_0102"
    miyako "\"?!\"" id a07_comn_08_5abf1bfe

    "Right when Miyako put her hand on the bed's ladder..."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0125"
    hina "\"Whoa, sparks! Static electricity?\"" id a07_comn_08_7b862c00

    show miyako 1 sm pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0103"
    miyako "\"......\"" id a07_comn_08_8368e1c6

    "Miyako peered curiously at her hand."

    $ side_image = "rin 2 side pyjama glasses e"

    voice "2RI_0116"
    rin "\"Happens a lot with synthetic fibers.\"" id a07_comn_08_99caac4e

    $ side_image = "fumi 1 side pyjama b"

    voice "2FU_0087"
    fumi "\"At this time of year, you should touch the railing first to dissipate the electricity.\"" id a07_comn_08_75849d66

    show miyako 1 sm pyjama_hood_a a with dict_dissolve_25

    voice "2MI_0104"
    miyako "\"Right... Good night.\"" id a07_comn_08_7041f516

    hide miyako with dict_dissolve_50

    "Miyako touched the railing like Fumi had suggested and then put her hand on the ladder once more."

    pause 0.3

    play sound se_2s_j037

    scene bg02dg with Dissolve(0.125)
    pause 0.675

    show hina 3 sm dark pyjama_pjm e
    show rin 3 sm dark pyjama glasses_b
    show fumi 3 sm dark pyjama c
    with dict_dissolve_25

    $ voice3("hina","2HI_0126","rin","2RI_0117","fumi","2FU_0088")
    hina_rin_fumi "\"Night!\"\n\"Night.\"\n\"Good night.\"" (show_name="Hina & Fumi & Rin", what_rest_indent=0)

    scene black with Dissolve(0.45)
    pause 1.65

    scene bg08ca with Dissolve(0.45)
    pause 1.35

    show miyako 3 sm dark pyjama h
    with Dissolve(0.5)
    pause 0.5

    voice "2MI_0105"
    miyako "\"...Static electricity?\"" id a07_comn_08_002e6519

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
