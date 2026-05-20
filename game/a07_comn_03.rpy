label a07_comn_03:

    scene black with Dissolve(0.5)
    pause 1.5

    "—Back to the present, lunch time."

    play music bgm01

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    show bg_obi behind fumi, miyako, hina, rin

    show fumi z4 1 lg school h:
        xcenter 118
    show miyako z4 1 lg school_a a behind fumi, hina:
        xcenter 383
    show hina z4 1 lg school n:
        xcenter 641
    show rin z4 2 lg school a:
        xcenter 906
    with Dissolve(0.25)

    if routes_cleared == 0:
        jump a07_comn_03_a
    else:
        jump a07_comn_03_b


label a07_comn_03_a:

    voice "2HI_0062"
    hina "\"Haah... I can't believe we were late on the first day...\""

    show miyako:
        "miyako z4 1 lg school_a l" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0015"
    miyako "\"...I'm really sorry.\""

    show miyako z4 1 lg school_a l:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z4 1 lg school l" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0063"
    hina "\"No, No, I'm not blaming you, Miyako.\""

    show hina z4 1 lg school l:
        xoffset 0 yoffset 0
    with None

    voice "2FU_0043"
    fumi "\"We were too absorbed in our usual routine...\""

    "The three of them all bowed their heads apologetically."

    voice "2RI_0059"
    rin "\"Yeah, that sure was an ambush.\""

    "And this one was pouring tea into a thermos. Acting like she had—"

    show hina z4 1 lg school f with dict_dissolve_25

    voice "2HI_0064"
    hina "\"Like you had nothing to do with it! You waited until the very last minute!\""

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_0060B"
    rin "\"I've got a very accurate internal clock.\""

    show hina:
        "hina z4 1 lg school g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0065"
    hina "\"Well, set it earlier! We're all on a Rin shift! Our mornings are so tailored to your schedule that we can't respond to unexpected situations like we had today!\""

    show hina z4 1 lg school g:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_0061"
    rin "\"Don't blame the shortcomings of the system on its user.\""

    show hina:
        ShakeJump
        ShakeJump

    voice "2HI_0066"
    hina "\"Shut up! It's all your fault, Rin!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_0044"
    fumi "\"Ahaha...\""

    jump a07_comn_03_c

label a07_comn_03_b:

    voice "2HI_0067"
    hina "\"Haah... That was really close, and on the first day, too...\""

    voice "2RI_0062"
    rin "\"We just barely made it.\""

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_0068"
    hina "\"We didn't, actually, it's just that the principal let us off the hook.\""

    show miyako z4 1 lg school_a l with dict_dissolve_25

    voice "2MI_0016"
    miyako "\"...I'll be more careful tomorrow.\""

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_0063"
    rin "\"All you gotta do is get used to it.\""

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0069"
    hina "\"You should talk!\""

    show hina z4 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_0045"
    fumi "\"It's rare to see the principal around in the morning like that.\""

    show hina z4 1 lg school k with dict_dissolve_25

    voice "2HI_0070"
    hina "\"True. And she said hi to you, Miyako. Do you know her?\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0017"
    miyako "\"No, it was my first time meeting her.\""

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0071"
    hina "\"She nodded when you said you were a transfer student, though.\""

    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_0046"
    fumi "\"Maybe she saw your face on your transfer forms.\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0018"
    miyako "\"Oh, that's right. I forgot to get the forms from Sachiko.\""

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_0072"
    hina "\"Huh? Then how'd she know you?\""

    show rin z4 1 lg school k with dict_dissolve_25

    voice "2RI_0064"
    rin "\"Well, she is an old lady...\""

    show fumi z4 2 lg school f with dict_dissolve_25

    voice "2FU_0047"
    fumi "\"Hey.\""

    jump a07_comn_03_c

