label a11_cou4_08:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_08:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09aa with Dissolve(0.25)
    pause 0.75

    play music bgm05 fadein 1.0

    show sachiko 2 lg outfit c with Dissolve(0.25)

    voice "2SA_1033"
    sachiko "\"......\""

    "Sachiko was stuffing canvases into cardboard boxes."

    "She picked up the canvas that had Noel's painting on it and stared at it."

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_1034"
    sachiko "\"I haven't forgotten.\""

    show sachiko 2 lg outfit c with dict_dissolve_25

    voice "2SA_1035"
    sachiko "\"But... are they really memories of Noel?\""

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_1036"
    sachiko "\"When I look at this painting, do I see Noel, or...\""

    hide sachiko with dict_dissolve_50

    "She put the portrait away as if to escape its gaze."

    play sound se_2s_f001
    pause 1.0

    $ side_image = "hina 2 side school f"

    voice "2HI_1620"
    hina "\"Sachiko, you there?\""

    show sachiko 1 sm outfit a:
        xcenter 152
    with dict_dissolve_25

    voice "2SA_1037"
    sachiko "\"I am. Come in~\""

    play sound se521
    pause 1.0

    show miyako 1 sm school_a a:
        xcenter 452
    show hina 2 sm school a:
        xcenter 632
    show rin 1 sm school a behind hina, fumi:
        xcenter 776
    show fumi 1 sm school a:
        xcenter 940
    with Dissolve(0.25)

    "The four peeked into the room after they got home."

    voice "2HI_1621"
    hina "\"Here's the mail.\""

    voice "2SA_1038"
    sachiko "\"Thanks. Can you leave it on my desk?\""

    voice "2FU_1307"
    fumi "\"Were you tidying up?\""

    "Fumi asked, seeing the boxes."

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_1039"
    sachiko "\"Yeah, I guess.\""

    voice "2RI_1716"
    rin "\"I don't think there's enough stuff in here to tidy up, really.\""

    "That's true."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1040"
    sachiko "\"Oh, I know. Since you guys are here, do you want some clothes? I bought them four or five years ago. I don't think there's anything too bad in there.\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "2FU_1308"
    fumi "\"I'll look, I'll look~♪\""

    hide rin
    hide fumi
    hide hina
    hide sachiko
    hide miyako
    with dict_dissolve_50

    "Fumi went straight to the clothes on the hangers to take a look."

    $ side_image = "fumi 2 side school g"

    voice "2FU_1309"
    fumi "\"Huh? These don't really look like things you'd wear.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_1041"
    sachiko "\"Yeah, it was kinda just trial and error, I guess? None of them ended up looking good on me. Everything over there I've pretty much never worn.\""

    $ side_image = "fumi 1 side school a"

    voice "2FU_1310"
    fumi "\"I see~\""

    $ side_image = "rin 2 side school g"

    voice "2RI_1717"
    rin "\"Huh, this stuff doesn't look bad.\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_1042"
    sachiko "\"You've got a good eye, rich kid.\""

    $ side_image = "miyako 2 side school a"

    voice "2MI_1153"
    miyako "\"Is Rin a rich kid?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_1043"
    sachiko "\"Oh, she actually wears brand-name stuff a lot. Her family's pretty wealthy, after all.\""

    $ side_image = "rin 1 side school i"

    voice "2RI_1718"
    rin "\"It's not my fault my family's wealthy.\""

    $ side_image = "miyako 2 side school a"

    voice "2MI_1154"
    miyako "\"But why are you suddenly getting rid of them? If you get rid of anything else...\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_1044"
    sachiko "\"I'll be able to travel lighter, right? I'm kinda wondering if I can get everything into one big bag, actually.\""

    $ side_image = "miyako 2 side school b"

    voice "2MI_1155"
    miyako "\"......\""

    hide sachiko with Dissolve(0.25)

    show sachiko 1 sm outfit a:
        xcenter 152
    show miyako 2 sm school b:
        xcenter 452
    show hina 1 sm school n:
        xcenter 632
    show rin 1 sm school a behind hina, fumi:
        xcenter 776
    show fumi 1 sm school h:
        xcenter 940
    with Dissolve(0.25)

    show fumi:
        ShakeNo_3_500

    voice "2FU_1311"
    fumi "\"Auuugh...\""

    "An anguished moan."

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_1156"
    miyako "\"What is it?\""

    show fumi:
        "fumi 1 sm school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1312"
    fumi "\"I can't put this on. The bust is too tight~\""

    show fumi 1 sm school k:
        xoffset 0 yoffset 0
    with None
    show miyako 1 sm school_a a with dict_dissolve_25

    voice "2MI_1157"
    miyako "\"Aah...\""

    show hina 1 sm school h with dict_dissolve_25

    voice "2HI_1622"
    hina "\"...This is too big.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "2RI_1719"
    rin "\"Then they'd probably be too short for me.\""

    "They're like \"Goldilocks and the Three Bears.\" Just without the baby bear."

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_1045"
    sachiko "\"Ah...\""

    show fumi 1 sm school h with dict_dissolve_25

    voice "2FU_1313"
    fumi "\"It's too bad, but...\""

    show rin 1 sm school a with dict_dissolve_25

    voice "2RI_1720"
    rin "\"Wouldn't they fit Mikoyan pretty well, though? They might still be a little tight in the chest, but...\""

    show miyako 1 sm school_a e with dict_dissolve_25

    voice "2MI_1158"
    miyako "\"I suppose so~\""

    show miyako:
        ShakeYes

    "Miyako put a shirt to her chest."

    show miyako:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school k
    show rin 1 sm school e
    show fumi 1 sm school b
    with dict_dissolve_25

    voice "2RI_1721"
    rin "\"Oh? Looks perfect.\""

    "Well, there's the baby bear."

    voice "2FU_1314"
    fumi "\"And it really suits you, too!\""

    voice "2HI_1623"
    hina "\"It's like you bought this stuff for Miyako.\""

    "...Well, I guess she did."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1046"
    sachiko "\"You can have 'em. It'll at least give you more stuff to wear.\""

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_1159"
    miyako "\"Are you sure? You just gave me a scarf, too.\""

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_1047"
    sachiko "\"Yeah, just take 'em. It's better if somebody who looks good in them wears them.\""

    show miyako 2 sm school c with dict_dissolve_25

    voice "2MI_1160"
    miyako "\"...Thanks.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
