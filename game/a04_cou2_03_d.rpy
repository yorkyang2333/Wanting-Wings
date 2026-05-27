label a04_cou2_03_d:

    $ side_image = "hina 2 side school f"

    voice "d/HIN_1281"
    hina "\"...Ah!\"" id a04_cou2_03_d_089a3c0f

    "Hina suddenly realized Rin's hands were going for her ribbon tie."

    $ side_image = "hina 2 side school h"

    voice "d/HIN_1282"
    hina "\"...Are we gonna do something dirty?\"" id a04_cou2_03_d_eada7f48

    "She looked nervously back at Rin."

    $ side_image = "rin 1 side school h"

    voice "d/RIN_1066"
    rin "\"Are you scared?\"" id a04_cou2_03_d_9996f926

    $ side_image = "hina 2 side school c"

    voice "d/HIN_1283"
    hina "\"...Not with you.\"" id a04_cou2_03_d_52f85e63

    "Hina said, giving her best attempt at a confident smile."

    "Rin felt a twinge in her heart."

    $ side_image = "rin 1 side school i"

    voice "d/RIN_1067"
    rin "\"...Ugh, so cute.\"" id a04_cou2_03_d_08a97d6a

    "Rin rained kisses on Hina's forehead, cheeks, neck... wherever her lips would reach."

    $ side_image = "hina 2 side school i"

    voice "d/HIN_1284"
    hina "\"Ahya... hyahn!\"" id a04_cou2_03_d_2c5b8bc7

    $ side_image = "rin 1 side school a"

    voice "d/RIN_1068"
    rin "\"Does that tickle?\"" id a04_cou2_03_d_a50c9e51

    $ side_image = "hina 2 side school f"

    voice "d/HIN_1285"
    hina "\"No... it kind of gives me chills.\"" id a04_cou2_03_d_b581b5d2

    $ side_image = "rin 1 side school c"

    voice "d/RIN_1069"
    rin "\"...You're sensitive.\"" id a04_cou2_03_d_e40c6cd1

    play sound se116a

    "Rin unbuttoned Hina's shirt and hiked up her bra."

    $ side_image = "hina 1 side school d"

    voice "d/HIN_1286"
    hina "\"Ah... h-hey?!\"" id a04_cou2_03_d_33ecd674

    "But Hina pushed it back down."

    $ side_image = "hina 2 side school h"

    voice "d/HIN_1287"
    hina "\"They're so small... I'm kind of embarrassed.\"" id a04_cou2_03_d_7738e3bd

    $ side_image = "rin 1 side school f"

    voice "d/RIN_1070"
    rin "\"Heh. That's obvious enough even with your clothes on, isn't it?\"" id a04_cou2_03_d_1e608625

    $ side_image = "hina 2 side school h"

    voice "d/HIN_1288"
    hina "\"Ugh...\"" id a04_cou2_03_d_80123e73

    $ side_image = "rin 2 side school g"

    voice "d/RIN_1071"
    rin "\"And you drink milk every day, too.\"" id a04_cou2_03_d_ec29543c

    $ side_image = "hina 2 side school i"

    voice "d/HIN_1289"
    hina "\"!!\"" id a04_cou2_03_d_2f1e5879

    camera:
        function LayerShake(10,10,0.25)
    $ persistent.layer_shaken = False

    play sound se103a

    $ side_image = "rin 1 side school j"

    voice "d/RIN_1072"
    rin "\"Ow!\"" id a04_cou2_03_d_b8258338

    camera
    with None

    "There was a thud as Hina's head collided with Rin's jaw."

    stop music fadeout 3.0

    scene black with Dissolve(0.5)
    pause 2.0

    "........."

    "......"

