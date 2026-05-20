label a07_cou2_02:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "fumi 1 side casual b"

    voice "2FU_0219"
    fumi "\"Can I ask you to come shopping with me, Takaoka?\""

    "Fumi asked as they waited for the red light."

    show fumi 1 lg casual a at pos_l
    show miyako 1 lg casual_a e at pos_r
    with dict_dissolve_25

    voice "2MI_0208"
    miyako "\"Just me? What about you two?\""

    "Miyako turned back to Hina and Rin."

    $ side_image = "rin 1 side casual b"

    voice "2RI_0233"
    rin "\"Umm, Hina and I have something else to do. Right?\""

    $ side_image = "hina 2 side casual_scarf h"

    voice "2HI_0252"
    hina "\"...Yeah.\""

    "She looked up at Miyako with the gaze of an imploring puppy."

    show miyako 1 lg casual_a c with dict_dissolve_25

    voice "2MI_0209"
    miyako "\"Ah. Alright, I'll come with you.\""

    $ side_image = "hina 1 side casual_scarf c"

    voice "2HI_0253"
    hina "\"Thank you!\""

    "Hina's expression lit up at that."

    $ side_image = "rin 2 side casual e"

    voice "2RI_0234"
    rin "\"Thank you, she says.\""

    show miyako 1 lg casual_a d with dict_dissolve_25

    voice "2MI_0210"
    miyako "\"Ahaha.\""

    hide fumi
    hide miyako
    with Dissolve(0.5)

    show hina 2 sm casual_scarf a:
        xcenter 382
    show rin 2 sm casual a:
        xcenter 642
    with dict_dissolve_25

    voice "2RI_0235"
    rin "\"Well, we'll see you guys later, then.\""

    $ side_image = "fumi 2 side casual h"

    voice "2FU_0220"
    fumi "\"Say, two hours?\""

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0236"
    rin "\"Is that okay?\""

    $ side_image = "miyako 1 side casual_b b"

    voice "2MI_0211"
    miyako "\"If you could give me a tour of the town while we shop, I'd like that.\""

    $ side_image = "fumi 2 side casual i"

    voice "2FU_0221"
    fumi "\"I'd be happy to.\""

    show rin 1 sm casual e with dict_dissolve_25

    voice "2RI_0237"
    rin "\"Ah...\""

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0254"
    hina "\"The light's green.\""

    "Hina was already halfway across the street."

    show rin:
        "rin 1 sm casual c" with Dissolve(0.25)
        ShakeYes

    voice "2RI_0238"
    rin "\"Umm... right, thank you.\""

    hide rin
    hide hina
    with dict_dissolve_50

    "With a quick bow of her head, Rin chased after Hina."

    $ side_image = "rin 1 side casual g"

    voice "2RI_0239"
    rin "\"Don't cling like that. It's hard to walk!\""

    $ side_image = "hina 2 side casual_scarf g"

    voice "2HI_0255"
    hina "\"Eheheh♪\""

    "Once Rin had caught up to her, Hina put her arms around her and clung on."

    "Fumi and Miyako waved as they left."

    show fumi 1 lg casual a at pos_l
    show miyako 1 lg casual_a b at pos_r
    with dict_dissolve_25

    voice "2MI_0212"
    miyako "\"They're very close, aren't they?\""

    voice "2FU_0222"
    fumi "\"Yes, they are.\""

    show miyako 2 lg casual c with dict_dissolve_25

    voice "2MI_0213"
    miyako "\"I'm sorry for not catching on earlier.\""

    show fumi 2 lg casual c with dict_dissolve_25

    voice "2FU_0223"
    fumi "\"Don't be! I think you actually caught on very quickly.\""

    show fumi 2 lg casual h with dict_dissolve_25

    voice "2FU_0224"
    fumi "\"It might be strange for me to be the one to tell you this, but Natsume and Ogata are—\""

    show miyako 1 lg casual_a b with dict_dissolve_25

    voice "2MI_0214"
    miyako "\"They're dating, right?\""

    show fumi 1 lg casual d with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "2FU_0225"
    fumi "\"...It's easy to tell, isn't it? Oh, but it's not as if they're hiding it or anything.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show miyako 1 lg casual_a c with dict_dissolve_25

    voice "2MI_0215"
    miyako "\"Yes. The air between them is a little warm.\""

    "She couldn't exactly tell her she'd been watching them since their relationship began."

    show fumi 2 lg casual h with dict_dissolve_25

    voice "2FU_0226"
    fumi "\"Does it bother you?\""

    show miyako 1 lg casual_b g with dict_dissolve_25

    voice "2MI_0216"
    miyako "\"What do you mean by that?\""

    show fumi 2 lg casual a with dict_dissolve_25

    voice "2FU_0227"
    fumi "\"Well, do you think it's awkward living together with a couple...?\""

    show fumi 2 lg casual h with dict_dissolve_25

    voice "2FU_0228"
    fumi "\"I've been with them from the beginning, and I think they're rather adorable to watch...\""

    show miyako 1 lg casual_b c with dict_dissolve_25

    voice "2MI_0217"
    miyako "\"I enjoy seeing them together too.\""

    show fumi 2 lg casual i with dict_dissolve_25

    voice "2FU_0229"
    fumi "\"...I'm glad you became our new roommate, Takaoka. I hope you'll continue to watch over them fondly from now on.\""

    show miyako 2 lg casual c with dict_dissolve_25

    voice "2MI_0218"
    miyako "\"I'm glad, too. I wanted to be your roommate...\""

    show miyako 2 lg casual f with dict_dissolve_25

    "Miyako stopped, realizing she'd said something she shouldn't have, but fortunately, Fumi didn't seem to have noticed."

    show fumi 1 lg casual a with dict_dissolve_25

    voice "2FU_0230"
    fumi "\"Should we take a walk by the station?\""

    "Fumi headed in the opposite direction Rin and Hina had gone, Miyako following."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg11aa with bg_effect_05
    pause 0.5

    show fumi 1 sm casual a at pos_ls
    show miyako 2 sm casual a at pos_rs
    with dict_dissolve_25

    voice "2MI_0219"
    miyako "\"Are Natsume and Ogata going on a date somewhere?\""

    show fumi 1 sm casual b with dict_dissolve_25

    voice "2FU_0231"
    fumi "\"I think they probably went back to the room. Natsume's been looking a little forlorn lately.\""

    show miyako 2 sm casual b with dict_dissolve_25

    voice "2MI_0220"
    miyako "\"It must be because I suddenly moved in.\""

    show fumi 2 sm casual g with dict_dissolve_25

    voice "2FU_0232"
    fumi "\"No, no, it's not your fault. If it were, then it would be mine, too.\""

    "Fumi waved her hands, denying Miyako's suggestion."

    show fumi 2 sm casual f with dict_dissolve_25

    voice "2FU_0233"
    fumi "\"We're all glad you moved in!\""

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0221"
    miyako "\"Th... Thank you.\""

    show fumi 1 sm casual d with dict_dissolve_25

    voice "2FU_0234"
    fumi "\"They're just in the early stage of their relationship where they want to spend time with each other, and they've got a low charge on their battery right now.\""

    show fumi 1 sm casual b with dict_dissolve_25

    voice "2FU_0235"
    fumi "\"They can't be alone together all that much since it's a four-person room, and they weren't able to cuddle much at our New Year's sleepover...\""

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0222"
    miyako "\"You want to give them time alone together every so often, yes? I'm fine with that at any time.\""

    show fumi 2 sm casual g with Dissolve(0.25)
    show fumi:
        2.3
        "fumi 2 sm casual i" with Dissolve(0.25)

    voice "2FU_0236"
    fumi "\"...Thanks. I'll take you up on that.\""

    show fumi 2 sm casual i:
        pass
    with None
    show fumi 2 sm casual b with dict_dissolve_25

    voice "2FU_0237"
    fumi "\"I'm very impressed by you, Takaoka. You seem to see through everything.\""

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0223"
    miyako "\"I'm impressed by you, too. You really watch them closely, don't you? I bet you know exactly what Natsume's thinking.\""

    show fumi 1 sm casual d with dict_dissolve_25

    voice "2FU_0238"
    fumi "\"Probably better than Ogata does, honestly. Sometimes I think I should just mind my own business, but...\""

    show miyako 1 sm casual_a h with dict_dissolve_25

    voice "2MI_0224"
    miyako "\"You're like their big sister.\""

    show fumi 1 sm casual b with dict_dissolve_25

    voice "2FU_0239"
    fumi "\"I'm relieved you didn't say 'mother.'\""

    show miyako 1 sm casual_a d with dict_dissolve_25

    voice "2MI_0225"
    miyako "\"Ahaha.\""

    "Rin would have said that."

    show fumi 1 sm casual f with dict_dissolve_25

    voice "2FU_0240"
    fumi "\"Well, I am a little older than them. I was born in April. Natsume's birthday is in December, and Ogata's is in March.\""

    show miyako 1 sm casual_a h with dict_dissolve_25

    voice "2MI_0226"
    miyako "\"I was also born in December, so you're my big sister, too.\""

    show fumi 2 sm casual c with dict_dissolve_25

    voice "2FU_0241"
    fumi "\"Should I call you Miyako, then?\""

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0227"
    miyako "\"I would like that, Fumi.\""

    "They smiled."

    show fumi 2 sm casual g with dict_dissolve_25

    voice "2FU_0242"
    fumi "\"Is your name written 'holy night' because you were born on Christmas?\""

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0228"
    miyako "\"Yes.\""

    show fumi 2 sm casual i with Dissolve(0.25)
    show fumi:
        1.5
        "fumi 1 sm casual e" with Dissolve(0.25)
        ShakeJump

    voice "2FU_0243"
    fumi "\"I thought s—wah!\""

    show fumi 1 sm casual e:
        xoffset 0 yoffset 0
    with None

    "Fumi suddenly exclaimed."

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0229"
    miyako "\"Is something—\""

    play sound se_2s_d011

    hide fumi with dict_dissolve_50

    "Fumi ran off before Miyako could find what she was looking at."

    voice "2MI_0230"
    miyako "\"...A toy store?\""

    pause 0.5

    scene white with bg_effect_12
    pause 1.5

    scene bg11aa with bg_effect_12
    pause 0.5

    "Among the shuttered stores all down the main street, this small toy store alone was open, anticipating children's New Year's money."

    "There were stuffed animals in a cart outside the store, and Fumi was picking up each one of them and saying something to them."

    show fumi 1 lg casual e at pos_l with dict_dissolve_25

    voice "2FU_0244"
    fumi "\"I never thought I'd see you here!\""

    "Miyako peered into the cart when she caught up with Fumi."

    show miyako 2 lg casual a at pos_r with dict_dissolve_25

    voice "2MI_0231"
    miyako "\"These look like the stuffed animals in our room.\""

    show fumi 2 lg casual i with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_0245"
    fumi "\"They are! These are their family!\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2FU_0245a"
    fumi "\"This is Uri, Micha's cousin, and this is Meta, and this is San. He's Gabe's classmate, but they're actually twins—\""

    show miyako 1 lg casual_b b with dict_dissolve_25

    voice "2MI_0232"
    miyako "\"It's a big family, isn't it?\""

    show fumi:
        ShakeYes
        3.5
        "fumi 2 lg casual d" with Dissolve(0.25)
        1.2
        "fumi 1 lg casual j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2FU_0246"
    fumi "\"It is! But they all get along... wait? Ah?! Oh!\""

    show fumi 1 lg casual j:
        xoffset 0 yoffset 0
    with None

    "She finally came to her senses."

    show fumi:
        "fumi 1 lg casual k" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_0247"
    fumi "\"I-I'm sorry! I got carried away.\""

    show fumi 1 lg casual k:
        xoffset 0 yoffset 0
    with None
    show miyako 1 lg casual_a d with dict_dissolve_25

    voice "2MI_0233"
    miyako "\"Ahaha. You really love these stuffed animals, don't you, Fumi?\""

    show miyako:
        "miyako 1 lg casual_a b" with Dissolve(0.25)
        ShakeYes

    "Miyako picked one of them up."

    show miyako 1 lg casual_a b:
        xoffset 0 yoffset 0
    with None
    show miyako 1 lg casual_a g with dict_dissolve_25

    voice "2MI_0234"
    miyako "\"Ooh...\""

    "Miyako exclaimed in wonder at the feel of the stuffed animal."

    show fumi 2 lg casual i with dict_dissolve_25

    voice "2FU_0248"
    fumi "\"They're so soft, aren't they? I love that about Angel Zoo.\""

    show miyako 2 lg casual a with dict_dissolve_25

    voice "2MI_0235"
    miyako "\"Angel Zoo...? Ah, that's what these stuffed animals are called? Uri and San, too?\""

    "Miyako looked at the toys' tags."

    show fumi 1 lg casual d with dict_dissolve_25

    voice "2FU_0249"
    fumi "\"Err... the names are just what I call them.\""

    show miyako 2 lg casual c with dict_dissolve_25

    voice "2MI_0236"
    miyako "\"They're very cute. But you don't have these ones in our room, do you?\""

    show fumi 1 lg casual a with dict_dissolve_25

    voice "2FU_0250"
    fumi "\"These were just released this winter. I always keep on top of the new information, but I've never seen them in stores around here.\""

    show miyako 1 lg casual_a c with dict_dissolve_25

    voice "2MI_0237"
    miyako "\"They must have been waiting for you here.\""

    show fumi 1 lg casual c with dict_dissolve_25

    voice "2FU_0251"
    fumi "\"You're right! I'm going to bring them home! Do you mind waiting for me?\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg11aa with bg_effect_05
    pause 0.5

    "They began walking again, this time with Fumi carrying a large bag."

    show fumi 1 sm casual d at pos_ls
    show miyako 1 sm casual_a b at pos_rs
    with Dissolve(0.25)

    show fumi:
        ShakeTameiki

    voice "2FU_0252"
    fumi "\"...Sorry your big sister doesn't have any self-control.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "She must have bought all the new releases."

    show miyako 1 sm casual_a h with dict_dissolve_25

    voice "2MI_0238"
    miyako "\"But I bet the ones in our room will be happy to have a bigger family.\""

    show fumi:
        "fumi 2 sm casual i" with Dissolve(0.25)
        1.2
        "fumi 2 sm casual h" with Dissolve(0.25)

    voice "2FU_0253"
    fumi "\"Right?! ...I'm sure Ogata's going to get on my case about where I'm going to put them, though.\""

    show fumi 2 sm casual h:
        pass
    with None

    "She'd actually just made Fumi send some home at the end of the year due to overcrowding."

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0239"
    miyako "\"Would you like to use my shelves? I have extra space.\""

    "She didn't have a lot of things yet, since she'd just \"moved.\""

    show fumi 2 sm casual i with dict_dissolve_25

    voice "2FU_0254"
    fumi "\"You're an angel, Miyako!\""

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0240"
    miyako "\"Huh?\""

    "No, no. She means you're an angel, like a good person."

    show fumi 1 sm casual c with dict_dissolve_25

    voice "2FU_0255"
    fumi "\"Uri, Meta, San, you can all stay together~\""

    "Naturally, Fumi didn't catch on to Miyako's misunderstanding, instead talking to the stuffed animals in her bag."

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0241"
    miyako "\"Your stuffed animals are all named after angels, huh?\""

    show fumi:
        "fumi 1 sm casual e" with Dissolve(0.25)
        ShakeJump

    voice "2FU_0256"
    fumi "\"What? You know them?!\""

    show fumi 1 sm casual e:
        xoffset 0 yoffset 0
    with None
    show miyako 1 sm casual_b c with dict_dissolve_25

    voice "2MI_0242"
    miyako "\"Uriel, Metatron, Sandalphon... It's the same for the ones in the room, right?\""

    "In reality, angels have no names. Miyako herself had been a nameless soul before she came down to earth and was named by Sachiko."

    "There was no hierarchy of angels and archangels, either. Humans had come up with all of that. They were all the same kind of existence."

    show fumi 2 sm casual g with dict_dissolve_25

    voice "2FU_0257"
    fumi "\"You believe in angels, right, Miyako? You said before you'd seen them...\""

    show miyako 1 sm casual_b b with dict_dissolve_25

    voice "2MI_0243"
    miyako "\"Yes. Just that I felt like I had, though.\""

    show fumi 2 sm casual c with dict_dissolve_25

    voice "2FU_0258B"
    fumi "\"U-Umm! I also saw one, when I was little—\""

    show fumi 2 sm casual h with dict_dissolve_25

    "Her usual excitement threatened to well up again, but she covered her own mouth. She was trying to show a little restraint toward her new friend."

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0244"
    miyako "\"It's alright. Please tell me.\""

    "Miyako smiled."

    show fumi 2 sm casual g with dict_dissolve_25

    voice "2FU_0259"
    fumi "\"You don't mind?\""

    show miyako 1 sm casual_b h with dict_dissolve_25

    voice "2MI_0245"
    miyako "\"I believe, too.\""

    "Fumi's eyes sparkled."

    show fumi 1 sm casual c with dict_dissolve_25

    voice "2FU_0260"
    fumi "\"U-Umm, so, the first time I saw an angel—\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_cou2_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
