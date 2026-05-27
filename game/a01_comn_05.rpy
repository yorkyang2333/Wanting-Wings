label a01_comn_05:

    scene bg01ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show fumi 2 lg pyjama c at pos_r
    show hina 1 lg pyjama a at pos_l
    with Dissolve(0.25)

    show fumi:
        ShakeYes

    play sound se009c

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "FUM_0061"
    fumi "\"Here you are. It might be a little hot still, so you should blow on it.\"" id a01_comn_05_275bd1f0

    "Steam wafted from the mug Fumi handed Hina."

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0076"
    hina "\"Thanks. I'm real sensitive to hot food. It's a pain.\"" id a01_comn_05_b200fba8

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0062"
    fumi "\"I'm the same way. Let's wait until they cool down.\"" id a01_comn_05_915fabda

    show hina 1 lg pyjama h with dict_dissolve_25

    voice "HIN_0077"
    hina "\"I like my baths hot, though~\"" id a01_comn_05_3359e782

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0063"
    fumi "\"Oh, I like my baths a little cool, too.\"" id a01_comn_05_e171a9fa

    play sound se521

    $ side_image = "rin 1 side pyjama a"

    voice "RIN_0078"
    rin "\"I'm back.\"" id a01_comn_05_75aa3721

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0078"
    hina "\"Hey. Where'd you go? You weren't taking a bath, right?\"" id a01_comn_05_da3ee4fb

    $ side_image = "rin 1 side pyjama b"

    voice "RIN_0079"
    rin "\"I couldn't even wash my bangs in five minutes. I'm not you.\"" id a01_comn_05_8bd1cb3b

    show hina:
        "hina 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0079"
    hina "\"It takes me longer than that! I'm not bald!\"" id a01_comn_05_2a377b5c

    show hina 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None

    $ side_image = "rin 1 side pyjama c"

    voice "RIN_0080"
    rin "\"I'm really rooting for your team, you know.\"" id a01_comn_05_97da867e

    show hina 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0080"
    hina "\"Enough about the baseball.\"" id a01_comn_05_7dd4e76e

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0064"
    fumi "\"Here, let me make you some too, Ogata. Upsy-daisy...\"" id a01_comn_05_ed5f2272

    show fumi:
        "fumi 2 lg pyjama b flat"
        alpha 1.0 xcenter 772
        easeout 0.5 alpha 0.0 xcenter 872
    pause 0.5
    hide fumi with None

    show rin behind hina at pos_r:
        "rin 1 lg pyjama a flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772

    "Fumi stood up and headed to the kitchen as Rin entered the living room in her place."

    show rin 1 lg pyjama a at pos_r:
        alpha 1.0 xcenter 772
    with None

    voice "RIN_0081"
    rin "\"'Upsy-daisy,' huh...?\"" id a01_comn_05_860a5398

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0081"
    hina "\"Eheheh. She kinda sounds like an old lady sometimes, doesn't she?\"" id a01_comn_05_24ede3b9

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0082"
    rin "\"Maybe she's drinking kelp tea or something.\"" id a01_comn_05_dab390a9

    "Rin picked up Fumi's mug and sniffed it."

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0082"
    hina "\"I feel like she should be drinking herbal tea.\"" id a01_comn_05_fe905f02

    show rin 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0083"
    rin "\"Yeah. And what's widdle baby Hina drinking? Warm milk?\"" id a01_comn_05_14f4dcf1

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0083"
    hina "\"I-It's coffee.\"" id a01_comn_05_ee180968

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0084"
    rin "\"......\"" id a01_comn_05_c9c3ebb9

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0084"
    hina "\"C-Café au lait.\"" id a01_comn_05_b382a264

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0085"
    rin "\"If the ratio's 1:9, it's not café au lait anymore.\"" id a01_comn_05_28c10fb3

    show hina 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0085"
    hina "\"Well, if there's too much coffee, it'll be bitter, and I won't be able to sleep.\"" id a01_comn_05_a92e317d

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0086"
    rin "\"Then why are you drinking it?\"" id a01_comn_05_1a4f480a

    show hina 1 lg pyjama h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0086"
    hina "\"Well, {i}you{/i} drink it. And it feels grown-up...\"" id a01_comn_05_a9cb90fd

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0087"
    rin "\"Are you a kid? Are you a little baby?\"" id a01_comn_05_a93f3383

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2


    show hina z3 1 lg pyjama h at pos_l2
    show fumi at pos_r2:
        "fumi z3 1 lg pyjama c flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    show rin z3 1 lg pyjama b behind hina, fumi at default
    with Dissolve(0.25)

    play sound se009c

    voice "FUM_0065"
    fumi "\"Here you are.\"" id a01_comn_05_93b9b7fe

    show fumi z3 1 lg pyjama c at pos_r2
    with None

    show rin z3 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0088"
    rin "\"Thanks.\"" id a01_comn_05_982f8aae

    "Rin brought the mug straight to her mouth after taking it from Fumi."

    voice "RIN_0089"
    rin "\"Mmm. You make some really good coffee, Asou. Hm? What's up?\"" id a01_comn_05_c5781e5c

    "Rin noticed Fumi and Hina watching her."

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0066"
    fumi "\"You're not worried about burning your tongue at all, are you?\"" id a01_comn_05_b0c1e288

    show hina z3 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0087"
    hina "\"And you drink it black.\"" id a01_comn_05_2e1e9da9

    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0090"
    rin "\"Black as the devil, hot as hell.\"" id a01_comn_05_6e18f46d

    show hina z3 1 lg pyjama k
    show fumi 1 lg pyjama e
    with dict_dissolve_25

    $ voice2("hina","HIN_0088","fumi","FUM_0067")
    hina_fumi "\"??\""

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0091"
    rin "\"What good coffee should be. Someone said that once.\"" id a01_comn_05_af5d65cd

    show hina z3 1 lg pyjama l
    show fumi 1 lg pyjama b
    with dict_dissolve_25

    $ voice2("hina","HIN_0089","fumi","FUM_0068")
    hina_fumi "\"Huh~\""


    if route1 == 3:

        scene black
        with bg_effect_05
        pause 0.5

        jump a01_comn_05_end
    else:


        python:
            _last_say_what = ""
            _last_say_who = None
            renpy.choice_for_skipping()

        stop music fadeout 2.0

        scene black
        with Dissolve(0.5)
        pause 1.5

        scene select_back with Dissolve(0.5)
        pause 1.5


        menu:
            "カメラ"((196, 485), "menu/btn_select_0101"):
                $ hina_fumi_score += 1
                jump a01_comn_05_a
            "包み"((400, 297), "menu/btn_select_0102"):
                $ rin_hina_score += 1
                jump a01_comn_05_b

