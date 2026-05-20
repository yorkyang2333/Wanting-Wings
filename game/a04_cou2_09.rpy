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
    rin "\"Haah, haah, haahh...\""

    "Rin turned on the light and looked around the chapel."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_1213"
    rin "\"Hina, you're here, aren't you? Come out.\""

    "There was no answer."

    "But a shadow was moving between the pews."

    "Rin had surely noticed it, too."

    show rin 1 lg school a with dict_dissolve_25:
        1.3
        "rin 1 lg school h" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_1214"
    rin "\"...HINA!\""

    show rin 1 lg school h:
        xoffset 0 yoffset 0
    with None

    "Rin took a deep breath and shouted. It was rare for her to show so much emotion."

    $ side_image = "hina 2 side school j"

    voice "HIN_1436"
    hina "\"Ah!\""

    "A figure popped up with a yelp and tried to hide in the corner of the building."

    show rin 2 lg school a with dict_dissolve_25

    voice "RIN_1215"
    rin "\"Stay!\""

    $ side_image = "hina 2 side school i"

    voice "HIN_1437"
    hina "\"!\""

    "The figure stopped."

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1216"
    rin "\"Come here.\""

    $ side_image = "hina 2 side school h"

    voice "HIN_1438"
    hina "\"...Augh.\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1217"
    rin "\"Get! Over! Here! Right! Now!\""

    $ side_image = "hina 2 side school h"

    voice "HIN_1439"
    hina "\"...Auuugh.\""

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
    hina "\"...How did you know I was here?\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1218"
    rin "\"Haahh. Where were you gonna go without your wallet? This is the only place with a roof you could get into.\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1441"
    hina "\".........\""

    show rin 2 lg school b with dict_dissolve_25

    voice "RIN_1219"
    rin "\"Come on, let's go home.\""

    "Rin said, holding out her hand."

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1442"
    hina "\"...But I can't be with you anymore.\""

    show rin 2 lg school a with dict_dissolve_25

    voice "RIN_1220"
    rin "\"Why can't you?\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1443"
    hina "\"It was just a little bit of fun for you, wasn't it, Rin?\""

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_1221"
    rin "\"Huh?\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1444"
    hina "\"I don't have any boobs or curves, and I suck at sex...\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_1222"
    rin "\"Huh?\""

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1445"
    hina "\"You'd rather be with a mature woman who knows what she's doing than a little shrimp like me.\""

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeJump

    voice "RIN_1223"
    rin "\"Huh?!\""

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1446"
    hina "\"But I love you. So I can't be with you anymore.\""

    show rin:
        ShakeSide
        ShakeSide

    voice "RIN_1224"
    rin "\"Huh, huh, huh?!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school j with dict_dissolve_25

    voice "HIN_1447"
    hina "\"Waaah!\""

    "Hina finally began to cry."

    stop music fadeout 3.0

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1225"
    rin "\"Okay, stay right there!\""

    show hina:
        "hina 2 lg school h" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1448"
    hina "\"Ugh...\""

    show hina 2 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1226"
    rin "\"Down!\""

    "Rin snapped when Hina was about to run again."

    show hina:
        ShakeSide

    voice "HIN_1449"
    hina "\"...Ugh.\""

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
    rin "\"...You really are a stupid dog.\""

    "She held Hina tight."

    show hina 2 lg school j with dict_dissolve_25

    voice "HIN_1450"
    hina "\"Weeeh...\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1228"
    rin "\"Since you're so stupid, I'll explain everything to you.\""

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1451"
    hina "\"...\""

    "Great, big tears fell from Hina's eyes and wet Rin's shirt."

    show hina 2 lg school j with dict_dissolve_25

    voice "HIN_1452"
    hina "\"You went to Sachiko's room... When you came back, you smelled like smoke.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1229"
    rin "\"You were awake last night.\""

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1453"
    hina "\"...I was waiting for you.\""

    show rin 1 lg school c with dict_dissolve_25

    "Rin smiled slightly and laid a hand on Hina's head."

    voice "RIN_1230"
    rin "\"I was going to Sachiko's room for work.\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1454"
    hina "\"...Dirty work?\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1231"
    rin "\"Don't be stupid. I was modeling for her.\""

    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1455"
    hina "\"...For a dirty picture?\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1232"
    rin "\"I had clothes on!\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1456"
    hina "\"But why now? You never would before.\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1233"
    rin "\"...To buy a present for you, duh.\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1457"
    hina "\"A computer?\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1234"
    rin "\"No, that's not happening. But... I think you'll like it more.\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1458"
    hina "\"...You could have told me.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_1235"
    rin "\"You're supposed to keep these things secret.\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1458a"
    hina "\"Did Asou know?\""

    show rin 1 lg school f with dict_dissolve_25

    voice "RIN_1236"
    rin "\"I told her not to tell you. She helped me pick it out.\""

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_1459"
    hina "\"...Is that what it was?\""

    "Hina sighed in relief."

    stop music fadeout 1.0

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1237"
    rin "\"And one more thing...\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1460"
    hina "\"Hunh?\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1238"
    rin "\"You said it was just fun for me...\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1461"
    hina "\"...!\""

    "Rin was quiet, but her harsh tone surprised Hina."

    voice "RIN_1239"
    rin "\"Do you know how much I stressed over you and over all this?\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1240"
    rin "\"I'm not an {i}angel{/i} like you...\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1462"
    hina "\"What do you mean?\""

    play music bgm03

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1241"
    rin "\"This is the first time I've been in love too! I don't have any idea what I'm doing!\""

    show hina 2 lg school e with dict_dissolve_25

    voice "HIN_1463"
    hina "\"I thought you were way more experienced, Rin...\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1242"
    rin "\"How? Have you ever even seen me communicate with anyone outside of the dorm... ugh!\""

    "She took a self-inflicted wound there."

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1464"
    hina "\"But you're good at sex...\""

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1243"
    rin "\"Wh... You think I'm not super nervous every time I touch you? Y-You're just too sensitive!\""

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school i with dict_dissolve_25

    voice "HIN_1465"
    hina "\"Augh... I'm sorry.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1244"
    rin "\"...So, does that clear up your misunderstanding?\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1466"
    hina "\"Yeah... but...\""

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1245"
    rin "\"What?\""

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1467"
    hina "\"You haven't told me you love me yet.\""

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1246"
    rin "\"Ugh...\""

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "She landed a critical hit."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1247"
    rin "\"Umm... I'm saving that for a special occasion.\""

    show hina 2 lg school d with dict_dissolve_25

    voice "HIN_1468"
    hina "\"......\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1248"
    rin "\"Fine... {size=15}I love you.{/size}\""

    "Rin put her mouth up to Hina's ear and whispered to her ever so quietly."

    show hina 2 lg school g with dict_dissolve_25:
        1.8
        ShakeJump
        ShakeJump

    voice "HIN_1469"
    hina "\"...Heh, heheheh! I love you, I love you, I love you, Rin!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "And Hina held out both hands to her, a beaming smile on her face."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1249"
    rin "\"...What's with the hands?\""

    show hina 2 lg school a with dict_dissolve_25

    voice "HIN_1470"
    hina "\"My present.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1250"
    rin "\"I'll put it in your stocking tonight.\""

    show hina 2 lg school b with dict_dissolve_25

    voice "HIN_1471"
    hina "\"I want it now!\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1251"
    rin "\"I'm saving it.\""

    show hina:
        "hina 2 lg school h" with Dissolve(0.25)
        ShakeUji

    voice "HIN_1472"
    hina "\"Uuuuugh.\""

    show hina 2 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1252"
    rin "\"Stop grumbling!\""

    show hina:
        "hina 2 lg school i" with Dissolve(0.25)
        ShakeNo

    voice "HIN_1473"
    hina "\"Uuuuugh!\""

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
