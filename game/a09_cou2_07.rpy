label a09_cou2_07:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Fumi and Miyako walked together, shopping bags in each hand."

    $ side_image = "miyako 1 side school_a_sei e"

    voice "2MI_0879"
    miyako "\"That's not heavy, is it? Should I carry the vegetables?\""

    "Miyako asked when she saw Fumi struggling."

    $ side_image = "fumi 1 side school_scarf a"

    voice "2FU_0823"
    fumi "\"It's alright. You're already carrying two. I have to take responsibility for giving in to the temptation of specials.\""

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0880"
    if persistent.dpatch:
        miyako "\"Ahaha. We should have taken into account Rin and Hina going back to the school while we were shopping.\"" id a09_cou2_07_31d947f1
    else:
        miyako "\"Ahaha. We should have taken into account Rin and Hina going back to the campus while we were shopping.\""

    "They'd run out of the store after Rin said she'd left something in the classroom, reducing their carrying power."

    $ side_image = "fumi 2 side school_scarf g"

    voice "2FU_0824"
    fumi "\"They should have gotten there by now. I hope she finds whatever it was right away.\""

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_0881"
    miyako "\"What did she forget?\""

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0825"
    fumi "\"Considering how panicked Ogata was and Natsume's bad mood, I'm guessing the choker...\""

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_0882"
    miyako "\"Uh oh... It makes sense they'd run back for it, then. Think they'll be okay?\""

    $ side_image = "fumi 2 side school_scarf h"

    voice "2FU_0826"
    fumi "\"As long as Ogata apologizes like she means it...\""

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_0883"
    miyako "\"I hope they're okay...\""

    "They exchanged a glance."

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0827"
    fumi "\"Forgetting things isn't exactly new for Ogata, of course.\""

    "Fumi smiled wryly, and Miyako nodded."

    $ side_image = "miyako 1 side school_b_sei e"

    voice "2MI_0884"
    miyako "\"Speaking of Rin and meaning it, on the weekend...\""

    stop music fadeout 1.0

    pause 0.5

    scene white with bg_effect_21
    pause 2.0

    scene bg01ah
    show bg_ef_01 zorder 2
    with bg_effect_21
    pause 1.0

    play music bgm01

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0885"
    miyako "\"Hina, you like a 1:9 ratio for your coffee, right?\""

    "Miyako asked from the kitchen."

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0886"
    miyako "\"Hina?\""

    show miyako:
        "miyako z4 2 lg pyjama a flat"
        alpha 0.0 xcenter 826
        easein 0.75 alpha 1.0 xcenter 726

    "There was no answer, so she poked her head into the living room, holding some mugs."

    show miyako z4 2 lg pyjama a:
        alpha 1.0 xcenter 726
    with None
    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_1017"
    rin "\"Yeah, the usual 'basically milk' should be good.\""

    "It was Rin, lounging around on the carpet, who answered instead of Hina."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_1018"
    rin "\"Nothing's getting through those headphones.\""

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0887"
    miyako "\"Oh, I see.\""

    hide miyako with Dissolve(0.5)

    show hina 1 lg pyjama_pjm headphones p with Dissolve(0.25)

    voice "2HI_1037"
    hina "\"......\""

    "Hina was facing away from the two of them, body swaying."

    hide hina with Dissolve(0.5)

    show miyako z4 1 lg pyjama_a a:
        xcenter 726
    with Dissolve(0.25)

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1019"
    rin "\"Does she really need to listen to it so loud that she can't hear someone call her, though?\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0888"
    miyako "\"She said something about the right way to listen to rock.\""

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1020"
    rin "\"Ha, when she doesn't even understand the lyrics? Her rock's dead.\""

    "Rin looked exasperated."

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1021"
    rin "\"Maybe Hina's so tone-deaf because her ears went stupid after listening to so much loud music.\""

    show miyako z4 1 lg pyjama_b c with dict_dissolve_25

    voice "2MI_0889"
    miyako "\"Well, if she used speakers, it might bother people in other rooms.\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1022"
    rin "\"Her out-of-tune yelling isn't much better. It's a 120-decibel racket.\""

    "Incidentally, 120 decibels is about the volume a jet engine makes at point blank. At that level, Hina's singing would get the local government involved."

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0890"
    miyako "\"She'll get mad at you again if you keep talking like that.\""

    "Miyako shot a glance at Hina."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_1023"
    rin "\"She can't hear me. I can hear the music coming from her headphones over here.\""

    "True, the noise reached Miyako as well."

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1024"
    rin "\"...I got in some trouble with this once in the past, so I'm being careful.\""

    show rin:
        "rin z4 1 lg pyjama glasses b flat"
        alpha 0.0 xcenter 298 ycenter 859
        easein 0.75 alpha 1.0 ycenter 759

    "Rin said, sitting up."

    show rin z4 1 lg pyjama glasses b:
        alpha 1.0 xcenter 298 ycenter 759
    with None
    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_1025"
    rin "\"She had her headphones on like now, and I said a bunch of stuff thinking she couldn't hear me, but the music stopped just in time for her to hear all of it.\""

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0891"
    miyako "\"Did you end up in a fight because of it?\""

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_1026"
    rin "\"Nope, we ended up going out.\""

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0892"
    miyako "\"Ah! That was the beginning of your romance! Hina confessed to you, but you only answered her with a kiss!\""

    show rin:
        "rin z4 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1027"
    rin "\"Ugh! Hey, wait a second, did we tell you about that, Mikoyan?\""

    show rin z4 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None

    "Rin was flustered when her history was brought up so frankly."

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0893"
    miyako "\"Oh, umm, Fumi told me.\""

    "Sure, that works."

    show rin:
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1028"
    rin "\"...Asou. It causes me pain every time I remember that... Can I just erase it from everyone's memory...\""

    show rin z4 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    "Rin picked up a pen from the table and faced Miyako. It didn't flash or anything, though."

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0894"
    miyako "\"Nope. It's because of that happy accident that you two are together now. It wouldn't do to erase it.\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1029"
    rin "\"I guess. I wonder why I could say what I meant then, though. Even if I didn't think she could hear me.\""

    show miyako z4 1 lg pyjama_b h with dict_dissolve_25

    voice "2MI_0895"
    miyako "\"If you could be a hundredth as honest as Hina, right?\""

    "That's what she'd said then."

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_1030"
    rin "\"Mikoyan!\""

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin's face went red."

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0896"
    miyako "\"How honest are you being right now?\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1031"
    rin "\"...A ninety-eighth, maybe?\""

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0897"
    miyako "\"...Just a slight increase, huh?\""

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_1032"
    rin "\"We still do nothing but fight.\""

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0898"
    miyako "\"Were you fighting when she bit your finger, too?\""

    "Rin's left index finger was still bandaged. Miyako had heard that Hina bit her, but not why."

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_1033"
    rin "\"Ah... I guess that was the opposite of fighting? She bit me during, you know...\""

    voice "2MI_0899"
    miyako "\"Is that what you two get up to?\""

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        2.2
        "rin z4 1 lg pyjama glasses i" with Dissolve(0.25)

    voice "2RI_1034"
    rin "\"No! It was an accident! Well, this was my fault. I got carried away and put my finger in her mouth and, chomp.\""

    show rin z4 1 lg pyjama glasses i:
        pass
    with None
    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0900"
    miyako "\"Chomp... I wonder if your finger tasted good.\""

    "Rin hid her finger when she noticed Miyako's gaze."

    show rin:
        "rin z4 2 lg pyjama glasses f" with Dissolve(0.25)
        4.2
        "rin z4 2 lg pyjama glasses e" with Dissolve(0.25)

    voice "2RI_1035"
    rin "\"No, Hina was just really into it... Uh, this is gonna be a little graphic. Is that okay?\""

    show rin z4 2 lg pyjama glasses e:
        pass
    with None
    show miyako z4 1 lg pyjama_a h with dict_dissolve_25

    "Guess she wants to talk about it. Miyako smiled and nodded."

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1036"
    rin "\"Hina's really sensitive when we mess around. She says it's because I'm good at it, but... oh, I'm not bragging about my technique or anything here. I really think it's just because Hina's super sensitive.\""

    show rin z4 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1037"
    rin "\"So that time, Hina was finishing for whatever time that day and bit her teeth down when she did, and I was into it too, so I didn't react quick enough to get away, and this is what happened.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0901"
    miyako "\"I see. What a disaster.\""

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1038"
    rin "\"Yeah. It hurt like hell. I was kinda happy about it too, though.\""

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0902"
    miyako "\"So you {i}are{/i} into that sort of thing...\""

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1039"
    rin "\"No! But it's like a special memory for us now. I'm sure the mark will disappear at some point, but I think I'll always remember it.\""

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    "Rin kissed the band-aid and the wound underneath it."

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1040"
    rin "\"No matter what I do, Hina always reacts like, 'no way,' and that makes me really happy. Whenever I'm touching her, it always feels really good for me, too.\""

    show rin:
        "rin z4 1 lg pyjama glasses d" with Dissolve(0.25)
        4.5
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)

    voice "2RI_1041"
    rin "\"That's why I love doing that stuff with her—wait, what am I saying? S-Stop me, why don't you!\""

    show rin z4 1 lg pyjama glasses g:
        pass
    with None

    "She suddenly came back to her senses and whirled on Miyako in embarrassment."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0903"
    miyako "\"I love hearing about this stuff. It's wonderful, isn't it?\""

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1042"
    rin "\"Mmm~ I gotta be careful around you, 'cause you're such a good listener.\""

    "I'd say you didn't need much help letting the cat out of the bag."

    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1043"
    rin "\"Anyway, Hina's the first person who's ever loved me so strongly, feeling it with her whole body.\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1044"
    rin "\"I love everything about her besides her tone-deafness. No, I love that, too. I feel like she's so bright that I'm scared to look directly at her sometimes.\""

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0904"
    miyako "\"You should tell her that.\""

    show rin:
        "rin z4 1 lg pyjama glasses k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1045"
    rin "\"I wouldn't be so twisted if I could just do that.\""

    show rin z4 1 lg pyjama glasses k:
        xoffset 0 yoffset 0
    with None
    hide rin with dict_dissolve_50

    "After that self-deprecating comment, she turned her back and lay down again."

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1046"
    rin "\"I can say it so easily to you, though.\""

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0905"
    miyako "\"......\""

    "Right when she was looking from Rin's back to Hina's..."

    show hina:
        Flatten(Composite((2423,3399),(0,0),"hina_1_150_pyjama_headphones_g.webp",(0,0),"hina_1_150_pyjama_choker.webp"))
        xcenter 512 ycenter 1235
    with dict_dissolve_10
    camera:
        function LayerShake(20,20,1.0)
    $ persistent.layer_shaken = False

    voice "2HI_1038"
    hina "\"Naaaaaaah!!\""

    camera
    with None

    show rin behind hina:
        "rin z4 1 lg pyjama glasses j flat"
        alpha 0.0 xcenter 298 ycenter 859
        easein 0.15 alpha 1.0 ycenter 759
    show miyako z4 1 lg pyjama_a f with dict_dissolve_25

    voice "2RI_1047"
    rin "\"Wah!\""

    show rin z4 1 lg pyjama glasses j:
        alpha 1.0 xcenter 298 ycenter 759
    with None

    "Rin leapt up at Hina's sudden shout."

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1048"
    rin "\"Wait, not... again?\""

    hide hina with dict_dissolve_25

    "She was about to leap to her feet, but Hina was still swaying excitedly in her seat. Guess she was just overcome with passion at the hook of the song."

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_1049"
    rin "\"Ha... ha... ha...\""

    show rin:
        ShakeYes

    "Rin reached out to the tray of sweets on the table."

    show rin:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0906"
    miyako "\"Oh...\""

    "And then suddenly..."

    show rin z4 1 lg pyjama glasses i with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2RI_1050"
    rin "\"Tyah!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    play sound strike

    $ side_image = "hina 1 side pyjama_pjm headphones l"

    voice "2HI_1039"
    hina "\"Ow!\""

    "She threw a candy that hit the back of Hina's head."

    hide miyako with Dissolve(0.25)

    show hina z4 1 lg pyjama_pjm d:
        xcenter 726
    with Dissolve(0.25)

    voice "2HI_1040"
    hina "\"Wh-What?!\""

    "Hina took her headphones off and spun around, surprise on her face."

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_1051"
    rin "\"Shut up!\""

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1041"
    hina "\"Just tell me!\""

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1052"
    rin "\"You can't hear me! You're wearing headphones!\""

    $ side_image = "miyako 2 side pyjama c"

    voice "2MI_0907"
    miyako "\"Now, now...\""

    "There it is..."

    scene white with bg_effect_21
    pause 1.5

    scene bg08ca with bg_effect_21
    pause 0.5

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0828"
    fumi "\"She should just say it to her.\""

    $ side_image = "miyako 2 side school_sei c"

    voice "2MI_0908"
    miyako "\"Yeah.\""

    "They looked at each other and smiled wryly as they climbed the hill up to the dorm."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0909"
    miyako "\"Kind of an unusual moon we have tonight, huh?\""

    $ side_image = "fumi 1 side school_scarf a"

    voice "2FU_0829"
    fumi "\"You're right. It's almost scary...\""

    "A big, round moon poked out over the roof of the dorm on the hill."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou2_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
