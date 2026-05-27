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
    sachiko "\"Pwah! Windy!\"" id a11_cou4_12_c43d9605

    "As soon as she opened the door, the wind blew her hair every which way."

    "Holding it down, Sachiko looked around and spotted Miyako."

    "She was sitting in the same spot she had on that Christmas Eve night."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1068"
    sachiko "\"Do you miss the sky?\"" id a11_cou4_12_f8223870

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
    miyako "\"You found me right away.\"" id a11_cou4_12_88cc3d7a

    voice "2SA_1069"
    sachiko "\"I saw your shoes at the door. The rest was easy enough.\"" id a11_cou4_12_13e63cdb

    "Sachiko tapped her temple."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1188"
    miyako "\"The brilliant detective.\"" id a11_cou4_12_63934500

    "Angels and smoke like high places."

    voice "2SA_1070"
    if persistent.dpatch:
        sachiko "\"This time I know you should still be in school.\"" id a11_cou4_12_28209e99
    else:
        sachiko "\"This time I know you should still be in class.\"" id a11_cou4_12_878ddf39

    $ side_image = "miyako 1 side school_a_sei c"

    voice "2MI_1189"
    miyako "\"I went home early.\"" id a11_cou4_12_bf6799ed

    voice "2SA_1071"
    sachiko "\"What a bad girl.\"" id a11_cou4_12_053f14cd

    "She breathed out some smoke. Her disapproval didn't sound particularly genuine."

    voice "2SA_1072"
    sachiko "\"So? Are you going right back up there?\"" id a11_cou4_12_fa3a299e

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_1190"
    miyako "\"Huh? Can you do that?\"" id a11_cou4_12_7716debf

    voice "2SA_1073"
    sachiko "\"I guess I don't know. Do you want to? That'd be a pretty quick turn-around.\"" id a11_cou4_12_0c91d46a

    $ side_image = "miyako 1 side school_b_sei h"

    voice "2MI_1191"
    miyako "\"Ahaha. I have no plans to return right now.\"" id a11_cou4_12_32b4e99f

    voice "2SA_1074"
    sachiko "\"There's plenty more to see on the surface, after all.\"" id a11_cou4_12_41434250

    $ side_image = "miyako 2 side school_sei d"

    voice "2MI_1192"
    miyako "\"But if I could go back to being an angel—\"" id a11_cou4_12_795850b9

    pause 0.5

    scene white with Dissolve(0.3)
    pause 0.5

    show a11_cou4_12_grayscale01 at truecenter with Dissolve(1.0)
    pause 0.5

    voice "2NO_0034"
    noel "\"Aww~ I wonder if I can become an angel when I die... Then I could watch over her forever.\"" id a11_cou4_12_0b4d3fcf

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
    miyako "\"I met Noel.\"" id a11_cou4_12_90adb791

    scene kimihane_03_l with Dissolve(0.5)

    voice "2SA_1075"
    sachiko "\"Huh...?\"" id a11_cou4_12_7e5f0973

    "She almost let the cigarette fall from her lips at the unexpected announcement."

    voice "2SA_1076"
    sachiko "\"When? Where?\"" id a11_cou4_12_6546b3b2

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1194"
    miyako "\"Yesterday, in the broadcasting room.\"" id a11_cou4_12_b3691f0a

    voice "2SA_1077"
    sachiko "\"Huh? What?\"" id a11_cou4_12_38502f97

    "Miyako's response only made Sachiko more confused."

    $ side_image = "miyako 1 side school_a_sei e"

    voice "2MI_1195"
    miyako "\"Though it's not like we actually talked. It was a one-sided meeting.\"" id a11_cou4_12_e0f79cbe

    $ side_image = "miyako 1 side school_b_sei i"

    voice "2MI_1196"
    miyako "\"I couldn't touch her or speak to her, but Noel was definitely there, and I saw and heard her.\"" id a11_cou4_12_704cf7fe

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1197"
    miyako "\"I didn't know what was happening at first either. When I first saw her, I thought she was a doppelgänger or something.\"" id a11_cou4_12_879005de

    $ side_image = "miyako 1 side school_b_sei a"

    voice "2MI_1198"
    miyako "\"But the me that I saw started smoking, so I realized it wasn't really me...\"" id a11_cou4_12_c6daa054

    voice "2SA_1078"
    sachiko "\"Wait, wait! Help me understand.\"" id a11_cou4_12_b28d6da3

    $ side_image = "miyako 1 side school_a_sei g"

    voice "2MI_1199"
    miyako "\"Oh... I'm sorry.\"" id a11_cou4_12_1dc4b39b

    "Miyako took a breath and began again."

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1200"
    miyako "\"After you left the room yesterday, I saw a record of the past.\"" id a11_cou4_12_7c3e95f8

    scene kimihane_03_i with Dissolve(0.5)

    voice "2SA_1079"
    sachiko "\"A record? There's no Device like that in that room...\"" id a11_cou4_12_bc8f993a

    $ side_image = "miyako 1 side school_a_sei j"

    voice "2MI_1201"
    miyako "\"The room itself is the Device. It wasn't just the transceiver.\"" id a11_cou4_12_234c827d

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1202"
    miyako "\"That room held a record of the events that took place inside it all this time. Like the jeweled box in Urashima Taro.\"" id a11_cou4_12_361b955a

    voice "2SA_1080"
    sachiko "\"......\"" id a11_cou4_12_51ce0929

    voice "2SA_1081"
    sachiko "\"But why? I've never seen anything like that in that room. And I've been there way more than you have.\"" id a11_cou4_12_8dc3b3f1

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1203"
    miyako "\"I don't know why I saw it either. I only saw it that one time, too.\"" id a11_cou4_12_b0c5e0a5

    scene kimihane_03_j with Dissolve(0.5)

    voice "2SA_1082"
    sachiko "\"...Maybe it's because there's still a little angel in you.\"" id a11_cou4_12_98f6eae6

    "She had a smile on her face that was doubtful, jealous."

    voice "2SA_1083"
    sachiko "\"So, what'd you see?\"" id a11_cou4_12_70218bc4

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1204"
    miyako "\"I saw Christmas morning, five years ago. You were there, sleeping under the desk, wrapped up in a blanket.\"" id a11_cou4_12_416e72b2

    voice "2SA_1084"
    sachiko "\"I see...\"" id a11_cou4_12_353452e3

    "Miyako had no way of knowing about that. Sachiko's doubt faded."

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1204a"
    miyako "\"It was the morning after you came down to the surface. And it was Noel's...\"" id a11_cou4_12_c7247cad

    scene kimihane_03_i with Dissolve(0.5)

    voice "2SA_1086"
    sachiko "\"......\"" id a11_cou4_12_f66ffe1e

    voice "2SA_1087"
    sachiko "\"Did she say something? I was asleep, so I don't know.\"" id a11_cou4_12_a066f422

    $ side_image = "miyako 1 side school_a_sei a"

    voice "2MI_1205"
    miyako "\"She called you a coward.\"" id a11_cou4_12_0bd99e98

    voice "2SA_1088"
    sachiko "\"God, she pisses me off...\"" id a11_cou4_12_e87ce339

    "She ground her teeth in frustration. There was no way for her to dispute it now, after all."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1206"
    miyako "\"But she was also really thankful that you were by her side.\"" id a11_cou4_12_91fbf3c9

    voice "2SA_1089"
    sachiko "\"Hmph. She'd never say that to my face. But I'm the coward?\"" id a11_cou4_12_1da355e3

    $ side_image = "miyako 1 side school_a_sei c"

    voice "2MI_1207"
    miyako "\"Heheh.\"" id a11_cou4_12_6dd6ea25

    scene kimihane_03_g with Dissolve(0.5)

    voice "2SA_1090"
    sachiko "\"What?\"" id a11_cou4_12_89369b0a

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1208"
    miyako "\"You two are so different, but you're kind of alike, too.\"" id a11_cou4_12_08b9bc21

    voice "2SA_1091"
    sachiko "\"...We're just both stubborn.\"" id a11_cou4_12_78e38ccb

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
    sachiko "\"It's easy for her to just say, 'forget me.' Maybe that's all we were to her.\"" id a11_cou4_12_b5dda704

    "Sachiko looked up to the sky and blew out some smoke."

    $ side_image = "miyako 1 side school_a_sei j"

    voice "2MI_1209"
    miyako "\"That's not—\"" id a11_cou4_12_e6218215

    voice "2SA_1093"
    sachiko "\"I know.\"" id a11_cou4_12_109aaed8

    "Sachiko cut Miyako off when she tried to correct her."

    voice "2SA_1094"
    sachiko "\"I told you, we're stubborn.\"" id a11_cou4_12_8e94fd3d

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1210"
    miyako "\"......\"" id a11_cou4_12_97ef0fa2

    scene kimihane_03_i with Dissolve(0.5)

    voice "2SA_1095"
    sachiko "\"That portrait of Noel... I painted it right after she died.\"" id a11_cou4_12_877d16d3

    $ side_image = "miyako 2 side school_sei f"

    voice "2MI_1211"
    miyako "\"Huh...?\"" id a11_cou4_12_e87bcbd4

    voice "2SA_1096"
    sachiko "\"It looks the way it does because I'd just become human. I was still pretty clumsy.\"" id a11_cou4_12_cc391056

    "Miyako shook her head."

    voice "2SA_1097"
    sachiko "\"But I was desperate. I just had to get her down on the canvas. Because memories evaporate faster than oil paint.\"" id a11_cou4_12_f97f6862

    voice "2SA_1098"
    sachiko "\"But no matter how hard you cling to memories, humans just can't hold on to them. Even if the portrait I painted stayed the same, my memory of Noel's face faded over time.\"" id a11_cou4_12_eba7096e

    voice "2SA_1099"
    sachiko "\"—And that's when you showed up.\"" id a11_cou4_12_8a6bddc6

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1212"
    miyako "\"......\"" id a11_cou4_12_45dabde4

    voice "2SA_1100"
    sachiko "\"As I watched you move and talk, the outline of Noel in my memories seemed to get clearer. But...\"" id a11_cou4_12_8b9ad778

    "Sachiko thought for as long as it took to finish her shortened cigarette. Miyako waited in silence for her to continue."

    voice "2SA_1101"
    sachiko "\"I wasn't sure if the outline was really hers or if it was yours. I got scared of falling in love with you because I was seeing her. So I tried to run away.\"" id a11_cou4_12_7a3f1ef3

    voice "2SA_1102"
    sachiko "\"How selfish, right? Totally not fair to you.\"" id a11_cou4_12_a7cb3645

    "She's really not nailing that smile."

    stop music fadeout 1.0

    $ side_image = "miyako 1 side school_a_sei k"

    voice "2MI_1213"
    miyako "\"But!\"" id a11_cou4_12_80f67a63

    scene kimihane_03_m with Dissolve(0.5)

    "Miyako stood up."

    voice "2SA_1103"
    sachiko "\"It's pretty windy. That's not very safe.\"" id a11_cou4_12_621adb0c

    "Miyako paid no heed to Sachiko's warning, raising her voice above the wind."

    pause 0.5

    show bg_obi
    show miyako 1 lg school_a_sei k:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    pause 0.5

    play music bgm08 fadein 1.0

    voice "2MI_1214"
    miyako "\"I don't mind if you're seeing Noel! Because we look the same!\"" id a11_cou4_12_532d2f93

    voice "2MI_1215"
    miyako "\"And I don't want you to forget Noel! I know how important she is to you! I want to love you {i}and{/i} your feelings for Noel!\"" id a11_cou4_12_e2dfce2d

    show miyako 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1216"
    miyako "\"I can't be her. But I want to spend the time with you that she wanted to spend with you.\"" id a11_cou4_12_700f3351

    scene kimihane_03_t with Dissolve(0.5)

    voice "2SA_1104"
    sachiko "\"...Pfft.\"" id a11_cou4_12_39a3211f

    "There was a beat of silence after Miyako's impassioned speech, and then Sachiko burst out laughing."

    show miyako 1 lg school_a_sei g:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1217"
    miyako "\"Huh? I'm being serious.\"" id a11_cou4_12_72cf4713

    voice "2SA_1105"
    sachiko "\"I'm sorry... You two are really nothing alike, but... you also kind of are.\"" id a11_cou4_12_73b033ef

    show miyako 2 lg school_sei b with dict_dissolve_25

    voice "2MI_1218"
    miyako "\"Are... Are we?\"" id a11_cou4_12_87a613ff

    voice "2SA_1106"
    sachiko "\"Like how pushy you are.\"" id a11_cou4_12_ada94684

    show miyako 1 lg school_b_sei g with dict_dissolve_25

    voice "2MI_1219"
    miyako "\"I'm... pushy?\"" id a11_cou4_12_57d02b49

    "All the more so since you're not aware of it."

    show miyako 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1220"
    miyako "\"So, what do you think?\"" id a11_cou4_12_2187a7a3

    scene kimihane_03_s with Dissolve(0.5)

    voice "2SA_1107"
    sachiko "\"What do I think...?\"" id a11_cou4_12_0e645327

    voice "2MI_1221"
    miyako "\"......\"" id a11_cou4_12_fc954994

    "See?"

    voice "2SA_1108"
    sachiko "\"......Hahh.\"" id a11_cou4_12_e2101c62

    "Sachiko took a good few minutes to agonize about it, Miyako waiting quietly the whole time."

    voice "2SA_1109"
    sachiko "\"They're my own feelings, but honestly, I don't know. And I don't know what'll happen after this, either.\"" id a11_cou4_12_dde0079d

    voice "2SA_1110"
    sachiko "\"I might keep you waiting a long time and then end up just saying goodbye anyway. Is that okay? You'll still wait?\"" id a11_cou4_12_b10fb3ec

    show miyako 1 lg school_a_sei i:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1222"
    miyako "\"I'll wait!\"" id a11_cou4_12_5573eaac

    "An instant reply."

    voice "2SA_1111"
    sachiko "\"I really wanted you to enjoy the surface and your life for your own sake, but...\"" id a11_cou4_12_6ea455ab


    show miyako 1 lg school_a_sei c
    show miyako_1_lg_school_a_sei_m as miyako_1 behind miyako:
        zoom 0.8 xoffset -308 yoffset -272
    with dict_dissolve_25

    voice "2MI_1223a"
    miyako "\"I'll say the same thing right back to you.\"" id a11_cou4_12_843b65be

    show miyako 1 lg school_a_sei c
    hide miyako_1
    with dict_dissolve_25

    voice "2SA_1112"
    sachiko "\"When you say it with that face, it's like you and Noel are teaming up on me.\"" id a11_cou4_12_91fb1c94

    show miyako 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1224"
    miyako "\"I know I can't replace Noel. And I don't know if I can make you happy.\"" id a11_cou4_12_8c0fbec2

    voice "2SA_1113"
    sachiko "\"You're not a replacement for her...\"" id a11_cou4_12_496bbeb9

    show miyako 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1225"
    miyako "\"But the fact that I chose this form and found you... I want to believe in that coincidence.\"" id a11_cou4_12_4b31031e

    voice "2SA_1114"
    sachiko "\"I told you—\"" id a11_cou4_12_3163b052

    show miyako 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_1226"
    miyako "\"You are my happiness. I'm staying here for you. So I'm making this choice for myself...\"" id a11_cou4_12_d2230375

    show miyako 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_1227"
    miyako "\"I love you.\"" id a11_cou4_12_0cee793f

    play sound se_wind03
    pause 1.0

    "Sure is windy today."

    scene kimihane_03_m with Dissolve(0.5)

    voice "2SA_1115"
    sachiko "\"W-Well, let's start as friends.\"" id a11_cou4_12_80ed4e99

    show miyako 1 lg school_a_sei a:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1228"
    miyako "\"Well, alright... If that's what you want.\"" id a11_cou4_12_5c12ccac

    "They both smiled lopsidedly at each other."

    voice "2SA_1116"
    sachiko "\"Well... I {i}am{/i} a coward.\"" id a11_cou4_12_e6911a33

    show miyako 2 lg school_sei d with dict_dissolve_25

    voice "2MI_1229"
    miyako "\"This one's real trouble, Noel.\"" id a11_cou4_12_25c1d916

    "Isn't she?"

    scene kimihane_03_r with Dissolve(0.5)

    voice "2SA_1117"
    sachiko "\"Let's take it slow. Come down from there for now.\"" id a11_cou4_12_bd8e12e0

    "Sachiko held her hand out to Miyako."

    show miyako 1 lg school_a_sei b:
        xcenter 252 ycenter 921
    with Dissolve(0.5)

    voice "2MI_1230"
    miyako "\"Okay.\"" id a11_cou4_12_99b64851

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
    miyako "\"Wah!\"" id a11_cou4_12_g_1f084908

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
    sachiko "\"Miyako!\"" id a11_cou4_12_g_0fab67f6

    "The cigarette fell from Sachiko's lips, drawing a white line in the air as it made its way to the roof."

    "She was already running when she shouted."

    voice "2MI_1232"
    miyako "\"Sachiko.\"" id a11_cou4_12_g_0de53778

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
    miyako "\"I did it again. I'm not an angel anymore, am I?\"" id a11_cou4_12_g_5b9ba300

    voice "2SA_1119"
    sachiko "\"Seriously... When are you gonna remember you don't have wings anymore?\"" id a11_cou4_12_g_e8870529

    voice "2MI_1234"
    miyako "\"I'm sorry.\"" id a11_cou4_12_g_0b771d20

    voice "2SA_1120"
    sachiko "\"Don't scare me like that. If something happens to you, it's the dorm manager who's gonna be the one in trouble.\"" id a11_cou4_12_g_06a125e0

    voice "2MI_0984"
    miyako "\"I know...\"" id a11_cou4_12_g_cbce8ba0

    voice "2SA_1121"
    sachiko "\"...I don't want to lose anyone else here.\"" id a11_cou4_12_g_62b61bac

    voice "2MI_1236"
    miyako "\"Sachiko...\"" id a11_cou4_12_g_df0c6096

    voice "2SA_1122"
    sachiko "\"I might not have an answer for you until my final moments, okay? So you have to promise to live longer than me.\"" id a11_cou4_12_g_c9b16a68

    voice "2MI_1237"
    miyako "\"...Can you give me an answer while we still have our youth?\"" id a11_cou4_12_g_9988e5b0

    voice "2SA_1123"
    sachiko "\"Hey, you were the one who said you were gonna wait.\"" id a11_cou4_12_g_3d1f24f2

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
    sachiko "\"Haah... Not this again. This is taking the physical affection a little too far, isn't it?\"" id a11_cou4_12_g_62e3ea83

    "Sachiko sighed underneath Miyako."

    $ side_image = "miyako 1 side school_a_sei e"

    voice "2MI_1238"
    miyako "\"......\"" id a11_cou4_12_g_72fcf96a

    "Miyako stared up at her face."

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_1125"
    sachiko "\"What is it?\"" id a11_cou4_12_g_495e247b

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_1239"
    miyako "\"Will there be funny business now?\"" id a11_cou4_12_g_3af08940

    $ side_image = "sachiko 2 side outfit h"

    voice "2SA_1126"
    sachiko "\"What?\"" id a11_cou4_12_g_722402d2

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_1240"
    miyako "\"Can we continue where we left off after the hot pot?\"" id a11_cou4_12_g_645dcd6c

    $ side_image = "sachiko 2 side outfit j"

    voice "2SA_1127"
    sachiko "\"......\"" id a11_cou4_12_g_7a1ddbfe

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_1128"
    sachiko "\"...You'd do it even if I said no. Just a little, okay?\"" id a11_cou4_12_g_e1499e0a

    $ side_image = "miyako 1 side school_a_sei d"

    voice "2MI_1241"
    miyako "\"Okay♪\"" id a11_cou4_12_g_12f1478f

    "Miyako's face lit up when she got her permission."

    if persistent.dpatch:
        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1129"
        sachiko "\"Mm, it's a special occasion, okay... Hey, wait! What are you trying to strip me for?!\"" id a11_cou4_12_g_39d5ee05

        $ side_image = "miyako 2 side school_sei a"

        voice "2MI_1242"
        miyako "\"I can't?\"" id a11_cou4_12_g_dee953eb

        "Miyako tilted her head, an innocent look on her face as she went for Sachiko's shirt."

        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1130"
        sachiko "\"Of course you can't! Actually, what made you think you could?!\"" id a11_cou4_12_g_f3a6f6e8

        "Apparently, she has some dirty expectations for \"special occasions.\""

        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1131"
        sachiko "\"We'll catch colds if we do that here anyway!\"" id a11_cou4_12_g_e60cc2b9

        $ side_image = "miyako 1 side school_b_sei h"

        voice "2MI_1243"
        miyako "\"I'm a big idiot right now so I won't catch one.\"" id a11_cou4_12_g_4374d823

        $ side_image = "sachiko 2 side outfit h"

        voice "2SA_1132"
        sachiko "\"Well, I'm not, so I will!\"" id a11_cou4_12_g_faa1bc66

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_13
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
