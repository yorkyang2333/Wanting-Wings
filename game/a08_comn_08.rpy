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
    sachiko "\"Heading out?\""

    "Sachiko languidly called out to them, broom in hand."

    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "2HI_0532"
    if persistent.dpatch:
        hina "\"We're going to school!\"" id a08_comn_08_9896a855
    else:
        hina "\"We're going to class!\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0222"
    sachiko "\"You guys are always in a rush.\""

    show hina 1 sm school_scarf e with dict_dissolve_25

    voice "2HI_0533"
    hina "\"Yeah, and we basically know why.\""

    show miyako:
        "miyako 2 sm school e" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0385"
    miyako "\"I'm sorry...\""

    show miyako 2 sm school e:
        xoffset 0 yoffset 0
    with None

    "Miyako looked guilty."

    show rin 1 sm school_scarf h with dict_dissolve_25

    voice "2RI_0551RE"
    rin "\"Don't worry about me, just go on ahead!\""

    show hina:
        "hina 1 sm school_scarf g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0534"
    hina "\"You could help out a little too!\""

    show hina 1 sm school_scarf g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0464"
    fumi "\"I think we actually have a little more time to spare than usual today.\""

    "Sachiko glanced at the clock on the wall."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0223"
    sachiko "\"True. Maybe you don't have to run today.\""

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "2FU_0465"
    fumi "\"Probably. We've got a little bit of time before the bus leaves.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0224"
    sachiko "\"That's good.\""

    show hina 1 sm school_scarf k with dict_dissolve_25

    voice "2HI_0535"
    hina "\"Why?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0225"
    sachiko "\"Because there's snow on the ground.\""

    show hina 1 sm school_scarf c
    show rin 1 sm school_scarf g
    with dict_dissolve_25

    $ voice2("hina","2HI_0536","rin","2RI_0552N")
    hina_rin "\"Really?!\"\n\"Really~?\"" (what_rest_indent=0)

    "Clearly one was happier to hear that than the other."

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0226"
    sachiko "\"It's probably only up to your ankles at the most, though. But it's still dangerous to run.\""

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0466"
    fumi "\"That's true. We'll be careful.\""

    "This was more of a rural area than anything else, but it wasn't bad enough to be snowed in easily."

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0227"
    sachiko "\"Ah, Foomin. Sorry, but could I ask you to go shopping on your way home?\""

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_0467"
    fumi "\"Sure, for the hotpot tonight? What would you like me to buy?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0228"
    sachiko "\"Thanks. I'll send you a LIME message later.\""

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0468B"
    fumi "\"Oh, my battery's been acting up lately, so can you send it to the group too, just in case?\""

    show sachiko:
        "sachiko 1 sm outfit g" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0229"
    sachiko "\"Mm, got it.\""

    show sachiko 1 sm outfit g:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0553"
    rin "\"Of course, the group is basically just me. Hina's got an old flip phone, and Mikoyan doesn't even have a phone.\""

    show miyako 2 sm school a
    show hina 1 sm school_scarf k
    with dict_dissolve_25

    "The two had blank looks on their faces."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0230"
    if persistent.dpatch:
        sachiko "\"Oh, can I ask one more thing? After school's fine, but can I get one of you to help me shovel the roof?\"" id a08_comn_08_010cfa91
    else:
        sachiko "\"Oh, can I ask one more thing? After class is fine, but can I get one of you to help me shovel the roof?\""

    show hina:
        "hina 1 sm school_scarf d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0537"
    hina "\"What? Is the dorm gonna collapse from snow?\""

    show hina 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0231"
    sachiko "\"No, it's not that bad. But you know, the building's old. I'm worried about the roof leaking.\""

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "2RI_0554"
    rin "\"It really is showing its age in some places, isn't it?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0232"
    sachiko "\"It's not real shoveling, you just gotta push some of it into the corners. It's real easy.\""

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0386"
    miyako "\"I'll help.\""

    "Miyako raised her hand."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0233"
    sachiko "\"Oh, thanks, Mikoyan.\""

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "2FU_0469"
    if persistent.dpatch:
        fumi "\"So, we'll go shopping after school, and Miyako will head home to help shovel.\"" id a08_comn_08_08fef3b1
    else:
        fumi "\"So, we'll go shopping after class, and Miyako will head home to help shovel.\""

    show miyako:
        "miyako 1 sm school_a c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0387"
    miyako "\"Yes.\""

    show miyako 1 sm school_a c:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0234"
    sachiko "\"That'll be great. Thanks.\""

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "2RI_0555"
    rin "\"Ah, aren't we gonna be late for the bus now?\""

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "2FU_0470"
    fumi "\"Oh, you're right!\""

    show hina 1 sm school_scarf l with dict_dissolve_25

    voice "2HI_0538"
    hina "\"Hurry! I hear it!\""

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0235"
    sachiko "\"You've got good ears.\""

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
    sachiko "\"Don't fall!\""

    $ side_image = "hina 1 side school_scarf d"

    voice "2HI_0539"
    hina "\"Hyaaaah?!\""

    show sachiko 2 sm outfit d with dict_dissolve_25

    voice "2SA_0237"
    sachiko "\"......\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
