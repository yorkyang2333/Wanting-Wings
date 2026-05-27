label a09_cou4_02:

    scene bg05da with Dissolve(0.5)
    pause 1.5

    play sound se521
    pause 0.5

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0776"
    sachiko "\"Cold...!\"" id a09_cou4_02_23f8f47a

    "Sachiko came back from her patrol around the dorm, scrunching her shoulders up."

    play sound se_2s_f012

    "Her evening rounds would be over once she finished locking up."

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0777"
    sachiko "\"Mm, mm, mm... Should be good.\"" id a09_cou4_02_7ca2f5ae

    "Storing her shoes, she pointed as she went through her mental checklist."

    "For all her flaws, she does take her work seriously. At her core, she really must be—"

    play sound se_2s_d015

    "—?"

    "Sachiko noticed as well and looked toward where the sound had come from."

    "It was the stairs down the hallway. There was a faint light coming from upstairs."

    $ side_image = "sachiko 2 side outfit b"

    voice "2SA_0778"
    sachiko "\"...Someone there?\"" id a09_cou4_02_70117d0a

    "She turned in that direction."

    scene black with Dissolve(1.5)
    pause 0.5

    play sound se_2s_d015

    "The light was coming from the stairs."

    "She tip-toed over, crouching by the landing and peering upstairs."

    "There, she found—"

    pause 1.0

    scene bg05da
    show bg_obi
    with bg_effect_26_750
    pause 0.5

    "Miyako."

    "She was sitting on the stairs knitting with some difficulty. She must have been concentrating hard, because she hadn't noticed Sachiko."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0779"
    sachiko "\"Haahh...\"" id a09_cou4_02_82435b5f

    "Sachiko stood, sighing with a mix of relief and exasperation."

    show sachiko z4 2 lg outfit e:
        xcenter 726
    with dict_dissolve_25

    voice "2SA_0780"
    sachiko "\"What are you doing this late?\"" id a09_cou4_02_66445055

    $ side_image = "miyako 1 side pyjama_a f"

    voice "2MI_0940"
    miyako "\"A-Awawawah?!\"" id a09_cou4_02_990715fc

    play music bgm02

    show miyako:
        "miyako z4 1 lg pyjama_a f flat"
        alpha 0.0 xcenter 298 ycenter 857
        easein 0.25 alpha 1.0 ycenter 757

    "Miyako jumped up at the voice, and when she saw Sachiko's face, she hurriedly hid the scarf she was knitting behind her back."

    show miyako z4 1 lg pyjama_a f:
        alpha 1.0 xcenter 298 ycenter 757
    with None

    "She'd gotten advice from Fumi to keep it a secret from Sachiko, after all."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0781"
    sachiko "\"Huh... You started knitting?\"" id a09_cou4_02_fb799eb5

    voice "2MI_0941"
    miyako "\"Wh-What are you talking about? Uhh, I was just going to the bathroom...\"" id a09_cou4_02_c1fbbe21

    "Her room and the bathroom were both on the first floor. Not a very good excuse."

    show sachiko z4 2 lg outfit i with dict_dissolve_25

    voice "2SA_0782"
    sachiko "\"Well, you're hiding your project and your needles, but the yarn's just sitting there.\"" id a09_cou4_02_8f644cd2

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0942"
    miyako "\"A... Ahahaha. Right.\"" id a09_cou4_02_7d0ce892

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0783"
    sachiko "\"But why out here in the dark? You'll ruin your eyesight.\"" id a09_cou4_02_dffa5965

    show miyako z4 2 lg pyjama b with dict_dissolve_25

    voice "2MI_0943"
    miyako "\"I'll wake the other three up if I turn the light on in our room...\"" id a09_cou4_02_78f89283

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0784"
    sachiko "\"Then just come to m—\"" id a09_cou4_02_cd304896

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    "Sachiko suddenly stopped."

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0785"
    sachiko "\"So, how's your progress?\"" id a09_cou4_02_f9a37711

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0944"
    miyako "\"I'm not making much, since I'm not very good at it.\"" id a09_cou4_02_242adb24

    "Miyako smiled awkwardly and stretched out the scarf she had been hiding behind her back... or she would have if there had been anything to stretch. It was more wide than long."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0786"
    sachiko "\"Hopefully you finish it while it's still cold.\"" id a09_cou4_02_26cf3915

    show miyako:
        "miyako z4 2 lg pyjama e" with Dissolve(0.25)
        1.5
        ShakeTameiki

    voice "2MI_0945"
    miyako "\"Yeah... haah...\"" id a09_cou4_02_b9eaae9a

    show miyako z4 2 lg pyjama e:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0787"
    sachiko "\"Are you okay being awake this late, snooze monster?\"" id a09_cou4_02_d56993e2

    show miyako z4 2 lg pyjama h with dict_dissolve_25

    voice "2MI_0946"
    miyako "\"I've actually nodded off a few times—\"" id a09_cou4_02_b2a2fdc9

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0788"
    sachiko "\"Stupid. Go back to your room and sleep. You'll catch a cold out here.\"" id a09_cou4_02_ddc7686c

    voice "2MI_0947"
    miyako "\"...Okay.\"" id a09_cou4_02_f0dd9a60

    "Miyako collected her things obediently."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg05da with bg_effect_05
    pause 0.5

    show miyako 2 sm pyjama j with dict_dissolve_25

    voice "2MI_0948"
    miyako "\"Good night.\"" id a09_cou4_02_dda88780

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0789"
    sachiko "\"Night.\"" id a09_cou4_02_7d788b4e

    play sound se_doorcl

    hide miyako with Dissolve(0.5)

    pause 1.5

    stop music fadeout 1.0

    "........."

    $ side_image = "sachiko 2 side outfit d"

    voice "2SA_0790"
    sachiko "\"This kind of thing just isn't fair.\"" id a09_cou4_02_c0a59224

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a09_cou1_04
    else:
        jump a09_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
