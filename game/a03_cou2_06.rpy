label a03_cou2_06:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm05

    show rin 1 lg school b with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0713"
    rin "\"...Haah...\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin was leaning against a wall in the classroom, staring up at the ceiling. She looked faint, like she could sink to the floor at any moment."

    show fumi:
        "fumi 2 lg school h flat"
        alpha 0.0 xcenter 152
        easein 0.5 alpha 1.0 xcenter 252
    show rin:
        "rin 1 lg school b" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 772
    pause 0.5

    show fumi 2 lg school h:
        alpha 1.0 xcenter 252
    show rin 1 lg school b:
        xcenter 772
    with None

    voice "FUM_0657"
    fumi "\"What's wrong? You've been sighing so much since yesterday.\""

    show rin 2 lg school d with dict_dissolve_25

    voice "RIN_0714"
    rin "\"...I might have made Hina hate me.\""

    "Rin confessed after hesitating for a moment."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0658"
    fumi "\"Oh? You're not just having one of your friendly squabbles?\""

    show rin 2 lg school e with dict_dissolve_25

    voice "RIN_0715"
    rin "\"No, we're not fighting... it's more like I just made her angry, I guess.\""

    show fumi 2 lg school f with dict_dissolve_25

    voice "FUM_0659"
    fumi "\"What did you do?\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0716"
    rin "\"Umm... I tickled her, almost kissed her, and then flicked her forehead, and she got pissed.\""

    show fumi:
        "fumi 1 lg school j" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0660"
    fumi "\"Huh? Huh? Huh?\""

    show fumi 1 lg school j:
        xoffset 0 yoffset 0
    with None

    "That threw Fumi for a loop."

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_0717"
    rin "\"You know... two nights ago. Remember?\""

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_0661"
    fumi "\"Umm... when you were messing around in her bed?\""

    show rin:
        "rin 2 lg school c" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0718"
    rin "\"Yeah. She's been avoiding me since then.\""

    show rin 2 lg school d:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "RIN_0719"
    rin "\"...I think it was the kiss thing that set her off. Hina doesn't like that stuff, you know?\""

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_0662"
    fumi "\"Yes, it does make her angry, but she's not really the type to hold a grudge...\""

    show fumi:
        "fumi 1 lg school e" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0663"
    fumi "\"...Oh!\""

    show fumi 1 lg school e:
        xoffset 0 yoffset 0
    with None

    "Fumi exclaimed, realization hitting her."

    show fumi 2 lg school f with dict_dissolve_25

    voice "FUM_0664"
    fumi "\"That's not it, it's the opposite!\""

    show rin 2 lg school g with dict_dissolve_25

    voice "RIN_0720"
    rin "\"Opposite?\""

    show fumi 2 lg school a with dict_dissolve_25

    voice "FUM_0665"
    fumi "\"Yes. She's not angry because you kissed her, she's angry because you didn't.\""

    show fumi 2 lg school i with dict_dissolve_25

    voice "FUM_0666"
    fumi "\"I've been thinking she's been acting strange lately. So that's what it was...\""

    "Fumi nodded to herself, satisfied with the conclusion she'd come to."

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0721"
    rin "\"Umm... Asou? What are you talking about?\""

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0667"
    fumi "\"Were you really going to kiss her then, Ogata?\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0722"
    rin "\"I was thinking about it, but then I felt kinda bad. She had her eyes all squeezed shut and she was trembling...\""

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_0668"
    fumi "\"You {i}should{/i} feel bad for doing that! It's cruel.\""

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0723"
    rin "\"Huh?\""

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0669"
    fumi "\"Natsume likes you, Ogata.\""

    show rin 2 lg school f with dict_dissolve_25

    voice "RIN_0724"
    rin "\"...Likes?\""

    play sound se000c

    hide rin
    hide fumi
    with Dissolve(0.25)

    $ side_image = "hina 2 side school f"

    voice "HIN_0919"
    hina "\"I'm back... Let's go.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou2_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
