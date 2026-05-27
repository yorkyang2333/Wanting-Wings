label a08_comn_14:

    scene bg09cc with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "—And the feast was done."

    "The pot was empty, and all present had recovered enough from their full bellies to move again."

    show sachiko:
        "sachiko z4 1 lg outfit a flat"
        alpha 0.0 xcenter 298 ycenter 873
        easein 0.5 alpha 1.0 ycenter 773

    voice "2SA_0353"
    sachiko "\"Thanks for everything today, guys.\"" id a08_comn_14_56bbf98b

    show sachiko z4 1 lg outfit a:
        alpha 1.0 xcenter 298 ycenter 773
    with None

    "Sachiko said, standing up."

    show fumi:
        "fumi z4 1 lg pyjama a flat"
        alpha 0.0 xcenter 726 ycenter 862
        easein 0.5 alpha 1.0 ycenter 762

    voice "2FU_0499"
    fumi "\"Let's get this cleaned up real quick.\"" id a08_comn_14_7de26e5a

    show fumi z4 1 lg pyjama a:
        alpha 1.0 xcenter 726 ycenter 762
    with None
    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0354"
    sachiko "\"It's fine, Foomin. I'll handle it.\"" id a08_comn_14_70282d9d

    "She stopped Fumi from stacking up all the dishes on the table."

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0500"
    fumi "\"Are you sure? There's a lot to wash.\"" id a08_comn_14_8d45ec8e

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0355"
    sachiko "\"Yeah, I'll figure it out. Is it okay if I leave her to you, though?\"" id a08_comn_14_e67caf9c

    "Sachiko's wry smile was directed at..."

    $ side_image = "miyako 2 side pyjama i"

    voice "2MI_0479"
    miyako "\"Zzz, zzz...\"" id a08_comn_14_e06db259

    "...Miyako, snoring with her head on the table."

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0356"
    sachiko "\"She eats, then sleeps. Really true to her physical desires, huh?\"" id a08_comn_14_6b53c493

    if routes_cleared == 0:
        jump a08_comn_14_a
    else:
        jump a08_comn_14_b

