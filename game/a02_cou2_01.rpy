label a02_cou2_01:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg01aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 lg pyjama g at pos_r
    show rin 1 lg pyjama glasses a at pos_l
    with Dissolve(0.25)

    show hina:
        ShakeJump2

    voice "HIN_0542"
    hina "\"N-Nnnnh~\"" id a02_cou2_01_f0df9c4a

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina put her pen down and looked up from her notes, stretching grandly."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0543"
    hina "\"...Huh? Where's Asou?\"" id a02_cou2_01_d51affa3

    "Hina glanced around the room."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0387"
    rin "\"She just left to get stuff for dinner. She said she'd go by herself since you were concentrating so hard.\"" id a02_cou2_01_cb5f79ec

    voice "HIN_0544"
    hina "\"Oh. I didn't notice at all.\"" id a02_cou2_01_9ca77037

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0388"
    rin "\"You've got focus. Just no endurance.\"" id a02_cou2_01_af0f7614

    show hina 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0545"
    hina "\"Mmh.\"" id a02_cou2_01_859a3b3e

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0389"
    rin "\"If you're taking a break, why don't you stretch? You've been hunched over the desk all this time.\"" id a02_cou2_01_f39815cf

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0546"
    hina "\"I guess so~\"" id a02_cou2_01_3639a3a9

    show hina 1 lg pyjama n with Dissolve(0.25)
    show hina:
        ShakeTameiki

    "Staying on her knees, Hina stretched her arms forward. Just like a cat."

    show hina 1 lg pyjama d:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "HIN_0547"
    hina "\"Ow ow ow. My back's cracking.\"" id a02_cou2_01_1cd7c7bd

    "She was trying to stretch, but wasn't accomplishing much other than a series of groans."

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0390"
    rin "\"You're less flexible than I thought you'd be, Hina.\"" id a02_cou2_01_13b6d734

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0548"
    hina "\"Huh? Isn't this normal?\"" id a02_cou2_01_e888e239

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0391"
    rin "\"I just thought you'd be softer, I guess.\"" id a02_cou2_01_6083379d

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_0549"
    hina "\"Well, you look like you'd be super stiff. Like an old lady.\"" id a02_cou2_01_34ee97f5

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0392"
    rin "\"I seem that way, don't I?\"" id a02_cou2_01_fa965f23

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_0550"
    hina "\"Yeah. I mean you never exercise or anything.\"" id a02_cou2_01_423b90f4

    show rin 1 lg pyjama glasses a with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "RIN_0393"
    rin "\"Good point.\"" id a02_cou2_01_17f746e0

    play sound se116a
    show rin:
        ycenter 1016 xoffset 0 yoffset 0
        easein 1.0 ycenter 1116

    "Rin spread her legs, bent forward, and beckoned Hina over."

    show rin 1 lg pyjama glasses a:
        ycenter 1116
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0394"
    rin "\"Come push my back?\"" id a02_cou2_01_19a40a5c

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0551"
    hina "\"Sure, but if it hurts, you should tell me right away.\"" id a02_cou2_01_2ddb6e3c

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0395"
    rin "\"Oui, oui.\"" id a02_cou2_01_2e05d79e

    show hina:
        "hina 2 lg pyjama d" with Dissolve(0.25)
        xcenter 772
        easein 1.0 xcenter 512
    pause 1.0

    show hina 2 lg pyjama d:
        xcenter 512
    with None

    show rin:
        "rin 2 lg pyjama glasses c flat"
        alpha 1.0 ycenter 1116
        easeout 1.0 alpha 0.0 ycenter 1216

    show hina:
        3.0
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0552"
    hina "\"Okay, here I go... Wait, huh? Huh?!\"" id a02_cou2_01_c3f753d2

    hide rin with None
    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None

    "Hina touched Rin's back and Rin went flat against the floor without her even having to exert any force."

    $ side_image = "rin 1 side pyjama glasses f"

    voice "RIN_0396"
    rin "\"Well? Surprised? Surprised?\"" id a02_cou2_01_d626a967

    "Rin was smug, her cheek against the carpet."

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0553"
    hina "\"A-Are you okay? You didn't lose an important screw or something?\"" id a02_cou2_01_2b971dd7

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses i"

    voice "RIN_0397"
    rin "\"What's that supposed to mean?\"" id a02_cou2_01_0990f2f9

    voice "HIN_0554"
    hina "\"Why? How?! What's the trick?\"" id a02_cou2_01_0a0909a0

    "Hina patted Rin as if looking for a mechanism."

    $ side_image = "rin 1 side pyjama glasses a"

    voice "RIN_0398"
    rin "\"There's no trick, but I did ballet right up until middle school. I never mentioned it?\"" id a02_cou2_01_443cc349

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0555"
    hina "\"First I've heard of it.\"" id a02_cou2_01_e1b1215d

    show hina 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0556"
    hina "\"That's so fancy. You're not like a rich girl, are you?\"" id a02_cou2_01_a21d0a47

    $ side_image = "rin 1 side pyjama glasses b"

    voice "RIN_0399"
    rin "\"I wouldn't say that, but we're reasonably well-off. My papa's a university professor, after all. And I'm an only child.\"" id a02_cou2_01_c37c9a70

    show hina:
        "hina 1 lg pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0557"
    hina "\"Asou plays the piano, Rin does ballet... Haahh, you guys are so classy.\"" id a02_cou2_01_ca82d72e

    show hina 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 2 side pyjama glasses a"

    voice "RIN_0400"
    rin "\"I mean, I don't do it anymore.\"" id a02_cou2_01_d385885c

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0558"
    hina "\"Why'd you quit?\"" id a02_cou2_01_130b87e6

    $ side_image = "rin 1 side pyjama glasses a"

    voice "RIN_0401"
    rin "\"'Cause I got huge as soon as I started middle school.\"" id a02_cou2_01_a0b62f9e

    play sound se116a

    show hina:
        "hina 1 lg pyjama k" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 772
    show rin:
        "rin 1 lg pyjama glasses b flat"
        alpha 0.0 xcenter 252 ycenter 1116
        easein 0.5 alpha 1.0 ycenter 1016

    pause 0.25

    "Rin stood up swiftly. True, she was tall."

    show hina 1 lg pyjama k:
        xcenter 772
    show rin 1 lg pyjama glasses b:
        alpha 1.0 xcenter 252 ycenter 1016
    with None
    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0559"
    hina "\"You were that tall in middle school?\"" id a02_cou2_01_e6a2b08f

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0402"
    rin "\"Yeah, by eighth grade or so.\"" id a02_cou2_01_aa77ce62

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0560"
    hina "\"Huh... I'm the same height I was in eighth grade, too.\"" id a02_cou2_01_29197167

    show rin 2 lg pyjama glasses a with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0403"
    rin "\"Mmh~\"" id a02_cou2_01_b648c508

    show rin:
        xoffset 0 yoffset 0
    with None

    "She was stretching now, using the back of a chair in place of a barre."

    show hina 1 lg pyjama i with dict_dissolve_25

    voice "HIN_0561"
    hina "\"Don't make a mess in here with your hugeness.\"" id a02_cou2_01_b64d3643

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0404"
    rin "\"I won't jump or spin or anything. Just hold some poses.\"" id a02_cou2_01_fa7eb504

    show rin 2 lg pyjama glasses a with Dissolve(0.25)
    show rin:
        ShakeJump2

    "Rin said, slowly raising her arms. A deep breath, and strength thrummed through them, all the way to her fingertips."

    show rin:
        xoffset 0 yoffset 0
    with None

    "There was a moment where it seemed like she'd reach the ceiling."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0562"
    hina "\"...Your arms are so long.\"" id a02_cou2_01_778d4571

    "Her fingers were beautiful and shapely as well."

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0405"
    rin "\"Mmh, this is pretty hard on the tendons.\"" id a02_cou2_01_c1479713

    "Rin then gradually went through different positions with her legs."

    "She put her heels together and spread her knees apart, then moved her heels apart, then put one slightly in front of the other."

    show rin 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0406"
    rin "\"Huh, your body just remembers this stuff. These are called positions and there's a set way to do all of them.\"" id a02_cou2_01_313d938b

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0563"
    hina "\"That's super ballet.\"" id a02_cou2_01_8be6c880

    show rin 2 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0407"
    rin "\"I'll try the knees next. You take your toes and put them to the ankle of your pivot leg... then up to the calf, and the knee...\"" id a02_cou2_01_dad1c8fa

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0564"
    hina "\"Ooh, that's really ballet, too... Huh?\"" id a02_cou2_01_09f93e6b

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0408"
    rin "\"What is it?\"" id a02_cou2_01_cfceac2b

    voice "HIN_0565"
    hina "\"Can you do that one again?\"" id a02_cou2_01_4346009b

    show rin 2 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0409"
    rin "\"Hm? This?\"" id a02_cou2_01_714ada77

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0566"
    hina "\"I knew it! You're doing all this stuff with your legs so I didn't notice, but your top half's not moving at all!\"" id a02_cou2_01_8d5d2137

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0410"
    rin "\"Huh? Oh, yeah... I guess so.\"" id a02_cou2_01_87b93bb1

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0567"
    hina "\"That's amazing, Rin! You're like a ballerina!\"" id a02_cou2_01_cd36cdc3

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0411"
    rin "\"Ahaha, a former one. But I don't mind the compliment, so I'll give you something extra. Mh, let's see if I can still get my leg up...\"" id a02_cou2_01_3b63c5a2

    hide rin with Dissolve(0.25)

    "Rin let her padded kimono drop to the floor."

    $ side_image = "rin 1 side pyjama glasses h"

    voice "RIN_0412"
    rin "\"...Here goes nothing.\"" id a02_cou2_01_90dbad5a

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0568"
    hina "\"Huh? What are you—\"" id a02_cou2_01_13cc768b

    stop music fadeout 1.0

    scene white with Dissolve(0.375)
    pause 1.125

    play sound se_bati

    show bati2 at truecenter

    pause 0.62

    scene ev05a with Dissolve(0.5)
    pause 1.5

    play music bgm03

    "Rin threw her chest out and grabbed her toes with both hands, her long hair bouncing with the action."

    voice "HIN_0569"
    hina "\"Ah...\"" id a02_cou2_01_47c00624

    voice "RIN_0413"
    rin "\"Hey, looks like I made it.\"" id a02_cou2_01_37586c18

    "Her limbs formed an elegant ring."

    "The light from the window framed her face... a rather handsome one."

    voice "HIN_0570"
    hina "\"......\"" id a02_cou2_01_e5d5c54d

    voice "RIN_0414"
    rin "\"Are you surprised?\"" id a02_cou2_01_b08abff7

    "Hina nodded, speechless."

    voice "HIN_0571"
    hina "\"...Wow.\"" id a02_cou2_01_07f29831

    voice "RIN_0415"
    rin "\"Please keep your hands off of the dancer~\"" id a02_cou2_01_cbb0198b

    "Rin quipped as usual, much more comfortable in the position than expected."

    voice "HIN_0572"
    hina "\"Your arms and legs... are so long.\"" id a02_cou2_01_a83f3728

    voice "RIN_0416"
    rin "\"Well, I {i}am{/i} huge.\"" id a02_cou2_01_ed3fab05

    voice "HIN_0573"
    hina "\"I don't really know anything about ballet, but... it's pretty. You're like, sparkling.\"" id a02_cou2_01_d2e339e3

    voice "RIN_0417"
    rin "\"Oh, no pictures either, please.\"" id a02_cou2_01_0bb292bd

    voice "HIN_0574"
    hina "\"I didn't even think about taking one... I just want to keep looking forever.\"" id a02_cou2_01_e402405c

    voice "RIN_0418"
    rin "\"Eheh. Well, I definitely can't keep this up forever.\"" id a02_cou2_01_9f54173a

    voice "HIN_0575"
    hina "\"...I didn't know you were so pretty.\"" id a02_cou2_01_e4477280

    voice "RIN_0419"
    rin "\"Hm? What, are you trying to catch flies over there? Wait, lemme guess, you fell for me.\"" id a02_cou2_01_dd54d080

    voice "HIN_0576"
    hina "\"D-Don't be stupid!\"" id a02_cou2_01_3e2b799a

    "Hina swung at her."

    voice "RIN_0420"
    rin "\"Wh-Whoa... h-hey! I'm gonna lose my—\"" id a02_cou2_01_75a48616

    voice "HIN_0577"
    hina "\"Huh? Huh?\"" id a02_cou2_01_cbf5995d

    scene black with bg_effect_13_100
    pause 0.1

    scene bg01aa with bg_effect_13_100
    pause 0.1

    play sound se113c

    camera:
        function LayerShake(30,30,0.5)
    $ persistent.layer_shaken = False

    "Rin lost her balance and fell on top of Hina."

    camera
    with None

    $ side_image = "rin 1 side pyjama glasses g"

    voice "RIN_0421"
    rin "\"Ouch... It's hard to jump right in after a few years. I didn't have shoes or anything either.\"" id a02_cou2_01_99b750cc

    $ side_image = "hina 1 side pyjama l"

    voice "HIN_0578"
    hina "\"Wh-Whatever, just get off me.\"" id a02_cou2_01_45ed5963

    $ side_image = "rin 1 side pyjama glasses f"

    stop music fadeout 1.0

    voice "RIN_0422"
    rin "\"Heh, heh, heh.\"" id a02_cou2_01_1bbfa7d3

    $ side_image = "hina 1 side pyjama d"

    voice "HIN_0579"
    hina "\"Wh-What?\"" id a02_cou2_01_0c30c9da

    play music bgm04

    $ side_image = "rin 1 side pyjama glasses d"

    voice "RIN_0423"
    rin "\"Oh, two young people in this position together, there's only one thing to do, isn't there?!\"" id a02_cou2_01_6da05c41

    $ side_image = "hina 1 side pyjama l"

    voice "HIN_0580"
    hina "\"Waaah, n-not this again!\"" id a02_cou2_01_9b815a35

    $ side_image = "rin 1 side pyjama glasses c"

    voice "RIN_0424"
    rin "\"Heheh, it's no use resisting. Not against my hugeness~\"" id a02_cou2_01_f2fd1470

    $ side_image = "hina 1 side pyjama d"

    voice "HIN_0581"
    hina "\"I-I guess not...\"" id a02_cou2_01_1a3c82fb

    "Hina muttered, eyeing the hands pinning her shoulders down."

    $ side_image = "hina 1 side pyjama d"

    voice "HIN_0582"
    hina "\"Wh-What are you gonna do to me?\"" id a02_cou2_01_d5389d7c

    $ side_image = "rin 1 side pyjama glasses f"

    voice "RIN_0425"
    rin "\"Well, this and that. I'll get my fill of your immature body.\"" id a02_cou2_01_e02e72e5

    "Rin wriggled her fingers lewdly."

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0583"
    hina "\"......\"" id a02_cou2_01_b3523b46

    $ side_image = "rin 1 side pyjama glasses e"

    voice "RIN_0426"
    rin "\"Huh? Where'd your fight go?\"" id a02_cou2_01_c8670ff5

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0584"
    hina "\"You said it was no use resisting...\"" id a02_cou2_01_ae871cba

    $ side_image = "rin 1 side pyjama glasses i"

    voice "RIN_0427"
    rin "\"Well, yeah, that's just what you say. It's no fun if you don't fight back, though.\"" id a02_cou2_01_0e33da9a

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0585"
    hina "\"Is it any fun touching me, Rin? I'm like a kid compared to you.\"" id a02_cou2_01_e4ec3e88

    $ side_image = "rin 1 side pyjama glasses g"

    voice "RIN_0428"
    rin "\"Well, sure, there's, you know, a genre you fit into.\"" id a02_cou2_01_e107b762

    "A genre..."

    $ side_image = "hina 1 side pyjama k"

    voice "HIN_0586"
    hina "\"Really...?\"" id a02_cou2_01_97555991

    $ side_image = "rin 1 side pyjama glasses h"

    voice "RIN_0429"
    rin "\"Hm? What's wrong? Are you upset about something?\"" id a02_cou2_01_a8ea8d72

    "Rin leaned in and peered at Hina's expression. Her face was reflected in Rin's glasses, and in her eyes behind them."

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0587"
    hina "\"Ngh!\"" id a02_cou2_01_43e038a6

    "Hina suddenly looked away."

    $ side_image = "rin 1 side pyjama glasses e"

    voice "RIN_0430"
    rin "\"Huh... what? Why are you blushing?\"" id a02_cou2_01_ba9dfd72

    $ side_image = "hina 2 side pyjama i"

    voice "HIN_0588"
    hina "\"...Kh!\"" id a02_cou2_01_224072ad

    $ side_image = "rin 1 side pyjama glasses e"

    voice "RIN_0431"
    rin "\"H-Hina...?\"" id a02_cou2_01_4dff79c0

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0589"
    hina "\"Y-Yes...?\"" id a02_cou2_01_392ec8a8

    $ side_image = "rin 1 side pyjama glasses g"

    voice "RIN_0432"
    rin "\"If you play the scene straight like this, I'm not really sure what to do...\"" id a02_cou2_01_0d6b1aa3

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0590"
    hina "\"W-Well...\"" id a02_cou2_01_da5c6397

    stop music fadeout 0.1
    play sound se521

    $ side_image = "fumi 1 side casual b"

    voice "FUM_0409"
    fumi "\"Hello, I'm home.\" " id a02_cou2_01_85046eb7

    $ voice2("hina","HIN_0591","rin","RIN_0433")
    hina_rin "\"?!\""

    play music bgm01

    $ side_image = "fumi 2 side casual d"

    voice "FUM_0410"
    fumi "\"Oh my.\"" id a02_cou2_01_2243a250

    "The two of them met eyes with Fumi, who stood in the door."

    $ side_image = "hina 1 side pyjama d"

    voice "HIN_0592"
    hina "\"U-Umm... we're just...!\"" id a02_cou2_01_d85167a7

    $ side_image = "fumi 2 side casual c"

    voice "FUM_0411"
    fumi "\"Fooling around again? You two sure get along.\"" id a02_cou2_01_00375161

    "Fumi started putting food in the refrigerator, completely unfazed by the sight of the two girls in a pile on the floor."

    show hina 1 sm pyjama k at pos_r
    show rin 1 sm pyjama glasses g at pos_l
    with Dissolve(0.25)

    $ voice2("hina","HIN_0593","rin","RIN_0434")
    hina_rin "\"Umm... yeah.\""

    "Rin and Hina glanced at each other and hastily pulled apart."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
