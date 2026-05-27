label a07_comn_05:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    $ side_image = "hina 1 side school_scarf o"

    voice "2HI_0089"
    hina "\"It's cold~\"" id a07_comn_05_37a3f875

    $ side_image = "fumi 1 side school_scarf b"

    voice "2FU_0061"
    fumi "\"We're home.\"" id a07_comn_05_7cee17df

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0062"
    sachiko "\"Welcome back! It's a cold one today~\"" id a07_comn_05_b4247473

    $ side_image = "rin 2 side school_scarf a"

    voice "2RI_0083"
    rin "\"Here.\"" id a07_comn_05_7e8dd69b

    show sachiko:
        "sachiko 1 lg outfit g" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0063"
    sachiko "\"Danke♪\"" id a07_comn_05_33fb6b9d

    show sachiko 1 lg outfit g:
        xoffset 0 yoffset 0
    with None
    hide sachiko with dict_dissolve_50

    "Rin tossed a pack of cigarettes to Sachiko, who caught them. A familiar sight."

    if persistent.dpatch:
        "It'd probably be a problem if the school or her parents found out, but the dorm manager was not the least bit concerned about that." id a07_comn_05_e473ef88
    else:
        "It'd probably be a problem if the academy or her parents found out, but the dorm manager was not the least bit concerned about that."

    show sachiko 1 sm outfit a:
        xcenter 184
    show hina 1 sm school_scarf k:
        xcenter 632
    show rin 1 sm school_scarf a behind hina, fumi:
        xcenter 776
    show fumi 1 sm school_scarf a:
        xcenter 940
    with Dissolve(0.25)

    voice "2SA_0064"
    sachiko "\"I'll treat you each to one drink from the vending machine as payment.\"" id a07_comn_05_eed18a85

    "The vending machine was Sachiko's property, and she used its proceeds to pay for her cigarettes. Well, at least everything in it is only 100 yen..."

    show rin 1 sm school_scarf k with dict_dissolve_25

    voice "2RI_0084"
    rin "\"Wow. Yay.\"" id a07_comn_05_22446761

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0065"
    sachiko "\"Oh, I only got cold ones, though.\"" id a07_comn_05_3d221fb2

    show hina:
        "hina 1 sm school_scarf g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0090"
    hina "\"What time of year do you think it is?!\"" id a07_comn_05_fcd97619

    show hina 1 sm school_scarf g with None
    show hina:
        ShakeJump

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0066"
    sachiko "\"But you got pissed at me when I put beer in it in the summer!\"" id a07_comn_05_c06ac880

    show hina:
        xoffset 0 yoffset 0
        ShakeJump

    voice "2HI_0091"
    hina "\"Put that in the fridge in your room!\"" id a07_comn_05_8af3f2d2

    show hina:
        xoffset 0 yoffset 0
    with None

    "What's that have to do with the time of year?"

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0085"
    rin "\"Talk about not catering to your customer's needs.\"" id a07_comn_05_d44d1d87

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0067"
    sachiko "\"If we're talking needs, I could get a cigarette vending—\"" id a07_comn_05_02114cf7

    show hina:
        ShakeJump
        ShakeJump

    voice "2HI_0092"
    hina "\"NO!!\"" id a07_comn_05_89ee55a5

    show hina:
        xoffset 0 yoffset 0
    with None

    play sound se521
    pause 0.5

    "Miyako walked in just then, after knocking the dirt from her shoes at the entrance."

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.5)

    show miyako 2 sm school a:
        xcenter 840
    with dict_dissolve_25

    voice "2MI_0038"
    miyako "\"I'm... home.\"" id a07_comn_05_7c14448a

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0068"
    sachiko "\"Welcome home, Mikoyan.\"" id a07_comn_05_7798130d

    show miyako 2 sm school c with dict_dissolve_25

    voice "2MI_0039"
    miyako "\"......\"" id a07_comn_05_69d4f8de

    voice "2SA_0069"
    sachiko "\"What is it?\"" id a07_comn_05_0a9713e5

    show miyako 1 sm school_a c with dict_dissolve_25

    voice "2MI_0040"
    miyako "\"'I'm home,' 'Welcome home'... They're very nice phrases.\"" id a07_comn_05_183ba621

    "It was Miyako's first time exchanging such pleasantries."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0070"
    sachiko "\"They are, aren't they?\"" id a07_comn_05_12ff1b55

    "Just saying \"I'm home\" and receiving a reply was a new experience for Miyako."

    show hina behind miyako:
        "hina 1 sm school_scarf k flat"
        alpha 0.0 xcenter 622
        linear 0.25 alpha 1.0
    show rin behind hina, miyako:
        "rin 1 sm school_scarf a flat"
        alpha 0.0 xcenter 776
        linear 0.25 alpha 1.0

    show miyako:
        xcenter 840
        easein 0.5 xcenter 930

    voice "2RI_0086"
    rin "\"You've been calling her that for a while now... Is it a new nickname?\"" id a07_comn_05_d8740dee

    show miyako:
        xcenter 930
    show hina 1 sm school_scarf k:
        alpha 1.0 xcenter 622
    show rin 1 sm school_scarf a:
        alpha 1.0 xcenter 776
    with None

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0071"
    sachiko "\"Mikoyan! It's cute, isn't it?\"" id a07_comn_05_0eb3f81d

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0087"
    rin "\"Well, I guess so. Do you like it, Takaoka?\"" id a07_comn_05_6f07402d

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0041"
    miyako "\"I don't mind. I can tell it's referring to me.\"" id a07_comn_05_10a25c51

    show miyako 1 sm school_a c with dict_dissolve_25

    voice "2MI_0042"
    miyako "\"And Sachiko gave me the name Miyako, too.\"" id a07_comn_05_b62d2e6b

    $ side_image = "fumi 1 side school_scarf e"

    voice "2FU_0062"
    fumi "\"Huh? Sachiko named you, Miyako?\"" id a07_comn_05_8b9fa8d3

    show miyako:
        ShakeYes

    "Miyako nodded."

    show miyako:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 sm school_scarf j" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2HI_0093"
    hina "\"There must be a pretty big age difference, then.\"" id a07_comn_05_f2e9c2d8

    show hina 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 sm school_scarf g" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2RI_0088"
    rin "\"Are you sure you're not her niece?\"" id a07_comn_05_36cbdfcd

    show rin 1 sm school_scarf g:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko 1 sm outfit j" with Dissolve(0.25)
        ShakeJump

    voice "2SA_0072"
    sachiko "\"Hey! What are you whispering about over there?!\"" id a07_comn_05_4220fe43

    show sachiko 1 sm outfit c:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2SA_0073"
    sachiko "\"I just picked from a list her parents had. {i}When I was little{/i}. Right, Mikoyan?\"" id a07_comn_05_7ff10e3d

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0043"
    miyako "\"Oh, yes. You're right.\"" id a07_comn_05_3ae1d04f

    "Nice save."

    show rin 2 sm school_scarf a with dict_dissolve_25

    voice "2RI_0089"
    rin "\"You always come up with the weirdest crap.\"" id a07_comn_05_03b81eca

    "Like Hinacchi and Foomin."

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0074"
    sachiko "\"What's weird about them, Rinrin?\"" id a07_comn_05_af517328

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0090"
    rin "\"I'm not answering to that!\"" id a07_comn_05_e98555c4

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_0044"
    miyako "\"Rinrin? Rin has a nickname, too?\"" id a07_comn_05_2ae41edb

    show hina 1 sm school_scarf m with dict_dissolve_25

    voice "2HI_0094"
    hina "\"It didn't stick.\"" id a07_comn_05_719fba7d

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0063"
    fumi "\"She never replied to it no matter how much Sachiko used it. They were both pretty stubborn, but—\"" id a07_comn_05_4520dfbb

    show hina 1 sm school_scarf a with dict_dissolve_25

    voice "2HI_0095"
    hina "\"In the end, Sachiko gave up.\"" id a07_comn_05_9353cd05

    show miyako 1 sm school_a a with dict_dissolve_25

    voice "2MI_0045"
    miyako "\"I see.\"" id a07_comn_05_f3ebe27d

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0075"
    sachiko "\"Oh, right. The maintenance on the bath is done today! They've still gotta hook the gas up though, so it'll be a little longer 'til you can use it.\"" id a07_comn_05_f869efc0

    show rin 2 sm school_scarf e with dict_dissolve_25

    voice "2RI_0091B"
    rin "\"Finally~ Now we don't have to freeze our butts off going to the other dorm.\"" id a07_comn_05_f73f7cd0

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0076"
    sachiko "\"Good for you, Rinrin!\"" id a07_comn_05_2df19a45

    show rin 1 sm school_scarf j with Dissolve(0.1)
    show rin:
        ShakeJump

    voice "2RI_0092"
    rin "\"Drop it!\"" id a07_comn_05_b4cea685

    show rin:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0077"
    sachiko "\"It should've been done over winter break, but they kept finding other stuff to fix, so it kinda became a big project.\"" id a07_comn_05_d1dd2296

    hide miyako
    with Dissolve(0.5)

    show rin 1 sm school_scarf b behind fumi
    show fumi 1 sm school_scarf a:
        xcenter 940
    with dict_dissolve_25

    voice "2FU_0064"
    fumi "\"There was some damage in places.\"" id a07_comn_05_11b3ef58

    show hina 1 sm school_scarf h with dict_dissolve_25

    voice "2HI_0096"
    hina "\"That's putting it lightly. It was falling apart.\"" id a07_comn_05_d15b8fb0

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0078"
    sachiko "\"So I'll let you girls have the first bath, special!\"" id a07_comn_05_9ce343b4

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "2FU_0065"
    fumi "\"Yay~\"" id a07_comn_05_8d0acf0a

    show sachiko 1 sm outfit e with dict_dissolve_25

    voice "2SA_0079"
    sachiko "\"It's bigger now, so let's all go in together♪\"" id a07_comn_05_4c35048b

    show hina:
        "hina 1 sm school_scarf f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0097"
    hina "\"Go in by yourself!\"" id a07_comn_05_d2d35912

    show hina 1 sm school_scarf f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0093B"
    rin "\"Can we go see it?\"" id a07_comn_05_54a84715

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0080"
    sachiko "\"Long as you don't run the water.\"" id a07_comn_05_298ad750

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "2RI_0094"
    rin "\"Gotcha. Let's go check it out, Hina.\"" id a07_comn_05_41e2f258

    show hina 1 sm school_scarf e with dict_dissolve_25

    voice "2HI_0098"
    hina "\"Sure.\"" id a07_comn_05_a1f27142

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.5)

    show fumi 1 sm school_scarf a:
        xcenter 672
    show miyako 1 sm school_a a:
        xcenter 872
    with dict_dissolve_25

    "The two of them headed for the bath, leaving the other three behind in the lobby."

    voice "2SA_0081"
    sachiko "\"Anywhere other than the bath you want fixed up?\"" id a07_comn_05_9ed9ebbd

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_0066"
    fumi "\"Hmm~ You fixed our water in the fall. I think everything else is fine.\"" id a07_comn_05_27453148

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0082"
    sachiko "\"Good. Actually, speaking of water, I think the roof might be leaking.\"" id a07_comn_05_7da204e5

    show fumi 2 sm school_scarf d with dict_dissolve_25

    voice "2FU_0067"
    fumi "\"Uh oh, you'll need to get that fixed before the rainy season, then.\"" id a07_comn_05_485ca688

    show sachiko 2 sm outfit a with dict_dissolve_25

    voice "2SA_0083"
    sachiko "\"Yeah... It's an old building, so it's starting to fall apart in places.\"" id a07_comn_05_e406c1b4

    show miyako 1 sm school_a e with dict_dissolve_25

    voice "2MI_0046"
    miyako "\"How long have you been watching over it?\"" id a07_comn_05_d758f02c

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0084"
    sachiko "\"Mm? Five years, I guess.\"" id a07_comn_05_420575e2

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0068"
    fumi "\"Huh, really?\"" id a07_comn_05_1528e184

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0047"
    miyako "\"......\"" id a07_comn_05_ca27023f

    play sound se_moooto
    pause 1.5

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "2SA_0085"
    sachiko "\"What was that?\"" id a07_comn_05_0283da4c

    "There was quite a bit of noise coming from the bath."

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "2SA_0086"
    sachiko "\"Hey! What the heck are you two doing in there?\"" id a07_comn_05_f19ebb1f

    $ side_image = "side/hina_rin_school_scarf_sozai01.webp"

    $ voice2("hina","2HI_0099","rin","2RI_0095")
    hina_rin "\"Checking for cameras!\""

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0087"
    sachiko "\"They have no faith in me.\"" id a07_comn_05_02c170ee

    show sachiko 1 sm outfit d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "2FU_0069"
    fumi "\"Ahaha...\"" id a07_comn_05_3b59bfc1

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0088"
    sachiko "\"They really think I'd hide 'em somewhere they'd find right away?\"" id a07_comn_05_acae532b

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "2FU_0070"
    fumi "\"...Haha.\"" id a07_comn_05_835a91be

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0089"
    sachiko "\"I'm joking. There aren't any cameras.\"" id a07_comn_05_c6c4a5ae

    show miyako 1 sm school_a e with dict_dissolve_25

    voice "2MI_0048"
    miyako "\"Oh, that's right.\"" id a07_comn_05_f9530ceb

    show miyako:
        ShakeYes2_5_500

    "Miyako had been watching their interactions with a smile, but she suddenly remembered something and dug through her bag."

    show miyako 1 sm school_a a:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2MI_0049"
    miyako "\"Can you sign this form for me?\"" id a07_comn_05_d0be6354

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0090"
    sachiko "\"You want my autograph? Sure, but I'm not co-signing any loans.\"" id a07_comn_05_1f34d198

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_0050"
    miyako "\"No, it's—\"" id a07_comn_05_05f10ed7

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "2FU_0071"
    fumi "\"She needs a guardian to fill out and sign a form. I thought it might take a long time to send it home, so she should ask you, since you're related.\"" id a07_comn_05_ca895abb

    "Fumi supplied."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0091"
    sachiko "\"Ah, gotcha.\"" id a07_comn_05_0e6c1545

    "She took the printout and looked over its contents."

    show sachiko:
        ShakeYes

    voice "2SA_0092"
    sachiko "\"Okay. I'll fill it out, so come and get it after dinner.\"" id a07_comn_05_42e841a3

    show miyako:
        "miyako 1 sm school_a c" with Dissolve(0.25)
        xoffset 0 yoffset 0
        ShakeYes

    voice "2MI_0051"
    miyako "\"Thank you.\"" id a07_comn_05_216e1814

    show miyako 1 sm school_a c:
        xoffset 0 yoffset 0
    with None

    "Miyako bowed her head."

    voice "2SA_0093"
    sachiko "\"Okay, I'm gonna go stop those two from wrecking the bath. You guys want to see it?\"" id a07_comn_05_349cef5c

    show fumi 1 sm school_scarf c
    show miyako 1 sm school_a b
    with dict_dissolve_25

    $ voice2("fumi","2FU_0072","miyako","2MI_0052")
    fumi_miyako "\"Sure.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