label a01_comn_05_a:

    play music bgm01

    scene white with Dissolve(0.75)
    pause 0.75
    scene ev01a with bg_effect_25
    pause 0.5

    voice "FUM_0069"
    fumi "\"You always look like you're having fun when you've got that camera in your hands, Natsume.\"" id a01_comn_05_a_63de2792

    scene ev01b with Dissolve(0.5)

    voice "HIN_0090"
    hina "\"Yeah. I've always felt calm holding it.\"" id a01_comn_05_a_e6f263d7

    voice "FUM_0070"
    fumi "\"Your father's a photographer, right?\"" id a01_comn_05_a_1622a77b

    voice "HIN_0091"
    hina "\"Yep. He's a nature photographer, so he takes pictures of flowers and trees and stuff.\"" id a01_comn_05_a_2b735fca

    voice "FUM_0071"
    fumi "\"Do you like nature photography too?\"" id a01_comn_05_a_c717f8a5

    voice "HIN_0092"
    hina "\"I wouldn't say I've got a preference. I take pictures of whatever I feel like.\"" id a01_comn_05_a_e0fa088e

    voice "FUM_0072"
    fumi "\"It does seem that way.\"" id a01_comn_05_a_40cc0b5f

    "There were a variety of pictures up around Hina's desk: of people, scenery, and still lifes."

    scene ev01c with Dissolve(0.5)

    voice "RIN_0092"
    rin "\"Why are you still using a film camera? Isn't it a waste paying to have them developed?\"" id a01_comn_05_a_1ebc478a

    voice "HIN_0093"
    hina "\"Nope, it's free. I get my dad to do it.\"" id a01_comn_05_a_b095600f

    voice "RIN_0093"
    rin "\"It's inconvenient not knowing how they came out until they're developed, though, isn't it? Why don't you just use your phone?\"" id a01_comn_05_a_1be3c610

    voice "HIN_0094"
    hina "\"Because! There's a certain feeling you can only get with film cameras.\"" id a01_comn_05_a_0e156e9a

    voice "RIN_0094"
    rin "\"Feeling, eh? But your pictures are kinda...\"" id a01_comn_05_a_428e8d47

    voice "HIN_0095"
    hina "\"What?\"" id a01_comn_05_a_f906c183

    voice "RIN_0095"
    rin "\"Aren't they usually kinda unfocused? And the corners are always weird. Are you getting your finger in front of the lens 'cause the camera's too small?\"" id a01_comn_05_a_70f9be24

    voice "HIN_0096"
    hina "\"No! That's just how toy camera pictures look!\"" id a01_comn_05_a_c3549fac

    voice "RIN_0096"
    rin "\"Huh? Really?\"" id a01_comn_05_a_0c182466

    scene ev01f with Dissolve(0.5)

    voice "FUM_0073"
    fumi "\"Is that right?\"" id a01_comn_05_a_5e73095c

    voice "HIN_0097"
    hina "\"You too, Asou?\"" id a01_comn_05_a_edac571b

    voice "FUM_0074"
    fumi "\"I-I'm sorry.\"" id a01_comn_05_a_ab069221

    voice "HIN_0098"
    hina "\"Listen, toy cameras are—\"" id a01_comn_05_a_412f18c8

    voice "RIN_0097"
    rin "\"Like cameras for kids, right?\"" id a01_comn_05_a_2ffc394e

    voice "HIN_0099"
    hina "\"Let me explain!\"" id a01_comn_05_a_72fd6643

    voice "HIN_0100"
    hina "\"They're made more simply than regular cameras, but the distortions and blur and tint and all that make the pictures interesting and unique.\"" id a01_comn_05_a_79024651

    voice "RIN_0098"
    rin "\"Huh. I just thought you sucked.\"" id a01_comn_05_a_02e26166

    voice "HIN_0101"
    hina "\"Are you trying to pick a fight with me?\"" id a01_comn_05_a_221193c8

    scene ev01c with Dissolve(0.5)

    voice "FUM_0075"
    fumi "\"I like your pictures, Natsume. I think they're very unique and cute.\"" id a01_comn_05_a_7a9bc3bd

    voice "HIN_0102"
    hina "\"See? Asou gets it!\"" id a01_comn_05_a_1f39492e

    voice "RIN_0099"
    rin "\"'Unique' is such a convenient word, don't you think?\"" id a01_comn_05_a_2b4fea3d

    voice "HIN_0103"
    hina "\"I'm not taking your picture anymore, Rin!\"" id a01_comn_05_a_32160454

    jump a01_comn_05_end

