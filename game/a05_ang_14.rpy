label a05_ang_14:

    scene white with Dissolve(0.5)
    pause 1.5

    scene ev03f with Dissolve(0.375)
    pause 2.125

    voice "SYO_0228"
    sachiko "\"Come on, come to my room. I've got cake. It's my birthday today, too.\"" id a05_ang_14_b0b74a89

    window hide

    $ persistent.angel_clear = True
    $ renpy.block_rollback()

    pause 1.0
    scene ed_d00 with Dissolve(0.75)
    pause 2.25
    show ed_d01 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 3.0



    scene ed_d02 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    $ persistent.game = None
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
