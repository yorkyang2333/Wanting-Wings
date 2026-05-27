label a04_comn_05:

    scene bg08aa with Dissolve(0.5)

    play sound se030a

    pause 3.0

    play music bgm01

    voice "2NO_0001"
    pa_system "\"Well, it's lunchtime on Christmas Eve Eve! How's everybody doing?\"" id a04_comn_05_9503214a

    voice "2NO_0002"
    pa_system "\"I've got a weather report for tomorrow, Christmas Eve: The rain just might turn to snow late at night~\"" id a04_comn_05_353d47e0

    voice "2NO_0003"
    pa_system "\"We might just be able to expect a romantic white Christmas this year!\"" id a04_comn_05_0992a4f2

    voice "2NO_0004"
    pa_system "\"Up next, Christmas E... ahem. Joy to the World.\"" id a04_comn_05_630222b6

    voice "2NO_0005"
    if persistent.dpatch:
        pa_system "\"Wait, there's no school today?! Tomorrow's the school day?!\"" id a04_comn_05_6c201493
    else:
        pa_system "\"Wait, there’s no class today?! Class is tomorrow?!\"" id a04_comn_05_b1516cdf

    "—Who was that?"

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_06
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_07
    else:
        jump a04_cou1_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
