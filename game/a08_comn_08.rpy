label a08_comn_08:

    scene bg05aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Morning. The dorm entrance."

    "The girls were scrambling to get their shoes on."

    show sachiko 1 sm outfit a:
        xcenter 152
    show miyako 1 sm school_a e behind sachiko, hina:
        xcenter 452
    show hina 1 sm school_scarf e:
        xcenter 632
    show rin 1 sm school_scarf a behind hina, fumi:
        xcenter 776
    show fumi 1 sm school_scarf a:
        xcenter 940
    with dict_dissolve_25

    voice "2SA_0221"
    sachiko "\"Heading out?\"" id a08_comn_08_d3a4952d

    "Sachiko languidly called out to them, broom in hand."

    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "2HI_0532"
    if persistent.dpatch:
        hina "\"We're going to school!\"" id a08_comn_08_9896a855
    else:
        hina "\"We're going to class!\"" id a08_comn_08_f2d16562

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0222"
    sachiko "\"You guys are always in a rush.\"" id a08_comn_08_5d3da41d

    show hina 1 sm school_scarf e with dict_dissolve_25

    voice "2HI_0533"
    hina "\"Yeah, and we basically know why.\"" id a08_comn_08_9cf80981

    show miyako:
        "miyako 2 sm school e" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0385"
    miyako "\"I'm sorry...\"" id a08_comn_08_761da605

    show miyako 2 sm school e:
        xoffset 0 yoffset 0
    with None

    "Miyako looked guilty."

    show rin 1 sm school_scarf h with dict_dissolve_25

    voice "2RI_0551RE"
    rin "\"Don't worry about me, just go on ahead!\"" id a08_comn_08_15aef027

    show hina:
        "hina 1 sm school_scarf g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0534"
    hina "\"You could help out a little too!\"" id a08_comn_08_bfe86de1

    show hina 1 sm school_scarf g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0464"
    fumi "\"I think we actually have a little more time to spare than usual today.\"" id a08_comn_08_22403e23

    "Sachiko glanced at the clock on the wall."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0223"
    sachiko "\"True. Maybe you don't have to run today.\"" id a08_comn_08_90af041a

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "2FU_0465"
    fumi "\"Probably. We've got a little bit of time before the bus leaves.\"" id a08_comn_08_0f9c9140

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0224"
    sachiko "\"That's good.\"" id a08_comn_08_d987d52e

    show hina 1 sm school_scarf k with dict_dissolve_25

    voice "2HI_0535"
    hina "\"Why?\"" id a08_comn_08_0e5e49c3

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0225"
    sachiko "\"Because there's snow on the ground.\"" id a08_comn_08_2fbf002c

    show hina 1 sm school_scarf c
    show rin 1 sm school_scarf g
    with dict_dissolve_25

    $ voice2("hina","2HI_0536","rin","2RI_0552N")
    hina_rin "\"Really?!\"\n\"Really~?\"" (what_rest_indent=0)

    "Clearly one was happier to hear that than the other."

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0226"
    sachiko "\"It's probably only up to your ankles at the most, though. But it's still dangerous to run.\"" id a08_comn_08_b7723417

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0466"
    fumi "\"That's true. We'll be careful.\"" id a08_comn_08_241d6bc3

    "This was more of a rural area than anything else, but it wasn't bad enough to be snowed in easily."

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0227"
    sachiko "\"Ah, Foomin. Sorry, but could I ask you to go shopping on your way home?\"" id a08_comn_08_dbcfe2ee

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_0467"
    fumi "\"Sure, for the hotpot tonight? What would you like me to buy?\"" id a08_comn_08_8281d9d7

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0228"
    sachiko "\"Thanks. I'll send you a LIME message later.\"" id a08_comn_08_40d54d20

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0468B"
    fumi "\"Oh, my battery's been acting up lately, so can you send it to the group too, just in case?\"" id a08_comn_08_2524d6c3

    show sachiko:
        "sachiko 1 sm outfit g" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0229"
    sachiko "\"Mm, got it.\"" id a08_comn_08_4ea8ed3c

    show sachiko 1 sm outfit g:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0553"
    rin "\"Of course, the group is basically just me. Hina's got an old flip phone, and Mikoyan doesn't even have a phone.\"" id a08_comn_08_8ef359f3

    show miyako 2 sm school a
    show hina 1 sm school_scarf k
    with dict_dissolve_25

    "The two had blank looks on their faces."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0230"
    if persistent.dpatch:
        sachiko "\"Oh, can I ask one more thing? After school's fine, but can I get one of you to help me shovel the roof?\"" id a08_comn_08_010cfa91
    else:
        sachiko "\"Oh, can I ask one more thing? After class is fine, but can I get one of you to help me shovel the roof?\"" id a08_comn_08_cfce38b9

    show hina:
        "hina 1 sm school_scarf d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0537"
    hina "\"What? Is the dorm gonna collapse from snow?\"" id a08_comn_08_1c9e69b9

    show hina 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0231"
    sachiko "\"No, it's not that bad. But you know, the building's old. I'm worried about the roof leaking.\"" id a08_comn_08_c44cb16b

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "2RI_0554"
    rin "\"It really is showing its age in some places, isn't it?\"" id a08_comn_08_294ca117

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0232"
    sachiko "\"It's not real shoveling, you just gotta push some of it into the corners. It's real easy.\"" id a08_comn_08_7a02db2d

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0386"
    miyako "\"I'll help.\"" id a08_comn_08_d856a393

    "Miyako raised her hand."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0233"
    sachiko "\"Oh, thanks, Mikoyan.\"" id a08_comn_08_e6c96c51

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "2FU_0469"
    if persistent.dpatch:
        fumi "\"So, we'll go shopping after school, and Miyako will head home to help shovel.\"" id a08_comn_08_08fef3b1
    else:
        fumi "\"So, we'll go shopping after class, and Miyako will head home to help shovel.\"" id a08_comn_08_bdd0173b

    show miyako:
        "miyako 1 sm school_a c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0387"
    miyako "\"Yes.\"" id a08_comn_08_c2bf0151

    show miyako 1 sm school_a c:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0234"
    sachiko "\"That'll be great. Thanks.\"" id a08_comn_08_0e20551d

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "2RI_0555"
    rin "\"Ah, aren't we gonna be late for the bus now?\"" id a08_comn_08_718b005d

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "2FU_0470"
    fumi "\"Oh, you're right!\"" id a08_comn_08_89f45042

    show hina 1 sm school_scarf l with dict_dissolve_25

    voice "2HI_0538"
    hina "\"Hurry! I hear it!\"" id a08_comn_08_17dd71f9

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0235"
    sachiko "\"You've got good ears.\"" id a08_comn_08_b2191c8f

    hide hina
    hide rin
    hide fumi
    hide miyako
    with Dissolve(0.5)

    play sound se521
    pause 0.5

    "The four of them ran out."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0236"
    sachiko "\"Don't fall!\"" id a08_comn_08_11ff3c45

    $ side_image = "hina 1 side school_scarf d"

    voice "2HI_0539"
    hina "\"Hyaaaah?!\"" id a08_comn_08_9c14b8e8

    show sachiko 2 sm outfit d with dict_dissolve_25

    voice "2SA_0237"
    sachiko "\"......\"" id a08_comn_08_9d078bf5

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