label a01_comn_05_b:

    play music bgm01

    scene white with Dissolve(0.75)
    pause 0.75
    scene ev01a with bg_effect_25
    pause 0.5

    voice "HIN_0104"
    hina "\"Oh, Rin, what's that?\"" id a01_comn_05_b_48aefa5e

    "Hina was pointing at the package on Rin's desk—the thing she'd furtively accepted from Sachiko earlier."

    voice "RIN_0100"
    rin "\"I'll give you three choices, then. If you get it right, I'll give it to you.\"" id a01_comn_05_b_d7ead510

    voice "HIN_0105"
    hina "\"Huh? Seriously?\"" id a01_comn_05_b_85a245a8

    voice "RIN_0101"
    rin "\"1. My allowance.\n2. A super difficult book.\n3. A brick.\"" id a01_comn_05_b_ae8c1e9e

    scene ev01f with Dissolve(0.5)

    voice "FUM_0076"
    fumi "\"#3 would be pretty scary.\"" id a01_comn_05_b_0a5c43ea

    voice "RIN_0102"
    rin "\"Is 3 your final answer, Asou?\"" id a01_comn_05_b_4eabb161

    voice "FUM_0077"
    fumi "\"Huh? Huh?\"" id a01_comn_05_b_fce65047

    voice "HIN_0106"
    hina "\"What would I want a brick for?\"" id a01_comn_05_b_56369e24

    voice "RIN_0103"
    rin "\"Build your house with 'em and you'll be safe from wolves.\"" id a01_comn_05_b_f701ce14

    "The Three Little Pigs?"

    voice "HIN_0107"
    hina "\"I won't have that problem!\"" id a01_comn_05_b_016996a8

    voice "FUM_0078"
    fumi "\"Well, I don't think she'd be giving you an allowance.\"" id a01_comn_05_b_9518f222

    voice "RIN_0104"
    rin "\"Who knows?\"" id a01_comn_05_b_e492d79d

    voice "HIN_0108"
    hina "\"It's gotta be #2! I don't want a difficult book...\"" id a01_comn_05_b_7e47f987

    voice "RIN_0105"
    rin "\"And the answer is...! Dodododododododo...\"" id a01_comn_05_b_a1da4cb6

    voice "HIN_0109"
    hina "\"Enough with the drum roll!\"" id a01_comn_05_b_06e4ea62

    voice "RIN_0106"
    rin "\"It's #2, a difficult book!\"" id a01_comn_05_b_63f95e37

    voice "HIN_0110"
    hina "\"Bah, what a stupid quiz!\"" id a01_comn_05_b_e8260247

    jump a01_comn_05_end

