label a08_comn_05:

    scene white with Dissolve(0.5)
    pause 2.0

    scene kimikara_02_a with Dissolve(0.5)
    pause 1.5

    play music bgm06 fadein 1.0

    play sound se_2s_j028

    voice "2HI_0466"
    hina "\"Look, it's snowing!\""

    play sound se_2s_h043

    "Hina looked excitedly out the window."

    "The difference in temperature between inside and outside made it fog up quickly, but every time she poured hot water on it, she could see the snow swirling outside."

    voice "2FU_0427"
    fumi "\"Watching the snow from a bath, how romantic.\""

    voice "2MI_0333"
    miyako "\"It feels very luxurious to soak in a hot bath while watching cold snow fall.\""

    "Like having ice cream at a heated table?"

    voice "2HI_0467"
    hina "\"It's like an outdoor hot spring.\""

    voice "2RI_0496"
    rin "\"Haahh... How many times has it snowed this winter already? And it's just the backyard out the window. Seen it.\""

    voice "2HI_0468"
    hina "\"Yeesh... You're so jaded. It's different when the situation is different!\""

    voice "2RI_0497"
    rin "\"I'm just glad we don't have to go next door to take baths anymore. We could've gotten lost over there.\""

    voice "2HI_0469"
    hina "\"That's a bit of an exaggeration, isn't it? It's not some hidden hot spring on a mountain.\""

    voice "2FU_0428"
    fumi "\"Eheh, it's fun getting to all go in together.\""

    voice "2HI_0470"
    hina "\"Yeah, big baths are great, you can really relax. It was too small before the construction. And run-down!\""

    "Before the construction, the room could only fit two people, and the bath could only fit one."

    "While one was in the bath, the other would have to wash up and wait her turn."

    voice "2RI_0498"
    rin "\"There's a lot of stuff other than the bath I'd like fixed...\""

    voice "2FU_0429"
    fumi "\"This is the oldest building on the campus.\""

    voice "2RI_0499"
    rin "\"Maybe it'd be easier to just rebuild the whole thing.\""

    voice "2FU_0430"
    fumi "\"Also, Sachiko said she's been managing it for five years.\""

    voice "2RI_0500"
    rin "\"How old is she?\""

    voice "2MI_0334"
    miyako "\"I wonder.\""

    voice "2RI_0501"
    rin "\"You don't know even though you're cousins?\""

    "Angels didn't have much of a sense of age. They either guessed or used how many years they'd been human."

    voice "2MI_0335"
    miyako "\"Oh, but her birthday is Christmas Eve.\""

    voice "2FU_0431"
    fumi "\"What? It is?!\""

    voice "2HI_0471"
    hina "\"Why didn't she tell us? We would have celebrated.\""

    voice "2RI_0502"
    rin "\"What's yours, Mikoyan?\""

    voice "2MI_0336"
    miyako "\"Oh, mine is Christmas Eve, too.\""

    voice "2HI_0472"
    hina "\"Why didn't you tell us?\""

    voice "2RI_0503"
    rin "\"Well, we can celebrate for all three of you next year.\""

    voice "2HI_0473"
    hina "\"Mine's on the 5th! It's different!\""

    "She's mad."

    voice "2MI_0337"
    miyako "\"Hya?\""

    "Miyako yelped."

    voice "2HI_0474"
    hina "\"What happened?\""

    voice "2MI_0338"
    miyako "\"Umm, something touched my leg.\""

    voice "2FU_0432"
    fumi "\"Oh, that's just the ducky.\""

    "A rubber ducky floated in the tub."

    voice "2MI_0339"
    miyako "\"What is it?\""

    "Miyako poked the ducky's head."

    voice "2HI_0475"
    hina "\"Probably just Sachiko messing around. Oh, and we checked it for a hidden camera, so don't worry.\""

    voice "2MI_0340"
    miyako "\"I see.\""

    "Miyako removed her finger and the ducky floated off again."

    scene kimikara_02_b with Dissolve(0.5)

    voice "2RI_0504"
    rin "\"Anyway, I'd rather enjoy the view in here than look at the snow outside.\""

    "Rin said, eyes glinting as she wiped off her glasses."

    voice "2RI_0505"
    if persistent.dpatch:
        rin "\"Two of the prettiest girls in the school in the nude. It's truly heaven for the eyes. I'm so glad I'm a girl and rooming with you.\"" id a08_comn_05_cc08b12d
    else:
        rin "\"Two of the prettiest girls in the academy in the nude. It's truly heaven for the eyes. I'm so glad I'm a girl and rooming with you.\""

    voice "2HI_0476"
    hina "\"Hey, don't look at your roommates impurely!\""

    voice "2RI_0506"
    rin "\"What do you think I brought my glasses for—augh, get outta here, you dirty bird!\""

    "Rin splashed away the ducky that had floated over to bump into her chest."

    voice "2HI_0477"
    hina "\"You're the dirty one!\""

    voice "2RI_0507"
    rin "\"Boobs, boobs, skip that one, and boobs.\""

    voice "2HI_0478"
    hina "\"Hey! Yours aren't that big either!\""

    voice "2RI_0508"
    rin "\"Huge boobs, big boobs, skip that one, beautiful boobs.\""

    voice "2HI_0479"
    hina "\"Youuuu!!\""

    play sound se_2s_h030

    voice "2MI_0341"
    miyako "\"What sort of face are you supposed to make at a time like this, Fumi?\""

    voice "2FU_0433"
    fumi "\"Ahaha... I'm not sure.\""

    if route2 == 1:
        jump a08_comn_05_a
    elif route2 == 2:
        jump a08_comn_05_b
    elif route2 == 3:
        jump a08_comn_05_c

