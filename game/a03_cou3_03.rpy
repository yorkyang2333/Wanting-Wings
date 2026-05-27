label a03_cou3_03:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg01aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    $ side_image = "fumi 2 side pyjama c"

    play sound se620_120 fadein 0.5

    voice "FUM_0694"
    fumi "\"♪No tax on the 5th and the 20th, on the 5th and the 20th~\"" id a03_cou3_03_0ba26c23

    "Fumi was cheerfully vacuuming."

    "She was (again subconsciously?) singing the no-tax day song from the drugstore she frequented."

    play sound2 se013a

    voice "RIN_0780"
    rin "\"......\"" id a03_cou3_03_37494e47

    "And again, Rin was stealing glances at her, pretending to read a book."

    stop sound fadeout 1.0

    $ side_image = "fumi 2 side pyjama i"

    voice "FUM_0695"
    fumi "\"Okay.\"" id a03_cou3_03_d9604038

    "The room became very quiet when she turned off the vacuum."

    play sound se013a

    "Rin flipped the pages of her book without running her eyes over the words at all."

    show rin 1 lg pyjama glasses b at pos_r
    show fumi 2 lg pyjama b at pos_l
    with Dissolve(0.25)

    voice "RIN_0781"
    rin "\"I-It's quiet.\"" id a03_cou3_03_81359b00

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0696"
    fumi "\"Oh, I'm sorry. Was the vacuum loud?\"" id a03_cou3_03_fb8230cb

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0782"
    rin "\"No, it didn't bother me.\"" id a03_cou3_03_d17180b3

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0697"
    fumi "\"You've got good concentration~\"" id a03_cou3_03_26ff29f0

    "Fumi said, looking at the cover of Rin's book."

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0698"
    fumi "\"'A Guide to Dog Ownership'? Do you have a pet dog, Ogata?\"" id a03_cou3_03_b7639962

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0783"
    rin "\"Oh, it's something different on the inside.\"" id a03_cou3_03_264c3104

    "Rin took the cover off, revealing a book with an alluring title."

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0699"
    fumi "\"Oh, it's a dirty one. I thought you just went and returned those.\"" id a03_cou3_03_636d270f

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0784"
    rin "\"I wasn't finished with this one.\"" id a03_cou3_03_14b84116

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0700"
    fumi "\"Is it good?\"" id a03_cou3_03_945e4205

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0785"
    rin "\"Probably not to a princess type like you.\"" id a03_cou3_03_883b7bef

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0701"
    fumi "\"Can I see a little of it?\"" id a03_cou3_03_1f6b54a7

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0786"
    rin "\"Oh...\"" id a03_cou3_03_b98ccf43

    play sound [se013a,se013a]

    "The \"princess\" plucked the book from Rin's hands and flipped through it."

    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0702"
    fumi "\"Hmm~, uh huh. Ah, I see.\"" id a03_cou3_03_6cee3d6e

    play sound se013b

    "She exclaimed as she turned the pages."

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0703"
    fumi "\"You're quite the adult to be reading things like this, Ogata~\"" id a03_cou3_03_a356cdee

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0787"
    rin "\"Haha, maybe it's a little too soon for you, Asou.\"" id a03_cou3_03_58f21aef

    "Rin said, eyes wandering for a moment."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0788"
    rin "\"So, have you ever...?\"" id a03_cou3_03_eb1b76cf

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0704"
    fumi "\"Hmm?\"" id a03_cou3_03_f6f5b9e8

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0789"
    rin "\"Kissed, or anything.\"" id a03_cou3_03_a3a1de53

    play sound se013b

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0705"
    fumi "\"I have~\"" id a03_cou3_03_b9d932d9

    "Fumi said, turning a page."

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0790"
    rin "\"What?! S-Seriously? With who?\"" id a03_cou3_03_72c10ab3

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin was shocked at her answer."

    show fumi:
        "fumi 2 lg pyjama i" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0706"
    fumi "\"Aha, just my dog.\"" id a03_cou3_03_6b1cfa98

    show fumi 2 lg pyjama i:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0791"
    rin "\"O... Oh.\"" id a03_cou3_03_21921413

    "She was clearly relieved to hear it."

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0707"
    fumi "\"Haven't with another person yet~\"" id a03_cou3_03_0646ae00

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0792"
    rin "\"Well, wanna try, then?\"" id a03_cou3_03_9bf9d8d8

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0708"
    fumi "\"Huh? With you?\"" id a03_cou3_03_c34a2405

    "Fumi took her eyes off the book and looked at Rin."

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0793"
    rin "\"...Oh, no, I didn't mean that! I was just kidding!\"" id a03_cou3_03_32e5350a

    "She took it back right away."

    stop music fadeout 3.0

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0709"
    fumi "\"Well, alright~\"" id a03_cou3_03_15f9b2bb

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0794"
    rin "\"Huh...?\"" id a03_cou3_03_0c879f5c

    "Fumi's face was right in front of Rin's."

    show rin:
        "rin 1 lg pyjama glasses k" with Dissolve(0.25)
    show fumi:
        "fumi 2 lg pyjama j" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 412

    voice "FUM_0710"
    fumi "\"Mmh...\"" id a03_cou3_03_6dc0e2b9

    play sound se_bati

    show bati2 at truecenter

    show rin 1 lg pyjama glasses k:
        ShakeSide

    voice "RIN_0795"
    rin "\"?!\"" id a03_cou3_03_1680dcdb

    show rin:
        xoffset 0 yoffset 0
    with None

    "They were only touching for a few seconds."

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0711"
    fumi "\"Wow, so soft.\"" id a03_cou3_03_d46c18dc

    "Fumi commented blithely, touching her lips."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0796"
    rin "\"Y-Yeah... I couldn't really tell much though, so can we—\"" id a03_cou3_03_7441d262

    stop music fadeout 1.0

    play sound se521

    $ side_image = "hina 1 side school c"

    voice "HIN_0946"
    hina "\"I'm back!\"" id a03_cou3_03_ee5618d9

    "Once again, Hina opened the door with perfect timing."

    play music bgm01

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0712"
    fumi "\"Oh, hello.\"" id a03_cou3_03_2cb0077d

    show rin:
        "rin 1 lg pyjama glasses g" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 852
    show fumi:
        "fumi 2 lg pyjama d" with Dissolve(0.25)
        xcenter 412
        easein 0.25 xcenter 172
    show hina 1 lg school h with dict_dissolve_25
    pause 0.25

    show rin 1 lg pyjama glasses g:
        xcenter 852
    show fumi 2 lg pyjama d:
        xcenter 172
    with None

    show hina:
        ShakeTameiki

    voice "HIN_0947"
    hina "\"Hey, you two are awfully close again! Come on, break it up!" id a03_cou3_03_14f8cc72

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina inserted herself between them."

    voice "RIN_0797"
    rin "\"Oh, would you be quiet? You're too loud.\"" id a03_cou3_03_ccabed27

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0948"
    hina "\"I will not! You need to stay away from Asou, Rin!\"" id a03_cou3_03_c8f04e4e

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou3_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
