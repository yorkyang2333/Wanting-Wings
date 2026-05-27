label a10_cou1_05:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    show rin z4 1 lg school k with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "2RI_1251"
    rin "\"I'm impressed at that quick decision-making. From you and your dad.\"" id a10_cou1_05_d71d7db3

    show rin:
        xoffset 0 yoffset 0
    with None

    "Hina and Rin had arrived home first, and Rin had said that while changing clothes."

    $ side_image = "hina 2 side school d"

    voice "2HI_1221"
    hina "\"I know how busy they are.\"" id a10_cou1_05_1faffede

    "Hina was putting the food they'd bought in the fridge before she changed."

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_1252"
    rin "\"I was kinda worried you two were fighting.\"" id a10_cou1_05_1d3b78a4

    $ side_image = "hina 1 side school e"

    voice "2HI_1222"
    hina "\"We're not. We love each other.\"" id a10_cou1_05_7a34675c

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1253"
    rin "\"R-Right. You can say it with no hesitation, huh?\"" id a10_cou1_05_c03ad7c3

    "Once again, Rin was awed by Hina's emotional fortitude."

    hide rin with Dissolve(0.25)

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1223"
    hina "\"I want to be with her for as much of our limited time as I can.\"" id a10_cou1_05_5b80128f

    $ side_image = "rin 1 side school e"

    voice "2RI_1254"
    rin "\"Hm? Limited time? What do you mean? You're not gonna be together forever?\"" id a10_cou1_05_71cb84de

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1224"
    hina "\"...Fumi's gonna have to get married someday. Then we won't be able to be together anymore.\"" id a10_cou1_05_d1949c8f

    $ side_image = "rin 1 side school j"

    voice "2RI_1255"
    rin "\"Hwha?\"" id a10_cou1_05_f74e3586

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1225"
    hina "\"So we're only dating until we graduate.\"" id a10_cou1_05_271a608f

    $ side_image = "rin 1 side school g"

    voice "2RI_1256"
    rin "\"Did Asou say that?\"" id a10_cou1_05_82399bd6

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_1226"
    hina "\"No...\"" id a10_cou1_05_cc5d8a13

    $ side_image = "rin 1 side school i"

    voice "2RI_1257"
    rin "\"Then did her parents say something to you?\"" id a10_cou1_05_d764f05f

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1227"
    hina "\"No...\"" id a10_cou1_05_2ab83157

    $ side_image = "rin 1 side school i"

    voice "2RI_1258"
    rin "\"So, are you okay with that?\"" id a10_cou1_05_5bf2d6da

    voice "2HI_1228"
    hina "\"I...\"" id a10_cou1_05_65310624

    pause 0.5

    scene white with bg_effect_27_750
    pause 1.0

    scene bg05ba with bg_effect_27_750
    pause 0.5

    "Fumi was wiping the snow off the shoes by the door. Hers, Hina's, and Rin's."

    show fumi z4 2 lg school_scarf h with Dissolve(0.5)

    play sound se521
    pause 2.0

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0994"
    miyako "\"I'm back, Fumi.\"" id a10_cou1_05_d7cafc78

    show fumi z4 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_0972"
    fumi "\"Oh, hello, Miyako.\"" id a10_cou1_05_58291fe4

    "Miyako had also returned. She must have been on the next bus after theirs."

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_0995"
    miyako "\"You must be worried about your mom, huh?\"" id a10_cou1_05_fcfccd50

    "She said, taking her shoes off."

    show fumi z4 1 lg school_scarf i with dict_dissolve_25

    voice "2FU_0973"
    fumi "\"Yeah. But it seems like it's not the flu, so that's a relief. Oh, want me to get your shoes?\"" id a10_cou1_05_d6e79dfe

    $ side_image = "miyako 1 side school_a_sei c"

    voice "2MI_0996"
    miyako "\"Thanks, but I'll do it.\"" id a10_cou1_05_11173e1d

    "She sat down next to Fumi."

    show fumi:
        xcenter 512
        easein 0.5 xcenter 298
    pause 0.5

    show fumi:
        xcenter 298
    with None
    show miyako z4 1 lg school_a_sei b:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0997"
    miyako "\"Are you relieved to have Hina helping out tomorrow too?\"" id a10_cou1_05_93637300

    show fumi:
        "fumi z4 1 lg school_scarf d" with Dissolve(0.25)
        4.0
        "fumi z4 2 lg school_scarf i" with Dissolve(0.25)

    voice "2FU_0974RE"
    fumi "\"Yes. I feel bad about it, but I was happy she said she would. I went, 'Hina!!' on the inside.\"" id a10_cou1_05_bb068e80

    show fumi z4 2 lg school_scarf i:
        pass
    with None

    "Fumi lovingly wiped Hina's shoes."

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0998"
    miyako "\"She really loves you.\"" id a10_cou1_05_a62e8e21

    show fumi z4 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_0975"
    fumi "\"Oh, I really love her, too.\"" id a10_cou1_05_c2d3070a

    "They both smiled."

    show fumi z4 2 lg school_scarf h with dict_dissolve_25

    voice "2FU_0976"
    fumi "\"So... I really want to value what limited time we have together. At least until graduation.\"" id a10_cou1_05_b1dac5d8

    "Fumi's face fell."

    show miyako z4 2 lg school_sei a with dict_dissolve_25

    voice "2MI_0999"
    miyako "\"Limited time? What do you mean?\"" id a10_cou1_05_ea518f04

    hide fumi
    hide miyako
    with dict_dissolve_50

    "Fumi told Miyako the same thing Hina had told Rin."

    $ side_image = "miyako 2 side school_sei d"

    voice "2MI_1000"
    miyako "\"......\"" id a10_cou1_05_9730d3b8

    "Miyako had listened silently to the whole thing. She slowly opened her mouth now."

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1001"
    miyako "\"So, are you alright with that, Fumi?\"" id a10_cou1_05_8ebbebc0

    $ side_image = "fumi 1 side school_scarf h"

    voice "2FU_0977"
    fumi "\"I...\"" id a10_cou1_05_642a4958

    scene bg_sozai01
    show hina 2 lg school h:
        xcenter 272
    show fumi 1 lg school_scarf h:
        xcenter 782
    with Dissolve(0.5)

    $ voice2("hina","2HI_1229","fumi","2FU_0978")
    hina_fumi "\"I want Fumi to be happy.\"\n\"I want Hina to be happy.\"" (what_rest_indent=0)

    pause 0.5

    scene white with Dissolve(0.75)
    pause 1.0

    scene bg02bg with bg_effect_26_750
    pause 0.5

    show hina z4 2 lg school h:
        xcenter 298
    show rin z4 1 lg school g:
        xcenter 726
    with dict_dissolve_25

    voice "2RI_1259"
    rin "\"What? Is she gonna be unhappy with you?\"" id a10_cou1_05_377acb55

    voice "2HI_1230"
    hina "\"I dunno. But it's not natural.\"" id a10_cou1_05_379dc2ef

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1260"
    rin "\"Not natural? Says who?\"" id a10_cou1_05_dd045814

    voice "2HI_1231"
    hina "\"I dunno who, but that's just normal, isn't it? I want Fumi to have a normal happiness, and I'm sure her parents feel the same way.\"" id a10_cou1_05_85168e97

    voice "2HI_1232"
    hina "\"...Her dad said on LIME that he wanted her to get married and take over the store.\"" id a10_cou1_05_28e3c8b1

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1261"
    rin "\"Oh...\"" id a10_cou1_05_f8211754

    "That seemed to clue Rin in to a few things."

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1262"
    rin "\"Hey, Hina? Falling in love with someone is the most natural thing in the world.\"" id a10_cou1_05_f399f9a4

    show hina z4 1 lg school n with dict_dissolve_25

    voice "2HI_1233"
    hina "\"...Uh huh.\"" id a10_cou1_05_4f547478

    voice "2RI_1263"
    rin "\"So why do you think she'd be unhappy for cherishing that feeling?\"" id a10_cou1_05_a1e11b98

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1234"
    hina "\"I...\"" id a10_cou1_05_304c14c9

    voice "2RI_1264"
    rin "\"If this is something you both decided, then that's fine. You can just be friends again. But it's not, is it? You still love her, don't you?\"" id a10_cou1_05_5dfd31ff

    show hina:
        ShakeYes

    "Hina nodded."

    stop music fadeout 1.0

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z4 1 lg school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1265"
    rin "\"Phew...\"" id a10_cou1_05_4c76985b

    show rin z4 1 lg school k:
        xoffset 0 yoffset 0
    with None

    "Rin suddenly sucked in a deep breath."

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1266"
    rin "\"If this country won't allow it, then go somewhere else! The Netherlands, Belgium, France, Germany, Spain, Norway, Sweden, Malta, England, Luxembourg,\"" id a10_cou1_05_b01f6ddc

    show hina z4 2 lg school f
    show rin z4 2 lg school a
    with dict_dissolve_25

    voice "2RI_1267"
    rin "\"Taiwan, Canada, Uruguay, Denmark, Portugal, Argentina, Brazil, Mexico, Colombia, Iceland, Ireland, Finland, Greenland, New Zealand, Australia, South Africa!\"" id a10_cou1_05_178e367b

    "She listed off in one breath. Like a tongue twister or something."

    show rin z4 1 lg school h with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "2RI_1268"
    rin "\"There's same-sex marriage in all of those countries!\"" id a10_cou1_05_aec680ce

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg school k with dict_dissolve_25

    voice "2HI_1235"
    hina "\"O-Oh.\"" id a10_cou1_05_fbee77e3

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1269"
    rin "\"If that's not enough for you, then there's America! Hawaii, Illinois, Massachusetts, Maine, Iowa, Vermont, Minnesota, Delaware, Washington,\"" id a10_cou1_05_8fb43847

    show rin z4 2 lg school c with dict_dissolve_25

    voice "2RI_1270"
    rin "\"Maryland, Rhode Island, California, Connecticut, New York, New Mexico, New Jersey, New Hampshire, Washington D.C.!\"" id a10_cou1_05_281667d3

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1236"
    hina "\"That's... pretty amazing.\"" id a10_cou1_05_6b88b020

    "Hina was shocked both by Rin's memory and her passion."

    show rin z4 1 lg school i with Dissolve(0.25)
    show rin:
        ShakeTameiki
        ShakeTameiki

    voice "2RI_1271"
    rin "\"Hahh, hahh... I'm just saying that's how natural it is, not that you actually have to leave the country, okay? It'll be a pain to see you if you do...\"" id a10_cou1_05_867a36cd

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_1237"
    hina "\"Plus, I suck at English.\"" id a10_cou1_05_8d511937

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1272"
    rin "\"Th-That too...\"" id a10_cou1_05_211833ad

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1273"
    rin "\"Anyway. Didn't you vow to stay together forever on Christmas in the chapel? Were you lying? Are you gonna break it already?\"" id a10_cou1_05_6766c02d

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1238"
    hina "\"...I wasn't lying.\"" id a10_cou1_05_63560ecf

    play music bgm07 fadein 1.0

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1274"
    rin "\"Then don't give up on it, no matter what anybody tells you!\"" id a10_cou1_05_4056a5fd

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1239"
    hina "\"Rin...\"" id a10_cou1_05_4f0d473d

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1275"
    rin "\"Then there's, you know. All the sexy stuff you could be doing, right? It would be such a waste.\"" id a10_cou1_05_0868cc4e

    "She got so passionate she had to cover it up with that comment."

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1240"
    hina "\"Will you support us, Rin?\"" id a10_cou1_05_87d24a12

    show rin z4 2 lg school b with dict_dissolve_25

    voice "2RI_1276"
    rin "\"Of course I will. Who do you think officiated for you in the chapel?\"" id a10_cou1_05_d060b3c6

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_1241"
    hina "\"That was you.\"" id a10_cou1_05_b777b6a8

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1277"
    rin "\"If anybody doesn't accept you, then bring 'em to me! My tongue will be my sword. I'll defeat them all with it!\"" id a10_cou1_05_1134de7c

    "Rin stuck her tongue out demonstratively."

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1242"
    hina "\"......\"" id a10_cou1_05_62208ba1

    hide hina with dict_dissolve_50

    "Hina had her head down in thought for a while, but eventually got up to leave the room."

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1278"
    rin "\"Hey, where are you going?\"" id a10_cou1_05_63747c3d

    $ side_image = "hina 2 side school d"

    voice "2HI_1243"
    hina "\"I'm gonna go cool my head on the roof a bit.\"" id a10_cou1_05_fc2c87e3

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1279"
    rin "\"...Okay.\"" id a10_cou1_05_e0b7ecd3

    $ side_image = "hina 2 side school c"

    voice "2HI_1244"
    hina "\"Thanks... Rin.\"" id a10_cou1_05_56f51c79

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1280"
    rin "\"Yeah.\"" id a10_cou1_05_0de5f103

    pause 0.5

    scene white with bg_effect_27_750
    pause 1.0

    scene bg05bb with bg_effect_27_750
    pause 0.5

    "At the same time, at the front door."

    show fumi z4 1 lg school_scarf h:
        xcenter 298
    show miyako z4 2 lg school_sei a:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_1002"
    miyako "\"Hm? Are you not happy now?\"" id a10_cou1_05_3796f3b4

    "Miyako tilted her head, confused."

    show fumi z4 1 lg school_scarf k with dict_dissolve_25

    voice "2FU_0979"
    fumi "\"I'm very happy with Hina. But Hina...\"" id a10_cou1_05_7f571e17

    voice "2MI_1003"
    miyako "\"Hina also looks very happy to me.\"" id a10_cou1_05_76666ad0

    show fumi z4 1 lg school_scarf h with dict_dissolve_25

    voice "2FU_0980"
    fumi "\"...Hina is very honest and kind.\"" id a10_cou1_05_7f28e2c2

    show miyako z4 2 lg school_sei b with dict_dissolve_25

    voice "2MI_1004"
    miyako "\"Yes.\"" id a10_cou1_05_c638d231

    "I don't disagree."

    voice "2FU_0981"
    fumi "\"She's great at sports, a great leader, and everyone loves her. She'll be able to do anything in the future. She can shine even brighter.\"" id a10_cou1_05_e1fee9f9

    show fumi z4 1 lg school_scarf i with dict_dissolve_25

    voice "2FU_0982"
    fumi "\"...I can't hold her back. I have to let her go so she can become anything she wants.\"" id a10_cou1_05_21308fa1

    "Fumi was trying to smile, but I couldn't say she was succeeding by any measure."

    show fumi z4 1 lg school_scarf k with dict_dissolve_25

    voice "2FU_0983"
    fumi "\"But for a little while longer... at least until graduation, while we're here in this dorm, I'd like to be together.\"" id a10_cou1_05_5e7e2d85

    show fumi z4 1 lg school_scarf h with dict_dissolve_25

    voice "2FU_0984"
    fumi "\"And I don't want her to do something bad because of me.\"" id a10_cou1_05_a4e34923

    show miyako z4 1 lg school_a_sei a with dict_dissolve_25

    voice "2MI_1005"
    miyako "\"What do you mean?\"" id a10_cou1_05_1be4ed35

    "Miyako couldn't agree or disagree with anything Fumi was saying. She was just listening to what she had to say."

    show miyako z4 1 lg school_a_sei e with dict_dissolve_25

    voice "2MI_1006"
    miyako "\"Because you're both girls?\"" id a10_cou1_05_4d7ef459

    show fumi:
        ShakeYes

    "Fumi bit her lip and nodded."

    show fumi z4 1 lg school_scarf k:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2FU_0985"
    fumi "\"It's against the law. And I want Hina to have a normal happiness.\"" id a10_cou1_05_a7bdde89

    show miyako z4 2 lg school_sei a with dict_dissolve_25

    voice "2MI_1007"
    miyako "\"It's only marriage that's against the law, right? Is it against the law for you to be together, too?\"" id a10_cou1_05_d1ff7554

    show fumi z4 1 lg school_scarf h with dict_dissolve_25

    voice "2FU_0986"
    fumi "\"......\"" id a10_cou1_05_e2f6c6cd

    show miyako z4 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1008"
    miyako "\"There's no such thing as normal or not normal happiness. All happiness should be cherished.\"" id a10_cou1_05_0b5feb4b

    show fumi z4 2 lg school_scarf h with dict_dissolve_25

    voice "2FU_0987"
    fumi "\"Miyako...\"" id a10_cou1_05_3c6ee3c2

    show miyako z4 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1009"
    miyako "\"Loving someone isn't a crime. If someone tries to accuse you of something, then let's fight it.\"" id a10_cou1_05_e88a45bb

    show miyako z4 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1010"
    miyako "\"I'll stand beside you as your guardian angel if that happens, protecting the two of you from baseless claims with my invincible aegis.\"" id a10_cou1_05_dc50c91a

    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_0988"
    fumi "\"Wow...\"" id a10_cou1_05_bc5f2648

    "Fumi was surprised at Miyako's uncharacteristically strong tone."

    show miyako z4 1 lg school_b_sei b with dict_dissolve_25

    voice "2MI_1011"
    miyako "\"I'll always be on your side. And I'm sure Rin and Sachiko will, too.\"" id a10_cou1_05_b52d7f46

    show miyako z4 1 lg school_b_sei h with dict_dissolve_25

    voice "2MI_1012"
    miyako "\"Didn't you promise to keep loving each other until you're old and grey, and to cherish each other forever?\"" id a10_cou1_05_6ee06962

    show fumi:
        "fumi z4 2 lg school_scarf a" with Dissolve(0.25)
        4.0
        "fumi z4 2 lg school_scarf g" with Dissolve(0.25)

    voice "2FU_0989"
    fumi "\"Yes, we did... Wait, but how did you...?\"" id a10_cou1_05_898d7946

    show fumi z4 2 lg school_scarf g:
        pass
    with None
    show miyako z4 1 lg school_a_sei f with Dissolve(0.25)
    show miyako:
        ShakeSide

    voice "2MI_1013"
    miyako "\"Umm, Rin told me.\"" id a10_cou1_05_1e21dbc6

    show miyako:
        xoffset 0 yoffset 0
    with None

    "She was watching."

    show miyako:
        "miyako z4 1 lg school_a_sei a" with Dissolve(0.25)
        ShakeYes

    voice "2MI_1014"
    miyako "\"Anyway, nothing can part you two other than your own feelings.\"" id a10_cou1_05_6575ed11

    show miyako z4 1 lg school_a_sei a:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school_scarf b with dict_dissolve_25

    voice "2FU_0990"
    fumi "\"Thank you, Miyako.\"" id a10_cou1_05_60e08ce4

    show miyako z4 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_1015"
    miyako "\"Now let's get back to our room.\"" id a10_cou1_05_6f228b5c

    show fumi:
        "fumi z4 1 lg school_scarf c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0991"
    fumi "\"Yeah!\"" id a10_cou1_05_2e3eebac

    show fumi z4 1 lg school_scarf c:
        xoffset 0 yoffset 0
    with None

    "They both stood, holding their shoes."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou1_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