label a08_comn_05_a:

    play sound se_2s_h042

    voice "2HI_0480"
    hina "\"Don't even look at Fumi!\""

    "Hina splashed Rin with bathwater."

    voice "2RI_0509"
    rin "\"Bbbbh! What the heck, Stingy?\""

    voice "2HI_0481"
    hina "\"I'm not being stingy! You're making her uncomfortable!\""

    voice "2RI_0510"
    rin "\"Huh? Asou, are you uncomfortable?\""

    voice "2FU_0434"
    fumi "\"Umm... I'm a little embarrassed.\""

    voice "2RI_0511"
    rin "\"She said she's just a little embarrassed.\""

    voice "2HI_0482"
    hina "\"That means she's uncomfortable!\""

    voice "2RI_0512"
    rin "\"Those boobs don't belong to you, you know.\""

    voice "2HI_0483"
    hina "\"They do!\""

    voice "2MI_0342"
    miyako "\"Wow.\""

    voice "2RI_0513"
    rin "\"It's not like I'm taking them from you just by looking at them a little~\""

    voice "2HI_0484"
    hina "\"Fumi, I can hit her, right?!\""

    voice "2FU_0435"
    fumi "\"Ahaha...\""

    play sound se_2s_h001

    jump a08_comn_05_d

label a08_comn_05_b:

    voice "2RI_0514"
    rin "\"Swipe~\""

    "Rin took advantage of Hina's excitement to take a swipe at her butt."

    voice "2HI_0485"
    hina "\"Aaah!\""

    "Hina jumped up with a cute shriek."

    voice "2RI_0515"
    rin "\"Yeah, you've definitely got the smallest, cutest butt.\""

    "How does she say stuff like this with a straight face?"

    voice "2HI_0486"
    hina "\"D-D-Don't do that in front of people!\""

    "She said, but her face was flushed and she clearly wasn't putting up a fight."

    voice "2RI_0516RE"
    rin "\"But I can do it otherwise?\""

    voice "2HI_0487"
    hina "\"I-If you want to...\""

    "She looked down, blushing."

    voice "2MI_0343"
    miyako "\"Oho.\""

    voice "2FU_0436"
    fumi "\"Wawawah, no, that's too much!\""

    jump a08_comn_05_d

label a08_comn_05_c:

    voice "2RI_0517"
    rin "\"It's steamy, but you're looking pretty sexy too, Fumi.\""

    "Rin pushed her glasses up."

    voice "2FU_0437"
    fumi "\"Umm, it's pretty embarrassing when you stare like that.\""

    voice "2RI_0518"
    rin "\"Oh, it's fine, isn't it?\""

    "Not a hint of guilt."

    voice "2FU_0438"
    fumi "\"Aah! Hey!\""

    "To make matters worse, her toes reached out to poke Fumi's thigh underwater."

    voice "2FU_0439"
    fumi "\"You need to be punished. Yah!\""

    voice "2RI_0519"
    rin "\"Wah?!\""

    "Fumi grabbed Rin's ankle and pushed deep into a pressure point on the bottom of her foot."

    voice "2RI_0520"
    rin "\"Gyaaa! Ow, ow!\""

    voice "2HI_0488"
    hina "\"Don't masochists like pain? It's not really punishment then, is it?\""

    voice "2RI_0521"
    rin "\"No! Uhh! This is...! Not that kind of pain! It's not like just anything wooorks!!\""

    voice "2MI_0344"
    miyako "\"I see~\""

    voice "2HI_0489"
    hina "\"Ahaha, get 'er good.\""

    voice "2RI_0522"
    rin "\"Forgive me! I'm sorry, I'm sorry, I'm sorryyy!!\""

    voice "2FU_0440"
    fumi "\"What should I do~♪\""

label a08_comn_05_d:

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene kimikara_02_a with bg_effect_05
    pause 0.5

    play sound se_2s_h048

    voice "2HI_0490"
    hina "\"Miyako, your back...\""

    voice "2MI_0345"
    miyako "\"Huh? Is there something on my back?\""

    "Miyako was about to leave the bath, but she turned around at Hina's voice."

    voice "2HI_0491"
    hina "\"You've got birthmarks.\""

    voice "2MI_0346"
    miyako "\"Birthmarks...\""

    "She tried to look at her own back over her shoulder, a mystified look on her face."

    voice "2RI_0523"
    rin "\"Hey, she might be sensitive about it. Nice tact.\""

    "Rin poked Hina in the hip."

    voice "2HI_0492"
    hina "\"Oh, I'm sorry!\""

    voice "2MI_0347"
    miyako "\"No, it's fine... I didn't know.\""

    voice "2FU_0441"
    fumi "\"They're really faint. They almost just look like your shoulder blades.\""

    voice "2MI_0348"
    miyako "\"Do they...\""

    voice "2HI_0493"
    hina "\"It's almost like you had wings.\""

    voice "2MI_0349"
    miyako "\"Ah...\""

    "She's sharp."

    "She really did have wings. The marks on her back were proof that she was once an angel."

    voice "2MI_0350"
    miyako "\"......\""

    voice "2RI_0524"
    rin "\"And you've still got your Mongolian spot on your butt, Hina.\""

    voice "2HI_0494"
    hina "\"What?! No way!\""

    "Hina spun around to check her butt."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
