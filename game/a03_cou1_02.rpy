label a03_cou1_02:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play music bgm04

    show fumi:
        "fumi 1 lg pyjama a flat"
        alpha 0.0 xcenter 272
        easein 1.0 alpha 1.0 xcenter 172
    pause 1.0

    show fumi 1 lg pyjama a at pos_l2:
        alpha 1.0 xcenter 172
    with None
    play sound se001a

    pause 0.5

    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "HIN_0690"
    hina "\"Wah! I'm still changing!\""

    show fumi:
        "fumi 1 lg pyjama j" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0509"
    fumi "\"Aah! I-I'm sorry!\""

    show fumi 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None
    play sound se002a

    pause 0.5

    show fumi:
        "fumi 1 lg pyjama h" with Dissolve(0.25)
        xcenter 172
        easein 0.25 xcenter 192

    voice "FUM_0510"
    fumi "\"I'm really sorry.\""

    show fumi 1 lg pyjama h:
        xcenter 192
    with None

    "Fumi apologized again, her back to the bathroom door."

    voice "HIN_0691"
    hina "\"It's alright. We're all girls here.\""

    "Hina's tone was indifferent."

    voice "HIN_0692"
    hina "\"I'm sorry for freaking out.\""

    "Fumi could hear Hina toweling off behind the door."

    voice "HIN_0693"
    hina "\"And it's not like my body's anything to see.\""

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0511"
    fumi "\"That's not true! I thought your back was very pretty when I saw it.\""

    voice "HIN_0694"
    hina "\"Ahaha, you're the only one who'd say something like that, Fumi.\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0512"
    fumi "\"...But...\""

    voice "HIN_0695"
    hina "\"Hm? What is it?\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0513"
    fumi "\"Well, you don't have wings, huh?\""

    voice "HIN_0696"
    hina "\"If I did, it'd be inconvenient, don't you think? I wouldn't be able to wear shirts!\""

    play sound se001a

    show fumi:
        "fumi 1 lg pyjama d" with Dissolve(0.25)
        xcenter 192
        easein 0.5 xcenter 512
    show hina:
        "hina 1 lg pyjama a flat"
        alpha 0.0 xcenter 72
        easein 0.5 alpha 1.0 xcenter 172
    pause 0.5

    voice "HIN_0697"
    hina "\"Thanks for waiting.\""

    show fumi 1 lg pyjama d:
        xcenter 512
    show hina 1 lg pyjama a:
        alpha 1.0 xcenter 172
    with None
    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0514"
    fumi "\"I was hoping you'd be the angel.\""

    show hina:
        "hina 1 lg pyjama c" with Dissolve(0.25)
        2.0
        "hina 2 lg pyjama h" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0698"
    hina "\"Ahaha, sorry. ...Ngh.\""

    show hina 2 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0515"
    fumi "\"A-Are you cold?\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0699"
    hina "\"Mm, a little bit.\""

    show fumi 1 lg pyjama j with dict_dissolve_25

    voice "FUM_0516"
    fumi "\"I'm sorry, you're right out of the bath! You should get back to the room before you get sick.\""

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0700"
    hina "\"Yeah, I'll do that... thanks.\""

    show hina:
        "hina 1 lg pyjama a flat"
        alpha 1.0 xcenter 172
        easeout 0.5 alpha 0.0 xcenter 72
    pause 1.0

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "FUM_0517"
    fumi "\"......\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
