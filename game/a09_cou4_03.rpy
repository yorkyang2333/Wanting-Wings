label a09_cou4_03:

    scene bg10bb with Dissolve(0.5)
    pause 1.5

    play sound se_2s_f008
    pause 0.5

    play music bgm01

    "The girls entered the broadcasting room."

    "Hina was carrying a microphone. It was the same situation as last time: returning a tool used in the auditorium."

    $ side_image = "hina 2 side school e"

    voice "2HI_1164"
    hina "\"Sachiko's not here today.\""

    "Hina looked around the room."

    $ side_image = "rin 1 side school f"

    voice "2RI_1210"
    rin "\"No Sachiko. But there is a presence...\""

    $ side_image = "hina 1 side school g"

    voice "2HI_1165"
    hina "\"Ah~ ah~ ah~!\""

    "Hina covered her ears."

    show fumi z4 1 lg school a:
        xcenter 298
    show miyako z4 1 lg school_a b:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0949"
    miyako "\"This is my first time coming in here.\""

    voice "2FU_0924"
    fumi "\"Yes, we stopped at the door last time.\""

    "Yeah, there was a guard in place last time."

    hide fumi
    hide miyako
    with Dissolve(0.25)

    show hina z4 2 lg school f:
        xcenter 298
    show rin z4 1 lg school a:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_1166"
    hina "\"Can I just put it on this shelf, you think?\""

    voice "2RI_1211"
    rin "\"Looks like that's where the other mics are. Don't see why not.\""

    show hina z4 1 lg school e with Dissolve(0.25)
    show hina:
        ShakeJump
        0.3
        ShakeJump

    voice "2HI_1167"
    hina "\"Mmh, hup...\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school k with dict_dissolve_25

    voice "2RI_1212"
    rin "\"I got it.\""

    "Rin took the mic from the stretching Hina and put it on the shelf."

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1168"
    hina "\"Thanks.\""

    show rin z4 1 lg school b with dict_dissolve_25

    voice "2RI_1213"
    rin "\"It's hard to clean these high places. If there's dust, I'm gonna go complain.\""

    show hina z4 1 lg school j with dict_dissolve_25

    voice "2HI_1169"
    hina "\"That's kinda mean. Weren't we just talking about thanking her?\""

    "Rin ran her finger over the edge of the shelf."

    show rin:
        "rin z4 1 lg school f" with Dissolve(0.25)
        3.0
        "rin z4 1 lg school e" with Dissolve(0.25)

    voice "2RI_1214"
    rin "\"Look at all the dust on my... wait, what? It's clean.\""

    show rin z4 1 lg school e:
        pass
    with None

    "Rin checked all over the shelf."

    show rin z4 2 lg school g with dict_dissolve_25

    voice "2RI_1215"
    rin "\"Is she actually working pretty hard?\""

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1170"
    hina "\"Sachiko likes to keep things clean. You've never seen any mess around the dorm, right?\""

    show rin z4 2 lg school a with dict_dissolve_25

    voice "2RI_1216"
    rin "\"I guess not.\""

    hide rin
    hide hina
    with Dissolve(0.25)

    show fumi z4 1 lg school e:
        xcenter 298
    show miyako z4 1 lg school_a a:
        xcenter 726
    with dict_dissolve_25

    voice "2FU_0925"
    fumi "\"...Huh?\""

    show miyako z4 1 lg school_a g with dict_dissolve_25

    voice "2MI_0950"
    miyako "\"What is it?\""

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_0926"
    fumi "\"I was just thinking this calendar is pretty old, huh?\""

    show miyako z4 1 lg school_b e with dict_dissolve_25

    voice "2MI_0951"
    miyako "\"It's from five years ago.\""

    show fumi z4 2 lg school h with dict_dissolve_25

    voice "2FU_0927"
    fumi "\"These posters for events, too. The culture and sports festivals here were both five years ago.\""

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_0952"
    miyako "\"Has this room not been used recently?\""

    show fumi z4 2 lg school a with dict_dissolve_25

    voice "2FU_0928"
    fumi "\"It doesn't seem like it. But Sachiko seems to be keeping it clean.\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_0953"
    if persistent.dpatch:
        miyako "\"Does this school even have a broadcasting club?\"" id a09_cou4_03_c4208bcf
    else:
        miyako "\"Does this campus even have a broadcasting club?\""

    show fumi:
        "fumi z4 2 lg school h" with Dissolve(0.25)
        2.5
        "fumi z4 2 lg school g" with Dissolve(0.25)

    voice "2FU_0929"
    fumi "\"I don't think I've ever heard of one, no. Oh, but there are club journals on this shelf. They're old too, though.\""

    show fumi z4 2 lg school g:
        pass
    with None
    show miyako z4 1 lg school_a i with dict_dissolve_25

    voice "2MI_0954"
    miyako "\"......\""

    python:
        _last_say_what = ""
        _last_say_who = None
        renpy.choice_for_skipping()

    stop music fadeout 1.0

    hide fumi
    hide miyako
    with Dissolve(0.25)

    pause 0.5

    scene select_back3 with Dissolve(0.5)
    pause 1.5

    menu:
        "■選択肢１枠"((713,334), "menu/btn_select_0601"):
            jump a09_cou4_03_g

