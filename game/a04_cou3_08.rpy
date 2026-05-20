label a04_cou3_08:

    scene bg08cb with Dissolve(0.5)
    pause 1.5

    scene bg06ca with Dissolve(0.25)
    pause 0.75

    play music bgm05

    show hina 2 lg school h at pos_r
    show fumi 1 lg school h at pos_l
    with dict_dissolve_25

    "An uneasy silence hung between them."

    "Of course, they were all clothed now, but..."

    voice "RIN_1462"
    rin "\"*sob* *sob*...\""

    "...one of them was covering her face, crying."

    "True, out of the three of them, this one had been discovered in the most compromising position."

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_1516"
    hina "\"Mm, well, I can't say I don't feel bad about this.\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina scratched her head as she watched Rin."

    show hina 2 lg school e with dict_dissolve_25

    voice "HIN_1517"
    hina "\"I thought you two were acting a little weird lately.\""

    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_1289"
    fumi "\"I'm sorry. We couldn't find the right time to tell you.\""

    "Fumi bit her lip guiltily."

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1518"
    hina "\"It's fine. You two are free to go out with each other. You don't need to worry about me.\""

    voice "FUM_1290"
    fumi "\"......\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1519"
    hina "\"Wasn't expecting Rin to be on the bottom, though~\""

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side school j"

    voice "RIN_1463"
    rin "\"Waaaaaaah!!\""

    camera
    with None

    play sound se118c

    show fumi:
        "fumi 2 lg school h" with Dissolve(0.25)
        ShakeYes

    "Rin almost ran out, but Fumi grabbed her by the collar."

    show fumi 2 lg school h with None

    show fumi:
        "fumi 2 lg school g" with Dissolve(0.25)
        xcenter 252 xoffset 0 yoffset 0
        easein 0.25 xcenter 172
    show rin:
        "rin 1 lg school i flat"
        alpha 0.0 xcenter 512 ycenter 1116
        easein 0.5 alpha 1.0 ycenter 1016
    show hina:
        xcenter 772
        easein 0.25 xcenter 852
    pause 0.5

    show fumi 2 lg school g:
        xcenter 172
    show rin 1 lg school i:
        alpha 1.0 xcenter 512 ycenter 1016
    show hina 1 lg school k:
        xcenter 852
    with None

    voice "FUM_1291"
    fumi "\"Umm, I was feeling a little mischievous today, but it's anyone's guess who will be in charge in the future...\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1292"
    fumi "\"It's just, I enjoyed Rin... Ogata's reactions more than I expected, and...\""

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_1520"
    hina "\"Really don't need the backstory there.\""

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide
        0.5
        ShakeSide

    voice "RIN_1464"
    rin "\"Aaaaah...\""

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None

    "Is this hell? Or an unexpected reward?"

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_1521"
    hina "\"Anyway, I understand your relationship now. I'm not really sure what to say... Congratulations, I guess.\""

    show fumi 1 lg school e
    show rin 1 lg school e
    with dict_dissolve_25

    voice "RIN_1465"
    rin "\"...Is that all?\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1522"
    hina "\"What do you mean?\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1466"
    rin "\"I thought you'd be mad.\""

    show hina 2 lg school d with dict_dissolve_25

    voice "HIN_1523"
    hina "\"Why?\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1467"
    rin "\"Well, your stance on deviancy, for one.\""

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_1524"
    hina "\"Like I said, you're free to go out with each other, and people who are going out... well, do that sort of stuff, I guess.\""

    show hina 2 lg school a with dict_dissolve_25

    voice "HIN_1525"
    hina "\"If it's out of love, no one has the right to object to that.\""

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_1293"
    fumi "\"Natsume...\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1468"
    rin "\"I always thought you were just a kid, but that was a real grown-up thing to say...\""

    show hina 1 lg school j with dict_dissolve_25

    voice "HIN_1526"
    hina "\"Shut up, masochist.\""

    show rin:
        "rin 1 lg school i" with Dissolve(0.25)
        ShakeUji

    voice "RIN_1469"
    rin "\"*sob* *sob*...\""

    show rin 1 lg school i:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1527"
    hina "\"But... I'm gonna move out.\""

    show rin 1 lg school e
    show fumi 1 lg school j
    with Dissolve(0.25)
    show rin:
        ShakeSide
    show fumi:
        ShakeSide

    $ voice2("rin","RIN_1470","fumi","FUM_1294")
    rin_fumi "\"What?!\""

    show rin:
        xoffset 0 yoffset 0
    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_1528"
    hina "\"Well, I don't want to get in your way. I'll feel bad, now that I know.\""

    show hina 2 lg school a with dict_dissolve_25

    voice "HIN_1529"
    hina "\"I'll ask Sachiko about it when we get back. I think all the rooms in our dorm are full, so I'll move to another—\""

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_1295"
    fumi "\"No! You can't leave! I want the three of us to stay together!\""

    "Fumi grabbed Hina's hand with both of hers."

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1530"
    hina "\"...Asou...\""

    show fumi 2 lg school f with dict_dissolve_25

    voice "FUM_1296"
    fumi "\"If it will bother you, we'll keep our distance when we're at home. You can handle that, right, Rin?\""

    show rin:
        "rin 1 lg school e" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1471"
    rin "\"Huh? Oh, yeah.\""

    show rin 1 lg school e:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1531"
    hina "\"I mean... as long as I can't see it, I don't mind. It doesn't bother you two to have me around, though?\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1472"
    rin "\"I wouldn't want you to leave either, Hina...\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1532"
    hina "\"Because Asou will bully you?\""

    show rin 1 lg school j with dict_dissolve_25

    voice "RIN_1473"
    rin "\"Will you drop it?!\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1474"
    rin "\"If you stay, we'll go back to how things were. {size=15}...Until we graduate.{/size}\""

    show fumi 2 lg school b with Dissolve(0.25)
    show fumi:
        ShakeYes

    "Rin glanced over at Fumi, who smiled and nodded."

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1533"
    hina "\"It's fine. I'd feel even worse if you did that.\""

    stop music fadeout 3.0

    show hina:
        "hina 2 lg school h" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1534"
    hina "\"...If you don't mind, I want to stay with you, too.\""

    show hina 2 lg school c:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    "Hina smiled tearily."

    play music bgm03

    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_1297"
    fumi "\"We want you to stay, Natsume.\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1475"
    rin "\"I told you about my ideal life, didn't I?\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1535"
    hina "\"Rin, Asou...\""

    "The three all held hands."

    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1536"
    hina "\"Asou, I leave Rin in your hands.\""

    show fumi:
        "fumi 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_1298"
    fumi "\"Of course.\""

    show fumi 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1476"
    rin "\"Why...?\""

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_1299"
    fumi "\"Oh, I know! We can share her.\""

    show hina:
        "hina 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1537"
    hina "\"D-D-Don't joke about that!\""

    show hina 1 lg school l:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1477"
    rin "\"...Didn't sound like a joke to me.\""

    pause 1.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene white with Dissolve(0.75)
    pause 2.25

    call staff_01 from _call_staff_01_2

    jump a04_cou3_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
