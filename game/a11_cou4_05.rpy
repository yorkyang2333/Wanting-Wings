label a11_cou4_05:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_05:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg05ca with Dissolve(0.25)
    pause 0.75

    play music bgm01 fadein 1.0

    show hina 1 sm pyjama_pjm a:
        xcenter 630
    show rin 1 sm pyjama glasses a behind hina, fumi:
        xcenter 776
    show fumi 1 sm pyjama a:
        xcenter 940
    with Dissolve(0.25)

    play sound se521
    pause 1.0

    show sachiko 1 sm outfit a:
        xcenter 184
    with dict_dissolve_25

    voice "2SA_0997"
    sachiko "\"Oh? What's everybody doing out here?\""

    "Leaving the manager's room, Sachiko ran into the girls."

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "2FU_1296"
    fumi "\"Well, I came to get those dishes.\""

    show sachiko:
        "sachiko 1 sm outfit g" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0998"
    sachiko "\"What a coincidence. I was just going to give them back. Thanks, it was really good.\""

    show sachiko 1 sm outfit g:
        xoffset 0 yoffset 0
    with None

    "Sachiko bowed her head and handed the dishes back to Fumi."

    show fumi:
        "fumi 1 sm pyjama a" with Dissolve(0.25)
        1.8
        "fumi 1 sm pyjama d" with Dissolve(0.25)

    voice "2FU_1297"
    fumi "\"Thank you. Oh, you washed them again. You really don't need to.\""

    show fumi 1 sm pyjama d:
        pass
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0999"
    sachiko "\"What about you guys?\""

    voice "2RI_1702"
    rin "\"I was gonna get some coffee from the vending machine. We forgot to buy beans, so I gotta put up with the canned crap.\""

    voice "2HI_1607"
    hina "\"I'm just along for the ride.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_1000"
    sachiko "\"I'll treat you as thanks for the food, then.\""

    show hina:
        "hina 1 sm pyjama_pjm c" with Dissolve(0.25)
        3.5
        "hina 1 sm pyjama_pjm d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1608"
    hina "\"Yay! Then I want some warm... cold ginger tea?!\""

    show hina 1 sm pyjama_pjm d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit c
    show rin 1 sm pyjama glasses j
    show fumi 1 sm pyjama e
    with dict_dissolve_25

    voice "2SA_1001"
    sachiko "\"Huh?\""

    show rin:
        ShakeJump

    voice "2RI_1703"
    rin "\"No matter what you pick... it's all warm cold ginger tea!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_1002"
    sachiko "\"Wouldn't that be hot ginger tea, then?\""

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "2RI_1704"
    rin "\"We keep telling you to keep this thing stocked!\""

    show fumi 1 sm pyjama c with dict_dissolve_25

    voice "2FU_1298"
    fumi "\"Ahahaha.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1003"
    sachiko "\"Well, never mind the vending machine, then. I'll treat you some other time.\""

    show hina 1 sm pyjama_pjm k with dict_dissolve_25

    voice "2HI_1609"
    hina "\"With what? Are you gonna take us somewhere?\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_1004"
    sachiko "\"No, I've got some things coming in soon, so I thought I'd throw a hot pot party. I'll invite you guys.\""

    show fumi 2 sm pyjama g with dict_dissolve_25

    voice "2FU_1299"
    fumi "\"Oh? Is that okay?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1005"
    sachiko "\"Yeah, you guys have been doing a lot for me lately. I've gotta thank you for Miyako, too...\""

    show hina 2 sm pyjama_pjm d
    show rin 1 sm pyjama glasses a
    show fumi 1 sm pyjama a
    with dict_dissolve_25

    "She realized Miyako was nowhere to be seen. The three of them all pointed back at their room."

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_1006"
    sachiko "\"Is she sleeping?\""

    "They all nodded and Sachiko looked at her watch with a wry smile."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1007"
    sachiko "\"So, how is she as a roommate? What do you think of her after living together for a little while?\""

    show hina 2 sm pyjama_pjm f
    show rin 1 sm pyjama glasses k
    show fumi 1 sm pyjama d
    with dict_dissolve_25

    $ voice3("hina","2HI_1610","rin","2RI_1705","fumi","2FU_1300N")
    hina_rin_fumi "\"She sleeps a lot.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_1008"
    sachiko "\"Pfft.\""

    "Sachiko burst out laughing at their perfect synchronization."

    show hina 1 sm pyjama_pjm a with dict_dissolve_25

    voice "2HI_1611"
    hina "\"She falls asleep while standing up a lot in the morning. Or when she's putting her shoes on, or tying her ribbon, or coming down from her bed.\""

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_1009"
    sachiko "\"That's pretty impressive...\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "2FU_1301"
    fumi "\"I have to wake her up sometimes in class when she nods off.\""

    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "2RI_1706"
    rin "\"And she gets sleepy at night right after dinner, too.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_1010"
    sachiko "\"It's like she's got Hina's ability to get to bed quick and Rin's inability to get up in the morning, combined to make her the ultimate snooze monster.\""

    show hina 1 sm pyjama_pjm f
    show rin 1 sm pyjama glasses i
    with dict_dissolve_25

    $ voice2("hina","2HI_1612","rin","2RI_1707")
    hina_rin "\"Hey!\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_1011"
    sachiko "\"I mean, I understand Rin, but I wasn't insulting you, Hinacchi.\""

    show fumi 2 sm pyjama b with dict_dissolve_25

    voice "2FU_1302"
    fumi "\"But she's a very good girl, Miyako. She helps out a lot, too.\""

    show hina 1 sm pyjama_pjm a with dict_dissolve_25

    voice "2HI_1613"
    hina "\"Yeah, unlike Rin.\""

    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "2RI_1708"
    rin "\"Hey. I help out when I need to.\""

    show hina 1 sm pyjama_pjm j with dict_dissolve_25

    voice "2HI_1614"
    hina "\"You don't help out. You just get in the way.\""

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "2RI_1709"
    rin "\"What was that~?\""

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "2FU_1303"
    fumi "\"I feel at ease around Miyako.\""

    show hina 1 sm pyjama_pjm c with dict_dissolve_25

    voice "2HI_1615"
    hina "\"Yeah! She makes you feel happy just being around her.\""

    show rin 1 sm pyjama glasses d with dict_dissolve_25

    voice "2RI_1710"
    rin "\"Well, she's beautiful, and has those huge ti—\""

    show hina:
        "hina 1 sm pyjama_pjm f" with Dissolve(0.25)
        ShakeYes

    voice "2HI_1616"
    hina "\"Seyah!\""

    show hina 1 sm pyjama_pjm f:
        xoffset 0 yoffset 0
    with None

    play sound se_2s_h001

    show rin:
        "rin 1 sm pyjama glasses j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1711"
    rin "\"Gfh?!\""

    show rin 1 sm pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin's knees buckled as Hina hit them from behind with a low kick."

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "2FU_1304"
    fumi "\"Anyway...\""

    show hina 1 sm pyjama_pjm p
    show rin 1 sm pyjama glasses c
    show fumi 1 sm pyjama c
    with dict_dissolve_25

    $ voice3("hina","2HI_1617","rin","2RI_1712N","fumi","2FU_1305N")
    hina_rin_fumi "\"She's like an angel.\"" (what_rest_indent=0)

    "They all said together."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1012"
    sachiko "\"...Oh yeah?\""

    show hina 1 sm pyjama_pjm f
    show rin 1 sm pyjama glasses h
    with dict_dissolve_25

    $ voice2("hina","2HI_1618","rin","2RI_1713")
    hina_rin "\"It's hard to believe she's your cousin!\""

    show sachiko:
        "sachiko 1 sm outfit j" with Dissolve(0.25)
        ShakeJump

    voice "2SA_1013"
    sachiko "\"You guys aren't coming to my party!\""

    show sachiko 1 sm outfit j:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 1 sm pyjama d" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1306"
    fumi "\"Now, now...\""

    show fumi 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1014"
    sachiko "\"Well, as her cousin, I think she's a good girl, too. It's pretty incredible how honestly impressed she is by everything.\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "2RI_1714"
    rin "\"Yeah. She's got a real light to her.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_1015"
    sachiko "\"She comes to my room every day and tells me everything that happened to her.\""

    show hina 2 sm pyjama_pjm f with dict_dissolve_25

    voice "2HI_1619"
    hina "\"Oh, is that where she was going?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1016"
    sachiko "\"Well, part of it is probably 'cause she was {i}abroad{/i}, but... she has a real talent for finding the fun in things.\""

    "The three nodded."

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_1017"
    sachiko "\"It's nice to be young~\""

    show rin 1 sm pyjama glasses f with dict_dissolve_25

    voice "2RI_1715"
    rin "\"Isn't it?\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_1018"
    sachiko "\"Ugh, it makes me mad when you go along with it.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
