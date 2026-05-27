label a01_comn_02:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm01




    show fumi z3 1 lg school d at pos_l2_z3
    show rin z3 1 lg school a at pos_r2_z3
    show hina z3 1 lg school a at default
    with Dissolve(0.25)

    voice "FUM_0021"
    fumi "\"We cut it a little close this morning, didn't we?\"" id a01_comn_02_f5ae7a11

    play sound se116a

    "Fumi smiled awkwardly as she opened up her lunch."

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0025"
    if persistent.dpatch:
        hina "\"You said it. If we were one minute later, our dash to the bus would've ended up being a run to school.\"" id a01_comn_02_832fece7
    else:
        hina "\"You said it. If we were one minute later, our dash to the bus would've ended up being a run to class.\"" id a01_comn_02_7a8616b2

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0030"
    rin "\"You could've just left without me.\"" id a01_comn_02_18bb5e43

    show hina 1 lg school e
    show fumi 1 lg school a
    with dict_dissolve_25

    voice "HIN_0026"
    if persistent.dpatch:
        hina "\"Uhh, if we did that, you'd just skip school.\"" id a01_comn_02_5c6bec90
    else:
        hina "\"Uhh, if we did that, you'd just skip class.\"" id a01_comn_02_0010ecaa

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0031"
    rin "\"Hahaha, that's ridiculous.\"" id a01_comn_02_3fd8a08e

    show hina 1 lg school j with dict_dissolve_25

    voice "HIN_0027"
    hina "\"Uh huh...\"" id a01_comn_02_38ee98aa

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0022"
    fumi "\"...It's happened before.\"" id a01_comn_02_a566fffd

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0032"
    rin "\"Just the once, though...\"" id a01_comn_02_e390d681

    show fumi 1 lg school g with dict_dissolve_25


    $ voice2("hina","HIN_0028","fumi","FUM_0023")
    hina_fumi "\"Uh huh...\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0033"
    rin "\"Was it... twice?\"" id a01_comn_02_f9f6b3db

    show hina:
        "hina z3 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0029"
    hina "\"Five times!\"" id a01_comn_02_55324717

    show hina z3 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0034"
    rin "\"Man, it's already lunch. I sure am hungry.\"" id a01_comn_02_f2e92554

    show hina 1 lg school f with dict_dissolve_25

    voice "HIN_0030"
    hina "\"You little—!\"" id a01_comn_02_e57a1d47

    show fumi 1 lg school c with dict_dissolve_25

    voice "FUM_0024"
    fumi "\"Ahaha. We should eat.\"" id a01_comn_02_229bee91

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_0031"
    hina "\"You're hungry 'cause you don't eat breakfast.\"" id a01_comn_02_3dc6e9da

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0035"
    rin "\"Yeah, that's not happening. Who can put food in their stomach right after waking up?\"" id a01_comn_02_7c700126

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_0032"
    hina "\"Asou makes really good breakfast, you know.\"" id a01_comn_02_97b00d5c

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0036"
    rin "\"I know that even without eating it. But I really can't eat in the morning.\"" id a01_comn_02_7e9b8897

    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_0025"
    fumi "\"Umm, should I get some stuff that's easy to eat, like cereal or oatmeal?\"" id a01_comn_02_e34665a8

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0033"
    hina "\"You don't need to baby her, Asou. Even if you made her something, she'd still stay in bed until the last minute.\"" id a01_comn_02_fed21bf9

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0037"
    rin "\"I suppose it's a question of whether you could gain more energy by eating breakfast or save more energy spending that time sleeping.\"" id a01_comn_02_4382f3ef

    show fumi 1 lg school d
    show hina 1 lg school f
    with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "HIN_0034"
    hina "\"Ah~! It's nothing but hypotheticals with you, isn't it?! Why don't you put yourself in the shoes of the people who have to run around after breakfast every day because of you?!\"" id a01_comn_02_e1e6c590

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school k with dict_dissolve_25

    voice "RIN_0038"
    rin "\"Now, what do I have to eat today~?\"" id a01_comn_02_52bc22e9

    play sound se116a

    "Unfazed, Rin opened her lunch."

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0035"
    hina "\"...Haah. I'll eat, too.\"" id a01_comn_02_66130c2e

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show fumi 2 lg school b at pos_l
    show rin 1 lg school c at pos_r
    with Dissolve(0.25)

    play sound se555

    voice "RIN_0039"
    if persistent.dpatch:
        rin "\"Ooh, it looks good again today. I only make it to school every day because I have a lunch from my loving wife to look forward to.\"" id a01_comn_02_b4a7a66a
    else:
        rin "\"Ooh, it looks good again today. I only make it to class every day because I have a lunch from my loving wife to look forward to.\"" id a01_comn_02_57423e1b

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0026"
    fumi "\"If it makes my husband happy, it makes me happy, too.\"" id a01_comn_02_c6b6876a

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0040"
    rin "\"There are parts of it that are disturbingly colorful, however.\"" id a01_comn_02_0e9aa4ab

    show fumi 1 lg school b with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "FUM_0027"
    fumi "\"Those would be peppers and carrots.\"" id a01_comn_02_13bad09c

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg school i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0041"
    rin "\"Ugh...\"" id a01_comn_02_68764237

    show rin 1 lg school i:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0028"
    fumi "\"You can't be picky. If I didn't make you, you wouldn't eat any vegetables at all, would you, Ogata?\"" id a01_comn_02_85d92f07

    $ side_image = "hina 1 side school d"

    voice "HIN_0036"
    hina "\"Huh? Huh?\"" id a01_comn_02_64c1ee6a

    play sound se557b

    "Hina was turning her bag inside out."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0029"
    fumi "\"What's wrong?\"" id a01_comn_02_764d2c7e

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show fumi 2 lg school d at pos_l2
    show rin 1 lg school a at pos_r2
    show hina 1 lg school l
    with Dissolve(0.25)

    voice "HIN_0037"
    hina "\"...My lunch... I don't have it.\"" id a01_comn_02_56267064

    show fumi 1 lg school e with dict_dissolve_25

    voice "FUM_0030"
    fumi "\"What?\"" id a01_comn_02_493f92c0

    show rin 1 lg school k with dict_dissolve_25

    voice "RIN_0042"
    rin "\"You're such a scatterbrain, Hina.\"" id a01_comn_02_8febf8f6

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0038"
    hina "\"It's because of all the chaos this morning! This is all your fault, Rin!\"" id a01_comn_02_5eb7aa6e

    show hina 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0043"
    rin "\"Yeesh. Shifting the blame is low.\"" id a01_comn_02_39bdead1

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show hina 2 lg school j at pos_l
    show rin 2 lg school a at pos_r
    with Dissolve(0.25)

    show hina:
        ShakeUji

    voice "HIN_0039"
    hina "\"I'm hungry~\"" id a01_comn_02_fa1c8251

    "Hina slumped over her desk."

    show hina 2 lg school j:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 2 lg school c" with Dissolve(0.25)
        ShakeTameiki
        7.6
        ShakeYes
        0.4
        ShakeYes

    voice "RIN_0044"
    rin "\"Oh, alright. Since I'm so nice, I'll share my lunch with you, just this once. Here, here.\"" id a01_comn_02_e88cfec4

    show rin 2 lg school c:
        xoffset 0 yoffset 0
    with None

    $ side_image = "fumi 1 side school e"

    voice "FUM_0031"
    fumi "\"Oh, there goes a pepper, and a carrot.\"" id a01_comn_02_ecbaad6f

    show hina at pos_l:
        "hina 1 lg school d" with Dissolve(0.25)
        2.0
        ShakeJump

    voice "HIN_0040"
    hina "\"Ugh... thanks... Hey, wait! This is just the stuff you don't like!\"" id a01_comn_02_67ab1c53

    hide rin
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show fumi 2 lg school b at pos_l
    show hina 1 lg school d at pos_r
    with Dissolve(0.25)

    voice "FUM_0032"
    fumi "\"Natsume, I'll split my lunch with you.\" " id a01_comn_02_87ffb9dc

    show hina 1 lg school l with dict_dissolve_25

    voice "HIN_0041"
    hina "\"Asou!\"" id a01_comn_02_e5cde34f

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0033"
    fumi "\"You might be hungry later since it's only half, though.\"" id a01_comn_02_d0043214

    show hina 1 lg school a with dict_dissolve_25

    voice "HIN_0042"
    hina "\"I'll just eat more at dinner.\"" id a01_comn_02_a55cd643

    show fumi 1 lg school c with dict_dissolve_25

    voice "FUM_0034"
    fumi "\"I'll cook a little more rice than usual, then.\"" id a01_comn_02_1489da98

    show hina 1 lg school b with dict_dissolve_25

    voice "HIN_0043"
    hina "\"Alright, let's eat, for real this time!\"" id a01_comn_02_d1b404e1

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0035"
    fumi "\"Here, you eat first.\"" id a01_comn_02_33a8ca15

    show hina 1 lg school c with dict_dissolve_25

    voice "HIN_0044"
    hina "\"Thank you, Asou! What should I eat first?!\"" id a01_comn_02_cfeb0a42

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show rin 1 lg school e at pos_r2
    show fumi 1 lg school a at pos_l2
    show hina 1 lg school a
    with Dissolve(0.25)

    voice "RIN_0045"
    rin "\"Umm... where's my 'Thank you, Rin!'?\"" id a01_comn_02_316ba89a

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0045"
    hina "\"Ngah!\"" id a01_comn_02_bb72b7a9

    show hina 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0036"
    fumi "\"Please eat your whole lunch.\"" id a01_comn_02_f8369586

    "She pushed the lid with the pepper and carrot on it back over to Rin."

    show rin:
        "rin 1 lg school i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0046"
    rin "\"Gh...\"" id a01_comn_02_1a50ac13

    show rin 1 lg school i:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school c with dict_dissolve_25

    voice "HIN_0046"
    hina "\"The peppers are good! And the carrots!\"" id a01_comn_02_74c47215

    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a01_cou3_01
    else:
        jump a01_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