label rp_scene02:

    if _in_replay:
        stop music fadeout 1.0
        stop sound fadeout 1.0
        scene black with Dissolve(0.5)
        pause 2.5

    scene ev08a with Dissolve(0.25)
    pause 1.25

    play music bgm04

    "They pulled away from each other, but their lips were still connected by a line of saliva."

    voice "d/HIN_1290"
    hina "\"Haahh... mmh... Rin...\"" id rp_scene02_0481aaf6

    "Hina's eyes swam and her cheeks burned. Her lips were wet and her voice was choked."

    voice "d/HIN_1291"
    hina "\"I thought... my tongue would melt.\"" id rp_scene02_91ccf5f5

    voice "d/HIN_1292"
    hina "\"Y... You're amazing, Rin... You're really good at kissing.\"" id rp_scene02_ec87119b

    "Hina stared at Rin, enraptured."

    voice "d/RIN_1073"
    rin "\"...You know, it's my first time, too.\"" id rp_scene02_5965ccbf

    voice "d/HIN_1293"
    hina "\"Mm...? What?\"" id rp_scene02_76cb66ea

    voice "d/RIN_1074"
    rin "\"Nothing.\"" id rp_scene02_b153e012

    "Rin smiled awkwardly."

    voice "d/RIN_1075"
    rin "\"I'm more impressed by you down here, Hina.\"" id rp_scene02_54614394

    scene ev08b with Dissolve(0.5)

    voice "d/HIN_1294"
    hina "\"Ugh...\"" id rp_scene02_dcf7911c

    "Hina averted her eyes."

    voice "d/RIN_1076"
    rin "\"You're gonna stain the sheets.\"" id rp_scene02_1827f2e2

    voice "d/HIN_1295"
    hina "\"I-I'll change them right now!\"" id rp_scene02_e50b494c

    "Hina tried to jump up, but Rin grabbed her before she could."

    voice "d/HIN_1296"
    hina "\"What is this? Why is this happening to me?\"" id rp_scene02_c14a091d

    voice "d/RIN_1077"
    rin "\"It's proof that you're in heat.\"" id rp_scene02_b65e7e32

    voice "d/HIN_1297"
    hina "\"In heat? What's that?\"" id rp_scene02_ae6fa4f6

    voice "d/RIN_1078"
    rin "\"Huh? You're embarrassed even though you don't know what it is?\"" id rp_scene02_9e6c8830

    voice "d/HIN_1298"
    hina "\"...I thought I was too old to wet myself.\"" id rp_scene02_e1870c41

    voice "d/RIN_1079"
    rin "\"Ahaha. Actually, it's more like this is only happening because you're an adult.\"" id rp_scene02_6ff61e5b

    voice "d/HIN_1299"
    hina "\"O-Oh...?\"" id rp_scene02_8ffe739e

    voice "d/RIN_1080"
    rin "\"...And anyway, what are you doing knocking dirty stuff when you don't know the first thing about it?\"" id rp_scene02_aba7d551

    voice "d/HIN_1300"
    hina "\"Ugh... well...\"" id rp_scene02_7b5a6adc

    voice "d/RIN_1081"
    rin "\"Must be because you're a baby.\"" id rp_scene02_bc88a536

    voice "d/HIN_1301"
    hina "\"Th-Then... teach me. You know a bunch about it, right, Rin?\"" id rp_scene02_3e2c632e

    voice "d/RIN_1082"
    rin "\"Huh? Oh... I guess so.\"" id rp_scene02_a4104608

    "Hina didn't notice Rin's voice cracking."

    scene black with Dissolve(0.25)
    pause 0.25

    scene ev08c with Dissolve(0.25)
    pause 0.75

    voice "d/HIN_1302"
    hina "\"Hnnh...!\"" id rp_scene02_fe919689

    "Hina went completely stiff as soon as Rin's fingers touched her."

    voice "d/RIN_1083"
    rin "\"...Are you sure you're not scared?\"" id rp_scene02_8648315c

    "Hina squeezed her eyes shut and clenched her teeth."

    voice "d/HIN_1303"
    hina "\"I-I'm fine!\"" id rp_scene02_fcd95943

    "She nodded exaggeratedly."

    voice "d/RIN_1084"
    rin "\"Y-Yeah?\"" id rp_scene02_94235149

    voice "d/RIN_1085"
    rin "\"...Well, I am. I feel like I'm gonna break you.\"" id rp_scene02_5909ac2a

    voice "d/RIN_1086"
    rin "\"It's okay... alright?\"" id rp_scene02_a88bfc1f

    "Her tender words were directed at herself as much as at Hina."

    voice "d/HIN_1304"
    hina "\"...Ah, nnh...\"" id rp_scene02_814ed0a2

    "Rin's hand slid down Hina's springy thigh to a soft hill."

    "The trail of Hina's arousal went all the way down to her butt. Rin scooped some up on her finger."

    voice "d/RIN_1087"
    rin "\"You get wet really easily... What a girl you are, Hina.\"" id rp_scene02_6e9629dc

    voice "d/HIN_1305"
    hina "\"Of... course I am.\"" id rp_scene02_50e7d86c

    voice "d/RIN_1088"
    rin "\"I was a little worried about what I'd find inside your underwear.\"" id rp_scene02_3abbb479

    voice "d/HIN_1306"
    hina "\"Are you stupid? That's a terrible thing to say to—\"" id rp_scene02_e06e33f5

    "Rin's fingers parted Hina's flower petals and touched the warmth hidden behind them."

    scene ev08e with Dissolve(0.5)

    voice "d/HIN_1307"
    hina "\"A-Aah... nnnh!!\"" id rp_scene02_2ed7630c

    voice "d/RIN_1089"
    rin "\"H-Hina?\"" id rp_scene02_dee47cd1

    voice "d/HIN_1308"
    hina "\"I-I'm okay... I was just surprised.\"" id rp_scene02_7abc20c1

    "Rin might have been even more surprised."

    voice "d/HIN_1309"
    hina "\"I've... never been touched there before...\"" id rp_scene02_f857a6d3

    voice "d/RIN_1090"
    rin "\"...Yeah, I figured.\"" id rp_scene02_54cb97cc

    "Rin nodded."

    voice "d/RIN_1091"
    rin "\"Want to keep going?\"" id rp_scene02_07b55f55

    "Hina nodded, too."

    scene ev08d with Dissolve(0.5)

    "Rin traced Hina's slit with her middle finger."

    voice "d/HIN_1310"
    hina "\"N... Nn... naaah!\"" id rp_scene02_fb994929

    "There were sticky sounds every time she moved her finger, and Hina shook her head, embarrassed."

    "Rin pressed down and moved her finger deeper in."

    "She was just a tiny bit inside Hina."

    voice "d/HIN_1311"
    hina "\"Unh... aaah! N-Not there!\"" id rp_scene02_40568c3a

    "Suddenly, the opening shut, preventing her intrusion."

    "Hina's hand grabbed Rin's."

    voice "d/RIN_1092"
    rin "\"Is that still... a little scary?\"" id rp_scene02_cedcfcb6

    voice "d/HIN_1312"
    hina "\"...I-I'm okay.\"" id rp_scene02_5841f8fe

    "She said, but her voice was trembling."

    voice "d/RIN_1093"
    rin "\"...Would this be better?\"" id rp_scene02_6ee6908a

    "Rin pulled her finger out and moved it to above the slit."

    voice "d/HIN_1313"
    hina "\"Mh... ah...\"" id rp_scene02_24c62b74

    "She pressed gently on the slick bead there, and a needy sound came from Hina."

    voice "d/RIN_1094"
    rin "\"Does that hurt?\"" id rp_scene02_992ab997

    voice "d/HIN_1314"
    hina "\"N-No... nh... ngh...\"" id rp_scene02_3c50124d

    "Rin gave a little nod at that confirmation."

    "Using only her fingertip, she skillfully stimulated the pearl."

    voice "d/HIN_1315"
    hina "\"...Nn... nah...\"" id rp_scene02_f17b4c73

    "Hina's reactions to even the slightest touch were pronounced."

    voice "d/HIN_1316"
    hina "\"Haah... haah...\"" id rp_scene02_f3f52f3f

    voice "d/RIN_1095"
    rin "\"That face you're making is really cute.\"" id rp_scene02_61dc6ee5

    "She brushed aside the hair sticking to Hina's forehead and looked at her face."

    "It was a heated expression Hina would normally never make."

    voice "d/HIN_1317"
    hina "\"Haahh... th-this feels... weird...\"" id rp_scene02_642fb531

    "The unknown sensations Hina was feeling were confusing her."

    "And knowing what her touch was doing to Hina... Rin just got more into it."

    voice "d/RIN_1096"
    rin "\"That's good, feel even weirder—\"" id rp_scene02_bd50278f

    "Rin's fingers pinched around Hina's everything."

    "And..."

    window hide
    show white:
        alpha 1.0 additive 1.0
        linear 0.7 alpha 0.0
        repeat 2
    pause 1.4
    window auto

    scene ev08e with Dissolve(0.5)

    voice "d/HIN_1318"
    hina "\"Nnh... aaah... ah... aaaaah!!\"" id rp_scene02_b45d0277

    "Hina suddenly screamed and threw her head back."

    voice "d/RIN_1097"
    rin "\"Huh...?\"" id rp_scene02_82f3ceb8

    "Hina's head hit Rin's shoulder."

    voice "d/HIN_1319"
    hina "\"Aah... aaaah... nnnnh!!\"" id rp_scene02_c2561ad2

    voice sustain
    voice "d/RIN_1098"
    rin "\"Whoa, wait, did you cum?\""

    voice "d/HIN_1320"
    hina "\"Ah... a-ah... ahn!!\"" id rp_scene02_aa0d8582

    "Hina couldn't answer."

    voice "d/HIN_1321"
    hina "\"Wh-What? What is this... I-It won't stop... haaaaah!!\"" id rp_scene02_c54dbf36

    "Hina merely shuddered in Rin's arms."

    voice "d/RIN_1099"
    rin "\"Hina? Hina?!\"" id rp_scene02_5a4e2378

    voice "d/HIN_1322"
    hina "\"H-Help me... Rin?! I-I feel like, I won't be able to come... back!!\"" id rp_scene02_97c11b9d

    voice "d/RIN_1100"
    rin "\"It's okay! It's okay!\"" id rp_scene02_6aa8d915

    "Rin wrapped her arms around Hina and held her."

    scene black with Dissolve(0.5)
    pause 1.5

    "......"

    voice "d/HIN_1323"
    hina "\"Hahh... phew...\"" id rp_scene02_64fc76cf

    "Hina took a deep breath."

    "Then she stretched up and fell back onto Rin's chest like a puppet with its strings cut."

    scene ev08f with Dissolve(0.5)
    pause 2.0

    voice "d/HIN_1324"
    hina "\"Haah... that scared me.\"" id rp_scene02_2be275ba

    voice "d/RIN_1101"
    rin "\"That's my line. Just how sensitive are you?\"" id rp_scene02_3528a27e

    voice "d/HIN_1325"
    hina "\"I-I don't think it's my fault! I-It's because you're too good at this!\"" id rp_scene02_824d9145

    voice "d/RIN_1102"
    rin "\"O-Oh...?\"" id rp_scene02_d1da88a3

    "Rin seemed embarrassed when the blame was shifted to her."

    voice "d/HIN_1326"
    hina "\"But... it really did feel good.\"" id rp_scene02_ca2dfdcd

    "Hina was still clinging to Rin's shirt."

    voice "d/RIN_1103"
    rin "\"Yeah? Th-Thanks.\"" id rp_scene02_e4e89470

    "She'd seemed nervous, but apparently that wasn't how Hina saw it."

    voice "d/HIN_1327"
    hina "\"Haahh... I'm really tired for some reason~\"" id rp_scene02_a39194d0

    "She must have calmed down some. Hina's usual smile had returned."

    voice "d/RIN_1104"
    rin "\"Haha, that was hard work, huh?\"" id rp_scene02_ecbf5b68

    voice "d/HIN_1328"
    hina "\"It was more normal than the stuff in the book, though. I'm relieved.\"" id rp_scene02_25ebfca9

    voice "d/RIN_1105"
    rin "\"I'm telling you, that book's different.\"" id rp_scene02_6cd27e4a

    voice "d/HIN_1329"
    hina "\"O... Oh.\"" id rp_scene02_ec62758f

    "Does she really get it?"

    voice "d/HIN_1330"
    hina "\"Umm, Rin?\"" id rp_scene02_cf914204

    voice "d/HIN_1331"
    hina "\"...Next time... Next time I want to make you feel good, Rin.\"" id rp_scene02_2971e0ed

    voice "d/RIN_1106"
    rin "\"What~? I wonder if you can.\"" id rp_scene02_7073f8c8

    voice "d/HIN_1332"
    hina "\"You're not taking me serously! I mean it, I'll pull out all the stops!\"" id rp_scene02_c2bd77f7

    voice "d/RIN_1107"
    rin "\"Heheh, I'm looking forward to it.\"" id rp_scene02_3cd6fb49

    voice "d/HIN_1333"
    hina "\"Okay, let me get my headphones!\"" id rp_scene02_8a61556c

    voice "d/RIN_1108"
    rin "\"No!\"" id rp_scene02_4b31c231

    jump rp_scene02_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
