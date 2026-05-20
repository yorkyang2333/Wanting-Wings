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
    rin "\"We're... alone.\""

    show fumi:
        "fumi 1 lg school d" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0747"
    fumi "\"W-We are... Natsume's at her committee meeting...\""

    show fumi 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0842"
    rin "\"It's about Christmas mass, right?\""

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0748"
    fumi "\"Yes. She said it might take a while...\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0843"
    rin "\"Hmm...\""

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0749"
    fumi "\"......\""

    "After three false starts, Rin broke the silence between them."

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0844"
    rin "\"Is this a 'chance'... you think?\""

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0750"
    fumi "\"You think?\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0845"
    rin "\"We got one sooner than I thought we would... huh?\""

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0751"
    fumi "\"Aha... haha...\""

    "The two smiled awkwardly at each other, their cheeks red in the light of the setting sun."

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0752"
    fumi "\"We might get interrupted again, though...\""

    show rin:
        "rin 1 lg school h" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 662
    pause 0.25

    show rin 1 lg school h:
        xcenter 662
        ShakeYes

    voice "RIN_0846"
    rin "\"......\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin grabbed Fumi by the wrist."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0753"
    fumi "\"...Ah...\""

    "Fumi could tell what was coming next from Rin's solemn face."

    "......"

    voice "RIN_0847"
    rin "\"But if you don't want to—\""

    "The short silence tempered Rin's courage."

    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_0754"
    fumi "\"I do... want to.\""

    "She placed her hand over Rin's sweaty hand on her wrist."

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_0848"
    rin "\"Asou...\""

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
    fumi "\"Umm...\""

    show rin:
        "rin 1 lg school e" with Dissolve(0.25)
        xcenter 612
        easein 0.25 xcenter 662

    voice "RIN_0849"
    rin "\"Huh?\""

    show rin 1 lg school e:
        xcenter 662
    with None
    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0756"
    fumi "\"Maybe we should lock the doors...\""

    "Fumi pointed out."

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0850"
    rin "\"Oh, right!\""

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
    rin "\"Okay...\""

    "Rin placed a hand on Fumi's shoulder."

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0757"
    fumi "\"We should close the curtains, too...\""

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0852"
    rin "\"Right... You're right.\""

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
    rin "\"...Is that good, you think?\""

    "Rin pointed to each door, the hall-side windows, and the courtyard-side windows, then turned back to Fumi."

    show fumi 2 lg school h with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "FUM_0758"
    fumi "\"Yes.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi nodded serenely."

    stop music fadeout 3.0

    show rin 2 lg school b with dict_dissolve_25

    voice "RIN_0854"
    rin "\"...Asou...\""

    show fumi 2 lg school j with dict_dissolve_25

    voice "FUM_0759"
    fumi "\"......\""

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
    rin "\"Daaah!!\""

    hide rin with Dissolve(0.25)

    "Rin shouted in frustration and pulled her phone out of her pocket. The screen was displaying Sachiko's name."

    play music bgm01

    play sound se026c

    $ side_image = "rin 1 side school g"

    voice "RIN_0856"
    rin "\"Yes, what is it? I'm kind of busy at the moment.\""

    $ side_image = "rin 1 side school j"

    voice "RIN_0857"
    rin "\"What? Cigarettes?! ...I got it, fine, I'll buy them!\""

    $ side_image = "rin 1 side school g"

    voice "RIN_0858"
    rin "\"Okay, I'm hanging up. ...A mood? Hell yes, I'm in a mood! I'm in the middle of something important!\""

    $ side_image = "rin 1 side school j"

    voice "RIN_0859"
    rin "\"What, you still want something? ...Huh?! What do you mean 'my rest'?!\""

    play sound se026c

    pause 1.0

    show rin 1 lg school j behind fumi at pos_r with Dissolve(0.25)

    voice "RIN_0860"
    rin "\"Geez!\""

    "Rin turned her phone off and jammed it back into her pocket."

    stop music fadeout 3.0

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        xcenter 772
        easein 0.5 xcenter 612

    voice "RIN_0861"
    rin "\"O-Okay, this time...!\""

    show rin 1 lg school g:
        xcenter 612
    with None

    "She grabbed Fumi by the shoulders."

    play sound se_bati

    show bati2 at truecenter
    pause 0.3

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0760"
    fumi "\"......Pfft.\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0862"
    rin "\"Huh? What?\""

    "Rin's eyes went wide when Fumi giggled."

    play music bgm02

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0761"
    fumi "\"I think this is the first time I've seen you lose your composure this much... eheheh.\""

    voice "RIN_0863"
    rin "\"......\""

    "Rin merely stared at Fumi, dumbfounded."

    show fumi 1 lg school i with dict_dissolve_25

    voice "FUM_0762"
    fumi "\"I'm sorry... Are you mad?\""

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0864"
    rin "\"...Hahh...\""

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "She sighed and loosened her grip on Fumi's shoulders."

    show rin:
        "rin 2 lg school e" with Dissolve(0.25)
        xcenter 612
        easein 0.5 xcenter 772

    voice "RIN_0865"
    rin "\"I really lost my cool there, huh?\""

    "Rin took a step back from Fumi and sat down at the desk behind her, smiling wryly."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0866"
    rin "\"I really thought I'd be smoother about all this, but it just doesn't go how you plan it, huh?\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0763"
    fumi "\"I think I'd be more nervous if you were used to this.\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0867"
    rin "\"Yeah, but I really... Sorry. I'm being really uncool.\""

    "Rin ran a hand through her hair embarrassedly."

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0764"
    fumi "\"I think it's cute.\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0868"
    rin "\"...Cute?\""

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0765"
    fumi "\"Yeah. How you try so hard to be cool for me.\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0869"
    rin "\"That obvious...?\""

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0766"
    fumi "\"That's what makes it cute.\""

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0870"
    rin "\"Ugh... sorry, I'm really not used to hearing that.\""

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "Rin looked down, covering her flushed face with her hands."

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0767"
    fumi "\"Haha. You'd better get used to it, because I'm going to say it a lot more from now on.\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0871"
    rin "\"...I'll try.\""

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0768"
    fumi "\"......\""

    show rin 2 lg school b with dict_dissolve_25

    voice "RIN_0872"
    rin "\"So, what should we do? Just give up for—\""

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
    rin "\"?!\""

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0769"
    fumi "\"Let's keep going.\""

    "Slowly pulling back, Fumi smiled tenderly."

    "The way the light of the setting sun shone through the curtains and outlined her companion was almost divine. Rin gasped."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0874"
    rin "\"...Okay.\""

    "Rin nodded after a long pause. She drew closer to Fumi, as if possessed."

    show fumi 2 lg school j
    show rin 1 lg school k
    with dict_dissolve_25

    voice "FUM_0770"
    fumi "\"...Nnh.\""

    "This time Rin initiated the kiss."

    voice "RIN_0875"
    rin "\"Mm... chp...\""

    voice "FUM_0771"
    fumi "\"Nnh... chlp...\""

    "Rin's tongue knocked against Fumi's lips, inviting Fumi's tongue out."

    "Their tongues poked hesitantly against each other, then boldly entwined."

    play sound se116a

    hide fumi with Dissolve(0.25)

    show rin:
        "rin 1 lg school h" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512

    voice "RIN_0876"
    rin "\"...Asou...\""

    "Moving the kiss from Fumi's lips to her cheek, Rin slowly lowered Fumi onto a desk..."

    $ side_image = "fumi 2 side school h"

    voice "FUM_0772"
    fumi "\"U-Umm...\""

    "Fumi again raised a hand apologetically."

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0877"
    rin "\"Ugh... did I do something again?\""

    "Rin asked nervously."

    $ side_image = "fumi 2 side school d"

    voice "FUM_0773"
    fumi "\"N-No, that's not it, just... it might be easier facing this way.\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0878"
    rin "\"Oh... you're right.\""

    "True, if she lay back like that, she'd probably fall off the desk."

    $ side_image = "fumi 1 side school h"

    voice "FUM_0774"
    fumi "\"I'm sorry. I didn't mean to...\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0879"
    rin "\"No, I should have realized.\""

    "Rin shook her head, then took Fumi's hand and turned her around."

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0880"
    rin "\"Well then...\""

    $ side_image = "fumi 2 side school i"

    voice "FUM_0775"
    fumi "\"Right.\""

    "They smiled and touched their foreheads together before lying down on their desk-bed once more."

    stop music fadeout 3.0
    scene black with Dissolve(0.5)
    pause 2.0

    $ side_image = "fumi 2 side school g"

    voice "FUM_0776"
    fumi "\"Will you really make me your wife?\""

    $ side_image = "rin 1 side school i"

    voice "RIN_0881"
    rin "\"Huh? Oh... yes.\""

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
    rin "\".........\""

    voice "FUM_0800"
    fumi "\"......\""

    "The two of them fixed their clothes silently, faces flushed."

    "When their eyes met, they merely exchanged awkward smiles. They probably both had no idea what to say to each other."

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0903"
    rin "\"Huh...?\""

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0801"
    fumi "\"Oh, your tie's over here.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0904"
    rin "\"Thanks—\""

    "Just when she was about to take the ribbon from Fumi..."

    play sound se557a

    voice "HIN_0962"
    hina "\"Huh? Why's the door locked?\""

    "...The door rattled."

    show fumi 1 lg school e with dict_dissolve_25

    voice "FUM_0802"
    fumi "\"Ah, Natsume's back.\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0905"
    rin "\"Is it that time already?\""

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
    hina "\"Rin~? Asou~?\""

    "She looked around the classroom."

    voice "HIN_0964"
    hina "\"They're... not here? The curtains are all closed, too...\""

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0965"
    hina "\"...I was kind of hoping they'd be waiting for me...\""

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None

    voice "HIN_0966"
    hina "\"Oh well... guess I'll head home.\""

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
    rin "\"Sheesh... I do feel a little bad for Hina, though.\""

    voice "FUM_0803"
    fumi "\"Sorry, Natsume... Let's buy her something on the way home to make up for it.\""

    show rin 1 lg school e with dict_dissolve_25:
        1.5
        ShakeSide

    voice "RIN_0907"
    rin "\"Sure... oop.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin lost her balance as she tried to get up from under the desk."

    show fumi 1 lg school e with dict_dissolve_25:
        1.5
        ShakeSide

    voice "FUM_0804"
    fumi "\"Are you okay? ...Oh.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi did the same."

    show rin:
        "rin 1 lg school c" with Dissolve(0.25)
        ShakeUji

    voice "RIN_0908"
    rin "\"Haha, my knees are all weak.\""

    show rin 1 lg school c:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0805"
    fumi "\"You think this is...?\""

    "The two looked at each other and laughed at the state they were in."

    show fumi:
        "fumi 2 lg school b" with Dissolve(0.25)
        xcenter 252
        easein 0.5 xcenter 412

    voice "FUM_0806"
    fumi "\"...Thanks.\""

    show fumi 2 lg school b:
        xcenter 412
    with None
    show fumi 2 lg school j
    show rin 1 lg school k
    with dict_dissolve_25

    voice "RIN_0909"
    rin "\"...Same here.\""

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
