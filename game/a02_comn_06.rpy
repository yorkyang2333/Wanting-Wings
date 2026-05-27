label a02_comn_06:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show rin 1 lg pyjama glasses a at pos_r
    show fumi 2 lg pyjama g at pos_l
    with Dissolve(0.25)

    voice "FUM_0286"
    fumi "\"Can you expand this problem?\"" id a02_comn_06_7077bb08

    "Rin peered over at Fumi's workbook."

    show rin 2 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0326"
    rin "\"Ah, for this type, it's easier to understand if you replace one letter in these formulas. For instance, if you replace this 'a+b' with 'A'...?\"" id a02_comn_06_69933650

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0287"
    fumi "\"Umm, it goes like this, and this... Oh, I think I can expand it!\"" id a02_comn_06_f38608c2

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0327"
    rin "\"Yep. Don't forget to put it back at the end.\"" id a02_comn_06_2c6303bf

    show fumi:
        "fumi 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0288"
    fumi "\"Right!\"" id a02_comn_06_62d2722c

    show fumi 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama j"

    voice "HIN_0386"
    hina "\"Advance, {i}susumeru{/i}. Destination, {i}mokutekichi{/i}. Plural, {i}fukusuu no{/i}.\"" id a02_comn_06_76086586

    "Hina was single-mindedly writing English vocab words and their meanings down in her notebook. She seemed like she was choosing the brute-force approach."

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0387"
    hina "\"Wealth, {i}tomi{/i}. Sentiment, {i}kanjou{/i}. Resolve, {i}toku{/i}...\"" id a02_comn_06_8c189518

    "Her incantations suddenly ceased."

    hide rin
    hide fumi
    with Dissolve(0.05)
    pause 0.2

    play sound se203a

    show hina:
        "hina z3 1 lg pyjama g flat"
        alpha 0.0 xcenter 512
        parallel:
            ShakeTameiki
        parallel:
            linear 0.25 alpha 1.0

    voice "HIN_0388"
    hina "\"Daaah!\"" id a02_comn_06_d8bcad9b

    show hina z3 1 lg pyjama g:
        alpha 1.0 xcenter 512 xoffset 0 yoffset 0
    with None

    "Hina faceplanted onto the table."

    show rin z3 1 lg pyjama glasses j behind hina at pos_r2_z3
    show fumi z3 1 lg pyjama e behind hina at pos_l2_z3
    with Dissolve(0.25)

    show rin:
        ShakeSide

    voice "RIN_0328"
    rin "\"Whoa, what the heck?!\"" id a02_comn_06_f73d1d7b

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0389"
    hina "\"Do you guys like skiing?\"" id a02_comn_06_a1e07ef7

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0289"
    fumi "\"Th-That was rather sudden.\"" id a02_comn_06_3ca527e1

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0390"
    hina "\"Let's talk about winter break!\"" id a02_comn_06_1d9dddcf

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0329"
    rin "\"Ah, the attempts to escape reality begin.\"" id a02_comn_06_73c9509c

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0290"
    fumi "\"This seems like a good time for a break.\"" id a02_comn_06_5d25d410

    scene black with bg_effect_05
    pause 0.5

    scene bg01ca with bg_effect_05
    pause 0.5

    show fumi z3 2 lg pyjama b behind rin, hina at pos_l2_z3
    show rin z3 1 lg pyjama glasses a behind hina at pos_r2_z3
    show hina z3 1 lg pyjama a
    with Dissolve(0.25)

    voice "HIN_0391"
    hina "\"What are you gonna do for New Year's? I'm going home after Christmas.\"" id a02_comn_06_737857f8

    voice "FUM_0291"
    fumi "\"I think I'm going to go home around that time, too.\"" id a02_comn_06_73508323

    "And Rin?"

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0330"
    rin "\"I'm staying here.\"" id a02_comn_06_360b053a

    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0392"
    hina "\"Huh? Really? You're not going home for break?\"" id a02_comn_06_a217eb47

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0331"
    rin "\"It's not like anybody'll be there if I go.\"" id a02_comn_06_89a6c375

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0292"
    fumi "\"What about your parents?\"" id a02_comn_06_cafb6966

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0332"
    rin "\"They'll be in Europe for New Year's.\"" id a02_comn_06_c03bc65b

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0393"
    hina "\"What?! They're going overseas and leaving you here? That's kinda mean.\"" id a02_comn_06_4368712d

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin z3 2 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0333"
    rin "\"No, it's for work. There's an academic conference.\"" id a02_comn_06_e84b6ed1

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0394"
    hina "\"Your dad's a university professor, right?\"" id a02_comn_06_25496bc3

    show rin:
        ShakeYes

    voice "RIN_0334"
    rin "\"Yep. And my mom's his assistant. So I'll hold down the fort here.\"" id a02_comn_06_121c3900

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0293"
    fumi "\"Is anyone else staying here for the break?\"" id a02_comn_06_ba805e57

    show rin z3 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0335"
    rin "\"I dunno. I imagine Sachiko will be here.\"" id a02_comn_06_b043918e

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0395"
    hina "\"What?! Isn't that kinda risky?\"" id a02_comn_06_11511d9b

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama f with dict_dissolve_25

    voice "FUM_0294"
    fumi "\"I suppose I would be a bit worried about that.\"" id a02_comn_06_e48a9019

    "...They really don't trust her."

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0336"
    rin "\"Right. I guess that's an option if I'm lonely.\"" id a02_comn_06_c7c7454f

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0396"
    hina "\"Nooo! Be sure to remember to lock the door!\"" id a02_comn_06_967f5545

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z3 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0337"
    rin "\"I-I'm joking.\"" id a02_comn_06_1ed4f917

    show rin z3 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0397"
    hina "\"I'm worried. Should I stay here, too?\"" id a02_comn_06_75f6f8e2

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0338"
    rin "\"It's fine. You've got family waiting for you, right? Spend your New Year's with them.\"" id a02_comn_06_50527d93

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0398"
    hina "\"Mm~, well then, let's all go to a shrine together! And we can have a party, too!\"" id a02_comn_06_4e7f1bf0

    show fumi:
        "fumi z3 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0295"
    fumi "\"Oh, that's a good idea! I can bring some food from home!\"" id a02_comn_06_d955e6a6

    show fumi z3 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0339"
    rin "\"O-Okay.\"" id a02_comn_06_be3113df

    show fumi z3 2 lg pyjama h
    show hina z3 1 lg pyjama k
    with Dissolve(0.25)

    voice "HIN_0399"
    hina "\"You don't want to?\"" id a02_comn_06_7f91b9ba

    show rin:
        "rin z3 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeUji

    voice "RIN_0340"
    rin "\"No... that's not it...\"" id a02_comn_06_0e4b5ada

    show rin z3 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0400"
    hina "\"Y-You don't have plans with Sachiko, do you?!\"" id a02_comn_06_a0fe6b8a

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z3 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeNo

    voice "RIN_0341"
    rin "\"No, no, no. No way.\"" id a02_comn_06_af4a1465

    show rin z3 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0296"
    fumi "\"I hope we're not being too pushy...\"" id a02_comn_06_6f05dcaf

    show rin z3 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0342"
    rin "\"Of course not. I'm happy you're thinking of me. I'm kinda sorry to make you, in fact.\"" id a02_comn_06_53841617

    show hina z3 1 lg pyjama e with dict_dissolve_25

    voice "HIN_0401"
    hina "\"It's not like that. I've wanted to go to a shrine and stuff with you two.\"" id a02_comn_06_4fc098f1

    show rin z3 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0343"
    rin "\"I've never even done that with my family before.\"" id a02_comn_06_e782eb4f

    show hina z3 1 lg pyjama b with dict_dissolve_25

    voice "HIN_0402"
    hina "\"Then you can think of us as your family.\"" id a02_comn_06_79f3203a

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0344"
    rin "\"......\"" id a02_comn_06_d5941b2e

    show fumi z3 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0297"
    fumi "\"She's right. We've lived together for months now. You don't need to worry about being a bother.\"" id a02_comn_06_6fa7c57c

    show rin z3 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0345"
    rin "\"Hina, Asou...\"" id a02_comn_06_580d26d8

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0403"
    hina "\"Hm?\"" id a02_comn_06_c6582d27


    show rin behind hina:
        "rin z3 1 lg pyjama glasses d" with Dissolve(0.25)
        xcenter 842 yoffset 0
        easein 0.25 xcenter 299 yoffset 64
    show fumi behind rin:
        "fumi z3 2 lg pyjama d" with Dissolve(0.25)
        xcenter 182
        easein 0.25 xcenter 108
    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 492
    pause 0.25

    play sound se118b

    show rin z3 1 lg pyjama glasses d:
        xcenter 299 yoffset 64
    with None
    show fumi z3 2 lg pyjama d:
        xcenter 108
        ShakeSide
    show hina z3 1 lg pyjama d:
        xcenter 492
        ShakeSide

    voice "RIN_0346"
    rin "\"I love youuu!\"" id a02_comn_06_cc35cbda

    show rin:
        "rin z3 1 lg pyjama glasses d flat"
        alpha 1.0 xcenter 299 yoffset 64
        easeout 0.5 alpha 0.0 xcenter 199
    show fumi:
        "fumi z3 2 lg pyjama d flat"
        alpha 1.0 xcenter 108
        easeout 0.5 alpha 0.0 xcenter 8
    show hina:
        "hina z3 1 lg pyjama d flat"
        alpha 1.0 xcenter 492
        easeout 0.5 alpha 0.0 xcenter 392
    pause 0.5

    play sound se113da

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    $ side_image = "fumi 1 side pyjama j"

    voice "FUM_0298"
    fumi "\"Aaah?!\"" id a02_comn_06_d1f5ddd2

    camera
    with None

    play sound se113da

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    $ side_image = "hina 1 side pyjama g"

    voice "HIN_0404"
    hina "\"Not this punchline again!\"" id a02_comn_06_20316d7a

    camera
    with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
