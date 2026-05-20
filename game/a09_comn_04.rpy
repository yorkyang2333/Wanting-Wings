label a09_comn_04:

    if route2 == 1:
        scene bg01cg with Dissolve(0.5)
    else:
        scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0615"
    fumi "\"......\""

    "Fumi was knitting."

    "Her hands moved with a practiced quickness. She really can do anything, can't she?"

    $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_0589"
    miyako "\"......\""

    "Miyako watched her, engrossed."

    show fumi z4 2 lg pyjama b:
        xcenter 298
    show miyako z4 1 lg pyjama_a e:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0590"
    miyako "\"What will it be?\""

    show fumi z4 1 lg pyjama c with dict_dissolve_25

    voice "2FU_0616"
    fumi "\"It's a scarf.\""

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0591"
    miyako "\"Ooh.\""

    show fumi z4 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0617"
    fumi "\"My brother shrunk his in the wash, so I'm knitting him a new one.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0592"
    miyako "\"That's nice of you.\""

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0618"
    fumi "\"Eheh, I'm just knitting as a hobby and foisting the finished product off on him.\""

    "Fumi's hands kept moving as they talked. Her fingers must just remember how to move."

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0593"
    miyako "\"Is it hard to do?\""

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0619"
    fumi "\"You just knit in a straight line for a scarf, so it's not that—\""

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    "Fumi suddenly stopped, coming to a realization."

    show fumi z4 1 lg pyjama c with Dissolve(0.25)
    show fumi:
        ShakeJump

    voice "2FU_0620"
    fumi "\"Miyako! If you're interested, do you want to try it? I'll teach you how♪\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show miyako z4 2 lg pyjama b with dict_dissolve_25

    voice "2MI_0594"
    miyako "\"Do you think I can do it?\""

    show fumi:
        "fumi z4 1 lg pyjama a" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0621"
    fumi "\"The way I'm doing it is a little advanced, but—\""

    show fumi z4 1 lg pyjama a:
        xoffset 0 yoffset 0
    with None

    "Fumi set down the scarf she was working on..."

    show fumi z4 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0622"
    fumi "\"If you want to just make something simple, you only need to learn the basics and then be patient until you're done.\""

    "...and took some balls of yarn and needles out of her bag, setting them down in front of Miyako."

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0595"
    miyako "\"Wow, you have a lot of different colors.\""

    "Miyako's eyes lit up when she saw the yarn balls."

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0623"
    fumi "\"Heh, I wonder what color would look good on Sachiko.\""

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0596"
    miyako "\"...!\""

    "Miyako raised her head and gave Fumi a curious look."

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0624"
    fumi "\"Was I wrong?\""

    show miyako z4 2 lg pyjama f with dict_dissolve_25

    voice "2MI_0597"
    miyako "\"Umm... no, you're not.\""

    "Fumi's very perceptive when it comes to love."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0598"
    miyako "\"What color do you think I should use?\""

    "Miyako cocked her head, picking up different balls of yarn."

    "Color coordinating is a bit of a challenge when you're new to the world of color."

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0625"
    fumi "\"Maybe you can take your time picking the color out and just learn the basics now.\""

    "Fumi picked up a ball of yarn that was already partially used."

    show fumi z4 1 lg pyjama c with dict_dissolve_25

    voice "2FU_0626"
    fumi "\"Let's use this super thick yarn. It's warm and really fluffy and cute when you finish with it.\""

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0599"
    miyako "\"Sounds good.\""

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0627"
    fumi "\"There's crocheting and there's knitting. I recommend knitting.\""

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0628"
    fumi "\"It might seem complicated because you use two needles, but it's easy to count the stitches, so it's good for beginners.\""

    show miyako:
        "miyako z4 1 lg pyjama_a c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0600"
    miyako "\"Okay. I'll go with the instructor's recommendation.\""

    show miyako z4 1 lg pyjama_a c:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0629"
    fumi "\"I'll show you how to do it. Watch carefully.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0601"
    miyako "\"Right!\""

    "Miyako scooted closer."

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0630"
    fumi "\"First you have to cast on...\""

    hide fumi
    hide miyako
    with dict_dissolve_50

    "On the other side of the table, the two less feminine girls were lazing about in their less feminine way."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0782"
    rin "\"Hey, Miss Hina~ Have you knitted before~?\""

    $ side_image = "hina 1 side pyjama_pjm m"

    voice "2HI_0768"
    hina "\"I've sewn cleaning cloths~\""

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_0783"
    rin "\"That's not knitting~\""

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_0769"
    hina "\"What about you then, Miss Rin~?\""

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0784"
    rin "\"I've done a little cat's cradle~\""

    $ side_image = "hina 1 side pyjama_pjm n"

    voice "2HI_0770"
    hina "\"That's super not knitting~\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    if route2 == 1:
        scene bg01cg with bg_effect_05
    else:
        scene bg01ch with bg_effect_05
    pause 0.5

    "........."

    show fumi 2 lg pyjama b at pos_l
    show miyako 2 lg pyjama a at pos_r
    with dict_dissolve_25

    voice "2MI_0602"
    miyako "\"Oh, it came off.\""

    "The yarn she was trying to loop came off of the needle. She was copying Fumi, but having trouble."

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0631"
    fumi "\"Start over from hooking it.\""

    show miyako 1 lg pyjama_a i with dict_dissolve_25

    "Miyako nodded and began the process again."

    "She went slowly, and carefully..."

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0603"
    miyako "\"—!\""

    "She looked up at Fumi. She'd taken her time and finished her first stitch."

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0632"
    fumi "\"Good job!\""

    "Fumi gave her a passing grade."

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0604"
    miyako "\"Ahaha. This is a little daunting.\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "2FU_0633"
    fumi "\"You'll be okay. Once you get used to it, you'll get quicker. You've just got to be patient.\""

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0605"
    miyako "\"Patient... I should be good at it then, I think.\""

    "Well, she {i}has{/i} seen eternity."

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0634"
    fumi "\"That's the spirit. And then you just need to put some love into it.\""

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0606"
    miyako "\"Aha... that's a little embarrassing.\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0635"
    fumi "\"Let's take our time and have fun.\""

    show miyako:
        "miyako 1 lg pyjama_a d" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0607"
    miyako "\"Yes!\""

    show miyako 1 lg pyjama_a d with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a09_cou1_01
    elif route2 == 2:
        jump a09_cou2_01
    elif route2 == 3:
        jump a09_cou3_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
