label a09_comn_06:

    scene white with Dissolve(0.5)
    pause 2.0

    if routes_cleared == 0:
        scene kimikara_10_g_ with Dissolve(2.0)
    else:
        scene kimikara_10_g with Dissolve(2.0)

    play music bgm03 fadein 1.0

    "Sachiko faced the canvas, Miyako watching her from nearby."

    "Miyako asked questions occasionally as she watched the paintbrush move, and Sachiko answered without stopping."

    "—\"I'll teach you to paint if you join me.\""

    "That was something Sachiko had told her back when Miyako still had her wings."

    if routes_cleared == 0:
        scene kimikara_10_h_ with Dissolve(0.5)
    else:
        scene kimikara_10_h with Dissolve(0.5)

    voice "2SA_0516"
    sachiko "\"How's it look now that your world's got color?\"" id a09_comn_06_7f14c70a

    "Sachiko asked for Miyako's opinion as she switched brushes."

    voice "2MI_0632"
    miyako "\"I like it much better with color. The mountains used to only be black and white, but now that there's so much color, they've gotten a lot livelier.\"" id a09_comn_06_2280d599

    voice "2SA_0517"
    sachiko "\"Ahaha. Well, I'm glad... hmm.\"" id a09_comn_06_26a78697

    "She'd been moving her brush around above her palette for a while now."

    if routes_cleared == 0:
        scene kimikara_10_m_ with Dissolve(0.5)
    else:
        scene kimikara_10_m with Dissolve(0.5)

    voice "2MI_0633"
    miyako "\"You're not putting any paint on it?\"" id a09_comn_06_8acf8835

    voice "2SA_0518"
    sachiko "\"I'm still not sure what color to use~\"" id a09_comn_06_3094a805

    voice "2MI_0634"
    miyako "\"I thought you just used the same colors as the scenery.\"" id a09_comn_06_35e280b6

    voice "2SA_0519"
    sachiko "\"Well, of course, but I have a hard time matching the colors I see to the colors of the paint. I'm not sure which ones are the same.\"" id a09_comn_06_62dd6e0a

    voice "2MI_0635"
    miyako "\"Isn't green just green?\"" id a09_comn_06_983e9a89

    voice "2SA_0520"
    sachiko "\"How many shades of green do you think there are? Emerald, parrot, viridian, turquoise, lime, jade, evergreen, viridian...\"" id a09_comn_06_a6bf4e85

    voice "2MI_0636"
    miyako "\"You said viridian twice again.\"" id a09_comn_06_ddc6a91f

    voice "2SA_0521"
    sachiko "\"Anyway, a lot of the time, I pick something and paint with it and it ends up looking completely different.\"" id a09_comn_06_6eba821d

    voice "2MI_0637"
    miyako "\"Come to think of it, why do you have red on your palette? You're painting green things now.\"" id a09_comn_06_10fa2638

    voice "2SA_0522"
    sachiko "\"Sometimes when you mix red in, it looks more green than just using green. I'm kind of still learning, though. Look here...\"" id a09_comn_06_40402365

    if routes_cleared == 0:
        scene kimikara_10_h_ with Dissolve(0.5)
    else:
        scene kimikara_10_h with Dissolve(0.5)

    "Sachiko pointed to a spot on the canvas. Miyako bent down and squinted."

    voice "2MI_0638"
    miyako "\"It's true, there's red there. I never would have noticed if you hadn't told me.\"" id a09_comn_06_8c033262

    "There were some faint bits of red hiding in the green. The points of crimson brought out the hue."

    if routes_cleared == 0:
        scene kimikara_10_g_ with Dissolve(0.5)
    else:
        scene kimikara_10_g with Dissolve(0.5)

    voice "2SA_0523"
    sachiko "\"All I'm trying to do is paint what I see in front of me, but even that's difficult.\"" id a09_comn_06_625f48e6

    voice "2SA_0524"
    sachiko "\"The reality that I see with my eyes changes as I interpret it with my mind. That's where factual knowledge and the information you get from your senses differ.\"" id a09_comn_06_b94ad21e

    voice "2SA_0525"
    sachiko "\"I just have to focus my eyes and move my brush to create what I see, eliminating as much interference from my brain as I can to create an image as close to reality as possible.\"" id a09_comn_06_2c24aa05

    if routes_cleared == 0:
        scene kimikara_10_m_ with Dissolve(0.5)
    else:
        scene kimikara_10_m with Dissolve(0.5)

    voice "2MI_0639"
    miyako "\"You're very serious about it.\"" id a09_comn_06_9c3555da

    if routes_cleared == 0:
        scene kimikara_10_h_ with Dissolve(0.5)
    else:
        scene kimikara_10_h with Dissolve(0.5)

    voice "2SA_0526"
    sachiko "\"I am. You didn't think so?\"" id a09_comn_06_a7e4d865

    "Sachiko scooped up some paint from her palette."

    if routes_cleared == 0:
        scene kimikara_10_m_ with Dissolve(0.5)
    else:
        scene kimikara_10_m with Dissolve(0.5)

    voice "2SA_0527"
    sachiko "\"Why are you in your uniform, anyway?\"" id a09_comn_06_8f07644f

    voice "2MI_0640"
    if persistent.dpatch:
        miyako "\"Because I came here from school.\"" id a09_comn_06_5a639625
    else:
        miyako "\"Because I came here from campus.\"" id a09_comn_06_e911eeda

    voice "2SA_0528"
    sachiko "\"On a Saturday?\"" id a09_comn_06_be7d09f4

    voice "2MI_0641"
    miyako "\"The principal wanted to see me.\"" id a09_comn_06_4eabca11

    voice "2SA_0529"
    sachiko "\"...The principal? I didn't hear about that. What'd she want?\"" id a09_comn_06_73c79191

    voice "2MI_0642"
    if persistent.dpatch:
        miyako "\"She wanted to know how I'd been doing at school and in the dorm.\"" id a09_comn_06_216ce356
    else:
        miyako "\"She wanted to know how I'd been doing on campus and in the dorm.\"" id a09_comn_06_9d69af98

    voice "2SA_0530"
    sachiko "\"...You didn't tell her anything unnecessary, did you?\"" id a09_comn_06_3030c95a

    voice "2MI_0643"
    miyako "\"Unnecessary? Oh, I kept my being an angel a secret—\"" id a09_comn_06_0a7113bc

    voice "2SA_0531"
    sachiko "\"No, not that. I mean about the smoking and booze and stuff—\"" id a09_comn_06_06b3b3f3

    if routes_cleared == 0:
        scene kimikara_10_p_ with Dissolve(0.5)
    else:
        scene kimikara_10_p with Dissolve(0.5)

    voice "2MI_0644"
    miyako "\"Ahaha. I kept those a secret too, of course.\"" id a09_comn_06_9bce87c9

    if routes_cleared == 0:
        scene kimikara_10_r_ with Dissolve(0.5)
    else:
        scene kimikara_10_r with Dissolve(0.5)

    voice "2SA_0532"
    sachiko "\"Good girl.\"" id a09_comn_06_320dbe95

    voice "2MI_0645"
    miyako "\"The principal asked about you, though. She said you should come visit again sometime.\"" id a09_comn_06_c1c7b2ed

    if routes_cleared == 0:
        scene kimikara_10_p_ with Dissolve(0.5)
    else:
        scene kimikara_10_p with Dissolve(0.5)

    voice "2SA_0533"
    sachiko "\"Yeah, yeah. Eventually.\"" id a09_comn_06_c891f610

    voice "2MI_0646"
    miyako "\"Are you two friends?\"" id a09_comn_06_ff422f06

    voice "2SA_0534"
    sachiko "\"I'd say I owe her more than that we're friends. She's a real busybody.\"" id a09_comn_06_470c39db

    "Sachiko swiped her brush across the canvas."

    if routes_cleared == 0:
        jump a09_comn_06_a
    elif routes_cleared >= 2:
        jump a09_comn_06_b

