label a10_cou3_10:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    "Once they were back in their room and alone together, they apologized to each other: Fumi for worrying Rin, and Rin for relying too much on Fumi. Once they were satisfied, the two returned to their usual serenity."

    "Yep, it was basically just as Hina and Sachiko predicted."

    show fumi 2 lg school i with dict_dissolve_25

    voice "2FU_1218"
    fumi "\"Oh, right!\"" id a10_cou3_10_9db29fd8

    $ side_image = "rin 1 side school j"

    voice "2RI_1636"
    rin "\"Whoa, you scared me. What?\"" id a10_cou3_10_736fb1c2

    "Rin was hanging her scarf up, but jumped at Fumi's sudden exclamation."

    hide fumi with Dissolve(0.25)

    show fumi z4 2 lg school c:
        xcenter 298
    show rin z4 1 lg school j:
        xcenter 726
    with dict_dissolve_25

    voice "2FU_1219"
    fumi "\"Let's go to an audition on Sunday, Rin.\"" id a10_cou3_10_2eed72e4

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1637"
    rin "\"...Huh?\"" id a10_cou3_10_33e83ddc

    "Fumi's words were completely unexpected, but she was giving Rin a brilliant smile."

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1638"
    rin "\"Oh, I get it. You want me to come with you when you turn them down?\"" id a10_cou3_10_9b126e46

    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_1220"
    fumi "\"No, I was clear with them about not wanting to be scouted. The audition on Sunday isn't for a movie or being an idol, it's for modeling in a magazine.\"" id a10_cou3_10_e40f547a

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1639"
    rin "\"...You were scouted to be a model now?\"" id a10_cou3_10_6c940b85

    show fumi z4 1 lg school i with dict_dissolve_25

    voice "2FU_1221"
    fumi "\"Umm, no... I turned down becoming an idol, but I sort of got to talking with the president of the agency...\"" id a10_cou3_10_0f8b9d0a

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1640"
    rin "\"Well, I get that. You're the type that gets along with people in high places.\"" id a10_cou3_10_3de199f8

    show fumi z4 2 lg school i with dict_dissolve_25

    voice "2FU_1222"
    if persistent.dpatch:
        fumi "\"And it turns out the president is an alum here! And she was actually in school with the current principal!\"" id a10_cou3_10_e0f8057c
    else:
        fumi "\"And it turns out the president is an alum here! And she was actually in the same class as the current principal!\"" id a10_cou3_10_5f8787a9

    show rin:
        "rin z4 1 lg school j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_1641"
    rin "\"Talk about a small world!\"" id a10_cou3_10_ad106871

    show rin z4 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_1223"
    fumi "\"So we were talking, and that agency is recruiting models for magazines, not just idols, and she asked me about this audition that's coming up.\"" id a10_cou3_10_c403bae1

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1642"
    rin "\"So you want me to go with you?\"" id a10_cou3_10_469f0b35

    show fumi:
        "fumi z4 1 lg school d" with Dissolve(0.25)
        5.0
        "fumi z4 1 lg school f" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1224"
    fumi "\"Oh, no, it's not me that she wants to audition... I'm sorry, I'm skipping around too much.\"" id a10_cou3_10_f83c181c

    show fumi z4 1 lg school f:
        xoffset 0 yoffset 0
    with None

    "Fumi stuck out her tongue in mock apology."

    show fumi z4 1 lg school a with dict_dissolve_25

    voice "2FU_1225"
    fumi "\"Let's see... The president said that while reviewing the footage from that TV spot, she stumbled upon a natural talent.\"" id a10_cou3_10_0f97d329

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1643"
    rin "\"Right, she said you're a talent that comes along once every thousand years. So she was really insistent about recruiting you.\"" id a10_cou3_10_769c61ad

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_1226"
    fumi "\"No... that was something you came up with, Rin.\"" id a10_cou3_10_76b8c962

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1644"
    rin "\"Wait, was it?\"" id a10_cou3_10_292d9a0b

    show fumi z4 2 lg school c with dict_dissolve_25

    voice "2FU_1227"
    fumi "\"But the person the president was talking about was a spectator who was only on camera for a moment through a window...\"" id a10_cou3_10_6504e854

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1645"
    rin "\"Wait, you don't mean...\"" id a10_cou3_10_9fc27205

    "Seems she's finally caught on."

    show fumi:
        "fumi z4 2 lg school i" with Dissolve(0.25)
        ShakeYes

    voice "2FU_1228"
    fumi "\"Yes, exactly! It's you, Rin Ogata~♪\"" id a10_cou3_10_33ff02a1

    show fumi z4 2 lg school i:
        xoffset 0 yoffset 0
    with None

    "She pointed with both hands at Rin. She's really excitable today."

    show fumi z4 2 lg school c with dict_dissolve_25

    voice "2FU_1229"
    fumi "\"I thought I had an idea who she was talking about, so I showed her a picture of you, and she was like, 'Yes, that's her!' She was really happy about it.\"" id a10_cou3_10_4d6a9043

    show fumi z4 1 lg school b with dict_dissolve_25

    voice "2FU_1230"
    fumi "\"So I told her I'd bring you on Sunday.\"" id a10_cou3_10_080bf4b4

    show rin:
        "rin z4 1 lg school j" with Dissolve(0.25)
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1646"
    rin "\"Just like that?! How'd you decide so fast? Aren't you the one who usually agonizes about whether to buy a whole or a half cabbage?\"" id a10_cou3_10_098f32e7

    show rin z4 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school c with dict_dissolve_25

    voice "2FU_1231"
    fumi "\"Yes! But for some reason, I could decide right away when it was about you, Rin. Oh, and they've got everything decided already, so you basically just have to stand there at the audition.\"" id a10_cou3_10_52c0c2fe

    show rin:
        ShakeJump

    voice "2RI_1647"
    rin "\"It's a fixed game?! Adults are so dirty! Show business is scary!\"" id a10_cou3_10_d803008a

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school a with dict_dissolve_25

    voice "2FU_1232"
    fumi "\"She showed me the magazine you'd be exclusive to, and it looked super fashionable.\"" id a10_cou3_10_aa4f82ce

    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_1233"
    fumi "\"They have a lot of foreign models, but you're tall, so you'd fit right in with them, plus you're good at English!\"" id a10_cou3_10_fe36cbea

    show rin:
        ShakeNo_2_250

    voice "2RI_1648"
    rin "\"No way, no way, no way, I can't be a model! I can't even take selfies. And I'm even worse at talking to people I don't know! Everybody knows this about me! I'm shy!\"" id a10_cou3_10_679c62e1

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school c with dict_dissolve_25

    voice "2FU_1234"
    fumi "\"Oh, she also said you could just do this one job. She said you should try it once and see what you think.\"" id a10_cou3_10_125bf625

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1649"
    rin "\"Ugh... I'm telling you, I can't even do it once~\"" id a10_cou3_10_76010f03

    show fumi z4 2 lg school i with dict_dissolve_25

    voice "2FU_1235"
    fumi "\"You can! You're my Rin! Let's try to just take some pictures for the occasion first, okay? And I'll go with you to the audition—\"" id a10_cou3_10_c2988785

    show fumi z4 2 lg school h with dict_dissolve_25

    "Seeing Rin on the verge of tears, Fumi stopped, realization dawning on her face."

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_1650"
    rin "\"...This isn't like you, Fumi.\"" id a10_cou3_10_591b114d

    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_1236"
    fumi "\"I'm sorry... I shouldn't be forcing this on you.\"" id a10_cou3_10_d2bd632d

    "She was silent for a moment, then slowly began:"

    show fumi z4 1 lg school a with dict_dissolve_25

    voice "2FU_1237"
    fumi "\"The president was serious. And the magazine she showed me just looked perfect for you, Rin.\"" id a10_cou3_10_8a3ad4b0

    voice "2FU_1237a"
    fumi "\"Everything looked like it would suit you perfectly: the clothes, the accessories, the makeup...\"" id a10_cou3_10_6846795e

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_1238"
    fumi "\"And she was way more insistent about recruiting you than she was about me.\"" id a10_cou3_10_3157543c

    "Rin listened, her feelings clearly mixed."

    show fumi z4 1 lg school i with dict_dissolve_25

    voice "2FU_1239"
    fumi "\"When I looked through the magazine and imagined the models in it as you, I got really excited.\"" id a10_cou3_10_590a625b

    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_1240"
    fumi "\"I started thinking about how one day you could be a cover model, and I couldn't stop. I'm sorry, I got all carried away.\"" id a10_cou3_10_92a7a081

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1651"
    rin "\"I... I see.\"" id a10_cou3_10_146dd98e

    "Rin found herself unable to be angry."

    "Fumi loved her girlfriend and wanted to show her off to the world. It was exactly like Rin had just been herself."

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1652"
    rin "\"I—\"" id a10_cou3_10_29428648

    show fumi z4 1 lg school a with dict_dissolve_25

    voice "2FU_1241"
    fumi "\"I know, we'll stop talking about this now. More importantly—\"" id a10_cou3_10_55194b51

    "Fumi dropped the subject of the audition and took some chocolate out of her tote bag."

    show fumi z4 2 lg school i with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_1242"
    fumi "\"Here. Happy Valentine's♪\"" id a10_cou3_10_d3d2242e

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1653"
    rin "\"Th-Thanks.\"" id a10_cou3_10_df1d0527

    "Rin wasn't finding it as easy to switch subjects and accepted the chocolate with a rather blank look on her face."

    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_1243"
    fumi "\"It's dark chocolate, so I think you might like it even though you're not fond of sweets.\"" id a10_cou3_10_9555603c

    show rin:
        "rin z4 1 lg school c" with Dissolve(0.25)
        9.0
        "rin z4 1 lg school g" with Dissolve(0.25)

    voice "2RI_1654"
    rin "\"Wow, it's even wrapped all fancy. And I didn't get you anything... Well, unless you want masks and sunglasses.\"" id a10_cou3_10_238b4f57

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_1244"
    fumi "\"You don't have to—\"" id a10_cou3_10_64dfa9b1

    "Fumi suddenly stopped, and Rin peered worriedly at her."

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1655"
    rin "\"Are you mad...?\"" id a10_cou3_10_c3388c40

    show fumi z4 2 lg school i with dict_dissolve_25

    voice "2FU_1245"
    fumi "\"Heheheheh♪\"" id a10_cou3_10_e9fde748

    show rin:
        "rin z4 1 lg school e" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1656"
    rin "\"Huh... What?\"" id a10_cou3_10_fc7c7bcc

    show rin z4 1 lg school e:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school c with dict_dissolve_25

    voice "2FU_1246"
    fumi "\"Didn't you say it a little while ago~?\"" id a10_cou3_10_c5cf2b67

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1657"
    rin "\"Wh-What did I... ah?\"" id a10_cou3_10_d3d86efc

    "Fumi took the chocolate back from Rin and undid the ribbon around the wrapping paper."

    show fumi z4 1 lg school i with dict_dissolve_25

    voice "2FU_1247"
    fumi "\"That you'd wrap yourself up in a big ribbon~\"" id a10_cou3_10_360aef2d

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1658"
    rin "\"D-D-Did I say something like that?\"" id a10_cou3_10_9ec2e1a6

    "From her face, I'd say she knows the answer to that question. I'd also say she didn't know Fumi was listening when she said it."

    show fumi:
        "fumi z4 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_1248"
    fumi "\"You {i}did{/i}. I remember it because as soon as you said it, I got really excited.\"" id a10_cou3_10_28989823

    show fumi z4 1 lg school c:
        xoffset 0 yoffset 0
    with None

    "Putting the chocolate back in her bag, Fumi pulled the ribbon taut between her hands with a {i}snap{/i} and inched toward Rin."

    show fumi z4 2 lg school e with dict_dissolve_25

    voice "2FU_1249"
    fumi "\"Eheheh, I'll be taking your gift now by force.\"" id a10_cou3_10_d11274a6

    show rin:
        "rin z4 1 lg school j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1659"
    rin "\"W-Wait, are you serious?!\"" id a10_cou3_10_e3f47227

    stop music fadeout 1.0
    scene black with Dissolve(0.5)
    pause 2.0

    if persistent.dpatch:
        jump rp_c_scene06
    else:
        stop sound fadeout 1.0
        pause 1.5
        "........."
        "......"
        window hide
        pause 0.5
        window auto

label rp_c_scene06_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    $ renpy.end_replay()


    if routes_cleared < 2:
        jump a10_comn_03
    else:
        jump a10_cou3_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
