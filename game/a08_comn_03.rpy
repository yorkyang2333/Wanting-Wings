label a08_comn_03:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    $ side_image = "hina 2 side school f"

    voice "2HI_0440"
    hina "\"Huh? It's open?\"" id a08_comn_03_69f6cf20

    "Hina looked perpelexed when she stuck the key into the broadcasting room's door."

    $ side_image = "fumi 2 side school g"

    voice "2FU_0405B"
    fumi "\"Did a teacher forget to lock it? Oh, maybe someone's inside.\"" id a08_comn_03_11876caf

    $ side_image = "rin 1 side school f"

    voice "2RI_0474"
    rin "\"But is that someone alive?\"" id a08_comn_03_5be1864f

    $ side_image = "hina 1 side school g"

    voice "2HI_0441"
    hina "\"Stop~ it~\"" id a08_comn_03_d3ed0975

    $ side_image = "miyako 1 side school_a b"

    voice "2MI_0310"
    miyako "\"Let's go in.\"" id a08_comn_03_7ccd7516

    play sound se_2s_f008
    pause 0.5

    play music bgm02

    scene bg10bb with Dissolve(0.5)
    pause 1.5

    "But it wasn't a ghost inside."

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0174"
    sachiko "\"Oh...\"" id a08_comn_03_4b68e474

    $ side_image = "hina 1 side school k"

    voice "2HI_0442"
    hina "\"Sachiko?\"" id a08_comn_03_5d35e5be

    if routes_cleared == 1:
        jump a08_comn_03_a
    elif routes_cleared >= 2:
        jump a08_comn_03_b

label a08_comn_03_a:

    "Sachiko put a blue notebook back on a shelf and came over to them, looking surprised."

    jump a08_comn_03_c

label a08_comn_03_b:
    python:
        _last_say_what = ""
        _last_say_who = None
        renpy.choice_for_skipping()

    pause 0.5

    stop music fadeout 1.0

    scene select_back3 with Dissolve(0.5)
    pause 1.5

    menu:
        "■選択肢１枠"((13,334), "menu/btn_select_0501"):
            jump a08_comn_03_g

label a08_comn_03_g:

    scene bg10bb with Dissolve(0.5)

    pause 0.5

    play music bgm02 fadein 0.5

    "Sachiko put the broadcasting club notebook back on the shelf and came over to them, looking surprised."

    $ side_image = "miyako 1 side school_b g"

    voice "2MI_0311"
    miyako "\"...?\"" id a08_comn_03_g_76f7a359

    jump a08_comn_03_c

