label a10_cou3_01:

    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "fumi 2 side pyjama d"

    voice "2FU_1151"
    fumi "\"Yes, yes. No, I haven't heard. But, I'm trying to say, I... Yes, yes.\""

    "Fumi's phone call went on while the other four kept quiet, watching."

    "They seemed to have decided on several things without her and didn't appear to be taking no for an answer."

    $ side_image = "fumi 1 side pyjama d"

    voice "2FU_1152"
    fumi "\"I'll have to discuss it with my family. I have to go!\""

    "Fumi sighed after finally managing to end the conversation somewhat forcefully."

    show fumi 1 lg pyjama h with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "2FU_1153"
    fumi "\"I'm sorry, I had a hard time hanging up—\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_1545"
    hina "\"Wait, what's going on?! You're getting scouted, Asou?!\""

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_1048"
    miyako "\"Are you going to be an idol, Fumi?\""

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0852"
    sachiko "\"Think they'll want to interview the beautiful dorm manager who's been taking care of you?\""

    show fumi:
        "fumi 1 lg pyjama j" with Dissolve(0.25)
        ShakeJump

    voice "2FU_1154"
    fumi "\"Wait, wait! One at a time!\""

    show fumi 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    "The girls all crowded around Fumi like the paparazzi while she tried to calm them down. Though, I don't think one of those really counted as a question."

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "2FU_1155"
    fumi "\"The call was from a talent agency, and the question was whether I wanted to audition for a movie.\""

    $ side_image = "miyako 1 side pyjama_b g"

    voice "2MI_1049"
    miyako "\"Audition? So it's not for sure, then?\""

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_1156"
    fumi "\"No, they did want to scout me, but they said it would be in the form of passing me through an audition.\""

    $ side_image = "sachiko 1 side outfit j"

    voice "2SA_0853"
    sachiko "\"The darkness of the entertainment industry!\""

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_1157"
    fumi "\"Anyway, I hadn't heard anything about it. And I don't know about a movie... I mean, I've never acted before.\""

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_1546"
    hina "\"Is it a starring role?\""

    show fumi 1 lg pyjama d with dict_dissolve_25

    voice "2FU_1158"
    fumi "\"It would be a co-starring role. And after that, they would want me to debut as an idol affiliated with their agency.\""

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_1050"
    miyako "\"When is the audition?\""

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_1159"
    fumi "\"It's on Valentine's... February 14th.\""

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_1547"
    hina "\"That's sooner than I expected.\""

    show fumi:
        "fumi 1 lg pyjama d" with Dissolve(0.25)
        ShakeTameiki

    voice "2FU_1160"
    fumi "\"Yes. It's too soon, really.\""

    show fumi 1 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_1543"
    rin "\"So what are you gonna do? Are you gonna take the audition?\""

    "Surprisingly, Rin had remained silent until just now."

    show fumi:
        "fumi 1 lg pyjama e" with Dissolve(0.25)
        ShakeJump

    voice "2FU_1161"
    fumi "\"Of course not!\""

    show fumi 1 lg pyjama e:
        xoffset 0 yoffset 0
    with None

    "Rin had asked nervously, but Fumi gave her answer immediately."

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_1162"
    fumi "\"I wanted to say no right away, but it was the president of the agency who called me...\""

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0854"
    sachiko "\"Straight from the president! That's pretty serious.\""

    show fumi 2 lg pyjama a with dict_dissolve_25

    voice "2FU_1163"
    fumi "\"I'll call home first. I don't know what my dad talked to them about.\""

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_1544"
    rin "\"Ah, okay...\""

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "2FU_1164"
    fumi "\"Honestly, I can't believe him!\""

    hide fumi with Dissolve(0.5)

    play sound se521
    pause 1.5

    "Fumi left the room, complaining about her father."

    show sachiko z4 1 lg outfit a:
        xcenter 298
    show rin z4 1 lg pyjama glasses e:
        xcenter 726
    with dict_dissolve_25

    voice "2RI_1545"
    rin "\"W-Well, Fumi's dad can be scatterbrained~\""

    "There still seemed to be something of an aftershock to the news after Fumi left the room."

    "Hina and Miyako were excited about the prospect of Fumi becoming famous, but Rin seemed to be having some mixed feelings about it."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0855"
    sachiko "\"You could be in trouble here, don't you think~?\""

    "Sachiko noticed right away and spared no time rubbing it in."

    show rin:
        "rin z4 2 lg pyjama glasses c" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_1546"
    rin "\"But she said she's not interested, so it's not like it's going to be a big deal.\""

    show rin z4 2 lg pyjama glasses c:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0856"
    sachiko "\"Oh? Your girlfriend just got scouted to be an idol. Are you not happy about that?\""

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1547"
    rin "\"W-Well, she is super cute!\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1548"
    rin "\"...But she's also mine.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
