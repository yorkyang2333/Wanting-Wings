label a10_cou3_03:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play sound se521
    pause 1.5

    show fumi:
        "fumi 1 sm school_scarf c flat"
        alpha 0.0 xcenter 832
        easein 0.75 alpha 1.0 xcenter 732
        0.2
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2FU_1169"
    fumi "\"I'm ba... wah!\""

    show fumi 1 sm school_scarf j:
        alpha 1.0 xcenter 732 xoffset 0 yoffset 0
    with None

    "Fumi yelped. She hadn't expected to find anyone in the entrance."

    "It was late enough that the building was supposed to be locked. She'd had to call Sachiko and ask her to open it."

    play music bgm05 fadein 1.0

    show rin 1 sm pyjama glasses i at pos_ls with dict_dissolve_25

    voice "2RI_1555"
    rin "\"...Welcome back.\""

    "The figure stood up from the step at the entrance. It was Rin."

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "2FU_1170"
    fumi "\"Rin, you weren't waiting here the whole time, were you? It was cold out here, wasn't it?\""

    show rin 2 sm pyjama glasses e with dict_dissolve_25

    voice "2RI_1556"
    rin "\"Nah. I just wanted to see your face as soon as I could.\""

    "She was too relieved to even crack a joke."

    show fumi:
        "fumi 1 sm school_scarf k" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1171"
    fumi "\"I'm sorry. I didn't think I would be this late.\""

    show fumi 1 sm school_scarf k:
        xoffset 0 yoffset 0
    with None

    voice "2RI_1557"
    rin "\"If you'd told me when you were coming, I could have gone and met you.\""

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "2FU_1172"
    fumi "\"My phone was almost out of battery.\""

    show rin 2 sm pyjama glasses d with dict_dissolve_25

    voice "2RI_1558"
    rin "\"Ah. So, umm, err...\""

    play sound se521
    pause 1.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0857"
    sachiko "\"Oh, Foomin's back.\""

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_1555"
    hina "\"Welcome home.\""

    "The manager's room door opened, and Hina and Sachiko came out."

    "Incidentally, Miyako was sound asleep in their room."

    show rin 1 sm pyjama glasses i
    show fumi 1 sm school_scarf a
    with dict_dissolve_25

    voice "2FU_1173"
    fumi "\"I'm back.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0858"
    sachiko "\"You talked to some people from the agency today, yeah?\""

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_1556"
    hina "\"Did you decide to do the audition?\""

    show rin:
        "rin 1 sm pyjama glasses i" with Dissolve(0.25)
        ShakeJump

    voice "2RI_1559"
    rin "\"Ah, oh, y-yeah, that!\""

    show rin 1 sm pyjama glasses i:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "2FU_1174"
    fumi "\"Erm... we ended up not coming to a conclusion.\""

    show rin 1 sm pyjama glasses e with dict_dissolve_25

    voice "2RI_1560"
    rin "\"What do you mean?\""

    show fumi:
        "fumi 1 sm school_scarf h" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1175"
    fumi "\"I tried to turn them down for real this time, but I just couldn't get them to agree to it. We ended up saying we'd make our final decision another time.\""

    show fumi 1 sm school_scarf h:
        xoffset 0 yoffset 0
    with None

    "Fumi sighed, looking exhausted."

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "2RI_1561"
    rin "\"How pushy. Maybe there's something fishy going on at that agency.\""

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1557"
    hina "\"It's a super famous place, isn't it?\""

    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "2RI_1562"
    rin "\"Just because it's famous doesn't mean it's safe! I mean, they've got those nasty comedians working there!\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0859"
    sachiko "\"Did you get a business card from them?\""

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_1176"
    fumi "\"Oh, yes.\""

    show fumi 1 sm school_scarf a with Dissolve(0.25)
    show fumi:
        ShakeYes

    "Fumi took the card out of her wallet and showed it to Sachiko."

    show fumi:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0860"
    sachiko "\"Let's see... Oh, it's the president's. Did the president come to talk to you today?\""

    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "2FU_1177"
    fumi "\"I guess so.\""

    $ side_image = "hina 1 side pyjama_pjm b"

    voice "2HI_1558"
    hina "\"The president called you, too! She must really want to scout you, Asou!\""

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0861"
    sachiko "\"This is quite the campaign.\""

    "Hina and Sachiko were getting excited, while Rin's expression was only souring."

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "2RI_1563"
    rin "\"Did they tell you what they wanted you to do, exactly?\""

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "2FU_1178"
    fumi "\"Yes, they gave me a general idea.\""

    show rin 1 sm pyjama glasses g with dict_dissolve_25

    voice "2RI_1564"
    rin "\"...They're not gonna make you do dirty stuff, are they?\""

    "Rin's imagination was getting out of control."

    show fumi:
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "2FU_1179"
    fumi "\"N-No, nothing like that!\""

    show fumi 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "2RI_1565"
    rin "\"...What about swimsuits?\""

    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "2FU_1180"
    fumi "\"Oh, there did seem to be something about swimsuits.\""

    show rin:
        "rin 1 sm pyjama glasses j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1566"
    rin "\"Not! Happening!!\""

    show rin 1 sm pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0862"
    sachiko "\"Seriously?! I'd buy a Foomin swimsuit photo collection, for sure!\""

    show rin:
        ShakeJump

    voice "2RI_1567"
    rin "\"You will not!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0863"
    sachiko "\"Under the bright sun on a southern island, an innocent, busty babe wears a nice, healthy bikini that she's almost spilling out of!\""

    show rin:
        ShakeJump

    voice "2RI_1568"
    rin "\"I'm not gonna let her wear a bewitching, adult expression on a moonlit bed!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "That's not on the table right now."

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "2FU_1181"
    fumi "\"Anyway, on another note...\""

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "2RI_1569"
    rin "\"...What?\""

    "Fumi seemed hesitant to bring it up, which gave Rin a bad feeling."

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "2FU_1182"
    fumi "\"I'll have to stay at home until Valentine's, starting this weekend.\""

    show rin:
        "rin 1 sm pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1570"
    rin "\"What?!\""

    show rin 1 sm pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1559"
    hina "\"To help out at the store?\""

    show fumi 1 sm school_scarf i with dict_dissolve_25

    voice "2FU_1183"
    fumi "\"Yes. We've got a ton more customers now since we were shown on TV. I have to be there to help out, at least in the morning and at night.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0864"
    sachiko "\"I gotcha. I'll handle the paperwork, then.\""

    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "2FU_1184"
    fumi "\"Thank you.\""

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0865"
    sachiko "\"Which is all well and good, but...\""

    voice "2RI_1571"
    rin "\"......\""

    "Rin appeared to be frozen in shock."

    show fumi 1 sm school_scarf i with dict_dissolve_25

    voice "2FU_1185"
    fumi "\"I'm sorry, Rin. It's only for a week, okay?\""

    show rin:
        ShakeJump

    voice "2RI_1572"
    rin "\"Huh? Oh, I-I-I'm fine.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "She said, clearly not fine."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
