label a04_cou3_03:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg02de with Dissolve(0.25)
    pause 0.75

    play music bgm02

    play sound se117a

    show rin:
        "rin 3 lg nightlight pyjama_bed_b glasses_c flat"
        alpha 0.0 xcenter 593 ycenter 478
        easein 0.5 alpha 1.0 xcenter 493
    pause 0.5

    stop sound fadeout 2.0

    show rin 3 lg nightlight pyjama_bed_b glasses_c:
        alpha 1.0 xcenter 493 ycenter 478
    with None

    voice "RIN_1285"
    rin "\"Heh heh heh.\"" id a04_cou3_03_20ffb366

    "Rin poked her head out of Fumi's bed."

    show fumi 3 lg nightlight pyjama e:
        xcenter 166 ycenter 546
    with dict_dissolve_25

    voice "FUM_1108"
    fumi "\"Waaah?! Ogata—\"" id a04_cou3_03_3aca5c9a

    "Fumi almost shouted in surprise, but Rin covered her mouth."

    show rin 3 lg nightlight pyjama_bed_b glasses_f with dict_dissolve_25

    voice "RIN_1286"
    rin "\"Don't make too much noise.\"" id a04_cou3_03_00b0485c

    "Rin looked over at the opposite bed."

    show hina 3 lg dark pyjama a with dict_dissolve_25

    voice "HIN_1494"
    hina "\"Mmn... mmn...\"" id a04_cou3_03_5ae52481

    hide hina with Dissolve(0.25)

    show rin 3 lg nightlight pyjama_bed_b glasses_c with dict_dissolve_25

    voice "RIN_1287"
    rin "\"Safe.\"" id a04_cou3_03_d46cd757

    show fumi 3 lg nightlight pyjama g with dict_dissolve_25

    voice "FUM_1109"
    fumi "\"Phah. Really, where do you think you're popping out from?\"" id a04_cou3_03_34264cc7

    "Fumi looked somewhat bothered by the intrusion."

    show rin 3 lg nightlight pyjama_bed_b glasses_i with dict_dissolve_25

    voice "RIN_1288"
    rin "\"It's warm in your bed~\"" id a04_cou3_03_18638a54

    "She wasn't listening."

    show fumi 3 lg nightlight pyjama d with dict_dissolve_25

    voice "FUM_1110"
    fumi "\"...Geez.\"" id a04_cou3_03_c5efa95c

    "Fumi sighed and closed her half-written diary."

    show fumi 3 lg nightlight pyjama e with dict_dissolve_25

    voice "FUM_1111"
    fumi "\"What if Natsume wakes up?\"" id a04_cou3_03_34201099

    show rin 3 lg nightlight pyjama_bed_b glasses_d with dict_dissolve_25

    voice "RIN_1289"
    rin "\"We'll just tell her she dreamed it.\"" id a04_cou3_03_30d32a7b

    show fumi 3 lg nightlight pyjama b with dict_dissolve_25

    voice "FUM_1112"
    fumi "\"Hmm...\"" id a04_cou3_03_33fa7a91

    "Fumi looked over at the other bed."

    show hina 3 lg dark pyjama a with dict_dissolve_25

    voice "HIN_1495"
    hina "\"Mmn... mmn...\"" id a04_cou3_03_62a095f9

    "Hina was curled up like a cat, snoring contentedly."

    hide hina with Dissolve(0.25)

    show fumi 3 lg nightlight pyjama d with dict_dissolve_25

    voice "FUM_1113"
    fumi "\"But, I really think—\"" id a04_cou3_03_4f60f62d

    show rin 3 lg nightlight pyjama_bed_b glasses_e with dict_dissolve_25

    voice "RIN_1290"
    rin "\"I really wanted to feel you.\"" id a04_cou3_03_4352e651

    show fumi 3 lg nightlight pyjama e with dict_dissolve_25

    voice "FUM_1114"
    fumi "\"Ah...\"" id a04_cou3_03_abceab8b

    "Rin whined, burying her face in Fumi's chest. Fumi felt the warmth of her breath and the cold metal of her glasses at the same time."

    voice "FUM_1115"
    fumi "\"...Does it have to be now?\"" id a04_cou3_03_75e524cd

    show rin 3 lg nightlight pyjama_bed_b glasses_c with dict_dissolve_25

    voice "RIN_1291"
    rin "\"Yeah, it does.\"" id a04_cou3_03_0769153b

    "Rin had a firm grip on Fumi's pajamas."

    show fumi 3 lg nightlight pyjama f with dict_dissolve_25

    voice "FUM_1116"
    fumi "\"What do I do with you...\"" id a04_cou3_03_6417829e

    "She didn't look that opposed to it, though."

    show fumi 3 lg nightlight pyjama c with dict_dissolve_25

    voice "FUM_1117"
    fumi "\"...Just for a little bit, okay?\"" id a04_cou3_03_9af2286f

    "She could feel Rin nod against her chest. Fumi smiled awkwardly and stroked the big child's hair."

    play sound se024a

    scene bg02da with Dissolve(0.25)
    pause 0.75

    "She turned off her light and gently removed Rin's glasses."

    if persistent.dpatch:
        jump a04_cou3_03_d
    else:
        stop music fadeout 1.0
        stop sound fadeout 1.0
        scene black with Dissolve(0.5)
        pause 3.5
        "........."
        "......"
        window hide
        pause 2.5
        window auto

