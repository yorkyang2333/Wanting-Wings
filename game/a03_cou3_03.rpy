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
    fumi "\"♪No tax on the 5th and the 20th, on the 5th and the 20th~\""

    "Fumi was cheerfully vacuuming."

    "She was (again subconsciously?) singing the no-tax day song from the drugstore she frequented."

    play sound2 se013a

    voice "RIN_0780"
    rin "\"......\""

    "And again, Rin was stealing glances at her, pretending to read a book."

    stop sound fadeout 1.0

    $ side_image = "fumi 2 side pyjama i"

    voice "FUM_0695"
    fumi "\"Okay.\""

    "The room became very quiet when she turned off the vacuum."

    play sound se013a

    "Rin flipped the pages of her book without running her eyes over the words at all."

    show rin 1 lg pyjama glasses b at pos_r
    show fumi 2 lg pyjama b at pos_l
    with Dissolve(0.25)

    voice "RIN_0781"
    rin "\"I-It's quiet.\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0696"
    fumi "\"Oh, I'm sorry. Was the vacuum loud?\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0782"
    rin "\"No, it didn't bother me.\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0697"
    fumi "\"You've got good concentration~\""

    "Fumi said, looking at the cover of Rin's book."

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0698"
    fumi "\"'A Guide to Dog Ownership'? Do you have a pet dog, Ogata?\""

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0783"
    rin "\"Oh, it's something different on the inside.\""

    "Rin took the cover off, revealing a book with an alluring title."

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0699"
    fumi "\"Oh, it's a dirty one. I thought you just went and returned those.\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0784"
    rin "\"I wasn't finished with this one.\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0700"
    fumi "\"Is it good?\""

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0785"
    rin "\"Probably not to a princess type like you.\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0701"
    fumi "\"Can I see a little of it?\""

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0786"
    rin "\"Oh...\""

    play sound [se013a,se013a]

    "The \"princess\" plucked the book from Rin's hands and flipped through it."

    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0702"
    fumi "\"Hmm~, uh huh. Ah, I see.\""

    play sound se013b

    "She exclaimed as she turned the pages."

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0703"
    fumi "\"You're quite the adult to be reading things like this, Ogata~\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0787"
    rin "\"Haha, maybe it's a little too soon for you, Asou.\""

    "Rin said, eyes wandering for a moment."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0788"
    rin "\"So, have you ever...?\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0704"
    fumi "\"Hmm?\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0789"
    rin "\"Kissed, or anything.\""

    play sound se013b

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0705"
    fumi "\"I have~\""

    "Fumi said, turning a page."

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0790"
    rin "\"What?! S-Seriously? With who?\""

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin was shocked at her answer."

    show fumi:
        "fumi 2 lg pyjama i" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0706"
    fumi "\"Aha, just my dog.\""

    show fumi 2 lg pyjama i:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0791"
    rin "\"O... Oh.\""

    "She was clearly relieved to hear it."

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0707"
    fumi "\"Haven't with another person yet~\""

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0792"
    rin "\"Well, wanna try, then?\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0708"
    fumi "\"Huh? With you?\""

    "Fumi took her eyes off the book and looked at Rin."

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0793"
    rin "\"...Oh, no, I didn't mean that! I was just kidding!\""

    "She took it back right away."

    stop music fadeout 3.0

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0709"
    fumi "\"Well, alright~\""

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0794"
    rin "\"Huh...?\""

    "Fumi's face was right in front of Rin's."

    show rin:
        "rin 1 lg pyjama glasses k" with Dissolve(0.25)
    show fumi:
        "fumi 2 lg pyjama j" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 412

    voice "FUM_0710"
    fumi "\"Mmh...\""

    play sound se_bati

    show bati2 at truecenter

    show rin 1 lg pyjama glasses k:
        ShakeSide

    voice "RIN_0795"
    rin "\"?!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "They were only touching for a few seconds."

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0711"
    fumi "\"Wow, so soft.\""

    "Fumi commented blithely, touching her lips."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0796"
    rin "\"Y-Yeah... I couldn't really tell much though, so can we—\""

    stop music fadeout 1.0

    play sound se521

    $ side_image = "hina 1 side school c"

    voice "HIN_0946"
    hina "\"I'm back!\""

    "Once again, Hina opened the door with perfect timing."

    play music bgm01

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0712"
    fumi "\"Oh, hello.\""

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
    hina "\"Hey, you two are awfully close again! Come on, break it up!"

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina inserted herself between them."

    voice "RIN_0797"
    rin "\"Oh, would you be quiet? You're too loud.\""

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0948"
    hina "\"I will not! You need to stay away from Asou, Rin!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou3_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
