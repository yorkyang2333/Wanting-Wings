label a10_cou1_03:

    scene bg01bg with Dissolve(0.5)
    pause 1.5

    play music bgm05 fadein 1.0

    "Hina and Fumi were alone in the room."

    "Today was their time alone. Rin and Miyako wouldn't be back for a while."

    "It's easy to tell what they were just doing from the way their clothes and hair are all disheveled."

    "But they don't have the usual sweet air around them."

    "Hina was hugging her knees next to Fumi, who was re-tying her hair."

    show fumi 2 lg pyjama a at pos_l
    show hina 2 lg pyjama_pjm h at pos_r
    with dict_dissolve_25

    voice "2HI_1202"
    hina "\"I'm sorry. I wasn't very good at it again.\"" id a10_cou1_03_3b7bc4b1

    "Hina mumbled, staring at her feet."

    show fumi 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0951"
    fumi "\"N-No... I should apologize...\"" id a10_cou1_03_22f2cb0f

    "Fumi shook her head and assigned the blame to herself instead."

    "Usually she would just say she was happy to feel Hina's skin against hers, but that wouldn't work today."

    voice "2HI_1203"
    hina "\"Am I not good at it because... it's unnatural?\"" id a10_cou1_03_1b5e02cd

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0952"
    fumi "\"Unnatural...?\"" id a10_cou1_03_f1fd9b93

    voice "2HI_1204"
    hina "\"Because we're both girls...\"" id a10_cou1_03_338d06a9

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0953"
    fumi "\"That's got nothing to do with it!\"" id a10_cou1_03_38345653

    "Fumi shot that down immediately."

    voice "2HI_1205"
    hina "\"...Fumi, I'm scared...\"" id a10_cou1_03_82ae73dd

    "Her expression was stiff."

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0954"
    fumi "\"What is it, Hina?\"" id a10_cou1_03_af096deb

    voice "2HI_1206"
    hina "\"I'm scared that we're doing something wrong...\"" id a10_cou1_03_7777a2c7

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0955"
    fumi "\"W...\"" id a10_cou1_03_bd2ff7c5

    "\"We're not!\" I'm guessing that's what she was about to say."

    show fumi 1 lg pyjama h with dict_dissolve_25

    "........."

    "......"

    hide fumi
    hide hina
    with dict_dissolve_50

    "That LIME from the other day had changed things for them."

    "They'd held each other's hands and planned to go through the rest of their lives hand in hand. That was completely natural to them."

    "But what if it wasn't natural to everyone else?"

    "That one drop of doubt had stained the purity of their relationship and was slowly beginning to spread."

    show fumi 2 lg pyjama f at pos_l
    show hina 2 lg pyjama_pjm d at pos_r
    with dict_dissolve_25

    $ voice2("hina","2HI_1207N","fumi","2FU_0956N")
    hina_fumi "\"Listen...\"\n\"U-Umm...\"" (what_rest_indent=0)

    "They said at the same time, then there was another stretch of silence."

    show fumi 2 lg pyjama h at pos_l
    show hina 2 lg pyjama_pjm h at pos_r
    with dict_dissolve_25

    $ voice2("hina","2HI_1208N","fumi","2FU_0957N")
    hina_fumi "\"You deserve somebody—\"\n\"You deserve someone—\"" (what_rest_indent=0)

    "After working up to it, they spoke at the same time again, but both stopped, sensing what the other was trying to say."

    "They were both worried about the other being vilified for being in an unnatural relationship."

    show hina 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_1209"
    hina "\"Can we still be friends after we graduate?\"" id a10_cou1_03_d4802878

    show fumi:
        ShakeYes

    "Fumi nodded."

    show fumi 2 lg pyjama a:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2FU_0958"
    fumi "\"Forever. I'll never forget you.\"" id a10_cou1_03_e6d6e39c

    show hina:
        "hina 2 lg pyjama_pjm h" with Dissolve(0.25)
        ShakeYes

    voice "2HI_1210"
    hina "\"Mm.\"" id a10_cou1_03_90a902f7

    show hina 2 lg pyjama_pjm h:
        xoffset 0 yoffset 0
    with None

    "They squeezed one another's hand."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
