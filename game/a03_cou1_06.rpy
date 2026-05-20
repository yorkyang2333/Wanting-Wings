label a03_cou1_06:

    scene bg02aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 3 sm light pyjama c:
        xcenter 646
    with Dissolve(0.25)

    voice "HIN_0759"
    hina "\"It's been a while since it was just you and me, huh?\""

    show rin 3 sm light pyjama glasses d with dict_dissolve_25

    voice "RIN_0589"
    rin "\"Huh? Has it?\""

    "Rin raised her head from the book she was reading in bed."

    show rin 3 sm light pyjama glasses b with dict_dissolve_25

    voice "RIN_0590"
    rin "\"Isn't it always just us when Asou leaves?\""

    show hina 3 sm light pyjama d with dict_dissolve_25

    voice "HIN_0760"
    hina "\"Don't you miss her when you think about how Fumi won't be back until tonight?\""

    show rin 3 sm light pyjama glasses d with dict_dissolve_25

    voice "RIN_0591"
    rin "\"I dunno. Asou always goes home every other Sunday. She was gone the week before last too, right?\""

    show hina 3 sm light pyjama j with dict_dissolve_25

    voice "HIN_0761"
    hina "\"I know, but I still miss her!\""

    show rin 3 sm light pyjama glasses c with dict_dissolve_25

    voice "RIN_0592"
    rin "\"What a baby. Why don't you just hug Rapha until she comes back?\""

    show hina 3 sm light pyjama f with dict_dissolve_25

    voice "HIN_0762"
    hina "\"Ugh...\""

    show rin 3 sm light pyjama glasses i with dict_dissolve_25

    voice "RIN_0593"
    rin "\"And I'll hug you, and then we'll all be good♪\""

    show hina 3 sm light pyjama j with dict_dissolve_25

    voice "HIN_0763"
    hina "\"What'll be good? ...{i}Achoo!{/i}\""

    show rin 3 sm light pyjama glasses f with dict_dissolve_25

    voice "RIN_0594"
    rin "\"Oh? Not over your cold yet?\""

    play sound se116a

    hide rin
    with Dissolve(0.25)

    "Rin put her book down and sat up."

    show hina 3 sm light pyjama b with dict_dissolve_25

    voice "HIN_0764"
    hina "\"It's nothing serious.\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "RIN_0595"
    rin "\"You're sneezing. You should take it easy today.\""

    show hina 3 sm light pyjama h with dict_dissolve_25

    voice "HIN_0765"
    hina "\"It's fine. Don't worry about it. It's just a dust allerg... {i}achoo!{/i}\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "RIN_0596"
    rin "\"We got rid of all the dust yesterday, didn't we?\""

    "Rin climbed down from her bunk."

    show hina 3 sm light pyjama g with dict_dissolve_25

    voice "HIN_0766"
    hina "\"Aaah, see, 'cause you just moved, there's all this invisible dust in the air!\""

    show rin 1 sm pyjama glasses g behind hina with dict_dissolve_25

    voice "RIN_0597"
    rin "\"If it's invisible, how do you know it's there?\""

    show hina 3 sm light pyjama e with dict_dissolve_25

    voice "HIN_0767"
    hina "\"Okay, I'm gonna get some fresh air in here!\""

    play sound se118b

    hide hina
    with Dissolve(0.25)

    "Hina jumped past Rin and off the bed."

    show rin:
        "rin 1 sm pyjama glasses e" with Dissolve(0.25)
        ShakeJump

    voice "RIN_0598"
    rin "\"Ah, hey—\""

    hide rin
    with Dissolve(0.25)

    scene black with bg_effect_12_250
    pause 0.25
    scene bg01aa with bg_effect_12_250
    pause 0.25

    play sound se000b

    pause 0.5

    play sound se041a_100 fadein 0.5

    show hina 1 lg pyjama l at pos_l with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "HIN_0768"
    hina "\"Hyah!!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg pyjama glasses j flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    pause 0.5

    show rin 1 lg pyjama glasses j:
        alpha 1.0 xcenter 852
        ShakeSide

    voice "RIN_0599"
    rin "\"Ugh, that's cold!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    stop sound2 fadeout 2.0

    "A chilly wind blew in, ruffling their bangs."

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0600"
    rin "\"Don't do that. You'll make your cold worse.\""

    show hina 1 lg pyjama h with dict_dissolve_25

    voice "HIN_0769"
    hina "\"I don't have a cold.\""

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0601"
    rin "\"...What are you trying to prove here?\""

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0770"
    hina "\"...Well, I don't want Fumi to worry. She thinks it's her fault.\""

    show rin 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0602"
    rin "\"What do you mean?\""

    show hina 1 lg pyjama n with dict_dissolve_25

    voice "HIN_0771"
    hina "\"The two of us went up to the roof to look at the stars on my birthday. I probably caught it then.\""

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0603"
    rin "\"What, dressed like that? It was really cold that day, wasn't it?\""

    show hina:
        ShakeYes

    "Hina nodded and Rin sighed."

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses g with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0604"
    rin "\"...But it's not like that would make it Asou's fault.\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0772"
    hina "\"I know! But still—\""

    play sound se041a_100 fadein 0.5

    "Another gust of wind battered the room. The pages of Fumi's diary flapped atop her desk."

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0773"
    hina "\"Oh, it's gonna blow away!\""

    show hina:
        "hina 1 lg pyjama l flat"
        alpha 1.0 xcenter 252 xoffset 0 yoffset 0
        easeout 0.5 alpha 0.0 xcenter 352
    pause 0.5

    hide hina with None

    "Hina rushed over to Fumi's desk."

    stop sound fadeout 2.0

    show rin:
        "rin 1 lg pyjama glasses a" with Dissolve(0.25)
        xcenter 852
        easein 0.5 xcenter 512

    voice "RIN_0605"
    rin "\"Wouldn't it be faster to close the window?\""

    show rin 1 lg pyjama glasses a:
        xcenter 512
    with None

    "She was right, but Hina didn't seem to hear her."

    play sound se530

    show rin:
        xcenter 512
        easein 0.5 xcenter 252
    show hina 1 lg pyjama k at pos_r with Dissolve(0.25)

    voice "HIN_0774"
    hina "\"...Whoa!\""

    show rin 1 lg pyjama glasses a at pos_l with None

    "Hina arrived at the desk just in time to hold down the pages the feather was in between."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0775"
    hina "\"There we go—\""

    stop music fadeout 3.0

    "She stopped, just as she was about to close the diary."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0776"
    hina "\"...This is... about me.\""

    scene white with Dissolve(0.5)
    pause 0.5
    scene bg08aa with Dissolve(0.75)
    pause 1.25

    play music bgm05

    voice "FUM_0572"
    fumi "{i}Hina told me it was okay to believe in angels today.{/i}" (what_first_indent=24, show_name=False)

    voice "FUM_0573"
    fumi "{i}She said it was impressive to believe in something for so long. But it was starting to get hard.{/i}" (what_first_indent=24, show_name=False)

    voice "FUM_0574"
    fumi "{i}Angels do exist. But no matter how many times I assert it, I still feel insecure. I don't know anymore whether I'm trying to convince other people, or just keep fooling myself.{/i}" (what_first_indent=24, show_name=False)

    voice "FUM_0575"
    fumi "{i}I've been all alone, clinging to an old memory with no proof. So I was all the more insistent when I found that feather.{/i}" (what_first_indent=24, show_name=False)

    voice "FUM_0576"
    fumi "{i}But today, Hina said we could believe together.{/i}" (what_first_indent=24, show_name=False)

    voice "FUM_0577"
    fumi "{i}I was so happy. How does she understand me so well?{/i}" (what_first_indent=24, show_name=False)

    voice "FUM_0578"
    fumi "{i}I don't have to stop believing. I can keep believing in angels forever, with Hina.{/i}" (what_first_indent=24, show_name=False)

    scene white with Dissolve(0.5)
    pause 0.5
    scene bg01aa with Dissolve(0.75)
    pause 0.75

    show hina 2 lg pyjama i at pos_r with Dissolve(0.25)

    voice "HIN_0777"
    hina "\"Fumi...\""

    show rin 1 lg pyjama glasses a at pos_l with dict_dissolve_25

    voice "RIN_0606"
    rin "\"Hey, reading somebody's diary is in pretty poor taste.\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0778"
    hina "\"Oh... y-yeah.\""

    play sound se041a_120 fadein 0.5

    show hina 1 lg pyjama l
    show rin 1 lg pyjama glasses e
    with Dissolve(0.25)

    show hina:
        ShakeJump

    $ voice2("hina","HIN_0779","rin","RIN_0607")
    hina_rin "\"Ah!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "An even stronger gust suddenly blew through the room, sending the feather on top of the pages tumbling into the air."

    "The two girls watched the feather flutter about the room."

    show hina:
        ShakeSide

    $ voice2("hina","HIN_0780","rin","RIN_0608")
    hina_rin "\"Aah!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    stop sound fadeout 2.0

    "In the next instant, the wind pulled back, tugging the feather out the window."

    show hina 1 lg pyjama f with Dissolve(0.25)

    $ renpy.sound.set_volume(1.0)
    play sound se133b

    show hina:
        "hina 1 lg pyjama f flat"
        alpha 1.0 xcenter 772
        easeout 0.25 alpha 0.0 xcenter 672

    voice "HIN_0781"
    hina "\"Hey, wait!\""

    hide hina with None

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 172

    voice "RIN_0609"
    rin "\"Huh? Wait, Hina?!\""

    show rin 1 lg pyjama glasses j at pos_l2 with None

    "And just like that, Hina's foot was on the window sill."

    show rin:
        ShakeJump
        ShakeJump

    voice "RIN_0610"
    rin "\"Hina, you're barefoot! And we're on the second floor!!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0782"
    hina "\"Fumi's feather!!\""

    play sound se118c

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    "Hina was in the air before Rin could even put a hand on her shoulder to stop her."

    "She grabbed a branch on a nearby tree and swung over to the roof next door."

    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0783"
    hina "\"Waaait!!\""

    "Leaving behind a dumbfounded Rin, Hina jumped from roof to roof, chasing the feather."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0611"
    rin "\"...Maybe she does have wings.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou1_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