label a07_comn_03_c:

    stop music fadeout 1.0

    pause 0.5

    scene white with bg_effect_05

    pause 0.75

    scene bg04aa
    show bg_obi behind fumi, miyako, hina, rin

    show fumi z4 2 lg school c:
        xcenter 118
    show miyako z4 1 lg school_a b behind fumi, hina:
        xcenter 383
    show hina z4 1 lg school a:
        xcenter 641
    show rin z4 1 lg school a:
        xcenter 906
    with bg_effect_05

    pause 0.5

    play music bgm01 fadein 1.0

    show fumi:
        ShakeYes

    voice "2FU_0048"
    fumi "Alright, let's eat.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0065"
    rin "\"Everybody got your lunch?\""

    voice "2HI_0073"
    hina "\"Yep.\""

    voice "2MI_0019"
    miyako "\"Yes.\""

    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_0049"
    fumi "\"I believe I do...\""

    hide fumi
    hide rin
    hide hina
    hide miyako
    with dict_dissolve_50

    play sound se_2s_g004

    "They all took their lunches out of their bags and opened them up."

    "Fumi had spared no effort, as always."

    show miyako z4 1 lg school_a f with dict_dissolve_25

    voice "2MI_0020"
    miyako "\"Wow! It's beautiful! There are so many colors...\""

    "Miyako exclaimed with glee as soon as she opened the lid."

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0021"
    miyako "\"It's like a little box of jewels... I'll get to eat this every day now... I can't believe it.\""

    "Miyako stared, spellbound, at the assortment of hues in her lunchbox."

    $ side_image = "fumi 1 side school i"

    voice "2FU_0050"
    fumi "\"I'm a little humbled by how impressed you are.\""

    "This wasn't the first time Miyako had gotten so emotional. In fact, it had been like this at just about every meal for the week since she'd arrived."

    hide miyako
    with Dissolve(0.5)

    show fumi z4 1 lg school a:
        xcenter 118
    show miyako z4 2 lg school f behind fumi, hina:
        xcenter 383
    show hina z4 1 lg school a:
        xcenter 641
    show rin z4 1 lg school a:
        xcenter 906
    with dict_dissolve_50

    voice "2MI_0022"
    miyako "\"I-I'm sorry for getting so excited.\""

    show rin z4 2 lg school g with dict_dissolve_25

    voice "2RI_0066"
    rin "\"It's always like it's your first meal ever.\""

    show fumi z4 1 lg school c with dict_dissolve_25

    voice "2FU_0051"
    fumi "\"Ahaha, it's nice to be appreciated.\""

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0074"
    hina "\"You always start with the color.\""

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_0023"
    miyako "\"Yes. The taste and smell and texture are all wonderful too, but the color always catches my eye first.\""

    show miyako z4 1 lg school_b b with dict_dissolve_25

    voice "2MI_0024"
    miyako "\"This tomato is such a beautiful...\""

    "She seemed to get stuck there."

    show rin z4 2 lg school a with dict_dissolve_25

    voice "2RI_0067"
    rin "\"Hm? Red?\""

    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_0025"
    miyako "\"Umm, yes, red... This is red, then.\""

    "She looked at the tomato and repeated the word as if to create an association in her mind."

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_0068"
    rin "\"You speak like you're fluent, but you trip up at pretty weird places.\""

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_0026"
    miyako "\"I'm still learning.\""

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0075"
    hina "\"It's almost like you're from a land without color or something.\""

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_0027"
    miyako "\"...Aha.\""

    "An astute observation."

    "It wasn't that Miyako didn't know the word \"red,\" it was that {i}she didn't know which color red was{/i}."

    show rin z4 1 lg school c with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2RI_0069"
    rin "\"Here, Takaoka. The peppers are a beautiful green, too.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin said, attempting to foist her hated peppers onto Miyako."

    show fumi z4 2 lg school f with Dissolve(0.25)
    show fumi:
        ShakeJump

    voice "2FU_0052B"
    fumi "\"Hey!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
