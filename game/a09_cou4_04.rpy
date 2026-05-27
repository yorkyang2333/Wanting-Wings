label a09_cou4_04:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play music bgm05

    play sound se_2s_f014
    pause 0.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0791"
    sachiko "\"Welc—\"" id a09_cou4_04_873a0cc7

    "Sachiko looked up at the violent sound the door made when it opened..."

    show bg_obi
    show miyako z4 1 lg school_a k:
        xcenter 726
    with Dissolve(0.5)

    show miyako:
        ShakeTameiki
        0.3
        ShakeTameiki

    voice "2MI_0963"
    miyako "\"Hahh... hahh...\"" id a09_cou4_04_f60d5253

    show miyako:
        xoffset 0 yoffset 0
    with None
    "...and found an out-of-breath Miyako in front of her."

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0792"
    sachiko "\"Just you?\"" id a09_cou4_04_da5bf640

    show miyako z4 1 lg school_a j with dict_dissolve_25

    voice "2MI_0964"
    miyako "\"...Yes.\"" id a09_cou4_04_a49a7e6c

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0793"
    sachiko "\"You must have been in a real hurry. Do you even have your bag...?\"" id a09_cou4_04_e59d76b2

    pause 0.5

    show sachiko:
        "sachiko z4 1 lg outfit i flat"
        alpha 0.0 xcenter 298 ycenter 873
        easein 0.75 alpha 1.0 ycenter 773
    pause 0.75

    show sachiko z4 1 lg outfit i:
        alpha 1.0 xcenter 298 ycenter 773
    with None

    "She finished tying her shoelaces and stood up."

    voice "2MI_0965"
    miyako "\"I had a feeling you were going to go somewhere.\"" id a09_cou4_04_48ab8fed

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0794"
    sachiko "\"Well, yeah, I'm kinda going out right now.\"" id a09_cou4_04_e2f17acb

    "She tapped the tip of her sneaker on the floor."

    voice "2MI_0966"
    miyako "\"I found this in the broadcasting room.\"" id a09_cou4_04_3af47747

    "Miyako held out the club journal."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0795"
    sachiko "\"Ah... The one with Noel's picture in it.\"" id a09_cou4_04_7115b7d6

    "She could tell just by giving the cover a glance."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0796"
    sachiko "\"But you knew her name and that she used to be a student here already, right? There's nothing to be surprised—\"" id a09_cou4_04_c669fd04

    show miyako z4 1 lg school_a i with dict_dissolve_25

    voice "2MI_0967"
    miyako "\"I realized what you meant when you said... that she's somewhere far away now.\"" id a09_cou4_04_21988877

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0797"
    sachiko "\"......\"" id a09_cou4_04_481c5539

    "There was a long stretch of silence. Miyako waited for the words Sachiko was searching for."

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0798"
    sachiko "\"...How did you figure that out?\"" id a09_cou4_04_47564fb1

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_0968"
    miyako "\"I heard from Hina. She told me a story about how her sister's friend's friend was praying for a friend in the hospital when an angel appeared before her.\"" id a09_cou4_04_d445ea0a

    voice "2SA_0799"
    sachiko "\"A friend of a friend, huh... That's confusing. Is that true?\"" id a09_cou4_04_f62076ff

    show miyako z4 2 lg school f with dict_dissolve_25

    voice "2MI_0969"
    miyako "\"The friend in the hospital was Noel... and the angel was you, I'm guessing.\"" id a09_cou4_04_a88ae45d

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0800"
    sachiko "\"......\"" id a09_cou4_04_adf5c301

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_0970"
    miyako "\"I heard that Noel passed away after that.\"" id a09_cou4_04_6ec91b8d

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0801"
    sachiko "\"...A month after, to be specific.\"" id a09_cou4_04_2874cbbb

    voice "2MI_0971"
    miyako "\"......\"" id a09_cou4_04_c6d4df02

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0802"
    if persistent.dpatch:
        sachiko "\"Noel was always in poor health and would sometimes spend time hospitalized in the city while she was in school. That must have been where you saw her.\"" id a09_cou4_04_d5c5943f
    else:
        sachiko "\"Noel was always in poor health and would sometimes spend time hospitalized in the city while she was enrolled. That must have been where you saw her.\"" id a09_cou4_04_e04dac83

    show miyako z4 1 lg school_a l with dict_dissolve_25

    voice "2MI_0972"
    miyako "\"I'm sorry...\"" id a09_cou4_04_7a991d8a

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0803"
    sachiko "\"What do you have to be sorry about?\"" id a09_cou4_04_9931044d

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_0973"
    miyako "\"I didn't know any of this, and never thought about what I was doing...\"" id a09_cou4_04_6de69ef9

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0804"
    sachiko "\"Of course you didn't know. It's not like you picked that face to torment me, right?\"" id a09_cou4_04_57378546

    "Miyako shook her head."

    show miyako z4 2 lg school e with dict_dissolve_25

    voice "2MI_0974"
    miyako "\"You were trying to forget her, and I...\"" id a09_cou4_04_64aa4b46

    "This time, Sachiko shook her head. Then she smiled sadly and said:"

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0805"
    sachiko "\"No... I don't want to forget her.\"" id a09_cou4_04_e569f3f8

    show miyako z4 2 lg school f with dict_dissolve_25

    voice "2MI_0975"
    miyako "\"...Oh.\"" id a09_cou4_04_9b252861

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0806"
    sachiko "\"I'm planning on leaving here sometime soon.\"" id a09_cou4_04_0a068c86

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0976"
    miyako "\"Huh...?\"" id a09_cou4_04_4a68d866

    voice "2SA_0807"
    sachiko "\"I was only taking over for the original manager here while she was sick, but she's gotten better now, so I thought this might be the right time.\"" id a09_cou4_04_d806a881

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0808"
    sachiko "\"Oh, but keep that a secret from the other three, would you? You've got good instincts, though. I was kinda surprised when you said you thought I was gonna go somewhere earlier.\"" id a09_cou4_04_a2ed148a

    show miyako z4 1 lg school_a k with dict_dissolve_25

    voice "2MI_0977"
    miyako "\"I-If it's because of me, I'll leave!\"" id a09_cou4_04_6c6a49c9

    "Miyako stood in Sachiko's path. She backed up and blocked the door."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0809"
    sachiko "\"You can't do that. It's my choice whether I stay or leave.\"" id a09_cou4_04_0471fdbe

    show miyako z4 1 lg school_a j with dict_dissolve_25

    voice "2MI_0978"
    miyako "\"Then I'll wait until you come back...\"" id a09_cou4_04_c932c3f4

    "Sachiko smiled awkwardly and shook her head."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0810"
    sachiko "\"A pretty girl like you'll find someone else right away. No need to—\"" id a09_cou4_04_d65ea385

    show miyako z4 2 lg school e with dict_dissolve_25

    voice "2MI_0979"
    miyako "\"...That's not fair.\"" id a09_cou4_04_90058166

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0811"
    sachiko "\"...Guess not.\"" id a09_cou4_04_f9d4d255

    hide bg_obi
    hide sachiko
    hide miyako
    with dict_dissolve_50

    "Sachiko put a hand on Miyako's shoulder and gently moved her away from the door."

    $ side_image = "miyako 2 side school f"

    voice "2MI_0980"
    miyako "\"You'll come back, right?\"" id a09_cou4_04_e8c43778

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0812"
    sachiko "\"Well, I haven't packed yet~\"" id a09_cou4_04_bc02c231

    scene black with Dissolve(1.5)
    pause 0.5

    "Sachiko showed her empty hands and walked out. Miyako was left standing there alone."

    window hide

    stop music fadeout 1.0

    pause 1.0

    scene bg05ba with bg_effect_05

    play music bgm02

    play sound se521
    pause 1.0

    show hina:
        "hina 2 sm school_scarf a flat"
        alpha 0.0 xcenter 682
        easein 0.75 alpha 1.0 xcenter 582
    show rin behind hina, fumi:
        "rin 2 sm school_scarf a flat"
        alpha 0.0 xcenter 856
        easein 0.75 alpha 1.0 xcenter 756
    show fumi:
        "fumi 1 sm school_scarf c flat"
        alpha 0.0 xcenter 1040
        easein 0.75 alpha 1.0 xcenter 940

    window auto

    voice "2RI_1228"
    rin "\"We're ba... oh, you came home, Mikoyan.\"" id a09_cou4_04_1a6c1014

    show hina 2 sm school_scarf a:
        alpha 1.0 xcenter 582
    show rin 2 sm school_scarf a behind hina, fumi:
        alpha 1.0 xcenter 756
    show fumi 1 sm school_scarf c:
        alpha 1.0 xcenter 940
    with None
    show miyako 2 sm school b at pos_l2 with dict_dissolve_25

    voice "2MI_0981"
    miyako "\"W-Welcome back...\"" id a09_cou4_04_eb3ac5f7

    show hina 2 sm school_scarf f with dict_dissolve_25

    voice "2HI_1185"
    hina "\"You surprised us, running out like that.\"" id a09_cou4_04_49926c1b

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_1229"
    rin "\"We worried you might have been possessed by something. Well, Hina did.\"" id a09_cou4_04_bebe7a7f

    show miyako 2 sm school f with dict_dissolve_25

    voice "2MI_0982"
    miyako "\"Umm, I'm fine.\"" id a09_cou4_04_22258291

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "2FU_0935"
    fumi "\"Here, you forgot your bag.\"" id a09_cou4_04_17efdf2e

    show miyako:
        "miyako 2 sm school c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0983"
    miyako "\"Oh, I'm sorry. Thank you.\"" id a09_cou4_04_c3c8d511

    show miyako 2 sm school c:
        xoffset 0 yoffset 0
    with None

    "Miyako took the bag and bowed her head."

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0936"
    fumi "\"We just went past Sachiko. Did you see her?\"" id a09_cou4_04_f1d615dc

    show miyako 2 sm school d with dict_dissolve_25

    voice "2MI_0984"
    miyako "\"Yes...\"" id a09_cou4_04_9d4006b0

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a09_cou1_06
    elif route2 == 2:
        jump a09_cou2_07
    elif route2 == 3:
        jump a09_cou3_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
