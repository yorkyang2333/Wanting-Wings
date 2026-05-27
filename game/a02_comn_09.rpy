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
    hina "\"Wow! The room's all decorated!\"" id a02_comn_09_5ba164b4

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
    fumi "\"Sorry, I didn't have time to do all that much.\"" id a02_comn_09_5eeeefe1

    show rin 1 sm school_scarf a:
        alpha 1.0 xcenter 776
    show fumi 1 sm school_scarf d:
        alpha 1.0 xcenter 940
    with None

    show hina 1 sm school_scarf c with dict_dissolve_25

    voice "HIN_0423"
    hina "\"No, this is more than enough!\"" id a02_comn_09_28b35148

    "Fumi seemed relieved as Hina looked around at all the decorations in the room."

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "RIN_0364"
    rin "\"We got a birthday cake, too. Special-made by Asou's dad!\"" id a02_comn_09_a26d5426

    show hina 1 sm school_scarf l with dict_dissolve_25

    voice "HIN_0424"
    hina "\"Your dad's a pro patissier, right?! When'd you get it?\"" id a02_comn_09_e790d5ca

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0314"
    fumi "\"We ordered it last week and Sachiko went and picked it up today.\"" id a02_comn_09_aaab948d

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0425"
    hina "\"Huh. You had to get a lot ready, didn't you? And you had tests, too.\"" id a02_comn_09_823375cc

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "FUM_0315"
    fumi "\"It was no trouble. If you like it, I'm happy.\"" id a02_comn_09_97ce6e99

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "RIN_0365"
    rin "\"Umm~ Asou, about this cake...\"" id a02_comn_09_a90d7814

    "Rin piped up when she opened the cake box."

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0316"
    fumi "\"Huh? It didn't fall apart, did it?\"" id a02_comn_09_fdb5a2fe

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "RIN_0366"
    rin "\"No, it's fine, just, this decoration on it...\"" id a02_comn_09_41e008b9

    voice "FUM_0317"
    fumi "\"Decoration?\"" id a02_comn_09_d0ede547

    "She gave a nervous glance at the cake when it emerged from the box."

    show fumi:
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0318"
    fumi "\"Aah! My dad messed it up!\"" id a02_comn_09_973691e8

    show fumi 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf k with dict_dissolve_25

    voice "HIN_0426"
    hina "\"What? What is it? Can I see?\"" id a02_comn_09_b6e26dbb

    "The three all peered at the cake."

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0427"
    hina "\"This little guy in red... This is a Christmas cake, right?\"" id a02_comn_09_cdb81ae2

    voice "FUM_0319"
    fumi "\"I-I'm so sorry! My dad must have misunderstood!\"" id a02_comn_09_f068bacf

    play sound se585

    show fumi 1 sm school_scarf e with dict_dissolve_25
    show rin:
        "rin 1 sm school_scarf d" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0367"
    rin "\"Merry Christmas!\"" id a02_comn_09_5fa8a328

    show rin 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "HIN_0428"
    hina "\"That was loud! And where did you pull those party poppers from, anyway?!\"" id a02_comn_09_95e7ec1b

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "RIN_0368"
    rin "\"Oh, there was some other stuff in the bag with the cake. If we had party hats now, it'd be perfect.\"" id a02_comn_09_d32c30a3

    show fumi:
        "fumi 1 sm school_scarf h" with Dissolve(0.25)
        ShakeUji

    voice "FUM_0320"
    fumi "\"Dad... you went all in on the wrong theme...\"" id a02_comn_09_dbb8a1c1

    show fumi 1 sm school_scarf h:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0429"
    hina "\"Aha, hahahaha... it's a little early for this, huh...\"" id a02_comn_09_1e155d58

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
    hina "\"Fhooo!\"" id a02_comn_09_8655fd40

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama c with dict_dissolve_25

    $ voice2("rin","RIN_0369","hina","FUM_0321")
    rin_fumi "\"Happy birthday!\""

    show hina z3 1 lg pyjama c with Dissolve(0.25)

    voice "HIN_0431"
    hina "\"Thanks! At least I got to do this, since it's supposed to be a birthday cake.\"" id a02_comn_09_dbd92785

    show fumi z3 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0322"
    fumi "\"Aha. It's a good thing I bought the candles separate.\"" id a02_comn_09_3e8823bc

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0370"
    rin "\"Now, it's time for the long-awaited present exchange!\"" id a02_comn_09_c303d231

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0432"
    hina "\"You don't exchange birthday presents!\"" id a02_comn_09_baf448da

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0323"
    fumi "\"Well... I hope you like this.\"" id a02_comn_09_4239d2f9

    "Fumi handed over a wrapped box."

    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0371"
    rin "\"Ho ho ho! A present from Santa! Now, where's your stocking?\"" id a02_comn_09_086e3986

    "She's really running with the Christmas thing."

    show hina z3 1 lg pyjama b with dict_dissolve_25

    voice "HIN_0433"
    hina "\"Thank you! Can I open it?\"" id a02_comn_09_9498a088

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0324"
    fumi "\"Of course.\"" id a02_comn_09_6a3ad29c

    play sound se558a

    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0434"
    hina "\"What could it be, what could it be... Wow! Is this an MP3 player?!\"" id a02_comn_09_5ff75580

    show fumi z3 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0325"
    fumi "\"Yes. You said your CD player didn't work that well anymore, so...\"" id a02_comn_09_dbd3742f

    show hina:
        "hina z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0435"
    hina "\"Wow, you remembered? I'm so happy! Thank you, Asou!\"" id a02_comn_09_ab109385

    show hina z3 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes2

    voice "RIN_0372"
    rin "\"Mhm, mhm. How wonderful.\"" id a02_comn_09_b7dc2c2d

    show rin z3 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0436"
    hina "\"...And Rin?\"" id a02_comn_09_a32508b8

    show rin z3 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0373"
    rin "\"What's with the hands?\"" id a02_comn_09_d688dcf6

    "Rin made a show of her empty-handedness."

    show hina:
        "hina z3 1 lg pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0437"
    hina "\"O-Oh. Well, it's not like I'd force you to get me something, so that's fine. But it's kinda...\"" id a02_comn_09_5ce31ee4

    show hina z3 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0326"
    fumi "\"Oh, no, that's not it! The gift is from both of us. The MP3 player is from me and the songs on it are from Ogata.\"" id a02_comn_09_6eb09a24

    show fumi z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0438"
    hina "\"Oh, really?\"" id a02_comn_09_7e1af1d6

    show rin z3 2 lg pyjama e with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "RIN_0374"
    rin "\"Yeah. I got a few compilation albums of western music. It should all be famous songs like the one we were listening to the other day.\"" id a02_comn_09_c539ac9e

    "Rin handed over a small paper bag with several CDs inside."

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg pyjama a
    show hina z3 1 lg pyjama c
    with dict_dissolve_25

    voice "HIN_0439"
    hina "\"Ooh!\"" id a02_comn_09_e677c85d

    "Hina took the CDs out and looked them over."

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0440"
    hina "\"Hm~ I don't think I know any of these bands.\"" id a02_comn_09_d8052dbe

    show rin z3 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0375"
    rin "\"Well, try listening. The music's already on the MP3 player, so you can listen to it right away.\"" id a02_comn_09_9232ce29

    show hina:
        "hina z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes2

    voice "HIN_0441"
    hina "\"Okay! I will!\"" id a02_comn_09_e3dae3a7

    scene black with bg_effect_05
    pause 0.5

    scene bg01cc with bg_effect_05
    pause 0.5

    show rin z3 1 lg pyjama a at pos_r2_z3
    show fumi z3 2 lg pyjama b at pos_l2_z3
    show hina z3 1 lg pyjama headphones c
    with Dissolve(0.25)

    voice "HIN_0442"
    hina "\"Oh, I've heard this, too! I've heard all of these!\"" id a02_comn_09_2906e891

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0376"
    rin "\"Thought so.\"" id a02_comn_09_ac8f3c86

    voice "HIN_0443"
    hina "\"This is awesome! Thank you so much, Rin!\"" id a02_comn_09_4700de82

    show rin z3 2 lg pyjama e with dict_dissolve_25

    voice "RIN_0377"
    rin "\"O-Oh yeah? Well, good!\"" id a02_comn_09_a33ff3ac

    show fumi z3 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0327"
    fumi "\"...Mhm, mhm♪\"" id a02_comn_09_39492694

    "Hina and Rin looked happy, and Fumi, in turn, looked pleased to see it."

    show rin z3 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0378"
    rin "\"Oh, right. When you want to put more songs on it, you can use Sachiko's computer.\"" id a02_comn_09_a49e7089

    show hina z3 1 lg pyjama headphones d with Dissolve(0.25)
    show hina:
        ShakeNo

    voice "HIN_0444"
    hina "\"What~?! I don't want to... you never know when you're gonna click on something dirty on that thing.\"" id a02_comn_09_e78b803d

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0379"
    rin "\"Well, you need a computer to put the music on the player, and we don't have one in here...\"" id a02_comn_09_347272aa

    show hina z3 1 lg pyjama headphones c with dict_dissolve_25

    voice "HIN_0445"
    hina "\"I know, you can buy me a computer for Christmas!\"" id a02_comn_09_50d364d1

    show rin z3 1 lg pyjama i with dict_dissolve_25

    voice "RIN_0380"
    rin "\"That's not happening.\"" id a02_comn_09_4a7d7ae2

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0328"
    fumi "\"...Unfortunately.\"" id a02_comn_09_11c5efc2

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
