label a02_cou1_01:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg01aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm pyjama a
    show rin 1 sm casual b at pos_r2
    show fumi 1 sm pyjama a at pos_l2
    with Dissolve(0.25)

    voice "RIN_0381"
    rin "\"So I just gotta buy what's on this list?\""

    show fumi:
        "fumi 1 sm pyjama b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0329"
    fumi "\"Yes. Thank you for doing this.\""

    show fumi 1 sm pyjama b:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama h with dict_dissolve_25

    voice "HIN_0446"
    hina "\"Sorry to make you go by yourself, Rin.\""

    show rin 1 sm casual c with dict_dissolve_25

    voice "RIN_0382"
    rin "\"It's okay. I wanted to go to the bookstore anyway. It's the last weekend before exams, so you two should study.\""

    play sound se116a

    show rin:
        ShakeYes

    "Rin said, putting on her scarf."

    voice "RIN_0383"
    rin "\"Alright, see ya.\""

    show rin:
        "rin 1 sm casual c flat"
        alpha 1.0 xcenter 852 xoffset 0 yoffset 0
        easeout 0.5 alpha 0.0 xcenter 952
    pause 0.5

    hide rin with None
    show hina 1 sm pyjama c
    show fumi 1 sm pyjama a
    with dict_dissolve_25

    $ voice2("hina","HIN_0447","fumi","FUM_0330")
    hina_fumi "\"See you later.\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01aa with bg_effect_05
    pause 0.5

    show hina 1 lg pyjama a at pos_r
    show fumi 1 lg pyjama a at pos_l
    with Dissolve(0.25)

    voice "FUM_0331"
    fumi "\"Should I make us something to drink?\""

    "Fumi set down her pencil when she noticed Hina yawning."

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0448"
    hina "\"Oh, I'll do it today. What do you want, Asou?\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0332"
    fumi "\"Are you sure? I'll have a coffee, then.\""

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0449"
    hina "\"Gotcha♪ Just give me a minute.\""

    show hina:
        "hina 1 lg pyjama a flat"
        alpha 1.0 xcenter 772
        easeout 0.5 alpha 0.0 xcenter 872
    pause 0.5

    hide hina with None
    show fumi:
        "fumi 2 lg pyjama b" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 512

    "Hina jumped up and headed to the kitchen."

    show fumi 2 lg pyjama b with None
    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0450"
    hina "\"Umm, the coffee is...\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0333"
    fumi "\"Oh, it's in the second cupboard from the right. The filters are there too, so just put the beans in and then pour the hot water.\""

    $ side_image = "hina 1 side pyjama a"

    voice "HIN_0451"
    hina "\"What about milk and sugar?\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0334"
    fumi "\"I'll have an 8:2 ratio of milk today and no sugar.\""

    $ side_image = "hina 2 side pyjama b"

    voice "HIN_0452"
    hina "\"That's 8 parts coffee and 2 milk, right? The opposite of me. Why no sugar? 'Cause you're on a diet or something?\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0335"
    fumi "\"Th-That's not really what I meant.\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01aa with bg_effect_05
    pause 0.5

    show hina 1 lg pyjama c at pos_r
    show fumi 2 lg pyjama b at pos_l
    with Dissolve(0.25)

    play sound se009c

    show hina:
        ShakeYes

    voice "HIN_0453"
    hina "\"Here you are~\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0336"
    fumi "\"Thank you. It smells really good.\""

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0454"
    hina "\"I hope it tastes good, too.\""

    "Fumi blew on the liquid several times before bringing the mug to her mouth."

    show fumi:
        "fumi 2 lg pyjama h" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0337"
    fumi "\"Bitter...\""

    show fumi 2 lg pyjama h:
        xoffset 0 yoffset 0
    with None

    "Fumi grimaced slightly."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0455"
    hina "\"Huh? Does it taste strange?\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0338"
    fumi "\"No, not strange, but it's a little stronger than usual, maybe.\""

    "Hina brought her own mug to her lips."

    show hina 1 lg pyjama d with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "HIN_0456"
    hina "\"Bleh! You're right, it's bitter!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0339"
    fumi "\"Maybe you used a little too many beans.\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0457"
    hina "\"I'm sorry...\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0340"
    fumi "\"You don't need to apologize. If it's stronger, it'll help keep us awake longer.\""

    show hina 1 lg pyjama h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0458"
    hina "\"Haah... I just can't get the hang of anything I do.\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0341"
    fumi "\"That's not true. There's plenty that you're good at, Natsume.\""

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_0459"
    hina "\"Stuff I'm good at... Oh, I know. I'll rub your shoulders to make up for it! You said you get sore shoulders a lot, right?\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0342"
    fumi "\"I guess they're a little tense right now, yeah.\""

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0460"
    hina "\"Then let me help!\""

    show fumi:
        "fumi 1 lg pyjama a" with Dissolve(0.25)
        ycenter 1021
        easein 0.25 ycenter 1087
    show hina:
        "hina 2 lg pyjama a" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 578

    "Hina slipped behind Fumi and began rubbing her neck, shoulders, and shoulder blades, looking for knots."

    show fumi 1 lg pyjama a:
        ycenter 1087
    show hina 2 lg pyjama a:
        xcenter 578
    with None

    show hina 2 lg pyjama g with Dissolve(0.25)

    voice "HIN_0461"
    hina "\"Wow, you really are tense—\""

    "Hina's hands stopped. Her eyes were glued to the sight of Fumi's breasts, their size visible even over her shoulders."

    "From behind, she couldn't see Fumi's thighs as she knelt on them."

    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0343"
    fumi "\"What's wrong?\""

    show hina:
        "hina 2 lg pyjama b" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0462"
    hina "\"N-No, it's nothing.\""

    show hina 2 lg pyjama b:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0344"
    fumi "\"Umm... do you really not mind?\""

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0463"
    hina "\"Not at all. This is thanks for everything you do for me.\""

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "FUM_0345"
    fumi "\"I don't think there's anything you really need to thank me for... wah?!\""

    "The moment Hina put pressure on Fumi's shoulders, a yelp came from Fumi's lips."

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_0464"
    hina "\"You okay? Did that hurt?\""

    show fumi 1 lg pyjama i with dict_dissolve_25

    voice "FUM_0346"
    fumi "\"It didn't... hurt...\""

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0465"
    hina "\"I'll keep going, then~\""

    "Fumi's face relaxed at Hina's skillful use of strength."

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0347"
    fumi "\"You're good at this, Natsume.\""

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0466"
    hina "\"I did this all the time for my mom, so I got good at it. She's also got big—\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0348"
    fumi "\"Hm?\""

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0467"
    hina "\"Uhh, nothing~\""

    scene black with bg_effect_05
    pause 0.5

    scene bg01aa with bg_effect_05
    pause 0.5

    show hina 1 lg pyjama a at pos_r
    show fumi 2 lg pyjama i at pos_l
    with Dissolve(0.25)

    voice "FUM_0349"
    fumi "\"Thank you! My shoulders feel so light now.\""

    "Fumi rolled her shoulders with a sunny smile on her face."

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0468"
    hina "\"You're welcome.\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0350"
    fumi "\"Should I do yours now?\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0469"
    hina "\"Mine don't really tend to get stiff.\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0351"
    fumi "\"Oh, really? Is there anything else I could do, then?\""

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0470"
    hina "\"What else... Oh, I know!\""

    "Hina thought for a bit, then came up with something."

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0352"
    fumi "\"What is it?\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0471"
    hina "\"Umm... do you think I could... rest on your lap?\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0353"
    fumi "\"My lap? If that'll make you happy.\""

    show hina 1 lg pyjama c with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "HIN_0472"
    hina "\"Yay!\""

    stop music fadeout 3.0

    hide hina
    hide fumi
    with Dissolve(0.25)
    pause 0.5

    scene white with Dissolve(0.25)
    pause 0.75

    scene ev04a with Dissolve(0.5)

    play music bgm02

    voice "HIN_0473"
    hina "\"It's been so long since I did this.\""

    voice "FUM_0354"
    fumi "\"Aha, same here.\""

    voice "HIN_0474"
    hina "\"Huh? Who'd you used to do it for? Your boyfriend?\""

    voice "FUM_0355"
    fumi "\"Oh, no. My brother. And only when he was little.\""

    voice "HIN_0475"
    hina "\"Ah. I was surprised for a second.\""

    voice "FUM_0356"
    fumi "\"Is this really enough to pay you back for the massage?\""

    voice "HIN_0476"
    hina "\"Of course. It's super soft and warm and comfy♪\""

    voice "FUM_0357"
    fumi "\"Well, alright, then.\""

    voice "HIN_0477"
    hina "\"I'm not too heavy, am I? Will your legs fall asleep?\""

    voice "FUM_0358"
    fumi "\"Oh, I'm fine. You're very light.\""

    voice "HIN_0478"
    hina "\"Okay.\""

    "The two of them almost looked like mother and daughter. They'd probably complain about that comparison, though."

    scene ev04c with Dissolve(0.5)

    voice "HIN_0479"
    hina "\"...Hmm.\""

    voice "FUM_0359"
    fumi "\"...Hm?\""

    voice "HIN_0480"
    hina "\"...Ooh...\""

    voice "FUM_0360"
    fumi "\"...Umm, Natsume?\""

    voice "HIN_0481"
    hina "\"...They're pretty impressive from below, too.\""

    scene ev04d with Dissolve(0.5)

    voice "FUM_0361"
    fumi "\"...Ahh...\""

    "She realized what Hina was looking at."

    voice "HIN_0482"
    hina "\"I can barely see your face from down here.\""

    voice "FUM_0362"
    fumi "\"Umm... I... I'm sorry.\""

    voice "HIN_0483"
    hina "\"Huh? Why are you apologizing? I told you before I'm kinda jealous of your boobs.\""

    voice "FUM_0363"
    fumi "\"A-And I told you before you shouldn't be, right?\""

    voice "HIN_0484"
    hina "\"I think it's nice to have big boobs. It's feminine.\""

    voice "FUM_0364"
    fumi "\"But it limits what clothes you can wear...\""

    voice "HIN_0485"
    hina "\"You're limited by being flat like me, too. I look like a boy no matter what I wear and cute stuff looks terrible on me.\""

    voice "FUM_0365"
    fumi "\"You think so? I think you're plenty cute, Natsume.\""

    scene ev04g with Dissolve(0.5)

    voice "HIN_0486"
    hina "\"I want to be a girl like you, Asou.\""

    voice "FUM_0366"
    fumi "\"Well, then, I want to be a girl like you.\""

    voice "HIN_0487"
    hina "\"...You know, do you think we're like, complimenting each other all the time?\""

    voice "FUM_0367"
    fumi "\"Could be.\""

    voice "HIN_0488"
    hina "\"I really mean it every time I compliment you, Asou.\""

    voice "FUM_0368"
    fumi "\"So do I.\""

    voice "HIN_0489"
    hina "\"Maybe you just always want what you don't have.\""

    voice "FUM_0369"
    fumi "\"Heheh, maybe.\""

    voice "HIN_0490"
    hina "\"It might be the first time we've talked this much. I'm glad I asked to rest on your lap.\""

    voice "FUM_0370"
    fumi "\"I am, too.\""

    voice "HIN_0491"
    hina "\"Hey, Asou...? Do you think I could ask one more thing?\""

    voice "FUM_0371"
    fumi "\"Sure. What is it?\""

    voice "HIN_0492"
    hina "\"Can I touch your boobs?\""

    voice "FUM_0372"
    fumi "\"Umm, uhh...\""

    voice "HIN_0493"
    hina "\"......\""

    voice "FUM_0373"
    fumi "\"Okay, but... only a little.\""

    voice "HIN_0494"
    hina "\"Yay! Okay—\""

    "Hina gulped."

    play sound se301a

    scene ev04e with Dissolve(0.5)

    voice "HIN_0495"
    hina "\"Wha...?!\""

    "She uttered a noise of surprise as she lifted Fumi's breasts up, one in each hand."

    voice "HIN_0496"
    hina "\"Th-They're like pillows!\""

    "Hina's fingers sank into the softness."

    voice "HIN_0497"
    hina "\"I think I might sort of get where Rin and Sachiko are coming from now.\""

    voice "FUM_0374"
    fumi "\"R-Really...?\""

    voice "HIN_0498"
    hina "\"I don't approve of their being perverted... but I kinda can't stop touching these.\""

    play sound se301b

    scene ev04f with Dissolve(0.5)

    "Hina was really getting into it, squeezing Fumi's breasts, their shape changing under her fingers."

    voice "FUM_0375"
    fumi "\"Nnh... nnh!\""

    voice "HIN_0499"
    hina "\"Oh, sorry. Did that hurt? Did I squeeze too hard?\""

    voice "FUM_0376"
    fumi "\"No, umm, that's not it...\""

    voice "HIN_0500"
    hina "\"W-Waaah!!\""

    play sound se118a

    "Hina cried out and tore her hands away from Fumi's breasts."

    voice "FUM_0377"
    fumi "\"Wh-What?!\""

    voice "HIN_0501"
    hina "\"A-Asou! Th-These boobs... they have a terrible power to corrupt!\""

    voice "FUM_0378"
    fumi "\"C-Corrupt?\""

    voice "HIN_0502"
    hina "\"Yeah, you never get tired of touching them! I've gotta stop now, for my own good...!\""

    voice "FUM_0379"
    fumi "\"I-I see.\""

    scene white with bg_effect_05
    pause 0.5

    scene ev04b with bg_effect_05

    voice "HIN_0503"
    hina "\"Oh no, if you pat my head like that, I'll fall asleep...\""

    voice "FUM_0380"
    fumi "\"Eheheh, I don't mind.\""

    voice "HIN_0504"
    hina "\"But I can't... I won't be able to wake up if I fall asleep...\""

    voice "FUM_0381"
    fumi "\"Really?\""

    voice "HIN_0505"
    hina "\"I need to study, but I just want to stay like this... I'm sorry, Asou.\""

    voice "FUM_0382"
    fumi "\"No, I feel really relaxed doing this, too.\""

    stop music fadeout 2.0

    scene ev04h with Dissolve(0.5)

    "The two of them found themselves staring into each other's eyes."

    voice "HIN_0506"
    hina "\"Huh?\""

    voice "FUM_0383"
    fumi "\"What is it?\""

    play music bgm04

    voice "HIN_0507"
    hina "\"That's weird. I was really relaxed until a second ago, but my heart's pounding really hard all of a sudden.\""

    voice "FUM_0384"
    fumi "\"It's pounding?\""

    voice "HIN_0508"
    hina "\"Yeah. Touch my chest, feel it.\""

    voice "FUM_0385"
    fumi "\"Is that okay...?\""

    voice "HIN_0509"
    hina "\"Well, it won't feel as good as touching your chest...\""

    voice "FUM_0386"
    fumi "\"No, I'd like to—\""

    stop music fadeout 1.0

    play sound se521

    $ side_image = "rin 1 side casual a"

    voice "RIN_0384"
    rin "\"I'm baaack.\""

    "Fumi jerked her hands back, but Hina wasn't quick enough getting up off of her lap."

    play music bgm01

    $ side_image = "rin 1 side casual e"

    voice "RIN_0385"
    rin "\"Aaah! Sleeping on Asou's lap?!\""

    play sound se115a

    "Rin chucked her groceries in the kitchen and leapt into the living room."

    $ side_image = "rin 1 side casual j"

    voice "RIN_0386"
    rin "\"Is this what you do when I'm not home?! No fair! I demand a turn on Asou's lap!\""

    voice "FUM_0387"
    fumi "\"Umm...\""

    voice "HIN_0510"
    hina "\"Shoo! Shoo!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
