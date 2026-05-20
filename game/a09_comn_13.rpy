label a09_comn_13:

    scene bg07bb with Dissolve(0.5)
    pause 1.5

    play music bgm05
    play sound se521
    pause 0.5

    "Beyond the door was the same roof scenery as always. Sachiko was leaned against the fence, smoking."

    show sachiko z4 2 lg outfit cigarette f:
        xcenter 298
    with dict_dissolve_25

    voice "2SA_0649"
    sachiko "\"Welcome back.\""

    "She greeted Miyako when she saw her, waving a hand her way."

    show miyako z4 1 lg school_a_sei a:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0755"
    miyako "\"Are you quitting your job?\""

    show sachiko z4 2 lg outfit cigarette e with dict_dissolve_25

    voice "2SA_0650"
    sachiko "\"Wow, news travels fast. You hear that from Rin and Hinacchi?\""

    "Miyako nodded."

    show sachiko z4 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0651"
    sachiko "\"I'll just say I'm thinking about it.\""

    show miyako z4 1 lg school_a_sei e with dict_dissolve_25

    voice "2MI_0756"
    miyako "\"What will you do after you quit? Become a painter?\""

    show sachiko z4 1 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_0652"
    sachiko "\"That might be nice. I dunno if I'm that reckless, though. I might travel some more.\""

    show miyako z4 1 lg school_a_sei a with dict_dissolve_25

    voice "2MI_0757"
    miyako "\"Where will you go?\""

    show sachiko z4 2 lg outfit cigarette e with dict_dissolve_25

    voice "2SA_0653"
    sachiko "\"Haven't decided.\""

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0758"
    miyako "\"Sounds very free. I suppose that's nice.\""

    show sachiko z4 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0654"
    sachiko "\"What's the cute bag?\""

    "Sachiko indicated the bag Miyako was carrying."

    show miyako z4 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_0759"
    miyako "\"These are for wrapping Valentine's gifts. Fumi's going to teach me how to do it. I hope you're excited.\""

    show sachiko z4 1 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_0655"
    sachiko "\"You're giving some to me?\""

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0760"
    miyako "\"Yes. And confessing my feelings.\""

    show sachiko z4 1 lg outfit cigarette g with dict_dissolve_25

    voice "2SA_0656"
    sachiko "\"Ahaha. I don't think you're supposed to say that now.\""

    show miyako z4 1 lg school_b_sei g with dict_dissolve_25

    voice "2MI_0761"
    miyako "\"Ah~\""

    show miyako z4 1 lg school_b_sei b with dict_dissolve_25

    "They laughed together."

    show miyako z4 2 lg school_sei c with dict_dissolve_25

    voice "2MI_0762"
    miyako "\"Also... I'm knitting you a scarf, but I don't think I'll finish before Valentine's—\""

    show sachiko z4 1 lg outfit cigarette i with dict_dissolve_25

    voice "2SA_0657"
    sachiko "\"Listen... I'm probably not coming back.\""

    "Sachiko cut Miyako off."

    show miyako z4 2 lg school_sei b with dict_dissolve_25

    voice "2MI_0763"
    miyako "\"...So you're really leaving?\""

    show miyako z4 1 lg school_a_sei a with dict_dissolve_25

    voice "2MI_0764"
    miyako "\"I'll come with you, then.\""

    show sachiko z4 1 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0658"
    if persistent.dpatch:
        sachiko "\"Don't you have school?\"" id a09_comn_13_b8ec91c1
    else:
        sachiko "\"Don't you have class?\""

    voice "2MI_0765"
    miyako "\"I'll drop out.\""

    show sachiko z4 1 lg outfit cigarette i with dict_dissolve_25

    voice "2SA_0659"
    sachiko "\"You can't. It's not that simple—\""

    voice "2MI_0766"
    miyako "\"But quitting your job is simple?\""

    show sachiko z4 2 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_0660"
    sachiko "\"Well, I'm an adult...\""

    show miyako z4 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_0767"
    miyako "\"A couple years after eternity is hardly a real difference. I'm—\""

    show sachiko z4 1 lg outfit cigarette j with dict_dissolve_25

    voice "2SA_0661"
    sachiko "\"You're not!\""

    "Her tone was harsh, completely changing the mood of the conversation."

    show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0662"
    sachiko "\"I just... I can't take you with me.\""

    "She tried to look away, but Miyako's voice pulled her gaze back."

    show miyako z4 2 lg school_sei e with dict_dissolve_25

    voice "2MI_0768"
    miyako "\"I don't want you to leave.\""

    show miyako z4 2 lg school_sei d with dict_dissolve_25

    voice "2MI_0769"
    miyako "\"I came here because you invited me. I'm only here because you're here. If you leave, there will be no reason for me to be here.\""

    play sound se_wind03

    show miyako z4 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_0770"
    miyako "\"I love you.\""

    "Strong wind today."

    show miyako z4 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_0771"
    miyako "\"Maybe it's just imprinting like you said. But I believe in the flash of lightning.\""

    "There was conviction in her eyes."

    "Unable to take it, Sachiko looked away."

    show miyako z4 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_0772"
    miyako "\"......\""

    "But Miyako stared right at her, waiting for Sachiko's lips to move."

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0663"
    sachiko "\"Yeah, you're right... I'm running away from those eyes.\""

    hide sachiko
    hide miyako
    with Dissolve(0.5)

    show sachiko 1 lg outfit cigarette a:
        xcenter 332
    show miyako 2 lg school_sei a:
        xcenter 692
    with dict_dissolve_25

    voice "2SA_0664"
    sachiko "\"...Thanks.\""

    "She smiled and put her hand on Miyako's head."

    voice "2MI_0773"
    miyako "\"...Ah.\""

    show sachiko 2 lg outfit cigarette e with dict_dissolve_25

    voice "2SA_0665"
    sachiko "\"I'm sorry. I knew it from the start. You wear your heart on your sleeve; it's easy enough to tell what you're feeling.\""

    show sachiko 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0666"
    sachiko "\"I knew your feelings, but I never responded to them. You never tried to hide them, but I did nothing but hide.\""

    show miyako 2 lg school_sei d with dict_dissolve_25

    voice "2MI_0774"
    miyako "\"......\""

    "Miyako shook her head."

    show sachiko 2 lg outfit cigarette e with dict_dissolve_25

    voice "2SA_0667"
    sachiko "\"You really are beautiful. It hurts my heart to look at you.\""

    "She ruffled Miyako's hair."

    show miyako 2 lg school_sei c with dict_dissolve_25

    voice "2MI_0775"
    miyako "\"Well, it's the prettiest face I can remember.\""

    show sachiko 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0668"
    sachiko "\"Heh, same here.\""

    "They both laughed."

    show sachiko 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0669"
    sachiko "\"Which is why...\""

    "She gently pulled her hand back."

    show sachiko 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0670"
    sachiko "\"I can't return your feelings.\""

    show miyako 2 lg school_sei f with dict_dissolve_25

    voice "2MI_0776"
    miyako "\"...Huh?\""

    stop music fadeout 2.0

    show sachiko 2 lg outfit cigarette e with dict_dissolve_25

    voice "2SA_0671"
    sachiko "\"There's someone I've always had feelings for.\""

    play sound se_2s_d019

    "The bag slipped from Miyako's fingers."

    show miyako 2 lg school_sei e with dict_dissolve_25

    voice "2MI_0777"
    miyako "\"Oh... I...\""

    "Miyako felt flustered for the first time at that."

    show miyako 2 lg school_sei b with dict_dissolve_25

    voice "2MI_0778"
    miyako "\"And... are they reciprocated?\""

    show sachiko 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0672"
    sachiko "\"Unfortunately, it's one-sided.\""

    show miyako 2 lg school_sei d with dict_dissolve_25

    voice "2MI_0779"
    miyako "\"Umm, is this where I should tell you 'good luck'?\""

    voice "2SA_0673"
    sachiko "\"Thanks. But it isn't ever meant to be.\""

    hide sachiko
    hide miyako
    with Dissolve(0.5)

    show sachiko z4 2 lg outfit cigarette f:
        xcenter 298
    show miyako z4 2 lg school_sei d:
        xcenter 726
    with dict_dissolve_25

    play sound se_fence

    "Sachiko said, pulling away from the fence."

    show miyako z4 2 lg school_sei b with dict_dissolve_25

    voice "2MI_0780"
    miyako "\"It's the person who invited you... isn't it?\""

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0674"
    sachiko "\"......\""

    show sachiko z4 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0675"
    sachiko "\"...Yeah.\""

    show miyako z4 2 lg school_sei c with dict_dissolve_25

    voice "2MI_0781"
    miyako "\"Then... I suppose I can't compete.\""

    "Miyako's own words were coming back to haunt her now."

    show sachiko z4 1 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0676"
    sachiko "\"I'm so—\""

    hide sachiko with dict_dissolve_50

    "Sachiko's hand moved to touch Miyako's cheek, but she pulled back at the last moment and walked past her instead."

    show miyako z4 2 lg school_sei d with dict_dissolve_25

    voice "2MI_0782"
    miyako "\"......\""

    pause 0.5

    scene white with bg_effect_25
    pause 1.5

    scene bg07bb
    show bg_obi
    with bg_effect_25
    pause 0.5

    show fumi z4 1 lg school_scarf h:
        xcenter 476
    show rin z4 1 lg school h:
        xcenter 880
    show hina z4 1 lg school d:
        xcenter 689
    with Dissolve(0.25)

    play music bgm05

    $ side_image = "sachiko 2 side outfit cigarette d"

    voice "2SA_0677"
    sachiko "\"......\""

    show fumi z4 1 lg school_scarf k with dict_dissolve_25

    voice "2FU_0678"
    fumi "\"Err, umm... we weren't eavesdropping, we just...\""

    "The girls were hiding behind the door."

    $ side_image = "sachiko 2 side outfit cigarette f"

    voice "2SA_0678"
    sachiko "\"It's fine. I knew you were there.\""

    voice "2HI_0812"
    hina "\"Awawa...\""

    voice "2RI_0820"
    rin "\"Why—\""

    $ side_image = "sachiko 1 side outfit cigarette f"

    voice "2SA_0679"
    sachiko "\"She's such a good girl, I'm worried I really might fall for her.\""

    $ side_image = "sachiko 1 side outfit cigarette b"

    voice "2SA_0680"
    sachiko "\"So I'm running away.\""

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_0821"
    rin "\"What?\""

    $ side_image = "sachiko 1 side outfit cigarette g"

    voice "2SA_0681"
    sachiko "\"Sorry, but I'll leave the rest to you~\""

    "Sachiko gave Rin a pat on the shoulder and headed down the stairs without looking back."

    show rin:
        "rin z4 1 lg school i" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0822"
    rin "\"What the hell?!\""

    show rin z4 1 lg school i with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
