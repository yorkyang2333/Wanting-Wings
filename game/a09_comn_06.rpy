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
    sachiko "\"How's it look now that your world's got color?\""

    "Sachiko asked for Miyako's opinion as she switched brushes."

    voice "2MI_0632"
    miyako "\"I like it much better with color. The mountains used to only be black and white, but now that there's so much color, they've gotten a lot livelier.\""

    voice "2SA_0517"
    sachiko "\"Ahaha. Well, I'm glad... hmm.\""

    "She'd been moving her brush around above her palette for a while now."

    if routes_cleared == 0:
        scene kimikara_10_m_ with Dissolve(0.5)
    else:
        scene kimikara_10_m with Dissolve(0.5)

    voice "2MI_0633"
    miyako "\"You're not putting any paint on it?\""

    voice "2SA_0518"
    sachiko "\"I'm still not sure what color to use~\""

    voice "2MI_0634"
    miyako "\"I thought you just used the same colors as the scenery.\""

    voice "2SA_0519"
    sachiko "\"Well, of course, but I have a hard time matching the colors I see to the colors of the paint. I'm not sure which ones are the same.\""

    voice "2MI_0635"
    miyako "\"Isn't green just green?\""

    voice "2SA_0520"
    sachiko "\"How many shades of green do you think there are? Emerald, parrot, viridian, turquoise, lime, jade, evergreen, viridian...\""

    voice "2MI_0636"
    miyako "\"You said viridian twice again.\""

    voice "2SA_0521"
    sachiko "\"Anyway, a lot of the time, I pick something and paint with it and it ends up looking completely different.\""

    voice "2MI_0637"
    miyako "\"Come to think of it, why do you have red on your palette? You're painting green things now.\""

    voice "2SA_0522"
    sachiko "\"Sometimes when you mix red in, it looks more green than just using green. I'm kind of still learning, though. Look here...\""

    if routes_cleared == 0:
        scene kimikara_10_h_ with Dissolve(0.5)
    else:
        scene kimikara_10_h with Dissolve(0.5)

    "Sachiko pointed to a spot on the canvas. Miyako bent down and squinted."

    voice "2MI_0638"
    miyako "\"It's true, there's red there. I never would have noticed if you hadn't told me.\""

    "There were some faint bits of red hiding in the green. The points of crimson brought out the hue."

    if routes_cleared == 0:
        scene kimikara_10_g_ with Dissolve(0.5)
    else:
        scene kimikara_10_g with Dissolve(0.5)

    voice "2SA_0523"
    sachiko "\"All I'm trying to do is paint what I see in front of me, but even that's difficult.\""

    voice "2SA_0524"
    sachiko "\"The reality that I see with my eyes changes as I interpret it with my mind. That's where factual knowledge and the information you get from your senses differ.\""

    voice "2SA_0525"
    sachiko "\"I just have to focus my eyes and move my brush to create what I see, eliminating as much interference from my brain as I can to create an image as close to reality as possible.\""

    if routes_cleared == 0:
        scene kimikara_10_m_ with Dissolve(0.5)
    else:
        scene kimikara_10_m with Dissolve(0.5)

    voice "2MI_0639"
    miyako "\"You're very serious about it.\""

    if routes_cleared == 0:
        scene kimikara_10_h_ with Dissolve(0.5)
    else:
        scene kimikara_10_h with Dissolve(0.5)

    voice "2SA_0526"
    sachiko "\"I am. You didn't think so?\""

    "Sachiko scooped up some paint from her palette."

    if routes_cleared == 0:
        scene kimikara_10_m_ with Dissolve(0.5)
    else:
        scene kimikara_10_m with Dissolve(0.5)

    voice "2SA_0527"
    sachiko "\"Why are you in your uniform, anyway?\""

    voice "2MI_0640"
    if persistent.dpatch:
        miyako "\"Because I came here from school.\"" id a09_comn_06_5a639625
    else:
        miyako "\"Because I came here from campus.\""

    voice "2SA_0528"
    sachiko "\"On a Saturday?\""

    voice "2MI_0641"
    miyako "\"The principal wanted to see me.\""

    voice "2SA_0529"
    sachiko "\"...The principal? I didn't hear about that. What'd she want?\""

    voice "2MI_0642"
    if persistent.dpatch:
        miyako "\"She wanted to know how I'd been doing at school and in the dorm.\"" id a09_comn_06_216ce356
    else:
        miyako "\"She wanted to know how I'd been doing on campus and in the dorm.\""

    voice "2SA_0530"
    sachiko "\"...You didn't tell her anything unnecessary, did you?\""

    voice "2MI_0643"
    miyako "\"Unnecessary? Oh, I kept my being an angel a secret—\""

    voice "2SA_0531"
    sachiko "\"No, not that. I mean about the smoking and booze and stuff—\""

    if routes_cleared == 0:
        scene kimikara_10_p_ with Dissolve(0.5)
    else:
        scene kimikara_10_p with Dissolve(0.5)

    voice "2MI_0644"
    miyako "\"Ahaha. I kept those a secret too, of course.\""

    if routes_cleared == 0:
        scene kimikara_10_r_ with Dissolve(0.5)
    else:
        scene kimikara_10_r with Dissolve(0.5)

    voice "2SA_0532"
    sachiko "\"Good girl.\""

    voice "2MI_0645"
    miyako "\"The principal asked about you, though. She said you should come visit again sometime.\""

    if routes_cleared == 0:
        scene kimikara_10_p_ with Dissolve(0.5)
    else:
        scene kimikara_10_p with Dissolve(0.5)

    voice "2SA_0533"
    sachiko "\"Yeah, yeah. Eventually.\""

    voice "2MI_0646"
    miyako "\"Are you two friends?\""

    voice "2SA_0534"
    sachiko "\"I'd say I owe her more than that we're friends. She's a real busybody.\""

    "Sachiko swiped her brush across the canvas."

    if routes_cleared == 0:
        jump a09_comn_06_a
    elif routes_cleared >= 2:
        jump a09_comn_06_b

