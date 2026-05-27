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
    sachiko "\"Good work.\"" id a08_comn_11_4b7d42cf

    voice "2MI_0400"
    miyako "\"You too.\"" id a08_comn_11_ccd463e1

    "They'd finished their shoveling."

    "It wasn't hard work. All they had to do was move the snow closer to the gutters so that it didn't melt and leak through the roof."

    "This wasn't a region with heavy snowfall, so the two of them were enough to get the work done."

    show sachiko:
        "sachiko 1 sm outfit cigarette c" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0250"
    sachiko "\"You've got more stamina than I thought you would. Is it your youth?\"" id a08_comn_11_d365687b

    show sachiko 1 sm outfit cigarette c:
        xoffset 0 yoffset 0
    with None

    "Sachiko rolled a shoulder and took out a cigarette."

    show miyako 1 sm school_b_sei j with dict_dissolve_25

    voice "2MI_0401"
    miyako "\"No, I think it's just because of {i}that{/i}.\"" id a08_comn_11_f5b3474f

    "She pointed at Sachiko's cigarette."

    show sachiko 1 sm outfit cigarette d with dict_dissolve_25

    voice "2SA_0251"
    sachiko "\"Ahh, uhh, ahh...\"" id a08_comn_11_4502b50b

    show miyako 2 sm school_sei b with dict_dissolve_25

    voice "2MI_0402"
    miyako "\"......\"" id a08_comn_11_ee313d6e

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0252"
    sachiko "\"I shoulda picked a younger model, at least in looks. Then I could be wearing a uniform like you guys instead of being dorm manager~\"" id a08_comn_11_98fe2a6f

    show sachiko 1 sm outfit -cigarette d:
        xoffset 0 yoffset 0
    with None

    "She put the cigarette back."

    show miyako 1 sm school_a_sei c with dict_dissolve_25

    voice "2MI_0403"
    miyako "\"You can still wear one.\"" id a08_comn_11_eb5a7dc2

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0253"
    sachiko "\"Eh, I dunno about that. It'd just be cosplay. I'm sure Rin would have something to say about it.\"" id a08_comn_11_ae2e37f5

    "I could just picture her smirking."

    show miyako 1 sm school_a_sei g with dict_dissolve_25

    voice "2MI_0404"
    miyako "\"Who did you model yourself on?\"" id a08_comn_11_a4bfc06c

    "Angels don't really have a clear form."

    "That's why when they come down to earth, they have to borrow someone's appearance."

    "They call those people their \"models.\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0254"
    sachiko "\"The lady selling strawberries at the grocery store sampling corner.\"" id a08_comn_11_fe7934eb

    show miyako 2 sm school_sei a with dict_dissolve_25

    voice "2MI_0405"
    miyako "\"Hm? Did you have some connection to her?\"" id a08_comn_11_8d37bb4c

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0255"
    sachiko "\"Nope. Just someone I saw. Don't know anything about her.\"" id a08_comn_11_7eed23ff

    play sound se_fence

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0256"
    sachiko "\"Now that I'm thinking about it, I really didn't plan anything at all...\"" id a08_comn_11_0770229b

    show sachiko 1 sm outfit d:
        xoffset 0 yoffset 0
    with None

    "Sachiko lamented, back against the fence."

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0406"
    miyako "\"Well, I think she was very pretty.\"" id a08_comn_11_4d142651

    "Miyako told her, watching her profile as she looked up at the sky."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0257"
    sachiko "\"Yeah, well, I'm pretty fond of it.\"" id a08_comn_11_ad325a35

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0407"
    miyako "\"So am I.\"" id a08_comn_11_dbb13884

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0258"
    sachiko "\"O-Oh yeah? Thanks.\"" id a08_comn_11_50c22e25

    hide sachiko
    hide miyako
    with dict_dissolve_50

    play sound se_wind01
    pause 2.0

    "Wind blew on the mountains, shaking the evergreen trees."

    "......"

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0259"
    sachiko "\"Hey... uh...\"" id a08_comn_11_bdcf9af1

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0408"
    miyako "\"Yes?\"" id a08_comn_11_256f7066

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0260"
    sachiko "\"What about your model? Is it someone you had a connection to?\"" id a08_comn_11_4d82b01c

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0409"
    miyako "\"No, it's the same for me. I don't know her name.\"" id a08_comn_11_a6e47cd9

    $ side_image = "sachiko 2 side outfit a"

    voice "2SA_0261"
    sachiko "\"You don't...?\"" id a08_comn_11_675f78bf

    show miyako 1 sm school_b_sei b with dict_dissolve_25

    voice "2MI_0410"
    miyako "\"No. I saw her a few years ago before I came here, somewhere far away. And it was just once that I passed by her.\"" id a08_comn_11_49f5409b

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0262"
    sachiko "\"Huh... Guess we're both pretty careless.\"" id a08_comn_11_f66c2e7b

    show miyako 1 sm school_b_sei c with dict_dissolve_25

    voice "2MI_0411"
    miyako "\"She's the prettiest person in my memories, though.\"" id a08_comn_11_79de9f2a

    "Wow."

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0263"
    sachiko "\"...Hmm.\"" id a08_comn_11_72e51149

    show miyako 1 sm school_a_sei a with dict_dissolve_25

    voice "2MI_0412"
    miyako "\"You were the one who said it.\"" id a08_comn_11_c95ae46f

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0264"
    sachiko "\"What? Did I say something?\"" id a08_comn_11_0069ca7c

    show miyako 1 sm school_a_sei c with dict_dissolve_25

    voice "2MI_0413"
    miyako "\"Yes, when you invited me. You told me to come down with a pretty face, since looks are important to you.\"" id a08_comn_11_5a7ebf6a

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0265"
    sachiko "\"Oh... Guess I might've said something like that.\"" id a08_comn_11_c09c12e7

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0414"
    miyako "\"You did. That's why I made sure to choose well.\"" id a08_comn_11_78b7b87e

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0266"
    sachiko "\"Well, I'm glad I did. It's a good thing you didn't come down as a trilobite.\"" id a08_comn_11_53909066

    "Sachiko joked, scratching her temple."

    hide miyako
    show miyako 1 lg school_a_sei i as miyako_1
    with dict_dissolve_50

    voice "2MI_0415"
    miyako "\"So?\"" id a08_comn_11_b739ca4f

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0267"
    sachiko "\"Wh-What? You're kinda close.\"" id a08_comn_11_f868164b

    "Miyako brought her face in close to Sachiko's."

    show miyako 1 lg school_b_sei e as miyako_1 with dict_dissolve_25

    voice "2MI_0416"
    miyako "\"What do you think about it?\"" id a08_comn_11_186ac6ba

    $ side_image = "sachiko 2 side outfit g"

    voice "2SA_0268"
    sachiko "\"Huh? Oh... You're real cute. You'll probably be popular.\"" id a08_comn_11_84c6fe00

    show miyako 1 lg school_b_sei j as miyako_1 with dict_dissolve_25

    voice "2MI_0417"
    miyako "\"I don't mean objectively. I want to know if I suit {i}your{/i} tastes.\"" id a08_comn_11_c39fe450

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0269"
    sachiko "\"......\"" id a08_comn_11_533410bf

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0270"
    sachiko "\"...It's fine.\"" id a08_comn_11_800ccc47

    show miyako 2 lg school_sei e as miyako_1 with Dissolve(0.25)
    show miyako 2 lg school_sei e as miyako_1:
        ShakeTameiki

    voice "2MI_0418"
    miyako "\"Haah...\"" id a08_comn_11_3ab7c68e

    play sound se_fence

    hide miyako_1 with dict_dissolve_50

    "Miyako sighed and backed away, turning toward the fence."

    $ side_image = "miyako 2 side school_sei d"

    voice "2MI_0419"
    miyako "\"I guess I'm fine with it too, then.\"" id a08_comn_11_bc878ba8

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0271"
    sachiko "\"......\"" id a08_comn_11_39bf54f6

    "Miyako looked up at the sky through the fence. This time, it was Sachiko that watched her profile."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0272"
    sachiko "\"...Heh.\"" id a08_comn_11_eb316ca2

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
    miyako "\"What is—hah?!\"" id a08_comn_11_7d45dc7c

    show miyako 1 sm school_a_sei f:
        xoffset 0 yoffset 0
    with None

    "The second she turned, a clump of white burst against her cheek."

    show bg_obi
    show sachiko 1 lg outfit a at pos_l
    with dict_dissolve_50

    voice "2SA_0273"
    sachiko "\"How does your first snowball feel?\"" id a08_comn_11_8f710770

    "She'd balled up some snow still in the net of the fence."

    show sachiko 1 lg outfit f with dict_dissolve_25

    voice "2SA_0274"
    sachiko "\"Is it cold? But you like it anyway?\"" id a08_comn_11_e6b64514

    "Sachiko brushed the snow from her hands, an impish look on her face."

    show miyako 1 sm school_a_sei g with dict_dissolve_25

    voice "2MI_0421"
    miyako "\"......\"" id a08_comn_11_081f60e8

    show sachiko:
        "sachiko 1 lg outfit g" with Dissolve(0.25)
        3.0
        "sachiko 1 lg outfit h" with Dissolve(0.25)
        0.25
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    play sound ["<silence 3.0>",snowseize]
    voice "2SA_0275"
    sachiko "\"Ahaha, you look like you're still trying to figure out what happened—bhyah?!\"" id a08_comn_11_4d6e7864

    show sachiko 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    "Miyako threw some of the snow at the base of the fence, which rained down on Sachiko."

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0422"
    miyako "\"......\"" id a08_comn_11_38956274

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
    miyako "\"Yaaah!!\"" id a08_comn_11_01ab4af2

    "Having exhausted the snow in her territory, Miyako held the last of her ammunition in both hands and charged."

    stop music fadeout 1.0

    scene bg07aa with Dissolve(0.25)
    pause 0.75

    show miyako 1 lg school_a_sei f at default:
        0.25
        ShakeSide
    with dict_dissolve_25

    voice "2MI_0424"
    miyako "\"Wawah!\"" id a08_comn_11_5664c032

    show miyako 1 lg school_a_sei f:
        xoffset 0 yoffset 0
    with None
    hide miyako with dict_dissolve_25

    "But she lost her balance on the frozen ground just before enemy territory."

    show sachiko 1 lg outfit h with dict_dissolve_25

    voice "2SA_0276"
    sachiko "\"Ah... Whoa!\"" id a08_comn_11_3fb922e1

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
    miyako "\"It's the opposite of what happened before.\"" id a08_comn_11_5fdebd8c

    voice "2SA_0278"
    sachiko "\"Before?\"" id a08_comn_11_c9f20e10

    voice "2MI_0427"
    miyako "\"On Christmas... When I came down, I was on top.\"" id a08_comn_11_831fcd9f

    voice "2SA_0279"
    sachiko "\"It was more like you fell down.\"" id a08_comn_11_a7c556ce

    voice "2MI_0428"
    miyako "\"Ahaha. Sorry.\"" id a08_comn_11_95d6907f

    voice "2SA_0280"
    sachiko "\"......\"" id a08_comn_11_49018c76

    voice "2MI_0429"
    miyako "\"What is it?\"" id a08_comn_11_e31185fd

    voice "2SA_0281"
    sachiko "\"That scarf looks good on you.\"" id a08_comn_11_a4a7bd03

    voice "2MI_0430"
    miyako "\"Thank you.\"" id a08_comn_11_c7f37b82

    voice "2SA_0282"
    sachiko "\"Keep it. It's better that you wear it.\"" id a08_comn_11_7c037ff6

    voice "2MI_0431"
    miyako "\"Is that alright? Isn't it important to you?\"" id a08_comn_11_4e22935e

    voice "2SA_0283"
    sachiko "\"Just take good care of it.\"" id a08_comn_11_2e585de2

    voice "2MI_0432"
    miyako "\"...Alright.\"" id a08_comn_11_7528100d

    voice "2SA_0284"
    sachiko "\"...I lied before.\"" id a08_comn_11_e6ffa859

    voice "2MI_0433"
    miyako "\"Huh?\"" id a08_comn_11_16d5aa8f

    voice "2SA_0285"
    sachiko "\"When I said your face was fine...\"" id a08_comn_11_9441beef

    voice "2MI_0434"
    miyako "\"Oh...\"" id a08_comn_11_4fccb536

    voice "2SA_0286"
    sachiko "\"I like it... It's great.\"" id a08_comn_11_7feea11f

    voice "2MI_0435"
    miyako "\"Good. That makes me happy.\"" id a08_comn_11_4e3dea44

    voice "2SA_0287"
    sachiko "\"......\"" id a08_comn_11_1db5b459

    voice "2MI_0436"
    miyako "\"Huh? Umm...\"" id a08_comn_11_71b825c1

    "Sachiko brought her face in close."

    if routes_cleared >= 2:
        jump a08_comn_11_a
    else:
        jump a08_comn_11_b

