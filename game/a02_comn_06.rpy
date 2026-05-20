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
    fumi "\"Can you expand this problem?\""

    "Rin peered over at Fumi's workbook."

    show rin 2 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0326"
    rin "\"Ah, for this type, it's easier to understand if you replace one letter in these formulas. For instance, if you replace this 'a+b' with 'A'...?\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0287"
    fumi "\"Umm, it goes like this, and this... Oh, I think I can expand it!\""

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0327"
    rin "\"Yep. Don't forget to put it back at the end.\""

    show fumi:
        "fumi 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0288"
    fumi "\"Right!\""

    show fumi 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama j"

    voice "HIN_0386"
    hina "\"Advance, {i}susumeru{/i}. Destination, {i}mokutekichi{/i}. Plural, {i}fukusuu no{/i}.\""

    "Hina was single-mindedly writing English vocab words and their meanings down in her notebook. She seemed like she was choosing the brute-force approach."

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0387"
    hina "\"Wealth, {i}tomi{/i}. Sentiment, {i}kanjou{/i}. Resolve, {i}toku{/i}...\""

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
    hina "\"Daaah!\""

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
    rin "\"Whoa, what the heck?!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0389"
    hina "\"Do you guys like skiing?\""

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0289"
    fumi "\"Th-That was rather sudden.\""

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0390"
    hina "\"Let's talk about winter break!\""

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0329"
    rin "\"Ah, the attempts to escape reality begin.\""

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0290"
    fumi "\"This seems like a good time for a break.\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01ca with bg_effect_05
    pause 0.5

    show fumi z3 2 lg pyjama b behind rin, hina at pos_l2_z3
    show rin z3 1 lg pyjama glasses a behind hina at pos_r2_z3
    show hina z3 1 lg pyjama a
    with Dissolve(0.25)

    voice "HIN_0391"
    hina "\"What are you gonna do for New Year's? I'm going home after Christmas.\""

    voice "FUM_0291"
    fumi "\"I think I'm going to go home around that time, too.\""

    "And Rin?"

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0330"
    rin "\"I'm staying here.\""

    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0392"
    hina "\"Huh? Really? You're not going home for break?\""

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0331"
    rin "\"It's not like anybody'll be there if I go.\""

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0292"
    fumi "\"What about your parents?\""

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0332"
    rin "\"They'll be in Europe for New Year's.\""

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0393"
    hina "\"What?! They're going overseas and leaving you here? That's kinda mean.\""

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin z3 2 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0333"
    rin "\"No, it's for work. There's an academic conference.\""

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0394"
    hina "\"Your dad's a university professor, right?\""

    show rin:
        ShakeYes

    voice "RIN_0334"
    rin "\"Yep. And my mom's his assistant. So I'll hold down the fort here.\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0293"
    fumi "\"Is anyone else staying here for the break?\""

    show rin z3 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0335"
    rin "\"I dunno. I imagine Sachiko will be here.\""

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0395"
    hina "\"What?! Isn't that kinda risky?\""

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama f with dict_dissolve_25

    voice "FUM_0294"
    fumi "\"I suppose I would be a bit worried about that.\""

    "...They really don't trust her."

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0336"
    rin "\"Right. I guess that's an option if I'm lonely.\""

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0396"
    hina "\"Nooo! Be sure to remember to lock the door!\""

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z3 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0337"
    rin "\"I-I'm joking.\""

    show rin z3 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0397"
    hina "\"I'm worried. Should I stay here, too?\""

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0338"
    rin "\"It's fine. You've got family waiting for you, right? Spend your New Year's with them.\""

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0398"
    hina "\"Mm~, well then, let's all go to a shrine together! And we can have a party, too!\""

    show fumi:
        "fumi z3 2 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0295"
    fumi "\"Oh, that's a good idea! I can bring some food from home!\""

    show fumi z3 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0339"
    rin "\"O-Okay.\""

    show fumi z3 2 lg pyjama h
    show hina z3 1 lg pyjama k
    with Dissolve(0.25)

    voice "HIN_0399"
    hina "\"You don't want to?\""

    show rin:
        "rin z3 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeUji

    voice "RIN_0340"
    rin "\"No... that's not it...\""

    show rin z3 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0400"
    hina "\"Y-You don't have plans with Sachiko, do you?!\""

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z3 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeNo

    voice "RIN_0341"
    rin "\"No, no, no. No way.\""

    show rin z3 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0296"
    fumi "\"I hope we're not being too pushy...\""

    show rin z3 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0342"
    rin "\"Of course not. I'm happy you're thinking of me. I'm kinda sorry to make you, in fact.\""

    show hina z3 1 lg pyjama e with dict_dissolve_25

    voice "HIN_0401"
    hina "\"It's not like that. I've wanted to go to a shrine and stuff with you two.\""

    show rin z3 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0343"
    rin "\"I've never even done that with my family before.\""

    show hina z3 1 lg pyjama b with dict_dissolve_25

    voice "HIN_0402"
    hina "\"Then you can think of us as your family.\""

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0344"
    rin "\"......\""

    show fumi z3 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0297"
    fumi "\"She's right. We've lived together for months now. You don't need to worry about being a bother.\""

    show rin z3 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0345"
    rin "\"Hina, Asou...\""

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0403"
    hina "\"Hm?\""


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
    rin "\"I love youuu!\""

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
    fumi "\"Aaah?!\""

    camera
    with None

    play sound se113da

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    $ side_image = "hina 1 side pyjama g"

    voice "HIN_0404"
    hina "\"Not this punchline again!\""

    camera
    with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
