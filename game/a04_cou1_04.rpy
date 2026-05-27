label a04_cou1_04:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg06ba with Dissolve(0.25)
    pause 0.75

    play sound organ04
    play sound2 se061

    show fumi 1 lg school a with Dissolve(0.25)

    "Fumi was playing the chapel's organ."

    if persistent.dpatch:
        "She had been entrusted with the organ accompaniment of the Christmas hymn recital, and had received special permission to practice the instrument after school." id a04_cou1_04_84fa1786
    else:
        "She had been entrusted with the organ accompaniment of the Christmas hymn recital, and had received special permission to practice the instrument after class."

    play sound2 [se061,se061]

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0901"
    fumi "\"Umm...\"" id a04_cou1_04_5ae48b52

    stop sound fadeout 1.0

    "Fumi paused."

    play music bgm02

    show fumi:
        xcenter 512
        easein 0.25 xcenter 252
    show hina 1 lg school d at pos_r with dict_dissolve_25

    voice "HIN_1077"
    hina "\"Oh, am I bothering you?\"" id a04_cou1_04_436a87eb

    "Hina was standing at the pulpit with her toy camera."

    "She had been standing and crouching all around the organ, snapping the camera shutter again and again."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0902"
    fumi "\"Not exactly, but... is it any fun getting pictures of me?\"" id a04_cou1_04_a3adebaa

    show hina:
        "hina 1 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_1078"
    hina "\"Of course it is! I want your picture more than anything else right now.\"" id a04_cou1_04_d4ac342a

    show hina 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0903"
    fumi "\"Do you?\"" id a04_cou1_04_15672c87

    show hina 1 lg school a with dict_dissolve_25

    voice "HIN_1079"
    hina "\"I told you I only take pictures of things I love.\"" id a04_cou1_04_c9469032

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0904"
    fumi "\"I-I suppose I should say... thank you, then?\"" id a04_cou1_04_7db3ee85

    "She stammered, not knowing what else to say."

    show hina 2 lg school b with dict_dissolve_25

    voice "HIN_1080"
    hina "\"I said I wanted to get another picture of an angel before, remember?\"" id a04_cou1_04_f61e8ddf

    "Fumi nodded."

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_1081"
    hina "\"Well, I just did, since I got a picture of you♪\"" id a04_cou1_04_90ac775d

    show fumi:
        "fumi 1 lg school e" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0905"
    fumi "\"W-Wawah...\"" id a04_cou1_04_eab5ce0f

    show fumi 1 lg school e:
        xoffset 0 yoffset 0
    with None

    "Sometimes Hina says really embarrassing things without realizing it, and it's always the person she says them to that suffers for it."

    show hina 1 lg school c with dict_dissolve_25

    voice "HIN_1082"
    hina "\"I want to take better pictures of you than anyone else in the world. I bet I can, too!\"" id a04_cou1_04_2b1eb037

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0906"
    fumi "\"U-Umm... I'd like that, I think.\"" id a04_cou1_04_5fdcb11c

    show hina 2 lg school g with dict_dissolve_25

    voice "HIN_1083"
    hina "\"I'm gonna keep going, then. Oh, you should keep practicing; don't mind me.\"" id a04_cou1_04_5cb77205

    hide hina
    with Dissolve(0.25)

    show fumi:
        "fumi 1 lg school h" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 512
    pause 0.25

    voice "FUM_0907"
    fumi "\"Alright...\"" id a04_cou1_04_4412d68b

    play sound organ02

    $ side_image = "hina 1 side school h"

    voice "HIN_1084"
    hina "\"You look kind of stiff, Fumi. Just practice like normal.\"" id a04_cou1_04_11b96675

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0908"
    fumi "\"R-Right.\"" id a04_cou1_04_d31cf796

    "Fumi only got more nervous when Hina said that."

    $ side_image = "hina 1 side school c"

    voice "HIN_1085"
    hina "\"Relax, relax~♪\"" id a04_cou1_04_db33c72a

    stop sound fadeout 1.0

    show fumi 1 lg school h with Dissolve(0.25)
    show fumi:
        ShakeUji

    voice "FUM_0909"
    fumi "\"U-Uuugh...\"" id a04_cou1_04_fa68c2cf

    show fumi:
        xoffset 0 yoffset 0
    with None

    "She'd likely taken all the candid shots she was going to get today..."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