label a09_comn_06_a:

    scene kimikara_10_m_ with Dissolve(0.5)

    voice "2SA_0535"
    sachiko "\"Let's see...\"" id a09_comn_06_a_c74e4655

    voice "2MI_0647"
    miyako "\"Is it done?\"" id a09_comn_06_a_66264907

    voice "2SA_0536"
    sachiko "\"Probably needs a stroke or two more...\"" id a09_comn_06_a_35f926fc

    "She carefully chose the brush to put the finishing touches on her painting."

    scene kimikara_10_g_ with Dissolve(0.5)

    voice "2MI_0648"
    miyako "\"This one's taking you a long time, too.\"" id a09_comn_06_a_b252d9f6

    voice "2SA_0537"
    sachiko "\"Yeah, I'm slow. There's a lot of evergreens around here, so not much changes, but there are some colors that have started to change. I have to draw from memory in some places.\"" id a09_comn_06_a_423733dd

    scene kimikara_10_j_ with Dissolve(0.5)

    voice "2MI_0649"
    miyako "\"Why don't you just use the color you think looks best? It's your painting.\"" id a09_comn_06_a_482737ab

    voice "2SA_0538"
    sachiko "\"...I guess you've got a point.\"" id a09_comn_06_a_390d109b

    "It's not like it's a photograph. There's a fence in between Sachiko and the view, but it's not in the painting."

    voice "2MI_0650"
    miyako "\"You were painting this the first time we met, too.\"" id a09_comn_06_a_a11bc1d3

    voice "2SA_0539"
    sachiko "\"Yeah. I started it just a little before then.\"" id a09_comn_06_a_c8f844b9

    voice "2MI_0651"
    miyako "\"Before I peeked at your canvas, I thought you painted much stranger pictures.\"" id a09_comn_06_a_21bac494

    voice "2SA_0540"
    sachiko "\"That's not very nice.\"" id a09_comn_06_a_e5f5f899

    scene kimikara_10_p_ with Dissolve(0.5)

    voice "2MI_0652"
    miyako "\"Well, you were screaming, 'I want to draw a cute girl in the nuuude!!'\"" id a09_comn_06_a_dbe17b12

    voice "2SA_0541"
    sachiko "\"That passion still lives on. Want me to scream again?\"" id a09_comn_06_a_65f864ef

    voice "2MI_0653"
    miyako "\"No thanks. Those three didn't want to model for you back then either, did they?\"" id a09_comn_06_a_e3d5eb2b

    voice "2SA_0542"
    sachiko "\"They're good at negotiating contracts.\"" id a09_comn_06_a_5b76a582

    "I don't think that's the issue."

    scene kimikara_10_m_ with Dissolve(0.5)

    voice "2MI_0654"
    miyako "\"When I saw you playing around with the three of them, I imagined what it would be like to join you.\"" id a09_comn_06_a_b64adcda

    voice "2MI_0655"
    miyako "\"Then, for just a second, there was color in the world. Maybe I'd already made my decision at that moment.\"" id a09_comn_06_a_3ad680ec

    voice "2SA_0543"
    sachiko "\"......\"" id a09_comn_06_a_b1758319

    voice "2MI_0656"
    miyako "\"You told me you wanted to see the things those girls saw, feel what they felt... so you got rid of your wings.\"" id a09_comn_06_a_270ecac8

    voice "2MI_0657"
    miyako "\"I thought the same thing myself.\"" id a09_comn_06_a_b55ced8b

    voice "2SA_0544"
    sachiko "\"Oh yeah?\"" id a09_comn_06_a_038f63f4

    scene kimikara_10_p_ with Dissolve(0.5)

    voice "2MI_0658"
    miyako "\"So what was the other reason?\"" id a09_comn_06_a_343c96db

    voice "2SA_0545"
    sachiko "\"Hunh?\"" id a09_comn_06_a_2608bf9e

    voice "2MI_0659"
    miyako "\"You said that wasn't the only reason. But that 'that's another story.'\"" id a09_comn_06_a_a10f1441

    voice "2SA_0546"
    sachiko "\"I said that?\"" id a09_comn_06_a_d7428c7f

    voice "2MI_0660"
    miyako "\"You did.\"" id a09_comn_06_a_e8a85259

    voice "2SA_0547"
    sachiko "\"...Okay! This is the final touch!\"" id a09_comn_06_a_95f0c0e8

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene kimikara_10_g_ with bg_effect_05
    pause 0.5

    "Sachiko put the date and her signature on the back of the canvas."

    voice "2MI_0661"
    miyako "\"Do you always date and sign your paintings when you finish them?\"" id a09_comn_06_a_93226e42

    voice "2SA_0548"
    sachiko "\"Yeah. You know, since you forget.\"" id a09_comn_06_a_dab320a4

    voice "2MI_0662"
    miyako "\"......\"" id a09_comn_06_a_8a379687

    jump a09_comn_06_c

