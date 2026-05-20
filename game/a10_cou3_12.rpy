label a10_cou3_12:

    scene white with Dissolve(0.5)
    pause 2.0

    "—A few weeks later."

    pause 0.5

    play music bgm06 fadein 1.0

    scene kimikara_22_a with Dissolve(2.0)

    voice "2FU_1287"
    fumi "\"Oh, this picture is so cool!\""

    voice "2RI_1694"
    rin "\"......\""

    voice "2FU_1288RE"
    fumi "\"Your face is small, and your legs are so long. You really do have a great figure, Rin.\""

    voice "2RI_1695"
    rin "\"......\""

    voice "2FU_1289"
    fumi "\"You don't want to look?\""

    voice "2RI_1696"
    rin "\"...I don't.\""

    voice "2FU_1290"
    fumi "\"Oh, wow, this lipstick picture is great! Hey, I've never seen you with such a mysterious look on your face, Rin.\""

    voice "2RI_1697"
    rin "\"They just turned a light on me all of a sudden, so I'm surprised in that one...\""

    voice "2FU_1291"
    fumi "\"Pfft.\""

    "The magazine Fumi was excitedly reading was, naturally, the one containing Rin's debut as a model."

    "It was a magazine aimed at working women in their 20s, but the tall, mature-looking Rin fit in with the other models with no issue."

    "Fumi had been so excited for this magazine that she put a mark on her calendar on the day it was releasing, and she had, of course, bought three copies: one for reading, one to keep in mint condition, and one to show people."

    if persistent.dpatch:
        "And now, after breaking the seal on her way home from school, she was giving it a thorough check." id a10_cou3_12_8f18af4f
    else:
        "And now, after breaking the seal on her way home from class, she was giving it a thorough check."

    "As for Rin, she had started clinging to Fumi a little while ago, pouting."

    voice "2RI_1698"
    rin "\"I'm not doing that again... It's super embarrassing trying to make expressions for the pictures.\""

    voice "2FU_1292"
    fumi "\"You think so? The president had nothing but good things to say about you, though.\""

    voice "2RI_1699"
    rin "\"...Like what?\""

    voice "2FU_1293"
    fumi "\"She said there are plenty of girls with nice faces and figures, but you're really good at showing listlessness and anxiety. She said you've got a genius talent for subtle nuance in your expressions.\""
    "...I don't think that's talent. I think that's just how she is."

    voice "2RI_1700"
    rin "\"I don't care about that, but I'm your girlfriend, so I'll think about it if it would make you happy.\""

    voice "2FU_1294"
    fumi "\"I'm very happy having such a cute girlfriend♪\""

    scene kimikara_22_b with Dissolve(0.5)

    "Fumi was much more excited than Rin, who was merely clinging to her like a child."

    "She fussed, complaining about how embarrassing it was, but when her girlfriend complimented her, she didn't seem too opposed to it."

    voice "2FU_1295"
    fumi "\"She said the next shoot would be next week, and it'll be swimsuits.\""

    voice "2RI_1701"
    rin "\"Wait! Bikinis in the middle of winter?!\""

    window hide

    $ persistent.fumi_rin_clear2 = True
    if sum([bool(persistent.hina_fumi_clear2),bool(persistent.rin_hina_clear2),bool(persistent.fumi_rin_clear2)]) == 3 and persistent.kimikara_menu_status == 0:
        $ persistent.kimikara_menu_status = 1
    $ renpy.block_rollback()

    pause 1.0
    scene ed2_c00 with Dissolve(0.75)
    pause 2.25
    show ed2_c01 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 3.0

    scene white with Dissolve(0.75)
    pause 2.25

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 2.5

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