label a01_comn_05_end:

    scene black with Dissolve(0.75)
    pause 0.75

    if route1 == 3:
        scene bg01ca with bg_effect_05
        pause 0.5
    else:
        scene bg01ca with Dissolve(0.75)
        pause 0.75

    show hina z3 1 lg pyjama a at pos_l2
    show fumi z3 1 lg pyjama a at pos_r2
    show rin z3 1 lg pyjama k behind hina, fumi at default
    with Dissolve(0.25)

    voice "FUM_0079"
    fumi "\"I think I'll have another cup.\"" id a01_comn_05_end_20defb53

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0107"
    rin "\"Oh, can you make me another cup of coffee, too?\"" id a01_comn_05_end_ea55f934

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0080"
    fumi "\"Sure. Natsume?\"" id a01_comn_05_end_4bbf49c2

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0111"
    hina "\"Umm, I'll have a café au lait, hold the coffee.\"" id a01_comn_05_end_8e600bbf

    show rin z3 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0108"
    rin "\"That's 100%% pure milk.\"" id a01_comn_05_end_4fc8c3bf

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0081"
    fumi "\"Eheh. Let me repeat your orders, then. One black coffee and one warm milk. Is that right?\"" id a01_comn_05_end_eb8d1e59

    show hina z3 1 lg pyjama c
    show rin z3 1 lg pyjama c
    with dict_dissolve_25

    $ voice2("hina","HIN_0112","rin","RIN_0109")
    hina_rin "\"Yeees.\""

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0082"
    fumi "\"Very well. I'll be right back with those. Upsy-daisy...\"" id a01_comn_05_end_64caa0d1

    show fumi:
        "fumi z3 2 lg pyjama c flat"
        alpha 1.0 xcenter 852
        easeout 0.5 alpha 0.0 xcenter 952
    pause 0.7
    hide fumi with None


    show hina:
        "hina z3 1 lg pyjama a" with Dissolve(0.25)
        pos_l2_z3
        easein 0.25 pos_l

    show rin:
        "rin z3 1 lg pyjama a" with Dissolve(0.25)
        easein 0.25 pos_r

    pause 0.25

    show hina z3 1 lg pyjama a at pos_l with None
    show rin z3 1 lg pyjama a at pos_r:
        ShakeYes

    voice "RIN_0110"
    rin "\"Guess I'll keep reading... hmm?\"" id a01_comn_05_end_9146d9f2

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0113"
    hina "\"Your glasses again? Did you check the top of your head?\"" id a01_comn_05_end_919e9177

    show rin z3 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0111"
    rin "\"First thing.\"" id a01_comn_05_end_4cf573f8

    "Rin said, a hand pawing at her head."

    show hina z3 1 lg pyjama h with dict_dissolve_25

    voice "HIN_0114"
    hina "\"You leave them all over the place. Are they in your bag?\"" id a01_comn_05_end_227cfcb3

    show rin:
        "rin z3 1 lg pyjama b" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0112"
    rin "\"...No.\"" id a01_comn_05_end_ed6f2a07

    show rin z3 1 lg pyjama b:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0115"
    hina "\"In your desk?\"" id a01_comn_05_end_def92586

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0113"
    rin "\"...No.\"" id a01_comn_05_end_b39b3237

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0116"
    hina "\"Gonna keep looking?\"" id a01_comn_05_end_e8ac0397

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0114"
    rin "\"...Well, I'm not gonna dance with you.\"" id a01_comn_05_end_2d3102a5

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0117"
    hina "\"Nyahahaha.\"" id a01_comn_05_end_41e52358

    $ side_image = "fumi 1 side pyjama d"

    voice "FUM_0083"
    fumi "\"Umm~\"" id a01_comn_05_end_bdbd00c7

    "Fumi's voice came from the kitchen."

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0118"
    hina "\"What is it?\"" id a01_comn_05_end_574f982e

    $ side_image = "fumi 1 side pyjama d"

    voice "FUM_0084"
    fumi "\"I opened the fridge to get the milk and found...\"" id a01_comn_05_end_b115fdd6

    "Fumi held out, pinched between her fingers, ice-cold—"

    show rin z3 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0115"
    rin "\"My glasses.\"" id a01_comn_05_end_db622d54

    show hina:
        "hina z3 1 lg pyjama g" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0119"
    hina "\"Why?!\"" id a01_comn_05_end_b5da5b88

    show hina z3 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None

    play sound se403a

    stop music fadeout 1.0

    scene black with Dissolve(0.25)
    pause 0.25

    $ side_image = "rin 1 side pyjama glasses j"

    voice "RIN_0116"
    rin "\"Cold! Cloudy!\"" id a01_comn_05_end_29aeb984

    window hide

    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause 2.0


    if route1 == 3:
        jump a01_cou3_02
    else:
        jump a01_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
