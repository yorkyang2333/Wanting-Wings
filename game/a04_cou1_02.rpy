label a04_cou1_02:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    scene bg02ca with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show hina 1 lg pyjama k at pos_r
    show fumi 1 lg pyjama a at pos_l
    with Dissolve(0.25)

    show hina:
        ShakeTameiki

    voice "HIN_1011"
    hina "\"Put the sugar in the pot...\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0844"
    fumi "\"Oh, don't stir it too hard. But it can burn easily, just go little by little.\""

    "Hina was making caramel sauce for the pudding."

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1012"
    hina "\"I'm excited. I didn't get to eat any Christmas pudding.\""

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0845"
    fumi "\"Oh, that Sachiko got?\""

    show hina 1 lg pyjama h with dict_dissolve_25

    voice "HIN_1013"
    hina "\"Yeah, I was kinda jealous of that.\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0846"
    fumi "\"Were you? But the pudding we're making is custard pudding.\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_1014"
    hina "\"Huh? Yeah? Was the pudding Sachiko got not really pudding?\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0847"
    fumi "\"Christmas pudding is made with dried fruits preserved in alcohol and baked with flour and sugar and eggs. It's more like a cake.\""

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_1015"
    hina "\"Huh... I guess I had the wrong idea.\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0848"
    fumi "\"You don't see it too often in Japan. Did you want that instead of this?\""

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1016"
    hina "\"No... I really just wanted to make something with you, Fumi.\""

    "Hina replied with an innocent smile."

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0849"
    fumi "\"Yes! Custard pudding is tasty, too.\""

    show hina:
        ShakeYes

    voice "HIN_1017"
    hina "\"Yeah!\""

    scene black with bg_effect_05
    pause 0.5

    scene bg02ca with bg_effect_05
    pause 0.5

    show hina 1 lg pyjama k at pos_r
    show fumi 2 lg pyjama b at pos_l
    with Dissolve(0.25)

    voice "FUM_0850"
    fumi "\"Since the sauce is done, let's do the pudding now. Mix the eggs, sugar, and milk really well.\""

    voice "HIN_1018"
    hina "\"Like this?\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0851"
    fumi "\"Yes, that's good. Now put in the vanilla extract there.\""

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1019"
    hina "\"Hwah, this smells so good.\""

    "A goofy smile lit up Hina's face as soon as she opened the bottle of vanilla."

    voice "HIN_1020"
    hina "\"I bet it's really sweet.\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0852"
    fumi "\"Oh, don't lick—\""

    "She was just a moment too late to stop her. Hina put a drop of vanilla extract on her finger and licked it."

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1021"
    hina "\"Gweh, that's bitter!!\""

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0853"
    fumi "\"I did the same thing when I was little.\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_1022"
    hina "\"How is it so bitter when it smells so sweet? It's like perfume.\""

    "It sounds like she's licked that, too."

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0854"
    fumi "\"I bet a vanilla perfume would suit you, Hina.\""

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1023"
    hina "\"I'll put some on, then.\""

    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0855"
    fumi "\"Ah...\""

    "She was too late to stop this, too. Hina put a dab of vanilla on the nape of her neck."

    "The sweet scent of vanilla wafted between them."

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_1024"
    hina "\"Ahh... It's like being in a cake shop.\""

    show fumi 2 lg pyjama e with dict_dissolve_25

    voice "FUM_0856"
    fumi "\"It's more like you're the cake, Hina. I bet you'd taste good.\""

    play sound se118a

    show fumi:
        "fumi 2 lg pyjama c" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 472
    pause 0.25

    voice "FUM_0857"
    fumi "\"...Nom.\""

    show fumi 2 lg pyjama c:
        xcenter 472
    with None

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeSide
        ShakeSide

    voice "HIN_1025"
    hina "\"Hyaaah?!\""

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None

    stop music fadeout 1.0

    "Hina crumpled to the floor when Fumi nibbled on her neck."

    play music bgm04

    show fumi 2 lg pyjama e with dict_dissolve_25

    voice "FUM_0858"
    fumi "\"You're so ticklish. Mmh...\""

    "This time, Fumi ran her tongue over Hina's skin."

    show hina:
        "hina 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "HIN_1026"
    hina "\"Hwah!\""

    show hina 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None

    voice "FUM_0859"
    fumi "\"Mmh... haah...\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1027"
    hina "\"Ah... Fumi... that feels... kind of weird...\""

    voice "FUM_0860"
    fumi "\"Chp... nnh... do you... not like it...?\""

    show hina 2 lg pyjama i with dict_dissolve_25

    voice "HIN_1028"
    hina "\"It's not that... ah... it just feels kind of... itchy... inside me...\""

    voice "FUM_0861"
    fumi "\"Nnh... ah... mmh...\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1029"
    hina "\"Fumi... can I... kiss... you...?\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0862"
    fumi "\"You want to kiss me?\""

    show hina 1 lg pyjama m
    show fumi 2 lg pyjama j
    with dict_dissolve_25

    voice "HIN_1030"
    hina "\"Mm...\""

    "This time, Hina kissed Fumi on the lips."

    "At first, it was just a brushing of their lips, but it gradually became more and more heated."

    voice "HIN_1031"
    hina "\"Ah... Your lips... are so soft...\""

    voice "FUM_0863"
    fumi "\"So are yours...\""

    "Fumi's lips parted, and Hina's tongue slipped inside."

    voice "FUM_0864"
    fumi "\"Nnh...\""

    voice "HIN_1032"
    hina "\"Your tongue is... sweet... nnh... mmh...\""

    voice "FUM_0865"
    fumi "\"Hah... ahn... Well, I just... tasted the caramel sauce...\""

    "There was a quiet sound of their tongues entwining."

    play sound se135a

    stop music fadeout 1.0

    "And, as if to disrupt that, footsteps coming down the hall."

    play sound2 se118c

    show fumi:
        "fumi 2 lg pyjama g" with Dissolve(0.25)
        xcenter 472
        easein 0.25 xcenter 252
    show hina 1 lg pyjama d with dict_dissolve_25

    "The two quickly pulled apart."

    show fumi 2 lg pyjama g:
        xcenter 252
    with None

    voice "FUM_0866"
    fumi "\"Ah, I wonder if that's Ogata—\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_1033"
    hina "\"Yeah...\""

    play sound se521

    play music bgm01

    $ side_image = "rin 1 side pyjama a"

    voice "RIN_0952"
    rin "\"I'm back... Whoa, sweet!\""

    "Rin gagged on the vanilla smell."

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0867"
    fumi "\"Umm, we were making pudding, and...\""

    $ side_image = "rin 1 side pyjama h"

    voice "RIN_0953"
    rin "\"I heard, but this smell... Hina? Is it coming from you?\""

    show hina 1 lg pyjama d with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_1034"
    hina "\"Umm, well, I...\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0868"
    fumi "\"She spilled some vanilla extract.\""

    show hina:
        "hina 1 lg pyjama g" with Dissolve(0.25)
        ShakeYes

    voice "HIN_1035"
    hina "\"Y-Yeah. Ahaha, I'm so clumsy~\""

    show hina 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama g"

    voice "RIN_0954"
    rin "\"Geez, what are you doing? You should go shower later.\""

    voice "HIN_1036"
    hina "\"Aha, ahahahaha...\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0869"
    fumi "\"She's right~\""

    $ side_image = "rin 1 side pyjama h"

    voice "RIN_0955"
    rin "\"......\""

    "Rin's gaze lingered on Hina's neck, where there was a faint bruise."

    $ side_image = "rin 1 side pyjama g"

    voice "RIN_0956"
    rin "\"...Seriously, what were you doing?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
