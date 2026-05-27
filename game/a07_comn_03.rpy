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
    hina "\"Haah... I can't believe we were late on the first day...\"" id a07_comn_03_a_ebe4dd98

    show miyako:
        "miyako z4 1 lg school_a l" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0015"
    miyako "\"...I'm really sorry.\"" id a07_comn_03_a_1c6ca30e

    show miyako z4 1 lg school_a l:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z4 1 lg school l" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0063"
    hina "\"No, No, I'm not blaming you, Miyako.\"" id a07_comn_03_a_447aa951

    show hina z4 1 lg school l:
        xoffset 0 yoffset 0
    with None

    voice "2FU_0043"
    fumi "\"We were too absorbed in our usual routine...\"" id a07_comn_03_a_bdcb964b

    "The three of them all bowed their heads apologetically."

    voice "2RI_0059"
    rin "\"Yeah, that sure was an ambush.\"" id a07_comn_03_a_e6d6ee2b

    "And this one was pouring tea into a thermos. Acting like she had—"

    show hina z4 1 lg school f with dict_dissolve_25

    voice "2HI_0064"
    hina "\"Like you had nothing to do with it! You waited until the very last minute!\"" id a07_comn_03_a_3306c8e6

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_0060B"
    rin "\"I've got a very accurate internal clock.\"" id a07_comn_03_a_2c9e4c6a

    show hina:
        "hina z4 1 lg school g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0065"
    hina "\"Well, set it earlier! We're all on a Rin shift! Our mornings are so tailored to your schedule that we can't respond to unexpected situations like we had today!\"" id a07_comn_03_a_525b63b4

    show hina z4 1 lg school g:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_0061"
    rin "\"Don't blame the shortcomings of the system on its user.\"" id a07_comn_03_a_77f421f4

    show hina:
        ShakeJump
        ShakeJump

    voice "2HI_0066"
    hina "\"Shut up! It's all your fault, Rin!\"" id a07_comn_03_a_7b06d644

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_0044"
    fumi "\"Ahaha...\"" id a07_comn_03_a_73f02263

    jump a07_comn_03_c

