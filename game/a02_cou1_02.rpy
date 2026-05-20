label a02_cou1_02:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play music bgm02

    show fumi:
        "fumi 1 sm pyjama a flat"
        alpha 0.0 xcenter 72
        easein 0.5 alpha 1.0 xcenter 172
    show hina:
        "hina 1 sm pyjama a flat"
        alpha 0.0 xcenter 312
        easein 0.5 alpha 1.0 xcenter 412
    pause 0.5

    show fumi 1 sm pyjama a:
        alpha 1.0 xcenter 172
    show hina 1 sm pyjama a:
        alpha 1.0 xcenter 412
    with None

    voice "HIN_0511"
    hina "\"Sachikooo, we come bearing gifts.\""

    "She didn't seem to be in her room."

    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0388"
    fumi "\"Guess she's not home.\""

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0512"
    hina "\"What should we do with these?\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0389"
    fumi "\"We can just put them in the fridge and give them to her tomorrow morning.\""

    "Hina agreed and the two of them were just about to leave, when..."

    play sound se123b
    pause 1.5

    show sachiko 1 sm outfit a:
        xcenter 792
    with Dissolve(0.25)

    voice "SYO_0065"
    sachiko "\"Hm? What's up?\""

    "Sachiko came down the stairs, smelling of cigarettes."

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0390"
    fumi "\"Perfect timing. We were just having a birthday party for Natsume, so we came to share some food.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0066"
    sachiko "\"Aw, thanks for sharing with me all the time. Whoa, what a feast!\""

    "Sachiko peeked under the plastic wrap on the plate they handed her."

    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0513"
    hina "\"And here's some cake and champagne.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0067"
    sachiko "\"Champagne? Why do you have that?\""

    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0391"
    fumi "\"My father accidentally gave us some.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0068"
    sachiko "\"Very well. I shall take this and dispose of it for you.\""

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0392"
    fumi "\"Thanks for going and picking up the cake for us.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0069"
    sachiko "\"Oh, it was no trouble. I even got some pudding from your dad for taking 'such good care of you.'\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0070"
    sachiko "\"Oh, that's right...\""

    "She stuck her hand in her pocket as if suddenly remembering something."

    show sachiko 1 sm outfit g with dict_dissolve_25

    play sound se565

    show sachiko:
        ShakeYes

    voice "SYO_0071"
    sachiko "\"Here, happy birthday.\""

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama a
    show hina 1 sm pyjama k
    with dict_dissolve_25

    voice "HIN_0514"
    hina "\"What's this?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0072"
    sachiko "\"The key to the roof. The stars are real pretty tonight, so go check 'em out.\""

    show hina:
        "hina 1 sm pyjama c" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0515"
    hina "\"Oh, wow! Thanks!\""

    show hina 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0073"
    sachiko "\"But it's chilly, so don't catch cold.\""

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0516"
    hina "\"Okay! Let's go, Asou!\""

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0393"
    fumi "\"Sure!\""

    stop music fadeout 1.0

    scene black with bg_effect_01_1000
    scene bg07ca with bg_effect_01_1000
    pause 0.5

    play music bgm05

    show hina 1 lg pyjama c at pos_r
    show fumi 1 lg pyjama b at pos_l
    with Dissolve(0.25)

    voice "HIN_0517"
    hina "\"Whoa! It's like they're right on top of us.\""

    "Hina reached out and made as if to grab the stars."

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0394"
    fumi "\"It's beautiful.\""

    "The two stood with their backs to the fence, looking up at the sky."

    scene black with bg_effect_14
    pause 0.25
    scene bg08ca with bg_effect_14
    pause 0.75

    $ side_image = "hina 1 side pyjama c"

    voice "HIN_0518"
    hina "\"This was a really nice birthday. I got to have a party, get some presents, and see these pretty stars with you at the end...\""

    scene black with bg_effect_13
    pause 0.25
    scene bg07ca
    show fumi 1 lg pyjama a at pos_l
    show hina 1 lg pyjama d at pos_r
    with bg_effect_13
    pause 0.75

    show hina:
        ShakeSide

    voice "HIN_0519"
    hina "\"Oh, not that I wouldn't like seeing them with Rin, but, you know, umm...\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Fumi smiled, waiting for Hina to find the words."

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0520"
    hina "\"I just mean, I'm even happier that you're the one here... Like, I would be happy with Rin, but I'm more happy with you!\""

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0395"
    fumi "\"I feel the same way.\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0521"
    hina "\"Hunh?\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0396"
    fumi "\"I'm also glad I'm looking at these stars with you, Natsume.\""

    show hina 2 lg pyjama c with Dissolve(0.25)
    show hina:
        ShakeNo

    voice "HIN_0522"
    hina "\"Heh... heheheh.\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina blushed and ran a hand through her hair."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0523"
    hina "\"Really though, thanks for today.\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0397"
    fumi "\"It was no trouble. I love parties. It makes me happy to see people enjoying themselves.\""

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0524"
    hina "\"My mom and my sister have said the same thing.\""

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0398"
    fumi "\"Do you not like parties?\""

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0525"
    hina "\"No, that's not it at all! I had a lot of fun.\""

    "Hina looked up at the sky again."

    scene black with bg_effect_14
    pause 0.25
    scene bg08ca with bg_effect_14
    pause 0.75

    $ side_image = "hina 1 side pyjama h"

    voice "HIN_0526"
    hina "\"Sheesh... I wonder why I can't be girly like you, Asou.\""

    "The puff of air Hina breathed out briefly hung in the air, like a feather."

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0527"
    if persistent.dpatch:
        hina "\"I thought maybe I could be a bit cuter if I came to this school, but I'm just the same as always.\"" id a02_cou1_02_49ac0dab
    else:
        hina "\"I thought maybe I could be a bit cuter if I came to this campus, but I'm just the same as always.\""

    $ side_image = "fumi 2 side pyjama f"

    voice "FUM_0399"
    fumi "\"You're too hard on yourself. You {i}are{/i} cute, Natsume!\""

    scene black with bg_effect_13
    pause 0.25
    scene bg07ca
    show fumi 1 lg pyjama g at pos_l
    show hina 1 lg pyjama d at pos_r
    with bg_effect_13
    pause 0.75

    show hina:
        ShakeSide

    voice "HIN_0528"
    hina "\"Ah, unh?\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0400"
    fumi "\"I want to be more like you, Natsume.\""

    show hina 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0529"
    hina "\"Wh-Why? There's nothing good about me!\""

    show fumi 1 lg pyjama g with dict_dissolve_25

    voice "FUM_0401"
    fumi "\"That's not true. You're little but you work so hard, and you're so cute, I always want to hug you.\""

    show hina 2 lg pyjama h with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_0530"
    hina "\"U-Uuugh...\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0402"
    fumi "\"So you should stay just how you are, Natsume.\""

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0531"
    hina "\"Then... you should stay how you are too, Asou.\""

    show fumi:
        "fumi 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0403"
    fumi "\"Alright.\""

    show fumi 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0532"
    hina "\"Umm, I have an idea, then. We should call each other by our first names, don't you think?\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0404"
    fumi "\"Oh! You're right. We're too close now to use our last names. Alright... Hina?\""

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0533"
    hina "\"Y-Yeah? ...Fumi...\""

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0405"
    fumi "\"Eheheh.\""

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0534"
    hina "\"...Heheh.\""

    "Hina and Fumi looked at each other and laughed."

    show hina:
        "hina 2 lg pyjama g" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 532

    play sound se118a

    voice "HIN_0535"
    hina "\"Yah!\""

    "Hina spun against the fence into a hug with Fumi."

    show fumi:
        "fumi 2 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0406"
    fumi "\"Hya! You're so cold, Hina!\""

    show fumi 2 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0536"
    hina "\"And you're nice and warm, Fumi.\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0407"
    fumi "\"...Want to stay like this for a bit?\""

    show hina:
        ShakeYes

    voice "HIN_0537"
    hina "\"Yeah...\""

    stop music fadeout 3.0

    scene black with Dissolve(1.0)
    pause 1.0

    play sound se_bati

    show bati at truecenter

    pause 2.5

    scene bg05ca with bg_effect_02
    pause 0.5

    play music bgm02

    show sachiko 1 sm outfit a at pos_l2
    show fumi 1 sm pyjama a at pos_r2
    show hina 1 sm pyjama a:
        xcenter 652
    with Dissolve(0.25)

    voice "SYO_0074"
    sachiko "\"You're finally back. I was about to go check on you since you were up there so long.\""

    show hina 1 sm pyjama c with dict_dissolve_25

    voice "HIN_0538"
    hina "\"Thanks for the key. The stars were really pretty.\""

    show sachiko:
        "sachiko 1 sm outfit h" with Dissolve(0.25)
        ShakeSide

    voice "SYO_0075"
    sachiko "\"That's goo—cold!\""

    show sachiko 1 sm outfit h:
        xoffset 0 yoffset 0
    with None

    "Sachiko was shocked by how cold Hina's fingers were."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "SYO_0076"
    sachiko "\"You're chilled to the bone! It's gonna be tragic if you catch a cold right before Christmas, you know?\""

    show hina:
        "hina 1 sm pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0539"
    hina "\"I'm oka...achoo!\""

    show hina 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 1 sm pyjama e" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0408"
    fumi "\"Wawah, let's get back to our room, Hina!\""

    show fumi 1 sm pyjama e:
        xoffset 0 yoffset 0
    with None

    "Fumi grabbed Hina's hands."

    show fumi 1 sm pyjama e flat:
        alpha 1.0 xcenter 852
        easeout 0.5 alpha 0.0 xcenter 752
    show hina 1 sm pyjama d flat:
        alpha 1.0 xcenter 652
        easeout 0.5 alpha 0.0 xcenter 552
    pause 0.5

    hide fumi
    hide hina
    with None

    show sachiko:
        "sachiko 1 sm outfit a" with Dissolve(0.5)
        xcenter 172
        easein 0.5 xcenter 512
    pause 0.5

    voice "SYO_0077"
    sachiko "\"Hm? ...Oho.\""

    "Sachiko stopped Hina before she could leave."

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "SYO_0078"
    sachiko "\"Hinacchi.\""

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0540"
    hina "\"Hm?\""

    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "SYO_0079"
    sachiko "\"Didja kiss?\""

    $ side_image = "hina 1 side pyjama g"

    voice "HIN_0541"
    hina "\"O-Of course not!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
