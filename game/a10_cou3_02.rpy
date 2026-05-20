label a10_cou3_02:

    scene expression "gui/kimikara/mainmenu_ground1.webp"
    show expression "gui/kimikara/title2.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter10c with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm01 fadein 1.0

    show hina z4 1 lg school e
    show fumi z4 1 lg school h:
        xcenter 172
    show rin z4 1 lg school i:
        xcenter 852
    with Dissolve(0.25)

    voice "2HI_1548"
    hina "\"That wasn't good, Rin. What you did at lunch.\""

    voice "2RI_1549"
    rin "\"How many times are you gonna say that? I get it already.\""

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1549"
    hina "\"I'm saying it because I know you don't get it.\""

    show hina z4 1 lg school f:
        xoffset 0 yoffset 0
    with None

    "What Hina was scolding her for was chasing away (rather unpleasantly) a girl who was trying to talk to Fumi after seeing her on TV."

    "Luckily, Hina had been there to smooth things over."

    "Rin was annoyed when Hina scolded her for it, and Fumi was flustered and apologetic watching them."

    show fumi z4 1 lg school k with dict_dissolve_25

    voice "2FU_1165"
    fumi "\"I'm sorry. This is all because I couldn't figure out how to end the conversation.\""

    show hina z4 1 lg school e
    show rin z4 1 lg school h
    with dict_dissolve_25

    $ voice2("hina","2HI_1550","rin","2RI_1550N")
    hina_rin "\"It's not your fault, Asou.\"\n\"It's not your fault, Fumi.\"" (what_rest_indent=0)

    show hina z4 1 lg school j
    show rin z4 1 lg school i
    with dict_dissolve_25

    $ voice2("hina","2HI_1551","rin","2RI_1551")
    hina_rin "\"......\""

    "They spoke at the same time and then exchanged a look."

    show fumi z4 2 lg school h with dict_dissolve_25

    voice "2FU_1166"
    fumi "\"Anyway, we're going to see what they have to say tonight.\""

    "Today was the day. People from the talent agency were coming to Fumi's house."

    "In the end, they hadn't been able to come to an agreement over the phone and had decided to meet in person... or rather, the president was able to talk her into it."

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_1167"
    fumi "\"Umm, for dinner tonight—\""

    show hina z4 1 lg school d with dict_dissolve_25

    voice "2HI_1552"
    hina "\"Oh, come on, you don't need to worry about that. We'll figure it out. Now, hurry. You're gonna miss your bus.\""

    show fumi z4 1 lg school d with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_1168"
    fumi "\"Th-Thank you.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "She bowed her head."

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1553"
    hina "\"I've gotta go to the faculty room, so I'll come with you partway.\""

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1552"
    rin "\"Oh, me too—\""

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1554"
    hina "\"You've got cleaning duty, Rin! Don't blow it off!\""

    show hina z4 1 lg school f with None
    hide hina
    hide fumi
    with dict_dissolve_50

    "Rin tried to wander after her, but Hina told her off."

    show rin:
        "rin z4 1 lg school g" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2RI_1553"
    rin "\"Ah... ngh...\""

    show rin z4 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "She watched them go, looking rather forlorn."

    "Miyako called out to her, sensing her mood."

    $ side_image = "miyako 2 side school c"

    voice "2MI_1051"
    miyako "\"I'll help you with the cleaning.\""

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_1554"
    rin "\"...Thanks.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