label rp_scene07_end:

    scene bg02da with bg_effect_05
    pause 0.5

    play music bgm02

    show rin 3 lg dark znd g:
        alpha 1.0 xcenter 493 ycenter 478
    with Dissolve(0.25)

    voice "RIN_1318"
    rin "\"Haahh... Were you always this vicious, Asou?\"" id rp_scene07_end_c2029100

    "Her bitter voice came from under the covers."

    show fumi 3 lg dark pyjama c:
        xcenter 166 ycenter 546
    with dict_dissolve_25

    voice "FUM_1152"
    fumi "\"Vicious~? I was punishing you.\"" id rp_scene07_end_393a719f

    "Fumi said with a big smile."

    show fumi 3 lg dark pyjama b with dict_dissolve_25

    voice "FUM_1153"
    fumi "\"Did you not like being on the receiving end?\"" id rp_scene07_end_bbb3da0f

    show rin 3 lg dark znd d with dict_dissolve_25

    voice "RIN_1319"
    rin "\"I didn't... {i}not{/i} like it...\"" id rp_scene07_end_df917d5f

    "She could tell from her voice that Rin's face was bright red."

    show fumi 3 lg dark pyjama c with dict_dissolve_25

    voice "FUM_1154"
    fumi "\"Good.\"" id rp_scene07_end_86dfdab0

    "Fumi patted Rin's head through the blanket."

    show fumi 3 lg dark pyjama e with dict_dissolve_25

    voice "FUM_1155"
    fumi "\"Oh... that's right.\"" id rp_scene07_end_d02254f1

    show rin 3 lg dark znd b with dict_dissolve_25

    voice "RIN_1320"
    rin "\"What?\"" id rp_scene07_end_d8177d31

    show fumi 3 lg dark pyjama f with dict_dissolve_25

    voice "FUM_1156"
    fumi "\"You can't keep calling your wife by her last name, can you?\"" id rp_scene07_end_fdd1730d

    show rin 3 lg dark znd d with dict_dissolve_25

    voice "RIN_1321"
    rin "\"Huh? Ah... I couldn't really... find the right moment... you know.\"" id rp_scene07_end_48410436

    show fumi 3 lg dark pyjama d with dict_dissolve_25

    voice "FUM_1157"
    fumi "\"......\"" id rp_scene07_end_0320fa04

    "A wordless push."

    show rin 3 lg dark znd f with dict_dissolve_25

    voice "RIN_1322"
    rin "\"O-Okay...\"" id rp_scene07_end_5eff0070

    "Rin's hand timidly emerged from the blanket. Fumi placed her own hand over it."

    show rin 3 lg dark znd d with dict_dissolve_25

    voice "RIN_1323"
    rin "\"...Fumi.\"" id rp_scene07_end_5153695f

    show fumi 3 lg dark pyjama h with dict_dissolve_25

    voice "FUM_1158"
    fumi "\"Yes.\"" id rp_scene07_end_6936f53d

    "They squeezed each other's hands."

    show fumi 3 lg dark pyjama f with dict_dissolve_25

    voice "FUM_1159"
    fumi "\"Would you like a pet name from me?\"" id rp_scene07_end_9127b43c

    show rin 3 lg dark znd b with dict_dissolve_25

    voice "RIN_1324"
    rin "\"...That would be embarrassing, so 'Rin' will be just fine.\"" id rp_scene07_end_812c9a10

    show fumi 3 lg dark pyjama c with dict_dissolve_25

    voice "FUM_1160"
    fumi "\"Rin.\"" id rp_scene07_end_ff04c483

    show rin 3 lg dark znd d with dict_dissolve_25

    voice "RIN_1325"
    rin "\"Yes.\"" id rp_scene07_end_98ccf74b

    "Rin buried her face in the pillow. Fumi couldn't see it, but she could tell."

    show fumi 3 lg dark pyjama f with dict_dissolve_25

    voice "FUM_1161"
    fumi "\"You should get back to your bed and go to sleep now, or you won't be able to get up in the morning.\"" id rp_scene07_end_a0e6baee

    "She patted Rin's head again."

    show rin 3 lg dark znd g with dict_dissolve_25

    voice "RIN_1326"
    rin "\"...Nngh.\"" id rp_scene07_end_7cf9159f

    "A grumble."

    show fumi 3 lg dark pyjama e with dict_dissolve_25

    voice "FUM_1162"
    fumi "\"Rin?\"" id rp_scene07_end_f75e40fb

    show rin 3 lg dark znd e with dict_dissolve_25

    voice "RIN_1327"
    rin "\"...Okay.\"" id rp_scene07_end_01cf4d25

    play sound se116a

    hide rin with Dissolve(0.25)

    "With a reluctant nod, Rin fixed her clothes underneath the blanket."

    show fumi 3 lg dark pyjama h with dict_dissolve_25

    "She slid out from under the covers, and Fumi burst out laughing at the messy state of her hair."

    scene black with bg_effect_05
    pause 0.5

    scene bg02da with bg_effect_05
    pause 0.5

    "......"

    show rin:
        "rin 1 sm pyjama i flat"
        alpha 0.0 xcenter 412
        easein 0.5 alpha 1.0 xcenter 512

    "Rin slipped out of the bed so as to not let the heat escape."

    show rin 1 sm pyjama i:
        alpha 1.0 xcenter 512
    with None
    show rin 1 sm pyjama g with dict_dissolve_25

    voice "RIN_1328"
    rin "\"...Well, good night... Fumi.\"" id rp_scene07_end_89fe79b9

    show fumi 3 lg dark pyjama f with dict_dissolve_25

    voice "FUM_1163"
    fumi "\"Good night, Rin.\"" id rp_scene07_end_dbb2a846

    show fumi 3 lg dark pyjama h with dict_dissolve_25

    show rin:
        "rin 1 sm pyjama k" with Dissolve(0.25)
        ShakeTameiki

    "Rin bent down, Fumi stretched up, and they exchanged a brief kiss."

    scene black with Dissolve(0.5)
    pause 2.0

    $ side_image = "rin 1 side pyjama g"

    voice "RIN_1329"
    rin "\"...Am I a bottom?\"" id rp_scene07_end_e60b9590

    "Rin muttered to herself, climbing into her own bed."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
