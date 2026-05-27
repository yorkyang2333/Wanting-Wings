label a04_cou1_07:

    scene bg05bb with Dissolve(0.5)
    pause 1.5

    scene bg02ba with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 1 sm school_scarf b with Dissolve(0.25)

    $ side_image = "hina 2 side school f"

    voice "HIN_1204"
    hina "\"Rin, can you sit down a sec?\"" id a04_cou1_07_686c25df

    "Hina sat down at the table and beckoned Rin over."

    show rin:
        "rin 1 sm school a" with Dissolve(0.25)
        ShakeYes

    play sound se116a

    voice "RIN_0974"
    rin "\"Can I change first?\"" id a04_cou1_07_e07304bf

    show rin 1 sm school -school_scarf a:
        xoffset 0 yoffset 0
    with None

    "Rin called back to the living room, removing her scarf."

    $ side_image = "fumi 2 side school a"

    voice "FUM_1022"
    fumi "\"We need to tell you something important.\"" id a04_cou1_07_b1e8fc1f

    "Fumi was seated next to Hina."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_0975"
    rin "\".........\"" id a04_cou1_07_1895cdac

    "Seeing their solemn faces, Rin sighed, hooked her scarf on a bedpost, and headed to the living room."

    stop music fadeout 1.0

    scene black with bg_effect_02
    pause 0.25

    scene bg01ac with bg_effect_02
    pause 0.5

    play music bgm05

    show rin z3 1 lg school b:
        xcenter 918
    show fumi z3 2 lg school a:
        xcenter 124
    show hina z3 1 lg school e behind rin, fumi:
        xcenter 440
    with Dissolve(0.25)

    voice "RIN_0976"
    rin "\"So, why the formality?\"" id a04_cou1_07_8817b282

    voice "HIN_1205"
    hina "\"We thought we should tell you...\"" id a04_cou1_07_98d1fd47

    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_1023"
    fumi "\"Please don't be surprised.\"" id a04_cou1_07_bb077544

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0977"
    rin "\"Uh huh...\"" id a04_cou1_07_78c6ffa6

    stop music fadeout 3.0

    show hina z3 2 lg school d with dict_dissolve_25

    voice "HIN_1206"
    hina "\"The truth is... the two of us are—\"" id a04_cou1_07_025b73a5

    "Hina turned and met Fumi's eye before facing Rin again, her face serious."

    show hina z3 1 lg school f with dict_dissolve_25

    voice "HIN_1207"
    hina "\"We're dating.\"" id a04_cou1_07_37d356e6

    show fumi z3 1 lg school h with dict_dissolve_25

    voice "FUM_1024"
    fumi "\"We're sorry for hiding it all this time! You're surprised, aren't you?\"" id a04_cou1_07_76e3ac4e

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0978"
    rin "\"...No, I was aware.\"" id a04_cou1_07_33d25196

    show hina 1 lg school l
    show fumi 1 lg school j
    with None

    camera:
        function LayerShake(40,40,0.5)
    $ persistent.layer_shaken = False

    $ voice2("hina","HIN_1208","fumi","FUM_1025")
    hina_fumi "\"Whaaat?!\""

    camera
    with None

    play music bgm01

    "The two jumped up in shock."

    show hina:
        "hina z3 1 lg school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1209"
    hina "\"H-How did you know...?\"" id a04_cou1_07_643e9a1d

    show hina z3 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0979"
    rin "\"Hahh... What I want to know is how did you think you were hiding it?\"" id a04_cou1_07_99ec5b81

    show fumi z3 1 lg school h with Dissolve(0.25)
    show fumi:
        ShakeNo

    voice "FUM_1026"
    fumi "\"But... we were being careful not to show any signs of it...\"" id a04_cou1_07_54bb0670

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg school f with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "HIN_1210"
    hina "\"Yeah, we were being totally normal, weren't we?\"" id a04_cou1_07_fa197412

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 2 lg school c with dict_dissolve_25

    voice "RIN_0980"
    rin "\"You were not.\"" id a04_cou1_07_972a7cbb

    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_1027"
    fumi "\"Umm, how long have you known?\"" id a04_cou1_07_e87dbe35

    show rin z3 2 lg school a with dict_dissolve_25

    voice "RIN_0981"
    rin "\"Since Hina had that fever.\"" id a04_cou1_07_6179dcd2

    show fumi z3 2 lg school d with dict_dissolve_25

    voice "FUM_1028"
    fumi "\"What?! Since the very beginning?\"" id a04_cou1_07_ca75ce84

    show rin z3 2 lg school c with dict_dissolve_25

    voice "RIN_0982"
    rin "\"I was right outside the door then.\"" id a04_cou1_07_38d9fb8c

    show hina z3 1 lg school j with dict_dissolve_25

    voice "HIN_1211"
    hina "\"...Eavesdropping?\"" id a04_cou1_07_d0e55b24

    show rin z3 1 lg school g with dict_dissolve_25

    voice "RIN_0983"
    rin "\"That's rude! You two were making out, so I couldn't come in!\"" id a04_cou1_07_2c6661e2

    show fumi z3 1 lg school h with dict_dissolve_25

    voice "FUM_1029"
    fumi "\"S-Sorry...\"" id a04_cou1_07_73ae55fa

    show rin z3 2 lg school c with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0984"
    rin "\"Try not leaving hickeys if you want to keep it a secret.\"" id a04_cou1_07_8cd428ca

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z3 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1212"
    hina "\"Huh?\"" id a04_cou1_07_8c33f1fa

    show hina z3 1 lg school l:
        xoffset 0 yoffset 0
    with None

    "Hina brought a hand to her neck."

    show rin z3 2 lg school e with dict_dissolve_25

    voice "RIN_0985"
    rin "\"And you were doing something dirty in the chapel, right?\"" id a04_cou1_07_cf1d0e42

    show hina:
        "hina z3 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_1213"
    hina "\"You were watching?! Pervert!\"" id a04_cou1_07_42f97d84

    show hina z3 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0986"
    rin "\"I didn't have to watch, I could just tell!\"" id a04_cou1_07_42427326

    show hina z3 1 lg school d with dict_dissolve_25

    voice "HIN_1214"
    hina "\"...Are you psychic?\"" id a04_cou1_07_2a70f5eb

    show rin z3 1 lg school i with dict_dissolve_25

    voice "RIN_0987"
    rin "\"It was written all over your faces.\"" id a04_cou1_07_13d74817

    show hina:
        "hina z3 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1215"
    hina "\"Huh?\"" id a04_cou1_07_67e885d1

    show hina z3 1 lg school l:
        xoffset 0 yoffset 0
    with None

    "This time she touched her face."

    show rin z3 2 lg school c with dict_dissolve_25

    voice "RIN_0988"
    rin "\"It's a figure of speech!\"" id a04_cou1_07_160fda69

    show fumi z3 1 lg school e with dict_dissolve_25

    voice "FUM_1030"
    fumi "\"But if you knew, why didn't you say anything?\"" id a04_cou1_07_9d21c1ef

    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0989"
    rin "\"I'm not gonna talk about it if you two don't want to bring it up.\"" id a04_cou1_07_030b332c

    show fumi z3 2 lg school h with dict_dissolve_25

    voice "FUM_1031"
    fumi "\"It wasn't that we didn't want to bring it up...\"" id a04_cou1_07_8d70ae9b

    show hina z3 2 lg school h with Dissolve(0.25)
    show hina:
        ShakeUji

    voice "HIN_1216"
    hina "\"...It's embarrassing.\"" id a04_cou1_07_0c027a14

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school g with dict_dissolve_25

    voice "RIN_0990"
    rin "\"Well, whatever. I've been having a pretty hard time of it, though.\"" id a04_cou1_07_6b0073d7

    show fumi z3 2 lg school d with dict_dissolve_25

    voice "FUM_1032"
    fumi "\"A hard time?\"" id a04_cou1_07_d382623e

    show rin z3 1 lg school i with dict_dissolve_25

    voice "RIN_0991"
    rin "\"I've had to keep Sachiko away from the room while you two were flirting. She's weirdly sharp about stuff like this.\"" id a04_cou1_07_1681cabb

    show hina z3 1 lg school d with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "HIN_1217"
    hina "\"What, really?!\"" id a04_cou1_07_7ee0de59

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_1033"
    fumi "\"Ah, is that why you suddenly decided to model for her...?!\"" id a04_cou1_07_a18c77b9

    show hina z3 1 lg school c with dict_dissolve_25

    voice "HIN_1218"
    hina "\"You're like our Cupid, Rin.\"" id a04_cou1_07_25be43d2

    show rin:
        "rin z3 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0992"
    rin "\"That's right. You'd better appreciate me.\"" id a04_cou1_07_c0f3debe

    show rin z3 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi z3 2 lg school i" with Dissolve(0.25)
        ShakeYes

    voice "FUM_1034"
    fumi "\"Of course we do!\"" id a04_cou1_07_cccff425

    show fumi z3 2 lg school i:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg school f
    show fumi z3 2 lg school h
    with dict_dissolve_25

    voice "HIN_1219"
    hina "\"So, Rin? While we're appreciating you, is there one more thing we can ask you...?\"" id a04_cou1_07_5429afe7

    show rin z3 1 lg school e with dict_dissolve_25

    voice "RIN_0993"
    rin "\"Like what...?\"" id a04_cou1_07_38f15173

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
