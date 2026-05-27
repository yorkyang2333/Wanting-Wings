label a08_comn_12:

    scene bg09cb with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_boiling1

    "The pot was boiling."

    "In it was a seafood soup Sachiko had prepared."

    "Hina, Rin, and Miyako were sitting around the table waiting for it to finish cooking."

    "Fumi and Sachiko were at the sink."

    play sound se_suidouto

    show sachiko 1 lg outfit a at pos_l
    show fumi 1 lg pyjama a at pos_r
    with dict_dissolve_25

    voice "2SA_0304"
    sachiko "\"Foomin, thanks for helping out.\"" id a08_comn_12_941785c7

    "Sachiko said, wiping her hands off with a towel."

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0485"
    fumi "\"Oh, I just chopped some vegetables. I was a little surprised to see you preparing that fish, though.\"" id a08_comn_12_c3509fe1

    "Fumi said, setting a cutting board upright."

    show sachiko 1 lg outfit f with dict_dissolve_25

    voice "2SA_0305"
    sachiko "\"Yeah, I did some training before I started here.\"" id a08_comn_12_4b375e8d

    show fumi 1 lg pyjama e with dict_dissolve_25

    voice "2FU_0486"
    fumi "\"Huh? You were a cook before becoming a dorm manager?\"" id a08_comn_12_b6f9b404

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0306"
    sachiko "\"Nothing serious like that.\"" id a08_comn_12_2c607bee

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0556"
    hina "\"Not yet!\"" id a08_comn_12_7f0a5e17

    "Hina's shrill voice cut off Rin's attempt to extend her chopsticks."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0557"
    hina "\"It's not done cooking yet. The cabbage is still hard, the tofu hasn't absorbed any of the flavor, and the crab and cod are still raw!\"" id a08_comn_12_058b1289

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "2SA_0307"
    sachiko "\"Heheh, looks like someone's taking charge over there, so we don't have to worry about the rest.\"" id a08_comn_12_d1b100d8

    show fumi 1 lg pyjama c with dict_dissolve_25

    voice "2FU_0487"
    fumi "\"It does.\"" id a08_comn_12_3be53e2d

    "The two laughed and headed to the living room."

    hide fumi
    hide sachiko
    with Dissolve(0.5)

    show bg_obi
    with bg_effect_30_1200

    pause 0.3

    show hina 1 lg pyjama_pjm e at pos_l
    show rin 1 lg pyjama glasses e at pos_r
    with dict_dissolve_25

    voice "2RI_0571"
    rin "\"What? Really? But it's bubbling.\"" id a08_comn_12_7cbf06cc

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0558"
    hina "\"Huh? Have you never done this at home before?\"" id a08_comn_12_2937fcd2

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0572RE"
    rin "\"Nope. I've barely ever eaten with my family.\"" id a08_comn_12_2d636652

    show hina 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0559"
    hina "\"Oh... sorry.\"" id a08_comn_12_df92d0e8

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0308"
    sachiko "\"Well, great! It's your first hotpot!\"" id a08_comn_12_893e7d5c

    "Sachiko patted Rin on the head as she sat."

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0573"
    rin "\"Mm. Well, it's more that I have no experience cooking rather than the whole family thing.\"" id a08_comn_12_dbf6d68d

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0309"
    sachiko "\"Try it sometime.\"" id a08_comn_12_ad328678

    $ side_image = "miyako 1 side pyjama_a d"

    voice "2MI_0453"
    miyako "\"It's my first hotpot, too!\"" id a08_comn_12_e4d18472

    $ side_image = "fumi 1 side pyjama c"

    voice "2FU_0488"
    fumi "\"It's fun. Let's all eat our fill.\"" id a08_comn_12_b19a4a1b

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0310"
    sachiko "\"You're in charge, chief!\"" id a08_comn_12_aea51e72

    play sound se_futa

    show hina 1 lg pyjama_pjm p with Dissolve(0.25)
    show hina:
        1.8
        "hina 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0560"
    hina "\"Leave it to me! Hey, what do you think you're opening?!\"" id a08_comn_12_0e721697

    show hina 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit j"

    voice "2SA_0311"
    sachiko "\"Well, I got some local sake with this stuff! I'm an adult, so what's wrong with it?\"" id a08_comn_12_046e8069

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0574"
    rin "\"Where are you from, anyway, Sachiko?\"" id a08_comn_12_143bcddb

    hide hina with Dissolve(0.25)

    show sachiko 1 lg outfit a at pos_l with dict_dissolve_25

    voice "2SA_0312"
    sachiko "\"Why?\"" id a08_comn_12_42e6c424

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0575"
    rin "\"This stuff's from all over the place. The ponzu sauce is from Shikoku, and isn't this booze from Tohoku?\"" id a08_comn_12_d8b1ece6

    "Rin picked up the bottles and examined their labels."

    voice "2SA_0313"
    sachiko "\"Oh. Well, it's not sent from home. People I met when I was traveling sent it.\"" id a08_comn_12_b74736a6

    show rin 1 lg pyjama glasses b with Dissolve(0.25)
    show rin:
        ShakeYes
        1.05
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0576"
    rin "\"Oh yeah?—Ow.\"" id a08_comn_12_e3f532a6

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit c
    show rin 1 lg pyjama glasses i
    with dict_dissolve_25

    "Sachiko slapped Rin's hand when she tried to nonchalantly pour the sake into her own glass."

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0561"
    hina "\"Traveling?\"" id a08_comn_12_ec4251c4

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0314"
    sachiko "\"Yeah, all around Japan, painting pictures.\"" id a08_comn_12_5e8b6f8b

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0562"
    hina "\"By yourself?\"" id a08_comn_12_bcaa0244

    voice "2SA_0315"
    sachiko "\"Yep. I had people to visit all over. Learned a lot from them, too.\"" id a08_comn_12_1e4220ab

    $ side_image = "fumi 2 side pyjama g"

    voice "2FU_0489"
    if persistent.dpatch:
        fumi "\"Learned? Did you meet them in school?\"" id a08_comn_12_3209f02d
    else:
        fumi "\"Learned? Did you meet them on campus?\"" id a08_comn_12_1ad488e1

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "2SA_0316"
    sachiko "\"Ah... yeah.\"" id a08_comn_12_b52dc453

    $ side_image = "miyako 1 side pyjama_a a"

    voice "2MI_0454"
    miyako "\"......\"" id a08_comn_12_b39adb52

    "Miyako was the only one who knew what it was Sachiko had learned from those people."

    show sachiko 1 lg outfit f with dict_dissolve_25

    voice "2SA_0317"
    sachiko "\"And so, I had a woman at every port—\"" id a08_comn_12_6b0ad432

    show rin 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0577"
    rin "\"Alright, no tall tales.\"" id a08_comn_12_e1ad6cae

    hide rin with Dissolve(0.25)

    show miyako 1 lg pyjama_a b at pos_r with dict_dissolve_25

    voice "2MI_0455"
    miyako "\"Sachiko, Sachiko.\"" id a08_comn_12_e6014c09

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0318"
    sachiko "\"Yeah?\"" id a08_comn_12_7332ef6a

    show miyako 1 lg pyjama_b e with dict_dissolve_25

    voice "2MI_0456"
    miyako "\"Are these paintings from then?\"" id a08_comn_12_941b8a18

    "Miyako pointed at some canvases that had been hastily set aside."

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "2SA_0319"
    sachiko "\"Oh, uhh, yeah.\"" id a08_comn_12_214af378

    show miyako 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0457"
    miyako "\"Do you mind if I see them?\"" id a08_comn_12_41d7977a

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0320"
    sachiko "\"Mmm, well... not really, but they're nothing special.\"" id a08_comn_12_da7f8184

    show miyako 1 lg pyjama_a d with Dissolve(0.25)
    show miyako:
        ShakeYes

    voice "2MI_0458"
    miyako "\"Thank you!\"" id a08_comn_12_f921ea1b

    show miyako:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 2 side pyjama i"

    voice "2FU_0490"
    fumi "\"Oh, I want to see them too.\"" id a08_comn_12_e497db6a

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0578"
    rin "\"Let's see here.\"" id a08_comn_12_bd3a148d

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_0563"
    hina "\"What~? I don't want to see any nudes.\"" id a08_comn_12_1b4a0491

    hide bg_obi
    hide sachiko
    hide miyako
    with Dissolve(0.5)

    "The four of them picked up some canvases."

    "Each painting was of scenery."

    show fumi z4 2 lg pyjama c:
        xcenter 118 ycenter 757
    show miyako z4 1 lg pyjama_a b behind fumi, hina:
        xcenter 383 ycenter 757
    show hina z4 1 lg pyjama_pjm k:
        xcenter 641 ycenter 730
    show rin z4 1 lg pyjama glasses h:
        xcenter 906 ycenter 753
    with dict_dissolve_25

    voice "2FU_0491"
    fumi "\"Wow... You're good!\"" id a08_comn_12_b6065be3

    voice "2MI_0459"
    miyako "\"Yes. The colors are wonderful!\"" id a08_comn_12_b182b3d3

    "Fumi and Miyako were very impressed by the painting between them."

    voice "2HI_0564"
    hina "\"Huh? There's no nudes.\"" id a08_comn_12_741c99df

    voice "2RI_0579"
    rin "\"That's disappointing. You don't have any?\"" id a08_comn_12_399602da

    $ side_image = "sachiko 1 side outfit e"

    voice "2SA_0321"
    sachiko "\"Nope. But if you model for me, I'll paint one any time♪\"" id a08_comn_12_3ed9c3f3

    show hina 1 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0565"
    hina "\"No thanks!\"" id a08_comn_12_ee3f954e

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0580"
    rin "\"Well, I wouldn't call you prolific.\"" id a08_comn_12_4c10c6af

    "Rin said, counting the canvases."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0322"
    sachiko "\"Yeah, I don't want to paint anything I don't like, so.\"" id a08_comn_12_338d9b44

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0566"
    hina "\"Do you still travel now?\"" id a08_comn_12_08c53654

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0323"
    sachiko "\"Sometimes, like on summer break.\"" id a08_comn_12_236988f5

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0492"
    fumi "\"All alone?\"" id a08_comn_12_83e0158c

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0324"
    sachiko "\"Heh... That's right, I'm always all alone on a sentimental journey...\"" id a08_comn_12_5e73e3c0

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0581"
    rin "\"Yeah, you seem like you'd travel to try and find yourself or whatever~\"" id a08_comn_12_8f1de08b

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0325"
    sachiko "\"So do {i}you{/i}. If you wait to catch the bug until you're older, the symptoms'll be worse, you know. You should get it over with\nsooner.\"" id a08_comn_12_0d3c390f

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0567"
    hina "\"So did you find yourself while traveling?\"" id a08_comn_12_02640937

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0326"
    sachiko "\"Nope, not at all. Still looking.\"" id a08_comn_12_64956dfc

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0460"
    miyako "\"......\"" id a08_comn_12_0faa69b6

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0327"
    sachiko "\"Oh, looks like it's cooked. Can we eat, Hinacchi?\"" id a08_comn_12_aa703bf3

    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0568"
    hina "\"Mm... looks good!\"" id a08_comn_12_9273d525

    "Time to eat."

    hide rin
    hide fumi
    hide hina
    hide miyako
    with Dissolve(0.5)

    show bg_obi with Dissolve(0.5)
    pause 0.5

    $ side_image = "sachiko 1 side outfit e"

    voice "2SA_0328"
    sachiko "\"Ahn, an indirect kiss~\"" id a08_comn_12_6f564e77

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0569"
    hina "\"Don't put your chopsticks in the pot!\"" id a08_comn_12_50f0e1c7

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a08_cou1_03
    elif route2 == 2:
        jump a08_cou2_04
    elif route2 == 3:
        jump a08_cou3_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
