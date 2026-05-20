label a09_cou3_02:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se521
    pause 0.5

    $ side_image = "hina 1 side school_scarf a"

    voice "2HI_1068"
    hina "\"I'm back!\""

    $ side_image = "fumi 2 side casual c"

    voice "2FU_0864"
    fumi "\"Hello. Good work on the class rep stuff.\""

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0910"
    miyako "\"Hello~\""

    "Miyako came in after Hina."

    show fumi z4 2 lg casual g:
        xcenter 298
    show hina z4 2 lg school_scarf a:
        xcenter 726
    with Dissolve(0.25)

    voice "2FU_0865"
    fumi "\"Oh, hello. Welcome back. You two came together?\""

    show hina z4 1 lg school_scarf a with dict_dissolve_25

    voice "2HI_1069"
    hina "\"Yeah, we met up on the bus.\""

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0911"
    miyako "\"Yep.\""

    show fumi:
        "fumi z4 2 lg casual i" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0866"
    fumi "\"Oh yeah? Thanks for running that errand for me, Miyako.\""

    show fumi z4 2 lg casual i:
        xoffset 0 yoffset 0
    with None

    "Fumi took the shopping bag from Miyako."

    $ side_image = "miyako 2 side school_sei c"

    voice "2MI_0912"
    miyako "\"Here's your receipt, and here's your change.\""

    show fumi z4 1 lg casual a with dict_dissolve_25

    voice "2FU_0867"
    fumi "\"Got it, got it. Thanks~\""

    hide fumi
    hide hina
    with dict_dissolve_50

    "Hina had her class rep work, and Miyako had an errand to run... At least, those were their excuses for the alone time they'd given Rin and Fumi."

    $ side_image = "hina 2 side school f"

    voice "2HI_1070"
    hina "\"You're going back home tonight, right? Sounds like it'd be real rough to run a bakery during Valentine's.\""

    "Hina said, taking off her scarf."

    "Meanwhile, Fumi was fully dressed and ready to leave at a moment's notice. She must have just been waiting for Miyako to get back before she took off."

    $ side_image = "fumi 1 side casual h"

    voice "2FU_0868"
    fumi "\"I'm sorry. I might not be able to do anything in the room on weekends for a while...\" "

    "Fumi apologized as she moved things from the bag Miyako had given her to the fridge."

    $ side_image = "hina 1 side school a"

    voice "2HI_1071"
    hina "\"No, we should apologize for leaving everything to you until now. Don't worry about us and go help out the store.\""

    $ side_image = "fumi 2 side casual c"

    voice "2FU_0869"
    fumi "\"Thanks, Natsume. Oh, there's some side dishes in the tupperware in the fridge. Go ahead and heat them up in the microwave. You'll just have to cook the rice, okay?\""

    show hina 1 lg school l at pos_r
    with Dissolve(0.25)

    show hina:
        ShakeJump

    voice "2HI_1072"
    hina "\"Whoa, you're way too well-prepared! There's basically nothing for us to do. You could have left a little more to us.\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina looked over Fumi's shoulder at the fridge full of tupperware with a half-impressed, half-exasperated face."

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_1073"
    hina "\"We're all just students living in the same dorm. It's not like we have set roles or anything. We really should probably be taking turns doing the cooking.\""

    show fumi 2 lg casual h at pos_l with dict_dissolve_25

    voice "2FU_0870"
    fumi "\"...It's okay. I do it because I like it.\""

    show hina 2 lg school d with dict_dissolve_25

    voice "2HI_1074"
    hina "\"Yeah, and we all take advantage of that. I mean, it tastes great, but it can't be entirely your responsibility.\""

    show hina 2 lg school a with dict_dissolve_25

    voice "2HI_1075"
    hina "\"Someone else can do it when you can't. That's only obvious, isn't it?\""

    show hina 1 lg school p with dict_dissolve_25

    voice "2HI_1076"
    hina "\"I can cook a little bit too, you know. It might not be as good, but you should let me help.\""

    show fumi 2 lg casual c with dict_dissolve_25

    voice "2FU_0871"
    fumi "\"Nonsense, I'm sure your cooking is wonderful. That would be great.\""

    show hina 1 lg school a with dict_dissolve_25

    voice "2HI_1077"
    hina "\"Nah, it's not gonna taste or look as good as when you do it. I can only make the kinda stuff my dad taught me when we went camping, so curry and things like that. Oh, and I can start fires, too.\""

    show fumi 1 lg casual e with dict_dissolve_25

    voice "2FU_0872"
    fumi "\"...That might be more impressive, actually.\""

    show hina 1 lg school p with dict_dissolve_25

    voice "2HI_1078"
    hina "\"Anyway, Asou, we'll handle what we can handle. Don't push yourself too hard.\""

    show fumi:
        "fumi 1 lg casual c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0873"
    fumi "\"Thank you! I'll take you up on that until Valentine's is over.\""

    show fumi 1 lg casual c:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_1079"
    hina "\"Oh, but we won't spoil Rin. I'm not letting her be picky!\""

    show fumi 1 lg casual d with dict_dissolve_25

    voice "2FU_0874"
    fumi "\"Ahaha.\""

    $ side_image = "miyako 1 side school_a g"

    voice "2MI_0913"
    miyako "\"...?\""

    "Miyako was glancing around."

    show hina 1 lg school k with dict_dissolve_25

    voice "2HI_1080"
    hina "\"What's up?\""

    $ side_image = "miyako 2 side school b"

    voice "2MI_0914"
    miyako "\"Speaking of Rin, I don't see her.\""

    show fumi 1 lg casual i
    show hina 1 lg school j
    with dict_dissolve_25

    $ voice2("hina","2HI_1081N","fumi","2FU_0875")
    hina_fumi "\"Ah...\""

    hide fumi
    hide hina
    with dict_dissolve_50

    "The two of them indicated Fumi's bed."

    show rin 3 lg light znd a with dict_dissolve_25

    voice "2RI_1117"
    rin "\"M...Mmm...\""

    "Rin was in the middle of turning over on said bed."

    $ side_image = "miyako 2 side school a"

    voice "2MI_0915"
    miyako "\"Oh, there she is.\""

    "Her bare shoulder peeked out from the blankets."

    $ side_image = "hina 1 side school j"

    voice "2HI_1082"
    hina "\"I'm sure she got tired and fell asleep, right?\""

    $ side_image = "fumi 1 side casual d"

    voice "2FU_0876"
    fumi "\"Well, umm... yes.\""

    "She'd gotten used to Hina catching on when they'd been intimate, so it didn't bother her anymore."

    show rin 3 lg light znd b with dict_dissolve_25

    voice "2RI_1118"
    rin "\"Hmmn...?\""

    "Looks like she's awake."

    show hina z4 2 lg school d:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_1083"
    hina "\"What do you mean 'hmmn'? Hurry up and get dressed.\""

    show rin 3 lg light znd d with dict_dissolve_25

    voice "2RI_1119"
    rin "\"No... I can't get out of the bed, I'm naked and you guys are all clothed. What is this, CMNF? ...Oh, I guess it'd be CFNF.\""

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_1084"
    hina "\"What? Are you half-asleep?\""

    voice "2RI_1120"
    rin "\"Clothed Males and Naked Female. But we're all girls, so it'd be CFNF, clothed females and naked female.\""

    show rin 3 lg light znd c with dict_dissolve_25

    voice "2RI_1121"
    rin "\"The argument in certain cultural circles is that this particular combination is meant to stimulate by way of humiliation and shame—\""

    $ side_image = "fumi 2 side casual h"

    voice "2FU_0877"
    fumi "\"......\""

    show rin 3 lg light znd f with dict_dissolve_25

    voice "2RI_1122"
    rin "\"Fumi! You don't need to listen so intently! We're not doing that!\""

    $ side_image = "fumi 2 side casual g"

    voice "2FU_0878"
    fumi "\"Ah...\""

    show hina z4 1 lg school f with dict_dissolve_25

    voice "2HI_1085"
    hina "\"I get it, I get it, you can change later. But at least say goodbye to Asou.\""

    show rin 3 lg light znd c with dict_dissolve_25

    voice "2RI_1123"
    rin "\"See ya later~\""

    "She waved a hand from under the futon."

    show hina:
        "hina z4 1 lg school g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1086"
    hina "\"You're so lazy!\""

    show hina z4 1 lg school g:
        xoffset 0 yoffset 0
    with None

    play sound se_2s_g002

    show rin:
        "rin 3 lg light znd f" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    "She threw Rin's tracksuit at her from where it was hanging off the railing of the bed."

    show rin 3 lg light znd f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 1 side casual d"

    voice "2FU_0879"
    fumi "\"Don't be too hard on her. She's just waking up.\""

    show hina z4 1 lg school e with dict_dissolve_25

    voice "2HI_1087"
    hina "\"There you go again. If you spoil her too much, you'll ruin her, you know.\""

    show rin 3 lg light znd b with dict_dissolve_25

    voice "2RI_1124"
    rin "\"Fumi practices positive reinforcement! Don't butt in on another family's parenting!\""

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1088"
    hina "\"Positive reinforcement doesn't work when it's not reinforcing anything!\""

    show hina z4 1 lg school f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 2 side casual h"

    voice "2FU_0880"
    fumi "\"......\""

    "Fumi was taken aback by Hina's words. They must have rung true to her after what she'd been thinking about earlier."

    if persistent.dpatch:
        show hina:
            "hina z4 1 lg school h" with Dissolve(0.25)
            ShakeTameiki

        voice "2HI_1089"
        hina "\"Haahh... You should spank her again.\""

        show hina z4 1 lg school h:
            xoffset 0 yoffset 0
        with None
        $ side_image = "fumi 2 side casual h"

        voice "2FU_0881"
        fumi "\"But she likes it when I do that.\""

        show rin 3 lg light znd f with dict_dissolve_25

        voice "2RI_1125"
        rin "\"FUMI!\""

        "Rin went red at Fumi's blithe comment."

        show hina z4 1 lg school j with dict_dissolve_25

        voice "2HI_1090"
        hina "\"This masochist is nothing but trouble.\""

        show rin 3 lg light znd g with dict_dissolve_25

        voice "2RI_1126"
        rin "\"Ungh...\""

    hide hina with Dissolve(0.25)

    show fumi z4 2 lg casual h:
        xcenter 726
    with Dissolve(0.25)

    voice "2FU_0882"
    fumi "\"Well, I should get going.\""

    "Fumi stood up with her bag, looking distracted."

    show rin 3 lg light znd f with dict_dissolve_25

    voice "2RI_1127"
    rin "\"Fumi, wait!\""

    show fumi z4 1 lg casual a with dict_dissolve_25

    voice "2FU_0883"
    fumi "\"Yes?\""

    show rin 3 lg light znd a with dict_dissolve_25

    voice "2RI_1128"
    rin "\"Mmm~\""

    "Rin stuck her lips out demandingly. After all this, she was past the point of being too embarrassed to ask for a goodbye kiss."

    show fumi z4 1 lg casual d with dict_dissolve_25

    voice "2FU_0884"
    fumi "\"Oh... umm...\""

    $ side_image = "hina 1 side school j"

    voice "2HI_1091"
    hina "\"Do you see me, Rin~? I'm right here!\""

    "Hina waved her hand. Her words were cheerful, but her face was dead serious."

    $ side_image = "miyako 1 side school_b d"

    voice "2MI_0916"
    miyako "\"I'm here too~♪\""

    "Miyako waved her hand too, excitedly. This one must be misunderstanding something."

    show rin 3 lg light znd d with dict_dissolve_25

    voice "2RI_1129"
    rin "\"Then move somewhere where you can't see.\""

    $ side_image = "hina 1 side school d"

    voice "2HI_1092"
    hina "\"Why do I have to?!\""

    scene black with Dissolve(1.5)
    pause 0.5

    $ voice2("rin","2RI_1130","fumi","2FU_0885")
    rin_fumi "\"Mm...\""

    pause 1.5

    scene bg02bg with bg_effect_05
    pause 0.5

    show rin 3 lg light znd g with Dissolve(0.25)

    voice "2RI_1131"
    rin "\"Ugh... cold.\""

    "When Fumi left, Rin curled up under the covers again."

    show hina z4 1 lg school g:
        xcenter 726
    with Dissolve(0.25)

    voice "2HI_1093"
    hina "\"I'm gonna rip the blanket off you!\""

    show rin 3 lg light znd f with dict_dissolve_25

    voice "2RI_1132"
    rin "\"Wait, wait, wait! I'm really not wearing anything!\""

    show hina:
        ShakeJump

    voice "2HI_1094"
    hina "\"Shut up! I've seen you naked in the bath!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "I'm guessing it's not her body Rin doesn't want them seeing, but the towel Fumi laid out under her."

    show rin 3 lg light znd h with dict_dissolve_25

    voice "2RI_1133"
    rin "\"Gyaaa! My virtue's in danger!\""

    show hina:
        ShakeJump

    voice "2HI_1095"
    hina "\"No it's not!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "miyako 1 side school_a d"

    voice "2MI_0917"
    miyako "\"Ooh.\""

    show hina:
        "hina z4 1 lg school d" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_1096"
    hina "\"It's not!\""

    show hina z4 1 lg school d with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou3_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
