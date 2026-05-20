label a09_cou3_06:

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Sunday night."

    "The girls were gathered in the living room, their eyes glued to the TV."

    "Fumi looked uncomfortable, since the program she was going to be on was currently airing. The girls sat with the embarrassed Fumi among them like it was some sort of humiliation roleplay scenario."

    "Except for Rin, who'd taken her bath quickly and sat right in front of the TV, ready and waiting."

    show bg_obi
    show miyako z4 1 lg pyjama_a a:
        xcenter 118
    show hina z4 2 lg pyjama_pjm a:
        xcenter 906

    show rin 1 pyjama glasses h:
        zoom 0.92 xcenter 512 ycenter 1135
    with dict_dissolve_25

    voice "2MI_0930"
    miyako "\"It's taking a while, huh?\""

    "Miyako cocked her head, a teacup in hand."

    "It wasn't a full hour-long special on the store, but rather, the store was one of many being featured on a Valentine-themed variety show."

    "The segment on Le Chocolat Chocolat must be in the second half."

    "Since they didn't know when Fumi would show up, they chatted excitedly during every commercial."

    show hina z4 1 lg pyjama_pjm l with dict_dissolve_25

    voice "2HI_1147"
    hina "\"Oh, that's Asou's store.\""

    "Hina said, pointing at the screen."

    "A familiar store was on screen in a preview of what was to come after the commercial. Looks like it's finally time."

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0900"
    fumi "\"Oh... I'll go get the laundry.\""

    "Fumi stood up when it went to commercial."

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0763"
    sachiko "\"Oh, come on, the dryer's still going.\""

    "Sachiko grabbed her sleeve and sat her down. Her obvious flight was quickly thwarted."

    "Oh yeah, Sachiko's here, too. She's not the type to miss something this fun."

    show hina z4 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_1148"
    hina "\"Let's all watch it together♪\""

    show miyako z4 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0931"
    miyako "\"Yeah, let's♪\""

    "Brilliant smiles. There wasn't a shred of ill intent between the two."

    $ side_image = "fumi 1 side pyjama k"

    voice "2FU_0901"
    fumi "\"Ugh...\""

    "...And the commercial came to an end."

    "The familiar red roof was back on screen, followed by the name of the store, \"Le Chocolat Chocolat,\" and two reporters entering the frame."

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_1149"
    hina "\"Oh, it's Par-Reggi on site.\""

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0932"
    miyako "\"Par-Reggi?\""

    show hina z4 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_1150"
    hina "\"A comedy duo called Parmigiano-Reggiano, Par-Reggi for short.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0933"
    miyako "\"I get it. That's what the two talking outside the store are called?\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0764"
    sachiko "\"Yeah. They moved from Kansai to Tokyo last year, I think. They're pretty popular.\""

    show rin 1 pyjama glasses g with dict_dissolve_25

    voice "2RI_1189"
    rin "\"I don't like them, though.\""

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0902"
    fumi "\"...?\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0934"
    miyako "\"Oh, they're going in the store!\""

    show hina z4 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_1151"
    hina "\"Here we go!\""

    "The door opened, and the camera proceeded into the store."

    voice "2FU_0903"
    fumi "\"W-Welcome!\""

    "Fumi welcomed the camera with a slight awkwardness, wearing an apron and a kerchief."

    hide rin
    show rin 1 120 pyjama_a glasses j as rin_1:
        xcenter 512
        function LayerShake(50,50,0.3)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_1190"
    rin "\"Fumiiiii!!\""

    show rin 1 120 pyjama_a glasses j as rin_1:
        xcenter 512 xoffset 0 yoffset 0
    with None

    "The second Fumi appeared on screen, Rin shrieked and lunged forward to practically wrap her arms around the TV."

    $ side_image = "sachiko 1 side outfit j"

    voice "2SA_0765"
    sachiko "\"Rin, shut up!\""

    show hina z4 1 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_1152"
    hina "\"We can't see! You're in the way!\""

    voice "2RI_1191"
    rin "\"It's Fumi! You're on TV, Fumi! You see, Fumi?\""

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0904"
    fumi "\"Y-Yes... I see.\""

    "Rin pointed out Fumi on the screen, though she was sitting right next to her. Fumi had no idea what to say."

    show hina z4 1 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_1153"
    hina "\"Eheheh, were you nervous, Asou?\""

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0905"
    fumi "\"Very nervous...\""

    "On screen, Fumi was answering questions politely with a smile, same as always, but Hina, who saw her every day, could tell how nervous she was."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0766"
    sachiko "\"You look great on screen, Foomin. And Par-Reggi are doing a great job messing with you. 100 points on the composition here.\""

    show rin 1 120 pyjama_a glasses f as rin_1 with dict_dissolve_25

    voice "2RI_1192"
    rin "\"Yeah!! This is like a promo vid! The first one for Fumi Asou, 'Chocolate Fairy'!\""

    $ side_image = "fumi 1 side pyjama h"

    voice "2FU_0906"
    fumi "\"Umm...\""

    "True, the editing made it clear how much Fumi was being emphasized. The store and its products were the focus of the show, but there were frequent cuts to Fumi as she showed everything off, too."

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0935"
    miyako "\"Wow, that chocolate looks delicious.\""

    "Here's one just watching the show from an average viewer's perspective."

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0907"
    fumi "\"Yeah. That one's new this year—\""

    show rin as rin_1:
        "rin 1 120 pyjama_a glasses i" with Dissolve(0.25)
        ShakeYes

    voice "2RI_1193"
    rin "\"Oh, who cares about the chocolate! Show Fumi, show how she works! Yeah, that's it, good. Hey, cameraman, what are you doing?!\""

    show rin 1 120 pyjama_a glasses i as rin_1:
        xoffset 0 yoffset 0
    with None

    "This girl's just no good."

    $ side_image = "sachiko 1 side outfit j"

    voice "2SA_0767"
    sachiko "\"Seriously, Rin, shut up!\""

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1154"
    hina "\"We can't see! Get out of the way already!\""

    show hina z4 1 lg pyjama_pjm f with None
    hide rin_1
    hide hina
    hide miyako
    with dict_dissolve_50

    "Hina and Sachiko peeled Rin away from the screen."

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_1194"
    rin "\"Let go a' me! I'm gonna see Fumi up close!\""

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_0908"
    fumi "\"Umm, Rin? I'm right here.\""

    "While they struggled, the TV showed a cut of onlookers outside of the window of the store."

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0936"
    miyako "\"Huh?\""

    "Miyako suddenly said."

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1155"
    hina "\"What is it?\""

    "Hina asked, hand firmly gripping the collar of Rin's padded kimono."

    $ side_image = "miyako 1 side pyjama_b g"

    voice "2MI_0937"
    miyako "\"Umm... there.\""

    "Miyako pointed to a person partially in frame—"

    stop music fadeout 1.0

    show fumi 1 lg pyjama j at pos_l2
    show sachiko 1 lg outfit h at pos_r2
    show hina 1 lg pyjama_pjm l
    with dict_dissolve_25
    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ voice3("hina","2HI_1156","fumi","2FU_0909","sachiko","2SA_0768N")
    hina_fumi_sachiko "\"Rin!\""

    camera
    with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou3_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
