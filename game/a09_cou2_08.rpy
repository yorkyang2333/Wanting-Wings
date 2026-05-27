label a09_cou2_08:

    scene bg04da with Dissolve(0.5)
    pause 1.5

    play music bgm05

    "—At the same time, that moon illuminated the two girls in the classroom."

    "Like Miyako had mentioned, the moon was shockingly bright. The two could easily look for their forgotten object without even turning on the lights."

    $ side_image = "rin 1 side school a"

    voice "2RI_1053"
    rin "\"Found it~\"" id a09_cou2_08_100d04d1

    "That didn't take long. Rin called Hina over from a locker."

    "Fumi's prediction was right. It was the collar they were looking for."

    if persistent.dpatch:
        "She'd realized at the grocery store. Rin had muttered, \"oh,\" which Hina hadn't missed, and the latter had practically dragged the former back to the school." id a09_cou2_08_97861fa7
    else:
        "She'd realized at the grocery store. Rin had muttered, \"oh,\" which Hina hadn't missed, and the latter had practically dragged the former back to the campus."

    show hina 2 lg school c with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_1042"
    hina "\"Oh, good...\"" id a09_cou2_08_3d20d13b

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina was relieved when she saw the collar."

    $ side_image = "rin 2 side school e"

    voice "2RI_1054"
    rin "\"You don't need to be that worried. I knew where it was, didn't I?\"" id a09_cou2_08_2da1572f

    "Rin spun the collar on her finger, looking exasperated."

    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_1043"
    hina "\"...That's not the problem.\"" id a09_cou2_08_0a444ebc

    "Hina bit her lip in the dim light. I'm not sure if Rin saw."

    $ side_image = "rin 1 side school k"

    voice "2RI_1055"
    rin "\"We could have just gotten it tomorrow, couldn't we?\"" id a09_cou2_08_4b285ad7

    show hina 1 lg school f with dict_dissolve_25

    voice "2HI_1044"
    hina "\"No, we couldn't!\"" id a09_cou2_08_8ecd2dca

    $ side_image = "rin 1 side school j"

    voice "2RI_1056"
    rin "\"Whoa!\"" id a09_cou2_08_464b20f5

    "Rin jumped up, surprised at Hina's vehement reaction to the offhand comment she'd made."

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_1045"
    hina "\"You treat my collar too carelessly! I keep telling you to take better care of it!\"" id a09_cou2_08_cc4a9671

    $ side_image = "rin 1 side school g"

    voice "2RI_1057"
    rin "\"It's not a collar, it's a choker...\"" id a09_cou2_08_aa9834fa

    show hina 1 lg school f with dict_dissolve_25

    voice "2HI_1046"
    hina "\"It doesn't matter what you call it!\"" id a09_cou2_08_593408a4

    "Rin's oblivious retort was thrown back in her face."

    show hina 2 lg school d with dict_dissolve_25

    voice "2HI_1047"
    hina "\"I treat that collar like it's a part of you and take good care of it, Rin. Can't you do the same thing and think of it as a piece of me?\"" id a09_cou2_08_9639cb4e

    $ side_image = "rin 1 side school i"

    voice "2RI_1058"
    rin "\"That's overblown, isn't it? Things aren't people...\"" id a09_cou2_08_58b735ff

    "The issue of Hina and Rin's different approaches to their belongings reared its head again."

    "To Rin, things were things. But to Hina, things were physical representations of feelings."

    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_1048"
    hina "\"...You forgot it at New Year's, too.\"" id a09_cou2_08_8f622d07

    $ side_image = "rin 2 side school e"

    voice "2RI_1059"
    rin "\"I just wasn't thinking then. I was nervous being at someone else's house...\"" id a09_cou2_08_3e86a81f

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_1049"
    hina "\"...It's not just the collar.\"" id a09_cou2_08_c8533ef9

    "Her gaze dropped lonesomely for a moment, but she quickly raised her head."

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_1050"
    hina "\"You brushed my hand away on our way back from the shrine, too.\"" id a09_cou2_08_9aea757f

    $ side_image = "rin 1 side school i"

    voice "2RI_1060"
    rin "\"That's 'cause I got embarrassed since I saw some girls from our class... I thought we were already over that, anyway.\"" id a09_cou2_08_627e8dec

    "Well, Rin was."

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_1051"
    hina "\"Would you be embarrassed if everyone found out we were dating?\"" id a09_cou2_08_70f582a7

    $ side_image = "rin 1 side school e"

    voice "2RI_1061"
    rin "\"What? What are you saying?\"" id a09_cou2_08_d436745a

    "She'd asked that question before. Hina admired Rin, so she was always worried that she wasn't a good match for her."

    "Rin didn't understand why Hina was repeating the question, didn't understand where her anxiety came from."

    "Hina's frustration was mounting. The water was starting to lap at the edges of the dam in her heart."

    "Usually, Fumi or Miyako would be able to interject at this point, but they weren't around this time."

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_1052"
    hina "\"Would you be embarrassed if you were dating Honjou?\"" id a09_cou2_08_ce939e01

    play sound se_locker_c

    $ side_image = "rin 1 side school h"

    voice "2RI_1062"
    rin "\"Where is this coming from?!\"" id a09_cou2_08_bc8d5d3b

    hide hina with dict_dissolve_25

    "Rin shut the locker a little violently and strode toward the front door of the classroom they'd come in from. Hina jogged after her."

    show bg_obi
    show rin z4 1 lg school h:
        xcenter 298
    show hina z4 2 lg school h:
        xcenter 726
    with dict_dissolve_25

    voice "2RI_1063"
    rin "\"I'm gonna get mad. You're making the same mistake you did before with Sachiko!\"" id a09_cou2_08_3df55ca7

    "She's not, Rin. Hina doesn't suspect you of cheating. She's just looking for some sincerity."

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1053"
    hina "\"Why didn't you turn her down clearly?\"" id a09_cou2_08_fad77760

    "Hina blocked Rin's escape. Rin gave up on leaving the classroom and leaned against the podium instead."

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1064"
    rin "\"I couldn't think of a way to do it. You know I don't want people to dislike me, right?\"" id a09_cou2_08_3f128413

    "Why don't you worry about how your girlfriend feels about you?"

    show hina z4 2 lg school h with dict_dissolve_25

    voice "2HI_1054"
    hina "\"I'm always only watching you, Rin, but you always look away from me.\"" id a09_cou2_08_4e16fe56

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1065"
    rin "\"What...? Do I really...?\"" id a09_cou2_08_43d56d31

    show hina z4 1 lg school f with dict_dissolve_25

    voice "2HI_1055"
    hina "\"You should look at me more often!\"" id a09_cou2_08_b2113532

    show rin z4 2 lg school e with dict_dissolve_25

    voice "2RI_1066"
    rin "\"...Haha.\"" id a09_cou2_08_f7ff8cb5

    show rin z4 2 lg school b with dict_dissolve_25

    "Rin averted her eyes again as Hina closed in on her."

    "With the {i}worst possible timing{/i}."

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_1056"
    hina "\"......\"" id a09_cou2_08_d484443f

    window hide
    show white:
        alpha 1.0 additive 1.0
        linear 0.5 alpha 0.0
    pause 1.0
    window auto

    "Soundless sparks flew."

    play sound se_2s_h004

    stop music fadeout 1.0

    scene white with Dissolve(0.1875)
    pause 1.5625

    scene kimikara_06_a with Dissolve(0.5)
    pause 1.5

    voice "2RI_1067"
    rin "\"Wah!\"" id a09_cou2_08_c312d564

    "Hina pushed Rin down against the blackboard. The collar fell from her hands and rolled away on the ground."

    voice "2RI_1068"
    rin "\"Hey, Hina?\"" id a09_cou2_08_491136a8

    voice "2HI_1057"
    hina "\"......\"" id a09_cou2_08_9ec9987f

    "Hina looked down at Rin. Her hair bristled, the glow of the moonlight making it look like a mane."

    voice "2RI_1069"
    rin "\"Uh, I gotta pick up the choker...\"" id a09_cou2_08_e56f2dfe

    "Rin tried to stand to flee, but Hina didn't loosen her grip on her."

    voice "2RI_1070"
    rin "\"Are you mad? I'm sorry. I won't forget it again. You should remind me if it seems like I'm gonna—\"" id a09_cou2_08_d9a31751

    voice "2HI_1058"
    hina "\"You don't get it.\"" id a09_cou2_08_98d94def

    voice "2RI_1071"
    rin "\"Come on, let's just stand up.\"" id a09_cou2_08_b469dff1

    "She tried to stand up again, but..."

    "Conk."

    "Hina headbutted her, though not hard, and only held her more firmly."

    voice "2HI_1059"
    hina "\"...We're {i}doing it{/i}.\"" id a09_cou2_08_5a37c8c4

    voice "2RI_1072"
    rin "\"Huh? Doing what?\"" id a09_cou2_08_bcc073d6

    "Hina didn't answer with words."

    play music bgm05 fadein 1.0

    scene kimikara_06_b with Dissolve(0.5)

    voice "2RI_1073"
    rin "\"Wait, you don't mean...? Here? Where did this come from?!\"" id a09_cou2_08_01bea2f7

    "Rin panicked when she caught on."

    voice "2RI_1074"
    rin "\"I mean, uniforms in the classroom is a pretty orthodox situation for some fun stuff, but there's such a thing as mood, you know? How 'bout next time, huh?\"" id a09_cou2_08_a4dfc89d

    "Rin tried to get out of it with her usual flippant laughter."

    "But that didn't work on Hina in her current state. She stared Rin down with her fiery gaze."

    voice "2RI_1075"
    rin "\"Hey, are you serious about this?\"" id a09_cou2_08_c8c28999

    voice "2HI_1060"
    hina "\"I've been bothered by it ever since you said I was heavy.\"" id a09_cou2_08_ce70e30b

    voice "2RI_1076"
    rin "\"What, about going on a diet? You're not fat—\"" id a09_cou2_08_cdd2340c

    voice "2HI_1061"
    hina "\"No. Not my weight. You said it the last time we were talking about the collar. You said that and then you left the room.\"" id a09_cou2_08_b524b70e

    voice "2RI_1077"
    rin "\"Did that happen?\"" id a09_cou2_08_f025ffaf

    voice "2HI_1062"
    hina "\"It did. So I've been trying not to cling to you 'cause I don't want to bother you.\"" id a09_cou2_08_7d9ac1dd

    voice "2RI_1078"
    rin "\"I'm not both—\"" id a09_cou2_08_2fda529e

    scene kimikara_06_c with Dissolve(0.5)

    voice "2HI_1063"
    hina "\"But I can't do it!!\"" id a09_cou2_08_c3d78ed3

    "Hina's shout shook the air in the classroom, pinning Rin to the wall even harder."

    voice "2HI_1064"
    hina "\"We're {i}doing it{/i}. When we're doing it, you only look at me.\"" id a09_cou2_08_254485a8

    "Her breath was close and hot."

    voice "2RI_1079"
    rin "\"But, listen, we're in the classroom. A security guard might come, and we'll get our uniforms dirty. So let's not, okay?\"" id a09_cou2_08_d2e9f3ce

    scene kimikara_06_d with Dissolve(0.5)

    voice "2HI_1065"
    hina "\"No.\"" id a09_cou2_08_19f445cb

    "The raging beast couldn't be contained by the flimsy cage of Rin's reasonable arguments."

    "The light of the moon made Hina's eyes glint even brighter."

    voice "2RI_1080"
    rin "\"Hold it, hold it... Okay, what if I tell you 'wait'? Hina?\"" id a09_cou2_08_ee88418d

    voice "2HI_1066"
    hina "\"That doesn't work without the collar.\"" id a09_cou2_08_806324a9

    voice "2RI_1081"
    rin "\"......\"" id a09_cou2_08_e02d3fa5

    "Rin paled at that. The collar had rolled halfway across the classroom. It was way out of her reach."

    voice "2RI_1082"
    rin "\"Ah!\"" id a09_cou2_08_8683ac6a

    "Hina pried open Rin's shirt to draw her attention back to her."

    voice "2HI_1067"
    hina "\"This is your fault, Rin...\"" id a09_cou2_08_214d7ae9

    voice "2RI_1083"
    rin "\"Hey, you're scaring me... Hina...\"" id a09_cou2_08_4742ca67

    "The ease was gone from her voice now. Rin was truly frightened."

    voice "2RI_1084"
    rin "\"This isn't a dog... it's a wolf.\"" id a09_cou2_08_80e619b8

    "And Rin's eyes were the eyes of a lamb."

    stop music fadeout 1.0
    scene black with Dissolve(2.0)
    pause 0.5

    scene continue with Dissolve(2.0)
    pause 2.0

    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
