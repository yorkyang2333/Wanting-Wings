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
    hina "\"Tests, tests... After tests, tests... Why do we even live...\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina faced her notes, muttering something rather frightening. She was the source of the prickliness."

    "It's a scene we've seen before. She was studying for her upcoming proficiency tests."

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0451"
    hina "\"Proficiency tests are even nastier than midterms and finals.\""

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0480"
    rin "\"Why's~ that~?\""

    "A lazy voice replied to her from under the table. As always, Rin didn't have to do much studying for tests."

    show hina 1 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0452"
    hina "\"Because they cover too much!\""

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0411"
    fumi "\"It's stuff from both first and second semester, yes.\""

    "Fumi pinched the pages of the textbook that the test would cover."

    show hina:
        "hina 1 lg pyjama_pjm d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0453"
    hina "\"That's almost the whole thing!\""

    show hina 1 lg pyjama_pjm d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0481"
    rin "\"Stuff like this~ is really about the work you put in every day~\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0454"
    hina "\"Really pisses me off to hear that from someone lying around on the floor.\""

    hide hina
    with Dissolve(0.25)

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0318"
    miyako "\"Umm, I have a question.\""

    "Miyako, copying some notes, addressed their original author, Fumi."

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0319"
    miyako "\"It says here that Minamoto no Yoshitsune committed suicide in the Battle of Koromo River in Oushuu, but what about after that?\""

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0412"
    fumi "\"Umm, after that?\""

    "Miyako pointed at the notes in question and Fumi stared blankly back at her."

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0482"
    rin "\"He actually lived and crossed over to the continent from Ezo, becoming Genghis Khan.\""

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0320"
    miyako "\"Yes—\""

    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_0455"
    hina "\"Huh? Seriously?!\""

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_0483"
    rin "\"Nah, it's legend, myth, folklore. Not academic stuff. The historical record shows it's nonsense.\""

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
    rin "\"You throw some really wild jokes around without warning sometimes, Mikoyan. That's not good. Idiots'll take you seriously.\""

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0456"
    hina "\"Hey! Don't throw insults without warning either! Look at me! No, don't look at me!\""

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0321"
    miyako "\"But that really—\""

    show miyako 2 lg pyjama b with dict_dissolve_25

    "Miyako stopped in the middle of her sentence as a realization hit her."

    "She was probably right."

    "She must have seen it."

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0413"
    fumi "\"Umm, are you okay?\""

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0322"
    miyako "\"Yes. I'm sorry for saying something so strange. Your notes are very easy to read, Fumi.\""

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0485"
    if persistent.dpatch:
        rin "\"Aren't Fumi's notes great? If you've got those, you've practically won already. I almost want to copy 'em and sell 'em at the school store.\"" id a08_comn_04_12117d9e
    else:
        rin "\"Aren't Fumi's notes great? If you've got those, you've practically won already. I almost want to copy 'em and sell 'em at the campus store.\""

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0414"
    fumi "\"...Please don't. That would be embarrassing.\""

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0486"
    rin "\"Oh, the coloring is important here, so if you're copying it, borrow a marker and—oh?\""

    "Rin looked down at Miyako's notes and froze."

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0415"
    fumi "\"Hm? What is it?\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0487"
    rin "\"No, uhh... you've just got some unique handwriting, Mikoyan.\""

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0323"
    miyako "\"Ahaha, it's not very good. I'm sure it looks worse next to Fumi's nice handwriting, too.\""

    "Miyako scratched her head, embarrassed."

    "The writing on her notes was less unique and more... clumsy."

    show miyako 2 lg pyjama b with dict_dissolve_25

    voice "2MI_0324"
    miyako "\"I'm not used to it yet. Just looking and doing it are pretty different.\""

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0457"
    hina "\"It's like you only just started writing. Is that because you were abroad, too?\""

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0416"
    fumi "\"You're very fluent when speaking. It's a little strange.\""

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0325"
    miyako "\"Ahaha, I have to practice.\""

    hide miyako
    with Dissolve(0.3)

    show hina 1 lg pyjama_pjm f at pos_l
    with Dissolve(0.3)

    show rin 1 lg pyjama glasses b with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2HI_0458"
    hina "\"Ah! What are you doing?\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Hina suddenly shouted. Rin had picked up her notes."

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0488"
    rin "\"I'm helping you study. Uhh, English? You're writing everything down blindly again, I see.\""

    "The pages were indeed packed. Hina's study strategy seemed to just be \"write it down and try to remember.\""

    play sound se_2s_h023
    pause 0.5

    play sound2 se_2s_h023

    show rin 1 lg pyjama glasses c with Dissolve(0.25)
    show rin:
        0.3
        "rin 1 lg pyjama glasses d" with Dissolve(0.25)

    voice "2RI_0489"
    rin "\"...Pfft!\""

    show rin 1 lg pyjama glasses d:
        pass
    with None

    "Rin suddenly burst out laughing, flipping through Hina's notes."

    show hina 1 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0459"
    hina "\"Hey, don't look at my notes and laugh!\""

    voice "2RI_0490"
    rin "\"Dahahaha!!\""

    "It {i}is{/i} pretty rude to laugh that hard."

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0491"
    rin "\"Well, you have '{i}uchuu kuukan{/i}' as 'space space'! Talk about a literal translation!\""

    "That should be \"outer space.\""

    show hina:
        "hina 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0460"
    hina "\"Shut up! Shut up! Give them back!\""

    show hina 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0492"
    rin "\"No, I wanna see more. You don't find joke books like this just anywhere!\""

    show hina:
        "hina 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0461"
    hina "\"It's not a joke book!\""

    hide hina
    hide rin
    with dict_dissolve_25

    "Hina leapt at Rin to take back her notebook, but Rin used the length of her arms to keep it from her."

    show fumi 2 lg pyjama g at pos_l
    show miyako 2 lg pyjama a at pos_r
    with dict_dissolve_25

    voice "2FU_0417"
    fumi "\"Are you going to go into the science class or the arts class, Miyako?\""

    "Their messing around was nothing out of the ordinary, so Fumi remained unbothered even with the ruckus they were making next to her."

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0326"
    miyako "\"I don't know... I suppose it will depend on my tests.\""

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0418"
    fumi "\"Your tests, huh... Do you have any plans for your future?\""

    show miyako 2 lg pyjama f with dict_dissolve_25

    voice "2MI_0327"
    miyako "\"Hmm~, no, I don't have anything like that yet. I'm sorry.\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0419"
    fumi "\"No, I think it's fine to not rush it. You can take your time deciding what you want to do.\""

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0328"
    miyako "\"Thank you. It's very exciting to think about the future though, isn't it?\""

    "That's right. Since there was no real difference between past, present, or future for her until just recently, this was a new sensation."

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "2FU_0420"
    fumi "\"I agree. Even worrying about it is kind of fun, isn't it?\""

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0329"
    miyako "\"Are you thinking about your future already, Fumi?\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0421"
    fumi "\"I've wanted to make sweets for a living ever since I was little.\""

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0330"
    miyako "\"I see. Is that arts? Or science?\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0422"
    fumi "\"...I-I'm not sure.\""

    hide fumi
    hide miyako
    with Dissolve(0.25)

    play sound se521
    pause 1.0

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0187"
    sachiko "\"Heeey, you can use the bath now~\""

    "Oh, it's Sachiko."

    show sachiko:
        "sachiko 2 sm outfit c flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0462"
    hina "\"Ah, you came in without knocking again!\""

    show sachiko 2 sm outfit c:
        alpha 1.0 xcenter 512
    with None
    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0188"
    sachiko "\"I~ did~ knock~ You guys were just making so much noise you didn't hear me~ I heard the ruckus from the hallway.\""

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0423"
    fumi "\"Sorry.\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0189"
    sachiko "\"You don't need to apologize, Foomin. It's an old building though, so don't blame me if the floor falls out under you.\""

    $ side_image = "rin 1 side pyjama glasses h"

    voice "2RI_0493"
    rin "\"Not my fault.\""

    "Rin pointed at Hina."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0463"
    hina "\"It's not my fault either.\""

    "Hina pointed at Rin."

    $ side_image = "miyako 2 side pyjama f"

    voice "2MI_0331"
    miyako "\"It isn't my fault... is it?\""

    "Miyako raised her hand timidly."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0190"
    sachiko "\"Ah~ Yeah, yeah. I'm gonna hit up the other rooms too, so you should hurry up if you want the first go.\""

    $ side_image = "fumi 2 side pyjama i"

    voice "2FU_0424"
    fumi "\"Yay~ I bought all new bath stuff for today~\""

    "Looks like Fumi was already prepared."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0191"
    sachiko "\"Come on, the rest of you get ready, too. I'll join you in a bit.\""

    "She added nonchalantly."

    $ side_image = "side/hina_rin_pyjama_sozai02_[route2].webp"

    $ voice2("hina","2HI_0464","rin","2RI_0494")
    hina_rin "\"You don't need to!\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0192"
    sachiko "\"Feh. Well, come make a report to me after you're done, then.\""

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0425"
    fumi "\"Alright.\""

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
    sachiko "\"Oh, and we're having that hot pot party tomorrow night~\""

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