label a09_comn_06_b:

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene kimikara_10_t with bg_effect_05
    pause 0.5

    voice "2MI_0663"
    miyako "\"Huh? You haven't seen Noel once since then?\"" id a09_comn_06_b_2a40c491

    voice "2SA_0549"
    sachiko "\"Nope. She's probably forgotten about me, too.\"" id a09_comn_06_b_c365ade1

    voice "2MI_0664"
    miyako "\"I don't think that's true. You said she lives somewhere far away now, right? It was somewhere far away where I saw her, too.\"" id a09_comn_06_b_fe3933c5

    voice "2SA_0550"
    sachiko "\"......\"" id a09_comn_06_b_6bff53b3

    voice "2MI_0665"
    miyako "\"I wonder if it would be hard to find her.\"" id a09_comn_06_b_b8a7f340

    voice "2SA_0551"
    sachiko "\"What would you do if you could? You're just strangers who happen to have the same face.\"" id a09_comn_06_b_c9a8a6ea

    voice "2MI_0666"
    miyako "\"Ahaha. She'd probably be surprised if someone who looked just like her showed up all of a sudden.\"" id a09_comn_06_b_c56430fe

    "Miyako put her hand to the cheek that looked just like Noel's."

    voice "2SA_0552"
    sachiko "\"...I was surprised, too.\"" id a09_comn_06_b_c58a0927

    voice "2MI_0667"
    miyako "\"......\"" id a09_comn_06_b_a4364927

    "Miyako's expression hardened slightly at that."

    scene kimikara_10_z with Dissolve(0.5)

    voice "2MI_0668"
    miyako "\"Will you paint me too one day?\"" id a09_comn_06_b_d784e267

    voice "2SA_0553"
    sachiko "\"......\"" id a09_comn_06_b_81decbc4

    "Sachiko's brush stopped."

    voice "2MI_0669"
    miyako "\"Would a painting of me look different than hers?\"" id a09_comn_06_b_48dfb2ee

    play sound se_wind01
    pause 1.0

    voice "2SA_0554"
    sachiko "\"......Can I paint you nude?\"" id a09_comn_06_b_d26221ea

    scene kimikara_10_i with Dissolve(0.5)

    voice "2MI_0670"
    miyako "\"Sure!\"" id a09_comn_06_b_f142de3d

    "Miyako's hand went straight for her scarf."

    scene kimikara_10_s with Dissolve(0.5)

    voice "2SA_0555"
    sachiko "\"No! No exhibitionism! I didn't mean strip right here!\"" id a09_comn_06_b_5539bc6d

    voice "2MI_0671"
    miyako "\"You're right. I wouldn't want to catch a cold.\"" id a09_comn_06_b_191613c9

    voice "2SA_0556"
    sachiko "\"That's not the problem!\"" id a09_comn_06_b_53420c7d

    scene kimikara_10_t with Dissolve(0.5)

    voice "2MI_0672"
    miyako "\"Huh...?\"" id a09_comn_06_b_f7ae7630

    voice "2SA_0557"
    sachiko "\"Okay, that's enough for today. I'm gonna clean up and head back down.\"" id a09_comn_06_b_b9ea6b8b

    "Sachiko took out a cloth and started wiping off her brush."

    scene kimikara_10_i with Dissolve(0.5)

    voice "2MI_0673"
    miyako "\"I'll put away the paint, then.\"" id a09_comn_06_b_88181296

    "Miyako gathered up the scattered paints."

    voice "2SA_0558"
    sachiko "\"Thanks. Be careful not to get your uniform dirty.\"" id a09_comn_06_b_ca112dd5

    voice "2MI_0674"
    miyako "\"Okay. .........♪\"" id a09_comn_06_b_f6ee4101

    "Miyako merrily lined up the tubes of paint in the box. It was a simple task, but one she could only do now that she could see colors."

    voice "2SA_0559"
    sachiko "\"......\"" id a09_comn_06_b_a7be50a7

    "Sachiko stopped washing her brush and looked at Miyako."

    voice "2SA_0560"
    sachiko "\"Listen...\"" id a09_comn_06_b_3a1d392b

    voice "2MI_0675"
    miyako "\"Yes?\"" id a09_comn_06_b_4b98342a

    jump a09_comn_06_c

