label a08_comn_03:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    $ side_image = "hina 2 side school f"

    voice "2HI_0440"
    hina "\"Huh? It's open?\""

    "Hina looked perpelexed when she stuck the key into the broadcasting room's door."

    $ side_image = "fumi 2 side school g"

    voice "2FU_0405B"
    fumi "\"Did a teacher forget to lock it? Oh, maybe someone's inside.\""

    $ side_image = "rin 1 side school f"

    voice "2RI_0474"
    rin "\"But is that someone alive?\""

    $ side_image = "hina 1 side school g"

    voice "2HI_0441"
    hina "\"Stop~ it~\""

    $ side_image = "miyako 1 side school_a b"

    voice "2MI_0310"
    miyako "\"Let's go in.\""

    play sound se_2s_f008
    pause 0.5

    play music bgm02

    scene bg10bb with Dissolve(0.5)
    pause 1.5

    "But it wasn't a ghost inside."

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0174"
    sachiko "\"Oh...\""

    $ side_image = "hina 1 side school k"

    voice "2HI_0442"
    hina "\"Sachiko?\""

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
    miyako "\"...?\""

    jump a08_comn_03_c

label a08_comn_03_c:

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0175"
    sachiko "\"Wait, what are you guys doing here?\""

    $ side_image = "hina 2 side school f"

    voice "2HI_0443"
    hina "\"We're here to return this.\""

    "Hina hefted the microphone she was carrying."

    $ side_image = "rin 1 side school h"

    voice "2RI_0475"
    rin "\"We should be asking you that. Why are you here, Sachiko?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0176"
    sachiko "\"Work. I come here and clean sometimes.\""

    $ side_image = "hina 1 side school k"

    voice "2HI_0444"
    hina "\"You're a janitor?\""

    $ side_image = "fumi 2 side school g"

    voice "2FU_0406"
    if persistent.dpatch:
        fumi "\"I've never seen you in the school, though.\"" id a08_comn_03_c_7feba120
    else:
        fumi "\"I've never seen you on campus, though.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0177"
    sachiko "\"I usually come during classes or on breaks.\""

    $ side_image = "rin 2 side school d"

    voice "2RI_0476"
    rin "\"...You need to take on more work to get by?\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0178"
    sachiko "\"Yeah, dorm management doesn't pay much... I haven't eaten since three days ago.\""

    $ side_image = "fumi 1 side school d"

    voice "2FU_0407"
    fumi "\"Weren't you eating pizza last night?\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0179"
    sachiko "\"Was I?\""

    $ side_image = "hina 1 side school h"

    voice "2HI_0445"
    hina "\"If you don't have any money, you could smoke less.\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0180"
    sachiko "\"Are you telling me to die?\""

    $ side_image = "rin 1 side school i"

    voice "2RI_0477"
    rin "\"That's a little extreme.\""

    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0181"
    sachiko "\"Actually, I'm saving money so I can make Sacchin Land and fill it with cute girls. I'll put you guys in it too, of course.\""

    $ side_image = "hina 1 side school g"

    voice "2HI_0446"
    hina "\"You will not!\""

    $ side_image = "miyako 1 side school_a e"

    voice "2MI_0312"
    miyako "\"......\""

    hide sachiko with dict_dissolve_50

    "While the four of them talked, Miyako headed into the room."

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0182"
    sachiko "\"Hey, where are you going?\""

    "Sachiko reached out and grabbed her."

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0313"
    miyako "\"I thought someone else might be here.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0183"
    sachiko "\"Nope. Just me.\""

    show miyako 1 sm school_b g with dict_dissolve_25

    voice "2MI_0314"
    miyako "\"I thought I sensed someone, though...\""

    "Miyako was looking up toward the ceiling."

    $ side_image = "hina 1 side school g"

    voice "2HI_0447"
    hina "\"Hwaaaaaaah!!\""

    "Hina screamed in fright when she realized what Miyako might be seeing."

    $ side_image = "rin 2 side school g"

    voice "2RI_0478"
    rin "\"Can you see spirits, Mikoyan?\""

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0315"
    miyako "\"Umm...\""

    hide miyako with Dissolve(0.25)

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0184"
    sachiko "\"Alright, you're getting in the way of my cleaning, so get out. I'll put away the mic.\""

    "Sachiko took the microphone from Hina."

    $ side_image = "hina 1 side school d"

    voice "2HI_0448"
    hina "\"Let's all go home, okay?!\""

    $ side_image = "rin 1 side school f"

    voice "2RI_0479"
    rin "\"In order to get to the truth of the matter, we must—\""

    $ side_image = "hina 1 side school g"

    voice "2HI_0449"
    hina "\"We must not!\""

    $ side_image = "fumi 1 side school d"

    voice "2FU_0408"
    fumi "\"Come on, we'll run out of time to go shopping.\""

    "Fumi hurried them out, sensing that Sachiko wanted to be alone."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0185"
    sachiko "\"See ya. I'll lock the door.\""

    $ side_image = "fumi 1 side school a"

    voice "2FU_0409"
    fumi "\"See you later.\""

    "Fumi pushed Hina and Rin out of the room."

    $ side_image = "miyako 2 side school a"

    voice "2MI_0316"
    miyako "\"......\""

    "Miyako was still looking around."

    $ side_image = "fumi 2 side school g"

    voice "2FU_0410"
    fumi "\"Miyako?\""

    $ side_image = "miyako 1 side school_a a"

    voice "2MI_0317"
    miyako "\"Yes, I'm coming.\""

    "Miyako followed the other three after bowing her head to Sachiko."

    stop music fadeout 0.1

    hide sachiko with dict_dissolve_50

    play sound se_2s_f007

    "........."

    "The broadcasting room regained its quiet with the girls gone."

    "Sachiko looked up to the spot Miyako had been focused on."

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0186"
    sachiko "\"...You're not there, are you?\""

    "With a little sigh, she put the microphone back on its shelf."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
