label a10_cou1_04:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    if persistent.dpatch:
        "—After school. The four girls were getting ready to go home." id a10_cou1_04_2388e125
    else:
        "—After class. The four girls were getting ready to go home."

    play sound se_lime
    pause 0.5

    show fumi z4 2 lg school g:
        xcenter 118
    show miyako z4 1 lg school_a e behind fumi, hina:
        xcenter 383
    show hina z4 1 lg school k:
        xcenter 641
    show rin z4 1 lg school a:
        xcenter 906
    with dict_dissolve_25

    voice "2HI_1211"
    hina "\"Is that you, Fumi?\""

    play music bgm01 fadein 1.0

    show fumi:
        "fumi z4 2 lg school h" with Dissolve(0.25)
        ShakeYes

    "Fumi took her phone out of her bag at Hina's prompt."

    show fumi z4 2 lg school h:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_0959"
    fumi "\"You're right. It's my mom. I wonder what it is. Something about the store?\""

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_1244"
    rin "\"Well, it's the big day tomorrow. Hm. But is it actually busy on Valentine's Day? You usually buy things before, right?\""

    show fumi z4 1 lg school a with dict_dissolve_25

    voice "2FU_0960"
    fumi "\"True, the peak day is the Sunday before, but it's still a lot more busy than usual on the day of.\""

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1245"
    rin "\"I see. The last-minute rush—\""

    show fumi z4 1 lg school k with dict_dissolve_25

    voice "2FU_0961"
    fumi "\"Huh?\""

    "Fumi exclaimed, a grave look on her face."

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1212"
    hina "\"What is it?\""

    show fumi z4 1 lg school h with dict_dissolve_25

    stop music fadeout 1.0

    voice "2FU_0962"
    fumi "\"My mother collapsed with a fever.\""

    show miyako z4 1 lg school_a f
    show hina z4 1 lg school d
    show rin z4 1 lg school e
    with dict_dissolve_25

    voice "2HI_1213"
    hina "\"What?! Is she in the hospital?\""

    show fumi z4 1 lg school d with dict_dissolve_25

    voice "2FU_0963"
    fumi "\"No, I don't think it's that serious. I mean, she's sending me messages on LIME... haha.\""

    "Her smile was strained. She must have been worried."

    play music bgm05 fadein 1.0

    show miyako z4 1 lg school_a i
    show hina z4 1 lg school n
    with dict_dissolve_25
    show hina:
        "hina z4 1 lg school n" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_1214"
    hina "\"It must be overwork.\""

    show hina z4 1 lg school n:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_0964"
    fumi "\"I think so, too. They've been so busy all the time lately.\""

    "The two who had actually witnessed her mother working exchanged a glance."

    show rin z4 2 lg school a with dict_dissolve_25

    voice "2RI_1246"
    rin "\"What are you gonna do about the store? You just said it'd be busy, right?\""

    "Her father alone would definitely not be able to handle it."

    show fumi z4 2 lg school a with dict_dissolve_25

    voice "2FU_0965"
    fumi "\"I... I think I'll go to the store tomorrow.\""

    show miyako z4 1 lg school_a e
    show hina z4 1 lg school k
    show rin z4 2 lg school g
    with dict_dissolve_25

    voice "2RI_1247"
    if persistent.dpatch:
        rin "\"You mean you'll skip school?\"" id a10_cou1_04_01973fed
    else:
        rin "\"You mean you'll skip class?\""

    show fumi:
        ShakeYes

    "Fumi nodded."

    show fumi:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_0992"
    miyako "\"Would you like me to take notes for you?\""

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_0966"
    fumi "\"Oh! You wouldn't mind, Miyako?\""

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_0993"
    miyako "\"I don't think mine will be as helpful as yours, of course.\""

    show fumi z4 2 lg school c with dict_dissolve_25

    voice "2FU_0967"
    fumi "\"That's not true!\""

    show hina:
        "hina z4 1 lg school a" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1215"
    hina "\"Oh, I'll go help out.\""

    show hina z4 1 lg school a:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school e with dict_dissolve_25

    voice "2FU_0968"
    fumi "\"Huh?\""

    "Fumi turned around, surprised at Hina's sudden declaration."

    show hina z4 1 lg school p with dict_dissolve_25

    voice "2HI_1216"
    hina "\"I just texted my dad, and he said it was okay.\""

    "Hina said, holding up her phone."

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1248"
    rin "\"You act fast!\""

    show fumi:
        "fumi z4 1 lg school k" with Dissolve(0.25)
        ShakeNo

    voice "2FU_0969"
    fumi "\"Well, but, I... That'll help... but...\""

    show fumi z4 1 lg school k:
        xoffset 0 yoffset 0
    with None

    if persistent.dpatch:
        "Fumi didn't seem to want Hina missing school." id a10_cou1_04_f7a662e4
    else:
        "Fumi didn't seem to want Hina missing class."

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_1217"
    hina "\"I know how busy you guys have been. You won't be able to handle it on your own, Fumi. And you can't close the store, right?\""

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_0970"
    fumi "\"...Right.\""

    "Partly for business reasons, of course, but also because they knew how girls felt on Valentine's."

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_1218"
    if persistent.dpatch:
        hina "\"It's okay. I got permission from a parent. He said he didn't care if I skipped a day of school and that I should go and help.\"" id a10_cou1_04_85d7ed0a
    else:
        hina "\"It's okay. I got permission from a parent. He said he didn't care if I skipped a day of class and that I should go and help.\""

    show fumi z4 1 lg school k with dict_dissolve_25

    voice "2FU_0971"
    fumi "\"......\""

    "Fumi's face clouded over when she heard what Hina's father had told her."

    "Because of the message from her own father, she was probably feeling doubly bad about having Hina help them."

    show hina z4 1 lg school p with dict_dissolve_25

    voice "2HI_1219"
    hina "\"He'd be mad at me if he knew someone important to me was in trouble and I didn't do anything about it.\""

    "Maybe Hina gets her chivalry from her father."

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1249"
    rin "\"Okay, I'll go too.\""

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_1220"
    hina "\"You wouldn't be any help, so you don't need to come.\""

    show rin:
        "rin z4 1 lg school j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1250"
    rin "\"Rude!\""

    show rin z4 1 lg school j with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared >= 2:
        jump a10_cou4_01
    else:
        jump a10_cou1_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
