label a02_comn_01:

    pause 0.5

    scene expression "gui/kimihane/mainmenu_ground1.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter02 with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm pyjama k
    show fumi 1 sm pyjama a at pos_r2
    show rin 1 sm pyjama glasses a at pos_l2
    with Dissolve(0.25)

    voice "HIN_0293"
    hina "\"Hmm? Huhhh?\""

    "Hina cocked her head, looking up at the calendar on the wall."

    "The action was particularly exaggerated."

    show hina:
        "hina 1 sm pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0294"
    hina "\"What was on December 5th again? I get the feeling it was something suuuper important for me and everyone else here~\""

    show hina 1 sm pyjama h:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "RIN_0258"
    rin "\"Last day of exams.\""

    "Rin answered, not taking her eyes off her book."

    show hina:
        "hina 1 sm pyjama i" with Dissolve(0.25)
        ShakeNo

    voice "HIN_0295"
    hina "\"Mmmmmh!\""

    show hina 1 sm pyjama i:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses e with dict_dissolve_25

    voice "RIN_0259"
    rin "\"What kind of retort was that?\""

    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0296"
    hina "\"It's a very important day!\""

    show hina 1 sm pyjama f:
        xoffset 0 yoffset 0
    with None

    "Apparently, exams are not important."

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0229"
    fumi "\"It's your birthday, isn't it, Natsume?\""

    show hina:
        "hina 1 sm pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0297"
    hina "\"That's right! That's what I wanted to hear! Good job, Asou!\""

    show hina 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0230"
    fumi "\"This seems like a good time to mention—\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0260"
    rin "\"December 5th is Thailand's King Phumiphon's birthday, too.\""

    show hina 1 sm pyjama f with dict_dissolve_25

    voice "HIN_0298"
    hina "\"What?! Who the heck is that?!\""

    show rin 1 sm pyjama glasses e with dict_dissolve_25

    voice "RIN_0261"
    rin "\"Oh, sorry. Technically that should be Bhumibol Adulyadej. Incidentally, the name means 'Strength of the Land, Incomparable Power.'\""

    show hina:
        "hina 1 sm pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0299"
    hina "\"The details don't help, I still don't know who that is! And what were you about to say, Asou—\""

    show hina 1 sm pyjama h:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0231"
    fumi "\"Ph-Phumiphon... Eheh, that sounds cute.\""

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0300"
    hina "\"Phumiphon hit her funny bone!\""

    show hina 1 sm pyjama l:
        xoffset 0 yoffset 0
    with None
    show fumi:
        ShakeSide

    voice "FUM_0232"
    fumi "\"Eheh, eheheh, u-umm, I was thinking... Ph-Phumipho—\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0301"
    hina "\"Take your time.\""

    show fumi:
        "fumi 1 sm pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0233"
    fumi "\"I-I'm... sorry... ahahaha!\""

    show fumi 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0262"
    rin "\"Hey, Hinaphon?\""

    show hina 1 sm pyjama f with dict_dissolve_25

    voice "HIN_0302"
    hina "\"Who's Hinaphon?!\""

    show fumi:
        "fumi 1 sm pyjama c" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0234"
    fumi "\"H-Hina...phon! Phahahaha!\""

    show fumi 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None

    "Fuel to the fire."

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0303"
    hina "\"Don't make it worse!\""

    show hina 1 sm pyjama l:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses c with dict_dissolve_25

    voice "RIN_0263"
    rin "\"Gotcha-phon.\""

    show fumi:
        ShakeSide
        ShakeSide

    voice "FUM_0235"
    fumi "\"Aha, ahahahaha! I-I can't breathe! My stomach!\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0304"
    hina "\"Rin!\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01ca with bg_effect_05
    pause 0.5

    show fumi 1 sm pyjama d at pos_r2
    show hina 1 sm pyjama j
    show rin 1 sm pyjama glasses a at pos_l2
    with Dissolve(0.25)

    show fumi:
        ShakeTameiki

    voice "FUM_0236"
    fumi "\"Whew... I've got it under control.\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0264"
    rin "\"You okay? Fumiph—gh!\""

    play sound se103b
    show rin:
        "rin 1 sm pyjama glasses j" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False
    pause 0.5

    show rin 1 sm pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama f
    with Dissolve(0.25)

    voice "HIN_0305"
    hina "\"Gnnh!\""

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0237"
    fumi "\"I was thinking, after exams are over, should we have a birthday party in our room?\""

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0306"
    hina "\"A birthday party? You mean it?!\""

    show hina 1 sm pyjama l:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0238"
    fumi "\"Yes. I was thinking about making it a surprise, but with exams, I didn't think we'd be able to prepare very much.\""

    show hina:
        "hina 1 sm pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0307"
    hina "\"That's fine—thanks! That makes me really happy!\""

    show hina 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 1 sm pyjama b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0239"
    fumi "\"I'm glad. I thought it would be nice if the three of us could celebrate together. What do you think, Ogata?\""

    show fumi 1 sm pyjama b:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses c with dict_dissolve_25

    voice "RIN_0265"
    rin "\"If you're making food, I'm for it.\""

    show hina 1 sm pyjama j with dict_dissolve_25

    voice "HIN_0308"
    hina "\"Do you understand what the party's for?\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0266"
    rin "\"The end of exams?\""

    voice "HIN_0309"
    hina "\"Were you listening to anything we said?\""

    show rin 1 sm pyjama glasses c with dict_dissolve_25

    voice "RIN_0267"
    rin "\"It's a birthday party.\""

    show hina 1 sm pyjama j with dict_dissolve_25

    voice "HIN_0310"
    hina "\"...For who?\""

    show rin 1 sm pyjama glasses d with dict_dissolve_25

    voice "RIN_0268"
    rin "\"Phumiph—\""

    play sound se103b
    show rin:
        "rin 1 sm pyjama glasses j" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False
    pause 0.5

    show rin 1 sm pyjama glasses i:
        xoffset 0 yoffset 0
    with Dissolve(0.25)

    voice "RIN_0269"
    rin "\"For Hinaphon, of course.\""

    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0311"
    hina "\"Stop calling me that!\""

    show hina 1 sm pyjama f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0240"
    fumi "\"Ahaha.\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0270"
    rin "\"It's close to Christmas, so should we celebrate that, too?\""

    show hina 1 sm pyjama g with dict_dissolve_25

    voice "HIN_0312"
    hina "\"No! Who am I supposed to be, Christ?!\""

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "RIN_0271"
    rin "\"That's a pretty scary thing to say.\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0241"
    fumi "\"We'll celebrate Christmas on Christmas.\""

    show rin:
        "rin 1 sm pyjama glasses b" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0272"
    rin "\"Yeesh. The expenses pile up when there's so many special occasions at the same time.\""

    show rin 1 sm pyjama glasses b:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama j with dict_dissolve_25

    voice "HIN_0313"
    hina "\"Grr. We won't celebrate your birthday, Rin!\""

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0242"
    fumi "\"Eheh. She's just joking. Ogata was the one who suggested throwing a party.\""

    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0314"
    hina "\"Oho.\""

    show rin:
        "rin 1 sm pyjama glasses i" with Dissolve(0.25)
        ShakeUji

    voice "RIN_0273"
    rin "\"Umm, I'm pretty sure I just said that some people do things like that here, didn't I?\""

    show rin 1 sm pyjama glasses i:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0243"
    fumi "\"Heheh, that's right.\""

    show hina 1 sm pyjama g with dict_dissolve_25

    voice "HIN_0315"
    hina "\"Why are you like this?\""

    show rin 1 sm pyjama glasses g with dict_dissolve_25

    voice "RIN_0274"
    rin "\"Shut u-phon.\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0244"
    fumi "\"Your birthday is March 9th, isn't it, Ogata?\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0275"
    rin "\"Sounds about right.\""

    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0245"
    fumi "\"'Sounds'...? We'll celebrate your birthday too, okay, Ogata?\""

    show hina:
        "hina 1 sm pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0316"
    hina "\"Wow~ So you're younger than me, Rin.\""

    show hina 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "RIN_0276"
    rin "\"Yeah, by three months.\""

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0317"
    hina "\"I think you should start showing me some respect.\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0277"
    rin "\"I think not.\""

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0318"
    hina "\"When's your birthday, Asou? We didn't miss it, did we?\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0246"
    fumi "\"Don't worry. It's April 4th, so it was before we moved in here.\""

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0319"
    hina "\"We'll have to have a party for you next year, then.\""

    show fumi:
        "fumi 1 sm pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0247"
    fumi "\"I'm looking forward to it♪\""

    show fumi 1 sm pyjama c:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama g with dict_dissolve_25

    voice "HIN_0320"
    hina "\"So, the Hina Natsume birthday celebration will be held on December 5th... and, set!\""

    "Hina stretched up and circled the date on the calendar in marker."

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0248"
    fumi "\"Is there anything you want to eat besides cake?\""

    show hina 1 sm pyjama c with dict_dissolve_25

    voice "HIN_0321"
    hina "\"Hmm, what do I want to eat...\""

    show rin 1 sm pyjama glasses d with dict_dissolve_25

    voice "RIN_0278"
    rin "\"Turkey!\""

    show hina:
        "hina 1 sm pyjama j" with Dissolve(0.25)
        ShakeSide
        ShakeSide

    voice "HIN_0322"
    hina "\"Urrrgh!\""

    show hina 1 sm pyjama j:
        xoffset 0 yoffset 0
    with None

    "Another grumbling retort."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
