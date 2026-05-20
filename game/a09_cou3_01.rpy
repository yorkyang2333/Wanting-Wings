label a09_cou3_01:



    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm04

    play sound se521
    pause 0.5

    $ side_image = "fumi 1 side school_scarf b"

    voice "2FU_0830"
    fumi "\"We're back.\""

    "Fumi returned to the room, cold air still clinging to the end of her hair and the hems of her uniform."

    "She went for the heater first, then hung her jacket up and turned around."

    show fumi 1 lg school a with dict_dissolve_25

    voice "2FU_0831"
    fumi "\"Here, Rin, give me your—\""

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
    fumi "\"Aah! H-Hey!\""

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
    rin "\"Waaah~ Fast charge~\""

    "She said something, face buried in Fumi's chest."

    "Her blouse had been unbuttoned, covering only her arms now (when did that happen?) "

    "Rin was getting her Fumi energy charged, but in exchange, Fumi had to endure the chill until the heater turned on."

    voice "2FU_0833"
    fumi "\"Come on, that's dangerous.\""

    "Fumi scolded the baby who was taller than her."

    voice "2RI_1086"
    rin "\"I made sure to aim for the bed.\""

    "Rin said without even lifting her face from Fumi's chest."

    voice "2FU_0834"
    fumi "\"You'll wrinkle your shirt and skirt.\""

    voice "2RI_1087"
    rin "\"That's okay, it's Friday~\""

    voice "2FU_0835"
    fumi "\"We left our jackets on the floor, too.\""

    voice "2RI_1088"
    rin "\"I'll pick them up later~\""

    voice "2FU_0836B"
    fumi "\"You've got an answer for everything, don't you? You're so clever, but you can't even wait long enough to change?\""

    scene kimikara_08_b with Dissolve(0.5)

    voice "2RI_1089"
    rin "\"......\""

    "Rin looked up at Fumi peevishly."

    voice "2FU_0837"
    fumi "\"What's wrong, Rin?\""

    voice "2RI_1090"
    rin "\"You're going home tonight, right, Fumi?\""

    voice "2FU_0838"
    fumi "\"Oh, yes.\""

    "Fumi's family's patisserie was so busy before Valentine's Day that she was going home tonight to help out."

    voice "2RI_1091"
    rin "\"You won't be home Saturday or Sunday, right? If I don't get my fill of you now, I won't last through the weekend!\""

    voice "2FU_0839"
    fumi "\"I've always gone home on the weekend, though. You never threw a fit like this before.\""

    voice "2RI_1092"
    rin "\"...It's not the same.\""

    scene kimikara_08_c with Dissolve(0.5)

    voice "2RI_1093"
    rin "\"Until now, you only went home every other week, and you left at noon on Saturday and came back by evening on Sunday...\""

    voice "2FU_0840"
    fumi "\"Well... It's Valentine's and the store is busy...\""

    voice "2RI_1094"
    rin "\"I know. I won't tell you not to go.\""

    voice "2FU_0841"
    fumi "\"I'm sorry... and thanks.\""

    voice "2RI_1095"
    rin "\"......\""

    "The desire to have Fumi to herself and the desire not to cause trouble for her warred inside Rin."

    voice "2FU_0842"
    fumi "\"It's not forever. It's just until Valentine's is over.\""

    "Fumi said soothingly."

    voice "2RI_1096"
    rin "\"Yeah... until Valentine's is over. And after that, we'll be together forever. Promise?\""

    voice "2FU_0843"
    fumi "\"Yes, yes.\""

    voice "2RI_1097"
    rin "\"One yes is enough!\""

    voice "2FU_0844"
    fumi "\"Yes. I promise.\""

    scene kimikara_08_d with Dissolve(0.5)

    "Rin returned to her charging, comforted by the promise. Fumi put her hand on Rin's head and stroked it gently."

    voice "2FU_0845"
    fumi "\"...So cute.\""

    "Guess it's not just Rin charging up."

    voice "2RI_1098"
    rin "\"Hey, are you gonna become a baker, Fumi?\""

    voice "2FU_0846"
    fumi "\"I plan to. That's what I wrote on my career survey.\""

    voice "2RI_1099"
    rin "\"Then who's gonna be my wife?\""

    voice "2FU_0847"
    fumi "\"Ahaha. I can do that and bake too, can't I? Or do I have to be a stay-at-home wife?\""

    voice "2RI_1100"
    rin "\"No.\""

    "Rin shook her head."

    voice "2FU_0848"
    fumi "\"Good. I know what I want to do for my career, but I haven't decided if I should study science or arts.\""

    voice "2RI_1101"
    rin "\"Does that have anything to do with baking?\""

    voice "2FU_0849"
    if persistent.dpatch:
        fumi "\"I want to be a patissier in the end, but I'm trying to decide between going to a baking school after I graduate or studying nutrition in college.\"" id a09_cou3_01_7d96a7a5
    else:
        fumi "\"I want to be a patissier in the end, but I'm trying to decide between going to a vocational baking school after I graduate or studying nutrition in college.\""

    voice "2RI_1102"
    rin "\"Nutrition? When you want to bake cakes?\""

    voice "2FU_0850"
    fumi "\"Yeah. I'm hoping to take that into account with my baking, instead of just making sweets that taste good.\""

    voice "2RI_1103"
    rin "\"Haahh... Cake that doesn't make you fat is an unobtainable dream, you know. It goes against the laws of the universe.\""

    voice "2FU_0851"
    fumi "\"...Rin? I never said anything about that.\""

    "Oh, that's a scary face."

    voice "2RI_1104"
    rin "\"I'm sorry, I'm sorry.\""

    voice "2FU_0852B"
    fumi "\"I want to make cakes that nobody else in the world makes. That's been my dream ever since I was little.\""

    voice "2RI_1105"
    rin "\"You're really serious about this, huh?\""

    voice "2FU_0853"
    fumi "\"Though I don't have any of the specifics planned yet.\""

    "Fumi smiled awkwardly. To do something that no one else in the world can is pretty cliché as dreams go, but I bet Fumi can get pretty close."

    voice "2RI_1106"
    rin "\"Are you gonna take over Chocolat? Or start a new store?\""

    voice "2FU_0854"
    fumi "\"I hope I can get some practice at Chocolat at first, but I don't see my dad quitting anytime soon, so I think I'll want my own store. Preferably not just a second Chocolat.\""

    voice "2FU_0855"
    fumi "\"By the way, did you do yours? We have to turn in our course plans soon.\""

    voice "2RI_1108"
    rin "\"I didn't, but I'll pick what you pick~\""

    voice "2FU_0856"
    fumi "\"You should take this seriously. You have the grades to pick either one, too.\""

    voice "2RI_1109"
    rin "\"Since I can pick either, I can do whatever you do~\""

    "True enough."

    voice "2FU_0857"
    fumi "\"Is there something you'd like to do in the future? Maybe become a college professor like your dad?\""

    voice "2RI_1110"
    rin "\"Not at all. Unlike you, I've never once seen my dad working.\""

    scene kimikara_08_e with Dissolve(0.5)

    voice "2FU_0858"
    fumi "\"......\""

    "As soon as the topic turned to her family, Rin's tone and attitude turned curt."

    "Fumi's face fell when that happened, but Rin didn't notice."

    voice "2RI_1111"
    rin "\"I'll be part of your family in the future~\""

    "So casual again."

    voice "2FU_0859"
    fumi "\"You should be serious about this...\""

    voice "2RI_1112"
    rin "\"I am serious~ Oh, maybe I'll get accounting qualifications and do the bookkeeping for your shop. Wonder what sort of qualifications you need to do accounting for a bakery. Could you ask your mom?\""

    voice "2FU_0860"
    fumi "\"Oh... okay.\""

    voice "2RI_1113"
    rin "\"We'll have a little shop, you baking and me behind the scenes.\""

    voice "2RI_1113a"
    rin "\"But I bet your sweets'll be really popular, so we'll have to expand the store to get more customers inside. Hmm, but then we won't have as much time alone...\""

    "Rin muttered to herself."

    voice "2RI_1114"
    rin "\"I know. I'll think of names for your sweets. I'll be the one who names the cakes no one else in the world can make♪\""

    voice "2FU_0861"
    fumi "\"......\""

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
    rin "\"Mon Bijou... No, Gyogyomu?\""

    voice "2FU_0862"
    fumi "\"I'm not ruining you, am I, Rin?\""

    voice "2RI_1116"
    rin "\"How d'you mean~? Sexually, maybe~\""

    "Rin just held Fumi harder and buried her face deeper into her chest."

    voice "2FU_0863"
    fumi "\"......\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou3_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