label a09_comn_06_c:

    stop music fadeout 1.0
    play sound se521
    pause 0.5

    scene white with Dissolve(0.375)
    pause 2.125

    scene bg07aa with Dissolve(0.5)
    pause 1.5

    $ side_image = "hina 1 side school a"

    voice "2HI_0771"
    hina "\"Oh, there they are.\"" id a09_comn_06_c_22eb42d3

    "It was Hina. She'd scrunched her shoulders up from the cold, but trotted over to them nonetheless."

    play music bgm01 fadein 1.0

    $ side_image = "hina 1 side school c"

    voice "2HI_0772"
    hina "\"We're having some sweet potatoes as a snack. Do you two want some?\"" id a09_comn_06_c_86a061e5

    show miyako 1 sm school_a_sei b at pos_ls
    show sachiko 1 sm outfit cigarette g at pos_rs
    with dict_dissolve_25

    voice "2SA_0561"
    sachiko "\"Oh, I was just getting hungry. I'll be right down after I clean this up~\"" id a09_comn_06_c_e0a9eefa

    show miyako 1 sm school_a_sei c with dict_dissolve_25

    voice "2MI_0676"
    miyako "\"Sweet potatoes... I've never had them before. I'm looking forward to it♪\"" id a09_comn_06_c_77d00659

    $ side_image = "hina 1 side school k"

    voice "2HI_0773"
    hina "\"Need help?\"" id a09_comn_06_c_9951a8fd

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0562"
    sachiko "\"Well hey, if you're offering, mind folding up the easel?\"" id a09_comn_06_c_e52ff198

    $ side_image = "hina 2 side school a"

    voice "2HI_0774"
    hina "\"Sure thing. What were you two talking about while you were painting?\"" id a09_comn_06_c_204a0098

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0677"
    miyako "\"I—\"" id a09_comn_06_c_6015cfe8

    show sachiko 1 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0563"
    sachiko "\"Negotiating some nude modeling.\"" id a09_comn_06_c_42c146a9

    $ side_image = "hina 1 side school f"

    voice "2HI_0775"
    hina "\"Chwaaah!!\"" id a09_comn_06_c_93944c29

    show sachiko:
        "sachiko 1 sm outfit cigarette h" with Dissolve(0.25)
        ShakeSide

    voice "2SA_0564"
    sachiko "\"No! No brandishing the easel!!\"" id a09_comn_06_c_143e4fa1

    show sachiko 1 sm outfit cigarette h:
        xoffset 0 yoffset 0
    with None
    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    stop music fadeout 1.0
    stop sound fadeout 1.0

    camera
    with None

    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a09_cou1_02
    elif route2 == 2:
        jump a09_cou2_03
    elif route2 == 3:
        jump a09_cou3_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
