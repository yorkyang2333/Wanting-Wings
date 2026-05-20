label a10_cou1_05:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    show rin z4 1 lg school k with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "2RI_1251"
    rin "\"I'm impressed at that quick decision-making. From you and your dad.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Hina and Rin had arrived home first, and Rin had said that while changing clothes."

    $ side_image = "hina 2 side school d"

    voice "2HI_1221"
    hina "\"I know how busy they are.\""

    "Hina was putting the food they'd bought in the fridge before she changed."

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_1252"
    rin "\"I was kinda worried you two were fighting.\""

    $ side_image = "hina 1 side school e"

    voice "2HI_1222"
    hina "\"We're not. We love each other.\""

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1253"
    rin "\"R-Right. You can say it with no hesitation, huh?\""

    "Once again, Rin was awed by Hina's emotional fortitude."

    hide rin with Dissolve(0.25)

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1223"
    hina "\"I want to be with her for as much of our limited time as I can.\""

    $ side_image = "rin 1 side school e"

    voice "2RI_1254"
    rin "\"Hm? Limited time? What do you mean? You're not gonna be together forever?\""

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1224"
    hina "\"...Fumi's gonna have to get married someday. Then we won't be able to be together anymore.\""

    $ side_image = "rin 1 side school j"

    voice "2RI_1255"
    rin "\"Hwha?\""

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1225"
    hina "\"So we're only dating until we graduate.\""

    $ side_image = "rin 1 side school g"

    voice "2RI_1256"
    rin "\"Did Asou say that?\""

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_1226"
    hina "\"No...\""

    $ side_image = "rin 1 side school i"

    voice "2RI_1257"
    rin "\"Then did her parents say something to you?\""

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1227"
    hina "\"No...\""

    $ side_image = "rin 1 side school i"

    voice "2RI_1258"
    rin "\"So, are you okay with that?\""

    voice "2HI_1228"
    hina "\"I...\""

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
    miyako "\"I'm back, Fumi.\""

    show fumi z4 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_0972"
    fumi "\"Oh, hello, Miyako.\""

    "Miyako had also returned. She must have been on the next bus after theirs."

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_0995"
    miyako "\"You must be worried about your mom, huh?\""

    "She said, taking her shoes off."

    show fumi z4 1 lg school_scarf i with dict_dissolve_25

    voice "2FU_0973"
    fumi "\"Yeah. But it seems like it's not the flu, so that's a relief. Oh, want me to get your shoes?\""

    $ side_image = "miyako 1 side school_a_sei c"

    voice "2MI_0996"
    miyako "\"Thanks, but I'll do it.\""

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
    miyako "\"Are you relieved to have Hina helping out tomorrow too?\""

    show fumi:
        "fumi z4 1 lg school_scarf d" with Dissolve(0.25)
        4.0
        "fumi z4 2 lg school_scarf i" with Dissolve(0.25)

    voice "2FU_0974RE"
    fumi "\"Yes. I feel bad about it, but I was happy she said she would. I went, 'Hina!!' on the inside.\""

    show fumi z4 2 lg school_scarf i:
        pass
    with None

    "Fumi lovingly wiped Hina's shoes."

    show miyako z4 1 lg school_a_sei c with dict_dissolve_25

    voice "2MI_0998"
    miyako "\"She really loves you.\""

    show fumi z4 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_0975"
    fumi "\"Oh, I really love her, too.\""

    "They both smiled."

    show fumi z4 2 lg school_scarf h with dict_dissolve_25

    voice "2FU_0976"
    fumi "\"So... I really want to value what limited time we have together. At least until graduation.\""

    "Fumi's face fell."

    show miyako z4 2 lg school_sei a with dict_dissolve_25

    voice "2MI_0999"
    miyako "\"Limited time? What do you mean?\""

    hide fumi
    hide miyako
    with dict_dissolve_50

    "Fumi told Miyako the same thing Hina had told Rin."

    $ side_image = "miyako 2 side school_sei d"

    voice "2MI_1000"
    miyako "\"......\""

    "Miyako had listened silently to the whole thing. She slowly opened her mouth now."

    $ side_image = "miyako 2 side school_sei b"

    voice "2MI_1001"
    miyako "\"So, are you alright with that, Fumi?\""

    $ side_image = "fumi 1 side school_scarf h"

    voice "2FU_0977"
    fumi "\"I...\""

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
    rin "\"What? Is she gonna be unhappy with you?\""

    voice "2HI_1230"
    hina "\"I dunno. But it's not natural.\""

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1260"
    rin "\"Not natural? Says who?\""

    voice "2HI_1231"
    hina "\"I dunno who, but that's just normal, isn't it? I want Fumi to have a normal happiness, and I'm sure her parents feel the same way.\""

    voice "2HI_1232"
    hina "\"...Her dad said on LIME that he wanted her to get married and take over the store.\""

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1261"
    rin "\"Oh...\""

    "That seemed to clue Rin in to a few things."

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1262"
    rin "\"Hey, Hina? Falling in love with someone is the most natural thing in the world.\""

    show hina z4 1 lg school n with dict_dissolve_25

    voice "2HI_1233"
    hina "\"...Uh huh.\""

    voice "2RI_1263"
    rin "\"So why do you think she'd be unhappy for cherishing that feeling?\""

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1234"
    hina "\"I...\""

    voice "2RI_1264"
    rin "\"If this is something you both decided, then that's fine. You can just be friends again. But it's not, is it? You still love her, don't you?\""

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
    rin "\"Phew...\""

    show rin z4 1 lg school k:
        xoffset 0 yoffset 0
    with None

    "Rin suddenly sucked in a deep breath."

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1266"
    rin "\"If this country won't allow it, then go somewhere else! The Netherlands, Belgium, France, Germany, Spain, Norway, Sweden, Malta, England, Luxembourg,\""

    show hina z4 2 lg school f
    show rin z4 2 lg school a
    with dict_dissolve_25

    voice "2RI_1267"
    rin "\"Taiwan, Canada, Uruguay, Denmark, Portugal, Argentina, Brazil, Mexico, Colombia, Iceland, Ireland, Finland, Greenland, New Zealand, Australia, South Africa!\""

    "She listed off in one breath. Like a tongue twister or something."

    show rin z4 1 lg school h with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "2RI_1268"
    rin "\"There's same-sex marriage in all of those countries!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg school k with dict_dissolve_25

    voice "2HI_1235"
    hina "\"O-Oh.\""

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1269"
    rin "\"If that's not enough for you, then there's America! Hawaii, Illinois, Massachusetts, Maine, Iowa, Vermont, Minnesota, Delaware, Washington,\""

    show rin z4 2 lg school c with dict_dissolve_25

    voice "2RI_1270"
    rin "\"Maryland, Rhode Island, California, Connecticut, New York, New Mexico, New Jersey, New Hampshire, Washington D.C.!\""

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1236"
    hina "\"That's... pretty amazing.\""

    "Hina was shocked both by Rin's memory and her passion."

    show rin z4 1 lg school i with Dissolve(0.25)
    show rin:
        ShakeTameiki
        ShakeTameiki

    voice "2RI_1271"
    rin "\"Hahh, hahh... I'm just saying that's how natural it is, not that you actually have to leave the country, okay? It'll be a pain to see you if you do...\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_1237"
    hina "\"Plus, I suck at English.\""

    show rin z4 1 lg school g with dict_dissolve_25

    voice "2RI_1272"
    rin "\"Th-That too...\""

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1273"
    rin "\"Anyway. Didn't you vow to stay together forever on Christmas in the chapel? Were you lying? Are you gonna break it already?\""

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1238"
    hina "\"...I wasn't lying.\""

    play music bgm07 fadein 1.0

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1274"
    rin "\"Then don't give up on it, no matter what anybody tells you!\""

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1239"
    hina "\"Rin...\""

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1275"
    rin "\"Then there's, you know. All the sexy stuff you could be doing, right? It would be such a waste.\""

    "She got so passionate she had to cover it up with that comment."

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1240"
    hina "\"Will you support us, Rin?\""

    show rin z4 2 lg school b with dict_dissolve_25

    voice "2RI_1276"
    rin "\"Of course I will. Who do you think officiated for you in the chapel?\""

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_1241"
    hina "\"That was you.\""

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1277"
    rin "\"If anybody doesn't accept you, then bring 'em to me! My tongue will be my sword. I'll defeat them all with it!\""

    "Rin stuck her tongue out demonstratively."

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1242"
    hina "\"......\""

    hide hina with dict_dissolve_50

    "Hina had her head down in thought for a while, but eventually got up to leave the room."

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1278"
    rin "\"Hey, where are you going?\""

    $ side_image = "hina 2 side school d"

    voice "2HI_1243"
    hina "\"I'm gonna go cool my head on the roof a bit.\""

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1279"
    rin "\"...Okay.\""

    $ side_image = "hina 2 side school c"

    voice "2HI_1244"
    hina "\"Thanks... Rin.\""

    show rin z4 1 lg school c with dict_dissolve_25

    voice "2RI_1280"
    rin "\"Yeah.\""

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
    miyako "\"Hm? Are you not happy now?\""

    "Miyako tilted her head, confused."

    show fumi z4 1 lg school_scarf k with dict_dissolve_25

    voice "2FU_0979"
    fumi "\"I'm very happy with Hina. But Hina...\""

    voice "2MI_1003"
    miyako "\"Hina also looks very happy to me.\""

    show fumi z4 1 lg school_scarf h with dict_dissolve_25

    voice "2FU_0980"
    fumi "\"...Hina is very honest and kind.\""

    show miyako z4 2 lg school_sei b with dict_dissolve_25

    voice "2MI_1004"
    miyako "\"Yes.\""

    "I don't disagree."

    voice "2FU_0981"
    fumi "\"She's great at sports, a great leader, and everyone loves her. She'll be able to do anything in the future. She can shine even brighter.\""

    show fumi z4 1 lg school_scarf i with dict_dissolve_25

    voice "2FU_0982"
    fumi "\"...I can't hold her back. I have to let her go so she can become anything she wants.\""

    "Fumi was trying to smile, but I couldn't say she was succeeding by any measure."

    show fumi z4 1 lg school_scarf k with dict_dissolve_25

    voice "2FU_0983"
    fumi "\"But for a little while longer... at least until graduation, while we're here in this dorm, I'd like to be together.\""

    show fumi z4 1 lg school_scarf h with dict_dissolve_25

    voice "2FU_0984"
    fumi "\"And I don't want her to do something bad because of me.\""

    show miyako z4 1 lg school_a_sei a with dict_dissolve_25

    voice "2MI_1005"
    miyako "\"What do you mean?\""

    "Miyako couldn't agree or disagree with anything Fumi was saying. She was just listening to what she had to say."

    show miyako z4 1 lg school_a_sei e with dict_dissolve_25

    voice "2MI_1006"
    miyako "\"Because you're both girls?\""

    show fumi:
        ShakeYes

    "Fumi bit her lip and nodded."

    show fumi z4 1 lg school_scarf k:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2FU_0985"
    fumi "\"It's against the law. And I want Hina to have a normal happiness.\""

    show miyako z4 2 lg school_sei a with dict_dissolve_25

    voice "2MI_1007"
    miyako "\"It's only marriage that's against the law, right? Is it against the law for you to be together, too?\""

    show fumi z4 1 lg school_scarf h with dict_dissolve_25

    voice "2FU_0986"
    fumi "\"......\""

    show miyako z4 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1008"
    miyako "\"There's no such thing as normal or not normal happiness. All happiness should be cherished.\""

    show fumi z4 2 lg school_scarf h with dict_dissolve_25

    voice "2FU_0987"
    fumi "\"Miyako...\""

    show miyako z4 1 lg school_a_sei i with dict_dissolve_25

    voice "2MI_1009"
    miyako "\"Loving someone isn't a crime. If someone tries to accuse you of something, then let's fight it.\""

    show miyako z4 1 lg school_a_sei j with dict_dissolve_25

    voice "2MI_1010"
    miyako "\"I'll stand beside you as your guardian angel if that happens, protecting the two of you from baseless claims with my invincible aegis.\""

    show fumi z4 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_0988"
    fumi "\"Wow...\""

    "Fumi was surprised at Miyako's uncharacteristically strong tone."

    show miyako z4 1 lg school_b_sei b with dict_dissolve_25

    voice "2MI_1011"
    miyako "\"I'll always be on your side. And I'm sure Rin and Sachiko will, too.\""

    show miyako z4 1 lg school_b_sei h with dict_dissolve_25

    voice "2MI_1012"
    miyako "\"Didn't you promise to keep loving each other until you're old and grey, and to cherish each other forever?\""

    show fumi:
        "fumi z4 2 lg school_scarf a" with Dissolve(0.25)
        4.0
        "fumi z4 2 lg school_scarf g" with Dissolve(0.25)

    voice "2FU_0989"
    fumi "\"Yes, we did... Wait, but how did you...?\""

    show fumi z4 2 lg school_scarf g:
        pass
    with None
    show miyako z4 1 lg school_a_sei f with Dissolve(0.25)
    show miyako:
        ShakeSide

    voice "2MI_1013"
    miyako "\"Umm, Rin told me.\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "She was watching."

    show miyako:
        "miyako z4 1 lg school_a_sei a" with Dissolve(0.25)
        ShakeYes

    voice "2MI_1014"
    miyako "\"Anyway, nothing can part you two other than your own feelings.\""

    show miyako z4 1 lg school_a_sei a:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school_scarf b with dict_dissolve_25

    voice "2FU_0990"
    fumi "\"Thank you, Miyako.\""

    show miyako z4 1 lg school_a_sei b with dict_dissolve_25

    voice "2MI_1015"
    miyako "\"Now let's get back to our room.\""

    show fumi:
        "fumi z4 1 lg school_scarf c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0991"
    fumi "\"Yeah!\""

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
