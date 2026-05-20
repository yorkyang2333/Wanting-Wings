label a06_cou1_01:

    $ route2 = 1
    $ rin_pyjama = "pyjama_b"

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg01cg with Dissolve(0.5)
    pause 1.5

    play music bgm03

    $ side_image = "rin 2 side pyjama c"

    voice "2RI_0011"
    rin "\"Say... girls?\""

    show bg_obi
    with bg_effect_30_1200

    show fumi 2 lg pyjama i at pos_l
    show hina 2 lg pyjama a at pos_r
    with Dissolve(0.25)

    show hina:
        "hina 2 lg pyjama a flat"
        3.5
        "hina 2 lg pyjama f" with Dissolve(0.25)

    voice "2HI_0007"
    hina "\"Hmm, would they be cuter this way? Huh? What?\""

    show hina 2 lg pyjama f with None

    $ side_image = "rin 2 side pyjama c"

    voice "2RI_0012"
    rin "\"Maybe this is a stupid question, but... do you know what you do with shoes?\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "2HI_0008"
    hina "\"Huh? What do you mean?\""

    $ side_image = "rin 2 side pyjama c"

    voice "2RI_0013"
    rin "\"Well, I mean what I said.\""

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "2HI_0009"
    hina "\"You wear them, duh.\""

    $ side_image = "rin 1 side pyjama k"

    voice "2RI_0014"
    rin "\"Good, good. So what is it the two of you are doing right now?\""

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "2HI_0010"
    hina "\"Displaying our shoes.\""

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0015"
    rin "\"Wear them!\""

    show fumi 1 lg pyjama d with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "2FU_0012"
    fumi "\"Haha... It sort of feels like a waste.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama d with dict_dissolve_25

    voice "2HI_0011"
    hina "\"I mean, if we wear them now, they'll get all dirty from the snow.\""

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0016"
    rin "\"That's how shoes work.\""

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "2HI_0012"
    hina "\"But... it's my first Christmas present from Fumi!\""

    "Fumi held her own shoes to her chest and nodded in agreement."

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_0017"
    rin "\"I'm wearing mine.\""

    "Rin's padded kimono had been a gift from Hina and Fumi."

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0013"
    fumi "\"I'm glad you like it.\""

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0018"
    rin "\"Yes! Thank you so much!\""

    $ side_image = "rin 2 side pyjama c"

    voice "2RI_0019"
    rin "\"Haah... Why don't you just wear them inside?\""

    show hina 1 lg pyjama n with dict_dissolve_25

    voice "2HI_0013"
    hina "\"I don't want the soles to wear out...\""

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0020"
    rin "\"Walk on your hands, then!\""

    camera
    with None

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "2HI_0014"
    hina "\"I'll wear them in spring... probably.\""

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0014"
    fumi "\"Let's display them until then.\""

    $ side_image = "rin 2 side pyjama c"

    voice "2RI_0021"
    rin "\"Guh. Do what you like.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
