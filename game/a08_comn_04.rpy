label a08_comn_04:

    if route2 == 1:
        scene bg01cg
    else:
        scene bg01ch
    with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Lounging after dinner."

    "But the usually relaxed air was more prickly today."

    show hina 1 lg pyjama_pjm h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_0450"
    hina "\"Tests, tests... After tests, tests... Why do we even live...\"" id a08_comn_04_e1abc2b6

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina faced her notes, muttering something rather frightening. She was the source of the prickliness."

    "It's a scene we've seen before. She was studying for her upcoming proficiency tests."

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0451"
    hina "\"Proficiency tests are even nastier than midterms and finals.\"" id a08_comn_04_df5c3807

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0480"
    rin "\"Why's~ that~?\"" id a08_comn_04_0bdabf40

    "A lazy voice replied to her from under the table. As always, Rin didn't have to do much studying for tests."

    show hina 1 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0452"
    hina "\"Because they cover too much!\"" id a08_comn_04_e51e966f

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0411"
    fumi "\"It's stuff from both first and second semester, yes.\"" id a08_comn_04_d773324a

    "Fumi pinched the pages of the textbook that the test would cover."

    show hina:
        "hina 1 lg pyjama_pjm d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0453"
    hina "\"That's almost the whole thing!\"" id a08_comn_04_76d4b683

    show hina 1 lg pyjama_pjm d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0481"
    rin "\"Stuff like this~ is really about the work you put in every day~\"" id a08_comn_04_a6e842b9

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0454"
    hina "\"Really pisses me off to hear that from someone lying around on the floor.\"" id a08_comn_04_d7aa29be

    hide hina
    with Dissolve(0.25)

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0318"
    miyako "\"Umm, I have a question.\"" id a08_comn_04_366e7e40

    "Miyako, copying some notes, addressed their original author, Fumi."

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0319"
    miyako "\"It says here that Minamoto no Yoshitsune committed suicide in the Battle of Koromo River in Oushuu, but what about after that?\"" id a08_comn_04_70d9d3bb

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0412"
    fumi "\"Umm, after that?\"" id a08_comn_04_69370e26

    "Miyako pointed at the notes in question and Fumi stared blankly back at her."

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0482"
    rin "\"He actually lived and crossed over to the continent from Ezo, becoming Genghis Khan.\"" id a08_comn_04_92283620

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0320"
    miyako "\"Yes—\"" id a08_comn_04_599336a7

    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_0455"
    hina "\"Huh? Seriously?!\"" id a08_comn_04_5759763d

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_0483"
    rin "\"Nah, it's legend, myth, folklore. Not academic stuff. The historical record shows it's nonsense.\"" id a08_comn_04_b0e8f778

    show miyako:
        xcenter 512
        easein 0.5 xcenter 252
    pause 1.0

    show rin:
        "rin 2 lg pyjama glasses a flat"
        alpha 0.0 xcenter 772 ycenter 1116
        easein 1.0 alpha 1.0 ycenter 1016

    "Rin shut her book and sat up."

    show miyako:
        xcenter 252
    show rin 2 lg pyjama glasses a:
        alpha 1.0 xcenter 772 ycenter 1016
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0484"
    rin "\"You throw some really wild jokes around without warning sometimes, Mikoyan. That's not good. Idiots'll take you seriously.\"" id a08_comn_04_60635afa

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0456"
    hina "\"Hey! Don't throw insults without warning either! Look at me! No, don't look at me!\"" id a08_comn_04_84132bd5

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0321"
    miyako "\"But that really—\"" id a08_comn_04_870fc5fa

    show miyako 2 lg pyjama b with dict_dissolve_25

    "Miyako stopped in the middle of her sentence as a realization hit her."

    "She was probably right."

    "She must have seen it."

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0413"
    fumi "\"Umm, are you okay?\"" id a08_comn_04_32ba9aad

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0322"
    miyako "\"Yes. I'm sorry for saying something so strange. Your notes are very easy to read, Fumi.\"" id a08_comn_04_b07e3a23

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0485"
    if persistent.dpatch:
        rin "\"Aren't Fumi's notes great? If you've got those, you've practically won already. I almost want to copy 'em and sell 'em at the school store.\"" id a08_comn_04_12117d9e
    else:
        rin "\"Aren't Fumi's notes great? If you've got those, you've practically won already. I almost want to copy 'em and sell 'em at the campus store.\"" id a08_comn_04_7792739a

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0414"
    fumi "\"...Please don't. That would be embarrassing.\"" id a08_comn_04_4b9f28fe

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0486"
    rin "\"Oh, the coloring is important here, so if you're copying it, borrow a marker and—oh?\"" id a08_comn_04_5efb97ba

    "Rin looked down at Miyako's notes and froze."

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0415"
    fumi "\"Hm? What is it?\"" id a08_comn_04_961ccfa0

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0487"
    rin "\"No, uhh... you've just got some unique handwriting, Mikoyan.\"" id a08_comn_04_b57a250c

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0323"
    miyako "\"Ahaha, it's not very good. I'm sure it looks worse next to Fumi's nice handwriting, too.\"" id a08_comn_04_cf85745c

    "Miyako scratched her head, embarrassed."

    "The writing on her notes was less unique and more... clumsy."

    show miyako 2 lg pyjama b with dict_dissolve_25

    voice "2MI_0324"
    miyako "\"I'm not used to it yet. Just looking and doing it are pretty different.\"" id a08_comn_04_60277b76

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0457"
    hina "\"It's like you only just started writing. Is that because you were abroad, too?\"" id a08_comn_04_eaaa06e8

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0416"
    fumi "\"You're very fluent when speaking. It's a little strange.\"" id a08_comn_04_87553721

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0325"
    miyako "\"Ahaha, I have to practice.\"" id a08_comn_04_769f0cc0

    hide miyako
    with Dissolve(0.3)

    show hina 1 lg pyjama_pjm f at pos_l
    with Dissolve(0.3)

    show rin 1 lg pyjama glasses b with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2HI_0458"
    hina "\"Ah! What are you doing?\"" id a08_comn_04_e1153064

    show rin:
        xoffset 0 yoffset 0
    with None

    "Hina suddenly shouted. Rin had picked up her notes."

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0488"
    rin "\"I'm helping you study. Uhh, English? You're writing everything down blindly again, I see.\"" id a08_comn_04_13639aba

    "The pages were indeed packed. Hina's study strategy seemed to just be \"write it down and try to remember.\""

    play sound se_2s_h023
    pause 0.5

    play sound2 se_2s_h023

    show rin 1 lg pyjama glasses c with Dissolve(0.25)
    show rin:
        0.3
        "rin 1 lg pyjama glasses d" with Dissolve(0.25)

    voice "2RI_0489"
    rin "\"...Pfft!\"" id a08_comn_04_d30e1714

    show rin 1 lg pyjama glasses d:
        pass
    with None

    "Rin suddenly burst out laughing, flipping through Hina's notes."

    show hina 1 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0459"
    hina "\"Hey, don't look at my notes and laugh!\"" id a08_comn_04_8ffd3948

    voice "2RI_0490"
    rin "\"Dahahaha!!\"" id a08_comn_04_c1672fc0

    "It {i}is{/i} pretty rude to laugh that hard."

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0491"
    rin "\"Well, you have '{i}uchuu kuukan{/i}' as 'space space'! Talk about a literal translation!\"" id a08_comn_04_4250eab1

    "That should be \"outer space.\""

    show hina:
        "hina 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0460"
    hina "\"Shut up! Shut up! Give them back!\"" id a08_comn_04_7e833418

    show hina 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0492"
    rin "\"No, I wanna see more. You don't find joke books like this just anywhere!\"" id a08_comn_04_2e6b9f6f

    show hina:
        "hina 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0461"
    hina "\"It's not a joke book!\"" id a08_comn_04_e65d9aa6

    hide hina
    hide rin
    with dict_dissolve_25

    "Hina leapt at Rin to take back her notebook, but Rin used the length of her arms to keep it from her."

    show fumi 2 lg pyjama g at pos_l
    show miyako 2 lg pyjama a at pos_r
    with dict_dissolve_25

    voice "2FU_0417"
    fumi "\"Are you going to go into the science class or the arts class, Miyako?\"" id a08_comn_04_58a2d0a7

    "Their messing around was nothing out of the ordinary, so Fumi remained unbothered even with the ruckus they were making next to her."

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0326"
    miyako "\"I don't know... I suppose it will depend on my tests.\"" id a08_comn_04_27685975

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0418"
    fumi "\"Your tests, huh... Do you have any plans for your future?\"" id a08_comn_04_d6dac213

    show miyako 2 lg pyjama f with dict_dissolve_25

    voice "2MI_0327"
    miyako "\"Hmm~, no, I don't have anything like that yet. I'm sorry.\"" id a08_comn_04_fdcd6492

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0419"
    fumi "\"No, I think it's fine to not rush it. You can take your time deciding what you want to do.\"" id a08_comn_04_1f2874b0

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0328"
    miyako "\"Thank you. It's very exciting to think about the future though, isn't it?\"" id a08_comn_04_521b095b

    "That's right. Since there was no real difference between past, present, or future for her until just recently, this was a new sensation."

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "2FU_0420"
    fumi "\"I agree. Even worrying about it is kind of fun, isn't it?\"" id a08_comn_04_806af081

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0329"
    miyako "\"Are you thinking about your future already, Fumi?\"" id a08_comn_04_b685acae

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0421"
    fumi "\"I've wanted to make sweets for a living ever since I was little.\"" id a08_comn_04_bdcb0c74

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0330"
    miyako "\"I see. Is that arts? Or science?\"" id a08_comn_04_5f40451e

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0422"
    fumi "\"...I-I'm not sure.\"" id a08_comn_04_00c4780a

    hide fumi
    hide miyako
    with Dissolve(0.25)

    play sound se521
    pause 1.0

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0187"
    sachiko "\"Heeey, you can use the bath now~\"" id a08_comn_04_0a282811

    "Oh, it's Sachiko."

    show sachiko:
        "sachiko 2 sm outfit c flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0462"
    hina "\"Ah, you came in without knocking again!\"" id a08_comn_04_2f5c80d7

    show sachiko 2 sm outfit c:
        alpha 1.0 xcenter 512
    with None
    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0188"
    sachiko "\"I~ did~ knock~ You guys were just making so much noise you didn't hear me~ I heard the ruckus from the hallway.\"" id a08_comn_04_56de8b2e

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0423"
    fumi "\"Sorry.\"" id a08_comn_04_fedcc708

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0189"
    sachiko "\"You don't need to apologize, Foomin. It's an old building though, so don't blame me if the floor falls out under you.\"" id a08_comn_04_7ae9cd23

    $ side_image = "rin 1 side pyjama glasses h"

    voice "2RI_0493"
    rin "\"Not my fault.\"" id a08_comn_04_6512ff43

    "Rin pointed at Hina."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0463"
    hina "\"It's not my fault either.\"" id a08_comn_04_0ec3a356

    "Hina pointed at Rin."

    $ side_image = "miyako 2 side pyjama f"

    voice "2MI_0331"
    miyako "\"It isn't my fault... is it?\"" id a08_comn_04_d788f1f3

    "Miyako raised her hand timidly."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0190"
    sachiko "\"Ah~ Yeah, yeah. I'm gonna hit up the other rooms too, so you should hurry up if you want the first go.\"" id a08_comn_04_6bee5a14

    $ side_image = "fumi 2 side pyjama i"

    voice "2FU_0424"
    fumi "\"Yay~ I bought all new bath stuff for today~\"" id a08_comn_04_a5bced3d

    "Looks like Fumi was already prepared."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0191"
    sachiko "\"Come on, the rest of you get ready, too. I'll join you in a bit.\"" id a08_comn_04_0d724d69

    "She added nonchalantly."

    $ side_image = "side/hina_rin_pyjama_sozai02_[route2].webp"

    $ voice2("hina","2HI_0464","rin","2RI_0494")
    hina_rin "\"You don't need to!\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0192"
    sachiko "\"Feh. Well, come make a report to me after you're done, then.\"" id a08_comn_04_4fe3a55a

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0425"
    fumi "\"Alright.\"" id a08_comn_04_50f42817

    hide sachiko with Dissolve(0.5)

    show fumi z4 1 lg pyjama a:
        xcenter 118 ycenter 757
    show miyako z4 1 lg pyjama_a b behind fumi, hina:
        xcenter 383 ycenter 757
    show hina z4 1 lg pyjama a:
        xcenter 641 ycenter 730
    show rin z4 1 lg pyjama glasses a:
        xcenter 906 ycenter 753
    with Dissolve(0.25)

    play sound se521
    pause 0.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0193"
    sachiko "\"Oh, and we're having that hot pot party tomorrow night~\"" id a08_comn_04_e299d608

    show fumi 1 lg pyjama c
    show miyako 1 lg pyjama_a c
    show hina z4 1 lg pyjama_pjm c
    show rin z4 1 lg pyjama glasses k
    with dict_dissolve_25

    $ voice4("hina","2HI_0465","rin","2RI_0495","fumi","2FU_0426","miyako","2MI_0332")
    hina_rin_fumi_miyako "\"Okay~\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