label a09_comn_06_a:

    scene kimikara_10_m_ with Dissolve(0.5)

    voice "2SA_0535"
    sachiko "\"Let's see...\""

    voice "2MI_0647"
    miyako "\"Is it done?\""

    voice "2SA_0536"
    sachiko "\"Probably needs a stroke or two more...\""

    "She carefully chose the brush to put the finishing touches on her painting."

    scene kimikara_10_g_ with Dissolve(0.5)

    voice "2MI_0648"
    miyako "\"This one's taking you a long time, too.\""

    voice "2SA_0537"
    sachiko "\"Yeah, I'm slow. There's a lot of evergreens around here, so not much changes, but there are some colors that have started to change. I have to draw from memory in some places.\""

    scene kimikara_10_j_ with Dissolve(0.5)

    voice "2MI_0649"
    miyako "\"Why don't you just use the color you think looks best? It's your painting.\""

    voice "2SA_0538"
    sachiko "\"...I guess you've got a point.\""

    "It's not like it's a photograph. There's a fence in between Sachiko and the view, but it's not in the painting."

    voice "2MI_0650"
    miyako "\"You were painting this the first time we met, too.\""

    voice "2SA_0539"
    sachiko "\"Yeah. I started it just a little before then.\""

    voice "2MI_0651"
    miyako "\"Before I peeked at your canvas, I thought you painted much stranger pictures.\""

    voice "2SA_0540"
    sachiko "\"That's not very nice.\""

    scene kimikara_10_p_ with Dissolve(0.5)

    voice "2MI_0652"
    miyako "\"Well, you were screaming, 'I want to draw a cute girl in the nuuude!!'\""

    voice "2SA_0541"
    sachiko "\"That passion still lives on. Want me to scream again?\""

    voice "2MI_0653"
    miyako "\"No thanks. Those three didn't want to model for you back then either, did they?\""

    voice "2SA_0542"
    sachiko "\"They're good at negotiating contracts.\""

    "I don't think that's the issue."

    scene kimikara_10_m_ with Dissolve(0.5)

    voice "2MI_0654"
    miyako "\"When I saw you playing around with the three of them, I imagined what it would be like to join you.\""

    voice "2MI_0655"
    miyako "\"Then, for just a second, there was color in the world. Maybe I'd already made my decision at that moment.\""

    voice "2SA_0543"
    sachiko "\"......\""

    voice "2MI_0656"
    miyako "\"You told me you wanted to see the things those girls saw, feel what they felt... so you got rid of your wings.\""

    voice "2MI_0657"
    miyako "\"I thought the same thing myself.\""

    voice "2SA_0544"
    sachiko "\"Oh yeah?\""

    scene kimikara_10_p_ with Dissolve(0.5)

    voice "2MI_0658"
    miyako "\"So what was the other reason?\""

    voice "2SA_0545"
    sachiko "\"Hunh?\""

    voice "2MI_0659"
    miyako "\"You said that wasn't the only reason. But that 'that's another story.'\""

    voice "2SA_0546"
    sachiko "\"I said that?\""

    voice "2MI_0660"
    miyako "\"You did.\""

    voice "2SA_0547"
    sachiko "\"...Okay! This is the final touch!\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene kimikara_10_g_ with bg_effect_05
    pause 0.5

    "Sachiko put the date and her signature on the back of the canvas."

    voice "2MI_0661"
    miyako "\"Do you always date and sign your paintings when you finish them?\""

    voice "2SA_0548"
    sachiko "\"Yeah. You know, since you forget.\""

    voice "2MI_0662"
    miyako "\"......\""

    jump a09_comn_06_c

