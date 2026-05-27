label a10_cou3_09:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    "—The manager's room."

    scene bg09ba with Dissolve(0.5)
    pause 1.5

    show hina z4 1 lg school a
    show miyako z4 2 lg school a:
        xcenter 172
    show sachiko z4 1 lg outfit a:
        xcenter 852
    with Dissolve(0.25)

    voice "2MI_1056"
    miyako "\"Did you two know?\"" id a10_cou3_09_623b826a

    "Miyako asked, face blank."

    show hina:
        ShakeYes

    voice "2HI_1588"
    hina "\"Yeah, I guess.\"" id a10_cou3_09_040b6060

    show hina:
        xoffset 0 yoffset 0
    with None

    if routes_cleared >= 2:
        jump a10_cou3_09_a
    else:
        jump a10_cou3_09_b

label a10_cou3_09_a:

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1589"
    hina "\"Wait, why are you here, Miyako?\"" id a10_cou3_09_a_609cceff

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_1057"
    miyako "\"Well, because—\"" id a10_cou3_09_a_03108e0a

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0876"
    sachiko "\"Oh, just some Takaoka business...\"" id a10_cou3_09_a_33d46ac1

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1590"
    hina "\"Alright...\"" id a10_cou3_09_a_bcc563f1

    "Hina went on without pursuing the matter."

    jump a10_cou3_09_b

label a10_cou3_09_b:

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_1591"
    hina "\"I mean, Asou said from the start that she wasn't going to audition, right?\"" id a10_cou3_09_b_4967b068

    "Hina shot a look at her accomplice."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0877"
    sachiko "\"I just thought it'd be fun, so I told her she should go, just to do it. But she said the TV appearance was enough for her.\"" id a10_cou3_09_b_32aedb11

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1592"
    hina "\"But the biggest reason she didn't want to was because it'd mean she'd get less time with Rin.\"" id a10_cou3_09_b_138da888

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_1058"
    miyako "\"I see. That's very like Fumi.\"" id a10_cou3_09_b_4a43ee6b

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0878"
    sachiko "\"But she stressed about it a little.\"" id a10_cou3_09_b_e6cc6d02

    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_1059"
    miyako "\"Mm~ About how she was worried she was spoiling Rin too much and ruining her?\"" id a10_cou3_09_b_b3c5bdc4

    show hina z4 1 lg school f
    show sachiko z4 2 lg outfit b
    with dict_dissolve_25

    $ voice2("hina","2HI_1593","sachiko","2SA_0879")


    hina_sachiko "\"Yeah, that!\""

    "She's sharp."

    show hina z4 1 lg school e with dict_dissolve_25

    voice "2HI_1594"
    hina "\"That's why when Asou asked me about it, I gave her a suggestion.\"" id a10_cou3_09_b_9848ce97

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0880"
    sachiko "\"To keep it a secret that she wasn't going to go to the audition and put a little distance between herself and Rin.\"" id a10_cou3_09_b_183d1834

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1595"
    hina "\"Right. And that might spur Rin to act.\"" id a10_cou3_09_b_ce89d3a1

    show miyako z4 1 lg school_b b with dict_dissolve_25

    voice "2MI_1060"
    miyako "\"And it worked like a charm.\"" id a10_cou3_09_b_c9ca8bce

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0881"
    sachiko "\"It wasn't that easy, though. Rin's simple enough, so she behaved pretty much exactly as we planned.\"" id a10_cou3_09_b_8460d117

    show hina:
        "hina z4 1 lg school n" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_1596"
    hina "\"But Asou was the one who really missed Rin. It was getting to be too much for her. We decided Valentine's Day was probably the longest we could push it.\"" id a10_cou3_09_b_7003d8f2

    show hina z4 1 lg school n:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_1061"
    miyako "\"Ah~\"" id a10_cou3_09_b_9fbc6fa3

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0882"
    sachiko "\"Then her mom collapsed and it got a bit complicated at the end.\"" id a10_cou3_09_b_1b758a09

    show miyako z4 1 lg school_a i with dict_dissolve_25

    voice "2MI_1062"
    miyako "\"I see. So that's what was going on...\"" id a10_cou3_09_b_a7f8738f

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0883"
    sachiko "\"Rin got it into her head that Fumi was going to be an idol, so she didn't want to get in her way, but Fumi was worried about ruining Rin's potential by spoiling her.\"" id a10_cou3_09_b_b854c06f

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_1597"
    hina "\"So Asou and Rin were basically feeling the same way about each other.\"" id a10_cou3_09_b_d623ffa9

    "Reminds me of \"The Gift of the Magi.\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1063"
    miyako "\"That's pretty incredible, though. That everything went just as you planned? How were you able to plan everything so carefully?\"" id a10_cou3_09_b_3a660ad8

    show hina z4 2 lg school f
    show sachiko z4 2 lg outfit b
    with dict_dissolve_25

    $ voice2("hina","2HI_1598","sachiko","2SA_0884N")
    hina_sachiko "\"'Cause we're not involved.\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1064"
    miyako "\"Huh?\"" id a10_cou3_09_b_67641798

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0885"
    sachiko "\"I mean, I don't mean that in a cold way. When you're on the outside looking in, sometimes things are way more obvious to you.\"" id a10_cou3_09_b_4afa1229

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1599"
    hina "\"Right. They think they're facing the end of the world, but to us, it just looks like they're bragging about their girlfriend.\"" id a10_cou3_09_b_5fd9f6c7

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0886"
    sachiko "\"It was a lot easier for us to find a solution than it would have been for them.\"" id a10_cou3_09_b_ffb1fd2e

    "Hina and Sachiko smiled, completely unconcerned."

    show miyako:
        "miyako z4 1 lg school_b g" with Dissolve(0.25)
        3.5
        "miyako z4 1 lg school_b c" with Dissolve(0.25)

    voice "2MI_1065"
    miyako "\"Is that how it is...? No, you might be right.\"" id a10_cou3_09_b_389c993b

    show miyako z4 1 lg school_b c:
        pass
    with None

    "Miyako was probably thinking about what she had seen when she was an angel."

    if routes_cleared >= 2:
        jump a10_cou3_09_c
    else:
        jump a10_cou3_09_d

label a10_cou3_09_c:

    "—On the outside looking in. Everyone's the same in this world. It's the same for you and for me too, of course."

    jump a10_cou3_09_end

label a10_cou3_09_d:

    "—On the outside looking in. Everyone's the same in this world. It's the same for you too, of course."

label a10_cou3_09_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
