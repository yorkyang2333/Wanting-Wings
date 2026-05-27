label a10_cou2_08:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    $ side_image = "rin 1 side school_scarf h"

    voice "2RI_1369"
    rin "\"......\"" id a10_cou2_08_c54683ec

    "Rin seemed to have an idea where Hina could be. Her long legs strode purposefully toward that location."

    "She was headed for the chapel, naturally."

    play sound woodendoor
    pause 0.5

    scene bg06ba with Dissolve(0.375)
    pause 1.125

    $ side_image = "rin 2 side school_scarf a"

    voice "2RI_1370"
    rin "\"......\"" id a10_cou2_08_7a2512ba

    "The door flew open, and she took a look around the building."

    $ side_image = "rin 1 side school_scarf h"

    voice "2RI_1371"
    rin "\"...!\"" id a10_cou2_08_47029503

    play music bgm08

    "Just as she expected, in the back of the chapel, she could see a shadow moving behind the pulpit."

    show rin 1 lg school_scarf h with dict_dissolve_25

    voice "2RI_1372"
    rin "\"Hina, listen to me.\"" id a10_cou2_08_a9f48be2

    "Rin took a deep breath and called out to the shadow."

    voice "2RI_1373"
    rin "\"You don't need to come out, just listen from there. Though I really wanted to say this face-to-face.\"" id a10_cou2_08_41eba392

    "She started speaking more quietly than she had on Christmas."

    show rin 2 lg school_scarf a with dict_dissolve_25

    voice "2RI_1374"
    rin "\"Feeling affection from someone is amazing. It can make you feel happier than anything else.\"" id a10_cou2_08_4b2d1c4a

    voice "2RI_1375"
    rin "\"And you're so free with your affection, Hina. You show it in your words, your actions, it pours from you like a fountain.\"" id a10_cou2_08_f83dff5d

    show rin 2 lg school_scarf b with dict_dissolve_25

    voice "2RI_1376"
    rin "\"But like any spoiled fool, I got used to it quickly. I started taking your affection for granted. In only a month!\"" id a10_cou2_08_f9da4dcb

    show rin 2 lg school_scarf d with dict_dissolve_25

    voice "2RI_1377"
    rin "\"And I only took, even though I should have been giving, too.\"" id a10_cou2_08_3c2a7e6a

    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1378"
    rin "\"But it's... it's hard. Not for you; you're so brave. But I'm a coward.\"" id a10_cou2_08_42254158

    show rin 2 lg school_scarf d with dict_dissolve_25

    voice "2RI_1379"
    rin "\"But... that's just an excuse.\"" id a10_cou2_08_bfcbf91f

    show rin 2 lg school_scarf b with dict_dissolve_25

    voice "2RI_1380"
    rin "\"I don't just belong to myself anymore. I need to change, for the only person who could love someone like me.\"" id a10_cou2_08_b87cd3c6

    "She slowly stepped forward."

    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1381"
    rin "\"I was also... scared of how you were changing. I never imagined how affectionate you'd get.\"" id a10_cou2_08_fb4e67c0

    show rin 1 lg school_scarf b with dict_dissolve_25

    voice "2RI_1382"
    rin "\"I've always been afraid of other people changing on me.\"" id a10_cou2_08_e42d698b

    show rin 1 lg school_scarf a with dict_dissolve_25

    voice "2RI_1383"
    rin "\"But when I started going out with you, I became even more scared of how I could change other people.\"" id a10_cou2_08_5f3f1c3b

    show rin 1 lg school_scarf h with dict_dissolve_25

    voice "2RI_1384"
    rin "\"Changing another person with my actions... That responsibility is the 'heaviness' I was really feeling.\"" id a10_cou2_08_390ee6d9

    "Rin put her arms around something unseen."

    show rin 2 lg school_scarf a with dict_dissolve_25

    voice "2RI_1385"
    rin "\"...But I think that's just what love is. It's not like we're an exception.\"" id a10_cou2_08_46e5e992

    show rin 2 lg school_scarf d with dict_dissolve_25

    voice "2RI_1386"
    rin "\"I'm still scared of myself or someone else changing, but I'm more scared of being alone.\"" id a10_cou2_08_28626554

    show rin 1 lg school_scarf a with dict_dissolve_25

    voice "2RI_1387"
    rin "\"So can we please just...\"" id a10_cou2_08_ce4fb798

    play sound se_2s_f015

    stop music fadeout 1.0

    show rin:
        ShakeTameiki

    "Rin took the collar out of her pocket."

    show rin 1 lg school_scarf h:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2RI_1388"
    rin "\"Come!\"" id a10_cou2_08_68346d1c

    "Her voice echoed through the chapel."

    "........."

    "The shadow shuffled out from behind the pulpit."

    show rin 1 lg school_scarf c with dict_dissolve_25

    voice "2RI_1389"
    rin "\"I'm not mad...\"" id a10_cou2_08_e3aef2b8

    "Rin called Hina soothingly."

    play sound se_2s_g010

    show rin:
        "rin 1 lg school_scarf e" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1390"
    rin "\"Huh?!\"" id a10_cou2_08_a2f0082c

    show rin 1 lg school_scarf e:
        xoffset 0 yoffset 0
    with None

    "The shadow leapt out and, like a cannonball, barreled down the aisle and crashed into Rin."

    play sound se_2s_h002

    hide rin with Dissolve(0.25)

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side school_scarf j"

    voice "2RI_1391"
    rin "\"Waaah!\"" id a10_cou2_08_8a879828

    camera
    with None

    "Rin fell down as the ball of fur collided with her."

    $ side_image = "rin 2 side school_scarf e"

    voice "2RI_1392"
    rin "\"Hey, be careful... I-Isn't this a little sudden? Geez, you're so furry...\"" id a10_cou2_08_58e0c91a

    $ side_image = "rin 1 side school_scarf j"

    voice "2RI_1393"
    rin "\"Furry?!\"" id a10_cou2_08_879f9c19

    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff!\"" id a10_cou2_08_f64a2b55_1

    play music bgm01 fadein 1.0

    "The identity of the furball was revealed."

    $ side_image = "rin 1 side school_scarf e"

    voice "2RI_1394"
    rin "\"A-Arthur?!\"" id a10_cou2_08_4baf50e2

    "The shadow Rin had been talking to, that she'd thought was Hina, was actually the Asous' dog, Arthur."

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side school_scarf j"

    voice "2RI_1395"
    rin "\"W-Wait... Don't lick me so much! Aaaah, stop panting! S-Stay, stay~!\"" id a10_cou2_08_dc1d0926

    camera
    with None

    "Arthur was merely excited and playing, but Rin was finding it difficult to escape from directly under him."

    voice "2HI_1396"
    hina "\"Stay! Down!\"" (show_name="???") id a10_cou2_08_f3a54153

    "Two sharp commands came from the back of the chapel."

    "Arthur quickly leapt off of Rin and lay down on the floor, waiting."

    $ side_image = "rin 1 side school_scarf e"

    voice "2RI_1396"
    rin "\"...?!\"" id a10_cou2_08_e912fb10

    "Freed from his weight, Rin managed to sit up and turn to the source of the voice."

    "A small figure walked in, backlit by the sunlight streaming in from the door."

    pause 0.5

    scene white with bg_effect_05
    pause 1.0

    scene bg06ba with bg_effect_05
    pause 0.5

    show hina 2 lg school_scarf a with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "2HI_1397"
    hina "\"Good boy, Arthur.\"" id a10_cou2_08_ba4ac66a

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina petted Arthur's back for his show of obedience."

    $ side_image = "rin 1 side school_scarf i"

    voice "2RI_1397"
    rin "\"Where were you, Hina? What were you doing, Hina? What's going on, Hina?\"" id a10_cou2_08_78792ac9

    "Rin threw a barrage of questions."

    show hina 1 lg school_scarf e with dict_dissolve_25

    voice "2HI_1398"
    hina "\"Stop saying my name. Just get up. Are we gonna do this with you sitting on the floor?\"" id a10_cou2_08_db73c455

    $ side_image = "rin 1 side school_scarf h"

    voice "2RI_1398"
    rin "\"Oh... right.\"" id a10_cou2_08_4ed88246

    hide hina with Dissolve(0.5)
    pause 0.5

    show hina z4 1 lg school_scarf a:
        xcenter 298
    show rin z4 1 lg school_scarf i:
        xcenter 726
    with Dissolve(0.25)

    voice "2HI_1399"
    hina "\"I was looking for Arthur. I got a call from Asou—\"" id a10_cou2_08_09b06e90

    show rin:
        "rin z4 1 lg school_scarf j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_1399"
    rin "\"That's right! Arthur! What are you doing here?!\"" id a10_cou2_08_82183c2e

    show rin z4 1 lg school_scarf j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff?\"" id a10_cou2_08_f64a2b55_1

    show hina z4 1 lg school_scarf f with dict_dissolve_25

    voice "2HI_1400"
    hina "\"Just listen! I'll explain!\"" id a10_cou2_08_b72b7be2

    show rin z4 1 lg school_scarf i with dict_dissolve_25

    voice "2RI_1400"
    rin "\"Oh, right.\"" id a10_cou2_08_fc983403

    show hina z4 1 lg school_scarf e with dict_dissolve_25

    voice "2HI_1401"
    hina "\"I got a call from Asou that she took her eyes off of him for a second and he ran off, and the store was just getting busy, so she couldn't chase after him.\"" id a10_cou2_08_d8c12682

    show rin z4 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1401"
    rin "\"So she asked you to look for him? Wouldn't it be a pretty huge range you'd have to search?\"" id a10_cou2_08_dcc18b9d

    show hina z4 2 lg school_scarf d with dict_dissolve_25

    voice "2HI_1402"
    if persistent.dpatch:
        hina "\"No, she just asked me to look inside school grounds.\"" id a10_cou2_08_17f8a5d2
    else:
        hina "\"No, she just asked me to look on campus grounds.\"" id a10_cou2_08_83607d9e

    show rin z4 1 lg school_scarf i with dict_dissolve_25

    voice "2RI_1402"
    rin "\"Why? Isn't this pretty far from the store? We're up on a mountain, too.\"" id a10_cou2_08_27970136

    show hina z4 2 lg school_scarf f with dict_dissolve_25

    voice "2HI_1403"
    hina "\"According to Asou, Arthur's really taken a liking to you and me.\"" id a10_cou2_08_2d86a0eb

    show rin z4 2 lg school_scarf b with dict_dissolve_25

    voice "2RI_1403"
    rin "\"Is that true, boy?\"" id a10_cou2_08_01308777

    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff!\"" id a10_cou2_08_f64a2b55_1

    "It seemed to be an affirmative."

    show hina z4 1 lg school_scarf e with dict_dissolve_25

    voice "2HI_1404"
    hina "\"She thought he might have come here.\"" id a10_cou2_08_b4e44e84

    show rin z4 2 lg school_scarf a with dict_dissolve_25

    voice "2RI_1404"
    rin "\"And she was right.\"" id a10_cou2_08_78c572cf

    show hina:
        "hina z4 1 lg school_scarf a" with Dissolve(0.25)
        ShakeYes

    voice "2HI_1405"
    hina "\"Yeah. She called during lunch, and I thought I saw him while I was on the phone with her, so I ran after him—\"" id a10_cou2_08_4224cf57

    show hina z4 1 lg school_scarf a:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school_scarf h with dict_dissolve_25

    voice "2RI_1405"
    rin "\"...Can you tell me when you do stuff like this?\"" id a10_cou2_08_258bfd85

    show hina z4 2 lg school_scarf h with dict_dissolve_25

    voice "2HI_1406"
    hina "\"Sorry... I got kind of wrapped up in it.\"" id a10_cou2_08_3a38f447

    show rin z4 1 lg school_scarf g with dict_dissolve_25

    voice "2RI_1406"
    rin "\"It's fine... I just thought you'd run away again.\"" id a10_cou2_08_8f728625

    show hina z4 2 lg school_scarf f with dict_dissolve_25

    voice "2HI_1407"
    if persistent.dpatch:
        hina "\"Of course not. We were supposed to talk after school.\"" id a10_cou2_08_04ffdd07
    else:
        hina "\"Of course not. We were supposed to talk after class.\"" id a10_cou2_08_5f36d9d6

    show rin z4 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1407"
    rin "\"R-Right... we are, aren't we?\"" id a10_cou2_08_24616ecb

    show hina z4 2 lg school_scarf d with dict_dissolve_25

    voice "2HI_1408"
    hina "\"You should believe in my feelings for you more.\"" id a10_cou2_08_980bbcae

    show rin z4 2 lg school_scarf d with dict_dissolve_25

    voice "2RI_1408"
    rin "\"...Yeah.\"" id a10_cou2_08_488ac8f4

    "As always, she'd had the tables turned on her instantly."

    show rin z4 1 lg school_scarf i with dict_dissolve_25

    voice "2RI_1409"
    rin "\"...So how much did you hear?\"" id a10_cou2_08_9bbf89aa

    show hina z4 2 lg school_scarf b with dict_dissolve_25

    voice "2HI_1409"
    hina "\"I saw you coming this way and ran after you, so... all of it, I think.\"" id a10_cou2_08_0b7dd70d

    show rin:
        "rin z4 1 lg school_scarf g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1410"
    rin "\"Ugh... It's the same as before.\"" id a10_cou2_08_88044f71

    show rin z4 1 lg school_scarf g with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
