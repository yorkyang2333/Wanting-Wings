label a07_comn_05:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    $ side_image = "hina 1 side school_scarf o"

    voice "2HI_0089"
    hina "\"It's cold~\""

    $ side_image = "fumi 1 side school_scarf b"

    voice "2FU_0061"
    fumi "\"We're home.\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0062"
    sachiko "\"Welcome back! It's a cold one today~\""

    $ side_image = "rin 2 side school_scarf a"

    voice "2RI_0083"
    rin "\"Here.\""

    show sachiko:
        "sachiko 1 lg outfit g" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0063"
    sachiko "\"Danke♪\""

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
    sachiko "\"I'll treat you each to one drink from the vending machine as payment.\""

    "The vending machine was Sachiko's property, and she used its proceeds to pay for her cigarettes. Well, at least everything in it is only 100 yen..."

    show rin 1 sm school_scarf k with dict_dissolve_25

    voice "2RI_0084"
    rin "\"Wow. Yay.\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0065"
    sachiko "\"Oh, I only got cold ones, though.\""

    show hina:
        "hina 1 sm school_scarf g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0090"
    hina "\"What time of year do you think it is?!\""

    show hina 1 sm school_scarf g with None
    show hina:
        ShakeJump

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0066"
    sachiko "\"But you got pissed at me when I put beer in it in the summer!\""

    show hina:
        xoffset 0 yoffset 0
        ShakeJump

    voice "2HI_0091"
    hina "\"Put that in the fridge in your room!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "What's that have to do with the time of year?"

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0085"
    rin "\"Talk about not catering to your customer's needs.\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0067"
    sachiko "\"If we're talking needs, I could get a cigarette vending—\""

    show hina:
        ShakeJump
        ShakeJump

    voice "2HI_0092"
    hina "\"NO!!\""

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
    miyako "\"I'm... home.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0068"
    sachiko "\"Welcome home, Mikoyan.\""

    show miyako 2 sm school c with dict_dissolve_25

    voice "2MI_0039"
    miyako "\"......\""

    voice "2SA_0069"
    sachiko "\"What is it?\""

    show miyako 1 sm school_a c with dict_dissolve_25

    voice "2MI_0040"
    miyako "\"'I'm home,' 'Welcome home'... They're very nice phrases.\""

    "It was Miyako's first time exchanging such pleasantries."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0070"
    sachiko "\"They are, aren't they?\""

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
    rin "\"You've been calling her that for a while now... Is it a new nickname?\""

    show miyako:
        xcenter 930
    show hina 1 sm school_scarf k:
        alpha 1.0 xcenter 622
    show rin 1 sm school_scarf a:
        alpha 1.0 xcenter 776
    with None

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0071"
    sachiko "\"Mikoyan! It's cute, isn't it?\""

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0087"
    rin "\"Well, I guess so. Do you like it, Takaoka?\""

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0041"
    miyako "\"I don't mind. I can tell it's referring to me.\""

    show miyako 1 sm school_a c with dict_dissolve_25

    voice "2MI_0042"
    miyako "\"And Sachiko gave me the name Miyako, too.\""

    $ side_image = "fumi 1 side school_scarf e"

    voice "2FU_0062"
    fumi "\"Huh? Sachiko named you, Miyako?\""

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
    hina "\"There must be a pretty big age difference, then.\""

    show hina 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 sm school_scarf g" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2RI_0088"
    rin "\"Are you sure you're not her niece?\""

    show rin 1 sm school_scarf g:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko 1 sm outfit j" with Dissolve(0.25)
        ShakeJump

    voice "2SA_0072"
    sachiko "\"Hey! What are you whispering about over there?!\""

    show sachiko 1 sm outfit c:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2SA_0073"
    sachiko "\"I just picked from a list her parents had. {i}When I was little{/i}. Right, Mikoyan?\""

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0043"
    miyako "\"Oh, yes. You're right.\""

    "Nice save."

    show rin 2 sm school_scarf a with dict_dissolve_25

    voice "2RI_0089"
    rin "\"You always come up with the weirdest crap.\""

    "Like Hinacchi and Foomin."

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0074"
    sachiko "\"What's weird about them, Rinrin?\""

    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0090"
    rin "\"I'm not answering to that!\""

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_0044"
    miyako "\"Rinrin? Rin has a nickname, too?\""

    show hina 1 sm school_scarf m with dict_dissolve_25

    voice "2HI_0094"
    hina "\"It didn't stick.\""

    $ side_image = "fumi 1 side school_scarf d"

    voice "2FU_0063"
    fumi "\"She never replied to it no matter how much Sachiko used it. They were both pretty stubborn, but—\""

    show hina 1 sm school_scarf a with dict_dissolve_25

    voice "2HI_0095"
    hina "\"In the end, Sachiko gave up.\""

    show miyako 1 sm school_a a with dict_dissolve_25

    voice "2MI_0045"
    miyako "\"I see.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0075"
    sachiko "\"Oh, right. The maintenance on the bath is done today! They've still gotta hook the gas up though, so it'll be a little longer 'til you can use it.\""

    show rin 2 sm school_scarf e with dict_dissolve_25

    voice "2RI_0091B"
    rin "\"Finally~ Now we don't have to freeze our butts off going to the other dorm.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0076"
    sachiko "\"Good for you, Rinrin!\""

    show rin 1 sm school_scarf j with Dissolve(0.1)
    show rin:
        ShakeJump

    voice "2RI_0092"
    rin "\"Drop it!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0077"
    sachiko "\"It should've been done over winter break, but they kept finding other stuff to fix, so it kinda became a big project.\""

    hide miyako
    with Dissolve(0.5)

    show rin 1 sm school_scarf b behind fumi
    show fumi 1 sm school_scarf a:
        xcenter 940
    with dict_dissolve_25

    voice "2FU_0064"
    fumi "\"There was some damage in places.\""

    show hina 1 sm school_scarf h with dict_dissolve_25

    voice "2HI_0096"
    hina "\"That's putting it lightly. It was falling apart.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0078"
    sachiko "\"So I'll let you girls have the first bath, special!\""

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "2FU_0065"
    fumi "\"Yay~\""

    show sachiko 1 sm outfit e with dict_dissolve_25

    voice "2SA_0079"
    sachiko "\"It's bigger now, so let's all go in together♪\""

    show hina:
        "hina 1 sm school_scarf f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0097"
    hina "\"Go in by yourself!\""

    show hina 1 sm school_scarf f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0093B"
    rin "\"Can we go see it?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0080"
    sachiko "\"Long as you don't run the water.\""

    show rin 1 sm school_scarf c with dict_dissolve_25

    voice "2RI_0094"
    rin "\"Gotcha. Let's go check it out, Hina.\""

    show hina 1 sm school_scarf e with dict_dissolve_25

    voice "2HI_0098"
    hina "\"Sure.\""

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
    sachiko "\"Anywhere other than the bath you want fixed up?\""

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_0066"
    fumi "\"Hmm~ You fixed our water in the fall. I think everything else is fine.\""

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0082"
    sachiko "\"Good. Actually, speaking of water, I think the roof might be leaking.\""

    show fumi 2 sm school_scarf d with dict_dissolve_25

    voice "2FU_0067"
    fumi "\"Uh oh, you'll need to get that fixed before the rainy season, then.\""

    show sachiko 2 sm outfit a with dict_dissolve_25

    voice "2SA_0083"
    sachiko "\"Yeah... It's an old building, so it's starting to fall apart in places.\""

    show miyako 1 sm school_a e with dict_dissolve_25

    voice "2MI_0046"
    miyako "\"How long have you been watching over it?\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0084"
    sachiko "\"Mm? Five years, I guess.\""

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0068"
    fumi "\"Huh, really?\""

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0047"
    miyako "\"......\""

    play sound se_moooto
    pause 1.5

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "2SA_0085"
    sachiko "\"What was that?\""

    "There was quite a bit of noise coming from the bath."

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "2SA_0086"
    sachiko "\"Hey! What the heck are you two doing in there?\""

    $ side_image = "side/hina_rin_school_scarf_sozai01.webp"

    $ voice2("hina","2HI_0099","rin","2RI_0095")
    hina_rin "\"Checking for cameras!\""

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0087"
    sachiko "\"They have no faith in me.\""

    show sachiko 1 sm outfit d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "2FU_0069"
    fumi "\"Ahaha...\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0088"
    sachiko "\"They really think I'd hide 'em somewhere they'd find right away?\""

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "2FU_0070"
    fumi "\"...Haha.\""

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0089"
    sachiko "\"I'm joking. There aren't any cameras.\""

    show miyako 1 sm school_a e with dict_dissolve_25

    voice "2MI_0048"
    miyako "\"Oh, that's right.\""

    show miyako:
        ShakeYes2_5_500

    "Miyako had been watching their interactions with a smile, but she suddenly remembered something and dug through her bag."

    show miyako 1 sm school_a a:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2MI_0049"
    miyako "\"Can you sign this form for me?\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0090"
    sachiko "\"You want my autograph? Sure, but I'm not co-signing any loans.\""

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_0050"
    miyako "\"No, it's—\""

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "2FU_0071"
    fumi "\"She needs a guardian to fill out and sign a form. I thought it might take a long time to send it home, so she should ask you, since you're related.\""

    "Fumi supplied."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0091"
    sachiko "\"Ah, gotcha.\""

    "She took the printout and looked over its contents."

    show sachiko:
        ShakeYes

    voice "2SA_0092"
    sachiko "\"Okay. I'll fill it out, so come and get it after dinner.\""

    show miyako:
        "miyako 1 sm school_a c" with Dissolve(0.25)
        xoffset 0 yoffset 0
        ShakeYes

    voice "2MI_0051"
    miyako "\"Thank you.\""

    show miyako 1 sm school_a c:
        xoffset 0 yoffset 0
    with None

    "Miyako bowed her head."

    voice "2SA_0093"
    sachiko "\"Okay, I'm gonna go stop those two from wrecking the bath. You guys want to see it?\""

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
