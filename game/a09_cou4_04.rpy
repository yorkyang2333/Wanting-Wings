label a09_cou4_04:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play music bgm05

    play sound se_2s_f014
    pause 0.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0791"
    sachiko "\"Welc—\""

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
    miyako "\"Hahh... hahh...\""

    show miyako:
        xoffset 0 yoffset 0
    with None
    "...and found an out-of-breath Miyako in front of her."

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0792"
    sachiko "\"Just you?\""

    show miyako z4 1 lg school_a j with dict_dissolve_25

    voice "2MI_0964"
    miyako "\"...Yes.\""

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0793"
    sachiko "\"You must have been in a real hurry. Do you even have your bag...?\""

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
    miyako "\"I had a feeling you were going to go somewhere.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0794"
    sachiko "\"Well, yeah, I'm kinda going out right now.\""

    "She tapped the tip of her sneaker on the floor."

    voice "2MI_0966"
    miyako "\"I found this in the broadcasting room.\""

    "Miyako held out the club journal."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0795"
    sachiko "\"Ah... The one with Noel's picture in it.\""

    "She could tell just by giving the cover a glance."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0796"
    sachiko "\"But you knew her name and that she used to be a student here already, right? There's nothing to be surprised—\""

    show miyako z4 1 lg school_a i with dict_dissolve_25

    voice "2MI_0967"
    miyako "\"I realized what you meant when you said... that she's somewhere far away now.\""

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0797"
    sachiko "\"......\""

    "There was a long stretch of silence. Miyako waited for the words Sachiko was searching for."

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0798"
    sachiko "\"...How did you figure that out?\""

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_0968"
    miyako "\"I heard from Hina. She told me a story about how her sister's friend's friend was praying for a friend in the hospital when an angel appeared before her.\""

    voice "2SA_0799"
    sachiko "\"A friend of a friend, huh... That's confusing. Is that true?\""

    show miyako z4 2 lg school f with dict_dissolve_25

    voice "2MI_0969"
    miyako "\"The friend in the hospital was Noel... and the angel was you, I'm guessing.\""

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0800"
    sachiko "\"......\""

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_0970"
    miyako "\"I heard that Noel passed away after that.\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0801"
    sachiko "\"...A month after, to be specific.\""

    voice "2MI_0971"
    miyako "\"......\""

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0802"
    if persistent.dpatch:
        sachiko "\"Noel was always in poor health and would sometimes spend time hospitalized in the city while she was in school. That must have been where you saw her.\"" id a09_cou4_04_d5c5943f
    else:
        sachiko "\"Noel was always in poor health and would sometimes spend time hospitalized in the city while she was enrolled. That must have been where you saw her.\""

    show miyako z4 1 lg school_a l with dict_dissolve_25

    voice "2MI_0972"
    miyako "\"I'm sorry...\""

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0803"
    sachiko "\"What do you have to be sorry about?\""

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_0973"
    miyako "\"I didn't know any of this, and never thought about what I was doing...\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0804"
    sachiko "\"Of course you didn't know. It's not like you picked that face to torment me, right?\""

    "Miyako shook her head."

    show miyako z4 2 lg school e with dict_dissolve_25

    voice "2MI_0974"
    miyako "\"You were trying to forget her, and I...\""

    "This time, Sachiko shook her head. Then she smiled sadly and said:"

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0805"
    sachiko "\"No... I don't want to forget her.\""

    show miyako z4 2 lg school f with dict_dissolve_25

    voice "2MI_0975"
    miyako "\"...Oh.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0806"
    sachiko "\"I'm planning on leaving here sometime soon.\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_0976"
    miyako "\"Huh...?\""

    voice "2SA_0807"
    sachiko "\"I was only taking over for the original manager here while she was sick, but she's gotten better now, so I thought this might be the right time.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0808"
    sachiko "\"Oh, but keep that a secret from the other three, would you? You've got good instincts, though. I was kinda surprised when you said you thought I was gonna go somewhere earlier.\""

    show miyako z4 1 lg school_a k with dict_dissolve_25

    voice "2MI_0977"
    miyako "\"I-If it's because of me, I'll leave!\""

    "Miyako stood in Sachiko's path. She backed up and blocked the door."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0809"
    sachiko "\"You can't do that. It's my choice whether I stay or leave.\""

    show miyako z4 1 lg school_a j with dict_dissolve_25

    voice "2MI_0978"
    miyako "\"Then I'll wait until you come back...\""

    "Sachiko smiled awkwardly and shook her head."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0810"
    sachiko "\"A pretty girl like you'll find someone else right away. No need to—\""

    show miyako z4 2 lg school e with dict_dissolve_25

    voice "2MI_0979"
    miyako "\"...That's not fair.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0811"
    sachiko "\"...Guess not.\""

    hide bg_obi
    hide sachiko
    hide miyako
    with dict_dissolve_50

    "Sachiko put a hand on Miyako's shoulder and gently moved her away from the door."

    $ side_image = "miyako 2 side school f"

    voice "2MI_0980"
    miyako "\"You'll come back, right?\""

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0812"
    sachiko "\"Well, I haven't packed yet~\""

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
    rin "\"We're ba... oh, you came home, Mikoyan.\""

    show hina 2 sm school_scarf a:
        alpha 1.0 xcenter 582
    show rin 2 sm school_scarf a behind hina, fumi:
        alpha 1.0 xcenter 756
    show fumi 1 sm school_scarf c:
        alpha 1.0 xcenter 940
    with None
    show miyako 2 sm school b at pos_l2 with dict_dissolve_25

    voice "2MI_0981"
    miyako "\"W-Welcome back...\""

    show hina 2 sm school_scarf f with dict_dissolve_25

    voice "2HI_1185"
    hina "\"You surprised us, running out like that.\""

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_1229"
    rin "\"We worried you might have been possessed by something. Well, Hina did.\""

    show miyako 2 sm school f with dict_dissolve_25

    voice "2MI_0982"
    miyako "\"Umm, I'm fine.\""

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "2FU_0935"
    fumi "\"Here, you forgot your bag.\""

    show miyako:
        "miyako 2 sm school c" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0983"
    miyako "\"Oh, I'm sorry. Thank you.\""

    show miyako 2 sm school c:
        xoffset 0 yoffset 0
    with None

    "Miyako took the bag and bowed her head."

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "2FU_0936"
    fumi "\"We just went past Sachiko. Did you see her?\""

    show miyako 2 sm school d with dict_dissolve_25

    voice "2MI_0984"
    miyako "\"Yes...\""

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
