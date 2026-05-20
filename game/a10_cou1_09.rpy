label a10_cou1_09:

    scene bg01cg with Dissolve(0.5)
    pause 1.5

    play music bgm01 fadein 1.0

    show bg_obi behind fumi, miyako, hina, rin

    show fumi z4 2 lg pyjama c:
        xcenter 118
    show miyako z4 1 lg pyjama_a g behind fumi, hina:
        xcenter 383
    show hina z4 1 lg pyjama_pjm a:
        xcenter 641
    show rin z4 1 lg pyjama glasses a:
        xcenter 906
    with Dissolve(0.5)

    voice "2FU_1084"
    fumi "\"Okay, now let's all have some cake.\""

    "Fumi said, presenting the box she'd received from her father."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0828"
    sachiko "\"I kinda showed up at the perfect time, huh? Sorry~\""

    show fumi z4 1 lg pyjama c with dict_dissolve_25

    voice "2FU_1085"
    fumi "\"It's alright. It's a whole cake, so we couldn't have finished it on our own anyway. I was planning on sharing some with you.\""

    show miyako z4 1 lg pyjama_a l with dict_dissolve_25

    voice "2MI_1024"
    miyako "\"Ohhh...\""

    "Someone seemed to be reliving some sort of trauma..."

    voice "2RI_1292"
    rin "\"Isn't it pretty hard to split a cake five ways?\""

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_1086"
    fumi "\"I'll just do it by eye.\""

    show hina z4 2 lg pyjama_pjm f with Dissolve(0.25)
    show hina:
        ShakeYes

    voice "2HI_1343"
    hina "\"Here, plates and forks. We don't have enough for everyone, so do you mind using chopsticks, Sachiko?\""

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0829"
    sachiko "\"What~? I don't want to eat it like it's tofu or something~\n ...She says, but actually, she came bearing her own fork!\""

    "Sachiko took out a case from her vest pocket with a fork in it."

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1344"
    hina "\"So you came here fully expecting to be fed.\""

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_1087"
    fumi "\"Ah...\""

    "Fumi let out as they chatted."

    show rin z4 2 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1293"
    rin "\"Hm? What is it? It didn't fall apart, did it?\""

    show fumi z4 2 lg pyjama d with dict_dissolve_25

    voice "2FU_1088"
    fumi "\"No, the cake is fine, but my dad did something weird again...\""

    "Everyone peered at the cake as it was revealed from the box."

    show miyako z4 2 lg pyjama a
    show hina z4 1 lg pyjama_pjm c
    show rin z4 2 lg pyjama glasses f
    with dict_dissolve_25

    voice "2HI_1345"
    hina "\"Ahahahaha.\""

    "Hina laughed and awkward smiles appeared on everyone else's faces."

    "Two small figures in formal dress stood atop the cake."

    show hina z4 2 lg pyjama_pjm b with dict_dissolve_25

    voice "2HI_1346"
    hina "\"It's a wedding cake, huh~?\""

    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1294"
    rin "\"Oh yeah, and Hina's birthday cake was a Christmas cake, wasn't it?\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_1089"
    fumi "\"I wonder if my dad switched it with a customer's. If he did, then...\""

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0830"
    sachiko "\"Then it's no problem for us to eat this one, but if somebody's having a wedding, they might be in trouble.\""

    show miyako z4 2 lg pyjama b with dict_dissolve_25

    voice "2MI_1025"
    miyako "\"They'd be so disappointed.\""

    show fumi z4 1 lg pyjama d with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "2FU_1090"
    fumi "\"I'll ask him over LIME right now.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi sighed and started typing a message into her family groupchat."

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_1347"
    hina "\"Your dad's the same as ever. Did we have an order like that today, though?\""

    play sound se_vibes
    pause 1.0
    stop sound

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_1091"
    fumi "\"Oh, he replied. And it's really long...\""

    "Fumi's phone buzzed almost immediately, and she ran her eyes over the message."

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1295"
    rin "\"Was it for a customer?\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_1092"
    fumi "\"......\""

    "Fumi was frozen, looking at her phone."

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_1348"
    hina "\"Fumi?\""

    voice "2FU_1093"
    fumi "\"It wasn't a mistake...\""

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_1349"
    hina "\"Huh? The wedding cake?\""

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_1094"
    fumi "\"Yes. He made this cake for us.\""

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_1350"
    hina "\"What do you...\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_1095"
    fumi "\"Apparently my mom knew from the beginning that we were going out...\""

    show miyako z4 1 lg pyjama_b f
    show hina z4 1 lg pyjama_pjm l
    with dict_dissolve_25
    show rin:
        "rin z4 1 lg pyjama glasses e" with Dissolve(0.25)
        ShakeSide

    voice "2HI_1351"
    hina "\"Huh?!\""

    show rin z4 1 lg pyjama glasses e:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1296"
    rin "\"What, were you guys flirting on the job?\""

    show hina:
        "hina z4 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1352"
    hina "\"We wouldn't do that!\""

    show hina z4 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_1096"
    fumi "\"Umm, no, it was before working at the store. I guess she figured it out when you guys came over for New Year's. From how we acted together.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0831"
    sachiko "\"Well, you are pretty sharp about those things, Foomin. Guess you get it from your mom.\""

    "Makes sense."

    show miyako z4 1 lg pyjama_b g with dict_dissolve_25

    voice "2MI_1026"
    miyako "\"So how does your mom feel about your relationship?\""

    show fumi z4 1 lg pyjama b with dict_dissolve_25

    voice "2FU_1097"
    fumi "\"My mom... really loves Hina.\""

    show hina:
        "hina z4 1 lg pyjama_pjm l" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1353"
    hina "\"Whoa!\""

    show hina z4 1 lg pyjama_pjm l:
        xoffset 0 yoffset 0
    with None
    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1297"
    rin "\"So does your dad know now, too?\""

    show fumi:
        "fumi z4 1 lg pyjama a" with Dissolve(0.25)
        ShakeYes

    voice "2FU_1098"
    fumi "\"Yes, I guess he knows now. Though he didn't figure it out until recently.\""

    show fumi z4 1 lg pyjama a:
        xoffset 0 yoffset 0
    with None
    show rin:
        ShakeYes
    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_1354"
    hina "\"......\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_1099"
    fumi "\"So... when he sent that message about me getting married, my mom found out after and got really mad at him.\""

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0832"
    sachiko "\"Oh...\""

    play sound se_lime

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_1355"
    hina "\"Mm... you've got another message.\""

    show fumi z4 2 lg pyjama h
    show miyako z4 1 lg pyjama_a e
    show hina z4 1 lg pyjama_pjm k
    show rin z4 1 lg pyjama glasses a
    with dict_dissolve_25

    "......"

    "Hina peered over at her screen from the side, the other three watching them and waiting."

    show fumi z4 2 lg pyjama c
    show hina z4 2 lg pyjama_pjm g
    with dict_dissolve_25

    $ voice2("hina","2HI_1356","fumi","2FU_1100N")
    hina_fumi "\"......!\""

    "Bright smiles suddenly burst onto Fumi's and Hina's faces."

    show rin z4 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_1298"
    rin "\"Huh? What was it?\""

    show hina z4 1 lg pyjama_pjm q with dict_dissolve_25

    voice "2HI_1357"
    hina "\"Her dad approves of us, too!\""

    show miyako z4 1 lg pyjama_a f
    show hina z4 1 lg pyjama_pjm c
    show rin z4 1 lg pyjama glasses d
    with Dissolve(0.25)

    show hina:
        ease 0.4 yoffset -14
        ease 0.4 yoffset 0
    show rin:
        ease 0.4 yoffset -18
        ease 0.4 yoffset 0

    $ voice2("hina","2HI_1358N","rin","2RI_1299")
    hina_rin "\"Yay!\""

    play sound se_2s_h011

    "High five."

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_1101"
    fumi "\"Actually, it wasn't like he was ever against it, he just didn't realize, and wasn't thinking about it at all. I guess my dad is that sort of person...\""

    show miyako z4 1 lg pyjama_a h with dict_dissolve_25

    voice "2MI_1027"
    miyako "\"That's great. Sometimes your fear about a thing is worse than the thing itself.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0833"
    sachiko "\"Good thing your parents are so chill.\""

    show fumi z4 1 lg pyjama b with dict_dissolve_25

    voice "2FU_1102"
    fumi "\"Also, my dad really likes Hina too, and he says she can join us whenever she wants.\""

    show rin z4 2 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1300"
    rin "\"Join you, as in... the family?\""

    show fumi:
        "fumi z4 1 lg pyjama b" with Dissolve(0.25)
        ShakeYes

    "Fumi hesitated, then nodded."

    show fumi z4 1 lg pyjama b:
        xoffset 0 yoffset 0
    with None
    show hina z4 2 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_1359"
    hina "\"Geez, it's a little soon for that, isn't it?\""

    "Hina said, though she seemed happy about it, too."

    play sound windowknock

    pause 1.0

    show fumi z4 1 lg pyjama j
    show miyako z4 1 lg pyjama_a f
    show hina z4 1 lg pyjama_pjm d
    show rin z4 1 lg pyjama glasses j
    with Dissolve(0.25)

    show hina:
        ShakeSide

    voice "2HI_1360"
    hina "\"Wah!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Something soft whapped against the window. Everyone jumped and looked over."

    play sound se_2s_f011

    "There was some colorful yarn hanging off the clothesline. Sachiko went and took it in."

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0834"
    sachiko "\"Hm? Isn't this your scarf, Hinacchi?\""

    show fumi z4 1 lg pyjama e
    show miyako z4 1 lg pyjama_a g
    show hina z4 2 lg pyjama_pjm f
    show rin z4 1 lg pyjama glasses e
    with dict_dissolve_25

    voice "2HI_1361"
    hina "\"Huh? It got blown away at the bus stop...\""

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_1028"
    miyako "\"Do you think the wind took it back to its owner?\""

    show fumi z4 1 lg pyjama c with dict_dissolve_25

    voice "2FU_1103"
    fumi "\"Wow!\""

    "The whole group was astonished at the coincidence."

    "It was the moment all the winds started moving in their favor."

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1301"
    rin "\"I know, it's a perfect opportunity...\""

    show rin:
        ShakeYes

    "Rin took both of their hands and had them grip the knife together."

    show fumi z4 2 lg pyjama g
    show hina z4 2 lg pyjama_pjm f
    show rin z4 1 lg pyjama glasses c:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2RI_1302"
    rin "\"Here, it's your first job as a couple. Just a small one, though.\""

    show hina z4 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_1362"
    hina "\"Fumi.\""

    show fumi z4 2 lg pyjama c with dict_dissolve_25

    voice "2FU_1104"
    fumi "\"Hina.\""

    "They looked into each other's eyes, and the knife slid into the cake."

    show miyako z4 1 lg pyjama_b g with dict_dissolve_25

    voice "2MI_1029"
    miyako "\"So to split it five ways, where do you cut it next?\""

    show fumi z4 2 lg pyjama g
    show hina z4 2 lg pyjama_pjm f
    show rin z4 1 lg pyjama glasses e
    with dict_dissolve_25

    $ voice2("hina","2HI_1363","fumi","2FU_1105")
    hina_fumi "\"Umm?\""

    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with Dissolve(0.75)
    pause 2.25

    call staff_02 from _call_staff_02

    jump a10_cou1_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
