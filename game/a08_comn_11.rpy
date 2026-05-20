label a08_comn_11:

    play sound yukikaki
    pause 3.0

    scene bg07aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "The two of them looked out over the roof, shovels in hand."

    show sachiko 1 sm outfit a at pos_ls
    show miyako 1 sm school_a_sei b at pos_rs
    with dict_dissolve_25

    voice "2SA_0249"
    sachiko "\"Good work.\""

    voice "2MI_0400"
    miyako "\"You too.\""

    "They'd finished their shoveling."

    "It wasn't hard work. All they had to do was move the snow closer to the gutters so that it didn't melt and leak through the roof."

    "This wasn't a region with heavy snowfall, so the two of them were enough to get the work done."

    show sachiko:
        "sachiko 1 sm outfit cigarette c" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0250"
    sachiko "\"You've got more stamina than I thought you would. Is it your youth?\""

    show sachiko 1 sm outfit cigarette c:
        xoffset 0 yoffset 0
    with None

    "Sachiko rolled a shoulder and took out a cigarette."

    show miyako 1 sm school_b_sei j with dict_dissolve_25

    voice "2MI_0401"
    miyako "\"No, I think it's just because of {i}that{/i}.\""

    "She pointed at Sachiko's cigarette."

    show sachiko 1 sm outfit cigarette d with dict_dissolve_25

    voice "2SA_0251"
    sachiko "\"Ahh, uhh, ahh...\""

    show miyako 2 sm school_sei b with dict_dissolve_25

    voice "2MI_0402"
    miyako "\"......\""

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0252"
    sachiko "\"I shoulda picked a younger model, at least in looks. Then I could be wearing a uniform like you guys instead of being dorm manager~\""

    show sachiko 1 sm outfit -cigarette d:
        xoffset 0 yoffset 0
    with None

    "She put the cigarette back."

    show miyako 1 sm school_a_sei c with dict_dissolve_25

    voice "2MI_0403"
    miyako "\"You can still wear one.\""

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0253"
    sachiko "\"Eh, I dunno about that. It'd just be cosplay. I'm sure Rin would have something to say about it.\""

    "I could just picture her smirking."

    show miyako 1 sm school_a_sei g with dict_dissolve_25

    voice "2MI_0404"
    miyako "\"Who did you model yourself on?\""

    "Angels don't really have a clear form."

    "That's why when they come down to earth, they have to borrow someone's appearance."

    "They call those people their \"models.\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0254"
    sachiko "\"The lady selling strawberries at the grocery store sampling corner.\""

    show miyako 2 sm school_sei a with dict_dissolve_25

    voice "2MI_0405"
    miyako "\"Hm? Did you have some connection to her?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0255"
    sachiko "\"Nope. Just someone I saw. Don't know anything about her.\""

    play sound se_fence

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0256"
    sachiko "\"Now that I'm thinking about it, I really didn't plan anything at all...\""

    show sachiko 1 sm outfit d:
        xoffset 0 yoffset 0
    with None

    "Sachiko lamented, back against the fence."

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0406"
    miyako "\"Well, I think she was very pretty.\""

    "Miyako told her, watching her profile as she looked up at the sky."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0257"
    sachiko "\"Yeah, well, I'm pretty fond of it.\""

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0407"
    miyako "\"So am I.\""

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0258"
    sachiko "\"O-Oh yeah? Thanks.\""

    hide sachiko
    hide miyako
    with dict_dissolve_50

    play sound se_wind01
    pause 2.0

    "Wind blew on the mountains, shaking the evergreen trees."

    "......"

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0259"
    sachiko "\"Hey... uh...\""

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0408"
    miyako "\"Yes?\""

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0260"
    sachiko "\"What about your model? Is it someone you had a connection to?\""

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0409"
    miyako "\"No, it's the same for me. I don't know her name.\""

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0261"
    sachiko "\"You don't...?\""

    show miyako 1 sm school_b_sei b with dict_dissolve_25

    voice "2MI_0410"
    miyako "\"No. I saw her a few years ago before I came here, somewhere far away. And it was just once that I passed by her.\""

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0262"
    sachiko "\"Huh... Guess we're both pretty careless.\""

    show miyako 1 sm school_b_sei c with dict_dissolve_25

    voice "2MI_0411"
    miyako "\"She's the prettiest person in my memories, though.\""

    "Wow."

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0263"
    sachiko "\"...Hmm.\""

    show miyako 1 sm school_a_sei a with dict_dissolve_25

    voice "2MI_0412"
    miyako "\"You were the one who said it.\""

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0264"
    sachiko "\"What? Did I say something?\""

    show miyako 1 sm school_a_sei c with dict_dissolve_25

    voice "2MI_0413"
    miyako "\"Yes, when you invited me. You told me to come down with a pretty face, since looks are important to you.\""

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0265"
    sachiko "\"Oh... Guess I might've said something like that.\""

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0414"
    miyako "\"You did. That's why I made sure to choose well.\""

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0266"
    sachiko "\"Well, I'm glad I did. It's a good thing you didn't come down as a trilobite.\""

    "Sachiko joked, scratching her temple."

    hide miyako
    show miyako 1 lg school_a_sei i as miyako_1
    with dict_dissolve_50

    voice "2MI_0415"
    miyako "\"So?\""

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0267"
    sachiko "\"Wh-What? You're kinda close.\""

    "Miyako brought her face in close to Sachiko's."

    show miyako 1 lg school_b_sei e as miyako_1 with dict_dissolve_25

    voice "2MI_0416"
    miyako "\"What do you think about it?\""

    $ side_image = "sachiko 2 side outfit g"

    voice "2SA_0268"
    sachiko "\"Huh? Oh... You're real cute. You'll probably be popular.\""

    show miyako 1 lg school_b_sei j as miyako_1 with dict_dissolve_25

    voice "2MI_0417"
    miyako "\"I don't mean objectively. I want to know if I suit {i}your{/i} tastes.\""

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0269"
    sachiko "\"......\""

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0270"
    sachiko "\"...It's fine.\""

    show miyako 2 lg school_sei e as miyako_1 with Dissolve(0.25)
    show miyako 2 lg school_sei e as miyako_1:
        ShakeTameiki

    voice "2MI_0418"
    miyako "\"Haah...\""

    play sound se_fence

    hide miyako_1 with dict_dissolve_50

    "Miyako sighed and backed away, turning toward the fence."

    $ side_image = "miyako 2 side school_sei d"

    voice "2MI_0419"
    miyako "\"I guess I'm fine with it too, then.\""

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0271"
    sachiko "\"......\""

    "Miyako looked up at the sky through the fence. This time, it was Sachiko that watched her profile."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0272"
    sachiko "\"...Heh.\""

    "She laughed for some reason."

    show miyako 1 sm school_a_sei e at pos_r:
        1.0
        "miyako 1 sm school_a_sei f" with Dissolve(0.25)
        0.25
        function LayerShake(20,20,0.3)
    with dict_dissolve_25
    $ persistent.layer_shaken = False

    play sound ["<silence 0.99>",snowseize]

    voice "2MI_0420"
    miyako "\"What is—hah?!\""

    show miyako 1 sm school_a_sei f:
        xoffset 0 yoffset 0
    with None

    "The second she turned, a clump of white burst against her cheek."

    show bg_obi
    show sachiko 1 lg outfit a at pos_l
    with dict_dissolve_50

    voice "2SA_0273"
    sachiko "\"How does your first snowball feel?\""

    "She'd balled up some snow still in the net of the fence."

    show sachiko 1 lg outfit f with dict_dissolve_25

    voice "2SA_0274"
    sachiko "\"Is it cold? But you like it anyway?\""

    "Sachiko brushed the snow from her hands, an impish look on her face."

    show miyako 1 sm school_a_sei g with dict_dissolve_25

    voice "2MI_0421"
    miyako "\"......\""

    show sachiko:
        "sachiko 1 lg outfit g" with Dissolve(0.25)
        3.0
        "sachiko 1 lg outfit h" with Dissolve(0.25)
        0.25
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    play sound ["<silence 3.0>",snowseize]
    voice "2SA_0275"
    sachiko "\"Ahaha, you look like you're still trying to figure out what happened—bhyah?!\""

    show sachiko 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    "Miyako threw some of the snow at the base of the fence, which rained down on Sachiko."

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0422"
    miyako "\"......\""

    "She grinned. And..."

    hide bg_obi
    hide sachiko
    hide miyako
    with dict_dissolve_50

    play sound dash
    pause 1.0

    "They jumped apart, each running to different piles of snow."

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    "A snowball fight was suddenly upon them."

    "They gathered up snow and threw it, then again. And they'd just shoveled it all."

    "A little while ago, Sachiko was warning Miyako to get used to having a body without getting carried away by sensation."

    "—Basically telling her to be careful, since humans can catch colds."

    "And now, the two former angels were getting snow all over their hair and clothes, giggling and enjoying the cold."

    $ side_image = "miyako 1 side school_a_sei d"

    voice "2MI_0423"
    miyako "\"Yaaah!!\""

    "Having exhausted the snow in her territory, Miyako held the last of her ammunition in both hands and charged."

    stop music fadeout 1.0

    scene bg07aa with Dissolve(0.25)
    pause 0.75

    show miyako 1 lg school_a_sei f at default:
        0.25
        ShakeSide
    with dict_dissolve_25

    voice "2MI_0424"
    miyako "\"Wawah!\""

    show miyako 1 lg school_a_sei f:
        xoffset 0 yoffset 0
    with None
    hide miyako with dict_dissolve_25

    "But she lost her balance on the frozen ground just before enemy territory."

    show sachiko 1 lg outfit h with dict_dissolve_25

    voice "2SA_0276"
    sachiko "\"Ah... Whoa!\""

    "Sachiko reached out to prevent Miyako from falling, but the ground was too slippery to hold them both up."

    $ side_image = "miyako 1 side school_a_sei f"

    hide sachiko with dict_dissolve_25

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ voice2("miyako","2MI_0425","sachiko","2SA_0277")
    miyako_sachiko "\"Waaah!\"\n\"Whoooa!\"" (what_rest_indent=0)

    camera
    with None

    play sound se_2s_h004

    pause 0.5

    play music bgm08 fadein 1.0

    scene white with Dissolve(0.1875)
    pause 1.5625

    scene kimikara_23_a with Dissolve(0.5)
    pause 1.5

    "Sachiko fell over on top of Miyako. The two stared at each other."

    voice "2MI_0426"
    miyako "\"It's the opposite of what happened before.\""

    voice "2SA_0278"
    sachiko "\"Before?\""

    voice "2MI_0427"
    miyako "\"On Christmas... When I came down, I was on top.\""

    voice "2SA_0279"
    sachiko "\"It was more like you fell down.\""

    voice "2MI_0428"
    miyako "\"Ahaha. Sorry.\""

    voice "2SA_0280"
    sachiko "\"......\""

    voice "2MI_0429"
    miyako "\"What is it?\""

    voice "2SA_0281"
    sachiko "\"That scarf looks good on you.\""

    voice "2MI_0430"
    miyako "\"Thank you.\""

    voice "2SA_0282"
    sachiko "\"Keep it. It's better that you wear it.\""

    voice "2MI_0431"
    miyako "\"Is that alright? Isn't it important to you?\""

    voice "2SA_0283"
    sachiko "\"Just take good care of it.\""

    voice "2MI_0432"
    miyako "\"...Alright.\""

    voice "2SA_0284"
    sachiko "\"...I lied before.\""

    voice "2MI_0433"
    miyako "\"Huh?\""

    voice "2SA_0285"
    sachiko "\"When I said your face was fine...\""

    voice "2MI_0434"
    miyako "\"Oh...\""

    voice "2SA_0286"
    sachiko "\"I like it... It's great.\""

    voice "2MI_0435"
    miyako "\"Good. That makes me happy.\""

    voice "2SA_0287"
    sachiko "\"......\""

    voice "2MI_0436"
    miyako "\"Huh? Umm...\""

    "Sachiko brought her face in close."

    if routes_cleared >= 2:
        jump a08_comn_11_a
    else:
        jump a08_comn_11_b

