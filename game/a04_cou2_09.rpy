label a04_cou2_09:

    scene bg08cb with Dissolve(0.5)
    pause 1.5

    play music bgm05

    play sound se131a

    "With the setting of the sun, the rain had turned to snow."

    "Rin seemed to have an idea about where Hina had gone. She headed straight toward a certain location."

    scene black with Dissolve(0.25)
    pause 1.25

    scene bg06ca with Dissolve(0.25)
    pause 1.25

    play sound woodendoor

    show rin:
        "rin 1 sm school g flat"
        alpha 0.0 xcenter 412
        easein 0.5 alpha 1.0 xcenter 512
    pause 0.5

    show rin 1 sm school g:
        alpha 1.0 xcenter 512
    with None

    voice "RIN_1212"
    rin "\"Haah, haah, haahh...\"" id a04_cou2_09_adca22f6

    "Rin turned on the light and looked around the chapel."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_1213"
    rin "\"Hina, you're here, aren't you? Come out.\"" id a04_cou2_09_695e08a5

    "There was no answer."

    "But a shadow was moving between the pews."

    "Rin had surely noticed it, too."

    show rin 1 lg school a with dict_dissolve_25:
        1.3
        "rin 1 lg school h" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_1214"
    rin "\"...HINA!\"" id a04_cou2_09_d1b78929

    show rin 1 lg school h:
        xoffset 0 yoffset 0
    with None

    "Rin took a deep breath and shouted. It was rare for her to show so much emotion."

    $ side_image = "hina 2 side school j"

    voice "HIN_1436"
    hina "\"Ah!\"" id a04_cou2_09_0b9cd0b7

    "A figure popped up with a yelp and tried to hide in the corner of the building."

    show rin 2 lg school a with dict_dissolve_25

    voice "RIN_1215"
    rin "\"Stay!\"" id a04_cou2_09_87482508

    $ side_image = "hina 2 side school i"

    voice "HIN_1437"
    hina "\"!\"" id a04_cou2_09_9fe8aea2

    "The figure stopped."

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1216"
    rin "\"Come here.\"" id a04_cou2_09_1f7a4a56

    $ side_image = "hina 2 side school h"

    voice "HIN_1438"
    hina "\"...Augh.\"" id a04_cou2_09_ddc54995

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1217"
    rin "\"Get! Over! Here! Right! Now!\"" id a04_cou2_09_5e73af8a

    $ side_image = "hina 2 side school h"

    voice "HIN_1439"
    hina "\"...Auuugh.\"" id a04_cou2_09_264f2d0f

    "Hina emerged from behind the organ, trying to make herself look smaller."

    show rin:
        "rin 1 lg school h" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 252
    show hina:
        "hina 2 lg school e flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772
    pause 0.5

    show rin 1 lg school h:
        xcenter 252
    show hina 2 lg school e:
        alpha 1.0 xcenter 772
    with None

    voice "HIN_1440"
    hina "\"...How did you know I was here?\"" id a04_cou2_09_1aa4b6f5

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1218"
    rin "\"Haahh. Where were you gonna go without your wallet? This is the only place with a roof you could get into.\"" id a04_cou2_09_c60c5480

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1441"
    hina "\".........\"" id a04_cou2_09_5604dbb4

    show rin 2 lg school b with dict_dissolve_25

    voice "RIN_1219"
    rin "\"Come on, let's go home.\"" id a04_cou2_09_e88eab77

    "Rin said, holding out her hand."

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1442"
    hina "\"...But I can't be with you anymore.\"" id a04_cou2_09_2cadc92f

    show rin 2 lg school a with dict_dissolve_25

    voice "RIN_1220"
    rin "\"Why can't you?\"" id a04_cou2_09_659ebe76

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1443"
    hina "\"It was just a little bit of fun for you, wasn't it, Rin?\"" id a04_cou2_09_aa9df68b

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_1221"
    rin "\"Huh?\"" id a04_cou2_09_9b7888f8

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1444"
    hina "\"I don't have any boobs or curves, and I suck at sex...\"" id a04_cou2_09_1e541e35

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1222"
    rin "\"Huh?\"" id a04_cou2_09_92b40f17

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1445"
    hina "\"You'd rather be with a mature woman who knows what she's doing than a little shrimp like me.\"" id a04_cou2_09_618c6353

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeJump

    voice "RIN_1223"
    rin "\"Huh?!\"" id a04_cou2_09_f2ca6f2f

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1446"
    hina "\"But I love you. So I can't be with you anymore.\"" id a04_cou2_09_dccd3f78

    show rin:
        ShakeSide
        ShakeSide

    voice "RIN_1224"
    rin "\"Huh, huh, huh?!\"" id a04_cou2_09_cffa2cc3

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school j with dict_dissolve_25

    voice "HIN_1447"
    hina "\"Waaah!\"" id a04_cou2_09_d22e2dfc

    "Hina finally began to cry."

    stop music fadeout 3.0

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1225"
    rin "\"Okay, stay right there!\"" id a04_cou2_09_6d59233f

    show hina:
        "hina 2 lg school h" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1448"
    hina "\"Ugh...\"" id a04_cou2_09_f9098d7b

    show hina 2 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1226"
    rin "\"Down!\"" id a04_cou2_09_9a560b8e

    "Rin snapped when Hina was about to run again."

    show hina:
        ShakeSide

    voice "HIN_1449"
    hina "\"...Ugh.\"" id a04_cou2_09_f0d513f2

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin:
        xcenter 252
        easein 0.5 xcenter 542
    pause 0.5

    show rin 1 lg school h:
        xcenter 542
    with None

    play sound se118a

    "Rin gravely strode toward Hina and embraced her, holding her in place."

    play music bgm02

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1227"
    rin "\"...You really are a stupid dog.\"" id a04_cou2_09_84c74fc2

    "She held Hina tight."

    show hina 2 lg school j with dict_dissolve_25

    voice "HIN_1450"
    hina "\"Weeeh...\"" id a04_cou2_09_749485fe

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1228"
    rin "\"Since you're so stupid, I'll explain everything to you.\"" id a04_cou2_09_01152b61

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1451"
    hina "\"...\"" id a04_cou2_09_91599c70

    "Great, big tears fell from Hina's eyes and wet Rin's shirt."

    show hina 2 lg school j with dict_dissolve_25

    voice "HIN_1452"
    hina "\"You went to Sachiko's room... When you came back, you smelled like smoke.\"" id a04_cou2_09_e232ceb0

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1229"
    rin "\"You were awake last night.\"" id a04_cou2_09_f3058be4

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1453"
    hina "\"...I was waiting for you.\"" id a04_cou2_09_6433238e

    show rin 1 lg school c with dict_dissolve_25

    "Rin smiled slightly and laid a hand on Hina's head."

    voice "RIN_1230"
    rin "\"I was going to Sachiko's room for work.\"" id a04_cou2_09_fc6341fd

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1454"
    hina "\"...Dirty work?\"" id a04_cou2_09_f9b92a03

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1231"
    rin "\"Don't be stupid. I was modeling for her.\"" id a04_cou2_09_6898130f

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1455"
    hina "\"...For a dirty picture?\"" id a04_cou2_09_d6d314f0

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1232"
    rin "\"I had clothes on!\"" id a04_cou2_09_8d4d27ee

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1456"
    hina "\"But why now? You never would before.\"" id a04_cou2_09_8ad9a698

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1233"
    rin "\"...To buy a present for you, duh.\"" id a04_cou2_09_70d813df

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1457"
    hina "\"A computer?\"" id a04_cou2_09_0c5f3cf7

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1234"
    rin "\"No, that's not happening. But... I think you'll like it more.\"" id a04_cou2_09_b1e9ed17

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1458"
    hina "\"...You could have told me.\"" id a04_cou2_09_ad4af30b

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_1235"
    rin "\"You're supposed to keep these things secret.\"" id a04_cou2_09_52fc0eb4

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1458a"
    hina "\"Did Asou know?\"" id a04_cou2_09_e78094bc

    show rin 1 lg school f with dict_dissolve_25

    voice "RIN_1236"
    rin "\"I told her not to tell you. She helped me pick it out.\"" id a04_cou2_09_762352fd

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_1459"
    hina "\"...Is that what it was?\"" id a04_cou2_09_6c046f56

    "Hina sighed in relief."

    stop music fadeout 1.0

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1237"
    rin "\"And one more thing...\"" id a04_cou2_09_13ccf509

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1460"
    hina "\"Hunh?\"" id a04_cou2_09_9736ab67

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1238"
    rin "\"You said it was just fun for me...\"" id a04_cou2_09_81fc9c55

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1461"
    hina "\"...!\"" id a04_cou2_09_5ac2b5be

    "Rin was quiet, but her harsh tone surprised Hina."

    voice "RIN_1239"
    rin "\"Do you know how much I stressed over you and over all this?\"" id a04_cou2_09_d57d5e01

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1240"
    rin "\"I'm not an {i}angel{/i} like you...\"" id a04_cou2_09_8b12de3a

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1462"
    hina "\"What do you mean?\"" id a04_cou2_09_1b9967d5

    play music bgm03

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1241"
    rin "\"This is the first time I've been in love too! I don't have any idea what I'm doing!\"" id a04_cou2_09_c13c5708

    show hina 2 lg school e with dict_dissolve_25

    voice "HIN_1463"
    hina "\"I thought you were way more experienced, Rin...\"" id a04_cou2_09_b4587abf

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1242"
    rin "\"How? Have you ever even seen me communicate with anyone outside of the dorm... ugh!\"" id a04_cou2_09_44d47355

    "She took a self-inflicted wound there."

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1464"
    hina "\"But you're good at sex...\"" id a04_cou2_09_b4822da3

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1243"
    rin "\"Wh... You think I'm not super nervous every time I touch you? Y-You're just too sensitive!\"" id a04_cou2_09_ba0fd302

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1465"
    hina "\"Augh... I'm sorry.\"" id a04_cou2_09_66885500

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1244"
    rin "\"...So, does that clear up your misunderstanding?\"" id a04_cou2_09_aed07999

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1466"
    hina "\"Yeah... but...\"" id a04_cou2_09_f0cbc59b

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1245"
    rin "\"What?\"" id a04_cou2_09_e5b258c5

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1467"
    hina "\"You haven't told me you love me yet.\"" id a04_cou2_09_e0b37ea2

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1246"
    rin "\"Ugh...\"" id a04_cou2_09_09b234ee

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "She landed a critical hit."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1247"
    rin "\"Umm... I'm saving that for a special occasion.\"" id a04_cou2_09_dabab5d8

    show hina 2 lg school d with dict_dissolve_25

    voice "HIN_1468"
    hina "\"......\"" id a04_cou2_09_a953c5c0

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1248"
    rin "\"Fine... {size=15}I love you.{/size}\"" id a04_cou2_09_b8fe043a

    "Rin put her mouth up to Hina's ear and whispered to her ever so quietly."

    show hina 2 lg school g with dict_dissolve_25:
        1.8
        ShakeJump
        ShakeJump

    voice "HIN_1469"
    hina "\"...Heh, heheheh! I love you, I love you, I love you, Rin!\"" id a04_cou2_09_b5e50973

    show hina:
        xoffset 0 yoffset 0
    with None

    "And Hina held out both hands to her, a beaming smile on her face."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1249"
    rin "\"...What's with the hands?\"" id a04_cou2_09_e135e577

    show hina 2 lg school a with dict_dissolve_25

    voice "HIN_1470"
    hina "\"My present.\"" id a04_cou2_09_a91b9a8d

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1250"
    rin "\"I'll put it in your stocking tonight.\"" id a04_cou2_09_abc97ebf

    show hina 2 lg school b with dict_dissolve_25

    voice "HIN_1471"
    hina "\"I want it now!\"" id a04_cou2_09_86c2efef

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1251"
    rin "\"I'm saving it.\"" id a04_cou2_09_4673f8d1

    show hina:
        "hina 2 lg school h" with Dissolve(0.25)
        ShakeUji

    voice "HIN_1472"
    hina "\"Uuuuugh.\"" id a04_cou2_09_965a62a4

    show hina 2 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1252"
    rin "\"Stop grumbling!\"" id a04_cou2_09_6a071215

    show hina:
        "hina 2 lg school i" with Dissolve(0.25)
        ShakeNo

    voice "HIN_1473"
    hina "\"Uuuuugh!\"" id a04_cou2_09_81daa265

    show hina 2 lg school i:
        xoffset 0 yoffset 0
    with None

    pause 1.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene white with Dissolve(0.75)
    pause 2.25

    call staff_01 from _call_staff_01_1

    jump a04_cou2_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
