label a10_cou1_06:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    "Rin and Miyako were alone in the room."

    "Fumi had come back with Miyako, but when she heard that Hina was on the roof, she'd turned right back around and left."

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_1281"
    rin "\"Mikoyan, were you talking to Asou about something?\"" id a10_cou1_06_d25f23df

    "Rin had changed and was sitting in bed in her pajamas."

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_1016"
    miyako "\"Yes, a little. Why do you ask?\"" id a10_cou1_06_8f6ab8ac

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_1282"
    rin "\"'Cause she looked a little more cheerful.\"" id a10_cou1_06_2cdf501c

    "Miyako smiled as she took off her scarf."

    $ side_image = "rin 1 side pyjama c"

    voice "2RI_1283"
    rin "\"Thanks.\"" id a10_cou1_06_caaab709

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_1017"
    miyako "\"Hm? Why are you thanking me?\"" id a10_cou1_06_f7bb48ee

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_1284"
    rin "\"Those two are keeping me alive, so I'll be in trouble if they're not happy. I might die.\"" id a10_cou1_06_02eb151d

    show miyako 1 lg school_a g with dict_dissolve_25

    voice "2MI_1018"
    miyako "\"Y-You'll die?\"" id a10_cou1_06_0eaa3bd1

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_1285"
    rin "\"I'm exaggerating, but I'll really be in trouble.\"" id a10_cou1_06_cf6f73a8

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_1019"
    miyako "\"You said something like that before, too. That they were your hope.\"" id a10_cou1_06_4f4f5ee4

    $ side_image = "rin 2 side pyjama d"

    voice "2RI_1286"
    rin "\"Yeah. I was really twisted before I started living with them... Like, I think I was pretty terrible.\"" id a10_cou1_06_3c4641cd

    show miyako 1 lg school_b c with dict_dissolve_25

    voice "2MI_1020"
    miyako "\"'I'm not great in groups'... right?\"" id a10_cou1_06_f84e5434

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_1287"
    rin "\"...Mikoyan.\"" id a10_cou1_06_9d74a7d8

    "Even after all the ribbing, it seemed the phrase still did damage."

    $ side_image = "rin 1 side pyjama c"

    voice "2RI_1288"
    rin "\"But because of them, I was able to start liking people. To start being honest.\"" id a10_cou1_06_401d367d

    show miyako 1 lg school_b e with dict_dissolve_25

    voice "2MI_1021"
    miyako "\"Being honest?\"" id a10_cou1_06_276b50cd

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_1289"
    rin "\"To start... working on being honest.\"" id a10_cou1_06_26a82d78

    show miyako 1 lg school_a d with dict_dissolve_25

    voice "2MI_1022"
    miyako "\"Ahaha, you are, you are.\"" id a10_cou1_06_3bad1d69

    $ side_image = "rin 1 side pyjama i"

    voice "2RI_1290"
    rin "\"Anyway.\"" id a10_cou1_06_11a1fa78

    show miyako:
        "miyako 1 lg school_a b" with Dissolve(0.25)
        ShakeYes

    "Miyako nodded."

    show miyako 1 lg school_a b:
        xoffset 0 yoffset 0
    with None
    show miyako 1 lg school_a h with dict_dissolve_25

    $ side_image = "rin 1 side pyjama c"

    $ voice2("rin","2RI_1291","miyako","2MI_1023")
    rin_miyako "\"I want them both to be happy.\""

    pause 0.5

    scene white with Dissolve(1.0)
    pause 1.5

    scene bg08ba with Dissolve(2.0)
    pause 0.5

    play sound se521
    pause 0.5

    "—The roof."

    $ side_image = "hina 2 side school_scarf f"

    voice "2HI_1245"
    hina "\"...Fumi?\"" id a10_cou1_06_3d9aeb2c

    $ side_image = "fumi 2 side school_scarf b"

    voice "2FU_0992"
    fumi "\"I heard you were up here.\"" id a10_cou1_06_773944b0

    scene bg07bb with Dissolve(1.5)

    "The two stood silently, their backs against the fence."

    "But the air between them had become a little lighter, and they both seemed to feel it."

    show fumi 2 lg school_scarf b at pos_l
    show hina 2 lg school_scarf f at pos_r
    with dict_dissolve_25

    voice "2HI_1246"
    hina "\"Fumi?\"" id a10_cou1_06_b6d9d5f7

    show fumi 2 lg school_scarf g with dict_dissolve_25

    voice "2FU_0993"
    fumi "\"Yes?\"" id a10_cou1_06_a19aeaba

    "Hina was the first to speak."

    show hina 2 lg school_scarf c with dict_dissolve_25

    voice "2HI_1247"
    hina "\"Before, Rin was yelling at me about us.\"" id a10_cou1_06_89e53c79

    show fumi 2 lg school_scarf d with dict_dissolve_25

    voice "2FU_0994"
    fumi "\"Huh?! Did we do something?\"" id a10_cou1_06_5415d3ad

    show hina 2 lg school_scarf b with dict_dissolve_25

    voice "2HI_1248"
    hina "\"Eheh, she was yelling, but... like, encouraging yelling.\"" id a10_cou1_06_13259be0

    show fumi 2 lg school_scarf h with dict_dissolve_25

    "Hina told Fumi what Rin had said to her."

    "That loving someone was natural, that no one had the right to decide it was unnatural, and all the rest..."

    show hina 2 lg school_scarf g with dict_dissolve_25

    voice "2HI_1249"
    hina "\"She got more worked up about it than I thought she was capable of getting, and told me this whole list of countries that have same-sex marriage. It was like a tongue twister, it was amazing.\"" id a10_cou1_06_ac0392bd

    show fumi 1 lg school_scarf b with dict_dissolve_25

    voice "2FU_0995"
    fumi "\"I'm touched she looked all that up for us.\"" id a10_cou1_06_a94c23ef

    show hina 2 lg school_scarf a with dict_dissolve_25

    voice "2HI_1250"
    hina "\"She also said her tongue would be her sword, and she'll defeat anyone who doesn't accept us.\"" id a10_cou1_06_2e51ab55

    show fumi 1 lg school_scarf a with dict_dissolve_25

    voice "2FU_0996"
    fumi "\"Oh... so Ogata is a sword.\"" id a10_cou1_06_279ea2ca

    show hina 2 lg school_scarf f with dict_dissolve_25

    voice "2HI_1251"
    hina "\"Hm?\"" id a10_cou1_06_6e6e5a17

    show fumi 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_0997"
    fumi "\"Miyako had some words of encouragement for me, too.\"" id a10_cou1_06_20d83bab

    show hina 1 lg school_scarf k with dict_dissolve_25

    voice "2HI_1252"
    hina "\"Huh? She did?\"" id a10_cou1_06_889762f7

    show fumi 2 lg school_scarf i with dict_dissolve_25

    voice "2FU_0998"
    fumi "\"And she said she'd be our shield.\"" id a10_cou1_06_8ff29193

    show hina 1 lg school_scarf p with dict_dissolve_25

    voice "2HI_1253"
    hina "\"So Rin will be a sword and Miyako will be a shield! We'll be unstoppable!\"" id a10_cou1_06_9cf03486

    show fumi 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_0999"
    fumi "\"Yeah. ...I told her I was feeling guilty, and she asked me what I thought we were doing wrong, but I couldn't answer.\"" id a10_cou1_06_32f930d8

    show hina 2 lg school_scarf d with dict_dissolve_25

    voice "2HI_1254"
    hina "\"Mm...\"" id a10_cou1_06_9b38edd6

    show fumi 2 lg school_scarf i with dict_dissolve_25

    voice "2FU_1000"
    fumi "\"She said loving someone isn't a crime, and nothing can part us other than our feelings.\"" id a10_cou1_06_81453396

    show hina 2 lg school_scarf c with dict_dissolve_25

    voice "2HI_1255"
    hina "\"...Yeah. It's something we have to decide, isn't it? But we have people on our side. Rin and Miyako...\"" id a10_cou1_06_0cf5628b

    show fumi 1 lg school_scarf b with dict_dissolve_25

    voice "2FU_1001"
    fumi "\"Miyako said Sachiko would be, too.\"" id a10_cou1_06_740433b3

    show hina:
        ShakeYes

    "Hina nodded."

    show hina 2 lg school_scarf d:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2HI_1256"
    hina "\"Rin mentioned the chapel to me.\"" id a10_cou1_06_e1f3b04f

    show fumi 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_1002"
    fumi "\"So did Miyako.\"" id a10_cou1_06_a1218598

    show hina 2 lg school_scarf a with dict_dissolve_25

    voice "2HI_1257"
    hina "\"We swore to the angel, didn't we...?\"" id a10_cou1_06_79d95881

    show fumi 2 lg school_scarf c
    show hina 2 lg school_scarf g
    with dict_dissolve_25

    $ voice2("hina","2HI_1258N","fumi","2FU_1003")
    hina_fumi "\"We'll keep loving each other until we're old and grey, and cherish each other forever.\""

    show hina 2 lg school_scarf a with dict_dissolve_25

    voice "2HI_1259"
    hina "\"Do you still feel the same way?\"" id a10_cou1_06_f5e67796

    show fumi:
        "fumi 2 lg school_scarf i" with Dissolve(0.25)
        ShakeYes

    voice "2FU_1004"
    fumi "\"I do.\"" id a10_cou1_06_a65a7e85

    show fumi 2 lg school_scarf i:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school_scarf c with dict_dissolve_25

    voice "2HI_1260"
    hina "\"We have to uphold our vows. But we'll be invincible after this, won't we?\"" id a10_cou1_06_ba1245ad

    show fumi 2 lg school_scarf b with dict_dissolve_25

    voice "2FU_1005"
    fumi "\"Yes.\"" id a10_cou1_06_d07bd672

    "They squeezed one another's hands."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
