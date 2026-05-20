label a09_cou2_02:

    scene bg01ah with Dissolve(0.5)
    pause 1.5

    play music bgm03

    "Saturday afternoon."

    "Hina and Rin were the only ones in the living room."

    "Fumi had just gone back home, and Miyako was nowhere to be seen, either."

    "Meaning they were alone together."

    "Hina had been restless since Fumi had left."

    "She was worked up, clearly itching to do {i}something{/i}..."

    "Since the \"heavy\" conversation, Hina had been exercising a lot of restraint."

    "The tackle-like hugs she threw at Rin when she got home had gotten softer (I think, at least)."

    "Of course, there were always consequences to holding back."

    "Especially when the feeling was particularly strong."

    "When they were finally able to be alone together, it was just about to explode..."

    show hina z4 1 lg pyjama_pjm c:
        xcenter 298
    with dict_dissolve_25

    voice "2HI_0979"
    hina "\"Riiin!\""

    show rin z4 1 lg pyjama glasses a:
        xcenter 726
    with dict_dissolve_25

    voice "2RI_0942"
    rin "\"Oh, sorry. I can't today.\""

    show hina z4 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0980"
    hina "\"Hweh...\""

    "A strange noise came from Hina."

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0981"
    hina "\"Oh, y-you can't... I-I guess that's too bad...\""

    "She backed away unsteadily."

    show rin z4 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0943"
    rin "\"You wanted to?\""

    show hina:
        "hina z4 2 lg pyjama_pjm b" with Dissolve(0.25)
        6.0
        "hina z4 2 lg pyjama_pjm h" with Dissolve(0.25)

    voice "2HI_0982"
    hina "\"N-Not really~ I just thought maybe if you wanted to, I'd say okay. ...So I brushed my teeth and showered and changed my underwear...\""

    show hina z4 2 lg pyjama_pjm h:
        pass
    with None
    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0944"
    rin "\"...Rarin' to go, eh?\""

    show hina z4 2 lg pyjama_pjm b with dict_dissolve_25

    voice "2HI_0983"
    hina "\"O-Of course not.\""

    "She looked away. I'm guessing her ears were red, too."

    hide rin
    hide hina
    with Dissolve(0.5)

    show rin 1 lg pyjama glasses k:
        xcenter 662
    show hina 2 lg pyjama_pjm f:
        xcenter 362
    with dict_dissolve_50

    voice "2HI_0984"
    hina "\"...Ah.\""

    "Rin put her arms around Hina's head."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0945"
    rin "\"Should we do it, then? I can give, at least...\""

    show hina 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0985"
    hina "\"...Nah.\""

    "After thinking a bit, Hina shook her head."

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0946"
    rin "\"Are you sure? Weren't you super disappointed?\""

    voice "2HI_0986"
    hina "\"Honestly... I was. But it's okay.\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0947"
    rin "\"Oh yeah...?\""

    "Contrary to her words, disappointment was clear on Hina's face."

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0948"
    rin "\"Hey, Hina?\""

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0987"
    hina "\"Yeah?\""

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0949"
    rin "\"Wanna go on a date tomorrow?\""

    show hina 1 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0988"
    hina "\"Really?! Where? Where do you wanna go?!\""

    "In a flash, with that one word, the sparkle returned to Hina's eyes."

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0950"
    rin "\"Just got the idea now, so I don't have anything planned yet. Is there somewhere you want to go?\""

    show hina 1 lg pyjama_pjm q with dict_dissolve_25

    voice "2HI_0989"
    hina "\"I'll go anywhere if you take me, Rin!\""

    "I can see a wagging tail. She's like a dog excited to go on a walk."

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0951"
    rin "\"I know I was the one who invited you, but is it really that exciting?\""

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0990"
    hina "\"Well, this will be our first real date!\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0952"
    rin "\"W-Will it?\""

    show hina 2 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0991"
    hina "\"Since whenever we get time alone, all you wanna do is dirty stuff. Though I guess it was me who wanted to this time.\""

    show rin 2 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0953"
    rin "\"R-Right.\""

    "Dug her own grave there."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared == 1:
        jump a09_comn_05
    else:
        jump a09_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
