label a08_comn_10:

    scene bg05aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0238"
    sachiko "\"Gimme a sec, I'll grab the stuff we need.\"" id a08_comn_10_bb0e4071

    "Sachiko called from the manager's room."

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0388"
    miyako "\"Okay.\"" id a08_comn_10_4cec6d9b

    "Miyako waited in the hallway."

    "She had come back separate from the three who went shopping so that she could help shovel snow like she'd promised that morning."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0239"
    sachiko "\"Is it done snowing?\"" id a08_comn_10_8a145185

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0389"
    miyako "\"Yes, it was finished by the time I got back. It's clear out now.\"" id a08_comn_10_68cec110

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0240"
    sachiko "\"We won't need slickers, then. Let's see...\"" id a08_comn_10_b259614c

    play sound se_2s_j044

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_0390"
    miyako "\"Does the snow get deeper than this in this area?\"" id a08_comn_10_8e71b6b4

    "........."

    "......"

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0391"
    miyako "\"...?\"" id a08_comn_10_564508b6

    hide miyako with dict_dissolve_50

    "The door opened right when Miyako put her hand on the knob."

    play sound se521
    pause 1.0

    show sachiko:
        "sachiko 1 lg outfit h flat"
        alpha 0.0 xcenter 152
        easein 0.5 alpha 1.0 xcenter 252

    voice "2SA_0241"
    sachiko "\"G-Got the stuff.\"" id a08_comn_10_b66f6a1f

    show sachiko 1 lg outfit h:
        alpha 1.0 xcenter 252
    with None
    show miyako 2 lg school a at pos_r with dict_dissolve_25

    voice "2MI_0392"
    miyako "\"R-Right.\"" id a08_comn_10_5c187edc

    "They were both a little flustered."

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0242"
    sachiko "\"Sorry for making you wait.\"" id a08_comn_10_28b18c21

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_0393"
    miyako "\"It's fine. Is that all we need?\"" id a08_comn_10_85d942cd

    "Sachiko held two shovels and a small bucket with gloves in it."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0243"
    sachiko "\"Yeah, the bigger one's up on the roof already.\"" id a08_comn_10_da551be1

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_0394"
    miyako "\"I see... Oh.\"" id a08_comn_10_03ec2d70

    show sachiko:
        ShakeYes

    pause 1.0

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show miyako 2 lg school_scarf a with Dissolve(0.5)
    pause 1.0


    $ miyako_scarf = "_scarf"

    "Sachiko wrapped a scarf around Miyako."

    show miyako 1 lg school_a_sei g with dict_dissolve_25

    voice "2MI_0395"
    miyako "\"What's this...?\"" id a08_comn_10_ea0420a4

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "2SA_0244"
    sachiko "\"A scarf. It's cold out there.\"" id a08_comn_10_16bd92a6

    show miyako 1 lg school_a_sei e with dict_dissolve_25

    voice "2MI_0396"
    miyako "\"You don't mind?\"" id a08_comn_10_83c93202

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0245"
    sachiko "\"Nope.\"" id a08_comn_10_ba2f9089

    show miyako 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1294a"
    miyako "\"...Cigarettes...\"" id a08_comn_10_eb2125b6

    "Miyako noticed the smell on the scarf."

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0246"
    sachiko "\"What's wrong? Is it uncomfortable? You don't like the design?\"" id a08_comn_10_3adb5764

    show miyako 1 lg school_a_sei g with dict_dissolve_25

    voice "2MI_0397"
    miyako "\"That's not it. I've just never seen you wearing a scarf.\"" id a08_comn_10_159d94ba

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0247"
    sachiko "\"Mm, well, I had it put away... I thought it'd look good on you, though.\"" id a08_comn_10_d4f97e33

    show miyako:
        "miyako 1 lg school_a_sei d" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0398"
    miyako "\"Really? Thank you!\"" id a08_comn_10_836051ea

    show miyako 1 lg school_a_sei d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0248"
    sachiko "\"Sure. Okay, let's go.\"" id a08_comn_10_7468e787

    show miyako 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_0399"
    miyako "\"Yes!\"" id a08_comn_10_87c4ba98

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
