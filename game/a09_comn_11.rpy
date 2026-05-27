label a09_comn_11:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "—Break time. Hina's roommates were gathered around her desk."

    show hina z4 1 lg school a
    show fumi z4 1 lg school a:
        xcenter 172
    show rin z4 2 lg school a:
        xcenter 852
    with dict_dissolve_25

    voice "2HI_0799"
    hina "\"So, about Sachiko's chocolates.\"" id a09_comn_11_99ae95db

    "Hina looked up from the printouts she'd gathered from the class."

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_0806"
    rin "\"Now that you mention it, I'd totally forgotten about that. You're giving her some, Hina?\"" id a09_comn_11_08af79c5

    "Rin turned from where she was lazily looking out the window."

    show hina z4 1 lg school m with dict_dissolve_25

    voice "2HI_0800"
    hina "\"I'm not sure.\"" id a09_comn_11_ca249d6d

    show fumi z4 1 lg school e with dict_dissolve_25

    voice "2FU_0656"
    fumi "\"Huh? You're not giving her any?!\"" id a09_comn_11_badaee68

    "Fumi's stare toward both Hina and Rin accompanied her bewildered question."

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_0801"
    hina "\"We should probably give her some just as friends, huh?\"" id a09_comn_11_8c6b4849

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_0657"
    fumi "\"I was planning on it... huh?\"" id a09_comn_11_9b83325f

    "Fumi seemed perplexed by how unenthusiastic the other two were."

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_0807"
    rin "\"No, I get that we should give her some.\"" id a09_comn_11_c3d3c23c

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_0802"
    hina "\"It's just embarrassing handing them over all formally...\"" id a09_comn_11_f3aac8bf

    show fumi z4 1 lg school c with dict_dissolve_25

    voice "2FU_0658"
    fumi "\"Eheh, can't you just tell her they're thanks for her looking out for us?\"" id a09_comn_11_4ae2ce3d

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_0803"
    hina "\"Yeah. She {i}is{/i} taking care of us.\"" id a09_comn_11_4fb1b11a

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_0808"
    rin "\"Oh, can it be from all of us? Like, 'from the girls in Room 101.'\"" id a09_comn_11_5b723fd3

    show hina z4 1 lg school k with dict_dissolve_25

    voice "2HI_0804"
    hina "\"Maybe we can get some discounted Christmas wrapping paper for it.\"" id a09_comn_11_1e9b7153

    show fumi:
        "fumi z4 1 lg school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_0659"
    fumi "\"I don't think we should do that~\"" id a09_comn_11_a512d60f

    show fumi z4 1 lg school k:
        xoffset 0 yoffset 0
    with None

    if routes_cleared == 1:
        jump a09_comn_11_a
    else:
        jump a09_comn_11_end