label a08_comn_11_a:

    "They were close enough now for their breath to mingle."

    voice "2MI_0437"
    miyako "\"......\""

    "But Miyako never looked away no matter how close she got."

    "There was no apprehension or bashfulness in her eyes, just acceptance of Sachiko right before her."

    voice "2SA_0288"
    sachiko "\"...Close your eyes.\""

    "—Guess that was too much for her."

    voice "2MI_0438"
    miyako "\"...Okay.\""

    "Miyako did as she was told."

    scene kimikara_23_b with Dissolve(0.5)

    voice "2MI_0439"
    miyako "\"......\""

    "Her lips parted, trembling slightly, waiting for Sachiko's touch."

    voice "2SA_0289"
    sachiko "\"......\""

    "Sachiko brought her lips in once more—"

    pause 0.5

    window hide
    show white with Dissolve(0.15)
    scene white
    show kimikara_23_c at truecenter:
        alpha 0.0 zoom 1.0
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easeout 0.3 zoom 1.12
    pause 0.3
    scene white with Dissolve(0.3)
    pause 1.0
    scene kimikara_23_d with Dissolve(1.0)
    pause 1.0
    window auto

    voice "2SA_0290"
    sachiko "\"...?!\""

    "But she jumped back just before their lips could meet."

    "Her eyes were wide, lips trembling."

    voice "2SA_0291"
    sachiko "\"No—\""

    play sound se_wind02
    pause 0.5

    "A gust of wind stole away the rest of her words."

    scene kimikara_23_e with Dissolve(0.5)

    voice "2MI_0440"
    miyako "\"...?\""

    "Miyako opened her eyes, sensing that something had happened."

    "Sachiko's eyes had lost the heat they'd had a moment ago and now swam with self-loathing."

    voice "2SA_0292"
    sachiko "\"...I'm sorry.\""

    voice "2MI_0441"
    miyako "\"...Sachiko?\""

    jump a08_comn_11_b

