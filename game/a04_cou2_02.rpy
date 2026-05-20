label a04_cou2_02:

    scene bg07ca with Dissolve(0.5)
    pause 1.5

    play music bgm05

    play sound se001b

    $ side_image = "rin 1 side pyjama e"

    voice "RIN_1035"
    rin "\"Oh...\""

    "Rin went up to the roof and found..."

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "SYO_0152"
    sachiko "\"Hey, Rin, what's up?\""

    "...Sachiko, smoking."

    show rin:
        "rin 1 sm pyjama a flat"
        alpha 0.0 xcenter 152
        easein 0.5 alpha 1.0 xcenter 252

    show sachiko:
        "sachiko 1 sm outfit cigarette i" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 772

    voice "RIN_1036"
    rin "\"Just thought I might look at the stars.\""

    show rin 1 sm pyjama a:
        alpha 1.0 xcenter 252
    with None
    show sachiko:
        "sachiko 1 sm outfit cigarette b" with Dissolve(0.25)
        xcenter 772

    voice "SYO_0153"
    sachiko "\"Something on your mind? Should I get out of your hair?\""

    show sachiko 1 sm outfit cigarette b:
        xcenter 772
    with None

    show rin 1 sm pyjama c with dict_dissolve_25

    voice "RIN_1037"
    rin "\"No, you're fine.\""

    play sound se_fence

    "Rin leaned against the fence next to Sachiko."

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "SYO_0154"
    sachiko "\"So you're goin' out with Hinacchi now?\""

    show rin 1 sm pyjama g with dict_dissolve_25

    voice "RIN_1038"
    rin "\"...Those ears of yours scare me.\""

    "Rin paled for a moment."

    show sachiko 1 sm outfit cigarette g with dict_dissolve_25

    voice "SYO_0155"
    sachiko "\"Hinacchi sure is cute, ain't she?\""

    show rin 1 sm pyjama h with dict_dissolve_25

    voice "RIN_1039"
    rin "\"She is. She's little and honest and always sparkling. She's pure, passionate, and frankly too good for me.\""

    show sachiko 1 sm outfit cigarette c with dict_dissolve_25

    voice "SYO_0156"
    sachiko "\"Why the long face, then?\""

    show rin 1 sm pyjama i with dict_dissolve_25

    voice "RIN_1040"
    rin "\"Hmm~\""

    show rin 1 lg pyjama i with dict_dissolve_25

    show sachiko 1 lg outfit cigarette c with dict_dissolve_25

    play sound se116a

    "She reached for the cigarette in Sachiko's hand."

    show sachiko:
        "sachiko 1 lg outfit cigarette i" with Dissolve(0.25)
        ShakeTameiki

    voice "SYO_0157"
    sachiko "\"I don't think so.\""

    show sachiko 1 lg outfit cigarette i:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama a with dict_dissolve_25

    voice "RIN_1041"
    rin "\"Stingy.\""

    show sachiko 1 lg outfit cigarette c with dict_dissolve_25

    voice "SYO_0158"
    sachiko "\"It'll stunt your growth!\""

    show rin 2 lg pyjama c with dict_dissolve_25

    voice "RIN_1042"
    rin "\"I think I've grown enough.\""

    show sachiko 1 lg outfit cigarette i with dict_dissolve_25

    voice "SYO_0159"
    sachiko "\"Hinacchi'll be pissed at you if you go back smelling like cigarettes.\""

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_1043"
    rin "\"Oh, well, that'd be bad.\""

    show sachiko 1 lg outfit cigarette d with dict_dissolve_25

    voice "SYO_0160"
    sachiko "\"You've never even smoked before.\""

    show rin 1 lg pyjama h with dict_dissolve_25

    voice "RIN_1044"
    rin "\"I thought I'd feel a little more grown up if I did.\""

    show sachiko 1 lg outfit cigarette b with dict_dissolve_25

    voice "SYO_0161"
    sachiko "\"Growing up just means more problems.\""

    show rin 2 lg pyjama b with dict_dissolve_25

    voice "RIN_1045"
    rin "\"...Hmm.\""

    "Rin hesitated for a beat, and then finally started:"

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_1046"
    rin "\"I'm not used to being liked. I don't know what to do.\""

    show sachiko 1 lg outfit cigarette h with dict_dissolve_25

    voice "SYO_0162"
    sachiko "\"Huh?\""

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1047"
    rin "\"I'm happy for Hina's feelings, but I don't have the confidence that I can accept them.\""

    show sachiko 1 lg outfit cigarette c with dict_dissolve_25

    voice "SYO_0163"
    sachiko "\"That's a pretty cushy problem to have.\""

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_1048"
    rin "\"I know, but it's the first time anyone's had so much affection for me.\""

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_1049"
    rin "\"It just feels like Hina thinks too highly of me...\""

    show sachiko 1 lg outfit cigarette i with dict_dissolve_25

    voice "SYO_0164"
    sachiko "\"Too highly, eh...\""

    play sound se001b

    $ side_image = "hina 1 side pyjama l"

    voice "HIN_1256"
    hina "\"Ah! There you are!\""

    "The door flew open to reveal Hina."

    show sachiko 1 lg outfit cigarette a with dict_dissolve_25

    voice "SYO_0165"
    sachiko "\"Speak of the devil.\""

    hide rin
    hide sachiko
    with Dissolve(0.05)
    pause 0.2

    show sachiko 1 sm outfit cigarette a at pos_r
    show rin 1 sm pyjama i
    show hina:
        "hina 1 sm pyjama h flat"
        alpha 0.0 xcenter 202
        easein 0.5 alpha 1.0 xcenter 302
    pause 0.5

    show hina 1 sm pyjama h:
        alpha 1.0 xcenter 302
    with None

    voice "HIN_1257"
    hina "\"I got out of the bath and you were gone. I looked everywhere for you.\""

    "Hina made a beeline straight for Rin."

    show rin 1 sm pyjama b with dict_dissolve_25

    voice "RIN_1050"
    rin "\"Sorry, I thought I'd look at the—\""

    show hina 1 sm pyjama e with dict_dissolve_25

    voice "HIN_1258"
    hina "\"You shouldn't spend time with bad influences like her.\""

    "Hina glared at Sachiko and took Rin's hand."

    show hina 1 sm pyjama j with dict_dissolve_25

    voice "HIN_1259"
    hina "\"Let's go!\""

    show hina:
        "hina 1 sm pyjama j flat"
        alpha 1.0 xcenter 302
        easeout 0.5 alpha 0.0 xcenter 202
    show rin:
        "rin 1 sm pyjama b flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 412

    "She wrapped her arm around Rin's and tugged her back to the door."

    hide rin
    hide hina
    with None

    $ side_image = "hina 1 side pyjama d"

    voice "HIN_1260"
    hina "\"Ugh, gross! You smell like cigarettes! We'll have to Febreeze you as soon as we're back in our room.\""

    "Hina scowled, her nose twitching."

    $ side_image = "rin 2 side pyjama e"

    voice "RIN_1051"
    rin "\".........\""

    "Rin sent a wry smile Sachiko's way as Hina pulled her off."

    "Sachiko gave them a lazy wave and watched them leave."

    show sachiko 1 sm outfit cigarette g with dict_dissolve_25

    voice "SYO_0166"
    sachiko "\"Thanks for the treat.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
