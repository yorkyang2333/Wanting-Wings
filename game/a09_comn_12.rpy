label a09_comn_12:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    $ side_image = "miyako 1 side school_a_sei b"

    voice "2MI_0750"
    miyako "\"I didn't know which one I should pick, so I bought a bunch of different colored ribbons.\"" id a09_comn_12_96830676

    $ side_image = "fumi 1 side school_scarf a"

    voice "2FU_0670"
    fumi "\"You should try matching them with the wrapping paper and decide that way.\"" id a09_comn_12_95c6d0ca

    $ side_image = "miyako 2 side school_sei c"

    voice "2MI_0751"
    miyako "\"If this were Christmas, I could just pick green and red and not worry about it.\"" id a09_comn_12_a5bafeab

    $ side_image = "fumi 1 side school_scarf b"

    voice "2FU_0671"
    fumi "\"But you can wrap Valentine's chocolate however you want.\"" id a09_comn_12_076db5a1

    "Fumi and Miyako were on their way home from their trip to buy wrapping materials."

    stop music fadeout 1.0

    pause 0.5

    play music bgm05

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    show rin 2 sm school b:
        xcenter 332
    show hina 2 sm school d:
        xcenter 112
    with dict_dissolve_25

    play sound se521

    show miyako:
        "miyako 2 sm school_sei a flat"
        alpha 0.0 xcenter 792
        easein 0.75 alpha 1.0 xcenter 692
    show fumi:
        "fumi 1 sm school_scarf a flat"
        alpha 0.0 xcenter 1012
        easein 0.75 alpha 1.0 xcenter 912
    pause 1.25

    show miyako 2 sm school_sei a:
        alpha 1.0 xcenter 692
    show fumi 1 sm school_scarf a:
        alpha 1.0 xcenter 912
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "2RI_0813"
    rin "\"Hey, welcome back.\"" id a09_comn_12_3b38813c

    "Hina and Rin should have been back earlier than them, but they were still in their uniforms."

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "2FU_0672"
    fumi "\"Wait, where have you been?\"" id a09_comn_12_6cd8056e

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_0806"
    hina "\"Listen, Sachiko might stop managing the dorm.\"" id a09_comn_12_ec474636

    show miyako 2 sm school_sei a
    show fumi:
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2FU_0673"
    fumi "\"What?!\"" id a09_comn_12_b775d9e7

    show fumi 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show miyako 1 sm school_a_sei a with dict_dissolve_25

    voice "2MI_0752"
    miyako "\"Did she tell you that?\"" id a09_comn_12_453339e7

    show rin 1 sm school h with dict_dissolve_25

    voice "2RI_0814"
    rin "\"Umm, yeah. It sounds like she hasn't decided yet, though.\"" id a09_comn_12_8546f422

    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_0807"
    hina "\"When Rin and I got back to the dorm, Sachiko was talking to this lady we'd never seen before.\"" id a09_comn_12_048c3312

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_0808"
    hina "\"She was the manager before Sachiko, but she took a few years off of the job because of some health problems.\"" id a09_comn_12_880ce5dd

    show rin 1 sm school a with dict_dissolve_25

    voice "2RI_0815"
    rin "\"So Sachiko was only taking over for her in that time, and now that the old manager's feeling better, she came back to discuss taking the job back.\"" id a09_comn_12_f6f46246

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "2FU_0674"
    fumi "\"And Sachiko's going to quit?\"" id a09_comn_12_9163f879

    show rin:
        ShakeYes

    "Rin nodded."

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "2FU_0675"
    fumi "\"She didn't say she'd like to keep the job?\"" id a09_comn_12_06b6e1b8

    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_0809"
    hina "\"She wasn't really putting up a fight about it, no. We didn't hear the whole conversation, of course.\"" id a09_comn_12_ed52e6bf

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_0816"
    rin "\"I don't know what her contract's like or anything, but I'm guessing she doesn't have much say in it if she was just taking over temporarily.\"" id a09_comn_12_a5a47442

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "2FU_0676"
    fumi "\"I see... This is so sudden, though.\"" id a09_comn_12_2604eefd

    show rin 2 sm school e with dict_dissolve_25

    voice "2RI_0817"
    rin "\"At first I thought she'd pulled something and was getting chewed out about it.\"" id a09_comn_12_c2cb2302

    show hina 2 sm school e with dict_dissolve_25

    voice "2HI_0810"
    hina "\"...That would have been better.\"" id a09_comn_12_497868e7

    "They were joking, but there was no heart in it. Despite everything, Hina and Rin both really did like Sachiko."

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0753"
    miyako "\"Where is she now?\"" id a09_comn_12_dba4dac4

    "Miyako finally spoke after quietly listening all this time."

    show rin 1 sm school h with dict_dissolve_25

    voice "2RI_0818"
    rin "\"Umm, on the roof—\"" id a09_comn_12_77d70d5e

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0754"
    miyako "\"I'll go see what she has to say.\"" id a09_comn_12_1a0c0ea9

    hide miyako with dict_dissolve_50

    "She gave them a bright smile, then jogged over to the stairs."

    show hina 2 sm school d with dict_dissolve_25

    "The three girls all exchanged a glance at how calm Miyako appeared to be."

    show hina 2 sm school h with dict_dissolve_25

    voice "2HI_0811"
    hina "\"Even if she quits her job, she's not going to go anywhere, is she?\"" id a09_comn_12_87de2764

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_0819"
    rin "\"I mean... how would I know that?\"" id a09_comn_12_7caf4395

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "2FU_0677"
    fumi "\"...Miyako...\"" id a09_comn_12_41d2b6b3

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared >= 2:
        jump a09_cou4_04
    elif routes_cleared == 1:
        jump a09_comn_13
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