label a08_comn_14_a:

    hide fumi
    show sachiko z4 1 lg outfit i
    with Dissolve(0.25)

    show sachiko:
        ShakeYes

    voice "2SA_0357"
    sachiko "\"Mikoyan? Go back to your room and sleep there.\"" id a08_comn_14_a_7fd3b749

    show sachiko:
        xoffset 0 yoffset 0
    with None
    $ side_image = "miyako 2 side pyjama i"

    voice "2MI_0480"
    miyako "\"Zzz, zzz...\"" id a08_comn_14_a_fa6dca4f

    "Sachiko called her name and shook her shoulder, but Miyako showed no signs of coming to."

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0588"
    rin "\"Dead to the world.\"" id a08_comn_14_a_de391718

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0358"
    sachiko "\"Oh, fine... Hup.\"" id a08_comn_14_a_30d815b7

    show sachiko:
        ShakeTameiki
    show miyako:
        "miyako z4 2 lg pyjama i flat"
        alpha 0.0 xcenter 512 ycenter 857
        easein 0.75 alpha 1.0 ycenter 757

    "Sachiko put Miyako's arm over her shoulder and stood her up."

    show sachiko:
        xoffset 0 yoffset 0
    show miyako z4 2 lg pyjama i:
        alpha 1.0 xcenter 512 ycenter 757
    with None
    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0359"
    sachiko "\"Can you bring her to your room?\"" id a08_comn_14_a_486f3174

    show rin z4 2 lg pyjama glasses a behind miyako:
        xcenter 793
    with dict_dissolve_25

    voice "2RI_0589"
    rin "\"Yes, ma'am.\"" id a08_comn_14_a_31b2b763

    show rin:
        ShakeYes

    "Rin tried to take Miyako from Sachiko, but..."

    show rin z4 2 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2RI_0590"
    rin "\"Well, this isn't gonna work. She's clinging to you like a koala.\"" id a08_comn_14_a_8f978375

    "At some point, Miyako had locked her arms around Sachiko's waist."

    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2SA_0360"
    sachiko "\"Geez~ She's such a handful~\"" id a08_comn_14_a_6802b5f8

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 2 side pyjama_pjm e"

    voice "2HI_0576"
    hina "\"Guess you're just gonna have to carry her.\"" id a08_comn_14_a_e2b9f6e0

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0361"
    sachiko "\"...Guess so.\"" id a08_comn_14_a_96b3bc5d

    "Sachiko's face was resigned."

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0591"
    rin "\"We could try splashing water on her.\"" id a08_comn_14_a_d791f9c6

    $ side_image = "fumi 2 side pyjama f"

    voice "2FU_0501"
    fumi "\"We can't do that!\"" id a08_comn_14_a_19ec0894

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0592"
    rin "\"I was joking.\"" id a08_comn_14_a_f54db4e1

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0362"
    sachiko "\"Okay, Hinacchi, can you open the door?\"" id a08_comn_14_a_f65a846d

    $ side_image = "hina 2 side pyjama_pjm a"

    voice "2HI_0577"
    hina "\"Yeeep.\"" id a08_comn_14_a_3390d809

    play sound se521
    pause 0.5

    scene white with bg_effect_11
    pause 1.0

    scene bg05ca with bg_effect_11

    "Sachiko staggered over to the four girls' room, carrying Miyako."

    "The rest of the girls smiled as they watched her from behind."

    show fumi 2 sm pyjama b at pos_l2
    show hina 1 sm pyjama_pjm b
    show rin 2 sm pyjama glasses a at pos_r2
    with dict_dissolve_25

    voice "2FU_0502"
    fumi "\"Heheh, it's kind of nice, isn't it?\"" id a08_comn_14_a_c1d9b352

    show hina 1 sm pyjama_pjm p with dict_dissolve_25

    voice "2HI_0578"
    hina "\"Yeah. They're like sisters.\"" id a08_comn_14_a_73e3572d

    show rin 2 sm pyjama glasses g with dict_dissolve_25

    voice "2RI_0593"
    rin "\"Not a mom and daughter?\"" id a08_comn_14_a_dce2d422

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0363"
    sachiko "\"I can hear you, Rin. So you're gonna help me clean that pot~?\"" id a08_comn_14_a_ef65a2db

    show rin 1 sm pyjama glasses d with dict_dissolve_25

    voice "2RI_0594"
    rin "\"A pair of beautiful sisters!\"" id a08_comn_14_a_bd64b306

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0364"
    sachiko "\"Good.\"" id a08_comn_14_a_bd3f114b

    jump a08_comn_14_e

