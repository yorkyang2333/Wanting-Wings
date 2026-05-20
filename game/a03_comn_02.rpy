label a03_comn_02:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    play sound se001b

    scene bg05ba with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show rin:
        "rin 1 sm school_scarf a flat"
        alpha 0.0 xcenter 1028
        easein 0.5 alpha 1.0 xcenter 928
    show fumi:
        "fumi 1 sm school_scarf a flat"
        alpha 0.0 xcenter 684
        easein 0.5 alpha 1.0 xcenter 584
    show hina:
        "hina 1 sm school_scarf a flat"
        alpha 0.0 xcenter 864
        easein 0.5 alpha 1.0 xcenter 764
    show sachiko 1 sm outfit a with dict_dissolve_25:
        xcenter 188
    pause 0.25

    voice "SYO_0080"
    sachiko "\"Foomin, Foomin, you found an angel feather?!\""

    show rin 1 sm school_scarf a:
        alpha 1.0 xcenter 928
    show fumi 1 sm school_scarf a:
        alpha 1.0 xcenter 584
    show hina 1 sm school_scarf a:
        alpha 1.0 xcenter 764
    with None

    show fumi:
        "fumi 1 sm school_scarf e" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0473"
    fumi "\"Huh? Oh... yes.\""

    show fumi 1 sm school_scarf e:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf e with dict_dissolve_25

    voice "HIN_0637"
    hina "\"How do you know that?\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0081"
    sachiko "\"Well, y'know, 'cause I'm the dorm manager.\""

    show rin 1 sm school_scarf h with dict_dissolve_25

    voice "RIN_0519"
    rin "\"Guess we'll need to search for listening devices.\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0082"
    sachiko "\"Oh, whatever, just show me the feather already.\""

    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "HIN_0638"
    hina "\"Don't you 'whatever' us!\""

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "FUM_0474"
    fumi "\"Oh, it's in our room.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0083"
    sachiko "\"I'm gonna go look, then!\""

    show hina:
        "hina 1 sm school_scarf d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0639"
    hina "\"What? You're coming to our room?\""

    show hina 1 sm school_scarf d:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "RIN_0520"
    rin "\"Probably to pick up those listening devices.\""

    "The two were clearly bothered by the idea."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0084"
    sachiko "\"Let's go, Foomin!\""

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0475"
    fumi "\"Oh, okay.\""

    "But Sachiko paid no mind. She walked off, arm around Fumi's shoulder."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0085"
    sachiko "\"I don't think I've been in here since move-in~\""

    show hina 1 sm school_scarf h with dict_dissolve_25

    voice "HIN_0640"
    hina "\"We didn't want you in here until move-out.\""

    scene black with bg_effect_02

    play sound se521

    scene bg02ba with bg_effect_02
    pause 0.5

    show rin 1 sm school a:
        xcenter 928
    show fumi 1 sm school a:
        xcenter 584
    show hina 1 sm school j:
        xcenter 764
    show sachiko 1 sm outfit f:
        xcenter 188
    with Dissolve(0.25)

    show sachiko:
        ShakeUji

    voice "SYO_0086"
    sachiko "\"Ahh... It's the scent of young girls.\""

    show sachiko:
        xoffset 0 yoffset 0
    with None

    "Sachiko took a deep breath as soon as she entered the room."

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0641"
    hina "\"Quit being gross!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0087"
    sachiko "\"Now, let's have a look at the scene of the crime.\""

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0521"
    rin "\"What crime?\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0476"
    fumi "\"Umm, the feather is...\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0088"
    sachiko "\"This you, Foomin?\""

    play sound se637

    show sachiko:
        ShakeYes

    "Sachiko pulled out the drawer of a dresser."

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 1 sm school j" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0477"
    fumi "\"Huh? Wait!\""

    show fumi 1 sm school j:
        xoffset 0 yoffset 0
    with None

    "She had guessed the underwear drawer in one shot and was pulling out a bra."

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "SYO_0089"
    sachiko "\"Whoa, that's big! What size is this? E? That's like seven sizes bigger than Hinacchi.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0642"
    hina "\"E, D, C, B, A...\""

    "She's counting on her fingers..."

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0643"
    hina "\"What are my boobs, inverted?!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit e with dict_dissolve_25

    voice "SYO_0090"
    sachiko "\"They've got cute designs even for the big ones these days, huh?\""

    show fumi 1 sm school g with dict_dissolve_25

    voice "FUM_0478"
    fumi "\"P-Please don't study it like that!\""

    play sound se118c

    "She grabbed the bra from Sachiko."

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0091"
    sachiko "\"What? I was gonna line 'em all up on the floor.\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0522"
    rin "\"What are you, an underwear thief?\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0092"
    sachiko "\"Which dresser's yours, Rin?\""

    show rin 1 sm school j with dict_dissolve_25

    voice "RIN_0523"
    rin "\"Why would I tell you that?!\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0093"
    sachiko "\"Then—\""

    show rin 1 sm school i
    show hina 1 sm school j
    with dict_dissolve_25

    voice "HIN_0644"
    hina "\"I'm not telling you either.\""

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "SYO_0094"
    sachiko "\"Wait, Hinacchi, do you wear bras?\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0645"
    hina "\"Of course I do!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0095"
    sachiko "\"What kind?\""

    show hina 1 sm school h
    show sachiko 1 sm outfit e
    with dict_dissolve_25

    voice "HIN_0646"
    hina "\"This k—\""

    show fumi 1 sm school j with dict_dissolve_25

    if hina_fumi_score != 999:
        voice "FUM_0479"
        fumi "\"Natsume, Natsume!\""
    else:
        voice "FUM_0480"
        fumi "\"Hina, Hina!\""

    "Fumi hurriedly stopped Hina from pulling up her vest."

    play sound se231

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0096"
    sachiko "\"So close.\""

    "Sachiko snapped her fingers."

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "SYO_0097"
    sachiko "\"Well, I got to see Foomin's bras and Hinacchi's belly button, so I guess I'll go home.\""

    show hina 1 sm school l with dict_dissolve_25

    voice "HIN_0647"
    hina "\"What happened to the feather?!\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "SYO_0098"
    sachiko "\"Oh, I forgot~ Teehee.\""

    "She gave herself a rap on the head and stuck her tongue out."

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0648"
    hina "\"Let's hit her, Rin!\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0524"
    rin "\"I know how you feel, Hina, but calm down.\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0481"
    fumi "\"This is it...\""

    "Fumi handed Sachiko the feather from that morning."

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "SYO_0099"
    sachiko "\"Hmm...\""

    "She held the feather up to the light and turned it, peering at it."

    show fumi 1 sm school h with dict_dissolve_25

    voice "FUM_0482"
    fumi "\"...Do you know what it is?\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0100"
    sachiko "\"Nope~ Teehee!\""

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0649"
    hina "\"Rin!\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0525"
    rin "\"She gets three strikes. Just be patient.\""

    voice "FUM_0483"
    fumi "\"I don't think it's a regular bird's feather.\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0101"
    sachiko "\"Well, I'm not exactly a bird expert, so.\""

    show hina 1 sm school h with dict_dissolve_25

    voice "HIN_0650"
    hina "\"Then what the heck did you come here for?\""

    hide rin
    hide fumi
    hide hina
    hide sachiko
    with Dissolve(0.25)

    scene black with bg_effect_12

    scene bg01ba with bg_effect_12
    pause 0.5

    show rin 1 sm school a:
        xcenter 928
    show fumi 1 sm school a:
        xcenter 584
    show hina 1 sm school j:
        xcenter 764
    show sachiko 1 sm outfit b:
        xcenter 188
    with Dissolve(0.25)

    voice "SYO_0102"
    sachiko "\"Did you sleep with the window open last night?\""

    "Sachiko went into the living room and inspected the window frame."

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_0526"
    rin "\"That's what I said, but it was closed, right?\""

    "Fumi nodded."

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0103"
    sachiko "\"Which means there was no way in or out of this room last night.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0527"
    rin "\"Well, I guess so.\""

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "SYO_0104"
    sachiko "\"If there are no signs of infiltration from outside, then that means... the culprit is among us! Bam!\""

    "She added a sound effect."

    show sachiko 1 sm outfit e with dict_dissolve_25

    voice "SYO_0105"
    sachiko "\"Okay, everybody, strip! I'm gonna check you for wings!\""

    show hina 1 sm school g
    show rin 1 sm school j
    with dict_dissolve_25

    $ voice2("hina","HIN_0651","rin","RIN_0528")
    hina_rin "\"No way!\""

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0106"
    sachiko "\"Tch.\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0484"
    fumi "\"...We're not doing it?\""

    show hina 1 sm school l with dict_dissolve_25

    if hina_fumi_score != 999:
        voice "HIN_0652"
        hina "\"What are you playing along for, Asou?\""
    else:
        voice "HIN_0653"
        hina "\"What are you playing along for, Fumi?\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0485"
    fumi "\"Well, I thought one of you might be the angel.\""

    "Fumi looked between Rin and Hina."

    show hina 1 sm school d
    show rin 1 sm school e
    with dict_dissolve_25

    $ voice2("hina","HIN_0654","rin","RIN_0529")
    hina_rin "\"Well, we're not.\""

    "The two looked at each other to confirm."

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "SYO_0107"
    sachiko "\"I really think you should strip.\""

    show hina 1 sm school f
    show rin 1 sm school j
    with dict_dissolve_25

    $ voice2("hina","HIN_0655","rin","RIN_0530")
    hina_rin "\"We're not stripping!\""

    hide rin
    hide fumi
    hide hina
    hide sachiko
    with Dissolve(0.25)

    stop music fadeout 1.0

    scene black with bg_effect_11

    scene bg02ba with bg_effect_11
    pause 0.5

    play music bgm02

    show rin 1 sm school a:
        xcenter 928
    show fumi 1 sm school a:
        xcenter 584
    show hina 1 sm school f:
        xcenter 764
    show sachiko 1 sm outfit cigarette c:
        xcenter 188
    with Dissolve(0.25)

    voice "HIN_0656"
    hina "\"If you're gonna smoke, get out!\""

    show sachiko:
        "sachiko 1 sm outfit cigarette d" with Dissolve(0.25)
        ShakeTameiki

    voice "SYO_0108"
    sachiko "\"Oh, sorry. Habit, y'know?\""

    show sachiko 1 sm outfit cigarette d:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_0531"
    rin "\"You know there's no smoking in this whole dorm, right?\""

    show sachiko 1 sm outfit cigarette c with dict_dissolve_25

    voice "SYO_0109"
    sachiko "\"Wait, is that right? Is that a new rule, Foomin?\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0486"
    fumi "\"No, I believe it's always been the rule, since it's a student dorm.\""

    show sachiko 1 sm outfit cigarette d with dict_dissolve_25

    voice "SYO_0110"
    sachiko "\"Huh...\""

    play sound se521

    hide sachiko
    with Dissolve(0.25)

    pause 0.5

    $ side_image = "sachiko 1 side outfit cigarette d"

    voice "SYO_0111"
    sachiko "\"Oh, can I just say one last thing?\""

    "Sachiko turned around just after heading into the hallway."

    "She scratched her head, her other hand holding a cigarette, and said:"

    $ side_image = "sachiko 1 side outfit cigarette i"

    voice "SYO_0112"
    sachiko "\"If you guys are gonna have a lingerie party after this, could you invite me? Y'know, just to watch.\""

    show hina:
        "hina 1 sm school g" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0657"
    hina "\"We are not! Get lost already!!\""

    show hina 1 sm school g:
        xoffset 0 yoffset 0
    with None

    play sound se118c

    "Hina threw a cushion that hit the door and fell to the floor."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
