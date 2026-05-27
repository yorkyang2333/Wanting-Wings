label a03_cou1_09:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play sound se030a

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm05

    play sound2 se000c

    show rin 1 lg school a at pos_l
    show fumi:
        "fumi 1 lg school_scarf h flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772

    "Fumi was at Rin's desk before the bell had even finished ringing."

    show fumi 1 lg school_scarf h:
        alpha 1.0 xcenter 772
    with None

    show fumi 1 lg school_scarf j with dict_dissolve_25

    voice "FUM_0621"
    fumi "\"Let's hurry home!\"" id a03_cou1_09_8e63b0ae

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0634"
    rin "\"What about locking up the classroom? Since Hina's not here—\"" id a03_cou1_09_0dcc2d84

    show fumi 1 lg school_scarf h with dict_dissolve_25

    voice "FUM_0622"
    fumi "\"I asked someone else to do it.\"" id a03_cou1_09_6fc9fa83

    show rin:
        "rin 1 lg school a" with Dissolve(0.25)
        5.0
        "rin 1 lg school j"
        ShakeSide

    voice "RIN_0635"
    rin "\"And we asked Sachiko to look after Hina, so I don't think we really need to rush that... whoa!\"" id a03_cou1_09_1693cc5a

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None

    play sound se131a

    show fumi:
        "fumi 1 lg school_scarf h flat"
        alpha 1.0 xcenter 772
        easeout 0.25 alpha 0.0 xcenter 872

    play sound2 se131a

    pause 0.25

    show rin:
        "rin 1 lg school j flat"
        alpha 1.0 xcenter 252
        easeout 0.25 alpha 0.0 xcenter 352

    "Fumi grabbed Rin's arm before she could finish and ran off."

    hide rin
    hide fumi
    with None

    scene black with bg_effect_11
    pause 1.0

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg05ba with Dissolve(0.25)
    pause 0.75

    play sound se001b

    show sachiko 1 sm outfit a at pos_l2 with dict_dissolve_25
    show fumi:
        "fumi 1 sm school_scarf h flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512
    show rin:
        "rin 1 sm school a flat"
        alpha 0.0 xcenter 952
        0.5
        easein 0.5 alpha 1.0 xcenter 852

    voice "SYO_0127"
    sachiko "\"Hey, welc—\"" id a03_cou1_09_75c41bad

    show fumi 1 sm school_scarf h:
        alpha 1.0 xcenter 512
    show rin 1 sm school a:
        alpha 1.0 xcenter 852
    with None

    voice "RIN_0636"
    rin "\"We're—\"" id a03_cou1_09_d4366ffb

    play sound se133b

    show fumi:
        "fumi 1 sm school_scarf h flat"
        alpha 1.0 xcenter 512
        easeout 0.25 alpha 0.0 xcenter 412

    "Fumi ran straight through Sachiko and Rin's exchange to their room."

    hide fumi with None

    stop music fadeout 1.0

    scene black with bg_effect_12
    pause 0.25

    scene bg02ba with bg_effect_12
    pause 0.5

    play sound se001c

    $ side_image = "fumi 1 side school_scarf j"

    voice "FUM_0623"
    fumi "\"Hina!\"" id a03_cou1_09_cc3dde50

    show hina 2 lg pyjama b:
        xcenter 852 ycenter 1025
    with dict_dissolve_25

    voice "HIN_0805"
    hina "\"Oh, hi, Fumi.\"" id a03_cou1_09_ae114f93

    "Hina was sitting up in bed, the picture of health."

    show fumi:
        "fumi 1 lg school_scarf k flat"
        alpha 0.0 xcenter 312
        easein 0.5 alpha 1.0 xcenter 412

    voice "FUM_0624"
    fumi "\"Are you okay?\"" id a03_cou1_09_fbdd4535

    show fumi 1 lg school_scarf k:
        alpha 1.0 xcenter 412
    with None
    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0806"
    hina "\"Yeah, my fever was down by noon.\"" id a03_cou1_09_9c9bca0c

    show fumi 1 lg school_scarf i with dict_dissolve_25

    voice "FUM_0625"
    fumi "\"Oh, good...\"" id a03_cou1_09_f668b808

    play music bgm02

    "Fumi's bag slipped out of her hand to land on the floor with a {i}thud{/i}."

    play sound se118b

    show fumi:
        "fumi 1 lg school_scarf k" with Dissolve(0.25)
        ycenter 1021
        easein 0.25 ycenter 1097

    "She staggered over to the bed and sank to the floor."

    show fumi 1 lg school_scarf k:
        ycenter 1097
    with None

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0807"
    hina "\"Thanks for the soup. It was really good.\"" id a03_cou1_09_371a0792

    "She looked to the kitchen and noticed the soup she'd made for Hina that morning was completely gone."

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0808"
    hina "\"It's not very filling though, you know?\"" id a03_cou1_09_916b1d7d

    "She sighed, rubbing her stomach, the same Hina as always."

    show fumi 1 lg school_scarf e with dict_dissolve_25

    voice "FUM_0626"
    fumi "\"I'll make you some more right—\"" id a03_cou1_09_8246bc52

    "Fumi made to stand up, but Hina grabbed her hand."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0809"
    hina "\"Hey...\"" id a03_cou1_09_88194988

    "She stared at Fumi's face..."

    voice "HIN_0810"
    hina "\"...Did you kiss my forehead last night?\"" id a03_cou1_09_e0dcb35a

    "...and asked her that."

    show fumi:
        "fumi 1 lg school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0627"
    fumi "\"Huh? Umm...\"" id a03_cou1_09_2524b056

    show fumi 1 lg school_scarf j:
        ycenter 1097 xoffset 0 yoffset 0
    with None

    "Fumi hesitated."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0811"
    hina "\"It must have just been a dream.\"" id a03_cou1_09_3cf344f4

    "Hina said, letting go of Fumi's hand."

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0812"
    hina "\"Sorry for asking something so weird.\"" id a03_cou1_09_c517a175

    show fumi 1 lg school_scarf h with dict_dissolve_25

    voice "FUM_0628"
    fumi "\"It... It wasn't a dream.\"" id a03_cou1_09_f7308e18

    "Fumi confessed, her eyes on the floor."

    show fumi 1 lg school_scarf k with dict_dissolve_25

    voice "FUM_0629"
    fumi "\"...I'm sorry.\"" id a03_cou1_09_9a04ae00

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0813"
    hina "\"......\"" id a03_cou1_09_fe512ac0

    "There was silence between them for a moment."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0814"
    hina "\"Oh, okay!\"" id a03_cou1_09_ff4bc928

    show fumi 2 lg school_scarf h with dict_dissolve_25

    voice "FUM_0630"
    fumi "\"Huh?\"" id a03_cou1_09_2cd710d3

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0815"
    hina "\"Your lips were really soft. It felt good. I bet that's what cured my fever.\"" id a03_cou1_09_522e2f4f

    "Hina gave her a toothy grin."

    show fumi 2 lg school_scarf d with dict_dissolve_25

    voice "FUM_0631"
    fumi "\"Hina...\"" id a03_cou1_09_d2719fa4

    show hina 1 lg pyjama b with dict_dissolve_25

    voice "HIN_0816"
    hina "\"When I'm better, could you do it a—\"" id a03_cou1_09_a53da330

    play sound se116a

    show fumi:
        "fumi 2 lg school_scarf h" with Dissolve(0.25)
        xcenter 412 ycenter 1097
        easein 0.5 xcenter 562 ycenter 1111

    "Before she'd even finished, Fumi kissed Hina's forehead once more."

    show fumi 2 lg school_scarf h:
        xcenter 562 ycenter 1111
    with None
    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0817"
    hina "\"Aha, they really are sof—\"" id a03_cou1_09_e5b3bb18

    "Then on the mouth."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0818"
    hina "\"F-Fumi...?\"" id a03_cou1_09_1914bef9

    play sound se118c

    show fumi:
        "fumi 1 lg school_scarf j" with Dissolve(0.25)
        xcenter 562
        easein 0.25 xcenter 412

    voice "FUM_0632"
    fumi "\"...Huh? Ahh! I-I'm sorry, I don't know what came over me!\"" id a03_cou1_09_ffe7a784

    show fumi 1 lg school_scarf j:
        xcenter 412 ycenter 1111
    with None

    "Coming back to her senses, Fumi apologized earnestly."

    show fumi 1 lg school_scarf h with dict_dissolve_25

    voice "FUM_0633"
    fumi "\"Wh-What on earth am I doing?! I just, I was looking at you, and, I, umm...\"" id a03_cou1_09_ee5d2181

    voice "HIN_0819"
    hina "\"Uhh... I don't... mind you kissing me.\"" id a03_cou1_09_9de85ef8

    show fumi 1 lg school_scarf e with dict_dissolve_25

    voice "FUM_0634"
    fumi "\"Huh...?\"" id a03_cou1_09_4b9bd160

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0820"
    hina "\"Actually... it made me really happy.\"" id a03_cou1_09_1c777468

    show fumi 2 lg school_scarf h with dict_dissolve_25

    voice "FUM_0635"
    fumi "\"...Ahh...\"" id a03_cou1_09_845c091b

    show fumi:
        "fumi 2 lg school_scarf i" with Dissolve(0.25)
        xcenter 412
        easein 0.25 xcenter 562

    play sound se118a

    voice "FUM_0636"
    fumi "\"Hina!\"" id a03_cou1_09_3df404af

    show fumi 2 lg school_scarf i:
        xcenter 562 ycenter 1111
    with None

    "Fumi embraced Hina, overcome with emotion."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0821"
    hina "\"You'll catch my cold...\"" id a03_cou1_09_a3ac2c95

    show fumi 2 lg school_scarf c with dict_dissolve_25

    voice "FUM_0637"
    fumi "\"It's okay. I'm really healthy.\"" id a03_cou1_09_f6b96338

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0822"
    hina "\"...Fumi.\"" id a03_cou1_09_d1b558db

    show fumi 2 lg school_scarf d with dict_dissolve_25

    voice "FUM_0638"
    fumi "\"Oh, I'm not an idiot, though.\"" id a03_cou1_09_e248860d

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0823"
    hina "\"Nobody said that.\"" id a03_cou1_09_e5f5f794

    show fumi 2 lg school_scarf c with dict_dissolve_25

    voice "FUM_0639"
    fumi "\"I thought I'd say so before anyone did.\"" id a03_cou1_09_0276acbf

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0824"
    hina "\"...Eheheh.\"" id a03_cou1_09_2876bdd9

    show fumi 2 lg school_scarf i with dict_dissolve_25

    voice "FUM_0640"
    fumi "\"...Heh, eheheheh.\"" id a03_cou1_09_6f0d35b2

    "The two hugged tighter, giggling together."

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0825"
    hina "\"...Fumi.\"" id a03_cou1_09_d0cd851f

    show fumi 2 lg school_scarf d with dict_dissolve_25

    voice "FUM_0641"
    fumi "\"Yes?\"" id a03_cou1_09_c05250b4

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0826"
    hina "\"I think I love you, Fumi. As more than just a friend.\"" id a03_cou1_09_a1b79ff4

    show fumi 2 lg school_scarf i with dict_dissolve_25

    voice "FUM_0642"
    fumi "\"I think I feel the same way about you, Hina.\"" id a03_cou1_09_a69b0966

    show hina:
        "hina 2 lg pyjama h" with Dissolve(0.25)
        ShakeUji

    voice "HIN_0827"
    hina "\"Ugh... I think I'm gonna get a fever again.\"" id a03_cou1_09_d31f7af1

    show hina 2 lg pyjama h:
        ycenter 1025 xoffset 0 yoffset 0
    with None

    play sound se118c

    show fumi:
        "fumi 1 lg school_scarf j" with Dissolve(0.25)
        xcenter 562
        easein 0.25 xcenter 412

    voice "FUM_0643"
    fumi "\"Awawa! I-I'm sorry!\"" id a03_cou1_09_7df3847a

    show fumi 1 lg school_scarf j:
        xcenter 412 ycenter 1111
    with None

    "Fumi pulled back hurriedly."

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0828"
    hina "\"No, I just mean... my heart's pounding, and I feel really hot.\"" id a03_cou1_09_706c10a8

    show fumi 1 lg school_scarf i with dict_dissolve_25

    voice "FUM_0644"
    fumi "\"I... I know what you mean.\"" id a03_cou1_09_4e5fcff0

    scene black with Dissolve(0.5)
    pause 2.0

    scene bg05ba with bg_effect_01_1000
    pause 0.5

    "Meanwhile, out in the hallway..."

    show rin 1 sm school g at pos_l with Dissolve(0.25)

    voice "RIN_0637"
    rin "\"I can't exactly go in there, huh...?\"" id a03_cou1_09_d2864b19

    "Rin muttered, her back against the door."

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0128"
    sachiko "\"Hm? How come you can't go in?\"" id a03_cou1_09_b9b3a304

    show rin:
        "rin 1 sm school j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0638"
    rin "\"Huh?! Uhh, I'm just feeling a little dizzy.\"" id a03_cou1_09_c56a1b20

    show rin 1 sm school j:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "SYO_0129"
    sachiko "\"You okay?\"" id a03_cou1_09_0d899b99

    show rin:
        "rin 1 sm school d" with Dissolve(0.25)
        ShakeYes2

    voice "RIN_0639"
    rin "\"Totally okay. Other than not being able to go into the room, completely okay!\"" id a03_cou1_09_696ee459

    show rin 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0130"
    sachiko "\"...Are {i}you{/i} sick now?\"" id a03_cou1_09_06e3cec8

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    scene chapter04
    with Dissolve(0.5)
    pause 1.5

    show chapter04a with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