label a08_comn_14_b:

    hide fumi with Dissolve(0.25)

    show hina z4 1 lg pyjama_pjm k:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_0579"
    hina "\"Should we wake her up?\"" id a08_comn_14_b_7c56341b

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0365"
    sachiko "\"Nah, just let her sleep.\"" id a08_comn_14_b_f8401c00

    "Sachiko stopped the three girls from waking their roommate."

    voice "2SA_0366"
    sachiko "\"I'll wake her up when I'm done with the dishes. You guys can head back first.\"" id a08_comn_14_b_2ba5d892

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0595"
    rin "\"There won't be any funny business, will there?\"" id a08_comn_14_b_7b8df6df

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0367"
    sachiko "\"Hee hee hee.\"" id a08_comn_14_b_d5cf06c3

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0580"
    hina "\"Hey!\"" id a08_comn_14_b_a3cc9ced

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0368"
    sachiko "\"There won't.\"" id a08_comn_14_b_9b254690

    play sound se521
    pause 0.5

    scene white with bg_effect_11
    pause 1.0

    scene bg05ca with bg_effect_11
    pause 0.5

    "Sachiko saw the three of them back to their room."

    show fumi 2 sm pyjama b at pos_l2
    show hina 1 sm pyjama_pjm b
    show rin 2 sm pyjama glasses a at pos_r2
    with dict_dissolve_25

    voice "2FU_0503"
    fumi "\"We should get our bath stuff when we get back to our room. We probably all smell like fish right now.\"" id a08_comn_14_b_ee8f2c37

    show rin 2 sm pyjama glasses c with dict_dissolve_25

    voice "2RI_0596"
    rin "\"What~? I don't wanna~\"" id a08_comn_14_b_95a411f3

    show fumi 2 sm pyjama f with dict_dissolve_25

    voice "2FU_0504"
    fumi "\"You need to wash all that hair of yours.\"" id a08_comn_14_b_ebf0fe8d

    show rin 1 sm pyjama glasses i with dict_dissolve_25

    voice "2RI_0597"
    rin "\"I'll take one in the morning~\"" id a08_comn_14_b_13bc019c

    show hina 1 sm pyjama_pjm f with dict_dissolve_25

    voice "2HI_0581"
    hina "\"Yeah right!\"" id a08_comn_14_b_332e5b5f

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "2FU_0505"
    fumi "\"When Miyako wakes up, we'll come take her to the bath with us.\"" id a08_comn_14_b_92d1ae2e

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0369"
    sachiko "\"Alright.\"" id a08_comn_14_b_8520a85d

    play sound se521
    pause 0.5

    scene white with bg_effect_12
    pause 1.0

    scene bg09cc with bg_effect_12
    pause 0.5

    "Heading back to her room, Sachiko slowly took a cigarette out of her pocket."

    if routes_cleared == 1:
        jump a08_comn_14_c
    elif routes_cleared >= 2:
        jump a08_comn_14_d

