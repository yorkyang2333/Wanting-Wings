label a09_cou3_01:



    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm04

    play sound se521
    pause 0.5

    $ side_image = "fumi 1 side school_scarf b"

    voice "2FU_0830"
    fumi "\"We're back.\"" id a09_cou3_01_70c1ebf8

    "Fumi returned to the room, cold air still clinging to the end of her hair and the hems of her uniform."

    "She went for the heater first, then hung her jacket up and turned around."

    show fumi 1 lg school a with dict_dissolve_25

    voice "2FU_0831"
    fumi "\"Here, Rin, give me your—\"" id a09_cou3_01_1cc2e2be

    "She reached out to hang Rin's jacket too, but Rin leapt into her chest instead."

    play sound hug

    show fumi:
        "fumi 1 lg school j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False
    pause 0.75

    show fumi 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 1 lg school j flat"
        alpha 1.0 ycenter 1021
        easeout 0.25 alpha 0.0 ycenter 1121

    voice "2FU_0832"
    fumi "\"Aah! H-Hey!\"" id a09_cou3_01_834b9ccc

    hide fumi with None

    "Suddenly tackled, Fumi dropped the hanger and jacket in the entrance and was pushed all the way into the bedroom."

    "It was a surprise attack, so Rin, with her taller stature, naturally had the upper hand. Fumi fell to the bed, powerless to stop her."

    play sound intobed

    pause 0.5

    scene black with Dissolve(0.1875)
    pause 1.0625

    scene kimikara_08_a with Dissolve(0.25)
    pause 0.75

    voice "2RI_1085"
    rin "\"Waaah~ Fast charge~\"" id a09_cou3_01_2bc45ed7

    "She said something, face buried in Fumi's chest."

    "Her blouse had been unbuttoned, covering only her arms now (when did that happen?) "

    "Rin was getting her Fumi energy charged, but in exchange, Fumi had to endure the chill until the heater turned on."

    voice "2FU_0833"
    fumi "\"Come on, that's dangerous.\"" id a09_cou3_01_48e429e8

    "Fumi scolded the baby who was taller than her."

    voice "2RI_1086"
    rin "\"I made sure to aim for the bed.\"" id a09_cou3_01_6252b67d

    "Rin said without even lifting her face from Fumi's chest."

    voice "2FU_0834"
    fumi "\"You'll wrinkle your shirt and skirt.\"" id a09_cou3_01_652d8fcd

    voice "2RI_1087"
    rin "\"That's okay, it's Friday~\"" id a09_cou3_01_302af6d5

    voice "2FU_0835"
    fumi "\"We left our jackets on the floor, too.\"" id a09_cou3_01_d68ef29e

    voice "2RI_1088"
    rin "\"I'll pick them up later~\"" id a09_cou3_01_71800744

    voice "2FU_0836B"
    fumi "\"You've got an answer for everything, don't you? You're so clever, but you can't even wait long enough to change?\"" id a09_cou3_01_4b983179

    scene kimikara_08_b with Dissolve(0.5)

    voice "2RI_1089"
    rin "\"......\"" id a09_cou3_01_2880418d

    "Rin looked up at Fumi peevishly."

    voice "2FU_0837"
    fumi "\"What's wrong, Rin?\"" id a09_cou3_01_5cb14c13

    voice "2RI_1090"
    rin "\"You're going home tonight, right, Fumi?\"" id a09_cou3_01_8bf395a5

    voice "2FU_0838"
    fumi "\"Oh, yes.\"" id a09_cou3_01_29dd3c54

    "Fumi's family's patisserie was so busy before Valentine's Day that she was going home tonight to help out."

    voice "2RI_1091"
    rin "\"You won't be home Saturday or Sunday, right? If I don't get my fill of you now, I won't last through the weekend!\"" id a09_cou3_01_941758db

    voice "2FU_0839"
    fumi "\"I've always gone home on the weekend, though. You never threw a fit like this before.\"" id a09_cou3_01_f7b224d2

    voice "2RI_1092"
    rin "\"...It's not the same.\"" id a09_cou3_01_31cc4fed

    scene kimikara_08_c with Dissolve(0.5)

    voice "2RI_1093"
    rin "\"Until now, you only went home every other week, and you left at noon on Saturday and came back by evening on Sunday...\"" id a09_cou3_01_87ac5eba

    voice "2FU_0840"
    fumi "\"Well... It's Valentine's and the store is busy...\"" id a09_cou3_01_03cc12d3

    voice "2RI_1094"
    rin "\"I know. I won't tell you not to go.\"" id a09_cou3_01_b89215da

    voice "2FU_0841"
    fumi "\"I'm sorry... and thanks.\"" id a09_cou3_01_28df46f0

    voice "2RI_1095"
    rin "\"......\"" id a09_cou3_01_645149c3

    "The desire to have Fumi to herself and the desire not to cause trouble for her warred inside Rin."

    voice "2FU_0842"
    fumi "\"It's not forever. It's just until Valentine's is over.\"" id a09_cou3_01_11446d54

    "Fumi said soothingly."

    voice "2RI_1096"
    rin "\"Yeah... until Valentine's is over. And after that, we'll be together forever. Promise?\"" id a09_cou3_01_7ce13c93

    voice "2FU_0843"
    fumi "\"Yes, yes.\"" id a09_cou3_01_1324c972

    voice "2RI_1097"
    rin "\"One yes is enough!\"" id a09_cou3_01_ddb35f4c

    voice "2FU_0844"
    fumi "\"Yes. I promise.\"" id a09_cou3_01_aace464c

    scene kimikara_08_d with Dissolve(0.5)

    "Rin returned to her charging, comforted by the promise. Fumi put her hand on Rin's head and stroked it gently."

    voice "2FU_0845"
    fumi "\"...So cute.\"" id a09_cou3_01_f54e6002

    "Guess it's not just Rin charging up."

    voice "2RI_1098"
    rin "\"Hey, are you gonna become a baker, Fumi?\"" id a09_cou3_01_3502a9b0

    voice "2FU_0846"
    fumi "\"I plan to. That's what I wrote on my career survey.\"" id a09_cou3_01_612f10cd

    voice "2RI_1099"
    rin "\"Then who's gonna be my wife?\"" id a09_cou3_01_a9cf1ef6

    voice "2FU_0847"
    fumi "\"Ahaha. I can do that and bake too, can't I? Or do I have to be a stay-at-home wife?\"" id a09_cou3_01_e4bfd65e

    voice "2RI_1100"
    rin "\"No.\"" id a09_cou3_01_4b0296f1

    "Rin shook her head."

    voice "2FU_0848"
    fumi "\"Good. I know what I want to do for my career, but I haven't decided if I should study science or arts.\"" id a09_cou3_01_e5e0c032

    voice "2RI_1101"
    rin "\"Does that have anything to do with baking?\"" id a09_cou3_01_402da547

    voice "2FU_0849"
    if persistent.dpatch:
        fumi "\"I want to be a patissier in the end, but I'm trying to decide between going to a baking school after I graduate or studying nutrition in college.\"" id a09_cou3_01_7d96a7a5
    else:
        fumi "\"I want to be a patissier in the end, but I'm trying to decide between going to a vocational baking school after I graduate or studying nutrition in college.\"" id a09_cou3_01_04e75298

    voice "2RI_1102"
    rin "\"Nutrition? When you want to bake cakes?\"" id a09_cou3_01_01c250d9

    voice "2FU_0850"
    fumi "\"Yeah. I'm hoping to take that into account with my baking, instead of just making sweets that taste good.\"" id a09_cou3_01_bebbc316

    voice "2RI_1103"
    rin "\"Haahh... Cake that doesn't make you fat is an unobtainable dream, you know. It goes against the laws of the universe.\"" id a09_cou3_01_fd1c93b1

    voice "2FU_0851"
    fumi "\"...Rin? I never said anything about that.\"" id a09_cou3_01_1ebef260

    "Oh, that's a scary face."

    voice "2RI_1104"
    rin "\"I'm sorry, I'm sorry.\"" id a09_cou3_01_40d84024

    voice "2FU_0852B"
    fumi "\"I want to make cakes that nobody else in the world makes. That's been my dream ever since I was little.\"" id a09_cou3_01_8cab0eb4

    voice "2RI_1105"
    rin "\"You're really serious about this, huh?\"" id a09_cou3_01_377fb58c

    voice "2FU_0853"
    fumi "\"Though I don't have any of the specifics planned yet.\"" id a09_cou3_01_3ecfe8f1

    "Fumi smiled awkwardly. To do something that no one else in the world can is pretty cliché as dreams go, but I bet Fumi can get pretty close."

    voice "2RI_1106"
    rin "\"Are you gonna take over Chocolat? Or start a new store?\"" id a09_cou3_01_05a7fdab

    voice "2FU_0854"
    fumi "\"I hope I can get some practice at Chocolat at first, but I don't see my dad quitting anytime soon, so I think I'll want my own store. Preferably not just a second Chocolat.\"" id a09_cou3_01_b5bd44a4

    voice "2FU_0855"
    fumi "\"By the way, did you do yours? We have to turn in our course plans soon.\"" id a09_cou3_01_37ab4f05

    voice "2RI_1108"
    rin "\"I didn't, but I'll pick what you pick~\"" id a09_cou3_01_b3646e25

    voice "2FU_0856"
    fumi "\"You should take this seriously. You have the grades to pick either one, too.\"" id a09_cou3_01_38e70979

    voice "2RI_1109"
    rin "\"Since I can pick either, I can do whatever you do~\"" id a09_cou3_01_5cc21074

    "True enough."

    voice "2FU_0857"
    fumi "\"Is there something you'd like to do in the future? Maybe become a college professor like your dad?\"" id a09_cou3_01_da52a742

    voice "2RI_1110"
    rin "\"Not at all. Unlike you, I've never once seen my dad working.\"" id a09_cou3_01_5f23bcff

    scene kimikara_08_e with Dissolve(0.5)

    voice "2FU_0858"
    fumi "\"......\"" id a09_cou3_01_e582f9c4

    "As soon as the topic turned to her family, Rin's tone and attitude turned curt."

    "Fumi's face fell when that happened, but Rin didn't notice."

    voice "2RI_1111"
    rin "\"I'll be part of your family in the future~\"" id a09_cou3_01_ffe0195f

    "So casual again."

    voice "2FU_0859"
    fumi "\"You should be serious about this...\"" id a09_cou3_01_e022e03d

    voice "2RI_1112"
    rin "\"I am serious~ Oh, maybe I'll get accounting qualifications and do the bookkeeping for your shop. Wonder what sort of qualifications you need to do accounting for a bakery. Could you ask your mom?\"" id a09_cou3_01_c229184b

    voice "2FU_0860"
    fumi "\"Oh... okay.\"" id a09_cou3_01_5e0bfa05

    voice "2RI_1113"
    rin "\"We'll have a little shop, you baking and me behind the scenes.\"" id a09_cou3_01_06015c9f

    voice "2RI_1113a"
    rin "\"But I bet your sweets'll be really popular, so we'll have to expand the store to get more customers inside. Hmm, but then we won't have as much time alone...\"" id a09_cou3_01_d5e118d0

    "Rin muttered to herself."

    voice "2RI_1114"
    rin "\"I know. I'll think of names for your sweets. I'll be the one who names the cakes no one else in the world can make♪\"" id a09_cou3_01_c8ce2132

    voice "2FU_0861"
    fumi "\"......\"" id a09_cou3_01_646805f9

    "Fumi was being so quiet that Rin seemed positively loquacious in comparison."

    "Rin had always been good at things, starting with her general smarts. If she put her mind to it, she could be anything that she wanted to be."

    "And Fumi was well aware of that, which was why she felt uneasy about Rin refusing to think proactively about her future."

    "Fumi was the personification of motherly instinct, and no doubt influencing Rin's home environment. She was doing nothing to refuse Rin's insistence on being babied."

    "She worried that she was limiting Rin's potential."

    "But at the same time, she knew she was enjoying Rin's dependence on her."

    "Was she actually taking care of Rin for her own sake? Was she the one taking advantage?"

    "Maybe she was even thinking that. It's Fumi, after all."

    "Though she's not the type to overanalyze her emotions, so I imagine she's just feeling a sort of vague unease."

    voice "2RI_1115"
    rin "\"Mon Bijou... No, Gyogyomu?\"" id a09_cou3_01_168db826

    voice "2FU_0862"
    fumi "\"I'm not ruining you, am I, Rin?\"" id a09_cou3_01_638819c8

    voice "2RI_1116"
    rin "\"How d'you mean~? Sexually, maybe~\"" id a09_cou3_01_df18c273

    "Rin just held Fumi harder and buried her face deeper into her chest."

    voice "2FU_0863"
    fumi "\"......\"" id a09_cou3_01_003ce8a8

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou3_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
