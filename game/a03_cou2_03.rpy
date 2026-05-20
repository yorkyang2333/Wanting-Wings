label a03_cou2_03:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg01aa with Dissolve(0.25)
    pause 0.75

    play music bgm02

    $ side_image = "hina 1 side pyjama h"

    voice "HIN_0853"
    hina "\"Ugh, I'm hungry... Hurry up and come back from the store, Asou~\""

    "Hina lay on the floor in the living room, but there was no one to answer her."

    $ side_image = "hina 1 side pyjama j"

    voice "HIN_0854"
    hina "\"And Rin's not coming back from Sachiko's... How long does it take to return a few books—\""

    $ side_image = "hina 1 side pyjama d"

    voice "HIN_0855"
    hina "\"Wait, is she borrowing more?!\""

    "She got it in one."

    show hina:
        "hina 1 lg pyjama e flat"
        alpha 0.0 xcenter 512 ycenter 1081
        easein 0.5 alpha 1.0 ycenter 981
    pause 0.5

    voice "HIN_0856"
    hina "\"...There aren't more hidden around here, are there?\""

    show hina 1 lg pyjama e:
        alpha 1.0 xcenter 512 ycenter 981
    with None

    "Hina leapt up and peered at Rin's bookshelf."

    "There was a long line of paperbacks, but none of them seemed to have indecent titles."

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0857"
    hina "\"This looks suspicious...\""

    "Plucking out a book with a cover around it, she flipped through the pages."

    play sound se013a

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_0858"
    hina "\"'I couldn't tell whose lips were drawing closer first: hers or mine...'\""

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0859"
    hina "\"It starts right with a kiss...?\""

    "Hina kept reading, a puzzled look on her face."

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0860"
    hina "\"'The moment her tongue entered my mouth, my mind went completely blank—'\""

    show hina 1 lg pyjama d with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0861"
    hina "\"It {i}is{/i} a dirty one!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina averted her eyes from the book."

    show hina 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0862"
    hina "\"I knew she was hiding more!\""

    "She was grumbling about it, but she also looked somehow excited, like she'd discovered a secret treasure."

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0863"
    hina "\"I'll have to yell at her when she gets back...\""

    "Hina looked down to the book in her hands."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0864"
    hina "\"...If this was the only one that was covered, does it have something really crazy in it?\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0865"
    hina "\"Maybe... I should check.\""

    "Hina went back to the page, eyeing the words."

    stop music fadeout 1.0

    "........."

    play music bgm04

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0866"
    hina "\"Huh? That's weird...\""

    "Hina cocked her head."

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0867"
    hina "\"'Her' is Hanayo, right? And 'I' is Youko? Huh? They're both girls? Hwha? Hwha?\""

    play sound [se013a,se013a]

    "Hina went over the page once more."

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_0868"
    hina "\"'I'd never been attracted to another woman before.'\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0869"
    hina "\"So... they {i}are{/i} both women.\""

    "Hina's face bobbed up from the page, confusion painted across it."

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0870"
    hina "\"But they're doing dirty stuff, so... huh? Uh, wha?\""

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0871"
    hina "\"If this book is on Rin's bookshelf, does that mean Rin's also...?\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0872"
    hina "\"...Oh.\""

    "Hina found herself touching her lips."

    stop music fadeout 0.1

    $ side_image = "rin 1 side pyjama f"

    voice "RIN_0666"
    rin "\"So? You like that book?\""

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        function LayerShake(30,30,0.25)
    $ persistent.layer_shaken = False

    voice "HIN_0873"
    hina "\"Hyaaaah?!\""

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None

    "Rin's voice came from behind her and Hina screamed."

    play music bgm02

    show hina:
        "hina 1 lg pyjama d" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 252
    show rin:
        "rin 1 lg pyjama c flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772

    voice "HIN_0874"
    hina "\"Wh-When did you get back?!\""

    show hina 1 lg pyjama d:
        xcenter 252
    show rin 1 lg pyjama c:
        alpha 1.0 xcenter 772
    with None

    show rin 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0667"
    rin "\"You were so into it you didn't notice me coming in the door, huh?\""

    show hina 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0875"
    hina "\"H-H-H-Here! Hurry and give this back to Sachiko!\""

    play sound se118c

    "Hina thrust the book out to Rin."

    show rin 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0668"
    rin "\"Oh, that one's mine. I like that one.\""

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0876"
    hina "\"Y-You like it? This dirty book?!\""

    show rin 2 lg pyjama e with dict_dissolve_25

    voice "RIN_0669"
    rin "\"It's really good.\""

    "Rin plucked the book nonchalantly from Hina's hands."

    show rin 2 lg pyjama c with dict_dissolve_25

    voice "RIN_0670"
    rin "\"I suppose Hina the little baby wouldn't get it, though.\""

    show hina:
        "hina 2 lg pyjama h" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0877"
    hina "\"......\""

    show hina 2 lg pyjama h:
        xoffset 0 yoffset 0
    with None

    "It's rare for Hina to not get upset about being called a baby."

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0878"
    hina "\"...Are you...\""

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0671"
    rin "\"Hm?\""

    stop music fadeout 3.0

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0879"
    hina "\"...Into girls, Rin?\""

    play sound se521

    show hina:
        "hina 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    $ side_image = "fumi 1 side school_scarf c"

    voice "FUM_0649"
    fumi "\"I'm back!\""

    show hina 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0672"
    rin "\"Hey, Asou.\""

    play music bgm01

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show hina 1 sm pyjama d at pos_l2
    show rin 1 sm pyjama c
    with dict_dissolve_25
    show fumi:
        "fumi 1 sm school_scarf b flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    pause 0.5

    voice "FUM_0650"
    fumi "\"They had some good-looking sandwiches, so I bought some.\""

    show fumi 1 sm school_scarf b:
        alpha 1.0 xcenter 852
    with None

    show rin 1 sm pyjama d with dict_dissolve_25

    voice "RIN_0673"
    rin "\"Great, I was just getting hungry~\""

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "FUM_0651"
    fumi "\"They had the egg sandwiches you like too, Natsume.\""

    show hina 1 sm pyjama g with dict_dissolve_25

    voice "HIN_0880"
    hina "\"Y-Yay~\""

    show rin 1 sm pyjama e with dict_dissolve_25

    play sound se558a

    voice "RIN_0674"
    rin "\"Oh, right. Were you saying something a minute ago, Hina?\""

    "Rin asked, picking out a sandwich."

    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0881"
    hina "\"N-No, it was nothing.\""

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0652"
    fumi "\"...Natsume, your face is a little red.\""

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0882"
    hina "\"Huh? Huh? Huh? Huh? Is it?\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show hina 1 lg pyjama l at pos_l
    show fumi 1 lg school_scarf k
    with dict_dissolve_25

    voice "FUM_0653"
    fumi "\"Yes. You don't have a fever, do you...?\""

    play sound se116a

    "Fumi put her hand to Hina's forehead."

    show fumi 1 lg school_scarf d with dict_dissolve_25

    voice "FUM_0654"
    fumi "\"You're a little warm. I wonder if it's a cold.\""

    show hina 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0883"
    hina "\"N-No, it's not.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou2_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
