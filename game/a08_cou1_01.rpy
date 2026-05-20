label a08_cou1_01:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0585"
    hina "\"Business is booming, huh?\""

    "An endless stream of questions meant Fumi's class would likely continue on a little longer."

    show miyako z4 1 lg school_a b:
        xcenter 172
    show rin z4 1 lg school g:
        xcenter 852
    with dict_dissolve_25

    voice "2RI_0599"
    rin "\"Seriously. Are there more people over there now? They've gotta be coming from other classes at this point, right?\""

    voice "2MI_0520"
    miyako "\"She's really amazing, answering each and every question like that.\""

    show hina z4 2 lg school g with dict_dissolve_25

    voice "2HI_0586"
    hina "\"Yeah. It might have been faster to just go to the home ec room and give them a demonstration.\""

    show rin:
        ShakeTameiki

    voice "2RI_0600"
    rin "\"Haahh... Do we have time to get groceries on our way home?\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0587"
    hina "\"We'll be fine. Fumi knows what we need.\""

    "It was starting to creep into Rin's voice how tired she was of waiting, but Hina was perfectly content."

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_0588"
    hina "\"Maybe I'll get Fumi to teach me too and make chocolate myself this year.\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_0521"
    miyako "\"What did you do until now?\""

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0589"
    hina "\"My mom or my sister always made it before. I just wrapped it.\""

    show rin z4 1 lg school f
    with Dissolve(0.25)

    show rin:
        1.75
        "rin z4 1 lg school j" with Dissolve(0.1)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False
    show hina:
        1.75
        "hina z4 2 lg school d" with Dissolve(0.25)

    play sound ["<silence 1.75>",se_2s_h001]

    voice "2RI_0601"
    rin "\"Ah, the ones with the huge—hgh!\""

    show rin z4 1 lg school j:
        xoffset 0 yoffset 0
    show hina z4 2 lg school d:
        xoffset 0 yoffset 0
    with None

    "A sharp kick to Rin's calf."

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_0590"
    hina "\"Well, I never had anyone to give it to but my dad before. But this year...\""

    "Hina's eyes were, of course, on Fumi."

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0522"
    miyako "\"That's wonderful.\""

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_0591"
    hina "\"Eheh.\""

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_0602"
    rin "\"I'm usually on the receiving end.\""

    show miyako z4 1 lg school_a g with dict_dissolve_25

    voice "2MI_0523"
    miyako "\"Ooh~\""

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_0592"
    hina "\"This is what I'm talking about.\""

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_0603"
    rin "\"What?\""

    show hina:
        "hina z4 1 lg school h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0593"
    hina "\"Haah...\""

    show hina z4 1 lg school h:
        xoffset 0 yoffset 0
    with None

    "It's clear she's not trying to be snide or sarcastic, but..."

    show rin z4 1 lg school k with Dissolve(0.25)
    show rin:
        6.0
        "rin z4 1 lg school f" with Dissolve(0.25)

    voice "2RI_0604"
    rin "\"I'm not really that into sweets, though. I can never eat them all. I know! I'll melt them down and give them back on White—\""

    show rin z4 1 lg school f with None

    voice "2HI_0594"
    hina "\"Seriously, this is what I'm talking about.\""

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_0605"
    rin "\"Huh? Are you mad?\""

    voice "2HI_0595"
    hina "\"I'm not mad, I'm just disgusted. Think about the feelings of the people giving you the chocolate.\""

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_0606"
    rin "\"I'm sure they're just giving it to me to give it to someone.\""

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_0596"
    hina "\"Still. It's not like you have to give them something homemade in return, but...\""

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_0607"
    rin "\"Wait, but if I melt them down, then they're homemade, right? Isn't that right, Mikoyan?\""

    show miyako z4 1 lg school_a c with dict_dissolve_25

    voice "2MI_0524"
    miyako "\"This is what she's talking about~\""

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_0608"
    rin "\"O-Oh?\""

    "It really is."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 0:
        jump a08_comn_03
    else:
        jump a08_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