label a08_comn_11_a:

    "They were close enough now for their breath to mingle."

    voice "2MI_0437"
    miyako "\"......\"" id a08_comn_11_a_37576318

    "But Miyako never looked away no matter how close she got."

    "There was no apprehension or bashfulness in her eyes, just acceptance of Sachiko right before her."

    voice "2SA_0288"
    sachiko "\"...Close your eyes.\"" id a08_comn_11_a_9e112141

    "—Guess that was too much for her."

    voice "2MI_0438"
    miyako "\"...Okay.\"" id a08_comn_11_a_c20882a6

    "Miyako did as she was told."

    scene kimikara_23_b with Dissolve(0.5)

    voice "2MI_0439"
    miyako "\"......\"" id a08_comn_11_a_d6dfc0ce

    "Her lips parted, trembling slightly, waiting for Sachiko's touch."

    voice "2SA_0289"
    sachiko "\"......\"" id a08_comn_11_a_cde02d69

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
    sachiko "\"...?!\"" id a08_comn_11_a_6a90b842

    "But she jumped back just before their lips could meet."

    "Her eyes were wide, lips trembling."

    voice "2SA_0291"
    sachiko "\"No—\"" id a08_comn_11_a_ee3ef335

    play sound se_wind02
    pause 0.5

    "A gust of wind stole away the rest of her words."

    scene kimikara_23_e with Dissolve(0.5)

    voice "2MI_0440"
    miyako "\"...?\"" id a08_comn_11_a_8f840f72

    "Miyako opened her eyes, sensing that something had happened."

    "Sachiko's eyes had lost the heat they'd had a moment ago and now swam with self-loathing."

    voice "2SA_0292"
    sachiko "\"...I'm sorry.\"" id a08_comn_11_a_5ab628ea

    voice "2MI_0441"
    miyako "\"...Sachiko?\"" id a08_comn_11_a_84e93f45

    jump a08_comn_11_b

