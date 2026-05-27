label a01_comn_11:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_wind02
    pause 1.0

    $ side_image = "hina 2 side school i"

    voice "HIN_0238"
    hina "\"It's cold! It hurts!\"" id a01_comn_11_ddc1f986

    "A frigid wind was whipping at the girls, mercilessly blowing dead leaves against their exposed legs."

    $ side_image = "rin 1 side school d"

    voice "RIN_0195"
    rin "\"Hey, Rin, Asou! The weather's so nice today, so let's eat lunch outside!\"" id a01_comn_11_ac3d4463

    $ side_image = "hina 1 side school h"

    voice "HIN_0239"
    hina "\"I'm sorry, okay?! I didn't think the wind would be this bad!\"" id a01_comn_11_feb1d134

    $ side_image = "fumi 1 side school d"

    voice "FUM_0171"
    fumi "\"I don't think we'll be able to eat outside today... We don't want sand getting into our food.\"" id a01_comn_11_48b4c7dd

    $ side_image = "rin 1 side school b"

    voice "RIN_0196"
    rin "\"Guess we'll just have to go back to the class—\"" id a01_comn_11_f376bfda

    $ side_image = "hina 1 side school c"

    voice "HIN_0240"
    hina "\"Or there!\"" id a01_comn_11_5c39cf90

    "Hina was pointing at a building with a pointed roof adorned with a cross."

    $ side_image = "fumi 1 side school e"

    voice "FUM_0172"
    fumi "\"Umm... the chapel?\"" id a01_comn_11_138ff4ac

    $ side_image = "hina 2 side school a"

    voice "HIN_0241"
    hina "\"Yeah, it's closest. Let's head there.\"" id a01_comn_11_5d88a8a3

    $ side_image = "fumi 1 side school e"

    voice "FUM_0173"
    fumi "\"But—\"" id a01_comn_11_f71e3883

    $ side_image = "hina 1 side school c"

    voice "HIN_0242"
    hina "\"Full speed ahead!\"" id a01_comn_11_8cdd6eda

    play sound se128c

    "With that shout, Hina ran off toward the chapel."

    $ side_image = "rin 1 side school a"

    voice "RIN_0197"
    rin "\"Is it even open?\"" id a01_comn_11_9cc9975c

    $ side_image = "hina 1 side school c"

    voice "HIN_0243"
    hina "\"Iii dunnooo!\"" id a01_comn_11_f809af77

    "Hina was already far away."

    "Rin and Fumi exchanged a glance."

    $ side_image = "fumi 1 side school d"

    voice "FUM_0174"
    fumi "\"...Guess we should go after her.\"" id a01_comn_11_ea6365e6

    $ side_image = "rin 1 side school i"

    voice "RIN_0198"
    rin "\"...Guess so.\"" id a01_comn_11_3338135e

    scene white with bg_effect_11
    pause 0.5

    scene bg06aa with Dissolve(0.25)
    pause 1.25

    show hina 1 sm school a at pos_l2
    show rin 1 sm school a
    show fumi 1 sm school h at pos_r2
    with Dissolve(0.25)

    voice "FUM_0175"
    fumi "\"Do you think we'll get in trouble if someone sees us in here?\"" id a01_comn_11_efb2db43

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0244"
    hina "\"Well, it wasn't locked, so that means it's okay to go inside, right?\"" id a01_comn_11_4edbcc14

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0199"
    rin "\"Maybe, but I dunno if this is exactly the place for a carefree lunch.\"" id a01_comn_11_3c1cffc6

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0245"
    hina "\"Hey, the Bible says, 'Man shall not live by bread alone,' doesn't it?\"" id a01_comn_11_5827de35

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0200"
    rin "\"It does, but I'm not sure how that's relevant.\"" id a01_comn_11_4ab3d5b4

    show fumi 1 sm school k with dict_dissolve_25

    voice "FUM_0176"
    fumi "\"O Lord, please forgive us for eating lunch in the chapel.\"" id a01_comn_11_064606fc

    show hina 1 sm school h with dict_dissolve_25

    voice "HIN_0246"
    hina "\"Please forgive us.\"" id a01_comn_11_250cb5ac

    "Fumi folded her hands in prayer and Hina followed suit."

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0201"
    rin "\"Please punish only the little one who suggested the idea.\"" id a01_comn_11_9f6ca108

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0247"
    hina "\"What the heck?!\"" id a01_comn_11_fe7a6f40

    scene black with bg_effect_05
    pause 0.5

    scene bg06aa with bg_effect_05
    pause 0.5

    show hina 1 sm school c at pos_l2
    show rin 1 sm school c
    show fumi 1 sm school c at pos_r2
    with Dissolve(0.25)

    $ voice3("hina","HIN_0248","rin","RIN_0202","fumi","FUM_0177")
    hina_rin_fumi "\"Thank you for the food.\""

    show rin:
        "rin 1 sm school d" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0203"
    if persistent.dpatch:
        rin "\"Delicious as always. Now that I've tasted Asou's food, I can't go back to the cafeteria or the school store.\"" id a01_comn_11_0056cd98
    else:
        rin "\"Delicious as always. Now that I've tasted Asou's food, I can't go back to the cafeteria or the campus store.\"" id a01_comn_11_fcd5cc0c

    show rin 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0178"
    fumi "\"I appreciate the compliment.\"" id a01_comn_11_a11ac13a

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0249"
    hina "\"It's nice to eat somewhere different from usual, huh?\"" id a01_comn_11_9831d4b5

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0204"
    rin "\"Desperate to make up for your mistake, eh?\"" id a01_comn_11_0e63ea2e

    show hina 1 sm school h with dict_dissolve_25

    voice "HIN_0250"
    hina "\"Oh, shut it.\"" id a01_comn_11_ca8e2969

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0179"
    fumi "\"I think it's fun. There's a nice atmosphere in here, with the stained glass.\"" id a01_comn_11_242c0185

    voice "RIN_0205"
    rin "\"Yeah, the chapel's pretty famous for that, isn't it?\"" id a01_comn_11_70a2bf43

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0251"
    hina "\"Oh yeah, that's right! I've been in here a few times before, but this might be the first time I was able to get a really good look at it.\"" id a01_comn_11_fc456eb2

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0180"
    fumi "\"The design is of an angel. Isn't it so romantic?\"" id a01_comn_11_23ebfae9

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0252"
    hina "\"Maybe I should bring my camera sometime.\"" id a01_comn_11_69bd6319

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0181"
    fumi "\"Did you know they have weddings here sometimes?\"" id a01_comn_11_5ec4f42c

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0206"
    rin "\"Yeah, they let Seiyou graduates use it, right?\"" id a01_comn_11_61d7081c

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0253"
    hina "\"Do you want to get married here, Asou?\"" id a01_comn_11_b7a446c5

    show fumi:
        "fumi 1 sm school b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0182"
    fumi "\"That might be nice. I'll have to find someone first, of course.\"" id a01_comn_11_f3c47660

    show fumi 1 sm school b:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school c with dict_dissolve_25

    voice "HIN_0254"
    hina "\"I get the feeling you won't have much trouble with that.\"" id a01_comn_11_bb1448d2

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0183"
    fumi "\"Ahaha, you think so?\"" id a01_comn_11_4f4f2d5f

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_0207"
    rin "\"I'll marry Asou, and we'll keep Hina as our pet! That's my ideal life!\"" id a01_comn_11_48522df7

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0255"
    hina "\"As a what?!\"" id a01_comn_11_edf5d424

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0184"
    fumi "\"I think I wouldn't mind having an energetic kid like Natsume.\"" id a01_comn_11_189e5ce7

    show hina:
        "hina 1 sm school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0256"
    hina "\"A kid?!\"" id a01_comn_11_3134bf14

    show hina 1 sm school l:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 sm school f" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 662

    voice "RIN_0208"
    rin "\"Ah~ Mommy and Daddy have stuff to do, so go to bed, kiddo.\"" id a01_comn_11_bbc8ddce

    show rin 1 sm school f:
        xcenter 662
    with None

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0257"
    hina "\"Don't joke like that in the middle of the day! And here, of all places!\"" id a01_comn_11_bb8b5353

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
