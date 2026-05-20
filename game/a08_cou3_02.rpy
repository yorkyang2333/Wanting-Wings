label a08_cou3_02:

    scene bg02dg with Dissolve(0.5)
    pause 1.5

    play music bgm02

    "They were still talking about their first day at the dorm after getting in bed."

    "Even Miyako, who normally fell asleep as soon as she got under the covers, was wide awake tonight."

    "She was eager to hear about the three girls from before she started watching them."

    show miyako 3 sm dark pyjama c
    show fumi 3 sm dark pyjama c
    show hina 3 sm dark pyjama_pjm c
    with dict_dissolve_25

    voice "2MI_0551"
    miyako "\"That's surprising.\""

    voice "2HI_0699"
    hina "\"It's true, though. It took way more time for Rin to open up to Asou.\""

    show miyako 3 sm dark pyjama e with dict_dissolve_25

    voice "2MI_0552"
    miyako "\"Even though now, they're...\""

    show hina 3 sm dark pyjama_pjm e with dict_dissolve_25

    voice "2HI_0700"
    hina "\"Yep~ All over each other, right?\""

    show fumi 3 sm dark pyjama f with dict_dissolve_25

    voice "2FU_0550"
    fumi "\"Ahaha...\""

    voice "2HI_0701"
    hina "\"Her parents are never around, so she wasn't used to people taking care of her, or so she said.\""

    scene white with bg_effect_21
    pause 1.5

    if persistent.dpatch:
        "—Last May. The morning, before school." id a08_cou3_02_f93fb466
    else:
        "—Last May. The morning, before class."

    pause 0.5

    scene bg02aa
    show bg_ef_01 zorder 2
    with bg_effect_21
    pause 1.0

    play music bgm01

    show hina 1 lg school f with Dissolve(0.25)
    show hina:
        ShakeYes

    voice "2HI_0702"
    hina "\"Hey, we gotta go or we're gonna miss the bus!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "She was small, but her voice really carried. And it sounded a little annoyed."

    $ side_image = "rin 1 side school k"

    voice "2RI_0716"
    rin "\"...You can leave first. I'll be right behind you.\""

    "And this one had a lazy voice."

    "She'd managed to get her uniform on, but was struggling to get away from her bed."

    show hina:
        ShakeJump

    voice "2HI_0703"
    hina "\"You said that before and you didn't show up until noon!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    $ side_image = "rin 1 side school b"

    voice "2RI_0717"
    rin "\"......\""

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_0704"
    hina "\"You can't get up in the morning because you're always up late reading.\""

    $ side_image = "rin 1 side school h"

    voice "2RI_0718"
    rin "\"So? I can do what I want, can't I?\""

    show hina 1 lg school f with dict_dissolve_25

    voice "2HI_0705"
    hina "\"You can't! As your roommate and your classmate, I won't let you be late!\""

    "Hina grabbed Rin's arm and tried to pull her upright."

    $ side_image = "rin 1 side school h"

    voice "2RI_0719"
    rin "\"...Don't pull that. You'll stretch it.\""

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_0706"
    hina "\"Then stand on your own feet!\""

    $ side_image = "rin 1 side school h"

    voice "2RI_0720"
    rin "\"...What, are you trying to score points as a good little class rep?\""

    show hina 1 lg school j with dict_dissolve_25

    voice "2HI_0707"
    hina "\"What? What points?\""

    hide hina with Dissolve(0.5)

    show hina z4 1 lg school j:
        xcenter 298
    show rin z4 2 lg school a:
        xcenter 726
    with Dissolve(0.5)

    "When Rin stood up, their height difference became very apparent."

    "They glared at each other, and Hina didn't back down at all despite having to look up at Rin."

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_0721"
    rin "\"...Hmph.\""

    "Rin was the first one to look away, shaking off Hina's grip on her sleeve."

    $ side_image = "fumi 1 side school c"

    voice "2FU_0551"
    fumi "\"Okay, let's get going♪\""

    "Fumi slipped right into the precarious air between them."

    hide hina with Dissolve(0.25)

    show fumi z4 2 lg school i:
        xcenter 298
    with Dissolve(0.25)

    show fumi:
        ShakeYes

    voice "2FU_0552"
    fumi "\"Here, your handkerchief. I washed it for you.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "She held Rin's handkerchief out to her."

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_0722"
    rin "\"Huh...?\""

    "Rin stared blankly between the handkerchief and Fumi's face."

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_0723"
    rin "\"Uhh, you don't need to... do that.\""

    show fumi:
        "fumi z4 2 lg school c" with Dissolve(0.25)
        2.2
        "fumi z4 2 lg school i" with Dissolve(0.25)
        1.2
        ShakeYes

    voice "2FU_0553"
    fumi "\"Well, I already have. Here, your commuter pass. Here, your lunch.\""

    show fumi z4 2 lg school i:
        xoffset 0 yoffset 0
    with None

    "Fumi held out some more items, smiling."

    voice "2RI_0724"
    rin "\"Huh? Lunch...?\""

    show fumi z4 1 lg school c with dict_dissolve_25

    voice "2FU_0554"
    fumi "\"Yes, I made enough for everyone♪\""

    $ side_image = "hina 1 side school p"

    voice "2HI_0708"
    hina "\"They looked so good! I'm really excited for them♪\""

    "Hina was fired up after watching Fumi fill the lunchboxes."

    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_0555"
    fumi "\"Would you like to eat lunch with us from now on?\""

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_0725"
    rin "\"Huh...? Why?\""

    show fumi z4 2 lg school a with dict_dissolve_25

    voice "2FU_0556"
    fumi "\"Well, you always leave the classroom alone at lunch.\""

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_0726"
    rin "\"I...\""

    $ side_image = "hina 1 side school a"

    voice "2HI_0709"
    hina "\"Just hang out with us one time, Ogata. If you hate it, we won't force you to do it again.\""

    voice "2RI_0727"
    rin "\"......\""

    "Hina and Fumi patently waited for Rin's answer. This was more important than catching the bus."

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_0728"
    rin "\"...Sure, if it's just today.\""

    show fumi z4 2 lg school i with dict_dissolve_25

    voice "2FU_0557"
    fumi "\"Oh, good! I hope you like the lunch.\""

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_0729"
    rin "\"...Umm, I don't like peppers.\""

    show fumi z4 1 lg school c with dict_dissolve_25

    voice "2FU_0558"
    fumi "\"It's not good to be picky.\""

    stop music fadeout 1.0

    scene white with bg_effect_21
    pause 1.5

    scene bg02dg with bg_effect_21
    pause 0.5

    play music bgm02

    show miyako 3 sm dark pyjama g
    show fumi 3 sm dark pyjama f
    show hina 3 sm dark pyjama_pjm e
    with dict_dissolve_25

    voice "2MI_0553"
    miyako "\"Wow, I can't even imagine that!\""

    voice "2HI_0710"
    hina "\"She's still just as twisted, though.\""

    show miyako 3 sm dark pyjama d with dict_dissolve_25

    voice "2MI_0554"
    miyako "\"Ahaha.\""

    show hina 3 sm dark pyjama_pjm d with dict_dissolve_25

    voice "2HI_0711"
    hina "\"We're only so close now because Asou never stopped bugging her until Rin opened up.\""

    show miyako 3 sm dark pyjama c with dict_dissolve_25

    voice "2MI_0555"
    miyako "\"I see~\""

    show fumi 3 sm dark pyjama d with dict_dissolve_25

    voice "2FU_0559"
    fumi "\"You... think so?\""

    show hina 3 sm dark pyjama_pjm j with dict_dissolve_25

    voice "2HI_0712"
    hina "\"Now she just babies her too much, though. Like this morning—\""

    stop music fadeout 1.0

    scene white with bg_effect_21
    pause 1.5

    if persistent.dpatch:
        "—That morning, before school." id a08_cou3_02_93409271
    else:
        "—That morning, before class."

    pause 0.5

    scene bg02ag
    show bg_ef_01 zorder 2
    with bg_effect_21
    pause 1.0

    play music bgm01

    show fumi 2 lg school f with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_0560"
    fumi "\"Come on, Rin, please get up? Pick up your bag!\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "On the new version of the Rin Shift, they couldn't move on to the next item on the list unless Rin took her bag first."

    $ side_image = "rin 2 side school c"

    voice "2RI_0730"
    rin "\"No! I'm not getting up without a kiss!\""

    show fumi 2 lg school d with dict_dissolve_25

    voice "2FU_0561"
    fumi "\"Huh? Huh?\""

    $ side_image = "hina 1 side school j"

    voice "2HI_0713"
    hina "\"Yuck, what a baby...\""

    show fumi:
        "fumi 2 lg school h" with Dissolve(0.25)
        ShakeNo_4_500
        4.0
        "fumi 2 lg school f" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0562"
    fumi "\"Umm... uhh, I'll give you a kiss when we come home. Please just get up now.\""

    show fumi 2 lg school f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 2 side school c"

    voice "2RI_0731"
    rin "\"But I want one now.\""

    "The baby would not negotiate."

    $ side_image = "hina 1 side school h"

    voice "2HI_0714"
    hina "\"This is bad... You should say something to her too, Miyako.\""

    $ side_image = "miyako 2 side school i"

    voice "2MI_0556"
    miyako "\"Zzz...\""

    $ side_image = "hina 1 side school d"

    voice "2HI_0715"
    hina "\"Are you sleeping standing up?!\""

    scene white with bg_effect_21
    pause 1.5

    scene bg02dg with bg_effect_21
    pause 0.5

    play music bgm02

    show miyako 3 sm dark pyjama f
    show fumi 3 sm dark pyjama c
    show hina 3 sm dark pyjama_pjm j
    with dict_dissolve_25

    voice "2MI_0557"
    miyako "\"Ahahahaha.\""

    "—You laugh, but you're pretty bad, too."

    show hina 3 sm dark pyjama_pjm h with dict_dissolve_25

    voice "2HI_0716"
    hina "\"I really can't believe her...\""

    voice "2RI_0732RE"
    rin "\"You should leave it at that. Poor Rin is a delicate flower, you know.\"" (show_name="Fumi?")

    show hina:
        "hina 3 sm dark pyjama_pjm d" with Dissolve(0.25)
        1.2
        "hina 3 sm dark pyjama_pjm f" with Dissolve(0.25)

    voice "2HI_0717"
    hina "\"Asou...? No, that voice is clearly coming from under Asou's covers...\""

    show hina 3 sm dark pyjama_pjm f:
        pass
    with None
    show fumi 3 sm dark pyjama f with dict_dissolve_25

    voice "2FU_0563"
    fumi "\"Ahahahaha...\""

    show hina 3 sm dark pyjama_pjm j with dict_dissolve_25

    voice "2HI_0718"
    hina "\"I thought it was too quiet up there...\""

    "There was a conspicuous lump under Fumi's covers. She must have been hiding there for the whole conversation."

    show hina 3 sm dark pyjama_pjm h with dict_dissolve_25

    voice "2HI_0719"
    hina "\"Rin! Get out of Asou's bed and get into your own!\""

    voice "2RI_0733RE"
    rin "\"Rin is a—\""

    show hina 3 sm dark pyjama_pjm j with dict_dissolve_25

    voice "2HI_0720"
    hina "\"Enough about how delicate you are!\""

    voice "2RI_0734"
    rin "\"Uuugh...\""

    show rin 3 sm dark pyjama_bed_b b:
        xcenter 526 ycenter 476
    with dict_dissolve_25

    "Rin slunk out of the bed."

    show fumi 3 sm dark pyjama c with dict_dissolve_25

    voice "2FU_0564"
    fumi "\"Get into your bed while you're still warm, okay?\""

    "Fumi patted her on the back."

    show rin 3 sm dark pyjama_bed_b d with dict_dissolve_25

    voice "2RI_0735"
    rin "\"...I won't go unless you kiss me.\""

    show fumi 3 sm dark pyjama d with dict_dissolve_25

    voice "2FU_0565"
    fumi "\"Hahh, well, if I must...\""

    play sound se_2s_g002

    hide hina with dict_dissolve_25
    show rin:
        "rin 3 sm dark pyjama_bed_b f" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_0736"
    rin "\"Gyuh!\""

    show rin 3 sm dark pyjama_bed_b f:
        xcenter 526 ycenter 476 xoffset 0 yoffset 0
    with None

    "Hina threw a pillow at the back of the big baby's head."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0721"
    hina "\"Get up there!!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
