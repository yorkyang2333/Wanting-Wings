label a09_cou1_06:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "As soon as the bakery Le Chocolat Chocolat opened, customers who weren't able to get in had formed a line on the sidewalk outside."

    "Business was booming due to it being the Sunday before Valentine's Day, on top of the feature in the local magazine the shop had received."

    if persistent.dpatch:
        "As a stomping ground for the local girls' school students, the area around the station was a veritable battleground when it came to sales of sweets, but it looked like Le Chocolat Chocolat was by far the winner when it came to this year's Valentine's sales." id a09_cou1_06_67712464
    else:
        "As a stomping ground for the local girls' academy students, the area around the station was a veritable battleground when it came to sales of sweets, but it looked like Le Chocolat Chocolat was by far the winner when it came to this year's Valentine's sales."

    "Hina had also come to the bustling bakery first thing in the morning, full of energy and ready to work her shift."

    "Since she was a small girl, it seemed Fumi's mother intended to ask her to help Fumi with serving customers."

    "However, just after greeting the woman, Hina spotted a pile of cardboard boxes that would hinder traffic inside the store and immediately headed into the back of the shop with them, starting on the physical work necessary to open the store."

    "Impressing Fumi's parents with her surprising strength, Hina ended up continuing to help in the back right up until the shop opened."

    scene white with Dissolve(0.1875)
    pause 1.5625

    scene kimikara_09_c with Dissolve(0.5)
    pause 1.5

    voice "2FU_0774"
    fumi "\"Yes, this is the one that was featured in the article.\"" id a09_cou1_06_5b0203d0

    "With a smile, Fumi handed over a heart-shaped container full of cute chocolates."

    voice "2FU_0775"
    fumi "\"It contains an assortment of milk, sweet, and bitter chocolates.\"" id a09_cou1_06_4f86a813

    "This assortment was the season's best-selling product, featured in the magazine with a picture."

    "Since it was so popular, many people asked about it every day. Fumi smiled and introduced it like every time was her first."

    "She was the perfect face of the store, her customer service skills flawless. It almost seemed a waste to have her become a patissier and fall back to the kitchen."

    scene bg08aa with Dissolve(1.5)

    "Hina was similarly excelling in her work, going between the front and back of the store."

    "She brought ingredients into the kitchen at Fumi's father's request and restocked the shop at her mother's request. The way she weaved about inside the tight confines of the store with her small frame brought to mind a hamster."

    $ side_image = "hina 1 side casual b"

    voice "2HI_0932"
    hina "\"Four here, Mr. Asou! Huh? Two's fine? It's okay, I can hold four!\"" id a09_cou1_06_63b69697

    scene kimikara_09_c with Dissolve(1.5)

    "Even hours after the store opened, the rush of customers didn't cease, and the store and kitchen were still just as busy."

    "The fact that they were getting through the day with no unhappy customers was largely due to Hina and Fumi's hard work."

    play sound se_2s_k040

    $ side_image = "hina 1 side casual c"

    $ voice2("hina","2HI_0933N","fumi","2FU_0776")
    hina_fumi "\"Welcome!\""

    pause 0.5

    scene white with Dissolve(0.75)
    pause 1.5

    "At the same time, in the dorm..."

    window hide

    pause 0.5

    scene bg01ag with bg_effect_27
    pause 0.5

    $ side_image = "miyako 2 side pyjama c"

    window auto

    voice "2MI_0850"
    miyako "\"It's time for snacks, Rin~\"" id a09_cou1_06_49614c47

    "Miyako carried some coffee and sweets in from the kitchen on a tray."

    $ side_image = "rin 1 side pyjama glasses c"

    voice "2RI_0917"
    rin "\"Mm~ Thanks. What's for snacks?\"" id a09_cou1_06_df1f0c30

    show rin:
        "rin z4 1 lg pyjama glasses c flat"
        alpha 0.0 xcenter 726 ycenter 859
        easein 1.0 alpha 1.0 ycenter 759

    "Rin sat up."

    show rin z4 1 lg pyjama glasses c:
        alpha 1.0 xcenter 726 ycenter 759
    with None
    show miyako z4 1 lg pyjama_a b:
        xcenter 298
    with dict_dissolve_25

    voice "2MI_0851"
    miyako "\"Chocolate that Hina and Fumi made.\"" id a09_cou1_06_1f8741ea

    "Miyako sat down, placing the tray on the table."

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0918"
    rin "\"Blech, chocolate they made... I don't really like sweet stuff...\"" id a09_cou1_06_7d5026d1

    show miyako:
        "miyako z4 1 lg pyjama_a e" with Dissolve(0.25)
        3.5
        ShakeYes
        1.0
        "miyako z4 1 lg pyjama_a b" with Dissolve(0.25)

    voice "2MI_0852"
    miyako "\"They said not to worry about how it looks since it was just practice, but... mmm! It's good! And it's not too sweet, either.\"" id a09_cou1_06_8ad38df0

    show miyako z4 1 lg pyjama_a b:
        xoffset 0 yoffset 0
    with None

    "Miyako pushed the tray over to Rin, who took a chocolate just to be civil."

    show rin:
        "rin z4 1 lg pyjama glasses i" with Dissolve(0.25)
        4.0
        ShakeYes
        2.5
        "rin z4 1 lg pyjama glasses e" with Dissolve(0.25)

    voice "2RI_0919"
    rin "\"It's not the chocolate that's sweet, y'see... amh... ohh...\"" id a09_cou1_06_bcc9de22

    show rin z4 1 lg pyjama glasses e:
        xoffset 0 yoffset 0
    with None

    show miyako z4 1 lg pyjama_a h with dict_dissolve_25

    voice "2MI_0853"
    miyako "\"Right?\"" id a09_cou1_06_f72a1847

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0920"
    rin "\"Mmh...\"" id a09_cou1_06_84c0a213

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0854"
    miyako "\"They're probably pretty busy right now, huh?\"" id a09_cou1_06_47b92ce5

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0921"
    rin "\"Yeah, they're both busy bees. Especially Hina; I bet she's working really hard to get Asou's parents to like her.\"" id a09_cou1_06_b89d40e0

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0855"
    miyako "\"They already had their wedding and everything.\"" id a09_cou1_06_72665e31

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0922"
    rin "\"Yep, and I was the priest.\"" id a09_cou1_06_60cdac79

    "She raised one hand in what I'm guessing was a priestly gesture."

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0923"
    rin "\"Of course, I've got no authority or binding power, so it was just an imitation... playing make-believe, really.\"" id a09_cou1_06_3680aee5

    voice "2RI_0923a"
    rin "\"It's not just the wedding. Feels like everything those two do is playing make-believe. It's embarrassing just watching them, personally.\"" id a09_cou1_06_40dc8ece

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0856"
    miyako "\"So you say, but you always go along with them, don't you?\"" id a09_cou1_06_95117495

    "Miyako, of course, caught on to the softness in Rin's voice that didn't match her words."

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0924"
    rin "\"I guess. They're kind of my dream.\"" id a09_cou1_06_efdd488d

    show miyako z4 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0857"
    miyako "\"Your dream?\"" id a09_cou1_06_274d6399

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0925"
    rin "\"Yep. The pure dream of a twisted girl.\"" id a09_cou1_06_635bedfd

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0926"
    rin "\"My parents are never home, so I don't really have a lot of warm family memories.\"" id a09_cou1_06_3558684c

    voice "2RI_0926a"
    rin "\"Oh, just because I don't have any good ones doesn't mean I have bad ones, though. It's not like I hate my parents or anything.\"" id a09_cou1_06_8ec58512

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0858"
    miyako "\"Right.\"" id a09_cou1_06_bd4089ce

    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0927"
    rin "\"So those two are sort of like a fantasy for me. Though I know I shouldn't idealize them or anything.\"" id a09_cou1_06_92925aa9

    "Miyako shook her head."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0859"
    miyako "\"You're just watching over them. You're not forcing them to do anything.\"" id a09_cou1_06_afead501

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0928"
    rin "\"Thanks. Anyway, I just want them to have what they have forever. I want to believe that something can last forever.\"" id a09_cou1_06_27131f74

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0860"
    miyako "\"Yes... I'm sure they will.\"" id a09_cou1_06_7d687446

    pause 0.5

    stop music fadeout 1.0

    scene white with Dissolve(1.0)
    pause 2.0

    scene bg08ba with Dissolve(0.5)
    pause 0.5

    "The sign that had been standing outside was now folded up, and screens covered the windows."

    "It was earlier than their usual closing time, but they'd sold out of everything save Fumi's smile."

    "With the store closed, the two girls' shift ended as well."

    if persistent.dpatch:
        "They'd intended to help with the cleanup too, but they had school the next day, so Fumi's mother insisted they head home." id a09_cou1_06_b8ce735d
    else:
        "They'd intended to help with the cleanup too, but they had class the next day, so Fumi's mother insisted they head home."

    play music bgm02 fadein 1.0

    scene bg11ba
    show fumi 2 sm casual b at pos_ls
    with Dissolve(1.2)
    pause 0.5

    play sound se_2s_k040

    show hina:
        "hina 2 sm casual a flat"
        alpha 0.0 xcenter 832
        easein 0.75 alpha 1.0 xcenter 732
    pause 0.75

    show hina 2 sm casual a:
        alpha 1.0 xcenter 732
    with None
    show fumi 2 sm casual i with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_0777"
    fumi "\"Thank you for today, Hina.\"" id a09_cou1_06_15f93c3f

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi bowed to Hina as soon as they left the shop."

    show hina 2 sm casual b with dict_dissolve_25

    voice "2HI_0934"
    hina "\"Geez. How many times is that now?\"" id a09_cou1_06_228921b4

    "It was a lot. Fumi had been thanking her since morning."

    show hina 2 sm casual f with dict_dissolve_25

    voice "2HI_0935"
    hina "\"The pay is thanks enough. Actually, it seems high, if anything.\"" id a09_cou1_06_fdac8a18

    "The envelope of cash Hina had received was pretty full."

    show fumi:
        "fumi 2 sm casual c" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0778"
    fumi "\"No, you earned it! And my mother told me to make sure I thanked you! You really helped!\"" id a09_cou1_06_6be635e9

    show fumi 2 sm casual c:
        xoffset 0 yoffset 0
    with None

    "She bowed again."

    show hina:
        "hina 2 sm casual g" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0936"
    hina "\"You and your mom and dad worked really hard too. We all did good♪\"" id a09_cou1_06_04c5d881

    show hina 2 sm casual g:
        xoffset 0 yoffset 0
    with None

    "With a small smile, Hina bowed her head back."

    show fumi 1 sm casual h with dict_dissolve_25

    voice "2FU_0779"
    fumi "\"Rei should have been helping out too, really.\"" id a09_cou1_06_de0f3f63

    "Fumi looked apologetic at that. Rei was her younger brother who was in middle school."

    show hina:
        "hina 2 sm casual a" with Dissolve(0.25)
        6.5
        "hina 1 sm casual c" with Dissolve(0.25)
        ShakeJump2

    voice "2HI_0937"
    hina "\"It's alright; he did enough yesterday. I wouldn't have been able to reach all the stuff on the high shelves.\"" id a09_cou1_06_43d0f13d

    show hina 1 sm casual c:
        xoffset 0 yoffset 0
    with None

    "Hina jumped up."

    show fumi 1 sm casual k with dict_dissolve_25

    voice "2FU_0780"
    fumi "\"He had to be in a basketball game today. But you had to cancel your game... I'm sorry.\"" id a09_cou1_06_4586dcdd

    show hina 1 sm casual f with dict_dissolve_25

    voice "2HI_0938"
    hina "\"It's fine, really! Our situations are totally different!\"" id a09_cou1_06_cb526ad5

    show fumi 1 sm casual e with dict_dissolve_25

    "Hina's face was dead serious. Fumi was a little taken aback at her strong reaction."

    show hina 1 sm casual e with dict_dissolve_25

    voice "2HI_0939"
    hina "\"I'm only a part-time team member, but Rei has practiced really hard to earn a spot on the team as a regular! Of course he wants to play in games!\"" id a09_cou1_06_00942737

    show fumi 2 sm casual h with dict_dissolve_25

    voice "2FU_0781"
    fumi "\"True, he always goes to morning practice and practices late into the night, too.\"" id a09_cou1_06_f60cf795

    show hina 2 sm casual c with dict_dissolve_25

    voice "2HI_0940"
    hina "\"Right? If he really wanted to be in it, I'm sure it was an important game. I hope he really made a difference today♪\"" id a09_cou1_06_40c29fa2

    show fumi 2 sm casual b with dict_dissolve_25

    voice "2FU_0782"
    fumi "\"...Let me thank you on his behalf, then.\"" id a09_cou1_06_150512a5

    hide fumi
    hide hina
    with dict_dissolve_50

    "They both smiled and walked off."

    show fumi 2 lg casual b at pos_l
    show hina 2 lg casual a at pos_r
    with dict_dissolve_25

    voice "2HI_0941"
    hina "\"Anyway, I had fun working with you today. That's enough for me♪\"" id a09_cou1_06_731a8566

    show fumi 2 lg casual i with dict_dissolve_25

    voice "2FU_0783"
    fumi "\"Eheh, me too♪\"" id a09_cou1_06_8b8671b1

    show hina 2 lg casual f with dict_dissolve_25

    voice "2HI_0942"
    hina "\"You want to become a pastry chef like your dad, right, Fumi?\"" id a09_cou1_06_1fe62f03

    show fumi:
        "fumi 2 lg casual b" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0784"
    fumi "\"Yes, I do.\"" id a09_cou1_06_40afb627

    show fumi 2 lg casual b:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg casual c with dict_dissolve_25

    voice "2HI_0943"
    hina "\"I thought it'd be really nice if we could have a shop together someday. We could always be together then, too.\"" id a09_cou1_06_8e27c8cf

    show hina 2 lg casual g with dict_dissolve_25

    voice "2HI_0944"
    hina "\"You'd bake, and I'd help out. Oh, I know. I'd take pictures of your sweets and advertise with them♪\"" id a09_cou1_06_f40b083f

    show fumi 1 lg casual c with dict_dissolve_25

    voice "2FU_0785"
    fumi "\"Hina! That's a great idea!\"" id a09_cou1_06_c56c8e47

    show fumi:
        "fumi 1 lg casual f" with Dissolve(0.25)
        ShakeTameiki

    "Fumi spread her arms wide like she was going to embrace her, but since they were out on the street, she left it at that."

    show fumi 1 lg casual f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg casual a
    show hina 1 lg casual b
    with dict_dissolve_25

    voice "2HI_0945"
    hina "\"Maybe I'll keep this pay and set it aside for that future, then.\"" id a09_cou1_06_6ab8ccb4

    "Hina patted her bag where the envelope of money was."

    play sound se_lime
    "Fumi's phone chirped."

    show fumi 2 lg casual g with dict_dissolve_25

    voice "2FU_0786"
    fumi "\"Hm? It's my dad.\"" id a09_cou1_06_d243ce55

    "She stopped and opened the message."

    show hina 1 lg casual k with dict_dissolve_25

    voice "2HI_0946"
    hina "\"What? Did we forget something?\"" id a09_cou1_06_04275da2

    show fumi 2 lg casual b with dict_dissolve_25

    voice "2FU_0787"
    fumi "\"No, he wanted to apologize for being so busy that he didn't have time to properly thank you.\"" id a09_cou1_06_fcdc927e

    "She showed Hina her phone screen."

    show hina 1 lg casual a with dict_dissolve_25

    voice "2HI_0947"
    hina "\"Wow, you're right. Tell him not to worry about it.\"" id a09_cou1_06_fe63498d

    show fumi 2 lg casual i with dict_dissolve_25

    voice "2FU_0788"
    fumi "\"Okay.\"" id a09_cou1_06_1e077318

    play sound se_vibes
    pause 1.0
    stop sound

    "A reply came right away from her dad. The two of them looked at the screen together."

    show hina 1 lg casual c with dict_dissolve_25

    voice "2HI_0948"
    hina "\"Eheh. 'We'll have to expand the store if this keeps up.'\"" id a09_cou1_06_bb7dce14

    show fumi 2 lg casual i with dict_dissolve_25

    voice "2FU_0789"
    fumi "\"It might just be because of Valentine's Day. Geez, he's always so optimistic.\"" id a09_cou1_06_6ece052f

    "Fumi sent a reply accompanied by a bear stamp with a troubled expression."

    show hina 1 lg casual b with dict_dissolve_25

    voice "2HI_0949"
    hina "\"Maybe the people who bought chocolate today will like it so much they become regulars.\"" id a09_cou1_06_1f5e327a

    show fumi 1 lg casual b with dict_dissolve_25

    voice "2FU_0790"
    fumi "\"Well, I'd be happy about that~\"" id a09_cou1_06_a7843a5b

    show hina 2 lg casual a with dict_dissolve_25

    voice "2HI_0950"
    hina "\"If that happens, I could work more regularly.\"" id a09_cou1_06_3cd1a7c5

    show fumi 1 lg casual c with dict_dissolve_25

    voice "2FU_0791"
    fumi "\"Eheh. I'd like that, too.\"" id a09_cou1_06_4e931148

    play sound se_vibes
    pause 1.0
    stop sound

    show fumi 1 lg casual a with dict_dissolve_25

    voice "2FU_0792"
    fumi "\"He says you work so hard, he'd like you to be one of his kids. He just says whatever he wants.\"" id a09_cou1_06_070ea6ac

    show hina 2 lg casual g with dict_dissolve_25

    voice "2HI_0951"
    hina "\"Eheheh. Even if he hadn't asked, I do plan on becoming part of the family one day♪\"" id a09_cou1_06_d2801560

    show fumi 1 lg casual c with dict_dissolve_25

    voice "2FU_0793"
    fumi "\"Heh, I'll have to go meet your parents, too.\"" id a09_cou1_06_361332c0

    show hina 2 lg casual f with dict_dissolve_25

    voice "2HI_0952"
    hina "\"Hmm, is Rei interested in baking?\"" id a09_cou1_06_da16656f

    show fumi 1 lg casual i with dict_dissolve_25

    voice "2FU_0794"
    fumi "\"Not really, no~\"" id a09_cou1_06_54269747

    show hina 1 lg casual k with dict_dissolve_25

    voice "2HI_0953"
    hina "\"Does he want to be a basketball player?\"" id a09_cou1_06_8d18aec8

    show fumi 1 lg casual a with dict_dissolve_25

    voice "2FU_0795"
    fumi "\"No, that's just a hobby. He says he wants to be a vet when he grows up. We have an uncle who teaches vet students in Hokkaido, so that's probably why.\"" id a09_cou1_06_db44b745

    show hina 1 lg casual a with dict_dissolve_25

    voice "2HI_0954"
    hina "\"Wow, a vet? I guess you'll have to take over the store, then.\"" id a09_cou1_06_4b519309

    show fumi 1 lg casual d with dict_dissolve_25

    voice "2FU_0796"
    fumi "\"I wonder what my parents are thinking about that.\"" id a09_cou1_06_2944301c

    play sound se_vibes

    "She got another message."

    stop sound

    show hina 2 lg casual c with dict_dissolve_25

    voice "2HI_0955"
    hina "\"Wow, 'you're our only hope for the future of the shop'? Eheheh, it's like he can hear our conversation.\"" id a09_cou1_06_44bd30ab

    show fumi 2 lg casual b with dict_dissolve_25

    voice "2FU_0797"
    fumi "\"I don't think it's recording...\"" id a09_cou1_06_1d0d9f2d

    "They looked at each other and laughed."

    show fumi 1 lg casual d with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "2FU_0798"
    fumi "\"He's so hasty. 'You shouldn't be retiring for a long'... oh?\"" id a09_cou1_06_352dbfab

    show fumi 1 lg casual a:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    play sound se_vibes

    "While she was typing a reply, another message came."

    stop sound

    show hina 2 lg casual f with dict_dissolve_25

    voice "2HI_0956"
    hina "\"What's it say...?\"" id a09_cou1_06_d31592e4

    stop music fadeout 1.0

    show fumi 1 lg casual k with dict_dissolve_25

    voice "2FU_0799"
    fumi "\"Ah......\"" id a09_cou1_06_872ab1b8

    fumi_father "{i}I hope you'll find a good husband and take over the shop with him.{/i}"

    scene black with Dissolve(2.0)
    pause 0.5

    scene continue with Dissolve(2.0)
    pause 2.0

    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou1_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
