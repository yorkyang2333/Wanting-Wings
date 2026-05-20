label a01_comn_11:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_wind02
    pause 1.0

    $ side_image = "hina 2 side school i"

    voice "HIN_0238"
    hina "\"It's cold! It hurts!\""

    "A frigid wind was whipping at the girls, mercilessly blowing dead leaves against their exposed legs."

    $ side_image = "rin 1 side school d"

    voice "RIN_0195"
    rin "\"Hey, Rin, Asou! The weather's so nice today, so let's eat lunch outside!\""

    $ side_image = "hina 1 side school h"

    voice "HIN_0239"
    hina "\"I'm sorry, okay?! I didn't think the wind would be this bad!\""

    $ side_image = "fumi 1 side school d"

    voice "FUM_0171"
    fumi "\"I don't think we'll be able to eat outside today... We don't want sand getting into our food.\""

    $ side_image = "rin 1 side school b"

    voice "RIN_0196"
    rin "\"Guess we'll just have to go back to the class—\""

    $ side_image = "hina 1 side school c"

    voice "HIN_0240"
    hina "\"Or there!\""

    "Hina was pointing at a building with a pointed roof adorned with a cross."

    $ side_image = "fumi 1 side school e"

    voice "FUM_0172"
    fumi "\"Umm... the chapel?\""

    $ side_image = "hina 2 side school a"

    voice "HIN_0241"
    hina "\"Yeah, it's closest. Let's head there.\""

    $ side_image = "fumi 1 side school e"

    voice "FUM_0173"
    fumi "\"But—\""

    $ side_image = "hina 1 side school c"

    voice "HIN_0242"
    hina "\"Full speed ahead!\""

    play sound se128c

    "With that shout, Hina ran off toward the chapel."

    $ side_image = "rin 1 side school a"

    voice "RIN_0197"
    rin "\"Is it even open?\""

    $ side_image = "hina 1 side school c"

    voice "HIN_0243"
    hina "\"Iii dunnooo!\""

    "Hina was already far away."

    "Rin and Fumi exchanged a glance."

    $ side_image = "fumi 1 side school d"

    voice "FUM_0174"
    fumi "\"...Guess we should go after her.\""

    $ side_image = "rin 1 side school i"

    voice "RIN_0198"
    rin "\"...Guess so.\""

    scene white with bg_effect_11
    pause 0.5

    scene bg06aa with Dissolve(0.25)
    pause 1.25

    show hina 1 sm school a at pos_l2
    show rin 1 sm school a
    show fumi 1 sm school h at pos_r2
    with Dissolve(0.25)

    voice "FUM_0175"
    fumi "\"Do you think we'll get in trouble if someone sees us in here?\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0244"
    hina "\"Well, it wasn't locked, so that means it's okay to go inside, right?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0199"
    rin "\"Maybe, but I dunno if this is exactly the place for a carefree lunch.\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0245"
    hina "\"Hey, the Bible says, 'Man shall not live by bread alone,' doesn't it?\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0200"
    rin "\"It does, but I'm not sure how that's relevant.\""

    show fumi 1 sm school k with dict_dissolve_25

    voice "FUM_0176"
    fumi "\"O Lord, please forgive us for eating lunch in the chapel.\""

    show hina 1 sm school h with dict_dissolve_25

    voice "HIN_0246"
    hina "\"Please forgive us.\""

    "Fumi folded her hands in prayer and Hina followed suit."

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0201"
    rin "\"Please punish only the little one who suggested the idea.\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0247"
    hina "\"What the heck?!\""

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
        rin "\"Delicious as always. Now that I've tasted Asou's food, I can't go back to the cafeteria or the campus store.\""

    show rin 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0178"
    fumi "\"I appreciate the compliment.\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0249"
    hina "\"It's nice to eat somewhere different from usual, huh?\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0204"
    rin "\"Desperate to make up for your mistake, eh?\""

    show hina 1 sm school h with dict_dissolve_25

    voice "HIN_0250"
    hina "\"Oh, shut it.\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0179"
    fumi "\"I think it's fun. There's a nice atmosphere in here, with the stained glass.\""

    voice "RIN_0205"
    rin "\"Yeah, the chapel's pretty famous for that, isn't it?\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0251"
    hina "\"Oh yeah, that's right! I've been in here a few times before, but this might be the first time I was able to get a really good look at it.\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0180"
    fumi "\"The design is of an angel. Isn't it so romantic?\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0252"
    hina "\"Maybe I should bring my camera sometime.\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0181"
    fumi "\"Did you know they have weddings here sometimes?\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0206"
    rin "\"Yeah, they let Seiyou graduates use it, right?\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0253"
    hina "\"Do you want to get married here, Asou?\""

    show fumi:
        "fumi 1 sm school b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0182"
    fumi "\"That might be nice. I'll have to find someone first, of course.\""

    show fumi 1 sm school b:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school c with dict_dissolve_25

    voice "HIN_0254"
    hina "\"I get the feeling you won't have much trouble with that.\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0183"
    fumi "\"Ahaha, you think so?\""

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_0207"
    rin "\"I'll marry Asou, and we'll keep Hina as our pet! That's my ideal life!\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0255"
    hina "\"As a what?!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0184"
    fumi "\"I think I wouldn't mind having an energetic kid like Natsume.\""

    show hina:
        "hina 1 sm school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0256"
    hina "\"A kid?!\""

    show hina 1 sm school l:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 sm school f" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 662

    voice "RIN_0208"
    rin "\"Ah~ Mommy and Daddy have stuff to do, so go to bed, kiddo.\""

    show rin 1 sm school f:
        xcenter 662
    with None

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0257"
    hina "\"Don't joke like that in the middle of the day! And here, of all places!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
