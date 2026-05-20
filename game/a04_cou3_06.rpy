label a04_cou3_06:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    "Just after noon. The messy sheets and disheveled hair were a clear indication of what had just taken place."

    scene white with Dissolve(0.5)
    pause 1.5

    scene ev06e with Dissolve(0.375)
    pause 1.5

    voice "FUM_1184"
    fumi "\"Wah!\""

    "Fumi exclaimed the moment she put the brush to Rin's hair."

    voice "RIN_1357"
    rin "\"Huh? What?\""

    voice "FUM_1185"
    fumi "\"The brush just goes right through it!\""

    voice "RIN_1358"
    rin "\"Oh, that? I thought you found a white hair or something.\""

    voice "FUM_1186"
    fumi "\"It might not be much to you, but think about the people who have unmanageable hair.\""

    voice "RIN_1359"
    rin "\"Yeah, Hina seems like she's at war every morning.\""

    voice "FUM_1187"
    fumi "\"I'm jealous. I wish my hair would behave.\""

    voice "RIN_1360"
    rin "\"But my hair is the only thing that behaves.\""

    voice "FUM_1188"
    fumi "\"You think so? I think your body's very well-behaved. I mean, just\nnow—\""

    scene ev06g with Dissolve(0.5)

    voice "RIN_1361"
    rin "\"Don't say any more.\""

    "Rin hurriedly covered Fumi's mouth."

    scene ev06f with Dissolve(0.5)

    voice "RIN_1362"
    rin "\"My body's just flexible~\""

    "Rin said, bending forward. She pressed her chest to the floor easily and then rose just as effortlessly."

    voice "FUM_1189"
    fumi "\"Oh, wow. It's like you do ballet.\""

    voice "RIN_1363"
    rin "\"I did. I'm glad you didn't say I was like a sumo wrestler.\""

    voice "FUM_1190"
    fumi "\"Did you really?\""

    voice "RIN_1364"
    rin "\"Yeah, only up until middle school, though.\""

    voice "FUM_1191"
    fumi "\"I never knew that.\""

    voice "RIN_1365"
    rin "\"Well, I never told you.\""

    scene ev06b with Dissolve(0.5)

    voice "FUM_1192"
    fumi "\"You should talk about yourself more.\""

    voice "RIN_1366"
    rin "\"There's nothing all that interesting to say.\""

    voice "FUM_1193"
    fumi "\"There you go acting all twisted again. It's the listener who decides if it's interesting or not.\""

    voice "RIN_1367"
    rin "\"Well, maybe some day~\""

    scene ev06a with Dissolve(0.5)

    voice "RIN_1368"
    rin "\"Hwaah... feels good to have your hair brushed. I'm getting kinda sleepy.\""

    voice "FUM_1194"
    fumi "\"Eheheh, my dog always falls asleep when I brush him, too.\""

    voice "RIN_1369"
    rin "\"Your dog's a big one, right?\""

    voice "FUM_1195"
    fumi "\"Yep. He's a retriever.\""

    voice "RIN_1370"
    rin "\"What's his name?\""

    voice "FUM_1196"
    fumi "\"Arthur. His mom lives up with my uncle in Hokkaido, and he has a big brother named Jack at the school where my uncle works.\""

    voice "RIN_1371"
    rin "\"Huh.\""

    voice "FUM_1197"
    fumi "\"...You really seem like you're about to fall asleep.\""

    voice "RIN_1372"
    rin "\"Hm? I'm okay. I'm not sleepy.\""

    "That's what all sleepy people say."

    voice "FUM_1198"
    fumi "\"Eheh, did you work too hard earlier?\""

    scene ev06c with Dissolve(0.5)

    voice "RIN_1373"
    rin "\"...You're kind of a bully lately, Fumi.\""

    voice "FUM_1199"
    fumi "\"A bully? I don't intend to be...\""

    voice "RIN_1374"
    rin "\"It's even worse if you're not trying to do it.\""

    voice "FUM_1200"
    fumi "\"I'll have to start trying, then.\""

    voice "RIN_1375"
    rin "\"What about just not bullying me?!\""

    scene ev06i with Dissolve(0.5)

    voice "FUM_1201"
    fumi "\"Ahaha.\""

    voice "RIN_1376"
    rin "\"Ugh... you sadist.\""

    "These exchanges were becoming routine for them."

    scene black with Dissolve(0.375)
    pause 1.125

    "........."

    "......"

    scene ev06h with bg_effect_05
    pause 0.5

    "Time passed slowly, the only sound in the room the brush sliding through Rin's hair."

    voice "FUM_1202"
    fumi "\"I'm done brushing it. Should I tie it back now?\""

    "There was no response."

    voice "FUM_1203"
    fumi "\"Rin?\""

    "Fumi peered at Rin's face from behind and realized that she'd fallen asleep."

    scene ev06d with Dissolve(0.5)

    voice "FUM_1204"
    fumi "\"So you did fall asleep.\""

    "Fumi watched Rin doze for a while."

    voice "FUM_1205"
    fumi "\"Eheh, you're a very interesting girl, Rin.\""

    "Fumi ran her fingers through Rin's glossy black hair."

    voice "FUM_1206"
    fumi "\"I want to see more sides of you.\""

    scene ev06j with Dissolve(0.5)

    voice "FUM_1207"
    fumi "\"Well, you might catch a cold if we stay like this. Let me just shift you a little~\""

    "Fumi gently moved Rin so as not to wake her."

    voice "FUM_1208"
    fumi "\"Here we go...\""

    play sound se116a

    scene black with Dissolve(0.5)
    pause 2.0

    scene bg02ba with bg_effect_05
    pause 0.5

    $ side_image = "rin 1 side pyjama k"

    show fumi 2 lg pyjama b with Dissolve(0.25)

    voice "RIN_1377"
    rin "\"Mm... nnh.\""

    "Rin stirred atop Fumi's lap."

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_1209"
    fumi "\"Are you awake?\""

    "Fumi looked down from her book at Rin's half-awake face."

    "She sat up and..."

    show rin behind fumi:
        "rin 1 lg pyjama e flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772
    show fumi:
        "fumi 2 lg pyjama i" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 252
    pause 0.5

    show rin 1 lg pyjama e:
        alpha 1.0 xcenter 772
    show fumi 2 lg pyjama i:
        xcenter 252
    with None

    voice "RIN_1378"
    rin "\"Huh? Where's the angel?\""

    "...was the first thing she said."

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_1210"
    fumi "\"What? Angel?\""

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1379"
    rin "\"...Oh, sorry. I was half-asleep.\""

    "Rin looked around, now fully awake."

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_1211"
    fumi "\"Were you dreaming?\""

    show rin 1 lg pyjama i with dict_dissolve_25

    voice "RIN_1380"
    rin "\"Yeah, I guess.\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_1212"
    fumi "\"About an angel?\""

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_1381"
    rin "\"Yeah. And I was a kid.\""

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_1213"
    fumi "\"Huh...\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_1214"
    fumi "\"Rin, why don't you tell me about it before you forget?\""

    show rin:
        ShakeYes

    "Rin nodded and started to explain."

    show rin:
        xoffset 0 yoffset 0
    with None

    window hide
    pause 0.5

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    show op_c01:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene black with Dissolve(0.5)
    pause 1.5

    window auto
    voice "RIN_0008"
    rin "{i}I heard a voice out of nowhere and jumped. When I looked up—there was an angel there.{/i}" (what_first_indent=24, show_name=False)

    voice "RIN_0009"
    rin "{i}I screamed and threw the book I was holding.{/i}" (what_first_indent=24, show_name=False)

    voice "RIN_0010"
    rin "{i}The book went right through the angel and hit the wall behind her.{/i}" (what_first_indent=24, show_name=False)

    window hide
    pause 0.5

    scene bg02ba
    show rin 1 lg pyjama b at pos_r
    show fumi 2 lg pyjama b at pos_l
    with Dissolve(1.5)
    pause 0.5

    show rin 1 lg pyjama a with dict_dissolve_25

    window auto
    voice "RIN_1382"
    rin "\"I threw all the books near me, but the angel didn't disappear, and all of a sudden, she was sitting next to me.\""

    voice "RIN_1383"
    rin "\"By then, I wasn't scared of her anymore, and we just quietly read a book together.\""

    voice "RIN_1384"
    rin "\"I feel like she kind of looked like someone I know, but that part's all foggy. I can't remember it.\""

    "Fumi listened to Rin's story, a gentle smile on her face."

    voice "RIN_1385"
    rin "\"Oh... and when I got tired, she let me sleep on her lap. Just like this...\""

    "Rin looked up at Fumi from her lap."

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_1215"
    fumi "\"It's rare for you to talk about angels.\""

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_1386"
    rin "\"Yeah... maybe you're rubbing off on me.\""

    show rin 2 lg pyjama e with dict_dissolve_25

    voice "RIN_1387"
    rin "\"I think I could believe now.\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_1216"
    fumi "\"Really?\""

    show rin 1 lg pyjama d with dict_dissolve_25

    voice "RIN_1388"
    rin "\"Because there was an angel when I woke up.\""

    play sound se118a

    show fumi 1 lg pyjama e with dict_dissolve_25
    show rin:
        xcenter 772
        easein 0.25 xcenter 512

    voice "FUM_1217"
    fumi "\"Aah!\""

    "Rin wrapped her arms around Fumi."

    show rin 1 lg pyjama f with dict_dissolve_25

    voice "RIN_1389"
    rin "\"Ah, and the angel's reading a dirty book~\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_1218"
    fumi "\"It's your book.\""

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_1390"
    rin "\"I know.\""

    show fumi 1 lg pyjama f with dict_dissolve_25

    voice "FUM_1219"
    fumi "\"I thought I'd do some studying for you.\""

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1391"
    rin "\"Ha... hahaha.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
