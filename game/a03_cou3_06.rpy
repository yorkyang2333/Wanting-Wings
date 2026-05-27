label a03_cou3_06:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 1 lg school b at pos_r
    show fumi 1 lg school a at pos_l
    with Dissolve(0.25)

    voice "RIN_0841"
    rin "\"We're... alone.\"" id a03_cou3_06_2b76cc91

    show fumi:
        "fumi 1 lg school d" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0747"
    fumi "\"W-We are... Natsume's at her committee meeting...\"" id a03_cou3_06_5df4437a

    show fumi 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0842"
    rin "\"It's about Christmas mass, right?\"" id a03_cou3_06_107cfc5c

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0748"
    fumi "\"Yes. She said it might take a while...\"" id a03_cou3_06_16c3e03e

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0843"
    rin "\"Hmm...\"" id a03_cou3_06_375dc30f

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0749"
    fumi "\"......\"" id a03_cou3_06_a81946a6

    "After three false starts, Rin broke the silence between them."

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0844"
    rin "\"Is this a 'chance'... you think?\"" id a03_cou3_06_90fe29bd

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0750"
    fumi "\"You think?\"" id a03_cou3_06_d22f0459

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0845"
    rin "\"We got one sooner than I thought we would... huh?\"" id a03_cou3_06_ce828864

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0751"
    fumi "\"Aha... haha...\"" id a03_cou3_06_274e4814

    "The two smiled awkwardly at each other, their cheeks red in the light of the setting sun."

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0752"
    fumi "\"We might get interrupted again, though...\"" id a03_cou3_06_f51ce81a

    show rin:
        "rin 1 lg school h" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 662
    pause 0.25

    show rin 1 lg school h:
        xcenter 662
        ShakeYes

    voice "RIN_0846"
    rin "\"......\"" id a03_cou3_06_29ca4572

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin grabbed Fumi by the wrist."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0753"
    fumi "\"...Ah...\"" id a03_cou3_06_5346dea0

    "Fumi could tell what was coming next from Rin's solemn face."

    "......"

    voice "RIN_0847"
    rin "\"But if you don't want to—\"" id a03_cou3_06_303bf6d7

    "The short silence tempered Rin's courage."

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0754"
    fumi "\"I do... want to.\"" id a03_cou3_06_7c3b059a

    "She placed her hand over Rin's sweaty hand on her wrist."

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_0848"
    rin "\"Asou...\"" id a03_cou3_06_34131e86

    "She made no attempt to hide her relief."

    show rin:
        "rin 2 lg school g" with Dissolve(0.25)
        xcenter 662
        easein 3.0 xcenter 612

    "And Rin leaned in to Fumi, almost falling on her—"

    show rin 2 lg school g:
        xcenter 612
    with None
    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0755"
    fumi "\"Umm...\"" id a03_cou3_06_7fd11ba8

    show rin:
        "rin 1 lg school e" with Dissolve(0.25)
        xcenter 612
        easein 0.25 xcenter 662

    voice "RIN_0849"
    rin "\"Huh?\"" id a03_cou3_06_6047f974

    show rin 1 lg school e:
        xcenter 662
    with None
    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0756"
    fumi "\"Maybe we should lock the doors...\"" id a03_cou3_06_60d256ca

    "Fumi pointed out."

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0850"
    rin "\"Oh, right!\"" id a03_cou3_06_26df964b

    show rin:
        "rin 1 lg school g flat"
        alpha 1.0 xcenter 662 xoffset 0 yoffset 0
        easeout 0.5 alpha 0.0 xcenter 762

    "Rin scrambled to bolt the classroom doors."

    scene black with bg_effect_05
    pause 0.5

    play sound se561

    scene bg04ba with bg_effect_05
    pause 0.5

    show fumi 2 lg school h at pos_l
    show rin 1 lg school i at pos_r
    with Dissolve(0.25)

    voice "RIN_0851"
    rin "\"Okay...\"" id a03_cou3_06_2249696e

    "Rin placed a hand on Fumi's shoulder."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0757"
    fumi "\"We should close the curtains, too...\"" id a03_cou3_06_3ae22bbb

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0852"
    rin "\"Right... You're right.\"" id a03_cou3_06_c11d4605

    show rin:
        "rin 1 lg school j flat"
        alpha 1.0 xcenter 772 xoffset 0 yoffset 0
        easeout 0.5 alpha 0.0 xcenter 672

    "This time she jogged over to the windows."

    scene black with bg_effect_05
    pause 0.5

    play sound se524

    scene bg04bb with bg_effect_05
    pause 0.5

    show rin 1 lg school i at pos_r
    show fumi 1 lg school d at pos_l
    with Dissolve(0.25)

    voice "RIN_0853"
    rin "\"...Is that good, you think?\"" id a03_cou3_06_93400e6d

    "Rin pointed to each door, the hall-side windows, and the courtyard-side windows, then turned back to Fumi."

    show fumi 2 lg school h with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "FUM_0758"
    fumi "\"Yes.\"" id a03_cou3_06_233ddd06

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi nodded serenely."

    stop music fadeout 3.0

    show rin 2 lg school b with dict_dissolve_25

    voice "RIN_0854"
    rin "\"...Asou...\"" id a03_cou3_06_db460825

    show fumi 2 lg school j with dict_dissolve_25

    voice "FUM_0759"
    fumi "\"......\"" id a03_cou3_06_c2bb9438

    show rin:
        "rin 2 lg school b" with Dissolve(0.25)
        xcenter 772
        easein 3.0 xcenter 612

    "Rin gazed at Fumi, who looked down. Their lips grew closer once again—"

    show rin 2 lg school b:
        xcenter 612
    with None

    play sound se026a

    show fumi:
        "fumi 2 lg school d" with Dissolve(0.25)
    show rin behind fumi:
        "rin 1 lg school j" with Dissolve(0.25)
        xcenter 612
        easein 0.25 xcenter 772
    pause 0.25

    show rin 1 lg school j:
        xcenter 772
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_0855"
    rin "\"Daaah!!\"" id a03_cou3_06_bc27cc36

    hide rin with Dissolve(0.25)

    "Rin shouted in frustration and pulled her phone out of her pocket. The screen was displaying Sachiko's name."

    play music bgm01

    play sound se026c

    $ side_image = "rin 1 side school g"

    voice "RIN_0856"
    rin "\"Yes, what is it? I'm kind of busy at the moment.\"" id a03_cou3_06_75b585ea

    $ side_image = "rin 1 side school j"

    voice "RIN_0857"
    rin "\"What? Cigarettes?! ...I got it, fine, I'll buy them!\"" id a03_cou3_06_3ed8f546

    $ side_image = "rin 1 side school g"

    voice "RIN_0858"
    rin "\"Okay, I'm hanging up. ...A mood? Hell yes, I'm in a mood! I'm in the middle of something important!\"" id a03_cou3_06_593ff39d

    $ side_image = "rin 1 side school j"

    voice "RIN_0859"
    rin "\"What, you still want something? ...Huh?! What do you mean 'my rest'?!\"" id a03_cou3_06_fb7ab22f

    play sound se026c

    pause 1.0

    show rin 1 lg school j behind fumi at pos_r with Dissolve(0.25)

    voice "RIN_0860"
    rin "\"Geez!\"" id a03_cou3_06_51b0acd8

    "Rin turned her phone off and jammed it back into her pocket."

    stop music fadeout 3.0

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        xcenter 772
        easein 0.5 xcenter 612

    voice "RIN_0861"
    rin "\"O-Okay, this time...!\"" id a03_cou3_06_0e85754d

    show rin 1 lg school g:
        xcenter 612
    with None

    "She grabbed Fumi by the shoulders."

    play sound se_bati

    show bati2 at truecenter
    pause 0.3

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0760"
    fumi "\"......Pfft.\"" id a03_cou3_06_92b33520

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0862"
    rin "\"Huh? What?\"" id a03_cou3_06_52f042a5

    "Rin's eyes went wide when Fumi giggled."

    play music bgm02

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0761"
    fumi "\"I think this is the first time I've seen you lose your composure this much... eheheh.\"" id a03_cou3_06_876bf1ef

    voice "RIN_0863"
    rin "\"......\"" id a03_cou3_06_6aac9222

    "Rin merely stared at Fumi, dumbfounded."

    show fumi 1 lg school i with dict_dissolve_25

    voice "FUM_0762"
    fumi "\"I'm sorry... Are you mad?\"" id a03_cou3_06_573f6b13

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0864"
    rin "\"...Hahh...\"" id a03_cou3_06_47bb8870

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "She sighed and loosened her grip on Fumi's shoulders."

    show rin:
        "rin 2 lg school e" with Dissolve(0.25)
        xcenter 612
        easein 0.5 xcenter 772

    voice "RIN_0865"
    rin "\"I really lost my cool there, huh?\"" id a03_cou3_06_0468a31c

    "Rin took a step back from Fumi and sat down at the desk behind her, smiling wryly."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0866"
    rin "\"I really thought I'd be smoother about all this, but it just doesn't go how you plan it, huh?\"" id a03_cou3_06_e3267152

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0763"
    fumi "\"I think I'd be more nervous if you were used to this.\"" id a03_cou3_06_30219faf

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0867"
    rin "\"Yeah, but I really... Sorry. I'm being really uncool.\"" id a03_cou3_06_6240c650

    "Rin ran a hand through her hair embarrassedly."

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0764"
    fumi "\"I think it's cute.\"" id a03_cou3_06_b2fb0991

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0868"
    rin "\"...Cute?\"" id a03_cou3_06_b05fed78

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0765"
    fumi "\"Yeah. How you try so hard to be cool for me.\"" id a03_cou3_06_9166def6

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0869"
    rin "\"That obvious...?\"" id a03_cou3_06_6aa6b124

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0766"
    fumi "\"That's what makes it cute.\"" id a03_cou3_06_ad25f7b2

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0870"
    rin "\"Ugh... sorry, I'm really not used to hearing that.\"" id a03_cou3_06_938f9f5a

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "Rin looked down, covering her flushed face with her hands."

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0767"
    fumi "\"Haha. You'd better get used to it, because I'm going to say it a lot more from now on.\"" id a03_cou3_06_d30a4613

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0871"
    rin "\"...I'll try.\"" id a03_cou3_06_faff0d9d

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0768"
    fumi "\"......\"" id a03_cou3_06_953b4cb8

    show rin 2 lg school b with dict_dissolve_25

    voice "RIN_0872"
    rin "\"So, what should we do? Just give up for—\"" id a03_cou3_06_4273f2d2

    show fumi:
        "fumi 2 lg school j" with Dissolve(0.25)
        xcenter 252
        easein 1.0 xcenter 482
    pause 1.0

    show fumi 2 lg school j:
        xcenter 482
    with None

    show rin 2 lg school f with dict_dissolve_25

    "When Rin raised her face, their lips met."

    show rin 1 lg school e
    show fumi 2 lg school h
    with dict_dissolve_25

    voice "RIN_0873"
    rin "\"?!\"" id a03_cou3_06_be84f34a

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0769"
    fumi "\"Let's keep going.\"" id a03_cou3_06_b3be2c2c

    "Slowly pulling back, Fumi smiled tenderly."

    "The way the light of the setting sun shone through the curtains and outlined her companion was almost divine. Rin gasped."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0874"
    rin "\"...Okay.\"" id a03_cou3_06_380ad411

    "Rin nodded after a long pause. She drew closer to Fumi, as if possessed."

    show fumi 2 lg school j
    show rin 1 lg school k
    with dict_dissolve_25

    voice "FUM_0770"
    fumi "\"...Nnh.\"" id a03_cou3_06_0a495d65

    "This time Rin initiated the kiss."

    voice "RIN_0875"
    rin "\"Mm... chp...\"" id a03_cou3_06_652681fc

    voice "FUM_0771"
    fumi "\"Nnh... chlp...\"" id a03_cou3_06_f29c3c31

    "Rin's tongue knocked against Fumi's lips, inviting Fumi's tongue out."

    "Their tongues poked hesitantly against each other, then boldly entwined."

    play sound se116a

    hide fumi with Dissolve(0.25)

    show rin:
        "rin 1 lg school h" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512

    voice "RIN_0876"
    rin "\"...Asou...\"" id a03_cou3_06_7e4d89bd

    "Moving the kiss from Fumi's lips to her cheek, Rin slowly lowered Fumi onto a desk..."

    $ side_image = "fumi 2 side school h"

    voice "FUM_0772"
    fumi "\"U-Umm...\"" id a03_cou3_06_98070eb8

    "Fumi again raised a hand apologetically."

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0877"
    rin "\"Ugh... did I do something again?\"" id a03_cou3_06_ae25bb5f

    "Rin asked nervously."

    $ side_image = "fumi 2 side school d"

    voice "FUM_0773"
    fumi "\"N-No, that's not it, just... it might be easier facing this way.\"" id a03_cou3_06_4ec84c8a

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0878"
    rin "\"Oh... you're right.\"" id a03_cou3_06_0e5d114d

    "True, if she lay back like that, she'd probably fall off the desk."

    $ side_image = "fumi 1 side school h"

    voice "FUM_0774"
    fumi "\"I'm sorry. I didn't mean to...\"" id a03_cou3_06_36e6dc49

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0879"
    rin "\"No, I should have realized.\"" id a03_cou3_06_d2bfeac4

    "Rin shook her head, then took Fumi's hand and turned her around."

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0880"
    rin "\"Well then...\"" id a03_cou3_06_9a78f903

    $ side_image = "fumi 2 side school i"

    voice "FUM_0775"
    fumi "\"Right.\"" id a03_cou3_06_c764a447

    "They smiled and touched their foreheads together before lying down on their desk-bed once more."

    stop music fadeout 3.0
    scene black with Dissolve(0.5)
    pause 2.0

    $ side_image = "fumi 2 side school g"

    voice "FUM_0776"
    fumi "\"Will you really make me your wife?\"" id a03_cou3_06_e8fbc227

    $ side_image = "rin 1 side school i"

    voice "RIN_0881"
    rin "\"Huh? Oh... yes.\"" id a03_cou3_06_c952567b

    if persistent.dpatch:
        jump rp_scene03
    else:
        pause 3.5
        "........."
        "......"
        window hide
        pause 2.5
        window auto