label a08_comn_03_c:

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0175"
    sachiko "\"Wait, what are you guys doing here?\"" id a08_comn_03_c_a263ec34

    $ side_image = "hina 2 side school f"

    voice "2HI_0443"
    hina "\"We're here to return this.\"" id a08_comn_03_c_65832ea6

    "Hina hefted the microphone she was carrying."

    $ side_image = "rin 1 side school h"

    voice "2RI_0475"
    rin "\"We should be asking you that. Why are you here, Sachiko?\"" id a08_comn_03_c_18fc1cd0

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0176"
    sachiko "\"Work. I come here and clean sometimes.\"" id a08_comn_03_c_e0dc123d

    $ side_image = "hina 1 side school k"

    voice "2HI_0444"
    hina "\"You're a janitor?\"" id a08_comn_03_c_157d924e

    $ side_image = "fumi 2 side school g"

    voice "2FU_0406"
    if persistent.dpatch:
        fumi "\"I've never seen you in the school, though.\"" id a08_comn_03_c_7feba120
    else:
        fumi "\"I've never seen you on campus, though.\"" id a08_comn_03_c_3404bc77

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0177"
    sachiko "\"I usually come during classes or on breaks.\"" id a08_comn_03_c_cab2d050

    $ side_image = "rin 2 side school d"

    voice "2RI_0476"
    rin "\"...You need to take on more work to get by?\"" id a08_comn_03_c_252ad9ab

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0178"
    sachiko "\"Yeah, dorm management doesn't pay much... I haven't eaten since three days ago.\"" id a08_comn_03_c_ba41673a

    $ side_image = "fumi 1 side school d"

    voice "2FU_0407"
    fumi "\"Weren't you eating pizza last night?\"" id a08_comn_03_c_f2bce814

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0179"
    sachiko "\"Was I?\"" id a08_comn_03_c_c6a2d461

    $ side_image = "hina 1 side school h"

    voice "2HI_0445"
    hina "\"If you don't have any money, you could smoke less.\"" id a08_comn_03_c_383231d7

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0180"
    sachiko "\"Are you telling me to die?\"" id a08_comn_03_c_b558fcb5

    $ side_image = "rin 1 side school i"

    voice "2RI_0477"
    rin "\"That's a little extreme.\"" id a08_comn_03_c_9c40fd5e

    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0181"
    sachiko "\"Actually, I'm saving money so I can make Sacchin Land and fill it with cute girls. I'll put you guys in it too, of course.\"" id a08_comn_03_c_7ebb4cd3

    $ side_image = "hina 1 side school g"

    voice "2HI_0446"
    hina "\"You will not!\"" id a08_comn_03_c_11d4fd74

    $ side_image = "miyako 1 side school_a e"

    voice "2MI_0312"
    miyako "\"......\"" id a08_comn_03_c_0abd3833

    hide sachiko with dict_dissolve_50

    "While the four of them talked, Miyako headed into the room."

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0182"
    sachiko "\"Hey, where are you going?\"" id a08_comn_03_c_20cd669d

    "Sachiko reached out and grabbed her."

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0313"
    miyako "\"I thought someone else might be here.\"" id a08_comn_03_c_1b8b82fc

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0183"
    sachiko "\"Nope. Just me.\"" id a08_comn_03_c_2a83a6c0

    show miyako 1 sm school_b g with dict_dissolve_25

    voice "2MI_0314"
    miyako "\"I thought I sensed someone, though...\"" id a08_comn_03_c_b7b51abc

    "Miyako was looking up toward the ceiling."

    $ side_image = "hina 1 side school g"

    voice "2HI_0447"
    hina "\"Hwaaaaaaah!!\"" id a08_comn_03_c_404a3440

    "Hina screamed in fright when she realized what Miyako might be seeing."

    $ side_image = "rin 2 side school g"

    voice "2RI_0478"
    rin "\"Can you see spirits, Mikoyan?\"" id a08_comn_03_c_d7f434d4

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0315"
    miyako "\"Umm...\"" id a08_comn_03_c_4df41777

    hide miyako with Dissolve(0.25)

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0184"
    sachiko "\"Alright, you're getting in the way of my cleaning, so get out. I'll put away the mic.\"" id a08_comn_03_c_6d056c0c

    "Sachiko took the microphone from Hina."

    $ side_image = "hina 1 side school d"

    voice "2HI_0448"
    hina "\"Let's all go home, okay?!\"" id a08_comn_03_c_7e723f5e

    $ side_image = "rin 1 side school f"

    voice "2RI_0479"
    rin "\"In order to get to the truth of the matter, we must—\"" id a08_comn_03_c_4fef5e92

    $ side_image = "hina 1 side school g"

    voice "2HI_0449"
    hina "\"We must not!\"" id a08_comn_03_c_b3a99fe2

    $ side_image = "fumi 1 side school d"

    voice "2FU_0408"
    fumi "\"Come on, we'll run out of time to go shopping.\"" id a08_comn_03_c_a7112aa7

    "Fumi hurried them out, sensing that Sachiko wanted to be alone."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0185"
    sachiko "\"See ya. I'll lock the door.\"" id a08_comn_03_c_64e5d8e3

    $ side_image = "fumi 1 side school a"

    voice "2FU_0409"
    fumi "\"See you later.\"" id a08_comn_03_c_be07912f

    "Fumi pushed Hina and Rin out of the room."

    $ side_image = "miyako 2 side school a"

    voice "2MI_0316"
    miyako "\"......\"" id a08_comn_03_c_0392ec5e

    "Miyako was still looking around."

    $ side_image = "fumi 2 side school g"

    voice "2FU_0410"
    fumi "\"Miyako?\"" id a08_comn_03_c_9dbd6173

    $ side_image = "miyako 1 side school_a a"

    voice "2MI_0317"
    miyako "\"Yes, I'm coming.\"" id a08_comn_03_c_fe320dfd

    "Miyako followed the other three after bowing her head to Sachiko."

    stop music fadeout 0.1

    hide sachiko with dict_dissolve_50

    play sound se_2s_f007

    "........."

    "The broadcasting room regained its quiet with the girls gone."

    "Sachiko looked up to the spot Miyako had been focused on."

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0186"
    sachiko "\"...You're not there, are you?\"" id a08_comn_03_c_af3c4d8c

    "With a little sigh, she put the microphone back on its shelf."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
