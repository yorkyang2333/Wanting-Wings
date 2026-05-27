label a09_comn_09:

    if route2 == 1:
        scene bg01cg with Dissolve(0.5)
    else:
        scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "After the bean-scattering..."

    show sachiko 1 lg outfit j with dict_dissolve_25

    voice "2SA_0599"
    sachiko "\"I object! Why did all the fire have to be focused on me?!\"" id a09_comn_09_e8484c20

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_0782"
    hina "\"Well, you're the namahage.\"" id a09_comn_09_83cbe2ed

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0790"
    rin "\"Yeah, that.\"" id a09_comn_09_a9d5e1c4

    show sachiko 1 lg outfit h with dict_dissolve_25

    voice "2SA_0600"
    sachiko "\"And why was it all 'demons out' and no 'luck in'? Why the super offense-focused bean-scattering?\"" id a09_comn_09_e26cb56a

    $ side_image = "hina 2 side pyjama_pjm b"

    voice "2HI_0783"
    hina "\"Ah~ Well, that I'll apologize for. I got pretty into chucking them at you.\"" id a09_comn_09_6d178d51

    "Hina and Rin had practically become berserkers as they'd chased the \"demon\" Sachiko."

    show sachiko:
        "sachiko 1 lg outfit j" with Dissolve(0.25)
        ShakeJump

    voice "2SA_0601"
    sachiko "\"Somebody else is gonna be the demon next year, okay?!\"" id a09_comn_09_09d9beee

    show sachiko 1 lg outfit j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama k"

    voice "2RI_0791"
    rin "\"Yeah, yeah. We'll see about that. Now, let's eat some of these beans.\"" id a09_comn_09_2bd6a23d

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_0784"
    hina "\"I'm glad we have enough left over to eat. We really threw a lot of them.\"" id a09_comn_09_e6f18890

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0639"
    fumi "\"It's good we bought some, too.\"" id a09_comn_09_d814125a

    hide sachiko with dict_dissolve_50

    "The beans they'd thrown had been prepared by Sachiko, while the beans the four girls had bought were untouched."

    show hina z4 1 lg pyjama_pjm a
    show fumi z4 2 lg pyjama b:
        xcenter 172
    show rin z4 1 lg pyjama b:
        xcenter 852
    with dict_dissolve_25

    voice "2RI_0792"
    rin "\"Really you're supposed to pick up and eat the ones you threw, but I don't really want to eat them when they've been on the floor.\"" id a09_comn_09_5a3e6b8c

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0602"
    sachiko "\"You guys were so gung-ho with your bean attacks, the dorm's covered with them now. I'm the one who has to clean it all up, you know.\"" id a09_comn_09_32180fd3

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0785"
    hina "\"You were the one who said you wanted to celebrate.\"" id a09_comn_09_99a1ecb7

    $ side_image = "sachiko 1 side outfit j"

    voice "2SA_0603"
    sachiko "\"I didn't say I wanted to be hunted!\"" id a09_comn_09_282ce990

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0640"
    fumi "\"Ahaha, I'll help you clean up later.\"" id a09_comn_09_11a9453c

    show rin:
        "rin z4 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "2RI_0793"
    rin "\"Here y'go. I counted out your age for you. Seven for Hina.\"" id a09_comn_09_280e10b1

    show rin z4 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None

    "Rin held out the beans to Hina."

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0786"
    hina "\"I'm eating more than that! I'm not—\"" id a09_comn_09_764c0db0

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0604"
    sachiko "\"I'll just have seventeen, then♪\"" id a09_comn_09_d624baf6

    show rin z4 1 lg pyjama h with dict_dissolve_25

    voice "2RI_0794"
    rin "\"Don't lie. Open your mouth, I'll pour 'em in, straight from the bag.\"" id a09_comn_09_c43479a0

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0605"
    sachiko "\"Stop iiit!\"" id a09_comn_09_059c7a7b

    show fumi z4 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0641"
    fumi "\"Miyako, you—\"" id a09_comn_09_94e58398

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.5)
    pause 0.5

    show miyako 1 lg pyjama_b a with Dissolve(0.5)
    show miyako:
        ShakeYes
        ShakeYes
        ShakeYes

    "Munch, munch, munch, munch..."

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Miyako silently, endlessly brought beans to her mouth."

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0642"
    fumi "\"U-Umm... Miyako? You're only supposed to eat one per year you've been alive.\"" id a09_comn_09_4775a0f6

    show miyako 1 lg pyjama_b g with Dissolve(0.5)
    show miyako:
        ShakeYes
        ShakeYes

    voice "2MI_0708"
    miyako "\"Om nom nom.\"" id a09_comn_09_1e482e7b

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Her cheeks are so full of beans I have no idea what she's saying."

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0606"
    sachiko "\"Hey, follow the script here.\"" id a09_comn_09_65f77bcc

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    if route2 == 1:
        scene bg01cg with bg_effect_05
    else:
        scene bg01ch with bg_effect_05
    pause 0.5

    show fumi 2 lg pyjama d at pos_l with dict_dissolve_25

    voice "2FU_0643"
    fumi "\"Huh? I don't need to cut the sushi?\"" id a09_comn_09_f0d78556

    "Sachiko stopped Fumi from bringing the sushi into the kitchen."

    show sachiko 1 lg outfit g at pos_r with dict_dissolve_25

    voice "2SA_0607"
    sachiko "\"Yeah, it's called ehoumaki. You just eat it like that.\"" id a09_comn_09_2c40af57

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0644"
    fumi "\"Ehoumaki?\"" id a09_comn_09_af225f5b

    $ side_image = "rin 1 side pyjama k"

    voice "2RI_0795"
    rin "\"The superstition is, on the night of setsubun, you eat the whole thing in one go while facing the lucky direction and thinking of a wish, and if you eat it all without talking, your wish will come true.\"" id a09_comn_09_acb9c907

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0787"
    hina "\"Lucky direction? What's that?\"" id a09_comn_09_f4783457

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0608"
    sachiko "\"There's a different direction that's supposed to be lucky every year. This year it's east-northeast.\"" id a09_comn_09_369b3c03

    $ side_image = "miyako 1 side pyjama_a d"

    voice "2MI_0709"
    miyako "\"That sounds fun. Let's do it, let's do it.\"" id a09_comn_09_c9ff17d7

    $ side_image = "hina 1 side pyjama_pjm p"

    voice "2HI_0788"
    hina "\"What should I wish for~?\"" id a09_comn_09_139925d9

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0796"
    rin "\"You know ehoumaki's just another marketing thing pushed by corporations like Valentine's chocolate, right?\"" id a09_comn_09_2d58081f

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "2SA_0609"
    sachiko "\"C'mon, stop being a Debbie Downer and join in, Rin.\"" id a09_comn_09_601dbe4e

    $ side_image = "rin 1 side pyjama b"

    voice "2RI_0797"
    rin "\"No way. It's just hard to eat it like that.\"" id a09_comn_09_48eb66d2

    show fumi 2 lg pyjama b with dict_dissolve_25

    if route2 == 3:
        voice "2FU_0645"
        fumi "\"Do you want me to cut yours, Rin?\"" id a09_comn_09_19c97a58
    else:
        voice "2FU_0646"
        fumi "\"Do you want me to cut yours, Ogata?\"" id a09_comn_09_4b8dd3d5

    "There she goes, spoiling her again."

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0610"
    sachiko "\"Alright, Rin, let's have a match to see who can finish theirs without talking. The winner doesn't have to be the demon for setsubun next year.\"" id a09_comn_09_68c4b0e6

    $ side_image = "rin 1 side pyjama f"

    voice "2RI_0798"
    rin "\"Heh, I was wondering what you'd say. Sounds stupid... Let's do it!\"" id a09_comn_09_7c09c3b3

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0647"
    fumi "\"...Haah. Well, I'll make some tea, then.\"" id a09_comn_09_635b793e

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    if route2 == 1:
        scene bg01cg with bg_effect_05
    else:
        scene bg01ch with bg_effect_05
    pause 0.5

    show sachiko z4 1 lg outfit g:
        xcenter 100
    show miyako z4 1 lg pyjama_a d:
        xcenter 288
    show fumi z4 1 lg pyjama c behind miyako, hina
    show hina z4 1 lg pyjama_pjm c:
        xcenter 736
    show rin z4 1 lg pyjama a behind hina:
        xcenter 930
    with dict_dissolve_25

    $ voice5("hina","2HI_0789N","rin","2RI_0799","fumi","2FU_0648","miyako","2MI_0710","sachiko","2SA_0611")
    hina_rin_fumi_miyako_sachiko "\"Let's eat.\""

    "The five of them faced the lucky direction and all put the sushi in their mouths at the same time."

    hide hina
    hide rin
    hide fumi
    hide miyako
    hide sachiko
    with Dissolve(0.25)

    if routes_cleared < 2:
        jump a09_comn_09_a
    else:
        jump a09_comn_09_b

