label a09_cou2_07:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Fumi and Miyako walked together, shopping bags in each hand."

    $ side_image = "miyako 1 side school_a_sei e"

    voice "2MI_0879"
    miyako "\"That's not heavy, is it? Should I carry the vegetables?\"" id a09_cou2_07_0e3c72a5

    "Miyako asked when she saw Fumi struggling."

    $ side_image = "fumi 1 side school_scarf a"

    voice "2FU_0823"
    fumi "\"It's alright. You're already carrying two. I have to take responsibility for giving in to the temptation of specials.\"" id a09_cou2_07_294e8ebb

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0880"
    if persistent.dpatch:
        miyako "\"Ahaha. We should have taken into account Rin and Hina going back to the school while we were shopping.\"" id a09_cou2_07_31d947f1
    else:
        miyako "\"Ahaha. We should have taken into account Rin and Hina going back to the campus while we were shopping.\"" id a09_cou2_07_10b42360

    "They'd run out of the store after Rin said she'd left something in the classroom, reducing their carrying power."

    $ side_image = "fumi 2 side school_scarf g"

    voice "2FU_0824"
    fumi "\"They should have gotten there by now. I hope she finds whatever it was right away.\"" id a09_cou2_07_bf5e5ff3

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_0881"
    miyako "\"What did she forget?\"" id a09_cou2_07_11389735

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0825"
    fumi "\"Considering how panicked Ogata was and Natsume's bad mood, I'm guessing the choker...\"" id a09_cou2_07_cea9dcc1

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_0882"
    miyako "\"Uh oh... It makes sense they'd run back for it, then. Think they'll be okay?\"" id a09_cou2_07_44926b9d

    $ side_image = "fumi 2 side school_scarf h"

    voice "2FU_0826"
    fumi "\"As long as Ogata apologizes like she means it...\"" id a09_cou2_07_d3c5e929

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_0883"
    miyako "\"I hope they're okay...\"" id a09_cou2_07_0be543d0

    "They exchanged a glance."

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0827"
    fumi "\"Forgetting things isn't exactly new for Ogata, of course.\"" id a09_cou2_07_efdd73d6

    "Fumi smiled wryly, and Miyako nodded."

    $ side_image = "miyako 1 side school_b_sei e"

    voice "2MI_0884"
    miyako "\"Speaking of Rin and meaning it, on the weekend...\"" id a09_cou2_07_d0146376

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
    miyako "\"Hina, you like a 1:9 ratio for your coffee, right?\"" id a09_cou2_07_08628d38

    "Miyako asked from the kitchen."

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0886"
    miyako "\"Hina?\"" id a09_cou2_07_e1986457

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
    rin "\"Yeah, the usual 'basically milk' should be good.\"" id a09_cou2_07_29f221f6

    "It was Rin, lounging around on the carpet, who answered instead of Hina."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_1018"
    rin "\"Nothing's getting through those headphones.\"" id a09_cou2_07_0b5b4444

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0887"
    miyako "\"Oh, I see.\"" id a09_cou2_07_42423932

    hide miyako with Dissolve(0.5)

    show hina 1 lg pyjama_pjm headphones p with Dissolve(0.25)

    voice "2HI_1037"
    hina "\"......\"" id a09_cou2_07_405b4484

    "Hina was facing away from the two of them, body swaying."

    hide hina with Dissolve(0.5)

    show miyako z4 1 lg pyjama_a a:
        xcenter 726
    with Dissolve(0.25)

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1019"
    rin "\"Does she really need to listen to it so loud that she can't hear someone call her, though?\"" id a09_cou2_07_616148e5

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0888"
    miyako "\"She said something about the right way to listen to rock.\"" id a09_cou2_07_e653ef72

    $ side_image = "rin 2 side pyjama glasses c"

    voice "2RI_1020"
    rin "\"Ha, when she doesn't even understand the lyrics? Her rock's dead.\"" id a09_cou2_07_0252126d

    "Rin looked exasperated."

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1021"
    rin "\"Maybe Hina's so tone-deaf because her ears went stupid after listening to so much loud music.\"" id a09_cou2_07_3e20a422

    show miyako z4 1 lg pyjama_b c with dict_dissolve_25

    voice "2MI_0889"
    miyako "\"Well, if she used speakers, it might bother people in other rooms.\"" id a09_cou2_07_38bc7a9e

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1022"
    rin "\"Her out-of-tune yelling isn't much better. It's a 120-decibel racket.\"" id a09_cou2_07_ede2399a

    "Incidentally, 120 decibels is about the volume a jet engine makes at point blank. At that level, Hina's singing would get the local government involved."

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0890"
    miyako "\"She'll get mad at you again if you keep talking like that.\"" id a09_cou2_07_d3ef5550

    "Miyako shot a glance at Hina."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_1023"
    rin "\"She can't hear me. I can hear the music coming from her headphones over here.\"" id a09_cou2_07_d3344196

    "True, the noise reached Miyako as well."

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1024"
    rin "\"...I got in some trouble with this once in the past, so I'm being careful.\"" id a09_cou2_07_45183776

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
    rin "\"She had her headphones on like now, and I said a bunch of stuff thinking she couldn't hear me, but the music stopped just in time for her to hear all of it.\"" id a09_cou2_07_fd9afbbf

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0891"
    miyako "\"Did you end up in a fight because of it?\"" id a09_cou2_07_225ce5a4

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_1026"
    rin "\"Nope, we ended up going out.\"" id a09_cou2_07_d85cfa10

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0892"
    miyako "\"Ah! That was the beginning of your romance! Hina confessed to you, but you only answered her with a kiss!\"" id a09_cou2_07_e26c49f4

    show rin:
        "rin z4 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1027"
    rin "\"Ugh! Hey, wait a second, did we tell you about that, Mikoyan?\"" id a09_cou2_07_f0a6630d

    show rin z4 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None

    "Rin was flustered when her history was brought up so frankly."

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0893"
    miyako "\"Oh, umm, Fumi told me.\"" id a09_cou2_07_75031127

    "Sure, that works."

    show rin:
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1028"
    rin "\"...Asou. It causes me pain every time I remember that... Can I just erase it from everyone's memory...\"" id a09_cou2_07_f54689ca

    show rin z4 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    "Rin picked up a pen from the table and faced Miyako. It didn't flash or anything, though."

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0894"
    miyako "\"Nope. It's because of that happy accident that you two are together now. It wouldn't do to erase it.\"" id a09_cou2_07_372975ff

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1029"
    rin "\"I guess. I wonder why I could say what I meant then, though. Even if I didn't think she could hear me.\"" id a09_cou2_07_d934227e

    show miyako z4 1 lg pyjama_b h with dict_dissolve_25

    voice "2MI_0895"
    miyako "\"If you could be a hundredth as honest as Hina, right?\"" id a09_cou2_07_9dda2aed

    "That's what she'd said then."

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_1030"
    rin "\"Mikoyan!\"" id a09_cou2_07_36c775cc

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin's face went red."

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0896"
    miyako "\"How honest are you being right now?\"" id a09_cou2_07_ba561b51

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1031"
    rin "\"...A ninety-eighth, maybe?\"" id a09_cou2_07_b191020f

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0897"
    miyako "\"...Just a slight increase, huh?\"" id a09_cou2_07_397fd59e

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_1032"
    rin "\"We still do nothing but fight.\"" id a09_cou2_07_157a756f

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0898"
    miyako "\"Were you fighting when she bit your finger, too?\"" id a09_cou2_07_d2f9cdee

    "Rin's left index finger was still bandaged. Miyako had heard that Hina bit her, but not why."

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_1033"
    rin "\"Ah... I guess that was the opposite of fighting? She bit me during, you know...\"" id a09_cou2_07_3a87afc7

    voice "2MI_0899"
    miyako "\"Is that what you two get up to?\"" id a09_cou2_07_8d1539d4

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        2.2
        "rin z4 1 lg pyjama glasses i" with Dissolve(0.25)

    voice "2RI_1034"
    rin "\"No! It was an accident! Well, this was my fault. I got carried away and put my finger in her mouth and, chomp.\"" id a09_cou2_07_8c90cdcb

    show rin z4 1 lg pyjama glasses i:
        pass
    with None
    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0900"
    miyako "\"Chomp... I wonder if your finger tasted good.\"" id a09_cou2_07_088f73fe

    "Rin hid her finger when she noticed Miyako's gaze."

    show rin:
        "rin z4 2 lg pyjama glasses f" with Dissolve(0.25)
        4.2
        "rin z4 2 lg pyjama glasses e" with Dissolve(0.25)

    voice "2RI_1035"
    rin "\"No, Hina was just really into it... Uh, this is gonna be a little graphic. Is that okay?\"" id a09_cou2_07_a2fe74e1

    show rin z4 2 lg pyjama glasses e:
        pass
    with None
    show miyako z4 1 lg pyjama_a h with dict_dissolve_25

    "Guess she wants to talk about it. Miyako smiled and nodded."

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1036"
    rin "\"Hina's really sensitive when we mess around. She says it's because I'm good at it, but... oh, I'm not bragging about my technique or anything here. I really think it's just because Hina's super sensitive.\"" id a09_cou2_07_2cde0d37

    show rin z4 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1037"
    rin "\"So that time, Hina was finishing for whatever time that day and bit her teeth down when she did, and I was into it too, so I didn't react quick enough to get away, and this is what happened.\"" id a09_cou2_07_ce52cf46

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0901"
    miyako "\"I see. What a disaster.\"" id a09_cou2_07_94925d57

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1038"
    rin "\"Yeah. It hurt like hell. I was kinda happy about it too, though.\"" id a09_cou2_07_244085b7

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0902"
    miyako "\"So you {i}are{/i} into that sort of thing...\"" id a09_cou2_07_a530f61e

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1039"
    rin "\"No! But it's like a special memory for us now. I'm sure the mark will disappear at some point, but I think I'll always remember it.\"" id a09_cou2_07_282e2a99

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    "Rin kissed the band-aid and the wound underneath it."

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1040"
    rin "\"No matter what I do, Hina always reacts like, 'no way,' and that makes me really happy. Whenever I'm touching her, it always feels really good for me, too.\"" id a09_cou2_07_73d1379b

    show rin:
        "rin z4 1 lg pyjama glasses d" with Dissolve(0.25)
        4.5
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)

    voice "2RI_1041"
    rin "\"That's why I love doing that stuff with her—wait, what am I saying? S-Stop me, why don't you!\"" id a09_cou2_07_2266df65

    show rin z4 1 lg pyjama glasses g:
        pass
    with None

    "She suddenly came back to her senses and whirled on Miyako in embarrassment."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0903"
    miyako "\"I love hearing about this stuff. It's wonderful, isn't it?\"" id a09_cou2_07_8be2a8a9

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1042"
    rin "\"Mmm~ I gotta be careful around you, 'cause you're such a good listener.\"" id a09_cou2_07_2049e756

    "I'd say you didn't need much help letting the cat out of the bag."

    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1043"
    rin "\"Anyway, Hina's the first person who's ever loved me so strongly, feeling it with her whole body.\"" id a09_cou2_07_7c90d609

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1044"
    rin "\"I love everything about her besides her tone-deafness. No, I love that, too. I feel like she's so bright that I'm scared to look directly at her sometimes.\"" id a09_cou2_07_ceabf993

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0904"
    miyako "\"You should tell her that.\"" id a09_cou2_07_46892fa0

    show rin:
        "rin z4 1 lg pyjama glasses k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1045"
    rin "\"I wouldn't be so twisted if I could just do that.\"" id a09_cou2_07_ae41402b

    show rin z4 1 lg pyjama glasses k:
        xoffset 0 yoffset 0
    with None
    hide rin with dict_dissolve_50

    "After that self-deprecating comment, she turned her back and lay down again."

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1046"
    rin "\"I can say it so easily to you, though.\"" id a09_cou2_07_181a1a2f

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0905"
    miyako "\"......\"" id a09_cou2_07_a8e1c370

    "Right when she was looking from Rin's back to Hina's..."

    show hina:
        Flatten(Composite((2423,3399),(0,0),"hina_1_150_pyjama_headphones_g.webp",(0,0),"hina_1_150_pyjama_choker.webp"))
        xcenter 512 ycenter 1235
    with dict_dissolve_10
    camera:
        function LayerShake(20,20,1.0)
    $ persistent.layer_shaken = False

    voice "2HI_1038"
    hina "\"Naaaaaaah!!\"" id a09_cou2_07_f72da550

    camera
    with None

    show rin behind hina:
        "rin z4 1 lg pyjama glasses j flat"
        alpha 0.0 xcenter 298 ycenter 859
        easein 0.15 alpha 1.0 ycenter 759
    show miyako z4 1 lg pyjama_a f with dict_dissolve_25

    voice "2RI_1047"
    rin "\"Wah!\"" id a09_cou2_07_33b445d5

    show rin z4 1 lg pyjama glasses j:
        alpha 1.0 xcenter 298 ycenter 759
    with None

    "Rin leapt up at Hina's sudden shout."

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1048"
    rin "\"Wait, not... again?\"" id a09_cou2_07_3c07a2e9

    hide hina with dict_dissolve_25

    "She was about to leap to her feet, but Hina was still swaying excitedly in her seat. Guess she was just overcome with passion at the hook of the song."

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_1049"
    rin "\"Ha... ha... ha...\"" id a09_cou2_07_639439db

    show rin:
        ShakeYes

    "Rin reached out to the tray of sweets on the table."

    show rin:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0906"
    miyako "\"Oh...\"" id a09_cou2_07_a89a3d71

    "And then suddenly..."

    show rin z4 1 lg pyjama glasses i with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2RI_1050"
    rin "\"Tyah!\"" id a09_cou2_07_1e023c23

    show rin:
        xoffset 0 yoffset 0
    with None
    play sound strike

    $ side_image = "hina 1 side pyjama_pjm headphones l"

    voice "2HI_1039"
    hina "\"Ow!\"" id a09_cou2_07_44638888

    "She threw a candy that hit the back of Hina's head."

    hide miyako with Dissolve(0.25)

    show hina z4 1 lg pyjama_pjm d:
        xcenter 726
    with Dissolve(0.25)

    voice "2HI_1040"
    hina "\"Wh-What?!\"" id a09_cou2_07_d55cc27c

    "Hina took her headphones off and spun around, surprise on her face."

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_1051"
    rin "\"Shut up!\"" id a09_cou2_07_86f9e2aa

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1041"
    hina "\"Just tell me!\"" id a09_cou2_07_f41487c0

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1052"
    rin "\"You can't hear me! You're wearing headphones!\"" id a09_cou2_07_75363aa8

    $ side_image = "miyako 2 side pyjama c"

    voice "2MI_0907"
    miyako "\"Now, now...\"" id a09_cou2_07_ab34ed43

    "There it is..."

    scene white with bg_effect_21
    pause 1.5

    scene bg08ca with bg_effect_21
    pause 0.5

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0828"
    fumi "\"She should just say it to her.\"" id a09_cou2_07_1cece3e0

    $ side_image = "miyako 2 side school_sei c"

    voice "2MI_0908"
    miyako "\"Yeah.\"" id a09_cou2_07_659b7749

    "They looked at each other and smiled wryly as they climbed the hill up to the dorm."

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0909"
    miyako "\"Kind of an unusual moon we have tonight, huh?\"" id a09_cou2_07_6b620f5c

    $ side_image = "fumi 1 side school_scarf a"

    voice "2FU_0829"
    fumi "\"You're right. It's almost scary...\"" id a09_cou2_07_a00bd716

    "A big, round moon poked out over the roof of the dorm on the hill."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou2_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