label a09_cou4_03_g:

    scene bg10bb with Dissolve(0.5)
    pause 0.5

    show hina z4 1 lg school k:
        xcenter 298
    show rin z4 2 lg school a:
        xcenter 726
    with dict_dissolve_25

    play music bgm01 fadein 0.5

    voice "2HI_1171"
    hina "\"Oh, a transceiver.\""

    "Hina noticed the object on the edge of the desk."

    show rin z4 2 lg school g with dict_dissolve_25

    voice "2RI_1217"
    rin "\"Isn't a transceiver something like a big old phone?\""

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_1172"
    hina "\"This is also called a transceiver. It's a wireless device that transmits and receives.\""

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1218"
    rin "\"Huh. You really do know a weird amount about machines, don't you?\""

    show hina z4 1 lg school b with dict_dissolve_25

    voice "2HI_1173"
    hina "\"Yeah, there was always a lot of that junk around my house.\""

    voice "2RI_1219"
    rin "\"Your dad's?\""

    show hina:
        "hina z4 2 lg school a" with Dissolve(0.25)
        3.0
        "hina z4 2 lg school d" with Dissolve(0.25)

    voice "2HI_1174"
    hina "\"Yep. That was around when he was working abroad. ...This thing looks really old. I wonder if it still works.\""

    show hina z4 2 lg school d:
        pass
    with None

    "—That thing's important, so you shouldn't touch it."

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_1175"
    hina "\"Oh, sorry.\""

    show rin z4 1 lg school e with dict_dissolve_25

    voice "2RI_1220"
    rin "\"Huh? What?\""

    show hina z4 1 lg school k with dict_dissolve_25

    voice "2HI_1176"
    hina "\"Didn't you just say I shouldn't touch it?\""

    show rin z4 1 lg school f with dict_dissolve_25

    voice "2RI_1221"
    rin "\"Not me. Maybe it was the ghost.\""

    show hina:
        "hina z4 1 lg school d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1177"
    hina "\"Eep!\""

    show hina z4 1 lg school d
    hide rin
    hide hina
    with dict_dissolve_50

    "While Fumi was looking at the old posters, Miyako headed for the shelf with the club journals on it."

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_0955"
    miyako "\"...She was looking at this one, I think.\""

    "She plucked one from the shelf and looked at it."

    show miyako 1 lg school_a a with dict_dissolve_25

    voice "2MI_0956"
    miyako "\"It's from five years ago, too...\""

    "It opened up easily to a certain page as if accustomed to that position."

    stop music fadeout 1.0

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_0957"
    miyako "\"Huh?\""

    "Miyako found her eyes glued to a picture of the members of the broadcasting club at the time."

    "One of them was..."

    play music bgm03 fadein 1.0

    show miyako 2 lg school b with dict_dissolve_25

    voice "2MI_0958"
    miyako "\"She looks... just like me...\""

    $ side_image = "rin 1 side school e"

    voice "2RI_1222"
    rin "\"What's up, Mikoyan?\""

    "Miyako didn't even hear her, she was so focused on the picture."

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_0959"
    miyako "\"Noel... Noel Nakatani.\""

    "She read the name of the girl from the note next to the picture."

    $ side_image = "hina 1 side school f"

    voice "2HI_1178"
    hina "\"Noel Nakatani! That was it!\""

    "Hina suddenly shouted in response to Miyako's mutterings."

    hide miyako with Dissolve(0.25)

    show fumi z4 2 lg school a:
        xcenter 118
    show miyako z4 1 lg school_a e behind fumi, hina:
        xcenter 383
    show hina z4 1 lg school f:
        xcenter 641
    show rin z4 1 lg school e:
        xcenter 906
    with dict_dissolve_25

    voice "2RI_1223"
    rin "\"Whoa, that scared me.\""

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_0960"
    miyako "\"You know Noel Nakatani?\""

    show hina z4 1 lg school e with dict_dissolve_25

    voice "2HI_1179"
    hina "\"Remember when we were talking about angels in the chapel?\""

    show rin z4 1 lg school a with dict_dissolve_25

    voice "2RI_1224"
    rin "\"When? Which time?\""

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_1180"
    hina "\"Umm, the thing about my sister's friend's friend.\""

    show fumi z4 2 lg school g with dict_dissolve_25

    voice "2FU_0930B"
    fumi "\"Oh, yes! She was praying for her friend in the hospital when the angel appeared.\""

    show hina z4 1 lg school f with Dissolve(0.25)
    show hina:
        ShakeYes

    voice "2HI_1181"
    hina "\"Yeah! The friend in the hospital, her name was Noel Nakatani!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1225"
    rin "\"It's a bit late for that, isn't it? I already forgot the whole story.\""

    show hina z4 1 lg school p with dict_dissolve_25

    voice "2HI_1182"
    hina "\"Well, I feel a lot better! It was bugging me all this time that I couldn't remember. I called my sister, but she forgot, too.\""

    show rin z4 1 lg school k with dict_dissolve_25

    voice "2RI_1226"
    rin "\"And now you're just gonna forget again.\""

    show fumi z4 2 lg school a with dict_dissolve_25

    voice "2FU_0931"
    fumi "\"So, what about Noel Nakatani?\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_0961"
    miyako "\"......\""

    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_0932"
    fumi "\"Umm, Miyako?\""

    show miyako z4 1 lg school_a j with dict_dissolve_25

    voice "2MI_0962"
    miyako "\"......!\""

    hide miyako with dict_dissolve_25
    show fumi:
        "fumi z4 1 lg school e" with Dissolve(0.25)
        ShakeSide

    voice "2FU_0933"
    fumi "\"Ah!\""

    show fumi z4 1 lg school e:
        xoffset 0 yoffset 0
    with None

    play sound se_2s_f008

    show hina z4 1 lg school k
    show rin z4 1 lg school e
    with dict_dissolve_25

    "Miyako ran out of the room, still holding the journal."

    voice "2HI_1183"
    hina "\"Huh? Miyako, what happened?\""

    show rin z4 1 lg school h with dict_dissolve_25

    voice "2RI_1227"
    rin "\"...Maybe the ghost possessed her.\""

    show hina:
        "hina z4 1 lg school g" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2HI_1184"
    hina "\"Gyaaaaaa!!\""

    show hina z4 1 lg school g:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg school h with dict_dissolve_25

    voice "2FU_0934"
    fumi "\"...She left her bag.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou4_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
