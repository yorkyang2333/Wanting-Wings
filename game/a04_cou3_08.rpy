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
    rin "\"*sob* *sob*...\"" id a04_cou3_08_27bcf91d

    "...one of them was covering her face, crying."

    "True, out of the three of them, this one had been discovered in the most compromising position."

    show hina 1 lg school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_1516"
    hina "\"Mm, well, I can't say I don't feel bad about this.\"" id a04_cou3_08_66649536

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina scratched her head as she watched Rin."

    show hina 2 lg school e with dict_dissolve_25

    voice "HIN_1517"
    hina "\"I thought you two were acting a little weird lately.\"" id a04_cou3_08_13772033

    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_1289"
    fumi "\"I'm sorry. We couldn't find the right time to tell you.\"" id a04_cou3_08_2b4a57fa

    "Fumi bit her lip guiltily."

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1518"
    hina "\"It's fine. You two are free to go out with each other. You don't need to worry about me.\"" id a04_cou3_08_56bfc14a

    voice "FUM_1290"
    fumi "\"......\"" id a04_cou3_08_41ffff0e

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1519"
    hina "\"Wasn't expecting Rin to be on the bottom, though~\"" id a04_cou3_08_d595e15c

    camera:
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side school j"

    voice "RIN_1463"
    rin "\"Waaaaaaah!!\"" id a04_cou3_08_b4db264f

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
    fumi "\"Umm, I was feeling a little mischievous today, but it's anyone's guess who will be in charge in the future...\"" id a04_cou3_08_639aca71

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1292"
    fumi "\"It's just, I enjoyed Rin... Ogata's reactions more than I expected, and...\"" id a04_cou3_08_b127110c

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_1520"
    hina "\"Really don't need the backstory there.\"" id a04_cou3_08_a8233d50

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide
        0.5
        ShakeSide

    voice "RIN_1464"
    rin "\"Aaaaah...\"" id a04_cou3_08_dc14b539

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None

    "Is this hell? Or an unexpected reward?"

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_1521"
    hina "\"Anyway, I understand your relationship now. I'm not really sure what to say... Congratulations, I guess.\"" id a04_cou3_08_1414e42c

    show fumi 1 lg school e
    show rin 1 lg school e
    with dict_dissolve_25

    voice "RIN_1465"
    rin "\"...Is that all?\"" id a04_cou3_08_e937a46a

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1522"
    hina "\"What do you mean?\"" id a04_cou3_08_409f1833

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1466"
    rin "\"I thought you'd be mad.\"" id a04_cou3_08_6b660b7f

    show hina 2 lg school d with dict_dissolve_25

    voice "HIN_1523"
    hina "\"Why?\"" id a04_cou3_08_74924be8

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1467"
    rin "\"Well, your stance on deviancy, for one.\"" id a04_cou3_08_5a4deb7c

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_1524"
    hina "\"Like I said, you're free to go out with each other, and people who are going out... well, do that sort of stuff, I guess.\"" id a04_cou3_08_56d8fdb2

    show hina 2 lg school a with dict_dissolve_25

    voice "HIN_1525"
    hina "\"If it's out of love, no one has the right to object to that.\"" id a04_cou3_08_188a4fb1

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_1293"
    fumi "\"Natsume...\"" id a04_cou3_08_4419b2e2

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1468"
    rin "\"I always thought you were just a kid, but that was a real grown-up thing to say...\"" id a04_cou3_08_5e7052dc

    show hina 1 lg school j with dict_dissolve_25

    voice "HIN_1526"
    hina "\"Shut up, masochist.\"" id a04_cou3_08_10ad695e

    show rin:
        "rin 1 lg school i" with Dissolve(0.25)
        ShakeUji

    voice "RIN_1469"
    rin "\"*sob* *sob*...\"" id a04_cou3_08_de0417aa

    show rin 1 lg school i:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1527"
    hina "\"But... I'm gonna move out.\"" id a04_cou3_08_c52c8dfb

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
    hina "\"Well, I don't want to get in your way. I'll feel bad, now that I know.\"" id a04_cou3_08_bbe84de7

    show hina 2 lg school a with dict_dissolve_25

    voice "HIN_1529"
    hina "\"I'll ask Sachiko about it when we get back. I think all the rooms in our dorm are full, so I'll move to another—\"" id a04_cou3_08_443b6070

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_1295"
    fumi "\"No! You can't leave! I want the three of us to stay together!\"" id a04_cou3_08_2f32ee13

    "Fumi grabbed Hina's hand with both of hers."

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1530"
    hina "\"...Asou...\"" id a04_cou3_08_46cb6e6c

    show fumi 2 lg school f with dict_dissolve_25

    voice "FUM_1296"
    fumi "\"If it will bother you, we'll keep our distance when we're at home. You can handle that, right, Rin?\"" id a04_cou3_08_2508bd68

    show rin:
        "rin 1 lg school e" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1471"
    rin "\"Huh? Oh, yeah.\"" id a04_cou3_08_3255e050

    show rin 1 lg school e:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1531"
    hina "\"I mean... as long as I can't see it, I don't mind. It doesn't bother you two to have me around, though?\"" id a04_cou3_08_48140cd7

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1472"
    rin "\"I wouldn't want you to leave either, Hina...\"" id a04_cou3_08_04acd263

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1532"
    hina "\"Because Asou will bully you?\"" id a04_cou3_08_2d522b56

    show rin 1 lg school j with dict_dissolve_25

    voice "RIN_1473"
    rin "\"Will you drop it?!\"" id a04_cou3_08_2a896b04

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1474"
    rin "\"If you stay, we'll go back to how things were. {size=15}...Until we graduate.{/size}\"" id a04_cou3_08_7f7f7ab5

    show fumi 2 lg school b with Dissolve(0.25)
    show fumi:
        ShakeYes

    "Rin glanced over at Fumi, who smiled and nodded."

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1533"
    hina "\"It's fine. I'd feel even worse if you did that.\"" id a04_cou3_08_552d516a

    stop music fadeout 3.0

    show hina:
        "hina 2 lg school h" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1534"
    hina "\"...If you don't mind, I want to stay with you, too.\"" id a04_cou3_08_c917b3a9

    show hina 2 lg school c:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    "Hina smiled tearily."

    play music bgm03

    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_1297"
    fumi "\"We want you to stay, Natsume.\"" id a04_cou3_08_4c1d1a19

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1475"
    rin "\"I told you about my ideal life, didn't I?\"" id a04_cou3_08_18a6b86c

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1535"
    hina "\"Rin, Asou...\"" id a04_cou3_08_610001dc

    "The three all held hands."

    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1536"
    hina "\"Asou, I leave Rin in your hands.\"" id a04_cou3_08_af5c5371

    show fumi:
        "fumi 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_1298"
    fumi "\"Of course.\"" id a04_cou3_08_3b2f393c

    show fumi 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1476"
    rin "\"Why...?\"" id a04_cou3_08_b962348c

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_1299"
    fumi "\"Oh, I know! We can share her.\"" id a04_cou3_08_0c9dc65b

    show hina:
        "hina 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1537"
    hina "\"D-D-Don't joke about that!\"" id a04_cou3_08_cedf721b

    show hina 1 lg school l:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1477"
    rin "\"...Didn't sound like a joke to me.\"" id a04_cou3_08_8415a25d

    pause 1.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene white with Dissolve(0.75)
    pause 2.25

    call staff_01 from _call_staff_01_2

    jump a04_cou3_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
