label a08_cou1_03:

    scene bg09cb with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_boiling1
    pause 0.5

    show bg_obi behind fumi, miyako, hina, rin
    with Dissolve(0.5)

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0609"
    hina "\"That part's cooked, so you can eat it. This is... gonna need some more time.\""

    "More than halfway into the hotpot, Hina was still busy, scooping out the scum and adding ingredients."

    show fumi 2 lg pyjama g at pos_l with dict_dissolve_25

    voice "2FU_0517"
    fumi "\"Are you eating too, Hina?\""

    show hina 2 lg pyjama_pjm a at pos_r with dict_dissolve_25

    voice "2HI_0610"
    hina "\"Yeah, I am. See?\""

    "Hina's shell bowl had several crab legs sticking out of it."

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0518"
    fumi "\"Good. You're really good at this.\""

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0611"
    hina "\"Thanks. You chopped the veggies, right?\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0519"
    fumi "\"I did... Did I mess something up?\""

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0612"
    hina "\"No, the opposite. You've separated the green and the white parts, and they're all the right size, too. You really pay a lot of attention.\""

    "Hina held up a piece of cabbage, impressed."

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "2FU_0520"
    fumi "\"Yes, since they cook at different speeds.\""

    show hina:
        "hina 1 lg pyjama_pjm n" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0613"
    hina "\"Everybody in my family is so sloppy. They just chop everything up at whatever sizes. It's always like we're out camping or something.\""

    show hina 1 lg pyjama_pjm n:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0521"
    fumi "\"Aha, well, we're a family of bakers, so we want to measure everything.\""

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0614"
    hina "\"That's so funny. Here, this crab is perfect right now. Take it before it gets hard.\""

    "Hina moved a crab leg to Fumi's bowl."

    show fumi:
        "fumi 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0522"
    fumi "\"Thank you. You're so considerate, Hina.\""

    show fumi 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0615"
    hina "\"Heheheh♪\""

    hide fumi
    hide hina
    with Dissolve(0.5)

    show rin z4 1 lg pyjama glasses a:
        xcenter 726
    show sachiko z4 1 lg outfit a:
        xcenter 298
    with dict_dissolve_25

    voice "2SA_0405"
    sachiko "\"You two are so close~\""

    "Across the table, Sachiko was watching them, tipping back a sake cup."

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0617"
    rin "\"They really are. So much it's a bit of a problem actually.\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0406"
    sachiko "\"Heheh. They raise the temperature too much? You know, it {i}is{/i} kinda hot in here.\""

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0618"
    rin "\"Don't say stuff like that. It's hot 'cause you're drinking. And we're cooking.\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0407"
    sachiko "\"Oh, right. So why's it a problem for you if Hinacchi and Foomin are too close?\""

    $ side_image = "hina 1 side pyjama_pjm d"

    voice "2HI_0616"
    hina "\"Huh? What? Are we causing problems for you, Rin?\""

    $ side_image = "fumi 1 side pyjama k"

    voice "2FU_0523"
    fumi "\"I'm sorry... we should have noticed.\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0619"
    rin "\"No, I don't mind that you're close. I mean, I was the one who read you your vows.\""

    "On Christmas Eve in the chapel."

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0620"
    rin "\"I just kinda wish you'd have some shame, y'know~\""

    $ side_image = "hina 1 side pyjama_pjm e"

    voice "2HI_0617"
    hina "\"Shame? Why?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0408"
    sachiko "\"What? Did something happen?\""

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0621"
    rin "\"Oh, plenty of things, but the worst was after our shrine visit on New Year's—\""

    $ side_image = "fumi 1 side pyjama j"

    voice "2FU_0524"
    fumi "\"Ah! That was—\""

    "Realizing where she was going, Fumi tried to stop her, but Rin continued..."

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0622B"
    rin "\"When Mikoyan and I came back, the two of them were sleeping on each other, {i}naked{/i}!\""

    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0409"
    sachiko "\"Oho! Was it after the act? Was it?\""

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0623"
    rin "\"I bet it was~ They looked like they wore themselves out and fell asleep just like that.\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0410"
    sachiko "\"Aaaaah!!\""

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0618"
    hina "\"We didn't do anything. We tried, but... We ended up happy just holding each other, and before I knew it, I'd dozed off.\""

    show sachiko z4 1 lg outfit e
    show rin z4 1 lg pyjama glasses d
    with dict_dissolve_25

    $ voice2("rin","2RI_0624RE","sachiko","2SA_0411")
    rin_sachiko "\"Aaaaah!!\""

    "Hina's blithe words elicited bittersweet screams from Rin and Sachiko."

    $ side_image = "fumi 1 side pyjama j"

    voice "2FU_0525"
    fumi "\"Hina, Hina...!\""

    "Fumi reddened at Hina's candidness."

    show black behind bg_obi:
        alpha 0.39
    with dict_dissolve_50

    show sachiko z4 1 lg outfit a with dict_dissolve_50

    voice "2SA_0412"
    sachiko "\"Well, it is a four-person room, but you've gotta let them get away with some stuff. Just look at how pure Hinacchi is!\""

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0625"
    rin "\"I know. I'm not really bothered by it. I just like teasing them.\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0413"
    sachiko "\"Yeah... I get that.\""

    hide black with dict_dissolve_50

    show sachiko z4 1 lg outfit f with dict_dissolve_50

    voice "2SA_0414"
    sachiko "\"If you asked, I'd let you use this room whenever you want! You get three hours' free time, just call extension 9 for inquiries.\""

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0526"
    fumi "\"Free time? Extension 9?\""

    "Fumi cocked her head, face blank."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0415"
    sachiko "\"Oh, free time means—\""

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0619"
    hina "\"Hey!\""

    play sound se_2s_h001

    "Kick!"

    "Hina kicked Sachiko's shin under the table."

    show sachiko:
        "sachiko z4 1 lg outfit h" with Dissolve(0.25)
        ShakeSide

    voice "2SA_0416"
    sachiko "\"Gfh?!\""

    show sachiko z4 1 lg outfit h:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm e"

    voice "2HI_0620"
    hina "\"I dunno what you're talking about, but it's dirty, isn't it?! Don't teach Fumi dirty stuff!\""

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0626"
    rin "\"She's got good instinct at least.\""

    "Or Sachiko's usual behavior just makes it easy to guess."

    hide sachiko with Dissolve(0.25)

    show fumi z4 2 lg pyjama g:
        xcenter 298
    with dict_dissolve_25

    voice "2FU_0527"
    fumi "\"Umm, Ogata, what did she mean by...?\""

    "Fumi asked Rin, still curious."

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0627"
    rin "\"Hell no. I'm not getting kicked by Hina.\""

    $ side_image = "hina 1 side pyjama_pjm m"

    voice "2HI_0621"
    hina "\"Darn right!\""

    "Hina gave an emphatic nod."

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0628"
    rin "\"Anyway, I just want you to think about how I feel when you put on displays like that.\""

    show fumi 1 lg pyjama d with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "2FU_0528"
    fumi "\"Umm... we'll be more careful.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0629"
    rin "\"After all, unlike you two, I'm all by my lonesome~\""

    $ side_image = "hina 2 side pyjama_pjm d"

    voice "2HI_0622"
    hina "\"Rin, you can't spend all your time sulking.\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0630"
    rin "\"Huh? What's that? Your eyes are full of pity... no, more like lofty compassion, isn't it?\""

    voice "2RI_0630a"
    rin "\"How can you look so grown-up when you don't even know what free time is?\""

    $ side_image = "hina 1 side pyjama_pjm e"

    voice "2HI_0623"
    hina "\"I might not know what you're talking about, but I know that if you don't start acting more true to yourself, you'll end up all alone. You'll become a sad, lonely adult like Sachiko.\""

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0417"
    sachiko "\"Hey!\""

    "Hina's words suddenly struck Sachiko on the right cheek."

    show rin z4 1 lg pyjama glasses j with dict_dissolve_25

    voice "2RI_0631"
    rin "\"Ack, I {i}really{/i} don't want that!\""

    $ side_image = "sachiko 1 side outfit j"

    voice "2SA_0418"
    sachiko "\"Hey!!\""

    "And there was the strike on the left cheek."

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0632"
    rin "\"Come on, Mikoyan, let's date!\""

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_0527"
    miyako "\"...Huh? What? I'm sorry, I was eating crab!\""

    "The crab-eating lion looked back at her blankly, crab spoon in hand."

    "...I thought she was being a little too quiet."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 0:
        jump a08_comn_13
    else:
        jump a08_comn_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
