label a03_cou2_05:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg01aa with Dissolve(0.25)
    pause 0.75

    play music bgm02

    play sound se013a

    show rin 2 lg pyjama glasses a with Dissolve(0.25)

    voice "RIN_0692"
    rin "\"...75 points. That's a passing grade.\""

    show rin:
        "rin 2 lg pyjama a" with Dissolve(0.25)
        ShakeYes

    play sound se636

    "Tracing the last sentence with her finger, Rin closed her book and set her glasses down on the table."

    show rin 2 lg pyjama a:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama -glasses g with dict_dissolve_25

    voice "RIN_0693"
    rin "\"Hey, Hina, wanna eat lunch?\""

    $ side_image = "hina 2 side pyjama headphones h"

    voice "HIN_0903"
    hina "\"......\""

    "There was no answer. She had her headphones on again."

    "Hina was sitting at her desk, opening and closing the film compartment on her camera."

    "She'd been like this since Fumi had left earlier."

    show rin 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0694"
    rin "\"Hiiinaaa!\""

    $ side_image = "hina 2 side pyjama headphones h"

    voice "HIN_0904"
    hina "\"......\""

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0695"
    rin "\"Oh, fine.\""

    hide rin with Dissolve(0.25)

    play sound se116a

    "Rin got up from the cushion."

    show rin 2 lg pyjama a
    show hina 2 lg pyjama headphones h at pos_l
    with Dissolve(0.25)

    show rin:
        ShakeTameiki

    voice "RIN_0696"
    rin "\"Hiiina!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    play sound se555b

    voice "HIN_0905"
    hina "\"Hyah?!\""

    show hina 1 lg pyjama -headphones d:
        xoffset 0 yoffset 0
    with None

    "Rin tapped Hina on the shoulder and Hina leapt up so fast, she almost knocked her chair over."

    "Loud singing came from the headphones now on the floor."

    show rin:
        "rin 2 lg pyjama d" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 772

    voice "RIN_0697"
    rin "\"Hey, what are you getting so surprised for? I'm hurt.\""

    show rin 2 lg pyjama d:
        xcenter 772
    with None
    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0906"
    hina "\"...Sorry.\""

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_0698"
    rin "\"Huh? No, I mean... you don't have to get so serious either...\""

    "Rin was taken aback by the sincere apology."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0907"
    hina "\"Did you want something?\""

    show rin 2 lg pyjama d with dict_dissolve_25

    voice "RIN_0699"
    rin "\"Yeah. It's lunchtime. What do you want to do?\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0908"
    hina "\"......\""

    show rin 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0700"
    rin "\"Asou made us some hayashi rice. You want to heat that up?\""

    voice "HIN_0909"
    hina "\"...Yeah.\""

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0701"
    rin "\"...Okay, I'll do that. Wait at the table, Hina?\""

    hide hina with Dissolve(0.25)

    "Hina nodded and stood from her chair."

    show rin 1 lg pyjama h:
        xcenter 772
        easein 0.25 xcenter 512

    voice "RIN_0702"
    rin "\"......\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01aa with bg_effect_05
    pause 0.5

    show hina 2 lg pyjama h at pos_l
    show rin 2 lg pyjama g at pos_r
    with Dissolve(0.25)

    show rin:
        ShakeYes

    play sound se009b

    voice "RIN_0703"
    rin "\"Here you go.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin set down two plates with spoons at the table."

    show hina 1 lg pyjama n with dict_dissolve_25

    voice "HIN_0910"
    hina "\"Thanks.\""

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0704"
    rin "\"Hey, what do you think about putting cheese in hayashi rice? Yes or no?\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0911"
    hina "\"I dunno, I've never done it before.\""

    show rin 2 lg pyjama a with dict_dissolve_25

    voice "RIN_0705"
    rin "\"Then, do you know where the term 'hayashi rice' came from?\""

    show hina 1 lg pyjama n with dict_dissolve_25

    voice "HIN_0912"
    hina "\"......\""

    show rin 2 lg pyjama g with dict_dissolve_25

    voice "RIN_0706"
    rin "\"There are all sorts of theories, like it comes from 'hashed' meat, or it's named after Yuteki Hayashi, or 'hayai' like 'fast' became 'hayashi'—\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0913"
    hina "\"Oh yeah?\""

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_0707"
    rin "\"...Not interested?\""

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_0914"
    hina "\"Huh? Oh, no, that's not it...\""

    show hina 2 lg pyjama h with dict_dissolve_25

    "........."

    "......"

    "The conversation carried on in that way, with Rin talking and Hina only giving short replies."

    scene black with bg_effect_05
    pause 0.5

    scene bg01aa with bg_effect_05
    pause 0.5

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0915"
    hina "\"Thanks for lunch.\""

    play sound se009a

    "Finishing first, Hina picked up her plate and stood up."

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0708"
    rin "\"Oh, just leave it in the sink. I'll wash it all.\""

    $ side_image = "hina 2 side pyjama f"

    voice "HIN_0916"
    hina "\"Really?\""

    show rin 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0709"
    rin "\"Mhm. Oh, have you done your homework yet? I'll help if there's something you don't get.\""

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0917"
    hina "\"Okay. I'm good for now.\""

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0710"
    rin "\"Yeah?\""

    $ side_image = "hina 2 side pyjama f"

    voice "HIN_0918"
    hina "\"Umm... I'm gonna go out for a bit.\""

    play sound se555

    "Leaving her dishes in the sink, Hina headed to the door and put her shoes on."

    show rin 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0711"
    rin "\"Huh? Hey, wait, you should put a coat on or—\""

    play sound se522

    "But Hina left just like that, without even turning back to Rin."

    show rin 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0712"
    rin "\"......\""

    "Rin was left staring at the door she'd just closed."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou2_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
