label a01_cou3_01:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm02

    show fumi 1 sm school a at pos_r
    show rin 1 sm school b at pos_l
    with Dissolve(0.25)

    voice "FUM_0207"
    fumi "\"I locked the back door.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0236"
    rin "\"And I got the windows.\""

    "The two sat down, holding their bags."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0208"
    fumi "\"Have you ever been a class rep before, Ogata?\""

    show rin 1 sm school c with dict_dissolve_25

    voice "RIN_0237"
    rin "\"No way. I've never even been on the library committee. What about you, Asou?\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0209"
    fumi "\"I was in charge of the class pet once. It was a hamster.\""

    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_0238"
    rin "\"Seems like it'd be stressful taking care of a living thing.\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0210"
    fumi "\"It wasn't, really. The hamster was sweet, and it was a lot less work than the class rep had.\""

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0239"
    rin "\"I can't understand why someone would want to do all that work. Do they just want attention?\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0211"
    fumi "\"Well, Natsume didn't volunteer. Everyone nominated her.\""

    show rin:
        "rin 1 sm school g" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0240"
    rin "\"Nominated, eh? You don't think they were just pushing it on her since no one volunteered?\""

    show rin 1 sm school g:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0212"
    fumi "\"I don't think so. Natsume's pretty popular.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0241"
    rin "\"Is she popular, or is she uncomplicated and easy to manipulate?\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0213"
    fumi "\"Eheheh, well, it seems to me that she enjoys the work.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0242"
    rin "\"Well, I don't get it. Is she just brimming with volunteer spirit, or what?\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0214"
    fumi "\"I think she's really incredible. She knows how to take charge, you know?\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0243"
    rin "\"Or is she just impulsive?\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0215"
    fumi "\"It's almost like she has wings.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0244"
    rin "\"Well, anything I can do, anybody else could do, but there's plenty of stuff that only Hina can do.\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0216"
    fumi "\"Heheh. You should compliment her to her face.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0245"
    rin "\"Don't I pat her on the head enough?\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0217"
    fumi "\"You should use words every once in a while.\""

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0246"
    rin "\"Too much work.\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0218"
    fumi "\"There you go again...\""

    play sound se000c

    $ side_image = "hina 1 side school a"

    voice "HIN_0289"
    hina "\"I'm done!\""

    show rin:
        "rin 1 sm school e" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 172
    show fumi:
        "fumi 1 sm school e" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512
    pause 0.25

    show rin 1 sm school e:
        xcenter 172
    show fumi 1 sm school e:
        xcenter 512
    with None
    show hina:
        "hina 1 sm school a flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852

    voice "RIN_0247"
    rin "\"Ah, speak of the devil.\""

    show hina 1 sm school d with dict_dissolve_25:
        1.0
        ShakeJump

    voice "HIN_0290"
    hina "\"What? Ah! Were you badmouthing me?!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0219"
    fumi "\"No, no, we were complimenting you.\""

    show hina:
        "hina 1 sm school j" with Dissolve(0.25)
        ShakeUji

    voice "HIN_0291"
    hina "\"Hrrrmh.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
