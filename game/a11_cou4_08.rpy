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
    sachiko "\"......\"" id a11_cou4_08_35a37341

    "Sachiko was stuffing canvases into cardboard boxes."

    "She picked up the canvas that had Noel's painting on it and stared at it."

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_1034"
    sachiko "\"I haven't forgotten.\"" id a11_cou4_08_731a1be3

    show sachiko 2 lg outfit c with dict_dissolve_25

    voice "2SA_1035"
    sachiko "\"But... are they really memories of Noel?\"" id a11_cou4_08_ca5559d9

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_1036"
    sachiko "\"When I look at this painting, do I see Noel, or...\"" id a11_cou4_08_2d8442da

    hide sachiko with dict_dissolve_50

    "She put the portrait away as if to escape its gaze."

    play sound se_2s_f001
    pause 1.0

    $ side_image = "hina 2 side school f"

    voice "2HI_1620"
    hina "\"Sachiko, you there?\"" id a11_cou4_08_434de965

    show sachiko 1 sm outfit a:
        xcenter 152
    with dict_dissolve_25

    voice "2SA_1037"
    sachiko "\"I am. Come in~\"" id a11_cou4_08_a77ae2d6

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
    hina "\"Here's the mail.\"" id a11_cou4_08_b623fa13

    voice "2SA_1038"
    sachiko "\"Thanks. Can you leave it on my desk?\"" id a11_cou4_08_2163a155

    voice "2FU_1307"
    fumi "\"Were you tidying up?\"" id a11_cou4_08_84100eb4

    "Fumi asked, seeing the boxes."

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_1039"
    sachiko "\"Yeah, I guess.\"" id a11_cou4_08_4efc7c77

    voice "2RI_1716"
    rin "\"I don't think there's enough stuff in here to tidy up, really.\"" id a11_cou4_08_7d47f380

    "That's true."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1040"
    sachiko "\"Oh, I know. Since you guys are here, do you want some clothes? I bought them four or five years ago. I don't think there's anything too bad in there.\"" id a11_cou4_08_ed870f1c

    show fumi 1 sm school c with dict_dissolve_25

    voice "2FU_1308"
    fumi "\"I'll look, I'll look~♪\"" id a11_cou4_08_7c0b716a

    hide rin
    hide fumi
    hide hina
    hide sachiko
    hide miyako
    with dict_dissolve_50

    "Fumi went straight to the clothes on the hangers to take a look."

    $ side_image = "fumi 2 side school g"

    voice "2FU_1309"
    fumi "\"Huh? These don't really look like things you'd wear.\"" id a11_cou4_08_dc4d4285

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_1041"
    sachiko "\"Yeah, it was kinda just trial and error, I guess? None of them ended up looking good on me. Everything over there I've pretty much never worn.\"" id a11_cou4_08_ba82df96

    $ side_image = "fumi 1 side school a"

    voice "2FU_1310"
    fumi "\"I see~\"" id a11_cou4_08_f1ed3352

    $ side_image = "rin 2 side school g"

    voice "2RI_1717"
    rin "\"Huh, this stuff doesn't look bad.\"" id a11_cou4_08_0a6d6673

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_1042"
    sachiko "\"You've got a good eye, rich kid.\"" id a11_cou4_08_536c0c47

    $ side_image = "miyako 2 side school a"

    voice "2MI_1153"
    miyako "\"Is Rin a rich kid?\"" id a11_cou4_08_0a3ea1ad

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_1043"
    sachiko "\"Oh, she actually wears brand-name stuff a lot. Her family's pretty wealthy, after all.\"" id a11_cou4_08_a34b0b3e

    $ side_image = "rin 1 side school i"

    voice "2RI_1718"
    rin "\"It's not my fault my family's wealthy.\"" id a11_cou4_08_63a202c5

    $ side_image = "miyako 2 side school a"

    voice "2MI_1154"
    miyako "\"But why are you suddenly getting rid of them? If you get rid of anything else...\"" id a11_cou4_08_2453a07f

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_1044"
    sachiko "\"I'll be able to travel lighter, right? I'm kinda wondering if I can get everything into one big bag, actually.\"" id a11_cou4_08_ebeb49f8

    $ side_image = "miyako 2 side school b"

    voice "2MI_1155"
    miyako "\"......\"" id a11_cou4_08_eecfba26

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
    fumi "\"Auuugh...\"" id a11_cou4_08_8dd61e59

    "An anguished moan."

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_1156"
    miyako "\"What is it?\"" id a11_cou4_08_42b41a55

    show fumi:
        "fumi 1 sm school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1312"
    fumi "\"I can't put this on. The bust is too tight~\"" id a11_cou4_08_26a67689

    show fumi 1 sm school k:
        xoffset 0 yoffset 0
    with None
    show miyako 1 sm school_a a with dict_dissolve_25

    voice "2MI_1157"
    miyako "\"Aah...\"" id a11_cou4_08_f7c4bb4c

    show hina 1 sm school h with dict_dissolve_25

    voice "2HI_1622"
    hina "\"...This is too big.\"" id a11_cou4_08_9e482bdf

    show rin 1 sm school b with dict_dissolve_25

    voice "2RI_1719"
    rin "\"Then they'd probably be too short for me.\"" id a11_cou4_08_74fd1cae

    "They're like \"Goldilocks and the Three Bears.\" Just without the baby bear."

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "2SA_1045"
    sachiko "\"Ah...\"" id a11_cou4_08_abbfbfcb

    show fumi 1 sm school h with dict_dissolve_25

    voice "2FU_1313"
    fumi "\"It's too bad, but...\"" id a11_cou4_08_db3e155c

    show rin 1 sm school a with dict_dissolve_25

    voice "2RI_1720"
    rin "\"Wouldn't they fit Mikoyan pretty well, though? They might still be a little tight in the chest, but...\"" id a11_cou4_08_9ffc911d

    show miyako 1 sm school_a e with dict_dissolve_25

    voice "2MI_1158"
    miyako "\"I suppose so~\"" id a11_cou4_08_d67a0c55

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
    rin "\"Oh? Looks perfect.\"" id a11_cou4_08_89ee9a16

    "Well, there's the baby bear."

    voice "2FU_1314"
    fumi "\"And it really suits you, too!\"" id a11_cou4_08_167c83ec

    voice "2HI_1623"
    hina "\"It's like you bought this stuff for Miyako.\"" id a11_cou4_08_0626822b

    "...Well, I guess she did."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_1046"
    sachiko "\"You can have 'em. It'll at least give you more stuff to wear.\"" id a11_cou4_08_70dd62b4

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_1159"
    miyako "\"Are you sure? You just gave me a scarf, too.\"" id a11_cou4_08_5e90e768

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_1047"
    sachiko "\"Yeah, just take 'em. It's better if somebody who looks good in them wears them.\"" id a11_cou4_08_63ded442

    show miyako 2 sm school c with dict_dissolve_25

    voice "2MI_1160"
    miyako "\"...Thanks.\"" id a11_cou4_08_41ae92aa

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
