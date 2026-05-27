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
    hina "\"Sachikooo, we come bearing gifts.\"" id a02_cou1_02_dc8aa886

    "She didn't seem to be in her room."

    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0388"
    fumi "\"Guess she's not home.\"" id a02_cou1_02_2ca562cc

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0512"
    hina "\"What should we do with these?\"" id a02_cou1_02_a1e01fc6

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0389"
    fumi "\"We can just put them in the fridge and give them to her tomorrow morning.\"" id a02_cou1_02_4c7eae68

    "Hina agreed and the two of them were just about to leave, when..."

    play sound se123b
    pause 1.5

    show sachiko 1 sm outfit a:
        xcenter 792
    with Dissolve(0.25)

    voice "SYO_0065"
    sachiko "\"Hm? What's up?\"" id a02_cou1_02_29248c64

    "Sachiko came down the stairs, smelling of cigarettes."

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0390"
    fumi "\"Perfect timing. We were just having a birthday party for Natsume, so we came to share some food.\"" id a02_cou1_02_d4a978bb

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0066"
    sachiko "\"Aw, thanks for sharing with me all the time. Whoa, what a feast!\"" id a02_cou1_02_8d8c478d

    "Sachiko peeked under the plastic wrap on the plate they handed her."

    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0513"
    hina "\"And here's some cake and champagne.\"" id a02_cou1_02_cb3e73c1

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0067"
    sachiko "\"Champagne? Why do you have that?\"" id a02_cou1_02_624c622c

    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0391"
    fumi "\"My father accidentally gave us some.\"" id a02_cou1_02_e6f9a304

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0068"
    sachiko "\"Very well. I shall take this and dispose of it for you.\"" id a02_cou1_02_1aefb678

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0392"
    fumi "\"Thanks for going and picking up the cake for us.\"" id a02_cou1_02_268f19c7

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0069"
    sachiko "\"Oh, it was no trouble. I even got some pudding from your dad for taking 'such good care of you.'\"" id a02_cou1_02_52521729

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0070"
    sachiko "\"Oh, that's right...\"" id a02_cou1_02_0b97f54d

    "She stuck her hand in her pocket as if suddenly remembering something."

    show sachiko 1 sm outfit g with dict_dissolve_25

    play sound se565

    show sachiko:
        ShakeYes

    voice "SYO_0071"
    sachiko "\"Here, happy birthday.\"" id a02_cou1_02_0db1159e

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama a
    show hina 1 sm pyjama k
    with dict_dissolve_25

    voice "HIN_0514"
    hina "\"What's this?\"" id a02_cou1_02_6f619918

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0072"
    sachiko "\"The key to the roof. The stars are real pretty tonight, so go check 'em out.\"" id a02_cou1_02_97681cb1

    show hina:
        "hina 1 sm pyjama c" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0515"
    hina "\"Oh, wow! Thanks!\"" id a02_cou1_02_8d8bd9ca

    show hina 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0073"
    sachiko "\"But it's chilly, so don't catch cold.\"" id a02_cou1_02_7a4bf323

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0516"
    hina "\"Okay! Let's go, Asou!\"" id a02_cou1_02_1aeb76d3

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0393"
    fumi "\"Sure!\"" id a02_cou1_02_1b244be0

    stop music fadeout 1.0

    scene black with bg_effect_01_1000
    scene bg07ca with bg_effect_01_1000
    pause 0.5

    play music bgm05

    show hina 1 lg pyjama c at pos_r
    show fumi 1 lg pyjama b at pos_l
    with Dissolve(0.25)

    voice "HIN_0517"
    hina "\"Whoa! It's like they're right on top of us.\"" id a02_cou1_02_866a2a85

    "Hina reached out and made as if to grab the stars."

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0394"
    fumi "\"It's beautiful.\"" id a02_cou1_02_d0c85947

    "The two stood with their backs to the fence, looking up at the sky."

    scene black with bg_effect_14
    pause 0.25
    scene bg08ca with bg_effect_14
    pause 0.75

    $ side_image = "hina 1 side pyjama c"

    voice "HIN_0518"
    hina "\"This was a really nice birthday. I got to have a party, get some presents, and see these pretty stars with you at the end...\"" id a02_cou1_02_55e65ba6

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
    hina "\"Oh, not that I wouldn't like seeing them with Rin, but, you know, umm...\"" id a02_cou1_02_e65e90cf

    show hina:
        xoffset 0 yoffset 0
    with None

    "Fumi smiled, waiting for Hina to find the words."

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0520"
    hina "\"I just mean, I'm even happier that you're the one here... Like, I would be happy with Rin, but I'm more happy with you!\"" id a02_cou1_02_82e55a10

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0395"
    fumi "\"I feel the same way.\"" id a02_cou1_02_bca3d5f3

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0521"
    hina "\"Hunh?\"" id a02_cou1_02_fe300f58

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0396"
    fumi "\"I'm also glad I'm looking at these stars with you, Natsume.\"" id a02_cou1_02_f7693f6e

    show hina 2 lg pyjama c with Dissolve(0.25)
    show hina:
        ShakeNo

    voice "HIN_0522"
    hina "\"Heh... heheheh.\"" id a02_cou1_02_87183d24

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina blushed and ran a hand through her hair."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0523"
    hina "\"Really though, thanks for today.\"" id a02_cou1_02_6a7392b5

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0397"
    fumi "\"It was no trouble. I love parties. It makes me happy to see people enjoying themselves.\"" id a02_cou1_02_77e5780d

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0524"
    hina "\"My mom and my sister have said the same thing.\"" id a02_cou1_02_7e32f3ad

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0398"
    fumi "\"Do you not like parties?\"" id a02_cou1_02_a7a3b8f6

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0525"
    hina "\"No, that's not it at all! I had a lot of fun.\"" id a02_cou1_02_e9452661

    "Hina looked up at the sky again."

    scene black with bg_effect_14
    pause 0.25
    scene bg08ca with bg_effect_14
    pause 0.75

    $ side_image = "hina 1 side pyjama h"

    voice "HIN_0526"
    hina "\"Sheesh... I wonder why I can't be girly like you, Asou.\"" id a02_cou1_02_01f6be4a

    "The puff of air Hina breathed out briefly hung in the air, like a feather."

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0527"
    if persistent.dpatch:
        hina "\"I thought maybe I could be a bit cuter if I came to this school, but I'm just the same as always.\"" id a02_cou1_02_49ac0dab
    else:
        hina "\"I thought maybe I could be a bit cuter if I came to this campus, but I'm just the same as always.\"" id a02_cou1_02_1c23ec8d

    $ side_image = "fumi 2 side pyjama f"

    voice "FUM_0399"
    fumi "\"You're too hard on yourself. You {i}are{/i} cute, Natsume!\"" id a02_cou1_02_e14f2c44

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
    hina "\"Ah, unh?\"" id a02_cou1_02_ed55f377

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0400"
    fumi "\"I want to be more like you, Natsume.\"" id a02_cou1_02_59c2bd4f

    show hina 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0529"
    hina "\"Wh-Why? There's nothing good about me!\"" id a02_cou1_02_441546e2

    show fumi 1 lg pyjama g with dict_dissolve_25

    voice "FUM_0401"
    fumi "\"That's not true. You're little but you work so hard, and you're so cute, I always want to hug you.\"" id a02_cou1_02_08cff845

    show hina 2 lg pyjama h with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_0530"
    hina "\"U-Uuugh...\"" id a02_cou1_02_98b53e86

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0402"
    fumi "\"So you should stay just how you are, Natsume.\"" id a02_cou1_02_b713fec5

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0531"
    hina "\"Then... you should stay how you are too, Asou.\"" id a02_cou1_02_28ebc339

    show fumi:
        "fumi 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0403"
    fumi "\"Alright.\"" id a02_cou1_02_ad462696

    show fumi 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0532"
    hina "\"Umm, I have an idea, then. We should call each other by our first names, don't you think?\"" id a02_cou1_02_912988ac

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0404"
    fumi "\"Oh! You're right. We're too close now to use our last names. Alright... Hina?\"" id a02_cou1_02_49f5bdbe

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0533"
    hina "\"Y-Yeah? ...Fumi...\"" id a02_cou1_02_4bd03442

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0405"
    fumi "\"Eheheh.\"" id a02_cou1_02_1476d2aa

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0534"
    hina "\"...Heheh.\"" id a02_cou1_02_9190518f

    "Hina and Fumi looked at each other and laughed."

    show hina:
        "hina 2 lg pyjama g" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 532

    play sound se118a

    voice "HIN_0535"
    hina "\"Yah!\"" id a02_cou1_02_49d99cb8

    "Hina spun against the fence into a hug with Fumi."

    show fumi:
        "fumi 2 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0406"
    fumi "\"Hya! You're so cold, Hina!\"" id a02_cou1_02_a0d3b74a

    show fumi 2 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0536"
    hina "\"And you're nice and warm, Fumi.\"" id a02_cou1_02_616a415e

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0407"
    fumi "\"...Want to stay like this for a bit?\"" id a02_cou1_02_14bd3577

    show hina:
        ShakeYes

    voice "HIN_0537"
    hina "\"Yeah...\"" id a02_cou1_02_5507fe21

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
    sachiko "\"You're finally back. I was about to go check on you since you were up there so long.\"" id a02_cou1_02_0a7fd3e1

    show hina 1 sm pyjama c with dict_dissolve_25

    voice "HIN_0538"
    hina "\"Thanks for the key. The stars were really pretty.\"" id a02_cou1_02_b58f9b8e

    show sachiko:
        "sachiko 1 sm outfit h" with Dissolve(0.25)
        ShakeSide

    voice "SYO_0075"
    sachiko "\"That's goo—cold!\"" id a02_cou1_02_08272fb6

    show sachiko 1 sm outfit h:
        xoffset 0 yoffset 0
    with None

    "Sachiko was shocked by how cold Hina's fingers were."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "SYO_0076"
    sachiko "\"You're chilled to the bone! It's gonna be tragic if you catch a cold right before Christmas, you know?\"" id a02_cou1_02_ab7a1174

    show hina:
        "hina 1 sm pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0539"
    hina "\"I'm oka...achoo!\"" id a02_cou1_02_2b96df90

    show hina 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 1 sm pyjama e" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0408"
    fumi "\"Wawah, let's get back to our room, Hina!\"" id a02_cou1_02_4a3026a5

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
    sachiko "\"Hm? ...Oho.\"" id a02_cou1_02_82d6dfb6

    "Sachiko stopped Hina before she could leave."

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "SYO_0078"
    sachiko "\"Hinacchi.\"" id a02_cou1_02_545e8501

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0540"
    hina "\"Hm?\"" id a02_cou1_02_2b37b282

    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "SYO_0079"
    sachiko "\"Didja kiss?\"" id a02_cou1_02_38f4a35b

    $ side_image = "hina 1 side pyjama g"

    voice "HIN_0541"
    hina "\"O-Of course not!\"" id a02_cou1_02_acc11d1d

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
