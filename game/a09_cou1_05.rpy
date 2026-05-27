label a09_cou1_05:

    scene bg01cg with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show fumi 1 lg pyjama a at pos_l
    show hina 1 lg pyjama_pjm a at pos_r
    with dict_dissolve_25

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_0906"
    rin "\"What? You've got sub duty again next Sunday? I'm impressed you've got the energy.\"" id a09_cou1_05_f2378c55

    show hina:
        "hina 1 lg pyjama_pjm c" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0916"
    hina "\"Of course I do. If I were actually on a team, I'd be doing this every day, you know.\"" id a09_cou1_05_11d010eb

    show hina 1 lg pyjama_pjm c:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "2FU_0759"
    fumi "\"I think it's more impressive that you're able to make a difference without practicing every day.\"" id a09_cou1_05_183b4d5f

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0917"
    hina "\"Thanks. But the team really belongs to the people who do practice. That's why I'm just a sub.\"" id a09_cou1_05_907711ed

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0760"
    fumi "\"Right...\"" id a09_cou1_05_d10f6426

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_0848"
    miyako "\"So what sport is it this time?\"" id a09_cou1_05_c60c1ab6

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0918"
    hina "\"Volleyball.\"" id a09_cou1_05_3fe0a4de

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_0907"
    rin "\"Now that's the real myste—\"" id a09_cou1_05_40280d4d

    play sound se_lime

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0761"
    fumi "\"Oh, that's me.\"" id a09_cou1_05_c7c01f82

    hide fumi with dict_dissolve_25

    "A message appeared on Fumi's LIME, and she picked her phone up from where it was charging."

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0919"
    hina "\"What's the mystery?\"" id a09_cou1_05_4b0569ee

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0908"
    rin "\"Why do they call you to sub in when volleyball is like the posterchild for tall-people sports? I'm not picking on you, by the way. This is genuine curiosity.\"" id a09_cou1_05_8b5cd7ab

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0920"
    hina "\"Ah, that's 'cause I play as a libero.\"" id a09_cou1_05_f46f752b

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_0909"
    rin "\"Libero?\"" id a09_cou1_05_10fcbafc

    show hina:
        ShakeYes

    voice "2HI_0921"
    hina "\"Yeah. Basically, I only do defense. I can receive, but not spike or block, so height doesn't really come into play.\"" id a09_cou1_05_a74a0857

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0910"
    rin "\"I see. Never heard of those rules before.\"" id a09_cou1_05_1b74985a

    "Rin knows a lot of trivia, but I guess she's not very interested in sports."

    show fumi 2 lg pyjama h at pos_l with dict_dissolve_25

    voice "2FU_0762"
    fumi "\"...Umm, sorry...\"" id a09_cou1_05_124808ba

    "Fumi timidly interrupted, phone in hand."

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0922"
    hina "\"What's up? The LIME?\"" id a09_cou1_05_a6c97b09

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0763"
    fumi "\"Yes. My mother's asking for a favor.\"" id a09_cou1_05_ffce5761

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0911"
    rin "\"What is it?\"" id a09_cou1_05_17aeaea3

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0764"
    fumi "\"It seems our store was featured in a local magazine recently, and we've been getting a ton of customers because of that.\"" id a09_cou1_05_68d59ab8

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0923"
    hina "\"That's great!\"" id a09_cou1_05_060dd2da

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0765"
    fumi "\"Yes. It's good news, but...\"" id a09_cou1_05_f9c4cd9c

    show hina 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0924"
    hina "\"But?\"" id a09_cou1_05_905199f1

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0766"
    fumi "\"It's getting hard for my mother to handle all the customers on her own. Weekdays are still somewhat manageable, but it might be hard on the weekends even with me helping out.\"" id a09_cou1_05_c5b7fe1e

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_0912"
    rin "\"That's on top of it being Valentine's season.\"" id a09_cou1_05_da0a3b25

    show fumi:
        ShakeYes

    "Fumi nodded."

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi's mother was typically the only one serving customers at Le Chocolat Chocolat. Fumi only joined her on weekends."

    "On the production side, it was possible to prepare more in advance, but that wasn't so with the customer service side."

    show fumi 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0767"
    fumi "\"They're hiring part-timers, of course, but that doesn't solve the immediate problem.\"" id a09_cou1_05_5a4fc73d

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0925"
    hina "\"Oh, is that the favor? Working part-time?\"" id a09_cou1_05_6a449537

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0768"
    fumi "\"Yes, that's right. She wanted me to ask my friends if anyone could take a shift on Sunday. For pay, of course.\"" id a09_cou1_05_d749cbf4

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0913"
    rin "\"Hey, Mikoyan, you interested in—\"" id a09_cou1_05_d12b6864

    $ side_image = "miyako 2 side pyjama i"

    voice "2MI_0849"
    miyako "\"Zzz, zzz.\"" id a09_cou1_05_cbd27995

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0914"
    rin "\"...Well, you know what they say about letting sleeping lions lie.\"" id a09_cou1_05_a94fa88a

    "In Miyako's defense, I'll mention that she fell asleep before all the talk of the bakery. Like, right after she asked Hina \"what sport?\""

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0915"
    rin "\"I don't really have any confidence in my stamina or my customer service skills, so I dunno...\"" id a09_cou1_05_f55e9d6e

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0769"
    fumi "\"Oh, there's no need to force yourself. I don't think she really expected much when she asked. I'll tell her no.\"" id a09_cou1_05_39d37a82

    "Fumi unlocked her phone to send a reply."

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0926"
    hina "\"Why? I'll help out.\"" id a09_cou1_05_5dda2fc0

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "2FU_0770"
    fumi "\"Huh? But you're playing volleyball on Sunday.\"" id a09_cou1_05_74914be0

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0927"
    hina "\"I'll just turn them down. Helping you is more important.\"" id a09_cou1_05_fc5dd885

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0771"
    fumi "\"Well, I'm thankful for that, but won't it inconvenience the team? You already said yes to them...\"" id a09_cou1_05_e08e379e

    show hina 1 lg pyjama_pjm m with dict_dissolve_25

    voice "2HI_0928"
    hina "\"I'll go apologize tomorrow. But I was thinking I'd have to say no one of these days. I've told the captain and manager that before.\"" id a09_cou1_05_2ee085be

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0929"
    hina "\"They should have the people practicing every day with the team play in the games, not me.\"" id a09_cou1_05_22687485

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0772"
    fumi "\"......\"" id a09_cou1_05_161e2a9f

    show hina 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0930"
    hina "\"So, tell your mom I'll take the shift.\"" id a09_cou1_05_e578926a

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0773"
    fumi "\"Thanks, Hina. That'll really help.\"" id a09_cou1_05_dbba06a1

    $ side_image = "rin 1 side pyjama glasses f"

    voice "2RI_0916"
    rin "\"Hopefully height's not a factor for the job.\"" id a09_cou1_05_9f7f769e

    show hina 1 lg pyjama_pjm g with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "2HI_0931"
    hina "\"Shut up!\"" id a09_cou1_05_71e7c6cc

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared < 2:
        jump a09_comn_10
    else:
        jump a09_comn_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
