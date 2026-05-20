label a09_cou3_04:

    scene bg01bh with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "The three girls, minus Fumi, were lounging around before dinner."

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1161"
    rin "\"Uunnaaah~\""

    "A groan came from the padded kimono on the floor."

    show miyako z4 1 lg pyjama_a j:
        xcenter 298
        ShakeJump
    with dict_dissolve_25

    voice "2MI_0918"
    miyako "\"Ah, a seal?\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Miyako was nodding off, but she raised her head at this."

    show hina z4 1 lg pyjama_pjm e:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_1121"
    hina "\"No, it's just Rin.\""

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1162"
    rin "\"Uunnaaah~\""

    "Rin writhed on the floor, groaning again."

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0919"
    miyako "\"...Rin?\""

    show hina z4 1 lg pyjama_pjm m with dict_dissolve_25

    voice "2HI_1122"
    hina "\"Just leave her be. She'll go back to normal when Asou comes back.\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1163"
    rin "\"...Serious shortage of Fumi power... Death.\""

    show hina:
        "hina z4 1 lg pyjama_pjm j" with Dissolve(0.25)
        5.5
        "hina z4 1 lg pyjama_pjm d" with Dissolve(0.25)
        ShakeSide

    voice "2HI_1123"
    hina "\"Don't be dramatic. You're like this every week lately. Just wait a little and—waaah!\""

    show hina z4 1 lg pyjama_pjm d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1164"
    rin "\"Naaah~\""

    "When she looked over at the clock, Rin reached out and wrapped her arms around Hina like an octopus."

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2HI_1124"
    hina "\"Hey, what are you doing?\""

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1165"
    rin "\"...Not enough volume.\""

    "Rin complained and swiftly let go."

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1125"
    hina "\"Grr.\""

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1166"
    rin "\"Uunnaaah~\""

    "And again."

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0920"
    miyako "\"Would a hug from me help?\""

    "Miyako extended her arms."

    show hina:
        "hina z4 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1126"
    hina "\"You don't need to do that!\""

    show hina z4 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1167"
    rin "\"Aaaah~!\""

    show hina:
        ShakeJump

    voice "2HI_1127"
    hina "\"Shut up!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    play sound se521
    pause 1.5

    hide miyako with Dissolve(0.25)

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25
    show rin:
        "rin z4 1 lg pyjama glasses e flat"
        alpha 0.0 xcenter 298 ycenter 859
        easein 0.25 alpha 1.0 ycenter 759

    voice "2RI_1168"
    rin "\"Fumi?!\""

    show rin z4 1 lg pyjama glasses e:
        alpha 1.0 xcenter 298 ycenter 759
    with None

    "Rin leapt up from the floor, but..."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0753"
    sachiko "\"Hey, guys~ If you're doing free hugs, let me in on it.\""

    "Sachiko peeked in from the doorway."

    show rin z4 2 lg pyjama glasses c with Dissolve(0.25)
    show rin:
        "rin z4 2 lg pyjama glasses c flat"
        alpha 1.0 ycenter 759
        easeout 0.75 alpha 0.0 ycenter 859

    voice "2RI_1169"
    rin "\"Uunnaaah~!\""

    hide rin with None

    "Rin didn't hide her disappointment. She plopped down to the floor and groaned again."

    $ side_image = "sachiko 1 side outfit e"

    voice "2SA_0754"
    sachiko "\"Hey, Hinacchi, c'mere~\""

    show hina:
        "hina z4 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1128"
    hina "\"No! We're not hugging! Go away!\""

    show hina z4 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    show miyako z4 2 lg pyjama c:
        xcenter 298
    with dict_dissolve_25

    voice "2MI_0921"
    miyako "\"I'll hug you.\""

    "Miyako extended her arms."

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1129"
    hina "\"You don't need to! Leave! Leave! Leave!\""

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0755"
    sachiko "\"No, I'm here for a reason, really.\""

    "Sachiko held out a sheaf of papers."

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0922"
    miyako "\"What's that?\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0756"
    sachiko "\"Local magazine.\""

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_1130"
    hina "\"Like, with coupons and stuff?\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0757"
    sachiko "\"Yeah. That's not what I wanted to show you, though. It might interest the one lazing around over there, too.\""

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1170"
    rin "\"It won't. Unless Fumi's in it.\""

    "Rin rolled over so her back was to them."

    stop music fadeout 1.0

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0923"
    miyako "\"That's Fumi on the cover.\""

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_1131"
    hina "\"Oh, you're right.\""

    show rin 1 120 pyjama_a glasses j as rin_1:
        "rin 1 120 pyjama_a glasses j flat"
        alpha 0.0 xcenter 512 ycenter 1784
        easein 0.25 alpha 1.0 xcenter 512 ycenter 1684

    pause 0.25

    show rin 1 120 pyjama_a glasses j as rin_1:
        alpha 1.0 xcenter 512 ycenter 1684 xoffset 0 yoffset 0
        function LayerShake(50,50,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1171"
    rin "\"What! Was! That?!\""

    show rin 1 120 pyjama_a glasses j as rin_1:
        xoffset 0 yoffset 0
    with None

    "Rin jumped up like she was spring-loaded."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01bh with bg_effect_05
    pause 0.5

    play music bgm06 fadein 1.0

    "The three of them pored over the magazine."

    "Not only was Fumi on the cover to represent the patisserie, there were several pictures of her inside as well, like she was the heroine of the Valentine's special issue."

    show rin 1 lg pyjama glasses j with Dissolve(0.25)
    show rin:
        ShakeJump

    voice "2RI_1172"
    rin "\"Huh? Wait a second! This is too much!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "As Hina and Miyako read the magazine, Rin got up and started pacing, for once seeming to be unable to look any more."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0758"
    sachiko "\"Interested you, right?\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_1173"
    rin "\"Sachiko, where'd you get this? I need one for reading, one to keep in mint condition, and one to show people, so at least three!\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0759"
    sachiko "\"The station. There's tons more.\""

    show rin 2 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_1174"
    rin "\"Maybe I should get all of them? No, wait, that'd limit Fumi's cuteness from getting out to as many people as possible!\""

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0760"
    sachiko "\"That's not the problem. You shouldn't do that anyway. These are free, but they're still a commodity.\""

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_1132"
    hina "\"Look, look. Asou's store's gonna be on TV, too.\""

    show rin 1 lg pyjama glasses j with Dissolve(0.25)
    show rin:
        ShakeSide

    voice "2RI_1175"
    rin "\"When?!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_1133"
    hina "\"Umm... The recording will be next Sunday, and then it'll air that night. Wow, right after.\""

    $ side_image = "miyako 1 side pyjama_b e"

    voice "2MI_0924"
    miyako "\"Is Fumi going to be on TV?\""

    $ side_image = "hina 2 side pyjama_pjm a"

    voice "2HI_1134"
    hina "\"Well, she is the face of the store~\""

    show rin:
        ShakeYes

    voice "2RI_1176"
    rin "\"Let's get a big screen TV! 100 inches! 4K? 8K?\""

    show rin:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_1135"
    hina "\"Where do we have the money for that? And even if we bought it, there's nowhere to put it!\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_1177"
    rin "\"We'll get rid of your desk.\""

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_1136"
    hina "\"Hey! And there's no 4K broadcast of local news.\""

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1178"
    rin "\"Aaah!\""

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "She's so excited she's starting to go funny."

    hide rin with dict_dissolve_50

    play sound se521
    pause 2.0

    $ side_image = "fumi 1 side casual b"

    voice "2FU_0886"
    fumi "\"I'm back... Huh?\""

    "The four all looked at her when they heard her voice."

    $ side_image = "fumi 2 side casual g"

    voice "2FU_0887"
    fumi "\"Wait, what's everyone doing together like—\""

    "Fumi understood everything when she saw the magazine in Rin's hand."

    $ side_image = "fumi 1 side casual k"

    voice "2FU_0888"
    fumi "\"...Haahh.\""

    "She looked up and sighed."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01bh with bg_effect_05
    pause 0.5

    show fumi 1 lg casual h at pos_l
    show sachiko 1 lg outfit a at pos_r
    with Dissolve(0.25)

    voice "2FU_0889"
    fumi "\"Where did you get that?\""

    "Fumi asked, flipping over the magazine on the table."

    voice "2SA_0761"
    sachiko "\"I found it at the station and brought it back. Should I not have?\""

    show fumi 2 lg casual h with dict_dissolve_25

    voice "2FU_0890"
    fumi "\"No, you're supposed to take them, so it's fine. I just didn't know it was out yet.\""

    show rin 1 120 pyjama_a glasses j as rin_1:
        xcenter 512 ycenter 1684
        function LayerShake(50,50,0.3)
    with dict_dissolve_25
    $ persistent.layer_shaken = False

    voice "2RI_1179"
    rin "\"Fumi! Why'd you keep such a big thing a secret?!\""

    show fumi 1 lg casual j
    show sachiko 1 lg outfit h
    with dict_dissolve_25

    "Fumi was surprised when Rin leapt at her."

    hide sachiko
    hide rin_1
    show rin 1 lg pyjama glasses j at pos_r
    with dict_dissolve_25

    voice "2FU_0891"
    fumi "\"Wah! It's not a big thing. It's just a local advertisement for the store.\""

    show rin:
        ShakeJump
        ShakeJump

    voice "2RI_1180"
    rin "\"But you're on the cover! The cover! My Fumi's on the cover of a book!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin held the magazine up high in the air."

    show fumi:
        "fumi 1 lg casual h" with Dissolve(0.25)
        6.0
        "fumi 1 lg casual g" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0892"
    fumi "\"It was only being distributed locally, and there weren't a ton of them printed, so I didn't think you'd find them... Give it here, Rin!\""

    show fumi 1 lg casual g:
        xoffset 0 yoffset 0
    with None

    "In an aerial battle, Rin's got the upper hand."

    $ side_image = "miyako 1 side pyjama_b g"

    voice "2MI_0925"
    miyako "\"When was this taken?\""

    show fumi 2 lg casual h with dict_dissolve_25

    voice "2FU_0893"
    fumi "\"About a month ago. They came to do an interview right when I happened to be at the store, and they were planning on getting a picture of my dad at first.\""

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0762"
    sachiko "\"But if there's a cute girl tending the store, they decided to go for that instead, of course.\""

    show rin:
        "rin 1 lg pyjama glasses h" with Dissolve(0.1)
        ShakeYes2

    "Rin nodded rapidly."

    show rin 1 lg pyjama glasses h:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg casual k with dict_dissolve_25

    voice "2FU_0894"
    fumi "\"I tried really hard to say no. I don't like the attention. But the photographer ended up wearing me down...\""

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_1137"
    hina "\"You've got a really nice smile in the picture, though.\""

    "She was right. Fumi had a brilliant, natural smile in the picture on the cover."

    show fumi 1 lg casual d with dict_dissolve_25

    voice "2FU_0895"
    fumi "\"Yeah, but it took a bunch of tries to get it. I couldn't smile right.\""

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1138"
    hina "\"Is this just the miracle shot, then?\""

    show fumi 1 lg casual a with dict_dissolve_25

    voice "2FU_0896"
    fumi "\"You could call it that... A regular just happened to come by, and that picture happened when I greeted them.\""

    $ side_image = "hina 1 side pyjama_pjm p"

    voice "2HI_1139"
    hina "\"Ahaha. I get it. That's why it looks so natural.\""

    $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_0926"
    miyako "\"Oh, are you gonna be on TV next week?\""

    show fumi 2 lg casual g with dict_dissolve_25

    voice "2FU_0897"
    fumi "\"TV?\""

    "Fumi repeated, face blank."

    show rin 2 lg pyjama glasses f with Dissolve(0.25)
    show rin:
        ShakeYes2

    voice "2RI_1181"
    rin "\"Right here.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin opened up to the page with the article and pointed out the bit about the TV interview."

    show fumi 1 lg casual j with Dissolve(0.25)
    show fumi:
        ShakeSide

    voice "2FU_0898"
    fumi "\"What? What? I haven't heard anything about this.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1182"
    rin "\"I'm gonna go watch for sure, Fumi!\""

    show fumi 1 lg casual k with dict_dissolve_25

    voice "2FU_0899"
    fumi "\"...U-Uhh?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou3_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
