label a03_cou1_03:

    scene bg01aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show rin 1 sm pyjama a
    show hina 1 sm pyjama a at pos_r2
    show fumi 1 sm pyjama b at pos_l2
    with Dissolve(0.25)

    voice "FUM_0518"
    fumi "\"That's right, I should let them get some sun, too.\"" id a03_cou1_03_325e8db5

    "Fumi said, moving a chair to the window and lining up some stuffed animals on it."

    voice "HIN_0701"
    hina "\"You really take good care of those, don't you?\"" id a03_cou1_03_945a7f12

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0519"
    fumi "\"They all have names, too.\"" id a03_cou1_03_2b5a0ec8

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "FUM_0520"
    fumi "\"This one is Micha; she's the oldest and most responsible. This one's Gabe, the rowdy little brother. And this one's Rapha, the spoiled youngest sister.\"" id a03_cou1_03_e3b14f43

    show hina 1 sm pyjama k
    show rin 1 sm pyjama e
    with dict_dissolve_25

    voice "RIN_0561"
    rin "\"O-Oh?\"" id a03_cou1_03_fe55a716

    "She looks a little weirded out."

    voice "FUM_0521"
    fumi "\"At home, they have a mom and a dad, and a grandma and grandpa, and Micha's best friend Hani, and Gabe's girlfriend—\"" id a03_cou1_03_3c976185

    "She noticed Hina staring blankly at her."

    show fumi:
        "fumi 1 sm pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0522"
    fumi "\"...I'm sorry. I got carried away. I know it's strange, giving names to my stuffed animals at my age.\"" id a03_cou1_03_e1fb3f7d

    show fumi 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0702"
    hina "\"No, it's just like you.\"" id a03_cou1_03_3669d6fd

    show fumi 1 sm pyjama h with dict_dissolve_25

    voice "FUM_0523"
    fumi "\"You're right, I need to grow up...\"" id a03_cou1_03_bcb2c1ae

    show hina 1 sm pyjama b with dict_dissolve_25

    voice "HIN_0703"
    hina "\"No, I meant it's cute. It was nice hearing about them.\"" id a03_cou1_03_cc4ec776

    show fumi 1 sm pyjama e with dict_dissolve_25

    voice "FUM_0524"
    fumi "\"Huh? Um... r-really...?\"" id a03_cou1_03_ea9e4d62

    show hina 1 sm pyjama a with dict_dissolve_25

    voice "HIN_0704"
    hina "\"Yeah. And I never really played with stuffed animals or dolls when I was a kid, so I kinda envy you.\"" id a03_cou1_03_c237a2f9

    show rin 1 sm pyjama a with dict_dissolve_25

    voice "RIN_0562"
    rin "\"Yeah, you don't seem the type.\"" id a03_cou1_03_ed0c2c30

    show hina 1 sm pyjama i with dict_dissolve_25

    voice "HIN_0705"
    hina "\"Well, I bet you haven't either, Rin.\"" id a03_cou1_03_59811bf7

    show rin 1 sm pyjama c with dict_dissolve_25

    voice "RIN_0563"
    rin "\"Nonsense. I was master-class.\"" id a03_cou1_03_34d6f024

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0706"
    hina "\"Hunh?\"" id a03_cou1_03_3ddccb52

    "Rin picked up Fumi's stuffed animals."

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show rin 1 lg pyjama h:
        xcenter 392
    with Dissolve(0.25)

    voice "RIN_0564"
    rin "\"Micha, the truth is I've always loved you!\"" id a03_cou1_03_3c1ffacb

    show rin:
        "rin 2 lg pyjama f" with Dissolve(0.25)
        xcenter 392
        easein 0.25 xcenter 662
    pause 0.25

    show rin 2 lg pyjama f:
        xcenter 662
        ShakeJump

    voice "RIN_0565"
    rin "\"What are you saying, Gabe? You know I don't appreciate those jokes.\"" id a03_cou1_03_51d488d8

    show rin:
        "rin 1 lg pyjama h" with Dissolve(0.25)
        xcenter 662 xoffset 0 yoffset 0
        easein 0.25 xcenter 392
    pause 0.25

    show rin 1 lg pyjama h:
        xcenter 392
        ShakeYes

    voice "RIN_0566"
    rin "\"It's not a joke! I'm serious about you! Glomp!\"" id a03_cou1_03_b30e3eba

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
    rin "\"Stop that, Gabe! We're siblings by blood! Oh, not there... Aah, ahn, ahn!\"" id a03_cou1_03_5b6b779b

    show rin 2 lg pyjama c:
        xcenter 662 xoffset 0 yoffset 0
    with None

    show rin 1 lg pyjama d with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "RIN_0568"
    rin "\"What're all those noises coming from sissy's room? I'm gonna go see! Pitter, patter, pitter.\"" id a03_cou1_03_eae35a5b

    show rin 2 lg pyjama c:
        xoffset 0 yoffset 0
    with Dissolve(0.25)
    show rin:
        ShakeSide
        0.2
        ShakeNo

    voice "RIN_0569"
    rin "\"Ahn, ahn! No, not so rough!\"" id a03_cou1_03_acf24414

    show rin:
        "rin 1 lg pyjama h" with Dissolve(0.25)
        xcenter 662 xoffset 0 yoffset 0
        easein 0.25 xcenter 392
    pause 0.25

    show rin 1 lg pyjama h:
        ShakeJump

    voice "RIN_0570"
    rin "\"I love you! Micha, I love you!\"" id a03_cou1_03_7122b3c3

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
    rin "\"Clack! Aaah, Micha, Gabe, what are you doing?! The scandal!\"" id a03_cou1_03_04797738

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
    hina "\"Wh—Wh-Wh-Wh-Wh—What are you doing?!!\"" id a03_cou1_03_aba4404d

    show rin 1 sm pyjama g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama e at pos_l2
    show hina 1 sm pyjama l at pos_r2
    with Dissolve(0.25)

    show rin:
        ShakeUji

    voice "RIN_0572"
    rin "\"Ow, ow, ow... you don't have to hit me so hard...\"" id a03_cou1_03_7b59f046

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0708"
    hina "\"Don't defile Fumi's stuffed animals! You creep!\"" id a03_cou1_03_e02f103c

    show fumi behind rin
    show hina 1 sm pyjama f behind rin:
        xoffset 0 yoffset 0
    show rin 2 lg pyjama c
    with Dissolve(0.25)

    show rin:
        ShakeNo

    voice "RIN_0573"
    rin "\"Aahn~, insult me more~!\"" id a03_cou1_03_2b73b968

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
    rin "\"Gfh...\"" id a03_cou1_03_ebbc9cff

    camera
    show rin 1 sm pyjama j:
        xoffset 0 yoffset 0
    with None

    show hina:
        ShakeJump

    voice "HIN_0709"
    hina "\"Stupid! You're forbidden from touching Fumi's stuffed animals, ever again!\"" id a03_cou1_03_7fe7a50a

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0525"
    fumi "\"A-Ahahahaha...\"" id a03_cou1_03_51281c86

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou1_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
