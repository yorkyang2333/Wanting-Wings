label a11_cou4_12:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_12:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg07bb with Dissolve(0.25)
    pause 0.75

    play sound se001b
    pause 0.7

    play sound se_wind02
    pause 1.0

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_1067"
    sachiko "\"Pwah! Windy!\""

    "As soon as she opened the door, the wind blew her hair every which way."

    "Holding it down, Sachiko looked around and spotted Miyako."

    "She was sitting in the same spot she had on that Christmas Eve night."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1068"
    sachiko "\"Do you miss the sky?\""

    pause 0.5

    scene white with Dissolve(0.1875)
    pause 1.5625

    play music bgm03 fadein 2.0

    scene kimihane_03_h with Dissolve(0.5)
    pause 1.5

    play sound se_fence

    pause 1.0

    play sound se_tabaco

    "Sachiko leaned against the fence and lit a cigarette. This was the same as that night, too."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1187"
    miyako "\"You found me right away.\""

    voice "2SA_1069"
    sachiko "\"I saw your shoes at the door. The rest was easy enough.\""

    "Sachiko tapped her temple."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1188"
    miyako "\"The brilliant detective.\""

    "Angels and smoke like high places."

    voice "2SA_1070"
    if persistent.dpatch:
        sachiko "\"This time I know you should still be in school.\"" id a11_cou4_12_28209e99
    else:
        sachiko "\"This time I know you should still be in class.\""

    $ side_image = "miyako 1 side school_a_sei c"

    voice "2MI_1189"
    miyako "\"I went home early.\""

    voice "2SA_1071"
    sachiko "\"What a bad girl.\""

    "She breathed out some smoke. Her disapproval didn't sound particularly genuine."

    voice "2SA_1072"
    sachiko "\"So? Are you going right back up there?\""

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_1190"
    miyako "\"Huh? Can you do that?\""

    voice "2SA_1073"
    sachiko "\"I guess I don't know. Do you want to? That'd be a pretty quick turn-around.\""

    $ side_image = "miyako 1 side school_b_sei h"

    voice "2MI_1191"
    miyako "\"Ahaha. I have no plans to return right now.\""

    voice "2SA_1074"
    sachiko "\"There's plenty more to see on the surface, after all.\""

    $ side_image = "miyako 2 side school_sei d"

    voice "2MI_1192"
    miyako "\"But if I could go back to being an angel—\""

    pause 0.5

    scene white with Dissolve(0.3)
    pause 0.5

    show a11_cou4_12_grayscale01 at truecenter with Dissolve(1.0)
    pause 0.5

    voice "2NO_0034"
    noel "\"Aww~ I wonder if I can become an angel when I die... Then I could watch over her forever.\""

    window hide

    pause 0.5

    show a11_cou4_12_grayscale01:
        alpha 1.0 zoom 1.0
        parallel:
            linear 0.25 alpha 0.0
        parallel:
            easein 0.25 zoom 1.12

    pause 1.25

    scene kimihane_03_h with Dissolve(1.0)
    pause 1.0

    $ side_image = "miyako 1 side school_a_sei a"

    window auto

    voice "2MI_1193"
    miyako "\"I met Noel.\""

    scene kimihane_03_l with Dissolve(0.5)

    voice "2SA_1075"
    sachiko "\"Huh...?\""

    "She almost let the cigarette fall from her lips at the unexpected announcement."

    voice "2SA_1076"
    sachiko "\"When? Where?\""

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1194"
    miyako "\"Yesterday, in the broadcasting room.\""

    voice "2SA_1077"
    sachiko "\"Huh? What?\""

    "Miyako's response only made Sachiko more confused."

    $ side_image = "miyako 1 side school_a_sei e"

    voice "2MI_1195"
    miyako "\"Though it's not like we actually talked. It was a one-sided meeting.\""

    $ side_image = "miyako 1 side school_b_sei i"

    voice "2MI_1196"
    miyako "\"I couldn't touch her or speak to her, but Noel was definitely there, and I saw and heard her.\""

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1197"
    miyako "\"I didn't know what was happening at first either. When I first saw her, I thought she was a doppelgänger or something.\""

    $ side_image = "miyako 1 side school_b_sei a"

    voice "2MI_1198"
    miyako "\"But the me that I saw started smoking, so I realized it wasn't really me...\""

    voice "2SA_1078"
    sachiko "\"Wait, wait! Help me understand.\""

    $ side_image = "miyako 1 side school_a_sei g"

    voice "2MI_1199"
    miyako "\"Oh... I'm sorry.\""

    "Miyako took a breath and began again."

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1200"
    miyako "\"After you left the room yesterday, I saw a record of the past.\""

    scene kimihane_03_i with Dissolve(0.5)

    voice "2SA_1079"
    sachiko "\"A record? There's no Device like that in that room...\""

    $ side_image = "miyako 1 side school_a_sei j"

    voice "2MI_1201"
    miyako "\"The room itself is the Device. It wasn't just the transceiver.\""

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1202"
    miyako "\"That room held a record of the events that took place inside it all this time. Like the jeweled box in Urashima Taro.\""

    voice "2SA_1080"
    sachiko "\"......\""

    voice "2SA_1081"
    sachiko "\"But why? I've never seen anything like that in that room. And I've been there way more than you have.\""

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1203"
    miyako "\"I don't know why I saw it either. I only saw it that one time, too.\""

    scene kimihane_03_j with Dissolve(0.5)

    voice "2SA_1082"
    sachiko "\"...Maybe it's because there's still a little angel in you.\""

    "She had a smile on her face that was doubtful, jealous."

    voice "2SA_1083"
    sachiko "\"So, what'd you see?\""

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1204"
    miyako "\"I saw Christmas morning, five years ago. You were there, sleeping under the desk, wrapped up in a blanket.\""

    voice "2SA_1084"
    sachiko "\"I see...\""

    "Miyako had no way of knowing about that. Sachiko's doubt faded."

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1204a"
    miyako "\"It was the morning after you came down to the surface. And it was Noel's...\""

    scene kimihane_03_i with Dissolve(0.5)

    voice "2SA_1086"
    sachiko "\"......\""

    voice "2SA_1087"
    sachiko "\"Did she say something? I was asleep, so I don't know.\""

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1205"
    miyako "\"She called you a coward.\""

    voice "2SA_1088"
    sachiko "\"God, she pisses me off...\""

    "She ground her teeth in frustration. There was no way for her to dispute it now, after all."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1206"
    miyako "\"But she was also really thankful that you were by her side.\""

    voice "2SA_1089"
    sachiko "\"Hmph. She'd never say that to my face. But I'm the coward?\""

    $ side_image = "miyako 1 side school_a_sei c"

    voice "2MI_1207"
    miyako "\"Heheh.\""

    scene kimihane_03_g with Dissolve(0.5)

    voice "2SA_1090"
    sachiko "\"What?\""

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1208"
    miyako "\"You two are so different, but you're kind of alike, too.\""

    voice "2SA_1091"
    sachiko "\"...We're just both stubborn.\""

    pause 0.5

    scene white with Dissolve(0.1875)
    pause 2.0625

    scene bg08ba with bg_effect_05
    pause 0.5

    "Miyako relayed the things she'd seen and heard in the broadcasting room as candidly as she could to Sachiko."

    pause 0.5

    scene kimihane_03_f with Dissolve(0.5)
    pause 1.5

    voice "2SA_1092"
    sachiko "\"It's easy for her to just say, 'forget me.' Maybe that's all we were to her.\""

    "Sachiko looked up to the sky and blew out some smoke."

    $ side_image = "miyako 1 side school_a_sei j"

    voice "2MI_1209"
    miyako "\"That's not—\""

    voice "2SA_1093"
    sachiko "\"I know.\""

    "Sachiko cut Miyako off when she tried to correct her."

    voice "2SA_1094"
    sachiko "\"I told you, we're stubborn.\""

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1210"
    miyako "\"......\""

    scene kimihane_03_i with Dissolve(0.5)

    voice "2SA_1095"
    sachiko "\"That portrait of Noel... I painted it right after she died.\""

    $ side_image = "miyako 2 side school_sei f"

    voice "2MI_1211"
    miyako "\"Huh...?\""

    voice "2SA_1096"
    sachiko "\"It looks the way it does because I'd just become human. I was still pretty clumsy.\""

    "Miyako shook her head."

    voice "2SA_1097"
    sachiko "\"But I was desperate. I just had to get her down on the canvas. Because memories evaporate faster than oil paint.\""

    voice "2SA_1098"
    sachiko "\"But no matter how hard you cling to memories, humans just can't hold on to them. Even if the portrait I painted stayed the same, my memory of Noel's face faded over time.\""

    voice "2SA_1099"
    sachiko "\"—And that's when you showed up.\""

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1212"
    miyako "\"......\""

    voice "2SA_1100"
    sachiko "\"As I watched you move and talk, the outline of Noel in my memories seemed to get clearer. But...\""

    "Sachiko thought for as long as it took to finish her shortened cigarette. Miyako waited in silence for her to continue."

    voice "2SA_1101"
    sachiko "\"I wasn't sure if the outline was really hers or if it was yours. I got scared of falling in love with you because I was seeing her. So I tried to run away.\""

    voice "2SA_1102"
    sachiko "\"How selfish, right? Totally not fair to you.\""

    "She's really not nailing that smile."

    stop music fadeout 1.0

    $ side_image = "miyako 1 side school_a_sei k"

    voice "2MI_1213"
    miyako "\"But!\""

    scene kimihane_03_m with Dissolve(0.5)

    "Miyako stood up."

    voice "2SA_1103"
    sachiko "\"It's pretty windy. That's not very safe.\""

    "Miyako paid no heed to Sachiko's warning, raising her voice above the wind."

    pause 0.5

    show bg_obi
    show miyako 1 lg school_a_sei k:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    pause 0.5

    play music bgm08 fadein 1.0

    voice "2MI_1214"
    miyako "\"I don't mind if you're seeing Noel! Because we look the same!\""

    voice "2MI_1215"
    miyako "\"And I don't want you to forget Noel! I know how important she is to you! I want to love you {i}and{/i} your feelings for Noel!\""

    show miyako 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1216"
    miyako "\"I can't be her. But I want to spend the time with you that she wanted to spend with you.\""

    scene kimihane_03_t with Dissolve(0.5)

    voice "2SA_1104"
    sachiko "\"...Pfft.\""

    "There was a beat of silence after Miyako's impassioned speech, and then Sachiko burst out laughing."

    show miyako 1 lg school_a_sei g:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1217"
    miyako "\"Huh? I'm being serious.\""

    voice "2SA_1105"
    sachiko "\"I'm sorry... You two are really nothing alike, but... you also kind of are.\""

    show miyako 2 lg school_sei b with dict_dissolve_25

    voice "2MI_1218"
    miyako "\"Are... Are we?\""

    voice "2SA_1106"
    sachiko "\"Like how pushy you are.\""

    show miyako 1 lg school_b_sei g with dict_dissolve_25

    voice "2MI_1219"
    miyako "\"I'm... pushy?\""

    "All the more so since you're not aware of it."

    show miyako 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1220"
    miyako "\"So, what do you think?\""

    scene kimihane_03_s with Dissolve(0.5)

    voice "2SA_1107"
    sachiko "\"What do I think...?\""

    voice "2MI_1221"
    miyako "\"......\""

    "See?"

    voice "2SA_1108"
    sachiko "\"......Hahh.\""

    "Sachiko took a good few minutes to agonize about it, Miyako waiting quietly the whole time."

    voice "2SA_1109"
    sachiko "\"They're my own feelings, but honestly, I don't know. And I don't know what'll happen after this, either.\""

    voice "2SA_1110"
    sachiko "\"I might keep you waiting a long time and then end up just saying goodbye anyway. Is that okay? You'll still wait?\""

    show miyako 1 lg school_a_sei i:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1222"
    miyako "\"I'll wait!\""

    "An instant reply."

    voice "2SA_1111"
    sachiko "\"I really wanted you to enjoy the surface and your life for your own sake, but...\""


    show miyako 1 lg school_a_sei c
    show miyako_1_lg_school_a_sei_m as miyako_1 behind miyako:
        zoom 0.8 xoffset -308 yoffset -272
    with dict_dissolve_25

    voice "2MI_1223a"
    miyako "\"I'll say the same thing right back to you.\""

    show miyako 1 lg school_a_sei c
    hide miyako_1
    with dict_dissolve_25

    voice "2SA_1112"
    sachiko "\"When you say it with that face, it's like you and Noel are teaming up on me.\""

    show miyako 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1224"
    miyako "\"I know I can't replace Noel. And I don't know if I can make you happy.\""

    voice "2SA_1113"
    sachiko "\"You're not a replacement for her...\""

    show miyako 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1225"
    miyako "\"But the fact that I chose this form and found you... I want to believe in that coincidence.\""

    voice "2SA_1114"
    sachiko "\"I told you—\""

    show miyako 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_1226"
    miyako "\"You are my happiness. I'm staying here for you. So I'm making this choice for myself...\""

    show miyako 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_1227"
    miyako "\"I love you.\""

    play sound se_wind03
    pause 1.0

    "Sure is windy today."

    scene kimihane_03_m with Dissolve(0.5)

    voice "2SA_1115"
    sachiko "\"W-Well, let's start as friends.\""

    show miyako 1 lg school_a_sei a:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1228"
    miyako "\"Well, alright... If that's what you want.\""

    "They both smiled lopsidedly at each other."

    voice "2SA_1116"
    sachiko "\"Well... I {i}am{/i} a coward.\""

    show miyako 2 lg school_sei d with dict_dissolve_25

    voice "2MI_1229"
    miyako "\"This one's real trouble, Noel.\""

    "Isn't she?"

    scene kimihane_03_r with Dissolve(0.5)

    voice "2SA_1117"
    sachiko "\"Let's take it slow. Come down from there for now.\""

    "Sachiko held her hand out to Miyako."

    show miyako 1 lg school_a_sei b:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1230"
    miyako "\"Okay.\""

    python:
        _last_say_what = ""
        _last_say_who = None
        renpy.choice_for_skipping()

    stop music fadeout 1.0

    scene select_back4 with Dissolve(0.5)
    pause 1.5

    menu:
        "■選択肢１枠"((437,271), "menu/btn_select_0801"):
            jump a11_cou4_12_g

