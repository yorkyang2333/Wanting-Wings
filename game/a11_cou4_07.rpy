label a11_cou4_07:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_07:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09cb with Dissolve(0.25)
    pause 0.75

    play music bgm01 fadein 1.0

    "The manager's room, during the hot pot party."

    show bg_obi
    show sachiko 1 lg outfit f:
        xcenter 682
    with Dissolve(0.5)

    show sachiko:
        ShakeTameiki

    voice "2SA_1021"
    sachiko "\"Miiikoyan?\""

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show miyako 1 lg pyjama_a f:
        xcenter 342
        function LayerShake(5,5,0.3)
    with dict_dissolve_25
    $ persistent.layer_shaken = False

    voice "2MI_1144"
    miyako "\"Wah!\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Sachiko put her arm around Miyako's shoulder jovially. She's got some booze in her at this point."

    show sachiko 1 lg outfit c with dict_dissolve_25

    voice "2SA_1022"
    sachiko "\"You've been pretty quiet... Wait, have you been eating crab this whole time?\""

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_1145"
    miyako "\"Yes, I can't stop... snff, hm?\""

    "She noticed the smell."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_1023"
    sachiko "\"What, can you smell the alcohol?\""

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_1146"
    miyako "\"And the cigarettes underneath it.\""

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_1024"
    sachiko "\"You've got a pretty sensitive nose.\""

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_1147"
    miyako "\"Ah...\""

    "Miyako seemed to suddenly remember something."

    "It was probably..."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_1025"
    sachiko "\"What is it?\""

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_1148"
    miyako "\"Finding yourself sounds nice.\""

    show sachiko 1 lg outfit h with dict_dissolve_25

    voice "2SA_1026"
    sachiko "\"Huh? Where'd that come from?\""

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_1149"
    miyako "\"Traveling, experiencing all sorts of things... I just think you're really amazing.\""

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "2SA_1027"
    sachiko "\"Oh yeah?\""

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_1150"
    miyako "\"Painting, cooking. You've got all sorts of skills. I'm still trying to make sense of everything. It's not going too well.\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_1028"
    sachiko "\"You just need to get used to it. I've got a lot more tangible experience than you. A million years as an angel isn't even close to one year as a human. I'm sure you'll—\""

    show miyako 1 lg pyjama_b c with dict_dissolve_25

    voice "2MI_1151"
    miyako "\"Maybe I should travel to find myself, too.\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_1029"
    sachiko "\"You don't need to take a big trip to do that. You're finding stuff every day, aren't you?\""

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_1030"
    sachiko "\"You might think I'm impressive, but I think you're way more incredible.\""

    hide sachiko with dict_dissolve_50

    "Sachiko stood, giving Miyako a pat on the head."

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_1152"
    miyako "\"Where are you going?\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_1031"
    sachiko "\"I gotta make the soup.\""

    hide miyako
    hide bg_obi
    with dict_dissolve_50

    "She headed for the sink."

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_1032"
    sachiko "\"I didn't have anything, so I had to go out and find it.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
