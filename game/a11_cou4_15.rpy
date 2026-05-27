label a11_cou4_15:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_15:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09da with Dissolve(0.25)
    pause 0.75

    play music bgm02 fadein 1.0

    "A darkened room."

    if persistent.dpatch:
        "Sachiko sat naked on the bed, looking up at the moon out the window."

    if persistent.dpatch:
        show sachiko 2 lg znd c with dict_dissolve_25
    else:
        show sachiko 2 lg outfit c with dict_dissolve_25

    voice "2SA_1179"
    sachiko "\"Haah... It's the middle of the night already~\"" id a11_cou4_15_ccff0f47

    if persistent.dpatch:
        show sachiko 2 lg znd f with dict_dissolve_25
    else:
        show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_1180"
    sachiko "\"Haha, you're just full of energy. Unlike her.\"" id a11_cou4_15_6149cdd6

    "Miyako was asleep on the bed."

    if persistent.dpatch:
        show sachiko 2 lg znd j with dict_dissolve_25
    else:
        show sachiko 2 lg outfit j with dict_dissolve_25

    voice "2SA_1181"
    sachiko "\"Ouch... Meanwhile, your big sis's back hurts...\"" id a11_cou4_15_d063df58

    "Sachiko rubbed her back."

    "Miyako had practically chased her into the room, going after her again and again, which had led to her current predicament."

    if persistent.dpatch:
        show sachiko 2 lg znd i with dict_dissolve_25
    else:
        show sachiko 2 lg outfit i with dict_dissolve_25

    voice "2SA_1182"
    sachiko "\"...I really am a pushover, aren't I?\"" id a11_cou4_15_a54455b9

    "You really are."

    play sound se_tabaco

    hide sachiko with dict_dissolve_50

    "Sachiko stood up unsteadily and grabbed a cigarette from her desk, lighting it."

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_b e"
    else:
        $ side_image = "miyako 1 side pyjama_b e"

    voice "2MI_1286"
    miyako "\"You don't have any marks on your back from your wings.\"" id a11_cou4_15_f77821fa

    "She heard from behind her."

    if persistent.dpatch:
        show sachiko z4 2 lg znd cigarette f with dict_dissolve_25
    else:
        show sachiko z4 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_1183"
    sachiko "\"Hm? Did I wake you?\"" id a11_cou4_15_7755074e

    "Miyako shook her head."

    if persistent.dpatch:
        show sachiko z4 1 lg znd cigarette a with dict_dissolve_25
    else:
        show sachiko z4 1 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_1184"
    sachiko "\"Yeah, mine are completely gone. You're still a little bit of an angel, though.\"" id a11_cou4_15_c9b16e34

    "Miyako cocked her head and tried to look over her shoulder at her back."

    voice "2SA_1185"
    sachiko "\"The marks will fade and disappear over time. Just like the memories.\"" id a11_cou4_15_cfafd360

    "Sachiko slowly blew out smoke."

    if persistent.dpatch:
        show sachiko z4 1 lg znd cigarette i with dict_dissolve_25
    else:
        show sachiko z4 1 lg outfit cigarette i with dict_dissolve_25

    voice "2SA_1186"
    sachiko "\"Every time you fall in love, you'll get stupider and stupider.\"" id a11_cou4_15_828a715e

    if persistent.dpatch:
        $ side_image = "miyako 2 side znd a"
    else:
        $ side_image = "miyako 2 side pyjama a"

    voice "2MI_1287"
    miyako "\"?\"" id a11_cou4_15_e255275b

    if persistent.dpatch:
        show sachiko z4 2 lg znd cigarette c with dict_dissolve_25
    else:
        show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_1187"
    sachiko "\"Love takes up such a vast capacity. These tiny little heads fill up with it right away, and it overwrites everything in there.\"" id a11_cou4_15_886e4a09

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_b g"
    else:
        $ side_image = "miyako 1 side pyjama_b g"

    voice "2MI_1288"
    miyako "\"Noel said the same thing.\"" id a11_cou4_15_18b44a4c

    if persistent.dpatch:
        show sachiko z4 2 lg znd cigarette e with dict_dissolve_25
    else:
        show sachiko z4 2 lg outfit cigarette e with dict_dissolve_25

    voice "2SA_1188"
    sachiko "\"Well, I get it all from—\"" id a11_cou4_15_662abd1f

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a b"
    else:
        $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_1289"
    miyako "\"No. She's still alive inside you.\"" id a11_cou4_15_a4e3e9db

    if persistent.dpatch:
        show sachiko z4 2 lg znd cigarette c with dict_dissolve_25
    else:
        show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_1189"
    sachiko "\"......\"" id a11_cou4_15_c67f92ea

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a c"
    else:
        $ side_image = "miyako 1 side pyjama_a c"

    voice "2MI_1290"
    miyako "\"So even if you get stupid, you won't forget her. Every time you remember her, it'll overwrite something.\"" id a11_cou4_15_19140307

    "This kid..."

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a h"
    else:
        $ side_image = "miyako 1 side pyjama_a h"

    voice "2MI_1291"
    miyako "\"Please tell me about her sometime. I want her to live inside me as well.\"" id a11_cou4_15_37639840

    "Thanks."

    if persistent.dpatch:
        show sachiko z4 1 lg znd cigarette f with dict_dissolve_25
    else:
        show sachiko z4 1 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_1190"
    sachiko "\"That's... well, I guess it's a story for another time.\"" id a11_cou4_15_eb5e63bd

    if persistent.dpatch:
        $ side_image = "miyako 2 side znd c"
    else:
        $ side_image = "miyako 2 side pyjama c"

    voice "2MI_1292"
    miyako "\"Not again~\"" id a11_cou4_15_d1332cee

    if persistent.dpatch:
        show sachiko z4 1 lg znd cigarette g with dict_dissolve_25
    else:
        show sachiko z4 1 lg outfit cigarette g with dict_dissolve_25

    voice "2SA_1191"
    sachiko "\"Heheh.\"" id a11_cou4_15_da75efc7

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a e"
    else:
        $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_1293"
    miyako "\"...Would you have fallen for me if I wasn't in this form?\"" id a11_cou4_15_6a549c03

    if persistent.dpatch:
        show sachiko z4 1 lg znd cigarette a with dict_dissolve_25
    else:
        show sachiko z4 1 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_1192"
    sachiko "\"......\"" id a11_cou4_15_d412e9c6

    hide sachiko with dict_dissolve_50

    "Sachiko bent down silently and kissed her."

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_b l"
    else:
        $ side_image = "miyako 1 side pyjama_b l"

    voice "2MI_1294"
    miyako "\"...You taste like cigarettes.\"" id a11_cou4_15_6eb36cc7

    "Miyako ran her fingers over her lips."

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a k"
    else:
        $ side_image = "miyako 1 side pyjama_a k"

    voice "2MI_1295"
    miyako "\"Ah! Cigarettes are bad for you. Please quit smoking, for your health!\"" id a11_cou4_15_814be330

    "She came back to her senses and tried to snatch the cigarette from Sachiko."

    if persistent.dpatch:
        show sachiko 1 lg znd cigarette c with dict_dissolve_25
    else:
        show sachiko 1 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_1193"
    sachiko "\"Where'd that come from? You're giving me life advice now?\"" id a11_cou4_15_9076f912

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a k"
    else:
        $ side_image = "miyako 1 side pyjama_a k"

    voice "2MI_1296"
    miyako "\"Yep!\"" id a11_cou4_15_667333b2

    voice "2SA_1194"
    sachiko "\"You know, if you're too strict, I might just walk out one day.\"" id a11_cou4_15_90e25fef

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a b"
    else:
        $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_1297"
    miyako "\"You couldn't. You're too cowardly.\"" id a11_cou4_15_5619d4ef

    "She giggled. That's right."

    if persistent.dpatch:
        show sachiko 1 lg znd cigarette b with dict_dissolve_25
    else:
        show sachiko 1 lg outfit cigarette b with dict_dissolve_25

    voice "2SA_1195"
    sachiko "\"...Ugh, this is gonna be tough.\"" id a11_cou4_15_eec22b81

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a b"
    else:
        $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_1298"
    miyako "\"Humans have bodies, you know.\"" id a11_cou4_15_c69d3cf4

    "Miyako reminded Sachiko of her own lessons."

    if persistent.dpatch:
        show sachiko 1 lg znd cigarette c with dict_dissolve_25
    else:
        show sachiko 1 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_1196"
    sachiko "\"I know that.\"" id a11_cou4_15_78322f33

    if persistent.dpatch:
        $ side_image = "miyako 1 side znd_a c"
    else:
        $ side_image = "miyako 1 side pyjama_a c"

    voice "2MI_1299"
    miyako "\"I want to spend as much time as I can with you, even if it's just one more day.\"" id a11_cou4_15_95842fc1

    if persistent.dpatch:
        show sachiko 2 lg znd cigarette f with dict_dissolve_25
    else:
        show sachiko 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_1197"
    sachiko "\"...You're no fair, Mikoyan.\"" id a11_cou4_15_e4b14455

    if persistent.dpatch:
        $ side_image = "miyako 2 side znd c"
    else:
        $ side_image = "miyako 2 side pyjama c"

    voice "2MI_1300"
    miyako "\"And when are you going to call me Miyako? You were the one who gave me the name, you know.\"" id a11_cou4_15_9cc05fc3

    if persistent.dpatch:
        show sachiko 1 lg znd cigarette d with dict_dissolve_25
    else:
        show sachiko 1 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_1198"
    sachiko "\"I know~\"" id a11_cou4_15_a558be47

    if persistent.dpatch:
        show sachiko:
            "sachiko 1 lg znd -cigarette d" with Dissolve(0.25)
            ShakeTameiki
    else:
        show sachiko:
            "sachiko 1 lg outfit -cigarette d" with Dissolve(0.25)
            ShakeTameiki

    "Sachiko put the cigarette out in an ashtray without even smoking half of it."

    if persistent.dpatch:








        show sachiko 1 lg znd -cigarette d:
            xoffset 0 yoffset 0
        with None





        $ side_image = "miyako 1 side znd_b b"

        voice "2MI_1301"
        miyako "\"Well, then—\"" id a11_cou4_15_51c879b3





        show sachiko 1 lg znd h with dict_dissolve_25

        voice "2SA_1199"
        sachiko "\"Hwah?\"" id a11_cou4_15_d20eb856

        play sound se_2s_g001

        hide sachiko with dict_dissolve_50
        camera:
            function LayerShake(5,5,0.3)
        $ persistent.layer_shaken = False

        "Miyako suddenly grabbed Sachiko's wrist and pulled her to her."

        camera
        with None





        $ side_image = "miyako 1 side znd_a d"

        voice "2MI_1302"
        miyako "\"Life is short. Let's get stupider. Enough for Noel, too!\"" id a11_cou4_15_c0efd93c





        $ side_image = "sachiko 2 side znd h"

        voice "2SA_1200"
        sachiko "\"What are you, bottomless?! G-Gimme a break... I need rest! Rest!\"" id a11_cou4_15_ecdc5051

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_16
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