label a09_comn_09_a:

    show miyako 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0711"
    miyako "\"It's good!\"" id a09_comn_09_a_f27954df

    "One bite in. This one seems to have absorbed exactly zero of the rules of the activity."

    "Likely completely unaware that she'd fallen out of the race, she continued munching on the sushi, an innocent smile on her face."

    show miyako:
        ShakeYes

    voice "2MI_0712"
    miyako "\"There's all sorts of different textures inside the ring of rice, so it's delicious for your teeth too, not just your tongue!\"" id a09_comn_09_a_ccf99851

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Great commentary, too."

    hide miyako with dict_dissolve_25

    jump a09_comn_09_b

label a09_comn_09_b:

    "........."

    show hina 1 lg pyjama_pjm g at pos_r
    with Dissolve(0.25)

    show hina:
        ShakeYes2

    voice "2HI_0790"
    hina "\"Koff, koff!\"" id a09_comn_09_b_047d237c

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina choked. She must have put too much in her mouth at once."

    show fumi 2 lg pyjama d at pos_l with dict_dissolve_25

    voice "2FU_0649"
    fumi "\"Here, tea—\"" id a09_comn_09_b_153a09dd

    show hina 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0791"
    hina "\"Thanks—\"" id a09_comn_09_b_1f9c6c82

    show fumi 1 lg pyjama e
    show hina 1 lg pyjama_pjm l
    with dict_dissolve_25

    "By the time they realized it, it was too late. Fumi handed over the teacup and Hina accepted it, talking to one another."

    show fumi:
        "fumi 1 lg pyjama k" with Dissolve(0.25)
        ease 0.4 yoffset 10
        ease 0.4 yoffset 0

    show hina:
        "hina 1 lg pyjama_pjm h" with Dissolve(0.25)
        ease 0.4 yoffset 8
        ease 0.4 yoffset 0

    $ voice2("hina","2HI_0792","fumi","2FU_0650")
    hina_fumi "\"...Haahh.\""

    show fumi 1 lg pyjama k with None
    show hina 1 lg pyjama_pjm h with None

    "They both sighed, shoulders drooping."

    show hina 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_0793"
    hina "\"Sorry I brought you down with me.\"" id a09_comn_09_b_2fbdb855

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0651"
    fumi "\"No, I spoke first. Let's just take our time now. Here, your tea.\"" id a09_comn_09_b_5859f5ab

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0794"
    hina "\"Yeah, thanks.\"" id a09_comn_09_b_3d42b670

    hide fumi
    hide hina
    with dict_dissolve_50

    "Probably a predictable outcome, considering their gentle personalities."

    show sachiko 1 lg outfit a at pos_l
    show rin 1 lg pyjama f at pos_r
    with dict_dissolve_25

    voice "2RI_0800"
    rin "\".........\"" id a09_comn_09_b_abc6bbcb

    voice "2SA_0612"
    sachiko "\"......\"" id a09_comn_09_b_514b06a2

    "Meanwhile, the two who were more cunning smirked at each other."

    "And they bit into their sushi dynamically, as if showing the action to one another."

    "Who would win their cutthroat competition—"

    show rin:
        "rin 1 lg pyjama i" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0801"
    rin "\"...Augh.\"" id a09_comn_09_b_9318777f

    show rin 1 lg pyjama i:
        xoffset 0 yoffset 0
    with None
    $ side_image = "side/hina_fumi_pyjama[hina_choker]_sozai01.webp"

    $ voice2("hina","2HI_0795","fumi","2FU_0652")
    hina_fumi "\"Huh?!\""

    "Rin suddenly let out a pathetic whine and their match was brought to a rather quick conclusion."

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0653"
    fumi "\"Umm, what is it?\"" id a09_comn_09_b_1f068b4e

    show rin:
        "rin 1 lg pyjama g" with Dissolve(0.25)
        ShakeNo_4_500

    voice "2RI_0802"
    rin "\"There's mushrooms in this~\"" id a09_comn_09_b_c2121e58

    show rin 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0796"
    hina "\"Oh, you didn't like those, right?\"" id a09_comn_09_b_89aff205

    show rin 1 lg pyjama j with Dissolve(0.25)
    show rin:
        ShakeNo_4_500

    voice "2RI_0803"
    rin "\"I~ hate~ them~\"" id a09_comn_09_b_4445ad42

    show rin:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 1 side pyjama a"

    voice "2FU_0654"
    fumi "\"Want to eat the rest without the mushrooms?\"" id a09_comn_09_b_c615c1d2

    show rin 2 lg pyjama d with dict_dissolve_25

    voice "2RI_0804"
    rin "\"Yeah... I'll do that.\"" id a09_comn_09_b_3832316b

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "2SA_0613"
    sachiko "\"Woohoo! I won~!\"" id a09_comn_09_b_78f190ab

    "Uhh."

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0797"
    hina "\"But you just talked before finishing.\"" id a09_comn_09_b_2a9ddbc3

    show sachiko:
        "sachiko 1 lg outfit h" with Dissolve(0.25)
        ShakeSide

    voice "2SA_0614"
    sachiko "\"Ah...\"" id a09_comn_09_b_afea41b3

    show sachiko 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    if routes_cleared >= 2:
        jump a09_comn_09_c
    else:
        jump a09_comn_09_end

label a09_comn_09_c:

    hide rin
    hide sachiko
    with Dissolve(0.5)

    show miyako 1 lg pyjama_a d with Dissolve(0.5)

    voice "2MI_0713"
    miyako "\"Delicious.\"" id a09_comn_09_c_af6571b6

    $ side_image = "side/hina[hina_choker]_fumi_rin_[rin_pyjama]_sachiko_sozai01.webp"

    $ voice4("hina","2HI_0798","rin","2RI_0805","fumi","2FU_0655","sachiko","2SA_0615")
    hina_rin_fumi_sachiko "\"Oh.\""

    "Miyako finished eating before everyone else."

    show miyako:
        "miyako 1 lg pyjama_a c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0714"
    miyako "\"That was really good♪\"" id a09_comn_09_c_5acbd43b

    show miyako 1 lg pyjama_a c:
        xoffset 0 yoffset 0
    with None
    scene black with Dissolve(1.5)
    pause 0.5

    "...Well, I hope her wish comes true."

label a09_comn_09_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a09_cou1_05
    elif routes_cleared < 2:
        jump a09_comn_10
    else:
        jump a09_comn_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
