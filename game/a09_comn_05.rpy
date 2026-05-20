label a09_comn_05:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Sachiko and Miyako walked down the street in front of the station."

    show sachiko 1 sm outfit a at pos_ls
    show miyako 1 sm casual_a b at pos_rs
    with dict_dissolve_25

    voice "2SA_0492"
    sachiko "\"Sorry to make you carry all that.\""

    voice "2MI_0608"
    miyako "\"It's fine. I was the one who asked to come along.\""

    "Sachiko looked apologetic, but Miyako was all smiles."

    "They both had bags from a candy store in their arms."

    "All full of Valentine's chocolate."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0493"
    sachiko "\"It does add up to quite the number.\""

    show miyako 1 sm casual_a e with dict_dissolve_25

    voice "2MI_0609"
    miyako "\"You give it to all of the students at the dorm?\""

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0494"
    sachiko "\"Happily, I always get some from all of them every year. Gotta reciprocate.\""

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0610"
    miyako "\"Not on White Day?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0495"
    sachiko "\"I get and give on White Day, too.\""

    voice "2MI_0611"
    miyako "\"Hm?\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0496"
    if persistent.dpatch:
        sachiko "\"That kinda thing happens at a girls' school. Everybody just likes wrapping up chocolate and giving it out. And if it's fun, the more the merrier, right?\"" id a09_comn_05_7d6beff9
    else:
        sachiko "\"That kinda thing happens on a girl’s campus. Everybody just likes wrapping up chocolate and giving it out. And if it's fun, the more the merrier, right?\""

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0612"
    miyako "\"I see.\""

    show sachiko:
        "sachiko 1 sm outfit f" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0497"
    sachiko "\"I'm happy to play along if it makes them happy♪\""

    show sachiko 1 sm outfit f:
        xoffset 0 yoffset 0
    with None
    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0498"
    sachiko "\"...Of course, there's a bunch of them and only one of me. It's a little hard on the budget.\""

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0613"
    miyako "\"Ahaha...\""

    "Four bags of chocolate... Yeah, that's probably not cheap."

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0614"
    miyako "\"Come to think of it, why didn't you buy them at Fumi's store?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0499"
    sachiko "\"Because I have to give some to Foomin, too. I don't think she'd be very happy to get something they sell at her own store.\""

    show miyako 1 sm casual_a e with dict_dissolve_25

    voice "2MI_0615"
    miyako "\"Oh, I get it.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0500"
    sachiko "\"Though she might be happy to get more allowance if her store gets more sales.\""

    "Sachiko laughed."

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0616"
    miyako "\"Did you buy chocolate for me, too?\""

    "Miyako looked over at Sachiko."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0501"
    sachiko "\"I did. I figure Fumi's likely to rope you into buying or making some.\""

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0617"
    miyako "\"You think so?\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0502"
    sachiko "\"Definitely.\""

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0618"
    miyako "\"I'll be able to join in the chocolate exchange too, then. I'm looking forward to Valentine's Day now.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0503"
    sachiko "\"That's not what the holiday's supposed to be about though, really.\""

    show miyako 1 sm casual_a h with dict_dissolve_25

    voice "2MI_0619"
    miyako "\"Well, I think it's okay. It's fun giving and receiving, isn't it?♪\""

    hide miyako with dict_dissolve_50

    "Miyako walked with wide steps, swinging the bags at her sides. Almost skipping."

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "2SA_0504"
    sachiko "\"Hey, don't swing them like that!\""

    $ side_image = "miyako 1 side casual_a d"

    voice "2MI_0620"
    miyako "\"Hm? What?\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_0505"
    sachiko "\"You'll smush the stuff in the bags... if you...\""

    show sachiko 1 sm outfit i with dict_dissolve_25

    "Sachiko stopped when Miyako turned around and squinted as if she was too bright to look at."

    show miyako 1 sm casual_a e at pos_rs with dict_dissolve_25

    voice "2MI_0621"
    miyako "\"What is it?\""

    show sachiko 2 sm outfit a with dict_dissolve_25

    voice "2SA_0506"
    sachiko "\"...Why'd you come down?\""

    "Her face was serious suddenly."

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0622"
    miyako "\"Well, because you invited me.\""

    "Miyako's face was blank at the sudden change in topic."

    show sachiko 2 sm outfit b with dict_dissolve_25

    voice "2SA_0507"
    sachiko "\"Is that the only reason why?\""

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0623"
    miyako "\"I started wanting to be human after watching their room for a while. Eventually, I thought I could get rid of my wings.\""

    voice "2MI_0624"
    miyako "\"But that was only because you introduced me to them since you were fond of them, so it does come back to you in the end.\""

    show sachiko 2 sm outfit d with dict_dissolve_25

    voice "2SA_0508"
    sachiko "\"......\""

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0625"
    miyako "\"If you hadn't called out to me that day on the roof, I'd probably still be flying somewhere now.\""

    "She smiled innocently."

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0509"
    sachiko "\"Do you think it's coincidence?\""

    show miyako 1 sm casual_a e with dict_dissolve_25

    voice "2MI_0626"
    miyako "\"Most likely. That day was my first time flying around here, after all.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0510"
    sachiko "\"...Right.\""

    "Sachiko's expression softened at that."

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0627"
    miyako "\"Why did you invite me?\""

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0511"
    sachiko "\"You asked me that before. But I just...\""

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0512"
    sachiko "\"No, I think it's 'cause I was cold.\""

    "This time there was a self-deriding look on her face. Boy, she's busy."

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0628"
    miyako "\"...Cold?\""

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0513"
    sachiko "\"I'm sorry.\""

    voice "2MI_0629"
    miyako "\"...?\""

    hide sachiko with dict_dissolve_50

    "Miyako merely stared blankly at her, not knowing why Sachiko had apologized to her."

    "Sachiko suddenly started walking again, silently passing by Miyako."

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0630"
    miyako "\"...!\""

    hide miyako with dict_dissolve_50

    "Miyako jogged to catch up with her..."

    show miyako 1 lg casual_a b:
        xcenter 662
    show sachiko 2 lg outfit f:
        xcenter 362
    with dict_dissolve_50
    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0514"
    sachiko "\"...Oh?\""

    camera
    with None

    "...and linked arms with her."

    show miyako 1 lg casual_a h with dict_dissolve_25

    voice "2MI_0631"
    miyako "\"Well, it is cold♪\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0515"
    sachiko "\"...You're toasty. Are you sleepy?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 1:
        jump a09_comn_06
    elif route2 == 1:
        jump a09_cou1_02
    elif route2 == 2:
        jump a09_cou2_03
    elif route2 == 3:
        jump a09_cou3_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