label a07_comn_03_b:

    voice "2HI_0067"
    hina "\"Haah... That was really close, and on the first day, too...\"" id a07_comn_03_b_3e901ef1

    voice "2RI_0062"
    rin "\"We just barely made it.\"" id a07_comn_03_b_d6f9ec8a

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_0068"
    hina "\"We didn't, actually, it's just that the principal let us off the hook.\"" id a07_comn_03_b_7c784bec

    show miyako z4 1 lg school_a l with dict_dissolve_25

    voice "2MI_0016"
    miyako "\"...I'll be more careful tomorrow.\"" id a07_comn_03_b_acf6c5b4

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_0063"
    rin "\"All you gotta do is get used to it.\"" id a07_comn_03_b_72d15db8

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0069"
    hina "\"You should talk!\"" id a07_comn_03_b_81c51333

    show hina z4 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_0045"
    fumi "\"It's rare to see the principal around in the morning like that.\"" id a07_comn_03_b_7ed5d99c

    show hina z4 1 lg school k with dict_dissolve_25

    voice "2HI_0070"
    hina "\"True. And she said hi to you, Miyako. Do you know her?\"" id a07_comn_03_b_33a19a82

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0017"
    miyako "\"No, it was my first time meeting her.\"" id a07_comn_03_b_70217a3b

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0071"
    hina "\"She nodded when you said you were a transfer student, though.\"" id a07_comn_03_b_7e080925

    show fumi z4 2 lg school b with dict_dissolve_25

    voice "2FU_0046"
    fumi "\"Maybe she saw your face on your transfer forms.\"" id a07_comn_03_b_25e1b205

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0018"
    miyako "\"Oh, that's right. I forgot to get the forms from Sachiko.\"" id a07_comn_03_b_2716f21f

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_0072"
    hina "\"Huh? Then how'd she know you?\"" id a07_comn_03_b_ed3595d4

    show rin z4 1 lg school k with dict_dissolve_25

    voice "2RI_0064"
    rin "\"Well, she is an old lady...\"" id a07_comn_03_b_964e1c2e

    show fumi z4 2 lg school f with dict_dissolve_25

    voice "2FU_0047"
    fumi "\"Hey.\"" id a07_comn_03_b_cb75a293

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
    fumi "Alright, let's eat.\"" id a07_comn_03_c_182398fe

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0065"
    rin "\"Everybody got your lunch?\"" id a07_comn_03_c_e71a1478

    voice "2HI_0073"
    hina "\"Yep.\"" id a07_comn_03_c_5ecdb2a7

    voice "2MI_0019"
    miyako "\"Yes.\"" id a07_comn_03_c_61a87ab0

    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_0049"
    fumi "\"I believe I do...\"" id a07_comn_03_c_47c7f254

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
    miyako "\"Wow! It's beautiful! There are so many colors...\"" id a07_comn_03_c_994ffa3d

    "Miyako exclaimed with glee as soon as she opened the lid."

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0021"
    miyako "\"It's like a little box of jewels... I'll get to eat this every day now... I can't believe it.\"" id a07_comn_03_c_60e06c92

    "Miyako stared, spellbound, at the assortment of hues in her lunchbox."

    $ side_image = "fumi 1 side school i"

    voice "2FU_0050"
    fumi "\"I'm a little humbled by how impressed you are.\"" id a07_comn_03_c_cd2efeb2

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
    miyako "\"I-I'm sorry for getting so excited.\"" id a07_comn_03_c_2b29f785

    show rin z4 2 lg school g with dict_dissolve_25

    voice "2RI_0066"
    rin "\"It's always like it's your first meal ever.\"" id a07_comn_03_c_8a4ab9df

    show fumi z4 1 lg school c with dict_dissolve_25

    voice "2FU_0051"
    fumi "\"Ahaha, it's nice to be appreciated.\"" id a07_comn_03_c_8e04ffca

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0074"
    hina "\"You always start with the color.\"" id a07_comn_03_c_55625358

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_0023"
    miyako "\"Yes. The taste and smell and texture are all wonderful too, but the color always catches my eye first.\"" id a07_comn_03_c_4cd23524

    show miyako z4 1 lg school_b b with dict_dissolve_25

    voice "2MI_0024"
    miyako "\"This tomato is such a beautiful...\"" id a07_comn_03_c_f041bd6f

    "She seemed to get stuck there."

    show rin z4 2 lg school a with dict_dissolve_25

    voice "2RI_0067"
    rin "\"Hm? Red?\"" id a07_comn_03_c_27d47e9a

    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_0025"
    miyako "\"Umm, yes, red... This is red, then.\"" id a07_comn_03_c_8e26f2c9

    "She looked at the tomato and repeated the word as if to create an association in her mind."

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_0068"
    rin "\"You speak like you're fluent, but you trip up at pretty weird places.\"" id a07_comn_03_c_e8a0e79f

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_0026"
    miyako "\"I'm still learning.\"" id a07_comn_03_c_38fad1b4

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0075"
    hina "\"It's almost like you're from a land without color or something.\"" id a07_comn_03_c_d285dc5b

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_0027"
    miyako "\"...Aha.\"" id a07_comn_03_c_dd90bfdf

    "An astute observation."

    "It wasn't that Miyako didn't know the word \"red,\" it was that {i}she didn't know which color red was{/i}."

    show rin z4 1 lg school c with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2RI_0069"
    rin "\"Here, Takaoka. The peppers are a beautiful green, too.\"" id a07_comn_03_c_931922d4

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin said, attempting to foist her hated peppers onto Miyako."

    show fumi z4 2 lg school f with Dissolve(0.25)
    show fumi:
        ShakeJump

    voice "2FU_0052B"
    fumi "\"Hey!\"" id a07_comn_03_c_86c070b8

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
