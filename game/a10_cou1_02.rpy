label a10_cou1_02:

    scene expression "gui/kimikara/mainmenu_ground1.webp"
    show expression "gui/kimikara/title2.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter10a with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg01cg with Dissolve(0.5)
    pause 1.5

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_1234"
    rin "\"We're back~\"" id a10_cou1_02_70fa3e65

    $ side_image = "miyako 1 side pyjama_a c"

    voice "2MI_0990"
    miyako "\"That was a nice bath~\"" id a10_cou1_02_03f08731

    "The two returned from the baths, nice and toasty, and entered the living room."

    show fumi 2 lg pyjama h at pos_l
    show hina 2 lg pyjama_pjm h at pos_r
    with dict_dissolve_25

    "They found Hina and Fumi sitting there, one's head on the other's shoulder."

    play music bgm05 fadein 1.0

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1235"
    rin "\"Yeesh, they were like that when we left, too. Haven't they been a little more all over each other than usual the last two or three days?\"" id a10_cou1_02_2f41d457

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0947"
    fumi "\"Oh, hello.\"" id a10_cou1_02_7c2fb47d

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0991"
    miyako "\"The bath's open for you.\"" id a10_cou1_02_265262ad

    voice "2HI_1197"
    hina "\"Yeah, we'll go in a bit.\"" id a10_cou1_02_0387a7c2

    "She said, showing no signs of moving."

    $ side_image = "rin 1 side pyjama glasses f"

    voice "2RI_1236"
    rin "\"They're stuck to each other again. Makes me more light-headed than the bath.\"" id a10_cou1_02_2b6f7032

    "Even when Rin teased her, she only gave her a glance."

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1237"
    rin "\"And why are you both holding your shoes like that? Are you supposed to be Toyotomi Hideyoshi?\"" id a10_cou1_02_6b678f84

    "They were holding the red shoes that they got for Christmas."

    $ side_image = "rin 1 side pyjama glasses h"

    voice "2RI_1238"
    rin "\"Are you finally gonna wear them?\"" id a10_cou1_02_0571faaf

    voice "2HI_1198"
    hina "\"...We're never gonna wear them.\"" id a10_cou1_02_3f04ff8f

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0948"
    fumi "\"We want to take good care of them since they're such important memories.\"" id a10_cou1_02_6fb87c3a

    "They both held the shoes closer to them."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_1239"
    rin "\"......\"" id a10_cou1_02_6447f3cf

    "Rin sighed."

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_1240"
    rin "\"Listen, ever since you went and helped at Asou's store, you two have been weird. Did something happen?\"" id a10_cou1_02_a40b2056

    show hina 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_1199"
    hina "\"...Nothing happened.\"" id a10_cou1_02_2469e48d

    "Hina responded without looking at Rin's face."

    $ side_image = "rin 1 side pyjama glasses h"

    voice "2RI_1241"
    rin "\"It's not like... a fight or anything.\"" id a10_cou1_02_f70af1d5

    show fumi 2 lg pyjama h
    show hina 2 lg pyjama_pjm h
    with dict_dissolve_25

    $ voice2("hina","2HI_1200N","fumi","2FU_0949")
    hina_fumi "\"'Cause we love each other...\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1242"
    rin "\"Th-That's nice.\"" id a10_cou1_02_5def8a75

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_1243"
    rin "\"They're just like usual... but something's off.\"" id a10_cou1_02_65248345

    "Rin and Miyako exchanged a look at the peculiar ennui that had settled around Hina and Fumi."

    voice "2FU_0950"
    fumi "\"How many more times will we be able to exchange presents like this?\"" id a10_cou1_02_9b43c401

    voice "2HI_1201"
    hina "\"......\"" id a10_cou1_02_90a79999

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou1_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
