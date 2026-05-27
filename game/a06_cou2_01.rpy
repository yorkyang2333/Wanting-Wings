label a06_cou2_01:

    $ route2 = 2
    $ hina_choker = "_choker"

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm03

    show hina 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0015"
    hina "\"Eheheheheheheh.\"" id a06_cou2_01_915dcdb0

    "Hina stole a glance at Fumi's face, eyes urging her for her opinion."

    $ side_image = "fumi 1 side pyjama c"

    voice "2FU_0015"
    fumi "\"Eheh, it looks great on you.\"" id a06_cou2_01_d8e73e9b

    show hina:
        "hina 1 lg pyjama_pjm p" with Dissolve(0.25)
        1.2
        "hina 2 lg pyjama_pjm g" with Dissolve(0.25)

    voice "2HI_0016"
    hina "\"Thanks, Asou♪ It's a collar Rin picked out for me, after all~\"" id a06_cou2_01_35776831

    show hina 2 lg pyjama_pjm g:
        xcenter 512
        easein 0.5 xcenter 252
    pause 0.5

    show rin 2 lg pyjama a at pos_r with dict_dissolve_25

    voice "2RI_0022"
    rin "\"It's not a collar. It's a choker. I bought it at an accessory shop. For humans. Not a pet store.\"" id a06_cou2_01_a8bf6b9f

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0017"
    hina "\"Either way, it's a present from you!\"" id a06_cou2_01_6e894791

    show rin:
        "rin 2 lg pyjama b" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0023"
    rin "\"Ngh... O-Only wear it in our room, okay?\"" id a06_cou2_01_b49d61c6

    show rin 2 lg pyjama b:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama_pjm l" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0018"
    hina "\"What?! I wanna wear it all the time, though!\"" id a06_cou2_01_65f9c786

    show hina 1 lg pyjama_pjm l:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama i with dict_dissolve_25

    voice "2RI_0024"
    if persistent.dpatch:
        rin "\"No. Who knows what people would say to you if you wore that to school.\"" id a06_cou2_01_e56c7ddc
    else:
        rin "\"No. Who knows what people would say to you if you wore that to class.\"" id a06_cou2_01_03f65964

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0019"
    hina "\"What? But it's a choker, right? It's fashion!\"" id a06_cou2_01_21923558

    show rin 1 lg pyjama h with dict_dissolve_25

    voice "2RI_0025"
    if persistent.dpatch:
        rin "\"Accessories are against the school rules. Aren't you class rep, Hina?\"" id a06_cou2_01_88a40e4e
    else:
        rin "\"Accessories are against the campus rules. Aren't you class rep, Hina?\"" id a06_cou2_01_adfec754

    show hina:
        "hina 1 lg pyjama_pjm o" with Dissolve(0.25)
        ShakeUji

    voice "2HI_0020"
    hina "\"Mmmm...!\"" id a06_cou2_01_23e73500

    show hina 1 lg pyjama_pjm o:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama h with dict_dissolve_25

    voice "2RI_0026"
    rin "\"Whining won't help. If you're not gonna be good, I'll take it back.\"" id a06_cou2_01_da44a7a7

    show hina 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0021"
    hina "\"Well, I...\"" id a06_cou2_01_3283bbb3

    "Hina fell silent for a short time, then took the collar off."

    play sound se_2s_f015

    show hina:
        "hina 2 lg pyjama -pyjama_pjm h" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0022"
    hina "\"......\"" id a06_cou2_01_36598803

    show hina 1 lg pyjama -pyjama_pjm n:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    "She silently handed it to Rin."

    show rin:
        "rin 1 lg pyjama j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_0027"
    rin "\"Huh? Really? You don't want it?!\"" id a06_cou2_01_93732d38

    show rin 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    "Now Rin was the one panicking, after she'd given it back so easily."

    show hina 1 lg pyjama e with dict_dissolve_25

    voice "2HI_0023"
    hina "\"No. I want you to hold onto it.\"" id a06_cou2_01_ed91b743

    show rin:
        "rin 1 lg pyjama g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0028"
    rin "\"Huh? You want me to wear it?\"" id a06_cou2_01_86e5da4a

    show rin 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama g with dict_dissolve_25

    voice "2HI_0024"
    hina "\"No! I want you to put it on me when you want me to wear it!\"" id a06_cou2_01_6fe484b4

    show rin:
        "rin 2 lg pyjama e" with Dissolve(0.25)
        1.5
        "rin 2 lg pyjama b" with Dissolve(0.25)

    voice "2RI_0029"
    rin "\"Oh, I get it. Why does it feel heavier all of the sudden...\"" id a06_cou2_01_e2acc03f

    show rin 2 lg pyjama b with None

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0016"
    fumi "\"Ahaha.\"" id a06_cou2_01_5ff44ef0

    show rin 2 lg pyjama d with dict_dissolve_25

    voice "2RI_0030"
    rin "\"You know... I tend to lose things.\"" id a06_cou2_01_003f3f69

    show hina 1 lg pyjama f with dict_dissolve_25
    $ side_image = "fumi 1 side pyjama g"

    $ voice2("hina","2HI_0025N","fumi","2FU_0017RE")
    hina_fumi "\"Be careful.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
