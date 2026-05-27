label a11_cou4_10:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_10:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene black with Dissolve(0.25)
    pause 0.75

    play sound howling
    pause 5.0

    $ side_image = "miyako 1 side school_a f"

    voice "2MI_1162"
    miyako "\"Aah!\"" id a11_cou4_10_fa02f433

    "The speaker suddenly screeched."

    "Miyako curled up and clutched her ears at the sound that almost seemed to shake the room."

    "But the piercing howl gradually softened into something bearable."

    "When the noise finally cleared..."

    voice "2NO_0006"
    noel "\"Merry Christmas!\"" (show_name="Voice") id a11_cou4_10_32c6a31a

    "...it became a voice."

    $ side_image = "miyako 1 side school_a f"

    voice "2MI_1163"
    miyako "\"Huh?!\"" id a11_cou4_10_ba6f945a

    "Miyako looked up at the half-a-month-late declaration."

    "And she found..."

    scene white with Dissolve(0.25)
    pause 1.75

    scene bg10ba_50 with Dissolve(0.5)
    pause 1.5

    show noel:
        "noel 1 lg school_a nb flat"
        alpha 0.0 xcenter 512
        linear 0.5 alpha 0.859375

    pause 1.0

    show noel:
        "noel 1 lg school_a nb flat"
        alpha 0.859375 xcenter 512
        2.2
        "noel 1 lg school_a no flat" with Dissolve(0.25)
        0.25
        ShakeSide

    voice "2NO_0007"
    noel "\"Not that I've got a tree or a cake... And it's cold!\"" (show_name="Girl") id a11_cou4_10_0225f5f3

    show expression "noel 1 lg school_a no flat" as noel:
        alpha 0.859375 xcenter 512 xoffset 0 yoffset 0
    with None

    "Miyako gasped."

    "Because the person she saw clutching her arms and shivering in the cold was {i}herself{/i}."

    play music bgm08 fadein 1.0

    $ side_image = "miyako 1 side school_a g"

    voice "2MI_1164"
    miyako "\"Is this... me?\"" id a11_cou4_10_108fc54e

    play sound se116a

    show noel:

        "noel 1 lg school_a no flat"
        "noel 1 lg school_scarf_a nc flat" with Dissolve(0.25)
        alpha 0.859375 xcenter 512 ycenter 1021
        ShakeYes

    "The \"vision\" looked around and found a scarf, wrapping it around her neck. It was the same scarf Miyako had with her."

    show expression "noel 1 lg school_scarf_a nc flat" as noel:
        xoffset 0 yoffset 0
    with None

    $ side_image = "miyako 2 side school b"

    voice "2MI_1165"
    miyako "\"Wh-What is this...?\"" id a11_cou4_10_04251645

    "She asked the figure, but the other her didn't even spare her a glance."

    show expression "noel 1 lg school_scarf_a nd flat" as noel with dict_dissolve_25

    voice "2NO_0008"
    if persistent.dpatch:
        noel "\"Probably shouldn't smoke inside the school, huh...\"" id a11_cou4_10_b60c3d4e (show_name="Miyako?")
    else:
        noel "\"Probably shouldn't smoke on campus grounds, huh...\"" (show_name="Miyako?") id a11_cou4_10_22615cc7

    $ side_image = "miyako 1 side school_b g"

    voice "2MI_1166"
    miyako "\"Smoke?\"" id a11_cou4_10_5f361d03

    "She asked, but got no answer."

    $ side_image = "miyako 2 side school a"

    voice "2MI_1167"
    miyako "\"Is she talking to herself? Can she not see me?\"" id a11_cou4_10_699b9adf

    show noel:
        "noel 1 lg school_scarf_a nd flat"
        "noel 1 lg school_scarf_cigarette nh flat" with Dissolve(0.25)
        ShakeYes

    voice "2NO_0009"
    noel "\"Oh well. It'll probably be my last one anyway.\"" (show_name="Miyako?") id a11_cou4_10_0304ef81

    show expression "noel 1 lg school_scarf_cigarette nh flat" as noel:
        xoffset 0 yoffset 0
    with None

    "She took a cigarette out of a box with well-practiced motions and put it in her mouth."

    play sound se_tabaco
    pause 1.0

    show expression "noel 1 lg school_scarf_cigarette ni flat" as noel with dict_dissolve_25

    voice "2NO_0010"
    noel "\"I feel like the little match girl. Just with a lighter. Oh wait, that's on New Year's, isn't it?\"" (show_name="Miyako?") id a11_cou4_10_78d9e859

    "The smoke curled upwards."

    $ side_image = "miyako 1 side school_b e"

    voice "2MI_1168"
    miyako "\"No... It's... not me...?\"" id a11_cou4_10_29dc8f59

    "Miyako had never smoked a cigarette."

    $ side_image = "miyako 2 side school f"

    voice "2MI_1169"
    miyako "\"H-Hello...? Huh? What?\"" id a11_cou4_10_19f994e3

    "Miyako timidly reached out to the girl's shoulder, but her hand went right through it."

    "She tried again, but couldn't make contact."

    $ side_image = "miyako 2 side school b"

    voice "2MI_1170"
    miyako "\"Huh...?\"" id a11_cou4_10_db179795

    hide noel with dict_dissolve_50

    "And as if to underline her confusion, this time, the illusion passed through Miyako."

    "The lit cigarette grazed her cheek, but it didn't feel like anything."

    play sound se_curtain

    "The illusion went over to the window and opened the curtains, running a hand over the condensation-fogged glass."

    show noel:
        "noel 1 sm school_scarf_cigarette ne flat"
        alpha 0.0 xcenter 512
        linear 0.25 alpha 0.859375

    voice "2NO_0011"
    noel "\"Ooh. I thought it was cold. 20XX is gonna be a white Christmas, huh~?\"" (show_name="Girl") id a11_cou4_10_2d9f5b40

    show noel 1 sm school_scarf_cigarette ne flat as noel:
        alpha 0.859375 xcenter 512
    with None

    "The illusion said cheerily, but the real curtains hadn't budged."

    $ side_image = "miyako 1 side school_b e"

    voice "2MI_1171"
    miyako "\"20XX? This is the past I'm seeing? Then...\"" id a11_cou4_10_c8e3f2f6

    "Miyako glanced around. She was looking for a Device."

    hide noel with dict_dissolve_50

    $ side_image = "miyako 1 side school_a i"

    voice "2MI_1172"
    miyako "\"Only a Device could cause this... It'd have to be a pretty powerful one, too...\"" id a11_cou4_10_80436d87

    "Her eyes landed on the transceiver first."

    "Nope. That one can pretty much only function as intended. It just connects with somewhere \"a little far away.\""

    $ side_image = "miyako 1 side school_a e"

    voice "2MI_1173"
    miyako "\"Ah...\"" id a11_cou4_10_83fadd4a

    "She looked around the room and then realized."

    $ side_image = "miyako 2 side school a"

    voice "2MI_1174"
    miyako "\"The whole broadcasting room is a Device!\"" id a11_cou4_10_05649814

    "—Exactly."

    $ side_image = "miyako 2 side school c"

    voice "2MI_1175"
    miyako "\"You're Noel. And I'm seeing...\"" id a11_cou4_10_22acb3ec

    "Miyako watched Noel nostalgically and listened to her voice."

    show noel:
        "noel 1 sm school_scarf_cigarette nh flat"
        alpha 0.0 xcenter 512
        linear 0.25 alpha 0.859375

    voice "2NO_0012"
    noel "\"Yeesh. It really took you long enough. Talk about last-minute.\"" id a11_cou4_10_eb38e686

    show noel 1 sm school_scarf_cigarette nh flat as noel:
        alpha 0.859375 xcenter 512
    with None

    "While Miyako was catching on to the situation, the illusion was muttering to herself, alternately breathing out smoke and sighs."

    voice "2SA_1065"
    sachiko "\"M... Mmh...\"" (show_name="???") id a11_cou4_10_5e9becc5

    show noel 1 sm school_scarf_cigarette nc flat as noel with dict_dissolve_25

    voice "2NO_0013"
    noel "\"Hm? You awake?\"" id a11_cou4_10_f80b5fff

    $ side_image = "miyako 2 side school a"

    voice "2MI_1176"
    miyako "\"Huh? There's someone else?\"" id a11_cou4_10_d11b5ee4

    hide noel with dict_dissolve_50

    "She turned around at the voice and closed the curtains. As she walked back, she picked up a blanket thrown over a chair."

    show noel:
        "noel 1 lg school_scarf_cigarette na flat"
        alpha 0.0 xcenter 512
        linear 0.25 alpha 0.859375

    voice "2NO_0014"
    noel "\"......\"" id a11_cou4_10_318fe024

    "Then she leaned down and peered under the desk. Miyako crouched down as well."

    show noel 1 lg school_scarf_cigarette na flat as noel:
        alpha 0.859375 xcenter 512
    with None
    show noel 1 lg school_scarf_cigarette nb flat as noel with dict_dissolve_25

    voice "2MI_1177"
    miyako "\"...They're not awake.\"" id a11_cou4_10_de5e0f2f

    "Someone was lying on the floor there, curled up under a thin blanket."

    show noel 1 lg school_scarf_cigarette nh flat as noel with dict_dissolve_25

    voice "2NO_0015"
    noel "\"I knew it. You {i}are{/i} cold. And last night you were like, 'I like it!'\"" id a11_cou4_10_1bfe5864

    play sound se_2s_g004

    show noel 1 lg school_scarf_cigarette nh flat as noel:
        ShakeYes

    "She covered the figure with the other blanket while she complained."

    show noel 1 lg school_scarf_cigarette nk flat as noel:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2NO_0016"
    noel "\"Don't blame me if you catch a cold. You're not an angel anymore, right?\"" id a11_cou4_10_412e88ab

    $ side_image = "miyako 1 side school_a f"

    voice "2MI_1178"
    miyako "\"It's Sachiko!\"" id a11_cou4_10_45e15213

    "Miyako exclaimed at the identity of the figure under the desk."

    play sound se_2s_h012

    "Noel pulled out the folding chair and sat backwards on it. She put her elbows on the back of the chair and looked down at Sachiko."

    show noel 1 lg school_scarf_cigarette nn flat as noel with dict_dissolve_25

    voice "2NO_0017"
    noel "\"You coward.\"" id a11_cou4_10_d2bcffc1

    voice "2MI_1179"
    miyako "\"Huh...?\"" id a11_cou4_10_5d2689d5

    voice "2NO_0018"
    noel "\"All you do is sulk and act like nothing affects you.\"" id a11_cou4_10_2c991e1d

    voice "2NO_0019"
    noel "\"I know you're really lonely. You're just afraid to come clean, right?\"" id a11_cou4_10_a236f8a4

    show noel 1 lg school_scarf_cigarette nh flat as noel with dict_dissolve_25

    voice "2NO_0020"
    noel "\"You say you're an angel, but there's nothing more human.\"" id a11_cou4_10_393bd3f9

    "You can say whatever you want when you know the person you're talking to is asleep."

    $ side_image = "miyako 2 side school b"

    voice "2MI_1180"
    miyako "\"Wait, this feels like...\"" id a11_cou4_10_5506f828

    "Miyako noticed something familiar."

    "Yep. When you complain about someone like this, you're usually hiding something else beneath it."

    $ side_image = "miyako 2 side school d"

    voice "2MI_1181"
    miyako "\"I see... Things are completely different between us and between them...\"" id a11_cou4_10_1ff583a3

    "Watching the illusion of the warmly smiling Noel and Sachiko, Miyako suddenly noticed the calendar behind Noel."

    $ side_image = "miyako 2 side school a"

    voice "2MI_1182"
    miyako "\"Wait, if this is Christmas, then Noel—\"" id a11_cou4_10_8957cbc9

    show noel 2 lg school_scarf cigarette nc flat as noel with Dissolve(0.25)
    show noel 2 lg school_scarf cigarette nc flat as noel:
        ShakeTameiki

    voice "2NO_0021"
    noel "\"Phew...\"" id a11_cou4_10_59727733

    show noel 2 lg school_scarf cigarette nc flat as noel:
        xoffset 0 yoffset 0
    with None

    "She sighed, looking tired."

    "Tapping the ash off in an empty can on the desk, she looked down at Sachiko's face as the latter rolled over in her sleep."

    show noel 1 lg school_scarf_cigarette nm flat as noel with dict_dissolve_25

    voice "2NO_0022"
    noel "\"I get why everybody goes crazy over that now.\"" id a11_cou4_10_ecf0c3fe

    "She brushed her fingers over her body, an entranced look on her face."

    show noel:
        "noel 1 lg school_scarf_cigarette nm flat"
        "noel 1 lg school_scarf_cigarette nl flat" with Dissolve(0.25)
        3.0
        "noel 1 lg school_scarf_cigarette nf flat" with Dissolve(0.25)

    voice "2NO_0023"
    noel "\"...It was really incredible. I almost died, though.\"" id a11_cou4_10_6d449261

    show noel 1 lg school_scarf_cigarette nf flat as noel:
        pass
    with None
    $ side_image = "miyako 2 side school b"

    voice "2MI_1183"
    miyako "\"Oh... huh.\"" id a11_cou4_10_be30b3f2

    "Miyako caught on to what had happened the night before."

    show noel 1 lg school_scarf_cigarette nb flat as noel with dict_dissolve_25

    voice "2NO_0024"
    noel "\"You were a little too focused on how you should be touching me, though.\"" id a11_cou4_10_0945bda7

    show noel 1 lg school_scarf_cigarette nn flat as noel with dict_dissolve_25

    voice "2NO_0025"
    noel "\"Well, I'm glad I had the experience. Can't say I really have any regrets now. The problem is...\"" id a11_cou4_10_c7d3539c

    show noel 1 lg school_scarf_cigarette na flat as noel with dict_dissolve_25

    voice "2NO_0026"
    noel "\"I'm sure you'll take all the wrong things with you from this...\"" id a11_cou4_10_2d7445c5

    $ side_image = "miyako 1 side school_a i"

    voice "2MI_1184"
    miyako "\"......\"" id a11_cou4_10_0584c3a8

    "Miyako was seeing that prediction come true in the present right now."

    show noel 2 lg school_scarf cigarette nb flat as noel with dict_dissolve_25

    voice "2NO_0027"
    noel "\"...Thank you for being with me. You gave me the strength to make it through the last six months. I'm not exaggerating. I really mean that.\"" id a11_cou4_10_86eadd2a

    show noel 1 lg school_scarf_cigarette nb flat as noel with dict_dissolve_25

    voice "2NO_0028"
    noel "\"I want you to enjoy the surface, your life, for your own sake now. Enough for me, too.\"" id a11_cou4_10_c8cc1c65

    show noel 1 lg school_scarf_cigarette nj flat as noel with dict_dissolve_25

    voice "2NO_0029"
    noel "\"Love takes up such a huge capacity, our stupid little heads get full with it right away. Every time you fall in love with someone, your old memories will get overwritten with new ones.\"" id a11_cou4_10_6b779bdb

    show noel 1 lg school_scarf_cigarette ni flat as noel with dict_dissolve_25

    voice "2NO_0030"
    noel "\"I want you to completely paint over me with a new love!\"" id a11_cou4_10_d4255f92

    show noel 1 lg school_scarf_cigarette nl flat as noel with dict_dissolve_25

    voice "2NO_0031"
    noel "\"That's my last wish. So, God, or an angel, or whatever, please grant it for me.\"" id a11_cou4_10_b406c03f

    show noel 1 lg school_scarf_cigarette nl flat as noel with dict_dissolve_25

    voice "2NO_0032"
    noel "\"Please let her love someone else someday. Please let someone else love her someday...\"" id a11_cou4_10_3fc35fe3

    show noel:
        "noel 1 lg school_scarf_cigarette nl flat"
        "noel 1 lg school_scarf_cigarette nk flat" with Dissolve(0.25)
        ShakeYes
        0.3
        ShakeYes

    voice "2NO_0033"
    noel "\"Koff! Koff!\"" id a11_cou4_10_a5f98f20

    show noel 1 lg school_scarf_cigarette nk flat as noel:
        xoffset 0 yoffset 0
    with None

    "A sudden coughing fit racked her. This wasn't just choking on cigarette smoke."

    show noel 1 lg school_scarf_cigarette nm flat as noel with dict_dissolve_25

    voice "2NO_0034"
    noel "\"Aww~ I wonder if I can become an angel when I die... Then I could watch over her forever.\"" id a11_cou4_10_0b4d3fcf

    $ side_image = "miyako 2 side school d"

    voice "2MI_1185"
    miyako "\"...Noel.\"" id a11_cou4_10_77757237

    voice "2SA_1066"
    sachiko "\"Mm... mmn?\"" (show_name="Voice") id a11_cou4_10_9170036b

    show noel 1 lg school_scarf_cigarette ng flat as noel with dict_dissolve_25

    voice "2NO_0035"
    noel "\"Oh, sorry, did I wake you up? What are you looking around for? You're in the broadcasting room. Were you dreaming?\"" id a11_cou4_10_909989e8

    window hide
    show white:
        alpha 1.0 additive 1.0
        linear 0.3 alpha 0.0
        repeat 2
    pause 0.6
    window auto
    pause 0.5

    scene white with Dissolve(0.125)
    pause 1.375

    scene black with Dissolve(0.375)
    pause 1.625

    "The vision ended there, the Device going silent."

    pause 0.5

    scene bg10bb with Dissolve(0.5)
    pause 1.5

    show miyako 1 lg school_a i with Dissolve(0.5)
    pause 0.5

    voice "2MI_1186"
    miyako "\"...Noel didn't blame her for anything.\"" id a11_cou4_10_182b3d1b

    "Miyako raised her head."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