label a08_comn_11_b:

    stop music fadeout 1.0

    $ side_image = "hina 1 side school_scarf c"

    voice "2HI_0553"
    hina "\"We're back~\""

    $ voice2("miyako","2MI_0442","sachiko","2SA_0293")
    miyako_sachiko "\"!\""

    play music bgm02 fadein 1.0

    pause 0.5

    scene white with Dissolve(0.1875)
    pause 1.5625

    scene bg07aa with Dissolve(0.1875)
    pause 1.0625

    $ side_image = "hina 1 side school_scarf l"

    voice "2HI_0554"
    hina "\"Done shoveling~?\""

    "It was Hina. They could hear her voice from below."

    $ side_image = "rin 1 side school_scarf i"

    voice "2RI_0570"
    rin "\"You're so loud. Who yells up at someone on the roof?\""

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0484"
    fumi "\"Ahaha, what if someone from the other dorm answered?\""

    $ side_image = "hina 1 side school_scarf k"

    voice "2HI_0555"
    hina "\"Well, I don't hear anything. Maybe they're already back inside?\""

    "The three entered the dorm, plastic bags rustling."

    "Meanwhile, the two on the roof listened awkwardly, still on top of one another."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0294"
    sachiko "\"Sounds like they're back.\""

    $ side_image = "miyako 1 side school_a_sei g"

    voice "2MI_0443"
    miyako "\"Yes.\""

    "Sachiko got up timidly."

    "Miyako followed her."

    show sachiko 2 sm outfit d at pos_ls
    show miyako 2 sm school_sei b at pos_r2
    with dict_dissolve_25

    voice "2MI_0444"
    miyako "\"Umm...\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0295"
    sachiko "\"Ahaha, did I surprise you?\""

    "Sachiko cut off Miyako's words with her laughter."

    show miyako 2 sm school_sei f with dict_dissolve_25

    voice "2MI_0445"
    miyako "\"...A little.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0296"
    sachiko "\"Come on, go change. You're all wet and cold, right?\""

    show miyako 2 sm school_sei h with dict_dissolve_25

    voice "2MI_0446"
    miyako "\"Actually, I feel a little hot.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0297"
    sachiko "\"Haha, well, we were moving around a lot.\""

    show miyako 2 sm school_sei d with dict_dissolve_25

    voice "2MI_0447"
    miyako "\"I suppose so...\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0298"
    sachiko "\"Go down first. They're probably waiting for you.\""

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0448"
    miyako "\"What about you?\""

    voice "2SA_0299"
    sachiko "\"I'll be right behind you, after I clean this stuff up.\""

    show miyako 1 sm school_a_sei a with dict_dissolve_25

    voice "2MI_0449"
    miyako "\"I'll help you.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0300"
    sachiko "\"You don't need to, I got it. Come on, go, go!\""

    show miyako 2 sm school_sei e with dict_dissolve_25

    voice "2MI_0450"
    miyako "\"Alright.\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0301"
    sachiko "\"Mikoyan.\""

    show miyako 2 sm school_sei c with dict_dissolve_25

    voice "2MI_0451"
    miyako "\"Yes?\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0302"
    sachiko "\"Thanks for helping me shovel.\""

    show miyako 2 sm school_sei b with dict_dissolve_25

    voice "2MI_0452"
    miyako "\"You're welcome. See you in a bit.\""

    hide miyako with Dissolve(0.5)
    pause 1.0

    "Miyako headed to the stairs."

    show sachiko 2 sm outfit d with dict_dissolve_25

    voice "2SA_0303"
    sachiko "\"...I screwed up.\""

    "Sachiko picked up her shovel, scratching her head."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
