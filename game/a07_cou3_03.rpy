label a07_cou3_03:

    scene bg02ag with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se521
    pause 0.5

    $ side_image = "rin 1 side casual d"

    voice "2RI_0332"
    rin "\"We're back!\""

    "The door swung open and Rin strolled in."

    $ side_image = "fumi 1 side casual d"

    voice "2FU_0280"
    fumi "\"Not that anyone's waiting for us.\""

    play sound se_doorcl

    "Fumi followed, quietly closing the door behind her."

    show rin z4 1 lg casual d:
        xcenter 668
    with dict_dissolve_25

    voice "2RI_0333"
    rin "\"Yep. Which means we're all alone~♪\""

    "She looked like she could pirouette on the spot."

    show fumi z4 2 lg casual i:
        xcenter 356
    with dict_dissolve_25

    voice "2FU_0281"
    fumi "\"We'll have to thank Natsume for giving us this opportunity.\""

    show rin z4 1 lg casual f with dict_dissolve_25

    voice "2RI_0334"
    rin "\"Let's give her some New Year's money later.\""

    show fumi z4 1 lg casual h with dict_dissolve_25

    voice "2FU_0282"
    fumi "\"There you go, treating her like a kid again. You could just tell her thank you.\""

    show rin z4 1 lg casual d with dict_dissolve_25

    voice "2RI_0335"
    rin "\"We've been having sleepovers since Christmas, then Takaoka moved in, so we haven't been alone together in so long~\""

    "Fumi sighed and smiled awkwardly."

    show fumi:
        "fumi z4 1 lg casual d" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_0283"
    fumi "\"I wonder if Takaoka's figured it out yet.\""

    show fumi z4 1 lg casual d:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0336"
    rin "\"You think? I think we've been pretty discreet since Christmas.\""

    "Huh?"

    show fumi z4 2 lg casual d with dict_dissolve_25

    voice "2FU_0284"
    fumi "\"Huh?\""

    "...Right?"

    show rin:
        "rin z4 1 lg casual c" with Dissolve(0.25)
        ShakeNo

    voice "2RI_0337B"
    rin "\"Fuuumiii.\""

    show rin z4 1 lg casual c:
        xoffset 0 yoffset 0
    with None

    "The restrained (so she said) Rin whined and went to put her arms around Fumi."

    play sound se_lime

    show fumi z4 2 lg casual g with dict_dissolve_25

    voice "2FU_0285"
    fumi "\"Oh, wait a second. I have a LIME message...\""

    show rin:
        "rin z4 1 lg casual i" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0338"
    rin "\"Pgh.\""

    show rin z4 1 lg casual i:
        xoffset 0 yoffset 0
    with None

    "Fumi put her finger on Rin's lips and looked down at her phone."

    show fumi z4 2 lg casual a with dict_dissolve_25

    voice "2FU_0286"
    fumi "\"Hm? It's from Rei?\""

    show rin z4 1 lg casual h with dict_dissolve_25

    voice "2RI_0339"
    rin "\"Rei... Oh, your brother? What'd he say?\""

    show fumi z4 2 lg casual h with dict_dissolve_25

    voice "2FU_0287"
    fumi "\"He wants to know if I've seen his pass case, since he can't find it. He has a habit of misplacing things...\""

    "Someone else in this room has that habit, too."

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0340"
    rin "\"You don't want to lose your train pass...\""

    show rin:
        ShakeYes

    "Rin dug in her pocket and took out her own case... probably just to check if she still had it."

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi z4 2 lg casual a" with Dissolve(0.25)
        2.5
        "fumi z4 1 lg casual e" with Dissolve(0.25)

    voice "2FU_0288"
    fumi "\"No, you don't. You should be careful, t—ah.\""

    show fumi z4 1 lg casual e:
        pass
    with None

    "Fumi did a double take when she saw the pass case in Rin's hand."

    show fumi z4 2 lg casual g with dict_dissolve_25

    voice "2FU_0289"
    fumi "\"I'm sorry, Rin. Can you check your other pocket?\""

    show rin:
        "rin z4 1 lg casual b" with Dissolve(0.25)
        1.5
        ShakeYes
        1.0
        "rin z4 1 lg casual e" with Dissolve(0.25)

    voice "2RI_0341"
    rin "\"Hm? There's nothing in—huh?\""

    show rin z4 1 lg casual e:
        xoffset 0 yoffset 0
    with None

    "A pass case appeared from this pocket as well."

    show rin:
        "rin z4 1 lg casual j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_0342"
    rin "\"It doubled?! Tap my pocket and I have two pass cases? Is it a magic pocket?!\""

    show rin z4 1 lg casual j:
        xoffset 0 yoffset 0
    with None

    "Rin tapped her pocket, but no more pass cases appeared, of course."

    show fumi z4 2 lg casual b with dict_dissolve_25

    voice "2FU_0290"
    fumi "\"No. Look closer. The first one you pulled out is Rei's, I think.\""

    "She opened up the case and looked at the train pass. The name on it was \"Rei Asou.\" Fumi's brother."

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0343B"
    rin "\"You're right! Wait, what? The case is mine, though.\""

    show fumi z4 1 lg casual a with dict_dissolve_25

    voice "2FU_0291"
    fumi "\"It's a little bit different. Look at the stitching here.\""

    show rin z4 1 lg casual a with dict_dissolve_25

    voice "2RI_0344"
    rin "\"Oh, yeah. You could tell from one look?\""

    show fumi z4 1 lg casual b with dict_dissolve_25

    voice "2FU_0292"
    fumi "\"Rei's pass case was a birthday present from me. And I see yours every morning.\""

    "Because of the Rin Shift, Fumi knew Rin's belongings better than Rin did."

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0345"
    rin "\"Ah~ It was probably on the shoe cupboard, and it looked exactly like mine, so I took it without thinking. I feel really bad about that.\""

    "The design of the case was another factor, since you couldn't see the train pass without opening it."

    show fumi z4 1 lg casual h with dict_dissolve_25

    voice "2FU_0293"
    fumi "\"No, it's Rei's fault for leaving it in a place like that.\""

    show rin z4 1 lg casual g with dict_dissolve_25

    voice "2RI_0346"
    rin "\"Nah, I shouldn't have put it in my pocket without checking. And I never noticed after that either.\""

    show fumi z4 2 lg casual b with dict_dissolve_25

    voice "2FU_0294"
    fumi "\"It's alright. I'll probably go home again before the new semester starts, so I can give it to him then.\""

    "Fumi sent a reply to her brother."

    show rin z4 2 lg casual d with dict_dissolve_25

    voice "2RI_0347"
    rin "\"Sorry. I'll put some money on it before you give it back.\""

    "She looked like she felt really bad about it."

    show fumi z4 2 lg casual a with dict_dissolve_25

    voice "2FU_0295"
    fumi "\"......\""

    "Fumi finished typing and closed the app, staring at Rin's face."

    show rin z4 2 lg casual g with dict_dissolve_25

    voice "2RI_0348"
    rin "\"Hm? What is it?\""

    show fumi z4 1 lg casual h with dict_dissolve_25

    voice "2FU_0296"
    fumi "\"Should we not have invited you over?\""

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0349"
    rin "\"What?! Where'd that come from?\""

    show fumi z4 1 lg casual k with dict_dissolve_25

    voice "2FU_0297"
    fumi "\"You were really nervous, weren't you? At my house and at Natsume's.\""

    show rin:
        "rin z4 1 lg casual g" with Dissolve(0.25)
        ShakeSide
        3.0
        "rin z4 1 lg casual i" with Dissolve(0.25)

    voice "2RI_0350"
    rin "\"Th-That's not... You could tell?\""

    show rin z4 1 lg casual i:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg casual h with dict_dissolve_25

    voice "2FU_0298"
    fumi "\"Yes. Taking the wrong pass case was probably—\""

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0351"
    rin "\"No, I'm always like that.\""

    voice "2FU_0299"
    fumi "\".........\""

    show rin z4 2 lg casual d with dict_dissolve_25

    voice "2RI_0352"
    rin "\"......\""

    show fumi z4 2 lg casual h with dict_dissolve_25

    voice "2FU_0300"
    fumi "\"You were very polite at both of our houses.\""

    show rin z4 2 lg casual a with dict_dissolve_25

    voice "2RI_0353"
    rin "\"Uh, yeah.\""

    "The subject changed."

    voice "2FU_0301"
    fumi "\"You spoke a lot to our parents, too.\""

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0354"
    rin "\"Ah~ I'm good at acting. And Hina was there, too.\""

    show fumi z4 2 lg casual a with dict_dissolve_25

    voice "2FU_0302"
    fumi "\"But you were really uncomfortable, right?\""

    show rin z4 2 lg casual d with dict_dissolve_25

    voice "2RI_0355"
    rin "\"...Yeah, I guess.\""

    "Even through Rin's façade, it had been obvious to her."

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0356"
    rin "\"Oh! But it's not because your family made me uncomfortable or anything.\""

    show fumi z4 1 lg casual h with dict_dissolve_25

    voice "2FU_0295"
    fumi "\"......\""

    "If Rin had been her usual careless self, Fumi wouldn't have worried."

    "But at both Natsume's and her own house, she had had perfect manners."

    "Knowing how she was normally, this was enough for Fumi to be able to tell that Rin had been nervous the whole time."

    show fumi z4 1 lg casual k with dict_dissolve_25

    voice "2FU_0304"
    fumi "\"Sorr—\""

    show rin z4 1 lg casual a with dict_dissolve_25

    voice "2RI_0357"
    rin "\"It was really fun. I was happy to be invited.\""

    "She didn't let her finish the apology."

    show rin z4 1 lg casual k with dict_dissolve_25

    voice "2RI_0358"
    rin "\"It was my first time spending New Year's with people. And I wouldn't have been able to have that experience if you and Hina hadn't dragged me with you.\""

    show rin z4 1 lg casual c with dict_dissolve_25

    voice "2RI_0359"
    rin "\"I mean, everybody knows I'm not exactly the sociable type.\""

    show fumi:
        "fumi z4 2 lg casual h" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0295"
    fumi "\"......\""

    show fumi z4 2 lg casual h:
        xoffset 0 yoffset 0
    with None

    "Everybody, eh?"

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0360"
    rin "\"So I use more energy than others when I interact with people for the first time. But it's not like I always hate to do it.\""

    show fumi z4 1 lg casual i with dict_dissolve_25

    voice "2FU_0306"
    fumi "\"I see...\""

    "Fumi smiled in relief."

    show rin z4 1 lg casual d with dict_dissolve_25

    voice "2RI_0361"
    rin "\"And, hey! I got to meet the mother- and father-in-law!\""

    "Aww, there she goes again."

    show fumi z4 2 lg casual b with dict_dissolve_25

    voice "2FU_0307"
    fumi "\"Are you going to introduce yourself to them properly someday?\""

    show rin:
        "rin z4 1 lg casual g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0362"
    rin "\"U-Umm...\""

    show rin z4 1 lg casual g:
        xoffset 0 yoffset 0
    with None

    "See? She should have known she'd get countered."

    show fumi z4 2 lg casual c with dict_dissolve_25

    voice "2FU_0308"
    fumi "\"I hope you will... one day.\""

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0363"
    rin "\"Ugh... uh... yeah.\""

    "Release."

    show fumi z4 2 lg casual i with dict_dissolve_25

    voice "2FU_0309"
    fumi "\"Heheh...\""

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0364"
    rin "\"Huh...?\""

    stop music fadeout 1.0
    hide rin
    hide fumi
    with Dissolve(0.5)

    show rin 1 lg casual e:
        xcenter 682
    show fumi 2 lg casual b:
        xcenter 342
    with Dissolve(0.5)

    "While Rin was busy being flustered, Fumi brought her face right up to hers."

    show fumi 2 lg casual c with dict_dissolve_25

    voice "2FU_0310"
    fumi "\"...Shall we?\""

    "Before she could even recover, Fumi was already making her next move."

    "She slowly lowered Rin to the bed."

    scene black with Dissolve(0.5)
    pause 2.0

    if persistent.dpatch:
        jump rp_c_scene05
    else:
        stop music fadeout 1.0
        stop sound fadeout 1.0
        pause 1.5
        "........."
        "......"
        window hide
        pause 2.5
        window auto

label rp_c_scene05_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    $ renpy.end_replay()

    jump a07_comn_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
