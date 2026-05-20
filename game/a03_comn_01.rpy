label a03_comn_01:

    scene expression "gui/kimihane/mainmenu_ground1.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter03 with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg02aa with Dissolve(0.5)
    pause 1.5

    play sound se027a_180

    show fumi 3 sm light pyjama a with Dissolve(0.25)

    voice "FUM_0463"
    fumi "\"Nnh...\""

    "Fumi's phone buzzed by her pillow and she opened her eyes."

    "It was 6:30. Rin and Hina were still sound asleep. Fumi was up at this hour to make their lunches."

    stop sound fadeout 0.25
    pause 0.5

    play sound se116a

    hide fumi with Dissolve(0.05)
    pause 0.2

    show fumi 1 sm pyjama h with Dissolve(0.25)
    show fumi:
        ShakeSide

    voice "FUM_0464"
    fumi "\"Cold...\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi got out of bed, shivering at the drop in temperature when she left her blankets."

    "She donned her slippers and was about to head to the kitchen as she always did, when..."

    show fumi 1 sm pyjama g with dict_dissolve_25

    voice "FUM_0465"
    fumi "\"...?\""

    show fumi:
        ShakeTameiki

    "She noticed something by her feet and picked it up."

    show fumi 1 sm pyjama e:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "FUM_0466"
    fumi "\"...What's this?\""

    "It was..."

    scene black with Dissolve(0.75)
    pause 2.7

    scene bg02aa with bg_effect_05
    pause 0.5

    play music bgm01

    show rin 1 lg school a
    show fumi 2 lg school b at pos_l2
    with Dissolve(0.25)

    show fumi:
        ShakeYes

    voice "FUM_0467"
    fumi "\"Whose feather could it be? Here's your lunch.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0513"
    rin "\"Yep. 'Whose?' A bird's, right?\""

    show fumi:
        "fumi 2 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0468"
    fumi "\"And your commuter pass. Or an angel...\""

    show fumi 2 lg school c:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0514"
    rin "\"Yep. Oh, right.\""

    hide fumi with Dissolve(0.25)

    show hina 2 lg school f at pos_r2
    with Dissolve(0.25)

    voice "HIN_0633"
    hina "\"I don't think I've seen many like that, though. It's definitely not a pigeon's or a crow's.\""

    show fumi 2 lg school b at pos_l2
    with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "FUM_0469"
    fumi "\"Your wallet. Right?\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "RIN_0515"
    rin "\"Yep. It's not from yesterday's turkey?\""

    show hina 1 lg school f with dict_dissolve_25

    voice "HIN_0634"
    hina "\"We didn't have turkey!\""

    show fumi:
        "fumi 2 lg school b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0470"
    fumi "\"And your handkerchief. It's really big and white, right?\""

    show fumi 2 lg school b:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0516"
    rin "\"Thanks. What was it doing in the room, anyway? We didn't sleep with the window open last night, did we?\""

    show fumi 2 lg school f with dict_dissolve_25

    voice "FUM_0471"
    fumi "\"No, it was closed.\""

    show hina 2 lg school e with dict_dissolve_25

    voice "HIN_0635"
    hina "\"I don't mind talking about this, but we've gotta leave soon, or we'll end up running.\""

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0472"
    fumi "\"Oh. You're right.\""

    show rin:
        "rin 1 lg school d" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0517"
    rin "\"I know. While you two are in class, I'll investigate this feather.\""

    show rin 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0636"
    hina "\"You will not! Come on, let's go!\""

    show hina 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0518"
    rin "\"Yeah, yeah.\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    play sound se522

    stop music fadeout 5.0

    "........."

    "......"

    "The feather danced atop the table."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a03_cou3_01
    elif rin_hina_score > hina_fumi_score:
        jump a03_cou2_01
    else:
        jump a03_cou1_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
