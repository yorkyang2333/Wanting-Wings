label a09_cou1_03:

    scene bg01cg with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "That night, everyone was present in the room."

    "They'd just gotten back from the bath and were folding laundry."

    "The dorm had washers and dryers in the bath area, so it was common to do laundry while bathing."

    show hina z4 1 lg pyjama_pjm k
    show fumi z4 2 lg pyjama g:
        xcenter 172
    show miyako z4 2 lg pyjama a:
        xcenter 852
    with dict_dissolve_25

    voice "2MI_0822"
    miyako "\"What's this?\"" id a09_cou1_03_164dc08f

    "Miyako pulled a brightly colored shirt out from the laundry basket."

    show hina z4 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0867"
    hina "\"Oh, that's my basketball uniform.\"" id a09_cou1_03_0f4b6736

    "Miyako spread the shirt out and found the basketball team's logo on it."

    voice "2MI_0823"
    miyako "\"Did you wear it in today's game?\"" id a09_cou1_03_56b12ea4

    show hina z4 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0868"
    hina "\"Yeah, it's a new one they just started wearing today.\"" id a09_cou1_03_ead9dd6c

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0722"
    fumi "\"That's why I didn't recognize it.\"" id a09_cou1_03_d2b96b8a

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0824"
    miyako "\"You don't have a softball one?\"" id a09_cou1_03_a7b033b3

    show hina z4 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0869"
    if persistent.dpatch:
        hina "\"The softball one's at school. The team managers have a heavy-duty washer they use.\"" id a09_cou1_03_1df5b027
    else:
        hina "\"The softball one's on campus. The team managers have a heavy-duty washer they use.\"" id a09_cou1_03_ff7c41c0

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0723"
    fumi "\"If you use a regular washing machine, the dirt and sand can get into the machine and break it.\"" id a09_cou1_03_aa24d65d

    show hina:
        "hina z4 1 lg pyjama_pjm q" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0870"
    hina "\"Yeah. I got mine all dirty today, too.\"" id a09_cou1_03_6a71501c

    show hina z4 1 lg pyjama_pjm q:
        xoffset 0 yoffset 0
    with None

    "Hina made a head-first slide gesture."

    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0724"
    fumi "\"I'd like to see one of your games, Hina.\"" id a09_cou1_03_e9f9099d

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0825"
    miyako "\"Oh, me too.\"" id a09_cou1_03_45a21a6d

    show hina z4 1 lg pyjama_pjm b with dict_dissolve_25

    voice "2HI_0871"
    hina "\"What do you want to see? Basketball? Track? Softball?\"" id a09_cou1_03_dde03599

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0725"
    fumi "\"Anything that you get to show off in.\"" id a09_cou1_03_3ec1741b

    show hina z4 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0872"
    hina "\"I'm good at all of them, so you can come and see any you want♪\"" id a09_cou1_03_d1707040

    $ side_image = "rin 1 side pyjama f"

    voice "2RI_0857"
    rin "\"Is this size special-order? Ah, must be for kids~\"" id a09_cou1_03_e7345b28

    "Rin spread out the uniform and barged her way into the atmosphere between the two girls."

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0873"
    hina "\"Alright, meet me on the roof. We'll have a one-on-one match.\"" id a09_cou1_03_f8d60acd

    "Hina raised one knee."

    hide miyako with Dissolve(0.25)

    show rin z4 1 lg pyjama glasses g:
        xcenter 852
    with dict_dissolve_25

    voice "2RI_0858"
    rin "\"Y-You misunderstand. I just meant it's impressive that you're called in for backup in volleyball and basketball at your height.\"" id a09_cou1_03_1aba3ab3

    "It {i}is{/i} impressive that Hina can contribute so much in sports where height is so valued."

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0859"
    rin "\"How do you compete with the height though, really?\"" id a09_cou1_03_5a40e823

    show hina z4 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0874"
    hina "\"I make up for it with speed and mobility, I'd say.\"" id a09_cou1_03_f9793102

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0860"
    rin "\"Hmm. The lack of chest makes her more lightweight?\"" id a09_cou1_03_a97aa1b1

    show hina:
        "hina z4 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0875"
    hina "\"Graaaaah!\"" id a09_cou1_03_61be01f2

    show hina z4 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg pyjama d with dict_dissolve_25

    voice "2FU_0726"
    fumi "\"Wah! That was close.\"" id a09_cou1_03_1a26c345

    "Fumi pulled back from where she was ironing everyone's shirts."

    show hina z4 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0876"
    hina "\"S-Sorry. You okay?\"" id a09_cou1_03_f4a39e30

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0861"
    rin "\"Your mobility works against you in a small room like this.\"" id a09_cou1_03_3973735c

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0877"
    hina "\"You're right. Let's go to the roof. I can show you what I'm really capable of up there.\"" id a09_cou1_03_30ec9db1

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0862"
    rin "\"Nooo! It's cold and dark out there!\"" id a09_cou1_03_44b0605c

    $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_0826"
    miyako "\"Are your breasts heavy if they're big?\"" id a09_cou1_03_5ce057e4

    "She gets right to the point."

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0727"
    fumi "\"Er, well... they do hurt when I run sometimes.\"" id a09_cou1_03_722a6d3c

    play sound se521
    pause 1.0

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0682"
    sachiko "\"What's this~? You talkin' about boobs?\"" id a09_cou1_03_bd715e6a

    "Suddenly, Sachiko appeared."

    show fumi z4 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0728"
    fumi "\"Those ears of yours are really starting to scare me.\"" id a09_cou1_03_8fc701ec

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0683"
    sachiko "\"Wait, were you really talking about boobs? Yay!\"" id a09_cou1_03_c0369d7f

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0863"
    rin "\"Put your victory pose away. Back to the roof with you!\"" id a09_cou1_03_ae71dce3

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0684"
    sachiko "\"No! No! I wanna talk about boobs!\"" id a09_cou1_03_23f89eea

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0878"
    hina "\"If you don't need something, can you leave?\"" id a09_cou1_03_dea5a125

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0685"
    sachiko "\"I do, I do, I do need something! Here, I got this!\"" id a09_cou1_03_f41662c7

    "Sachiko waved around a white object she was holding."

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0827"
    miyako "\"What is it?\"" id a09_cou1_03_d109f0f0

    show fumi z4 1 lg pyjama e with dict_dissolve_25

    voice "2FU_0729"
    fumi "\"Ah...\"" id a09_cou1_03_785b6f9b

    "Fumi alone quickly recognized it."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0686"
    sachiko "\"Foomin left her bra in a laundry basket, so I brought it over.\"" id a09_cou1_03_689d3480

    $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_0828"
    miyako "\"How could you tell that it was Fumi's?\"" id a09_cou1_03_31cfe372

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0687"
    sachiko "\"Well, Foomin's the only one in this dorm who's this big.\"" id a09_cou1_03_a9af26b3

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0864"
    rin "\"Ah~ That checks out.\"" id a09_cou1_03_f206fb00

    show fumi:
        "fumi z4 1 lg pyjama j" with Dissolve(0.25)
        ShakeSide

    voice "2FU_0730"
    fumi "\"...!!\"" id a09_cou1_03_f2936003

    show fumi z4 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    "The eyes in the room all locked on to Fumi's chest, which she hid behind her arms without thinking."

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0879"
    hina "\"Don't look at Fumi like that!\"" id a09_cou1_03_2b3d2540

    show hina z4 1 lg pyjama_pjm f with None

    pause 0.5
    scene white with bg_effect_05
    pause 1.5

    scene bg01cg with bg_effect_05
    pause 0.5

    "........."

    "After she put the underwear away in her dresser..."

    show fumi z4 2 lg pyjama b:
        xcenter 298
    show sachiko z4 1 lg outfit a:
        xcenter 726
    with dict_dissolve_25

    voice "2FU_0731"
    fumi "\"Thank you for bringing it to me.\"" id a09_cou1_03_b493bd5e

    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0688"
    sachiko "\"No prob. You can pay me back by letting me put my face in them\nand—\"" id a09_cou1_03_2eb9d90b

    $ side_image = "hina 1 side pyjama_pjm i"

    voice "2HI_0880"
    hina "\"Grrrrrrrrr!\"" id a09_cou1_03_1ce634ee

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0689"
    sachiko "\"They probably don't have many at your size, do they, Foomin? They're expensive, aren't they?\"" id a09_cou1_03_54e44503

    "Sachiko asked, skirting around the room so that Hina couldn't lunge at her."

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0732"
    fumi "\"Yeah... They don't go on sale all that often, either. And there aren't any cute ones anyway...\"" id a09_cou1_03_ad2b491d

    "Fumi wore a rare frown."

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0865"
    rin "\"Around my size is probably the cheapest. Lots of different kinds, too.\"" id a09_cou1_03_04c30f71

    show fumi z4 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0733"
    fumi "\"Ugh... I'm jealous.\"" id a09_cou1_03_05329d82

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0866"
    rin "\"And Mikoyan's probably about as big as you can get while still getting some variety.\"" id a09_cou1_03_c58de99b

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_0829"
    miyako "\"This size?\"" id a09_cou1_03_ac9c6053

    "Miyako lifted her breasts up in both hands."

    $ side_image = "rin 2 side pyjama f"

    voice "2RI_0867"
    rin "\"Bfft... Thanks.\"" id a09_cou1_03_da0df668

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0830"
    miyako "\"?\"" id a09_cou1_03_b9dad95d

    "The four of them had gone shopping around Christmas to buy Miyako's underwear."

    "She'd moved in suddenly and without any spare undies."

    hide sachiko with Dissolve(0.25)

    show hina z4 2 lg pyjama_pjm a:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_0881"
    hina "\"You're cute no matter what bra you wear, Fumi.\"" id a09_cou1_03_a42acaa6

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0734"
    fumi "\"Mmh... Thank you.\"" id a09_cou1_03_c6196251

    $ side_image = "rin 2 side pyjama e"

    voice "2RI_0868"
    rin "\"Well, you can't go without it when you've got the volume Asou has.\"" id a09_cou1_03_e69a2405

    show fumi z4 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0735"
    fumi "\"Right...\"" id a09_cou1_03_d600dd24

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0690"
    sachiko "\"As for Hinacchi—\"" id a09_cou1_03_06719700

    show hina z4 1 lg pyjama_pjm g with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "2HI_0882"
    hina "\"I'm not showing you anymore!\"" id a09_cou1_03_54d5afcd

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0736"
    fumi "\"They all bind them tightly and lift them up... it's pretty tiring.\"" id a09_cou1_03_481af901

    $ side_image = "rin 2 side pyjama g"

    voice "2RI_0869"
    rin "\"Yeah, the band on the back is pretty wide and they've got three or four hooks, too. The first time I saw them, I thought they were corsets.\"" id a09_cou1_03_f41b5a84

    show fumi:
        "fumi z4 1 lg pyjama d" with Dissolve(0.25)
        ShakeTameiki
        4.5
        "fumi z4 1 lg pyjama a" with Dissolve(0.25)

    voice "2FU_0737"
    fumi "\"Seriously... That's why it feels really nice to take them off when I get back to the dorm. Yours are pretty big too, Miyako. Are you okay?\"" id a09_cou1_03_4b3f4c76

    show fumi z4 1 lg pyjama a:
        xoffset 0 yoffset 0
    with None
    $ side_image = "miyako 1 side pyjama_a a"

    voice "2MI_0831"
    miyako "\"Mmh... I find them constricting too, so I don't really like wearing them. I make sure to wear them on days when we have PE, though. Otherwise, they move so much it's hard to run.\"" id a09_cou1_03_3e66960c

    "She's not—"

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0738"
    fumi "\"...Miyako, it's fine when you're at home, but you really should wear them when you're out.\"" id a09_cou1_03_d811f2bb

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0832"
    miyako "\"Oh, okay.\"" id a09_cou1_03_dfab464c

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0691"
    sachiko "\"Man, I really envy Hinacchi, though.\"" id a09_cou1_03_295ade78

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0883"
    hina "\"Why?\"" id a09_cou1_03_f7cac145

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0692"
    sachiko "\"Well, you can touch Foomin's boobs as much as you want, right?\"" id a09_cou1_03_4ef255b7

    show fumi z4 1 lg pyjama e with dict_dissolve_25
    $ side_image = "rin 1 side pyjama h"

    voice "2RI_0870"
    rin "\"I hear that.\"" id a09_cou1_03_9d672927

    show hina:
        "hina z4 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0884"
    hina "\"I keep telling you! Stop saying dirty stuff!\"" id a09_cou1_03_527cdc38

    show hina z4 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0693"
    sachiko "\"What? But you're dating, aren't you? Isn't that normal, then?\"" id a09_cou1_03_93b4558c

    show hina z4 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0885"
    hina "\"W-Well...\"" id a09_cou1_03_5cb80a93

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0739"
    fumi "\"......\"" id a09_cou1_03_d7b060e8

    "Hina and Fumi shared a look, both turning red."

    $ side_image = "rin 1 side pyjama f"

    voice "2RI_0871"
    rin "\"I'm sure all Hina's doing is sucking on them like a baby.\"" id a09_cou1_03_0e3a30e5

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0886"
    hina "\"...Huh? Ah...\"" id a09_cou1_03_94a5975f

    "She couldn't very well admit it."

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_0872"
    rin "\"Wait, what...? You don't have anything to say to that? Now it just seems like I'm honestly sexually harassing you.\"" id a09_cou1_03_9d5305e9

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0694"
    sachiko "\"Rin~\"" id a09_cou1_03_c2b5c43b

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0833"
    miyako "\"Oh, what kind of bra are you wearing, Sachiko?\"" id a09_cou1_03_0b68a56c

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0695"
    sachiko "\"This kind!\"" id a09_cou1_03_dd9f9cbd

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_0873"
    rin "\"You don't have to show us!\"" id a09_cou1_03_9d2fc8e0

    voice "2HI_0887"
    hina "\".........\"" id a09_cou1_03_d0e3d598

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0740"
    fumi "\"......\"" id a09_cou1_03_8f93372e

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared == 1:
        jump a09_comn_07
    elif routes_cleared >= 2:
        jump a09_cou4_02
    else:
        jump a09_cou1_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
