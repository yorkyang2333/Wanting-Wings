label a01_comn_02:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm01




    show fumi z3 1 lg school d at pos_l2_z3
    show rin z3 1 lg school a at pos_r2_z3
    show hina z3 1 lg school a at default
    with Dissolve(0.25)

    voice "FUM_0021"
    fumi "\"We cut it a little close this morning, didn't we?\""

    play sound se116a

    "Fumi smiled awkwardly as she opened up her lunch."

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0025"
    if persistent.dpatch:
        hina "\"You said it. If we were one minute later, our dash to the bus would've ended up being a run to school.\"" id a01_comn_02_832fece7
    else:
        hina "\"You said it. If we were one minute later, our dash to the bus would've ended up being a run to class.\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0030"
    rin "\"You could've just left without me.\""

    show hina 1 lg school e
    show fumi 1 lg school a
    with dict_dissolve_25

    voice "HIN_0026"
    if persistent.dpatch:
        hina "\"Uhh, if we did that, you'd just skip school.\"" id a01_comn_02_5c6bec90
    else:
        hina "\"Uhh, if we did that, you'd just skip class.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0031"
    rin "\"Hahaha, that's ridiculous.\""

    show hina 1 lg school j with dict_dissolve_25

    voice "HIN_0027"
    hina "\"Uh huh...\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0022"
    fumi "\"...It's happened before.\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0032"
    rin "\"Just the once, though...\""

    show fumi 1 lg school g with dict_dissolve_25


    $ voice2("hina","HIN_0028","fumi","FUM_0023")
    hina_fumi "\"Uh huh...\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0033"
    rin "\"Was it... twice?\""

    show hina:
        "hina z3 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0029"
    hina "\"Five times!\""

    show hina z3 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0034"
    rin "\"Man, it's already lunch. I sure am hungry.\""

    show hina 1 lg school f with dict_dissolve_25

    voice "HIN_0030"
    hina "\"You little—!\""

    show fumi 1 lg school c with dict_dissolve_25

    voice "FUM_0024"
    fumi "\"Ahaha. We should eat.\""

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_0031"
    hina "\"You're hungry 'cause you don't eat breakfast.\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0035"
    rin "\"Yeah, that's not happening. Who can put food in their stomach right after waking up?\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_0032"
    hina "\"Asou makes really good breakfast, you know.\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0036"
    rin "\"I know that even without eating it. But I really can't eat in the morning.\""

    show fumi z3 2 lg school g with dict_dissolve_25

    voice "FUM_0025"
    fumi "\"Umm, should I get some stuff that's easy to eat, like cereal or oatmeal?\""

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0033"
    hina "\"You don't need to baby her, Asou. Even if you made her something, she'd still stay in bed until the last minute.\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0037"
    rin "\"I suppose it's a question of whether you could gain more energy by eating breakfast or save more energy spending that time sleeping.\""

    show fumi 1 lg school d
    show hina 1 lg school f
    with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "HIN_0034"
    hina "\"Ah~! It's nothing but hypotheticals with you, isn't it?! Why don't you put yourself in the shoes of the people who have to run around after breakfast every day because of you?!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school k with dict_dissolve_25

    voice "RIN_0038"
    rin "\"Now, what do I have to eat today~?\""

    play sound se116a

    "Unfazed, Rin opened her lunch."

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0035"
    hina "\"...Haah. I'll eat, too.\""

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
        rin "\"Ooh, it looks good again today. I only make it to class every day because I have a lunch from my loving wife to look forward to.\""

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0026"
    fumi "\"If it makes my husband happy, it makes me happy, too.\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0040"
    rin "\"There are parts of it that are disturbingly colorful, however.\""

    show fumi 1 lg school b with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "FUM_0027"
    fumi "\"Those would be peppers and carrots.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg school i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0041"
    rin "\"Ugh...\""

    show rin 1 lg school i:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0028"
    fumi "\"You can't be picky. If I didn't make you, you wouldn't eat any vegetables at all, would you, Ogata?\""

    $ side_image = "hina 1 side school d"

    voice "HIN_0036"
    hina "\"Huh? Huh?\""

    play sound se557b

    "Hina was turning her bag inside out."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0029"
    fumi "\"What's wrong?\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show fumi 2 lg school d at pos_l2
    show rin 1 lg school a at pos_r2
    show hina 1 lg school l
    with Dissolve(0.25)

    voice "HIN_0037"
    hina "\"...My lunch... I don't have it.\""

    show fumi 1 lg school e with dict_dissolve_25

    voice "FUM_0030"
    fumi "\"What?\""

    show rin 1 lg school k with dict_dissolve_25

    voice "RIN_0042"
    rin "\"You're such a scatterbrain, Hina.\""

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0038"
    hina "\"It's because of all the chaos this morning! This is all your fault, Rin!\""

    show hina 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0043"
    rin "\"Yeesh. Shifting the blame is low.\""

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
    hina "\"I'm hungry~\""

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
    rin "\"Oh, alright. Since I'm so nice, I'll share my lunch with you, just this once. Here, here.\""

    show rin 2 lg school c:
        xoffset 0 yoffset 0
    with None

    $ side_image = "fumi 1 side school e"

    voice "FUM_0031"
    fumi "\"Oh, there goes a pepper, and a carrot.\""

    show hina at pos_l:
        "hina 1 lg school d" with Dissolve(0.25)
        2.0
        ShakeJump

    voice "HIN_0040"
    hina "\"Ugh... thanks... Hey, wait! This is just the stuff you don't like!\""

    hide rin
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show fumi 2 lg school b at pos_l
    show hina 1 lg school d at pos_r
    with Dissolve(0.25)

    voice "FUM_0032"
    fumi "\"Natsume, I'll split my lunch with you.\" "

    show hina 1 lg school l with dict_dissolve_25

    voice "HIN_0041"
    hina "\"Asou!\""

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0033"
    fumi "\"You might be hungry later since it's only half, though.\""

    show hina 1 lg school a with dict_dissolve_25

    voice "HIN_0042"
    hina "\"I'll just eat more at dinner.\""

    show fumi 1 lg school c with dict_dissolve_25

    voice "FUM_0034"
    fumi "\"I'll cook a little more rice than usual, then.\""

    show hina 1 lg school b with dict_dissolve_25

    voice "HIN_0043"
    hina "\"Alright, let's eat, for real this time!\""

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0035"
    fumi "\"Here, you eat first.\""

    show hina 1 lg school c with dict_dissolve_25

    voice "HIN_0044"
    hina "\"Thank you, Asou! What should I eat first?!\""

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
    rin "\"Umm... where's my 'Thank you, Rin!'?\""

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0045"
    hina "\"Ngah!\""

    show hina 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0036"
    fumi "\"Please eat your whole lunch.\""

    "She pushed the lid with the pepper and carrot on it back over to Rin."

    show rin:
        "rin 1 lg school i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0046"
    rin "\"Gh...\""

    show rin 1 lg school i:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school c with dict_dissolve_25

    voice "HIN_0046"
    hina "\"The peppers are good! And the carrots!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a01_cou3_01
    else:
        jump a01_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
