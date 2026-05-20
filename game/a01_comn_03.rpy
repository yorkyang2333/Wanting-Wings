label a01_comn_03:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    show rin 1 lg school b at pos_r
    show fumi 1 lg school a at pos_l
    with Dissolve(0.25)

    voice "RIN_0047"
    rin "\"Those sports team girls sure like to sweat, huh?\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0037"
    fumi "\"You should say they're putting effort in.\""

    show rin 2 lg school a with dict_dissolve_25

    voice "RIN_0048"
    rin "\"Why? It's not like we've got any teams going to nationals.\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0038"
    fumi "\"You shouldn't say that.\""

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0049"
    rin "\"What were you in in middle school again?\""

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0039"
    fumi "\"The home ec club.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0050"
    rin "\"That's you to a T. I can't picture you competing.\""

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0040"
    fumi "\"Oh? My school won a national cooking contest, you know?\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0051"
    rin "\"Oh yeah? Then why are you clubless now?\""

    show fumi 1 lg school c with dict_dissolve_25

    voice "FUM_0041"
    fumi "\"Well, I'm basically doing home ec club stuff every day now. And you?\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0052"
    rin "\"Clubless for life.\""

    play sound se000c

    $ side_image = "hina 1 side school c"

    voice "HIN_0047"
    hina "\"I'm done!\""

    stop music fadeout 1.0

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show rin 1 sm school c
    show fumi 1 sm school a at pos_l2
    show hina at pos_r2:
        "hina 1 sm school c flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    with Dissolve(0.25)

    play music bgm01

    voice "RIN_0053"
    rin "\"Hey, squirt.\""

    show hina 1 sm school c at pos_r2:
        alpha 1.0 xcenter 852
    with None

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0042"
    fumi "\"Good work, Natsume.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0048"
    hina "\"Are you two the last ones here?\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0043"
    fumi "\"Yep. We've locked up, so we're ready to go.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0054"
    rin "\"Can't believe you'd willingly be a class rep. Sounds like such a pain.\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0049"
    hina "\"It's not that bad. Today, all I had to do was collect handouts and turn them in to the faculty room.\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0055"
    rin "\"Ugh, what a pain.\""

    show hina 1 sm school j with dict_dissolve_25

    voice "HIN_0050"
    hina "\"Oh, and you're the only one who hasn't turned hers in yet, Rin.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0056"
    rin "\"Oh, right.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0051"
    hina "\"You have to get a parent's signature on it. Have you sent it home?\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0057"
    rin "\"Sure did. It'll probably come back today or tomorrow...\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0052"
    hina "\"Okay. You want to stop by the grocery store on the way home, Asou?\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0044"
    fumi "\"That sounds good. The fridge is pretty empty right now.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0058"
    rin "\"Oh, I want to get some shampoo and conditioner.\""

    show hina 1 sm school d with dict_dissolve_25

    voice "HIN_0053"
    hina "\"What? You're out already? Didn't you just buy some the other day?\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0059"
    rin "\"Well, I gotta use a lot.\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0045"
    fumi "\"You do have really long hair... Wow!\""

    "Fumi brushed her fingers through Rin's hair, awed at how silky it was."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_0060"
    rin "\"You just use body wash top to bottom, don't you, Hina?\""

    show hina:
        "hina 1 sm school e" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0054"
    hina "\"I'd ruin my hair! I use shampoo and conditioner like everybody else!\""

    show hina 1 sm school e:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0061"
    rin "\"Conditioner too?\""

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0055"
    hina "\"W-Well, it's in my shampoo.\""

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0062"
    rin "\"You know, it'd be easier to just shave it all off.\""

    show hina 1 sm school i with dict_dissolve_25

    voice "HIN_0056"
    hina "\"No thank you! And why would I do that?!\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0046"
    fumi "\"I don't know, I think you could pull it off.\""

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0057"
    hina "\"Et tu, Asou?!\""

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0063"
    rin "\"We'll come to all your games, Hina!\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0058"
    hina "\"We don't even have a baseball team here!\""

    show hina 1 sm school j:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "HIN_0059"
    hina "\"I'm leaving! You two should get going, too!\""

    show fumi:
        "fumi 1 sm school c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0047"
    fumi "\"Right.\""

    show fumi 1 sm school c:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0064"
    rin "\"Wanna try my shampoo and conditioner sometime, Hina?\""

    show hina 1 sm school i with dict_dissolve_25

    voice "HIN_0060"
    hina "\"No!\""

    show rin 1 sm school f with dict_dissolve_25

    voice "RIN_0065"
    rin "\"It might tame that mess of hair you have, you know.\""

    show hina 1 sm school g with dict_dissolve_25

    voice "HIN_0061"
    hina "\"Lay off! I like my hair like this!\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show hina 1 lg school g with Dissolve(0.25)
    $ side_image = "rin 1 side school f"

    voice "RIN_0066"
    rin "\"Oh. Do you need those wings of yours to sense how wide the doorway is so you don't bang into it?\""

    show hina 1 lg school f with dict_dissolve_25

    voice "HIN_0062"
    hina "\"What are they, cat whiskers?!\""

    $ side_image = "fumi 1 side school e"

    voice "FUM_0048"
    fumi "\"Ah, watch where you're going, Natsume!\""

    play sound se104b


    show hina:
        "hina 2 lg school i" with Dissolve(0.25)
    camera:
        function LayerShake(30,30,0.5)
    $ persistent.layer_shaken = False

    voice "HIN_0063"
    hina "\"Ugyah?!\""

    camera
    with None

    show hina:
        "hina 2 lg school i flat"
        alpha 1.0 yoffset 0
        easeout 0.25 alpha 0.0 yoffset 100

    play sound se203a

    scene black with Dissolve(0.5)
    pause 0.5

    $ side_image = "fumi 1 side school j"

    voice "FUM_0049"
    fumi "\"A-Are you okay?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