label a11_cou4_12_g:

    scene kimihane_03_r
    show miyako 1 lg school_a_sei b:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    play sound se_wind02

    show miyako 1 lg school_a_sei f:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    show miyako:
        xcenter 252 ycenter 921
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2MI_1231"
    miyako "\"Wah!\""

    show miyako:
        xoffset 0 yoffset 0 xcenter 252 ycenter 921
    with None
    scene kimihane_03_n with Dissolve(0.5)

    "A gust hit Miyako's back."

    "She lost her balance, foot stepping out onto air instead of concrete."

    window hide
    show white:
        alpha 1.0 additive 1.0
        linear 0.3 alpha 0.0
        repeat 2
    pause 0.6
    window auto
    pause 0.5

    scene white with Dissolve(0.1875)
    pause 1.0625

    voice "2SA_1118"
    sachiko "\"Miyako!\""

    "The cigarette fell from Sachiko's lips, drawing a white line in the air as it made its way to the roof."

    "She was already running when she shouted."

    voice "2MI_1232"
    miyako "\"Sachiko.\""

    "Miyako watched Sachiko underneath her as she fell."

    "Her scarf flapped in the wind, a pair of tiny wings to carry the grounded angel just a little bit farther."

    show bati at truecenter

    pause 1.0

    show kimikara_11_a at truecenter:
        zoom 1.12
        easein 0.75 zoom 1.0

    show kimikara_11_a as kimikara_11_a_1 at truecenter:
        alpha 1.0 zoom 1.0
        easein 0.75 alpha 0.0 zoom 1.75

    show white zorder 1:
        alpha 1.0
        linear 0.75 alpha 0.0

    pause 1.25

    "—Well, of course she's gonna make it."

    "Miyako alighted into Sachiko's open arms. It was just like that Christmas Eve night, but also the opposite of it—"

    play music bgm09 fadein 1.0

    scene kimikara_11_b with Dissolve(0.5)

    voice "2MI_1233"
    miyako "\"I did it again. I'm not an angel anymore, am I?\""

    voice "2SA_1119"
    sachiko "\"Seriously... When are you gonna remember you don't have wings anymore?\""

    voice "2MI_1234"
    miyako "\"I'm sorry.\""

    voice "2SA_1120"
    sachiko "\"Don't scare me like that. If something happens to you, it's the dorm manager who's gonna be the one in trouble.\""

    voice "2MI_0984"
    miyako "\"I know...\""

    voice "2SA_1121"
    sachiko "\"...I don't want to lose anyone else here.\""

    voice "2MI_1236"
    miyako "\"Sachiko...\""

    voice "2SA_1122"
    sachiko "\"I might not have an answer for you until my final moments, okay? So you have to promise to live longer than me.\""

    voice "2MI_1237"
    miyako "\"...Can you give me an answer while we still have our youth?\""

    voice "2SA_1123"
    sachiko "\"Hey, you were the one who said you were gonna wait.\""

    scene white with Dissolve(0.125)
    pause 0.875

    scene bg08ba with Dissolve(0.25)
    pause 0.75

    play sound se_2s_h004

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False
    pause 1.5

    camera
    with None

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_1124"
    sachiko "\"Haah... Not this again. This is taking the physical affection a little too far, isn't it?\""

    "Sachiko sighed underneath Miyako."

    $ side_image = "miyako 1 side school_a_sei e"

    voice "2MI_1238"
    miyako "\"......\""

    "Miyako stared up at her face."

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_1125"
    sachiko "\"What is it?\""

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_1239"
    miyako "\"Will there be funny business now?\""

    $ side_image = "sachiko 2 side outfit h"

    voice "2SA_1126"
    sachiko "\"What?\""

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1240"
    miyako "\"Can we continue where we left off after the hot pot?\""

    $ side_image = "sachiko 2 side outfit j"

    voice "2SA_1127"
    sachiko "\"......\""

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_1128"
    sachiko "\"...You'd do it even if I said no. Just a little, okay?\""

    $ side_image = "miyako 1 side school_a_sei d"

    voice "2MI_1241"
    miyako "\"Okay♪\""

    "Miyako's face lit up when she got her permission."

    if persistent.dpatch:
        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1129"
        sachiko "\"Mm, it's a special occasion, okay... Hey, wait! What are you trying to strip me for?!\""

        $ side_image = "miyako 2 side school_sei a"

        voice "2MI_1242"
        miyako "\"I can't?\""

        "Miyako tilted her head, an innocent look on her face as she went for Sachiko's shirt."

        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1130"
        sachiko "\"Of course you can't! Actually, what made you think you could?!\""

        "Apparently, she has some dirty expectations for \"special occasions.\""

        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1131"
        sachiko "\"We'll catch colds if we do that here anyway!\""

        $ side_image = "miyako 1 side school_b_sei h"

        voice "2MI_1243"
        miyako "\"I'm a big idiot right now so I won't catch one.\""

        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1132"
        sachiko "\"Well, I'm not, so I will!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_13
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