label a08_comn_11_b:

    stop music fadeout 1.0

    $ side_image = "hina 1 side school_scarf c"

    voice "2HI_0553"
    hina "\"We're back~\"" id a08_comn_11_b_cab697fb

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
    hina "\"Done shoveling~?\"" id a08_comn_11_b_b08318c6

    "It was Hina. They could hear her voice from below."

    $ side_image = "rin 1 side school_scarf i"

    voice "2RI_0570"
    rin "\"You're so loud. Who yells up at someone on the roof?\"" id a08_comn_11_b_cc54a6d8

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0484"
    fumi "\"Ahaha, what if someone from the other dorm answered?\"" id a08_comn_11_b_bfdfef80

    $ side_image = "hina 1 side school_scarf k"

    voice "2HI_0555"
    hina "\"Well, I don't hear anything. Maybe they're already back inside?\"" id a08_comn_11_b_31fdd047

    "The three entered the dorm, plastic bags rustling."

    "Meanwhile, the two on the roof listened awkwardly, still on top of one another."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0294"
    sachiko "\"Sounds like they're back.\"" id a08_comn_11_b_4e8290ac

    $ side_image = "miyako 1 side school_a_sei g"

    voice "2MI_0443"
    miyako "\"Yes.\"" id a08_comn_11_b_12d34bb5

    "Sachiko got up timidly."

    "Miyako followed her."

    show sachiko 2 sm outfit d at pos_ls
    show miyako 2 sm school_sei b at pos_r2
    with dict_dissolve_25

    voice "2MI_0444"
    miyako "\"Umm...\"" id a08_comn_11_b_6b5f3297

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0295"
    sachiko "\"Ahaha, did I surprise you?\"" id a08_comn_11_b_37ea55d7

    "Sachiko cut off Miyako's words with her laughter."

    show miyako 2 sm school_sei f with dict_dissolve_25

    voice "2MI_0445"
    miyako "\"...A little.\"" id a08_comn_11_b_fbdf503b

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0296"
    sachiko "\"Come on, go change. You're all wet and cold, right?\"" id a08_comn_11_b_34cb3ce5

    show miyako 2 sm school_sei h with dict_dissolve_25

    voice "2MI_0446"
    miyako "\"Actually, I feel a little hot.\"" id a08_comn_11_b_39dbebfe

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0297"
    sachiko "\"Haha, well, we were moving around a lot.\"" id a08_comn_11_b_589479b0

    show miyako 2 sm school_sei d with dict_dissolve_25

    voice "2MI_0447"
    miyako "\"I suppose so...\"" id a08_comn_11_b_df6e3905

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0298"
    sachiko "\"Go down first. They're probably waiting for you.\"" id a08_comn_11_b_2dee7000

    show miyako 1 sm school_a_sei e with dict_dissolve_25

    voice "2MI_0448"
    miyako "\"What about you?\"" id a08_comn_11_b_b5e6c831

    voice "2SA_0299"
    sachiko "\"I'll be right behind you, after I clean this stuff up.\"" id a08_comn_11_b_4038f302

    show miyako 1 sm school_a_sei a with dict_dissolve_25

    voice "2MI_0449"
    miyako "\"I'll help you.\"" id a08_comn_11_b_4b90e6d9

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0300"
    sachiko "\"You don't need to, I got it. Come on, go, go!\"" id a08_comn_11_b_517e877f

    show miyako 2 sm school_sei e with dict_dissolve_25

    voice "2MI_0450"
    miyako "\"Alright.\"" id a08_comn_11_b_99ba8c84

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0301"
    sachiko "\"Mikoyan.\"" id a08_comn_11_b_f1b4a857

    show miyako 2 sm school_sei c with dict_dissolve_25

    voice "2MI_0451"
    miyako "\"Yes?\"" id a08_comn_11_b_5f186889

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0302"
    sachiko "\"Thanks for helping me shovel.\"" id a08_comn_11_b_fc684345

    show miyako 2 sm school_sei b with dict_dissolve_25

    voice "2MI_0452"
    miyako "\"You're welcome. See you in a bit.\"" id a08_comn_11_b_87ee059e

    hide miyako with Dissolve(0.5)
    pause 1.0

    "Miyako headed to the stairs."

    show sachiko 2 sm outfit d with dict_dissolve_25

    voice "2SA_0303"
    sachiko "\"...I screwed up.\"" id a08_comn_11_b_73e6b837

    "Sachiko picked up her shovel, scratching her head."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_12
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
