label a02_comn_07:

    scene bg05da with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 1 lg pyjama glasses a at pos_l
    show hina 1 lg pyjama m at pos_r:
        ShakeYes
    with Dissolve(0.25)

    play sound se113a

    show hina:
        xoffset 0 yoffset 0
        function LayerShake(15,15,0.1)
    $ persistent.layer_shaken = False
    pause 0.25

    show rin 1 lg pyjama glasses e with Dissolve(0.25)
    show rin at pos_l:
        ShakeSide

    voice "RIN_0347"
    rin "\"Whoa, that scared me.\"" id a02_comn_07_47c6f1fc

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0405"
    hina "\"W-Wah?!\"" id a02_comn_07_3632781a

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None

    "Hina looked around, rubbing her forehead."


    show hina 1 lg pyjama l behind fumi:
        zoom 1.0 xcenter 772 ycenter 981
        easein 0.25 zoom 0.9625 xcenter 842 ycenter 959
    show rin 1 lg pyjama glasses e behind fumi:
        zoom 1.0 xcenter 252 ycenter 1016
        easein 0.25 zoom 0.9625 xcenter 182 ycenter 994
    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0299"
    fumi "\"What was that noise?\"" id a02_comn_07_db21fa27

    show hina z3 1 lg pyjama l at pos_r2_z3:
        zoom 1.0
    show rin z3 1 lg pyjama glasses at pos_l2_z3:
        zoom 1.0
    with None

    "Fumi came back from the kitchen carrying coffee and sandwiches."

    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0348"
    rin "\"Hina nodded off and hit her head on the table.\"" id a02_comn_07_0938d452

    show fumi:
        "fumi z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeTameiki

    voice "FUM_0300"
    fumi "\"Oh no, are you okay?\"" id a02_comn_07_7ff7ccd1

    show fumi z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0406"
    hina "\"I'm awake now.\"" id a02_comn_07_ee8a59df

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0349"
    rin "\"Look, Asou made us snacks while you were sleeping.\"" id a02_comn_07_23d0e5c7

    show hina:
        "hina z3 1 lg pyjama c" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0407"
    hina "\"Really? Yay! I was just getting hungry!\"" id a02_comn_07_a36342d0

    show hina z3 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None

    "Right after waking up. She boots up quick."

    show fumi z3 2 lg pyjama c with Dissolve(0.25)
    show fumi:
        ShakeYes

    play sound se009b

    voice "FUM_0301"
    fumi "\"And I made you a 2:8 café au lait, Natsume.\"" id a02_comn_07_df5c18c0

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0408"
    hina "\"Alright! I can stay awake 'til morning with this!\"" id a02_comn_07_9033fb83

    "I'm not sure that's true."

    show rin z3 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0350"
    rin "\"Thanks. I'll have some, too.\"" id a02_comn_07_15f35988

    show fumi z3 1 lg pyjama c with dict_dissolve_25

    voice "FUM_0302"
    fumi "\"Help yourselves.\"" id a02_comn_07_5dd5a089

    show hina z3 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0409"
    hina "\"Ah, it's so warm and good. Did you toast them a little?\"" id a02_comn_07_dfdeb022

    "Hina beamed after taking a bite of sandwich."

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0351"
    rin "\"Even your snacks are sophisticated.\"" id a02_comn_07_29da5cc2

    "They took a short break, Rin and Hina taking bite after bite of sandwich. Fumi watched them, smiling."

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0410"
    hina "\"Huh? You're not having any? We'll eat them all at this rate.\"" id a02_comn_07_b875fe5a

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0303"
    fumi "\"I know I was the one who made them, but I'm kinda worried I'll gain weight if I eat this late...\"" id a02_comn_07_5e426c2f

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0352"
    rin "\"Hm? Are you on a diet?\"" id a02_comn_07_da515acf

    show fumi:
        "fumi z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeTameiki

    voice "FUM_0304"
    fumi "\"Ahaha... I tend to gain weight as soon as I let my guard down~\"" id a02_comn_07_d12d43ed

    show fumi z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show hina z3 2 lg pyjama d with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "HIN_0411"
    hina "\"That sounds rough. Nom nom.\"" id a02_comn_07_ca0c3dea

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama glasses b with Dissolve(0.25)
    show rin:
        ShakeYes2

    voice "RIN_0353"
    rin "\"Mhmm. Nom nom.\"" id a02_comn_07_5ba0fdae

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0305"
    fumi "\"U-Umm... have you two ever had to diet before...?\"" id a02_comn_07_bfa8f764

    show rin z3 1 lg pyjama glasses a
    show hina z3 1 lg pyjama k
    with dict_dissolve_25

    $ voice2("hina","HIN_0412","rin","RIN_0354")
    hina_rin "\"Nope.\"\n\"Nuh-uh.\"" (what_rest_indent=0)

    show fumi:
        "fumi z3 1 lg pyjama e" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0306"
    fumi "\"Wh-What?!\"" id a02_comn_07_30428fea

    show fumi z3 1 lg pyjama e:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0355"
    rin "\"I don't really gain weight no matter what I eat.\"" id a02_comn_07_2b962c61

    show hina z3 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0413"
    hina "\"Ah, same here~\"" id a02_comn_07_8a6bf90c

    show fumi:
        "fumi z3 1 lg pyjama h" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0307"
    fumi "\"Wh-Wh... What charmed lives you lead.\"" id a02_comn_07_adb7fa1e

    show fumi z3 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None

    "Fumi's shoulders slumped."

    show rin z3 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0356"
    rin "\"I don't think you need to lose weight or anything though, Asou.\"" id a02_comn_07_3566fa23

    "Hina nodded in agreement."

    show fumi z3 1 lg pyjama k with dict_dissolve_25

    voice "FUM_0308"
    fumi "\"Th-Th-Thank... you...\"" id a02_comn_07_cdfb3b82

    "But Fumi's voice was trembling."

    show rin z3 1 lg pyjama glasses f with dict_dissolve_25

    voice "RIN_0357"
    rin "\"In faaact, you've got fat in all the right places, really♪\"" id a02_comn_07_9128ed70

    play sound se206b

    show fumi:
        "fumi z3 1 lg pyjama j" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0309"
    fumi "\"Hyah?!\"" id a02_comn_07_8e2b00a1

    show fumi z3 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    "Rin poked Fumi in the chest with the butt of her pen, and Fumi's breasts jiggled."

    show fumi z3 1 lg pyjama g with dict_dissolve_25

    voice "FUM_0310"
    fumi "\"O-Ogata!\"" id a02_comn_07_cb538104

    show hina z3 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0414"
    hina "\"Quit it with the assault already!\"" id a02_comn_07_3fe0ce0a

    voice "RIN_0358"
    rin "\"Now, where all the food that Hina eats is going is the real question.\"" id a02_comn_07_19d12fd9

    show hina:
        "hina z3 1 lg pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0415"
    hina "\"I-It's nourishing my brain!\"" id a02_comn_07_90e5747c

    show hina z3 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0359"
    rin "\"I find that hard to believe.\"" id a02_comn_07_4178fa39

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a02_cou3_02
    elif rin_hina_score > hina_fumi_score:
        jump a02_cou2_01
    else:
        jump a02_cou1_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