label a09_comn_11_a:

    $ side_image = "miyako 1 side school_a g"

    voice "2MI_0741"
    miyako "\"Umm...\"" id a09_comn_11_a_1c34b7e6

    "Miyako timidly raised her hand."

    hide hina
    hide fumi
    hide rin
    with Dissolve(0.25)

    show miyako 1 lg school_a g with dict_dissolve_25

    $ side_image = "rin 1 side school c"

    voice "2RI_0809"
    rin "\"Oh, you want to get in on this too, Mikoyan?\"" id a09_comn_11_a_fbed502c

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_0742"
    miyako "\"Do you think I should?\"" id a09_comn_11_a_49610cc0

    show miyako:
        xcenter 512
        easein 0.25 xcenter 772

    show fumi 2 lg school c at pos_l with dict_dissolve_25

    voice "2FU_0660"
    fumi "\"You absolutely shouldn't!\"" id a09_comn_11_a_400b0e4a

    $ side_image = "rin 1 side school e"

    voice "2RI_0810"
    rin "\"Wha?\"" id a09_comn_11_a_04c84625

    "Fumi butted in."

    show fumi 2 lg school i with dict_dissolve_25

    voice "2FU_0661"
    fumi "\"You want to give Sachiko something more {i}personal{/i}, isn't that right, Miyako?!\"" id a09_comn_11_a_84209453

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_0743"
    miyako "\"Y-Yes, I suppose. If I can...\"" id a09_comn_11_a_7783ba07

    show fumi 1 lg school g with dict_dissolve_25

    voice "2FU_0662"
    fumi "\"We can't put Miyako's heartfelt chocolate in with our joint gift!\"" id a09_comn_11_a_48a08bc5

    "Fumi pointed at Rin as she scolded her."

    $ side_image = "rin 1 side school g"

    voice "2RI_0811"
    rin "\"...Sorry for asking.\"" id a09_comn_11_a_75efa419

    "Rin bowed her head, but Miyako shook hers."

    show fumi 2 lg school i with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_0663B"
    fumi "\"Special feelings should be conveyed with special chocolate!\"" id a09_comn_11_a_d2b193d6

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi grasped Miyako's hands. She's more enthusiastic about this than the person in question."

    show miyako 2 lg school f with dict_dissolve_25

    voice "2MI_0744"
    miyako "\"I-I'll do my best.\"" id a09_comn_11_a_2e136f63

    show fumi 2 lg school c with dict_dissolve_25

    voice "2FU_0664"
    if persistent.dpatch:
        fumi "\"I know! Want to come look at gift-wrapping materials with me after school?\"" id a09_comn_11_a_029e0c2c
    else:
        fumi "\"I know! Want to come look at gift-wrapping materials with me after class?\"" id a09_comn_11_a_c67c048b

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_0745"
    miyako "\"Umm, Christmas wrap?\"" id a09_comn_11_a_556a08c5

    show fumi 1 lg school h with dict_dissolve_25

    voice "2FU_0665"
    fumi "\"...No.\"" id a09_comn_11_a_62f4320c

    show fumi 1 lg school c with dict_dissolve_25

    voice "2FU_0666"
    fumi "\"They'll be all colorful and sparkling! We'll get some really pretty wrapping paper and ribbons to decorate the boxes with!\"" id a09_comn_11_a_1f735c1f

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_0746"
    miyako "\"Colorful and sparkling... that sounds fun!\"" id a09_comn_11_a_718f4981

    "That got her attention."

    show fumi 2 lg school i with dict_dissolve_25

    voice "2FU_0667"
    fumi "\"Yes, it's a lot of fun! Special chocolate has to have special wrapping!\"" id a09_comn_11_a_65178bc7

    show miyako:
        "miyako 1 lg school_a d" with Dissolve(0.25)
        ShakeYes
        1.5
        "miyako 1 lg school_a g" with Dissolve(0.25)

    voice "2MI_0747"
    miyako "\"I'd like that! ...But do you think I can do it?\"" id a09_comn_11_a_09b42f4e

    show miyako 1 lg school_a g:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school c with dict_dissolve_25

    voice "2FU_0668"
    fumi "\"Of course you can! I'll teach you how! Once we buy everything, I'll hold a wrapping lesson!\"" id a09_comn_11_a_9df1fa54

    show miyako 1 lg school_a c with dict_dissolve_25

    voice "2MI_0748"
    miyako "\"Thank you for all your help, really.\"" id a09_comn_11_a_48976c93

    show fumi 2 lg school i with dict_dissolve_25

    voice "2FU_0669"
    fumi "\"Just leave everything to me, really♪ This is fun for me too, after all.\"" id a09_comn_11_a_a4ab8ece

    "Some people find more happiness in cheering someone else on (especially in matters of love). One of them's right here. "

    show miyako 2 lg school h with dict_dissolve_25

    voice "2MI_0749"
    miyako "\"...Do you think she'll be happy about it?\"" id a09_comn_11_a_e15ea16b

    "Miyako muttered. She held a hand to her chest to stop it from throbbing, her face the face of a maiden in love, filled with anticipation and unease."

    $ side_image = "side/hina_rin_school_sozai01.webp"

    $ voice2("hina","2HI_0805","rin","2RI_0812N")
    hina_rin "\"Huh...\""

    "Even Rin and Hina, who were out of the loop, gave a curious sigh at that."

    scene black with Dissolve(1.5)
    pause 0.5

    "I see. So she's making faces like this now."

    "Huh..."

label a09_comn_11_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 2:
        jump a09_cou2_06
    elif routes_cleared >= 2:
        jump a09_cou4_03
    elif routes_cleared == 1:
        jump a09_comn_12
    elif route2 == 1:
        jump a09_cou1_06
    elif route2 == 3:
        jump a09_cou3_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