label a09_comn_06_b:

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene kimikara_10_t with bg_effect_05
    pause 0.5

    voice "2MI_0663"
    miyako "\"Huh? You haven't seen Noel once since then?\""

    voice "2SA_0549"
    sachiko "\"Nope. She's probably forgotten about me, too.\""

    voice "2MI_0664"
    miyako "\"I don't think that's true. You said she lives somewhere far away now, right? It was somewhere far away where I saw her, too.\""

    voice "2SA_0550"
    sachiko "\"......\""

    voice "2MI_0665"
    miyako "\"I wonder if it would be hard to find her.\""

    voice "2SA_0551"
    sachiko "\"What would you do if you could? You're just strangers who happen to have the same face.\""

    voice "2MI_0666"
    miyako "\"Ahaha. She'd probably be surprised if someone who looked just like her showed up all of a sudden.\""

    "Miyako put her hand to the cheek that looked just like Noel's."

    voice "2SA_0552"
    sachiko "\"...I was surprised, too.\""

    voice "2MI_0667"
    miyako "\"......\""

    "Miyako's expression hardened slightly at that."

    scene kimikara_10_z with Dissolve(0.5)

    voice "2MI_0668"
    miyako "\"Will you paint me too one day?\""

    voice "2SA_0553"
    sachiko "\"......\""

    "Sachiko's brush stopped."

    voice "2MI_0669"
    miyako "\"Would a painting of me look different than hers?\""

    play sound se_wind01
    pause 1.0

    voice "2SA_0554"
    sachiko "\"......Can I paint you nude?\""

    scene kimikara_10_i with Dissolve(0.5)

    voice "2MI_0670"
    miyako "\"Sure!\""

    "Miyako's hand went straight for her scarf."

    scene kimikara_10_s with Dissolve(0.5)

    voice "2SA_0555"
    sachiko "\"No! No exhibitionism! I didn't mean strip right here!\""

    voice "2MI_0671"
    miyako "\"You're right. I wouldn't want to catch a cold.\""

    voice "2SA_0556"
    sachiko "\"That's not the problem!\""

    scene kimikara_10_t with Dissolve(0.5)

    voice "2MI_0672"
    miyako "\"Huh...?\""

    voice "2SA_0557"
    sachiko "\"Okay, that's enough for today. I'm gonna clean up and head back down.\""

    "Sachiko took out a cloth and started wiping off her brush."

    scene kimikara_10_i with Dissolve(0.5)

    voice "2MI_0673"
    miyako "\"I'll put away the paint, then.\""

    "Miyako gathered up the scattered paints."

    voice "2SA_0558"
    sachiko "\"Thanks. Be careful not to get your uniform dirty.\""

    voice "2MI_0674"
    miyako "\"Okay. .........♪\""

    "Miyako merrily lined up the tubes of paint in the box. It was a simple task, but one she could only do now that she could see colors."

    voice "2SA_0559"
    sachiko "\"......\""

    "Sachiko stopped washing her brush and looked at Miyako."

    voice "2SA_0560"
    sachiko "\"Listen...\""

    voice "2MI_0675"
    miyako "\"Yes?\""

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
    hina "\"Oh, there they are.\""

    "It was Hina. She'd scrunched her shoulders up from the cold, but trotted over to them nonetheless."

    play music bgm01 fadein 1.0

    $ side_image = "hina 1 side school c"

    voice "2HI_0772"
    hina "\"We're having some sweet potatoes as a snack. Do you two want some?\""

    show miyako 1 sm school_a_sei b at pos_ls
    show sachiko 1 sm outfit cigarette g at pos_rs
    with dict_dissolve_25

    voice "2SA_0561"
    sachiko "\"Oh, I was just getting hungry. I'll be right down after I clean this up~\""

    show miyako 1 sm school_a_sei c with dict_dissolve_25

    voice "2MI_0676"
    miyako "\"Sweet potatoes... I've never had them before. I'm looking forward to it♪\""

    $ side_image = "hina 1 side school k"

    voice "2HI_0773"
    hina "\"Need help?\""

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0562"
    sachiko "\"Well hey, if you're offering, mind folding up the easel?\""

    $ side_image = "hina 2 side school a"

    voice "2HI_0774"
    hina "\"Sure thing. What were you two talking about while you were painting?\""

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0677"
    miyako "\"I—\""

    show sachiko 1 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0563"
    sachiko "\"Negotiating some nude modeling.\""

    $ side_image = "hina 1 side school f"

    voice "2HI_0775"
    hina "\"Chwaaah!!\""

    show sachiko:
        "sachiko 1 sm outfit cigarette h" with Dissolve(0.25)
        ShakeSide

    voice "2SA_0564"
    sachiko "\"No! No brandishing the easel!!\""

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