label a08_comn_14_c:

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0481"
    miyako "\"Funny business?\"" id a08_comn_14_c_b361b42d

    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "sachiko 1 side outfit cigarette h"

    voice "2SA_0370"
    sachiko "\"Pfft!\"" id a08_comn_14_c_98af8381

    camera
    with None

    "Sachiko choked."

    $ side_image = "sachiko 1 side outfit cigarette h"

    voice "2SA_0371"
    sachiko "\"When did you wake up?\"" id a08_comn_14_c_1b422c1b

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0482"
    miyako "\"I don't mind, you know.\"" id a08_comn_14_c_4a10a3c0

    $ side_image = "sachiko 1 side outfit cigarette c"

    voice "2SA_0372"
    sachiko "\"...Are you half-asleep?\"" id a08_comn_14_c_bea20538

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0483"
    miyako "\"I'm awake, I think. Unless this is a dream.\"" id a08_comn_14_c_f63d7725

    "Sachiko sighed and put away the cigarette."

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0373"
    sachiko "\"Well, if you're awake, go back to your room.\"" id a08_comn_14_c_5b5bd046

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0484"
    miyako "\"When did you paint that picture?\"" id a08_comn_14_c_f31eb3bf

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0374"
    sachiko "\"...That's a secret.\"" id a08_comn_14_c_5c60774d

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0485"
    miyako "\"Is that what I look like when I smile?\"" id a08_comn_14_c_271c7430

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0375"
    sachiko "\"Nope. It's a crappy painting.\"" id a08_comn_14_c_1ef3e2de

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0486"
    miyako "\"That's not true. I'm really happy about it.\"" id a08_comn_14_c_0734030d

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0376"
    sachiko "\"Happy? Why?\"" id a08_comn_14_c_5c5d8ed3

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0487"
    miyako "\"Because you said you only paint things you like.\"" id a08_comn_14_c_32ee5e0f

    $ side_image = "sachiko 2 side outfit i"

    voice "2SA_0377"
    sachiko "\"......\"" id a08_comn_14_c_121f1c91

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0488"
    miyako "\"Can I see it again?\"" id a08_comn_14_c_c087fd95

    hide miyako with dict_dissolve_50

    "Miyako had stood up and grabbed the painting from the shelf before she was even finished asking the question."

    $ side_image = "sachiko 2 side outfit g"

    voice "2SA_0378"
    sachiko "\"Ah, hey! Don't touch it!\"" id a08_comn_14_c_d6dcfa39

    "Sachiko ran over to stop her."

    stop music fadeout 1.0
    play sound se_2s_h002

    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "miyako 1 side pyjama_a f"

    voice "2MI_0489"
    miyako "\"Ah... wawah?\"" id a08_comn_14_c_1d94c682

    camera
    with None

    "Sachiko practically tackled her, causing Miyako to lose her balance."

    play sound se_2s_h004

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False
    pause 2.0

    camera
    with None

    show bg_obi
    show miyako 2 lg pyjama c
    with Dissolve(0.5)

    voice "2MI_0490"
    miyako "\"We keep falling over today.\"" id a08_comn_14_c_3f33a221

    $ side_image = "sachiko 2 side outfit d"

    voice "2SA_0379"
    sachiko "\"Seriously.\"" id a08_comn_14_c_d51bdd8a

    "Sachiko sighed from underneath Miyako."

    show miyako 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0491"
    miyako "\"......\"" id a08_comn_14_c_4a358396

    "Miyako was staring at her."

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0380"
    sachiko "\"What is it?\"" id a08_comn_14_c_a33e8ab4

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0492"
    miyako "\"So, will there be funny business?\"" id a08_comn_14_c_5b860d8c

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0381"
    sachiko "\"...Like what?\"" id a08_comn_14_c_d307a117

    play music bgm02 fadein 1.0

    show miyako 1 lg pyjama_b g with dict_dissolve_25

    voice "2MI_0493"
    miyako "\"Like what you do to them all the time? Or what the two lovers do?\"" id a08_comn_14_c_8813dbc4

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0382"
    sachiko "\"Alright, that's enough messing around—\"" id a08_comn_14_c_3ecdacd5

    "Sachiko made to stand up, but Miyako didn't budge."

    show miyako 1 lg pyjama_b a with dict_dissolve_25

    voice "2MI_0494"
    miyako "\"Why did you stop, before?\"" id a08_comn_14_c_e97c087d

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0383"
    sachiko "\"I told you I was joking, didn't I?\"" id a08_comn_14_c_df7eb3da

    show miyako 2 lg pyjama d with dict_dissolve_25

    voice "2MI_0495"
    miyako "\"......\"" id a08_comn_14_c_d1c34789

    "There was disappointment on her face for a moment, but then..."

    show miyako 2 lg pyjama b with dict_dissolve_25

    voice "2MI_0496"
    miyako "\"Can we continue?\"" id a08_comn_14_c_ee6c2fbb

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0384"
    sachiko "\"Huh?\"" id a08_comn_14_c_cdc83659


    hide miyako
    show miyako 1 pyjama_a a:
        zoom 0.8 xcenter 512 yanchor 555 yoffset 384
    with dict_dissolve_25

    voice "2MI_0497"
    miyako "\"Can I continue? Mmh...\"" id a08_comn_14_c_06469742

    "Sachiko was pushed down again."

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0385"
    sachiko "\"Hey—\"" id a08_comn_14_c_c6fc8a17

    show miyako:
        zoom 0.8 yoffset 384
        "miyako 1 pyjama_a l" with Dissolve(1.5)
        easein 1.5 zoom 0.92 yoffset 301

    "Miyako brought her face closer, slowly."

    show miyako 1 pyjama_a l:
        zoom 0.92 yoffset 301
    with None

    stop music fadeout 1.0
    play sound se521
    pause 2.0

    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_0582"
    hina "\"Waaah! A lion's attacking Sachiko?!\"" id a08_comn_14_c_f54ccabc

    "—And that's where that ends tonight."

    jump a08_comn_14_e

