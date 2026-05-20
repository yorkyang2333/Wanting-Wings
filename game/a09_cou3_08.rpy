label a09_cou3_08:

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "The section introducing Le Chocolat Chocolat ended with a somewhat hackneyed shot of Fumi holding chocolate out for the camera to eat."

    "And Rin making a bunch of noise and Hina hitting her."

    show fumi z4 2 lg pyjama h:
        xcenter 298
    show rin z4 1 lg pyjama glasses f:
        xcenter 726
    with dict_dissolve_25

    voice "2FU_0917"
    fumi "\"I didn't know you were there at all.\""

    "Fumi looked visibly relieved that the segment was over. There was some other good-looking patissier on screen now."

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_1162"
    hina "\"Hey. Your eyes didn't meet, then.\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1204"
    rin "\"Huh?\""

    "Apparently, her narration was unreliable."

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0918"
    fumi "\"You were there three hours early? Wasn't it cold?\""

    show rin z4 2 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1205"
    rin "\"It was your debut! I had to see it with my own eyes!\""

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0919"
    fumi "\"My debut...? It was just an introduction to our store.\""

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1206"
    rin "\"Fumi didn't yet know that this was the beginning of her lege—\""

    play sound se_2s_j015
    pause 1.5

    show fumi z4 2 lg pyjama g
    show rin z4 1 lg pyjama glasses e
    with dict_dissolve_25

    "Fumi's phone rang then."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0773"
    sachiko "\"From home?\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0920"
    fumi "\"No, it's a number I don't know... But it's not withheld, so I guess I'll answer.\""

    hide fumi
    hide rin
    with Dissolve(0.5)

    play sound se_2s_j012
    pause 1.5

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0921"
    fumi "\"Hello, Asou speaking. ...Katsuragi Production? ...Oh! Yes, thanks for today—\""

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1163"
    hina "\"Katsuragi Production?\""

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0774"
    sachiko "\"Probably the talent agency? I think they've got Par-Reggi, right?\""

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_0939"
    miyako "\"You know a lot about them.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0775"
    if persistent.dpatch:
        sachiko "\"Well, I watch a lot of TV while you guys are at school.\"" id a09_cou3_08_2c922dcf
    else:
        sachiko "\"Well, I watch a lot of TV while you guys are in class.\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1207"
    rin "\"Their agency? I'm gonna complain to them about their sexual harassment of Fumi.\""

    show fumi 2 lg pyjama d with Dissolve(0.25)
    show fumi:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2FU_0922"
    fumi "\"What?!\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    stop music fadeout 1.0

    "Fumi had been speaking quietly on the phone, but she suddenly raised her voice."

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_1208"
    rin "\"What? What is it—\""

    show fumi 1 lg pyjama j with Dissolve(0.25)
    show fumi:
        ShakeSide

    voice "2FU_0923"
    fumi "\"Audition? To be an idol?!\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_1209"
    rin "\"Wha?!\""

    scene black with Dissolve(1.0)
    pause 0.5

    scene continue with Dissolve(2.0)
    pause 2.0

    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
