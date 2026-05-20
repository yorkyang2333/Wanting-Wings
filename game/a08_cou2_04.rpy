label a08_cou2_04:

    scene bg09cb with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_boiling1
    pause 0.5

    show bg_obi
    show fumi z4 1 lg pyjama d
    with dict_dissolve_25

    voice "2FU_0541"
    fumi "\"I'm feeling pretty full now~\""

    "Fumi let out a little sigh. They were getting to the end of the hotpot."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0419"
    sachiko "\"I've got some rice soup to finish up?\""

    show fumi z4 1 lg pyjama i with dict_dissolve_25

    voice "2FU_0542"
    fumi "\"Rice soup... That sounds good.\""

    "Does she have room for that?"

    show fumi:
        "fumi z4 1 lg pyjama d" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_0543"
    fumi "\"I'm full, but it tastes so good it's hard to stop.\""

    show fumi z4 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None

    "She seemed embarrassed, but kept right on eating."

    $ side_image = "miyako 1 side pyjama_a k"

    voice "2MI_0542"
    miyako "\"You're exactly right! But if you keep eating just because it tastes good, something {i}terrible{/i} could happen later!\""

    "Miyako emphasized. Seems the Christmas cake incident was still weighing heavily on her."

    show fumi:
        "fumi z4 1 lg pyjama k" with Dissolve(0.25)
        ShakeSide

    voice "2FU_0544"
    fumi "\"Augh! I figured today was a special exception, but I should probably stop, shouldn't I?\""

    show fumi z4 1 lg pyjama k:
        xoffset 0 yoffset 0
    with None

    "Fumi seemed to interpret Miyako's \"something terrible\" to mean something else."

    $ side_image = "rin 1 side pyjama glasses f"

    voice "2RI_0685"
    rin "\"Actually, since hotpots are so hot, they make you sweat, which cancels out the calories.\""

    show fumi:
        "fumi z4 1 lg pyjama e" with Dissolve(0.25)
        ShakeJump

    voice "2FU_0545B"
    fumi "\"Really?!\""

    show fumi z4 1 lg pyjama e:
        xoffset 0 yoffset 0
    with None

    "There goes Rin."

    hide bg_obi
    hide fumi
    with Dissolve(0.5)

    pause 0.5

    play sound se_2s_k006

    pause 1.0

    $ side_image = "hina 2 side pyjama_pjm e"

    voice "2HI_0669"
    hina "\"......\""

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0420"
    sachiko "\"Hm? Whatcha doin', Hinacchi?\""

    "Hina was rifling through the canvases stacked up in the corner of the room."


    show hina 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0670"
    hina "\"I wanna see Rin's picture. The one she modeled for before Christmas.\""

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0421"
    sachiko "\"Ah, that one's not in the canvases.\""

    "Sachiko stood up and plucked out a sketchbook from a shelf."

    show hina:
        xcenter 512
        easein 0.5 xcenter 252

    pause 1.0

    show sachiko 1 lg outfit a at pos_r with Dissolve(0.25)

    voice "2SA_0422"
    sachiko "\"Here y'go.\""

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0671"
    hina "\"A doodle book?\""

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "2SA_0423"
    sachiko "\"Ahaha, yeah, I guess they're basically doodles.\""

    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    "Hina opened up the sketchbook."

    "Rough pencil sketches filled the pages. From the balance of her arms and legs and the length of her hair, it did look like Rin."

    "They were mostly simple poses, some without any details on the arms and legs."

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0672"
    hina "\"They're not dirty. Or nudes.\""

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0686"
    rin "\"Of course they aren't!\""

    show sachiko 1 lg outfit f with dict_dissolve_25

    voice "2SA_0424"
    sachiko "\"I tried so hard to persuade her, too...\""

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0687"
    rin "\"Like hell I'm stripping for you!\""

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0673"
    hina "\"I wasn't expecting this. I thought there'd be more details.\""

    "Hina must have been expecting a portrait."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0425"
    sachiko "\"Rin's got long limbs and she's flexible, so she makes a perfect posing doll.\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0688"
    rin "\"How rude.\""

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "2SA_0426"
    sachiko "\"It's a compliment.\""

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_0689"
    rin "\"Doesn't sound like one. But hey, all that paid for this.\""

    "Rin said, tugging lightly on Hina's collar."

    show hina 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0674"
    hina "\"Yeah... thanks.\""

    $ side_image = "rin 1 side pyjama glasses f"

    voice "2RI_0690"
    rin "\"I worked real hard. I'm such a nice person.\""

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0675"
    hina "\"Sachiko, can I have these sketches?\""

    show sachiko 1 lg outfit c with dict_dissolve_25

    voice "2SA_0427"
    sachiko "\"Even though they're just doodles?\""

    show hina 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0676"
    hina "\"No, I think they're really good. They really show off Rin's stuff.\""

    show sachiko:
        "sachiko 1 lg outfit g" with Dissolve(0.25)
        2.8
        "sachiko 1 lg outfit f" with Dissolve(0.25)

    voice "2SA_0428"
    sachiko "\"Well hey, I can take a compliment. Thanks! I kinda want to hold on to my work, though.\""

    show sachiko 1 lg outfit f:
        pass
    with None
    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0677"
    hina "\"I'll take really good care of them.\""

    "Hina pointed her puppy-dog eyes at Sachiko."

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0429"
    sachiko "\"Mm~ I'll trade 'em for that choker, then.\""

    show hina 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0678"
    hina "\"......\""

    show sachiko:
        "sachiko 1 lg outfit h" with Dissolve(0.25)
        ShakeJump

    voice "2SA_0430"
    sachiko "\"Kidding! Kidding!\""

    show sachiko 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    "Sachiko backpedaled when she saw Hina about to cry."

    show hina 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0679"
    hina "\"...Could you draw us together sometime, then?\""

    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "2SA_0431"
    sachiko "\"Nude?\""

    show hina 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0680"
    hina "\"If it's with Rin...\""

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0691"
    rin "\"Hell no!\""

    "That's a \"no\" from the costar."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 0:
        jump a08_comn_13
    else:
        jump a08_comn_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
