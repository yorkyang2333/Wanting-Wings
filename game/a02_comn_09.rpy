label a02_comn_09:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play sound se521

    scene bg01cc_b with Dissolve(0.25)
    pause 0.75

    play music bgm01

    pause 0.5

    show hina:
        "hina 1 sm school_scarf l flat"
        alpha 0.0 xcenter 732
        easein 0.5 alpha 1.0 xcenter 632
    pause 0.5

    voice "HIN_0422"
    hina "\"Wow! The room's all decorated!\""

    show hina 1 sm school_scarf l:
        alpha 1.0 xcenter 632
    with None

    show rin behind hina, fumi:
        "rin 1 sm school_scarf a flat"
        alpha 0.0 xcenter 876
        easein 0.5 alpha 1.0 xcenter 776
    show fumi behind hina:
        "fumi 1 sm school_scarf d flat"
        alpha 0.0 xcenter 1040
        easein 0.5 alpha 1.0 xcenter 940
    pause 0.5

    voice "FUM_0313"
    fumi "\"Sorry, I didn't have time to do all that much.\""

    show rin 1 sm school_scarf a:
        alpha 1.0 xcenter 776
    show fumi 1 sm school_scarf d:
        alpha 1.0 xcenter 940
    with None

    show hina 1 sm school_scarf c with dict_dissolve_25

    voice "HIN_0423"
    hina "\"No, this is more than enough!\""

    "Fumi seemed relieved as Hina looked around at all the decorations in the room."

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "RIN_0364"
    rin "\"We got a birthday cake, too. Special-made by Asou's dad!\""

    show hina 1 sm school_scarf l with dict_dissolve_25

    voice "HIN_0424"
    hina "\"Your dad's a pro patissier, right?! When'd you get it?\""

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0314"
    fumi "\"We ordered it last week and Sachiko went and picked it up today.\""

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0425"
    hina "\"Huh. You had to get a lot ready, didn't you? And you had tests, too.\""

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "FUM_0315"
    fumi "\"It was no trouble. If you like it, I'm happy.\""

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "RIN_0365"
    rin "\"Umm~ Asou, about this cake...\""

    "Rin piped up when she opened the cake box."

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0316"
    fumi "\"Huh? It didn't fall apart, did it?\""

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "RIN_0366"
    rin "\"No, it's fine, just, this decoration on it...\""

    voice "FUM_0317"
    fumi "\"Decoration?\""

    "She gave a nervous glance at the cake when it emerged from the box."

    show fumi:
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0318"
    fumi "\"Aah! My dad messed it up!\""

    show fumi 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf k with dict_dissolve_25

    voice "HIN_0426"
    hina "\"What? What is it? Can I see?\""

    "The three all peered at the cake."

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0427"
    hina "\"This little guy in red... This is a Christmas cake, right?\""

    voice "FUM_0319"
    fumi "\"I-I'm so sorry! My dad must have misunderstood!\""

    play sound se585

    show fumi 1 sm school_scarf e with dict_dissolve_25
    show rin:
        "rin 1 sm school_scarf d" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0367"
    rin "\"Merry Christmas!\""

    show rin 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "HIN_0428"
    hina "\"That was loud! And where did you pull those party poppers from, anyway?!\""

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "RIN_0368"
    rin "\"Oh, there was some other stuff in the bag with the cake. If we had party hats now, it'd be perfect.\""

    show fumi:
        "fumi 1 sm school_scarf h" with Dissolve(0.25)
        ShakeUji

    voice "FUM_0320"
    fumi "\"Dad... you went all in on the wrong theme...\""

    show fumi 1 sm school_scarf h:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0429"
    hina "\"Aha, hahahaha... it's a little early for this, huh...\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01cc_b with bg_effect_05
    pause 0.7

    scene bg01cc with Dissolve(0.25)
    pause 1.75

    show rin z3 1 lg pyjama c at pos_r2_z3
    show fumi z3 1 lg pyjama a at pos_l2_z3
    show hina z3 1 lg pyjama m
    with Dissolve(0.25)

    show hina:
        ShakeTameiki

    voice "HIN_0430"
    hina "\"Fhooo!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama c with dict_dissolve_25

    $ voice2("rin","RIN_0369","hina","FUM_0321")
    rin_fumi "\"Happy birthday!\""

    show hina z3 1 lg pyjama c with Dissolve(0.25)

    voice "HIN_0431"
    hina "\"Thanks! At least I got to do this, since it's supposed to be a birthday cake.\""

    show fumi z3 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0322"
    fumi "\"Aha. It's a good thing I bought the candles separate.\""

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0370"
    rin "\"Now, it's time for the long-awaited present exchange!\""

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0432"
    hina "\"You don't exchange birthday presents!\""

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0323"
    fumi "\"Well... I hope you like this.\""

    "Fumi handed over a wrapped box."

    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0371"
    rin "\"Ho ho ho! A present from Santa! Now, where's your stocking?\""

    "She's really running with the Christmas thing."

    show hina z3 1 lg pyjama b with dict_dissolve_25

    voice "HIN_0433"
    hina "\"Thank you! Can I open it?\""

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0324"
    fumi "\"Of course.\""

    play sound se558a

    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0434"
    hina "\"What could it be, what could it be... Wow! Is this an MP3 player?!\""

    show fumi z3 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0325"
    fumi "\"Yes. You said your CD player didn't work that well anymore, so...\""

    show hina:
        "hina z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0435"
    hina "\"Wow, you remembered? I'm so happy! Thank you, Asou!\""

    show hina z3 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes2

    voice "RIN_0372"
    rin "\"Mhm, mhm. How wonderful.\""

    show rin z3 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0436"
    hina "\"...And Rin?\""

    show rin z3 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0373"
    rin "\"What's with the hands?\""

    "Rin made a show of her empty-handedness."

    show hina:
        "hina z3 1 lg pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0437"
    hina "\"O-Oh. Well, it's not like I'd force you to get me something, so that's fine. But it's kinda...\""

    show hina z3 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0326"
    fumi "\"Oh, no, that's not it! The gift is from both of us. The MP3 player is from me and the songs on it are from Ogata.\""

    show fumi z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0438"
    hina "\"Oh, really?\""

    show rin z3 2 lg pyjama e with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "RIN_0374"
    rin "\"Yeah. I got a few compilation albums of western music. It should all be famous songs like the one we were listening to the other day.\""

    "Rin handed over a small paper bag with several CDs inside."

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama a
    show hina z3 1 lg pyjama c
    with dict_dissolve_25

    voice "HIN_0439"
    hina "\"Ooh!\""

    "Hina took the CDs out and looked them over."

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0440"
    hina "\"Hm~ I don't think I know any of these bands.\""

    show rin z3 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0375"
    rin "\"Well, try listening. The music's already on the MP3 player, so you can listen to it right away.\""

    show hina:
        "hina z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes2

    voice "HIN_0441"
    hina "\"Okay! I will!\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01cc with bg_effect_05
    pause 0.5

    show rin z3 1 lg pyjama a at pos_r2_z3
    show fumi z3 2 lg pyjama b at pos_l2_z3
    show hina z3 1 lg pyjama headphones c
    with Dissolve(0.25)

    voice "HIN_0442"
    hina "\"Oh, I've heard this, too! I've heard all of these!\""

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0376"
    rin "\"Thought so.\""

    voice "HIN_0443"
    hina "\"This is awesome! Thank you so much, Rin!\""

    show rin z3 2 lg pyjama e with dict_dissolve_25

    voice "RIN_0377"
    rin "\"O-Oh yeah? Well, good!\""

    show fumi z3 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0327"
    fumi "\"...Mhm, mhm♪\""

    "Hina and Rin looked happy, and Fumi, in turn, looked pleased to see it."

    show rin z3 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0378"
    rin "\"Oh, right. When you want to put more songs on it, you can use Sachiko's computer.\""

    show hina z3 1 lg pyjama headphones d with Dissolve(0.25)
    show hina:
        ShakeNo

    voice "HIN_0444"
    hina "\"What~?! I don't want to... you never know when you're gonna click on something dirty on that thing.\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0379"
    rin "\"Well, you need a computer to put the music on the player, and we don't have one in here...\""

    show hina z3 1 lg pyjama headphones c with dict_dissolve_25

    voice "HIN_0445"
    hina "\"I know, you can buy me a computer for Christmas!\""

    show rin z3 1 lg pyjama i with dict_dissolve_25

    voice "RIN_0380"
    rin "\"That's not happening.\""

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0328"
    fumi "\"...Unfortunately.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a02_cou3_03
    elif rin_hina_score > hina_fumi_score:
        jump a02_cou2_02
    else:
        $ hina_fumi_score = 999
        jump a02_cou1_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
