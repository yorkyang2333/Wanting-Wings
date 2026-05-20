label a03_cou1_03:

    scene bg01aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show rin 1 sm pyjama a
    show hina 1 sm pyjama a at pos_r2
    show fumi 1 sm pyjama b at pos_l2
    with Dissolve(0.25)

    voice "FUM_0518"
    fumi "\"That's right, I should let them get some sun, too.\""

    "Fumi said, moving a chair to the window and lining up some stuffed animals on it."

    voice "HIN_0701"
    hina "\"You really take good care of those, don't you?\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0519"
    fumi "\"They all have names, too.\""

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0520"
    fumi "\"This one is Micha; she's the oldest and most responsible. This one's Gabe, the rowdy little brother. And this one's Rapha, the spoiled youngest sister.\""

    show hina 1 sm pyjama k
    show rin 1 sm pyjama e
    with dict_dissolve_25

    voice "RIN_0561"
    rin "\"O-Oh?\""

    "She looks a little weirded out."

    voice "FUM_0521"
    fumi "\"At home, they have a mom and a dad, and a grandma and grandpa, and Micha's best friend Hani, and Gabe's girlfriend—\""

    "She noticed Hina staring blankly at her."

    show fumi:
        "fumi 1 sm pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0522"
    fumi "\"...I'm sorry. I got carried away. I know it's strange, giving names to my stuffed animals at my age.\""

    show fumi 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0702"
    hina "\"No, it's just like you.\""

    show fumi 1 sm pyjama h with dict_dissolve_25

    voice "FUM_0523"
    fumi "\"You're right, I need to grow up...\""

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0703"
    hina "\"No, I meant it's cute. It was nice hearing about them.\""

    show fumi 1 sm pyjama e with dict_dissolve_25

    voice "FUM_0524"
    fumi "\"Huh? Um... r-really...?\""

    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0704"
    hina "\"Yeah. And I never really played with stuffed animals or dolls when I was a kid, so I kinda envy you.\""

    show rin 1 sm pyjama a with dict_dissolve_25

    voice "RIN_0562"
    rin "\"Yeah, you don't seem the type.\""

    show hina 1 sm pyjama i with dict_dissolve_25

    voice "HIN_0705"
    hina "\"Well, I bet you haven't either, Rin.\""

    show rin 1 sm pyjama c with dict_dissolve_25

    voice "RIN_0563"
    rin "\"Nonsense. I was master-class.\""

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0706"
    hina "\"Hunh?\""

    "Rin picked up Fumi's stuffed animals."

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show rin 1 lg pyjama h:
        xcenter 392
    with Dissolve(0.25)

    voice "RIN_0564"
    rin "\"Micha, the truth is I've always loved you!\""

    show rin:
        "rin 2 lg pyjama f" with Dissolve(0.25)
        xcenter 392
        easein 0.25 xcenter 662
    pause 0.25

    show rin 2 lg pyjama f:
        xcenter 662
        ShakeJump

    voice "RIN_0565"
    rin "\"What are you saying, Gabe? You know I don't appreciate those jokes.\""

    show rin:
        "rin 1 lg pyjama h" with Dissolve(0.25)
        xcenter 662 xoffset 0 yoffset 0
        easein 0.25 xcenter 392
    pause 0.25

    show rin 1 lg pyjama h:
        xcenter 392
        ShakeYes

    voice "RIN_0566"
    rin "\"It's not a joke! I'm serious about you! Glomp!\""

    show rin:
        "rin 2 lg pyjama e" with Dissolve(0.25)
        xcenter 392 xoffset 0 yoffset 0
        easein 0.25 xcenter 662
    pause 0.25

    show rin 2 lg pyjama e:
        xcenter 662
        ShakeSide
        3.8
        "rin 2 lg pyjama c" with Dissolve(0.25)
        ShakeSide
        0.5
        ShakeNo

    voice "RIN_0567"
    rin "\"Stop that, Gabe! We're siblings by blood! Oh, not there... Aah, ahn, ahn!\""

    show rin 2 lg pyjama c:
        xcenter 662 xoffset 0 yoffset 0
    with None

    show rin 1 lg pyjama d with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "RIN_0568"
    rin "\"What're all those noises coming from sissy's room? I'm gonna go see! Pitter, patter, pitter.\""

    show rin 2 lg pyjama c:
        xoffset 0 yoffset 0
    with Dissolve(0.25)
    show rin:
        ShakeSide
        0.2
        ShakeNo

    voice "RIN_0569"
    rin "\"Ahn, ahn! No, not so rough!\""

    show rin:
        "rin 1 lg pyjama h" with Dissolve(0.25)
        xcenter 662 xoffset 0 yoffset 0
        easein 0.25 xcenter 392
    pause 0.25

    show rin 1 lg pyjama h:
        ShakeJump

    voice "RIN_0570"
    rin "\"I love you! Micha, I love you!\""

    show rin:
        "rin 1 lg pyjama e" with Dissolve(0.25)
        xcenter 392 xoffset 0 yoffset 0
        easein 0.25 xcenter 512
    pause 0.25

    show rin 1 lg pyjama e:
        xcenter 512
        0.2
        "rin 1 lg pyjama j" with Dissolve(0.1)
        function LayerShake(20,20,0.5)
        0.2
        ShakeJump
        0.2
        ShakeJump
        1.5
        "rin 1 lg pyjama d" with Dissolve(0.1)
        ShakeJump
        ShakeJump
    $ persistent.layer_shaken = False

    voice "RIN_0571"
    rin "\"Clack! Aaah, Micha, Gabe, what are you doing?! The scandal!\""

    show rin 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None

    show hina behind rin:
        "hina 1 lg pyjama l flat"
        alpha 0.0 xcenter 952
        easein 0.2 alpha 1.0 xcenter 852
    pause 0.2

    show hina 1 lg pyjama l:
        alpha 1.0 xcenter 852
    with None
    show rin:
        "rin 1 lg pyjama g" with Dissolve(0.25)
        function LayerShake(40,40,0.5)
    $ persistent.layer_shaken = False

    play sound se103b

    voice "HIN_0707"
    hina "\"Wh—Wh-Wh-Wh-Wh—What are you doing?!!\""

    show rin 1 sm pyjama g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama e at pos_l2
    show hina 1 sm pyjama l at pos_r2
    with Dissolve(0.25)

    show rin:
        ShakeUji

    voice "RIN_0572"
    rin "\"Ow, ow, ow... you don't have to hit me so hard...\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0708"
    hina "\"Don't defile Fumi's stuffed animals! You creep!\""

    show fumi behind rin
    show hina 1 sm pyjama f behind rin:
        xoffset 0 yoffset 0
    show rin 2 lg pyjama c
    with Dissolve(0.25)

    show rin:
        ShakeNo

    voice "RIN_0573"
    rin "\"Aahn~, insult me more~!\""

    play sound se103b

    show rin:
        xoffset 0 yoffset 0
    with None

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False
    show rin 1 sm pyjama j with Dissolve(0.25):
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_0574"
    rin "\"Gfh...\""

    camera
    show rin 1 sm pyjama j:
        xoffset 0 yoffset 0
    with None

    show hina:
        ShakeJump

    voice "HIN_0709"
    hina "\"Stupid! You're forbidden from touching Fumi's stuffed animals, ever again!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0525"
    fumi "\"A-Ahahahaha...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou1_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
