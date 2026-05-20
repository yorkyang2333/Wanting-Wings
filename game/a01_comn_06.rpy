label a01_comn_06:

    scene bg02dd with Dissolve(0.5)
    pause 1.5

    play music bgm02

    show hina 3 sm dark pyjama d with Dissolve(0.25)

    window auto

    voice "HIN_0120"
    hina "\"Oh yeah, Rin.\""

    show rin 3 sm nightlight pyjama glasses_b with Dissolve(0.25)

    voice "RIN_0117"
    rin "\"Hm? Yeah~?\""

    show hina 3 sm dark pyjama b with dict_dissolve_25

    voice "HIN_0121"
    hina "\"Did you put your handout in your bag?\""

    show rin 3 sm nightlight pyjama glasses_e with dict_dissolve_25

    voice "RIN_0118"
    rin "\"Not yet~\""

    show fumi 3 sm nightlight pyjama e with Dissolve(0.25)

    voice "FUM_0085"
    fumi "\"You're gonna forget it again. You should put it in now.\""

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "RIN_0119"
    rin "\"What~? Can't I just wait until morning?\""

    show hina 3 sm dark pyjama j
    show fumi 3 sm nightlight pyjama d
    with dict_dissolve_25

    $ voice2("hina","HIN_0122","fumi","FUM_0086")
    hina_fumi "\"You can't.\"\n\"You shouldn't.\"" (what_rest_indent=0)

    show rin 3 sm nightlight pyjama glasses_g with dict_dissolve_25

    voice "RIN_0120"
    rin "\"Ugh, and I just got warm in here.\""

    "Rin slid out from under her covers, trying not to let any warmth escape."

    scene black with bg_effect_02
    pause 0.25
    scene bg01da with bg_effect_02
    pause 0.5

    show rin:
        "rin 1 lg pyjama glasses a flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    "Her handout was sitting on her desk."

    show rin 1 lg pyjama glasses a:
        alpha 1.0 xcenter 512
    with None

    if persistent.dpatch:
        "It was something about returning home for the winter break. \"Stay at school\" was circled, with a signature next to it." id a01_comn_06_5b15f288
    else:
        "It was something about returning home for the winter break. \"Stay on campus\" was circled, with a signature next to it."

    play sound se013a

    "Rin folded the paper and stuck it in her bag."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0121"
    rin "\"There, it's done!\""

    $ side_image = "hina 1 side pyjama j"

    voice "HIN_0123"
    hina "\"Very well. You have permission to return to bed.\""

    scene black with bg_effect_01
    pause 0.25
    scene bg02dd with bg_effect_01
    pause 0.5


    show rin:
        "rin 1 lg pyjama glasses i flat"
        alpha 0.0 xcenter 412
        easein 0.5 alpha 1.0 xcenter 512

    pause 0.5

    show rin 1 lg pyjama glasses i:
        alpha 1.0 xcenter 512
        ShakeUji

    voice "RIN_0122"
    rin "\"Unh, it's cold~\""

    show rin 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None

    "Rin returned from the living room, shoulders hunched."

    show fumi 3 sm nightlight pyjama c with Dissolve(0.25)

    voice "FUM_0087"
    fumi "\"Heh, hurry and get back under the covers.\""

    hide rin
    with Dissolve(0.25)

    play sound se116a

    "Rin nodded and crawled into Fumi's bed like it was the most natural thing in the world."

    show fumi 3 lg nightlight pyjama c
    show rin 3 lg nightlight pyjama_bed_b glasses_i:
        xcenter 534 ycenter 474
    with Dissolve(0.25)

    voice "RIN_0124"
    rin "\"Wah~ It's so warm and smells so good~\""

    show fumi 3 lg nightlight pyjama e with dict_dissolve_25

    voice "FUM_0088"
    fumi "\"U-Umm, this isn't your bed, is it, Ogata?\""

    show rin 3 lg nightlight pyjama_bed_b glasses_c with dict_dissolve_25

    voice "RIN_0125"
    rin "\"Don't worry about it, don't worry about it.\""

    show fumi 3 lg nightlight pyjama g with dict_dissolve_25

    voice "FUM_0089"
    fumi "\"H-Hey! Where are you touching... nnh!\""

    show rin 3 lg nightlight pyjama_bed_b glasses_i with dict_dissolve_25

    voice "RIN_0126"
    rin "\"Your boobs are so soft! Mhm, I figured you'd sleep braless!\""

    voice "FUM_0090"
    fumi "\"A-Aaaaah?!\""

    play sound se118b

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    pause 0.25

    play sound2 se025a

    scene bg02ca with Dissolve(0.1)
    pause 0.7

    show hina 1 lg pyjama f
    with Dissolve(0.25)

    show hina:
        function LayerShake(30,30,0.2)
    $ persistent.layer_shaken = False

    voice "HIN_0124"
    hina "\"HEY!!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina jumped out of bed at Fumi's scream."

    show fumi 3 lg nightlight pyjama g:
        ycenter 258
    show rin 3 lg nightlight pyjama_bed_b glasses_b:
        xcenter 210 ycenter 474
    with Dissolve(0.25)

    voice "RIN_0127"
    rin "\"Mommy and Daddy have stuff to do, so go to bed, kiddo.\""

    show hina 1 lg pyjama e with dict_dissolve_25

    voice "HIN_0125"
    hina "\"That's not funny!\""

    show rin 3 lg nightlight pyjama_bed_b glasses_c with dict_dissolve_25

    voice "RIN_0128"
    rin "\"Well, was it a joke?\""

    show fumi 3 lg nightlight pyjama g with dict_dissolve_25

    voice "FUM_0091"
    fumi "\"Hawawawa?!\""

    show hina:
        "hina 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0126"
    hina "\"Argh! Get out of Asou's bed!\""

    show hina 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show rin 3 lg nightlight pyjama_bed_b glasses_f with dict_dissolve_25

    voice "RIN_0129"
    rin "\"Ow! Wait, stop! People's arms aren't supposed to bend that way!\""

    hide rin
    hide fumi
    with Dissolve(0.25)

    show hina:
        "hina 1 lg pyjama d" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 772
    show rin:
        "rin 1 lg pyjama g glasses flat"
        alpha 0.0 xcenter 152
        easein 1.0 alpha 1.0 xcenter 252

    voice "HIN_0127"
    hina "\"Shut up! Are you okay, Asou? Did she violate you?\""

    show hina 1 lg pyjama d:
        xcenter 772
    show rin 1 lg pyjama g glasses:
        alpha 1.0 xcenter 252
    with None

    show rin 1 lg pyjama i glasses with dict_dissolve_25

    voice "RIN_0130"
    rin "\"That seems a little harsh.\""

    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0128"
    hina "\"It's not! You glasses molester!\""

    show rin 1 lg pyjama g glasses with dict_dissolve_25

    voice "RIN_0131"
    rin "\"Glasses molester...\""

    show hina:
        "hina 1 lg pyjama j" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0129"
    hina "\"Get back to your own lair!\""

    show hina 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    play sound se103b

    show rin:
        "rin 1 lg pyjama j glasses" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_0132"
    rin "\"Ow! Stop it with the low blows!\""

    show rin 1 lg pyjama j glasses:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0130"
    hina "\"That was a middle kick!\""

    scene black with bg_effect_05
    pause 1.5

    scene bg02db with bg_effect_05
    pause 1.0

    show fumi 3 sm dark pyjama e with dict_dissolve_25

    voice "FUM_0092"
    fumi "\"Come to think of it, Natsume?\""

    show hina 3 sm dark pyjama b with dict_dissolve_25

    voice "HIN_0131"
    hina "\"Yeah?\""

    show fumi 3 sm dark pyjama b with dict_dissolve_25

    voice "FUM_0093"
    if persistent.dpatch:
        fumi "\"You took a lot of pictures during the school festival, right?\"" id a01_comn_06_316ea2c7
    else:
        fumi "\"You took a lot of pictures during the class festival, right?\""

    show hina 3 sm dark pyjama c with dict_dissolve_25

    voice "HIN_0132"
    if persistent.dpatch:
        hina "\"The ones the school asked me to take? Yeah. I took some for myself, too.\"" id a01_comn_06_deace286
    else:
        hina "\"The ones the academy asked me to take? Yeah. I took some for myself, too.\""

    show fumi 3 sm dark pyjama e with dict_dissolve_25

    voice "FUM_0094"
    fumi "\"When can we see those?\""

    show hina 3 sm dark pyjama d with dict_dissolve_25

    voice "HIN_0133"
    if persistent.dpatch:
        hina "\"Mm, I dunno about the school ones, since I gave the camera back to the teacher.\"" id a01_comn_06_c4795964
    else:
        hina "\"Mm, I dunno about the class ones, since I gave the camera back to the teacher.\""

    show hina 3 sm dark pyjama c with dict_dissolve_25

    voice "HIN_0134"
    hina "\"But the personal ones, I sent home last weekend, so I think I'll get them back around tomorrow?\""

    show fumi 3 sm dark pyjama h with dict_dissolve_25

    voice "FUM_0095"
    fumi "\"Ahh, I'm looking forward to them.\""

    show hina 3 sm dark pyjama i with dict_dissolve_25

    voice "HIN_0135"
    hina "\"Me too. I hope they come out good.\""

    show rin 3 sm nightlight pyjama glasses_c with dict_dissolve_25

    voice "RIN_0133"
    rin "\"What'll you do if you got a picture of something weird?\""

    show fumi 3 sm dark pyjama e with dict_dissolve_25

    voice "FUM_0096"
    fumi "\"Something weird?\""

    voice "RIN_0134"
    rin "\"Like in one of the pictures, there's a ghost—\""

    show hina 3 sm dark pyjama g with dict_dissolve_25

    voice "HIN_0136"
    hina "\"Hey, you can't talk about that sort of thing at this time of night!\""

    show fumi 3 sm dark pyjama f with dict_dissolve_25

    voice "FUM_0097"
    fumi "\"It's fine. It's not like you were taking pictures of a graveyard or a temple.\""

    voice "RIN_0135"
    rin "\"School ghost stories.\""

    show hina 3 sm dark pyjama k with dict_dissolve_25

    voice "HIN_0137"
    hina "\"Eep!\""

    show fumi 3 sm dark pyjama e with dict_dissolve_25

    voice "FUM_0098"
    fumi "\"Ogata~\""

    voice "RIN_0136"
    rin "\"Want me to sleep with you, sport?\""

    show hina 3 sm dark pyjama j with dict_dissolve_25

    voice "HIN_0138"
    hina "\"No! You'll do something dirty!\""

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "RIN_0137"
    rin "\"Haahh. Nothing bitter. Nothing scary. And nothing dirty. You really are a little kid, Hina.\""

    hide hina
    with Dissolve(0.05)

    pause 0.2

    play sound se104b

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0139"
    hina "\"Shut it!\""

    camera
    with None

    "Hina kicked at the bed above her, the springs doing the work her short legs couldn't."

    show rin 3 lg nightlight pyjama glasses_h with dict_dissolve_25

    voice "RIN_0138"
    rin "\"Oof. Right in the gut...\""

    hide rin
    with Dissolve(0.05)

    $ side_image = "hina 1 side pyjama l"

    play sound se118c

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "HIN_0140"
    hina "\"Heheh—gafh?!\""

    camera
    with None

    "A pillow dropped from above onto Hina's face."

    $ side_image = "rin 1 side pyjama j glasses"

    voice "RIN_0139"
    rin "\"What are you gonna do if you open up a hole in the bottom of this thing?\""

    "Rin hung down over the side of her bed."

    $ side_image = "hina 2 side pyjama i"

    voice "HIN_0141"
    hina "\"Ptu, ptu... You started it!\""

    "Hina tried to hit her with the pillow, but Rin ducked back onto her bunk."

    $ side_image = "rin 2 side pyjama e glasses"

    voice "RIN_0140"
    rin "\"If you're gonna be like that, you're getting... 200 candelas!\""

    "Rin grabbed her reading light and shone it in Hina's face."

    $ side_image = "hina 2 side pyjama j"

    voice "HIN_0142"
    hina "\"Gwah, bright!\""

    "Hina covered her eyes and tried to escape the beam, but it followed her like a searchlight."

    show fumi 3 sm dark pyjama e with dict_dissolve_25

    voice "FUM_0099"
    fumi "\"Umm, it's getting late, you two. If you're too noisy, our neighbors\nwill—\""

    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0143"
    hina "\"Youuu!\""

    $ side_image = "rin 2 side pyjama f glasses"

    voice "RIN_0141"
    rin "\"Oho—\""

    "The pillow Hina was swinging slipped from her hand and flew past Rin, hitting—"

    play sound se118c

    show fumi 3 sm dark pyjama g with dict_dissolve_25

    voice "FUM_0100"
    fumi "\"Ouch!\""

    scene black with Dissolve(0.25)
    pause 0.25

    scene bg02db with Dissolve(0.25)
    pause 0.75

    show hina 1 lg pyjama d at pos_r
    show rin 1 lg pyjama g glasses at pos_l
    with Dissolve(0.25)

    $ voice2("hina","HIN_0144","rin","RIN_0142")
    hina_rin "\"...We're sorry.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
