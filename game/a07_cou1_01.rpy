label a07_cou1_01:

    scene white with Dissolve(0.5)
    pause 2.0

    scene kimikara_01_bm with Dissolve(0.5)
    pause 1.5

    play music bgm02

    play sound se_2s_h038

    voice "2MI_0159"
    miyako "\"......\""

    scene kimikara_01_bk with Dissolve(0.2)
    pause 0.6

    voice "2FU_0117"
    fumi "\"Yes?\""

    voice "2MI_0160"
    miyako "\"Oh, I'm sorry. I wasn't trying to spy or anything...\""

    voice "2FU_0118"
    fumi "\"I don't mind. I was just wondering if you wanted something.\""

    voice "2MI_0161"
    miyako "\"I was just watching your face.\""

    voice "2FU_0119"
    fumi "\"Wah... That might be more embarrassing than you reading my diary.\""

    voice "2MI_0162"
    miyako "\"Your expression keeps changing as you write.\""

    voice "2FU_0120"
    fumi "\"Huh? Really? I was making faces?\""

    scene kimikara_01_bn with Dissolve(0.2)
    pause 0.6

    voice "2MI_0163"
    miyako "\"Yes, lots of them.\""

    voice "2FU_0121"
    fumi "\"Well, you do sort of remember how you felt when you write about your experiences.\""

    voice "2MI_0164"
    miyako "\"Your memories must be very clear.\""

    voice "2FU_0122"
    fumi "\"I forget right away after I sleep, though. That's why I write things down before bed.\""

    scene kimikara_01_bk with Dissolve(0.2)
    pause 0.6

    voice "2MI_0165"
    miyako "\"I see.\""

    "People forget. So they keep records. Diaries, pictures, videos... They have many methods."

    "But angels don't forget, so they have no ways to keep records."

    voice "2FU_0123"
    fumi "\"If I write things down, I can remember them when I go back and read them.\""

    "Angels are observers, but they are also record keepers. Maybe Miyako found Fumi's diary-keeping relatable."

    voice "2FU_0124"
    fumi "\"Hina's album must be the same.\""

    voice "2MI_0166"
    miyako "\"......\""

    "Every human has their own memory, or to put it more grandly, history."

    voice "2FU_0125"
    fumi "\"She'd probably say her pictures are art, but—\""

    play sound se_kajiru
    pause 0.5

    scene kimikara_01_bl with Dissolve(0.2)
    pause 0.6

    voice "2RI_0157"
    rin "\"Alright, pay the fine.\""

    scene kimikara_01_bc with Dissolve(0.2)
    pause 0.6

    voice "2FU_0126"
    fumi "\"Ah.\""

    "Rin didn't miss the sound of Fumi nibbling on a cookie."

    voice "2RI_0158"
    rin "\"In case you forgot, the no-eating-after-nine rule was your idea, Asou.\""

    voice "2FU_0127"
    fumi "\"I know. Please keep reminding me...\""

    play sound se_tyokin

    "It's hard to break longtime habits."

    voice "2FU_0128"
    fumi "\"Haahh...\""

    "Her sigh blew something up from the pages of the diary; it floated to the rug, where Miyako picked it up."

    scene kimikara_01_bm with Dissolve(0.2)
    pause 0.6

    voice "2MI_0167"
    miyako "\"This is...\""

    scene kimikara_01_bk with Dissolve(0.2)
    pause 0.6

    voice "2FU_0129"
    fumi "\"Oh, it's an angel feather.\""

    "Yes. It was {i}Miyako's{/i} feather."

    "Though Sachiko had swapped it out for a goose's."

    voice "2FU_0130"
    fumi "\"I'm using it as a bookmark.\""

    "Fumi took the feather from Miyako and gently closed her diary around it."

    voice "2FU_0131"
    fumi "\"It flew out of the window once, and Hina went and found it for me.\""

    scene kimikara_01_bo with Dissolve(0.2)
    pause 0.6

    voice "2RI_0159"
    rin "\"That was quite a day. Hina caught a cold and was laid up with a fever.\""

    voice "2MI_0168"
    miyako "\"I'm sorry.\""

    scene kimikara_01_bl with Dissolve(0.2)
    pause 0.6

    voice "2FU_0132"
    fumi "\"Hm?\""

    voice "2MI_0169"
    miyako "\"N-Nothing.\""

    voice "2FU_0133"
    fumi "\"But it's thanks to that that Hina and I... Hina is my angel now.\""

    voice "2MI_0170"
    miyako "\"......\""

    voice "2RI_0160"
    rin "\"That angel of yours is snoring over here.\""

    "I {i}thought{/i} she was being rather quiet."

    voice "2FU_0134"
    fumi "\"Oh, I hope she doesn't catch a cold again.\""

    scene white with Dissolve(0.1875)
    pause 1.0625

    scene bg01cg with Dissolve(0.25)
    pause 0.75

    show miyako:
        "miyako z4 1 lg pyjama_a b flat"
        alpha 0.0 xcenter 298 ycenter 857
        easein 0.5 alpha 1.0 ycenter 757

    voice "2MI_0171"
    miyako "\"I'm going to go get my printout.\""

    show miyako z4 1 lg pyjama_a b:
        alpha 1.0 xcenter 298 ycenter 757
    with None

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0161"
    rin "\"I'll come with. I'm gonna go take a bath.\""

    pause 0.25

    show rin:
        "rin z4 1 lg pyjama glasses a flat"
        alpha 0.0 xcenter 726 ycenter 853
        easein 1.0 alpha 1.0 ycenter 759

    "When Miyako stood, Rin joined her, slightly unsteady."

    show rin z4 1 lg pyjama glasses a:
        alpha 1.0 xcenter 726 ycenter 759
    with None

    show rin:
        ShakeNo_3_500

    voice "2RI_0162"
    rin "\"Ugh... I have to go next-door again... It's cold and I'll be all alone...\""

    show rin:
        alpha 1.0 xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0135"
    fumi "\"You should have gone with us when we went earlier.\""

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0163"
    rin "\"I was right at the climax of the book I was reading...\""

    $ side_image = "fumi 1 side pyjama a"

    voice "2FU_0136"
    fumi "\"I know. Go warm up, and make sure you don't catch cold.\""

    show rin:
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeNo_3_500

    voice "2RI_0164"
    rin "\"Uuugh...\""

    hide rin
    hide miyako
    with Dissolve(0.5)
    pause 0.25

    scene white with bg_effect_05

    pause 1.5

    scene bg01cg
    show bg_obi
    with bg_effect_05

    pause 0.5

    show hina:
        "hina 1 lg pyjama j flat"
        alpha 0.0 xcenter 772 ycenter 1081
        easein 1.0 alpha 1.0 ycenter 981

    voice "2HI_0165"
    hina "\"Huh? Where's Rin and Miyako?\""

    "Hina looked around, rubbing her eyes."

    show fumi 2 lg pyjama b at pos_l with dict_dissolve_25

    voice "2FU_0137"
    fumi "\"Ogata went to take a bath and Miyako's getting her printout from Sachiko.\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "2HI_0166"
    hina "\"Oh. Was Rin whining?\""

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0138"
    fumi "\"Yes, I think that describes it.\""

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "2HI_0167"
    hina "\"I thought she would. That's why she should have come with us.\""

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0139"
    fumi "\"Right?\""

    "Miyako had gone with them."

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "2HI_0168"
    hina "\"It's kind of strange. It's only been two weeks since Miyako came, right?\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0140"
    fumi "\"Right. But it feels like she's been here longer.\""

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "2HI_0169"
    hina "\"Yeah. {i}She's{/i} also kind of strange, though.\""

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "2FU_0141"
    fumi "\"Aside from how she sleeps a lot?\""

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "2HI_0170"
    hina "\"Doesn't she bump into walls and doors a lot? Without even slowing down.\""

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0142"
    fumi "\"Oh, that's true. I guess she's pretty absentminded.\""

    show hina 1 lg pyjama c with dict_dissolve_25

    voice "2HI_0171"
    hina "\"Maybe. It's like she thinks she can go through them.\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0143"
    fumi "\"She jumps a lot, just out of nowhere.\""

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "2HI_0172"
    hina "\"Yeah, I've seen that. Like she's about to fly away! There's no way, though, right?\""

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0144"
    fumi "\"Ahaha, maybe she used to be an angel.\""

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "2HI_0173"
    hina "\"Yeah, right.\""

    "Well, she's not used to this."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