label rp_scene03_end:

    scene bg04bb with Dissolve(0.375)
    pause 1.125

    play music bgm02

    play sound se116a

    show rin 1 lg school h at pos_r
    show fumi 2 lg school h at pos_l
    with Dissolve(0.25)

    voice "RIN_0902"
    rin "\".........\"" id rp_scene03_end_6c9eb4b0

    voice "FUM_0800"
    fumi "\"......\"" id rp_scene03_end_27845e37

    "The two of them fixed their clothes silently, faces flushed."

    "When their eyes met, they merely exchanged awkward smiles. They probably both had no idea what to say to each other."

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0903"
    rin "\"Huh...?\"" id rp_scene03_end_f21e4a0f

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0801"
    fumi "\"Oh, your tie's over here.\"" id rp_scene03_end_1bad6024

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0904"
    rin "\"Thanks—\"" id rp_scene03_end_34ce0044

    "Just when she was about to take the ribbon from Fumi..."

    play sound se557a

    voice "HIN_0962"
    hina "\"Huh? Why's the door locked?\"" id rp_scene03_end_f7d6114f

    "...The door rattled."

    show fumi 1 lg school e with dict_dissolve_25

    voice "FUM_0802"
    fumi "\"Ah, Natsume's back.\"" id rp_scene03_end_8602fd8b

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0905"
    rin "\"Is it that time already?\"" id rp_scene03_end_3e55a986

    "The two shared a look."

    hide rin
    hide fumi
    with Dissolve(0.25)

    play sound se560

    pause 1.0

    play sound se000c

    show hina:
        "hina 1 sm school k flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512
    pause 0.5

    show hina 1 sm school k:
        alpha 1.0 xcenter 512
    with None

    voice "HIN_0963"
    hina "\"Rin~? Asou~?\"" id rp_scene03_end_2328f5ed

    "She looked around the classroom."

    voice "HIN_0964"
    hina "\"They're... not here? The curtains are all closed, too...\"" id rp_scene03_end_dc1ed97e

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0965"
    hina "\"...I was kind of hoping they'd be waiting for me...\"" id rp_scene03_end_392fada1

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None

    voice "HIN_0966"
    hina "\"Oh well... guess I'll head home.\"" id rp_scene03_end_31ccfa9f

    play sound se000f

    show hina:
        "hina 1 sm school h flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612

    "Hina sighed, closed the door, and locked it again."

    hide hina with None

    "Her footsteps faded into the distance."

    show rin 1 lg school h at pos_r
    show fumi 1 lg school d at pos_l
    with Dissolve(0.25)

    voice "RIN_0906"
    rin "\"Sheesh... I do feel a little bad for Hina, though.\"" id rp_scene03_end_b25fc96b

    voice "FUM_0803"
    fumi "\"Sorry, Natsume... Let's buy her something on the way home to make up for it.\"" id rp_scene03_end_b576d8b3

    show rin 1 lg school e with dict_dissolve_25:
        1.5
        ShakeSide

    voice "RIN_0907"
    rin "\"Sure... oop.\"" id rp_scene03_end_3ea325ba

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin lost her balance as she tried to get up from under the desk."

    show fumi 1 lg school e with dict_dissolve_25:
        1.5
        ShakeSide

    voice "FUM_0804"
    fumi "\"Are you okay? ...Oh.\"" id rp_scene03_end_a65c3b97

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi did the same."

    show rin:
        "rin 1 lg school c" with Dissolve(0.25)
        ShakeUji

    voice "RIN_0908"
    rin "\"Haha, my knees are all weak.\"" id rp_scene03_end_94671902

    show rin 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0805"
    fumi "\"You think this is...?\"" id rp_scene03_end_64973b70

    "The two looked at each other and laughed at the state they were in."

    show fumi:
        "fumi 2 lg school b" with Dissolve(0.25)
        xcenter 252
        easein 0.5 xcenter 412

    voice "FUM_0806"
    fumi "\"...Thanks.\"" id rp_scene03_end_5c4080d7

    show fumi 2 lg school b:
        xcenter 412
    with None
    show fumi 2 lg school j
    show rin 1 lg school k
    with dict_dissolve_25

    voice "RIN_0909"
    rin "\"...Same here.\"" id rp_scene03_end_52812735

    "They kissed again under the desks."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    scene chapter04
    with Dissolve(0.5)
    pause 1.5

    show chapter04c with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