label a08_comn_14_d:

    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "sachiko 1 side outfit cigarette h"

    voice "2SA_0386"
    sachiko "\"Wah?!\"" id a08_comn_14_d_0f71b6b5

    camera
    with None

    "Sachiko went white as a sheet."

    play music bgm05 fadein 1.0

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0498"
    miyako "\".........\"" id a08_comn_14_d_4bc46744

    "Miyako had woken up at some point and was staring straight at her."

    "Holding {i}that canvas{/i}, too."

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0499"
    miyako "\"Who is this painting of?\"" id a08_comn_14_d_84618206

    $ side_image = "sachiko 2 side outfit cigarette c"

    voice "2SA_0387"
    sachiko "\"What do you mean, who—\"" id a08_comn_14_d_65883f3f

    show miyako z4 1 lg pyjama_a i with dict_dissolve_25

    voice "2MI_0500"
    miyako "\"It says 'Noel' on the back. Is that her name?\"" id a08_comn_14_d_9a300774

    $ side_image = "sachiko 2 side outfit cigarette d"

    voice "2SA_0388"
    sachiko "\"......\"" id a08_comn_14_d_55122a30

    show miyako z4 1 lg pyjama_a j with dict_dissolve_25

    voice "2MI_0501"
    miyako "\"She's... my model, isn't she?\"" id a08_comn_14_d_5909dd2a

    $ side_image = "sachiko 2 side outfit cigarette d"

    voice "2SA_0389"
    sachiko "\"......\"" id a08_comn_14_d_f285b55b

    play sound se_tabaco

    show miyako:
        xcenter 512
        easein 0.5 xcenter 298
    pause 0.5

    show sachiko:
        "sachiko z4 2 lg outfit cigarette d flat"
        alpha 0.0 xcenter 826
        easein 0.5 alpha 1.0 xcenter 726
    pause 1.5

    show sachiko z4 2 lg outfit cigarette d:
        alpha 1.0 xcenter 726
    with None

    "Sachiko lit a cigarette while she searched for a response."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0502"
    miyako "\"So you knew her.\"" id a08_comn_14_d_62fe2513

    show sachiko z4 2 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_0390"
    sachiko "\"What a coincidence, right?\"" id a08_comn_14_d_29ccf700

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0503"
    miyako "\"It's unbelieveable!\"" id a08_comn_14_d_8c04e151

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0391"
    sachiko "\"I could barely believe it myself.\"" id a08_comn_14_d_b6581d11

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0504"
    miyako "\"What was Noel like?\"" id a08_comn_14_d_51578405

    show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0392"
    sachiko "\"Well, she looked just like you.\"" id a08_comn_14_d_31bc861b

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0505"
    miyako "\"I imagine she must have, since I modeled myself on her... Did she act like me, too?\"" id a08_comn_14_d_45d1e356

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0393"
    sachiko "\"Not in the least...\"" id a08_comn_14_d_07571ea8

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0506"
    miyako "\"Oh. So—\"" id a08_comn_14_d_fdea0d39

    "Miyako went on, blithe as ever:"

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0507"
    miyako "\"Is she wearing the Seiyou uniform—\"" id a08_comn_14_d_a0940985

    show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0394"
    sachiko "\"Why does that matter?\"" id a08_comn_14_d_2fcc1e45

    "Sachiko's face was as dark as Miyako's was bright."

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0508"
    miyako "\"I want to know more about the girl you liked.\"" id a08_comn_14_d_405eb20c

    show sachiko z4 2 lg outfit cigarette a with dict_dissolve_25

    voice "2SA_0395"
    sachiko "\"Huh...?\"" id a08_comn_14_d_df4aeb7a

    show miyako z4 1 lg pyjama_b c with dict_dissolve_25

    voice "2MI_0509"
    miyako "\"You said you only paint things you like.\"" id a08_comn_14_d_cbcf3150

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0396"
    sachiko "\"......\"" id a08_comn_14_d_c9e42a10

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0510"
    miyako "\"Noel invited you down, didn't she?\"" id a08_comn_14_d_d5ef2fb2

    show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0397"
    sachiko "\"...Why do you think so?\"" id a08_comn_14_d_9bd30b77

    voice "2MI_0511"
    miyako "\"Because it has a date from five years ago by the name.\"" id a08_comn_14_d_c853f354

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0398"
    sachiko "\"...I see.\"" id a08_comn_14_d_b1dfea59

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0512"
    miyako "\"But it's more because it's such a beautiful painting.\"" id a08_comn_14_d_23ae53b8

    show sachiko z4 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0399"
    sachiko "\"It's the first one I painted after I came down... It's not that good.\"" id a08_comn_14_d_fc60d4c3

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0513"
    miyako "\"I don't mean technically. You can tell how important she is to you.\"" id a08_comn_14_d_74d4d005

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0514"
    miyako "\"I wish it was me in the painting.\"" id a08_comn_14_d_eb61b047

    show sachiko z4 2 lg outfit cigarette c with dict_dissolve_25

    voice "2SA_0400"
    sachiko "\"......\"" id a08_comn_14_d_3f2d1892

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0515"
    miyako "\"I thought for sure she was someone older, what with the smoking.\"" id a08_comn_14_d_64c3805a

    show sachiko z4 2 lg outfit cigarette f with dict_dissolve_25

    voice "2SA_0401"
    sachiko "\"...She was a delinquent.\"" id a08_comn_14_d_df0ab283

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0516"
    miyako "\"Was she? What about now?\"" id a08_comn_14_d_8157a521

    show sachiko z4 2 lg outfit cigarette d with dict_dissolve_25

    voice "2SA_0402"
    sachiko "\"Now... she's somewhere far away.\"" id a08_comn_14_d_84f3f729

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0517"
    miyako "\"Far away?\"" id a08_comn_14_d_85a8384a

    play sound se521
    pause 2.0

    show sachiko z4 2 lg outfit cigarette a with dict_dissolve_25

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0598"
    rin "\"Oh, she's up.\"" id a08_comn_14_d_a201d0e0

    $ side_image = "hina 1 side pyjama_pjm c"

    voice "2HI_0583"
    hina "\"Miyako, we're gonna go take a bath~\"" id a08_comn_14_d_a4d30a20

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0518"
    miyako "\"Okay.\"" id a08_comn_14_d_b2afd0a6

    $ side_image = "fumi 1 side pyjama a"

    voice "2FU_0506"
    fumi "\"I brought your bath stuff and a change of clothes, so you can come straight with us.\"" id a08_comn_14_d_cec75c10

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0519"
    miyako "\"Thank you~\"" id a08_comn_14_d_a792dcb5

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0584"
    hina "\"Hey, you're smoking!\"" id a08_comn_14_d_1a3108d1

    show sachiko z4 1 lg outfit cigarette b with dict_dissolve_25

    voice "2SA_0403"
    sachiko "\"Oh, yeah...\"" id a08_comn_14_d_94d8c0a6

    hide sachiko
    hide miyako
    with dict_dissolve_50

    "The four girls left."

    play sound se521
    pause 2.0

    "........."

    "......"

    $ side_image = "sachiko 1 side outfit cigarette h"

    voice "2SA_0404"
    sachiko "\"Ouch...\"" id a08_comn_14_d_e6f2fda8

    "The cigarette had burned down to Sachiko's fingers."

    "And that's that."

    jump a08_comn_14_e

label a08_comn_14_e:

    scene white with Dissolve(0.375)
    pause 2.125

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    "February comes in like a lion—"

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
