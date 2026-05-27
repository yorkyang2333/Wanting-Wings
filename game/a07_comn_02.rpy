label a07_comn_02:

    scene black with Dissolve(0.5)
    pause 1.5

    "—Christmas Eve."

    play sound se521
    pause 0.5

    voice "2SA_0042"
    sachiko "\"Chaaarge!!\"" (show_name="???") id a07_comn_02_28a83c3e

    play sound [se585,se585]
    pause 0.3
    play sound2 [se585,se585]

    "The door crashed open and there was a series of deafening pops."

    scene white with Dissolve(0.05)
    pause 0.15


    if route2 == 1:
        scene bg01cg
    else:
        scene bg01ch

    show ef_cloud_01:
        alpha 0.6
    with Dissolve(0.25)
    pause 0.75

    $ side_image = "fumi 1 side pyjama j"

    voice "2FU_0031"
    fumi "\"Aaah?!\"" id a07_comn_02_a0a1661f

    $ side_image = "hina 1 side pyjama l"

    voice "2HI_0048"
    hina "\"What's going on?!\"" id a07_comn_02_02685b72

    show sachiko behind ef_cloud_01:
        "sachiko_1_sm_outfit_black"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    voice "2SA_0043"
    sachiko "\"Merry Christmas!! This room is now under the control of the armed group 'December Christmas'!\"" (show_name="???") id a07_comn_02_7fccf4fd

    "The only one who would do something like this was, of course..."

    show sachiko 1 sm outfit g behind ef_cloud_01 with dict_dissolve_50

    $ side_image = "fumi 1 side pyjama e"

    voice "2FU_0032"
    fumi "\"Sachiko...?!\"" id a07_comn_02_8f004b3e

    "Sachiko fired her weapons—several party poppers held skillfully between fingers."

    play sound [se585,se585]
    pause 0.3
    play sound2 [se585,se585]

    hide sachiko with dict_dissolve_25

    $ side_image = "hina 1 side pyjama l"

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2HI_0049"
    hina "\"Waaah?!\"" id a07_comn_02_eefba0e4

    camera
    with None

    "This time, the popping came from a different direction."

    show bg_obi behind ef_cloud_01 with Dissolve(0.5)

    show rin behind ef_cloud_01:
        "rin 2 lg pyjama a flat"
        alpha 0.0 xcenter 512
        linear 0.25 alpha 1.0 xcenter 772

    voice "2RI_0046"
    rin "\"Like hell!\"" id a07_comn_02_e38d212f

    show rin 2 lg pyjama a behind ef_cloud_01 with None

    "It was Rin. She scooped up popper after popper from the floor, pulling their strings one by one."

    show sachiko 1 sm outfit h behind ef_cloud_01, bg_obi at pos_l

    voice "2SA_0044"
    sachiko "\"I thought it was just civilians here!\"" id a07_comn_02_3d0bae96

    show rin 1 lg pyjama f with dict_dissolve_25

    voice "2RI_0047"
    rin "\"Yippee ki-yay, motherfucker!\"" id a07_comn_02_c5567750

    play sound [se585,se585]
    pause 0.3
    play sound2 [se585,se585]

    "The firefight(?) between terrorist and policeman had filled the room with smoke."

    $ side_image = "hina 1 side pyjama f"

    voice "2HI_0050"
    hina "\"Shut uuup!!\"" id a07_comn_02_362c0a60

    "Wrath of the RA."

    play music bgm01

    $ side_image = "hina 1 side pyjama g"

    voice "2HI_0051"
    hina "\"You two are officially way too into party poppers!\"" id a07_comn_02_e7b495de

    show sachiko 1 sm outfit g
    show rin 1 lg pyjama c
    with dict_dissolve_25

    $ voice2("sachiko","2SA_0045","rin","2RI_0048N")
    rin_sachiko "\"Can't argue with that.\""

    hide bg_obi
    hide sachiko
    hide rin
    with Dissolve(0.5)

    show fumi 1 sm pyjama h behind ef_cloud_01 at pos_ls
    show hina 1 sm pyjama d behind ef_cloud_01 at pos_rs
    with Dissolve(0.25)

    voice "2HI_0052"
    hina "\"Seriously! You're going to bother our neighbors! Aaah... There's streamers on the cake...\"" id a07_comn_02_ab1f4bf9

    show fumi:
        ShakeYes2

    voice "2FU_0033"
    fumi "\"Cough, cough... Hm?\"" id a07_comn_02_c075d268

    scene white with bg_effect_11
    pause 0.5

    scene bg02ca
    show miyako 1 sm school_a a
    show ef_cloud_01:
        alpha 0.6
    with Dissolve(0.25)
    pause 0.75

    show ef_cloud_01:
        alpha 0.6
        linear 3.0 alpha 0.0

    "Beyond the slowly dissipating smoke, a girl stood in the doorway."

    hide ef_cloud_01 with None

    "She was wearing the Seiyou uniform, but she wasn't in their class or their dorm. Fumi had never seen her face before."

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0034"
    fumi "\"Umm... who's this?\"" id a07_comn_02_dae8b66c

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0003"
    miyako "\"......\"" (show_name="???") id a07_comn_02_8b568918

    "The girl smiled meekly in response to Fumi's timid question."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0046"
    sachiko "\"That's Miyako. I came to introduce her.\"" id a07_comn_02_45bd7332

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0035"
    fumi "\"Miyako...?\"" id a07_comn_02_4ee358f8

    $ side_image = "side/hina_rin_[rin_pyjama]_sozai01.webp"

    $ voice2("hina","2HI_0053N","rin","2RI_0049")
    hina_rin "\"Who?\""

    voice "2MI_0004"
    miyako "\"......\"" (show_name="???") id a07_comn_02_8930f00d

    "The girl merely continued to smile."

    scene white with Dissolve(0.1875)
    pause 1.0625

    scene kimikara_03_a with Dissolve(0.25)
    pause 0.75

    voice "2SA_0047"
    sachiko "\"Miyako Takaoka. She's my cousin.\"" id a07_comn_02_1d741f15

    $ side_image = "rin 1 side pyjama e"

    voice "2RI_0050"
    rin "\"Cousin? Not niece?\"" id a07_comn_02_83a52be6

    voice "2SA_0048"
    sachiko "\"Hey, what's that supposed to mean?\"" id a07_comn_02_4c5bb65f

    $ side_image = "rin 1 side pyjama f"

    voice "2RI_0051"
    rin "\"Just wondering about the age difference, I guess...\"" id a07_comn_02_0977b636

    voice "2SA_0049"
    sachiko "\"F-Five years...\"" id a07_comn_02_337e6682

    $ side_image = "hina 1 side pyjama j"

    voice "2HI_0054"
    hina "\"......\"" id a07_comn_02_770f3609

    scene kimikara_03_c with Dissolve(0.5)

    voice "2SA_0050"
    sachiko "\"She's pretty, just like me, right?\"" id a07_comn_02_19aefc89

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0036"
    fumi "\"You don't really look that alike...\"" id a07_comn_02_e665509c

    voice "2SA_0051"
    sachiko "\"Hey, what's that supposed to mean?\"" id a07_comn_02_c779f722

    $ side_image = "fumi 2 side pyjama d"

    voice "2FU_0037"
    fumi "\"Ah, oh, just that you have different looks!\"" id a07_comn_02_d2b4ef8e

    voice "2SA_0052"
    sachiko "\"Well, it's just on paper. We're not actually related by blood.\"" id a07_comn_02_99b65bde

    $ side_image = "hina 1 side pyjama j"

    voice "2HI_0055"
    hina "\"So why'd you say you look alike?\"" id a07_comn_02_d360cb1c

    voice "2SA_0053"
    sachiko "\"Oh, just a whim, I guess. Come on, Miyako, introduce yourself.\"" id a07_comn_02_6666540f

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0052"
    rin "\"Unique as always.\"" id a07_comn_02_6c362147

    voice "2MI_0005"
    miyako "\"......\"" id a07_comn_02_9f0c0aed

    "Meanwhile, Miyako still had a blank look on her face. It was like she didn't even realize they were talking about her."

    voice "2SA_0054"
    sachiko "\"Miyako?\"" id a07_comn_02_8650da38

    "Sachiko shook her shoulder."

    scene kimikara_03_d with Dissolve(0.25)
    pause 0.75

    voice "2MI_0006"
    miyako "\"Oh, right.\"" id a07_comn_02_0c1848c1

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0038"
    fumi "\"?\"" id a07_comn_02_03bfce65

    voice "2SA_0055"
    sachiko "\"Ah, Miyako's been abroad for a while.\"" id a07_comn_02_b85000c4

    "Hm, insurance."

    $ side_image = "rin 2 side pyjama g"

    voice "2RI_0053"
    rin "\"Huh~\"" id a07_comn_02_6c811d90

    $ side_image = "hina 2 side pyjama b"

    voice "2HI_0056"
    hina "\"G-Guten Morgen?\"" id a07_comn_02_70f589c5

    scene kimikara_03_c with Dissolve(0.25)
    pause 0.75

    voice "2MI_0007"
    miyako "\"Japanese is just fine.\"" id a07_comn_02_f690e272

    $ side_image = "hina 2 side pyjama g"

    voice "2HI_0057"
    hina "\"Oh, good~\"" id a07_comn_02_ad86484c

    $ side_image = "rin 1 side pyjama k"

    voice "2RI_0054"
    rin "\"It's night, hon.\"" id a07_comn_02_6259d0ec

    scene kimikara_03_a with Dissolve(0.25)
    pause 0.75

    voice "2SA_0056"
    sachiko "\"Aaanyyywaaay. She'll be your new roommate starting today!\"" id a07_comn_02_e97eefe8

    $ side_image = "side/hina_fumi_rin_[rin_pyjama]_sozai01.webp"

    $ voice3("hina","2HI_0058","rin","2RI_0055","fumi","2FU_0039")
    hina_rin_fumi "\"Huuuh?!\""

    scene kimikara_03_b with Dissolve(0.25)
    pause 0.75

    voice "2MI_0008"
    miyako "\"Huh?\"" id a07_comn_02_0ea21896

    "The sudden announcement surprised not only the three of them but Miyako, too."

    voice "2MI_0009"
    miyako "\"You didn't tell me I'd be moving in today...\"" id a07_comn_02_796abf25

    scene kimikara_03_d with Dissolve(0.25)
    pause 0.75

    voice "2SA_0057"
    sachiko "\"Didn't I?\"" id a07_comn_02_af14acd1

    "Miyako shook her head."

    $ side_image = "hina 1 side pyjama h"

    voice "2HI_0059"
    hina "\"You're so irresponsible.\"" id a07_comn_02_046ea15e

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0040"
    fumi "\"Well, we do have an extra bed...\"" id a07_comn_02_28708f96

    $ side_image = "rin 1 side pyjama h"

    voice "2RI_0056"
    rin "\"You've gotta give us some warning before springing a whole other roommate on us.\"" id a07_comn_02_3bb74ec7

    $ side_image = "hina 1 side pyjama e"

    voice "2HI_0060"
    hina "\"But if we don't take her in, she'll have to live with Sachiko.\"" id a07_comn_02_2b7810e6

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0057"
    rin "\"...Good point. We're happy to have you.\"" id a07_comn_02_c0fcdf7d

    voice "2SA_0058"
    sachiko "\"Just how little do you trust me?!\"" id a07_comn_02_c19db853

    voice "2MI_0010"
    miyako "\"But I don't have any...\"" id a07_comn_02_b10afa03

    "Miyako herself seemed to be the most hesitant of them."

    voice "2SA_0059"
    sachiko "\"You'll be fine. I've got a toothbrush, towel, school supplies, everything you'll need for now, all ready for you.\"" id a07_comn_02_982e7076

    voice "2SA_0060"
    sachiko "\"Oh, but I didn't know your underwear size, so I'll give you some money and you'll have to go buy some tomorrow.\"" id a07_comn_02_ecbda94b

    voice "2MI_0011"
    miyako "\"Okay...\"" id a07_comn_02_7cf11f46

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0041"
    fumi "\"Oh, do you have pajamas?\"" id a07_comn_02_fe475024

    "She couldn't very well sleep in her uniform."

    voice "2MI_0012"
    miyako "\"All I have is this and a coat...\"" id a07_comn_02_e617638b

    voice "2SA_0061"
    sachiko "\"Oh, I've got pajamas, too! They're really good, lemme go get them. I'll bring your sheets, too!\"" id a07_comn_02_2782fb87

    play sound se521

    scene bg02ca with Dissolve(0.5)
    pause 1.5

    show miyako 2 sm school a with dict_dissolve_25

    $ side_image = "rin 1 side pyjama h"

    voice "2RI_0058"
    rin "\"There she goes.\"" id a07_comn_02_300247fd

    $ side_image = "hina 1 side pyjama j"

    voice "2HI_0061"
    hina "\"What is with her?\"" id a07_comn_02_5afe737c

    voice "2MI_0013"
    miyako "\"......\"" id a07_comn_02_0aca6bfa

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0042"
    fumi "\"Umm... well, would you like some cake?\"" id a07_comn_02_e61dd93b

    show miyako 2 sm school b with dict_dissolve_25

    voice "2MI_0014"
    miyako "\"That's fine... I just had some.\"" id a07_comn_02_c4856dac

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
