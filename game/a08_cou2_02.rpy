label a08_cou2_02:

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show rin 1 lg pyjama glasses k at pos_r
    with Dissolve(0.25)

    show rin:
        yoffset 0
        ease 1.0 yoffset -10
        ease 1.0 yoffset 0

    voice "2RI_0650"
    rin "\"Mmmmh~\""

    "Rin stretched grandly, reaching a good stopping point in her book."

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0532"
    miyako "\"Oh...\""

    "She was just stretching, but she was so flexible that it looked impressive. It almost looked like the cobra pose in yoga."

    show hina 2 lg pyjama_pjm c at pos_l with dict_dissolve_25

    voice "2HI_0640"
    hina "\"She's something, isn't she?\""

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0533"
    miyako "\"Yes.\""

    "Miyako tried imitating her but could only bend her back about half as much as Rin had. But Miyako wasn't inflexible, it was just that Rin was extremely limber."

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0651"
    rin "\"What?\""

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0641"
    hina "\"Just talking about how flexible you are.\""

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0530"
    fumi "\"Ugh...\""

    "Now that one's inflexible. She can't even get her chest off the floor. Though she's got a handicap in that area."

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0642"
    hina "\"Rin did ballet.\""

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0534"
    miyako "\"Did she?\""

    show rin 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0652"
    rin "\"I quit a long time ago, though.\""

    show hina 1 lg pyjama_pjm b with dict_dissolve_25

    voice "2HI_0643"
    hina "\"But she said she was good at it. Maybe she could have been a famous ballerina if she'd kept it up.\""

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0535"
    miyako "\"That's pretty amazing.\""

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0653"
    rin "\"I would have quit sooner or later. I don't have the personality for it.\""

    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0644"
    hina "\"There you go again. You put yourself down too much, Rin.\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0654"
    rin "\"No, you just give me too much credit.\""

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0645"
    hina "\"I do not! I know! Do that thing, Rin!\""

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0655"
    rin "\"What thing?\""

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0646"
    hina "\"Umm, where you stand on one foot and raise the other one. Uhh... arabica?\""

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0656"
    rin "\"Arabesque. And no, I don't want to.\""

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0647"
    hina "\"Why?\""

    show rin 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0657"
    rin "\"Because it's a pain. It's too late at night.\""

    hide rin with dict_dissolve_50

    "Rin rolled over, facing the other way."

    show hina:
        "hina 1 lg pyjama_pjm o" with Dissolve(0.25)
        ShakeNo

    voice "2HI_0648"
    hina "\"Mmmmmmh!\""

    show hina 1 lg pyjama_pjm o:
        xoffset 0 yoffset 0
    with None

    "The only comeback Hina had was to whine."

    $ side_image = "rin 1 side pyjama glasses h"

    voice "2RI_0658"
    rin "\"That won't convince me.\""

    $ side_image = "fumi 1 side pyjama b"

    voice "2FU_0531"
    fumi "\"Oh, I think I'd like to see that. What about you, Miyako?\""

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0536"
    miyako "\"Yes, I would, too.\""

    "Fumi put in her support behind Hina and Miyako quickly caught on and backed her up."

    show hina:
        "hina 1 lg pyjama_pjm n" with Dissolve(0.25)
        ShakeNo

    voice "2HI_0649"
    hina "\"Mmmh...\""

    show hina 1 lg pyjama_pjm n:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses g at pos_r with dict_dissolve_50

    voice "2RI_0659"
    rin "\"Haah... Okay, just a little. I'm not doing anything showy.\""

    "In the end, Rin folded."

    show hina:
        "hina 1 lg pyjama_pjm c" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0650"
    hina "\"Yay~! It's really cool! Everybody, watch.\""

    show hina 1 lg pyjama_pjm c:
        xoffset 0 yoffset 0
    with None

    "She bragged like it was her doing it."

    show rin 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0660RE"
    rin "\"Geez...\""

    hide rin
    hide hina
    with dict_dissolve_50

    "Setting her book down on the table, Rin stood slowly."

    "She twisted this way and that, doing the bare minimum of a stretch. Even that was somewhat impressive."

    "At the same time, Fumi pulled the table back to give her more space."

    show bg_obi with bg_effect_30_1200
    pause 0.5

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0661B"
    rin "\"Mmh...\""

    "She straightened up slowly, reaching her full height and making them all almost forget how she usually slouched."

    $ side_image = "miyako 1 side pyjama_a f"

    voice "2MI_0537"
    miyako "\"Wow!\""

    "She looked beautiful just standing there. That was enough for Miyako to exclaim."

    $ side_image = "hina 2 side pyjama_pjm g"

    voice "2HI_0651"
    hina "\"Watch what she does with her feet! It's really amazing!\""

    $ side_image = "fumi 1 side pyjama b"

    voice "2FU_0532"
    fumi "\"I'm watching.\""

    "Rin went through the positions at a quick pace. She must have done it so often in the past that she was going off of muscle memory."

    $ side_image = "hina 1 side pyjama_pjm q"

    voice "2HI_0652"
    hina "\"Now pay attention to her upper body. See? Her legs are moving so much, but her upper body stays completely still.\""

    $ side_image = "side/fumi_miyako_pyjama_sozai01.webp"

    $ voice2("fumi","2FU_0533","miyako","2MI_0538")
    fumi_miyako "\"It's true!\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0662"
    rin "\"...You're not making this easy.\""

    $ side_image = "hina 1 side pyjama_pjm p"

    voice "2HI_0653"
    hina "\"Don't look like you hate it. Come on, make a cool face, too!\""

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0663"
    rin "\"Haah... Last one. I'm lifting my leg a bit...\""

    "With another sigh, she faked a smile. It was a bit strained."

    "Her leg slowly lifted..."

    "She didn't lift it as high as last time, but it still made the length of her arms and legs prominent. It almost seemed like her limbs were filling up the room."

    $ side_image = "hina 2 side pyjama_pjm c"

    voice "2HI_0654"
    hina "\"......\""

    "Hina looked on admiringly."

    $ side_image = "hina 2 side pyjama_pjm g"

    voice "2HI_0655"
    hina "\"I fell in love with Rin when I saw this. That's why Rin's arapaima is a treasure of mine.\""

    $ side_image = "fumi 2 side pyjama c"

    voice "2FU_0534"
    fumi "\"Wow...\""

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0539"
    miyako "\"Ooh...\""

    "The two were touched."

    "...But it's an arabesque. Not a fish."

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0664"
    rin "\"......\""

    "She lowered her leg slowly to finish."

    hide bg_obi with bg_effect_31_1200
    pause 0.5

    show rin z4 1 lg pyjama glasses a as rin_1 with Dissolve(0.25)

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0540"
    miyako "\"It was beautiful.\""

    show rin z4 1 lg pyjama glasses k as rin_1 with dict_dissolve_25

    voice "2RI_0665"
    rin "\"Thanks. I'm not doing it again.\""

    $ side_image = "fumi 2 side pyjama i"

    voice "2FU_0535"
    fumi "\"Your tracksuit looked like a tutu to me.\""

    show rin z4 2 lg pyjama glasses e as rin_1 with dict_dissolve_25

    voice "2RI_0666"
    rin "\"Come on, I was just stretching a little.\""

    $ side_image = "hina 1 side pyjama_pjm o"

    voice "2HI_0656"
    hina "\"Mfh!\""

    "Hina raised her leg in imitation of Rin. She was flexible too, but in a different way, so it didn't go as well."

    show rin z4 1 lg pyjama glasses e as rin_1 with dict_dissolve_25

    voice "2RI_0667"
    rin "\"Ah, hey! An amateur shouldn't try that without a barre—\""

    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_0657"
    hina "\"Whoa, wah... aaah?!\""

    "Not even getting to the arabesque, she lost her balance just trying to stand on one leg."

    hide rin_1
    show rin 1 lg pyjama glasses h:
        xcenter 772
        ease 0.25 yoffset 6
        ease 0.25 yoffset 0
    show hina 1 lg pyjama_pjm d:
        xcenter 252
        ease 0.25 yoffset 8
        ease 0.25 yoffset 0
    with dict_dissolve_25

    voice "2RI_0668"
    rin "\"Ah!\""

    show rin 1 lg pyjama glasses h:
        xcenter 772 yoffset 0
    show hina 1 lg pyjama_pjm d:
        xcenter 252 yoffset 0
    with None

    "Rin reached out and caught her."

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0669"
    rin "\"What are you doing?! You could've hurt yourself!\""

    show hina 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0658"
    hina "\"I'm sorry... I thought maybe if I could do it too, I could dance with you.\""

    show rin:
        "rin 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0670"
    rin "\"Haah... I'm not doing that. I'm not good at dancing with people.\""

    show rin 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    voice "2HI_0659"
    hina "\"......\""

    show rin 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0671"
    rin "\"Alright, show's over.\""

    hide rin
    hide hina
    with dict_dissolve_50

    "Curtly letting go of Hina, Rin lay down once more."

    "Clap clap clap."

    $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_0541"
    miyako "\"......\""

    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0536"
    fumi "\"......\""

    "Miyako and Fumi exchanged a glance, applauding the performance."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_cou2_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
