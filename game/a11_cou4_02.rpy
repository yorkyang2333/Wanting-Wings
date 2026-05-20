label a11_cou4_02:

    scene chapter11
    with Dissolve(0.5)
    pause 1.5



    show chapter11a with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_02:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09ca with Dissolve(0.25)
    pause 0.75

    play music bgm01 fadein 1.0

    show miyako 1 lg school_a g with Dissolve(0.25)
    show miyako:
        ShakeYes

    voice "2MI_1118"
    miyako "\"Ohh... I see... huh...\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Miyako sat in the manager's room, giving her undivided attention to a slice of Christmas cake."

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_1119"
    miyako "\"...Mm... it's incredible...\""

    "It wasn't just the color. Miyako was experiencing a torrent of sensations she'd never before felt, like taste and smell, and she was deeply impressed with each and every one of them."

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0948"
    sachiko "\"......\""

    "Sachiko watched her intently until Miyako noticed her gaze."

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_1120"
    miyako "\"Is there something wrong with how I look?\""

    $ side_image = "sachiko 2 side outfit i"

    voice "2SA_0949"
    sachiko "\"Oh... no.\""

    "Sachiko averted her eyes."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0950"
    sachiko "\"I was just thinking you're in a uniform. It looks good on you, though.\""

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_1121"
    miyako "\"Yes. I was hoping to be able to go to school here.\""

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0951"
    sachiko "\"Yeah, I guess I was sort of thinking the same thing. I would've been pretty surprised if you'd come down as a MILF.\""

    "That would make it pretty hard to come up with a story, wouldn't it?"

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_1122"
    miyako "\"So what should I do now?\""

    "She wasn't prepared at all to live life as a human."

    voice "2MI_1123"
    miyako "\"I have a coat as well, but... other than that, these are the only clothes I have.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0952"
    sachiko "\"Oh, don't worry about that. You can leave it all to me.\""

    "Sachiko took a sip of her tea."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0953"
    sachiko "\"There are plenty of other angels who have become human.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0954"
    sachiko "\"Some of 'em are pretty high up in the world, too. Those ones help out the new arrivals with all sorts of stuff.\""

    show miyako:
        "miyako 1 lg school_a b" with Dissolve(0.25)
        1.5
        "miyako 1 lg school_b g" with Dissolve(0.25)

    voice "2MI_1124"
    miyako "\"Is that right? Oh, what should I do about my name?\""

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0955"
    sachiko "\"Noe... I mean, Miyako! Miyako, with the characters for 'holy night.' Since you were born on Christmas and all.\""

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_1125"
    miyako "\"'Miyako'... Did you just think of that now?\""

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0956"
    sachiko "\"Nah, I've been thinking about it for a while now. Miyako if you were a girl and Taumata if you were a boy.\""

    show miyako 1 lg school_b e with dict_dissolve_25

    voice "2MI_1126"
    miyako "{size=22}\"Short for Taumatawhakatangihangakoauauotamateapokaiwhenuakitanatahu, a location in New Zealand. The name means, 'the summit where Tamatea, the man with the big knees, who climbed mountains, traveled, and was known as Landeater, played his flute for his loved one.'\"{/size}" (last_what_size=11.5)

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0957"
    sachiko "\"Ooh, I'm impressed. So, what do you think?\""

    show miyako 2 lg school c with dict_dissolve_25

    voice "2MI_1127"
    miyako "\"...I'm glad I'm a girl.\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg09ca with bg_effect_05
    pause 0.5

    show miyako z4 2 lg school e:
        xcenter 298
    show sachiko z4 1 lg outfit a:
        xcenter 726
    with Dissolve(0.25)

    voice "2MI_1128"
    miyako "\"Thank you for that... urp.\""

    "Miyako looked slightly uncomfortable after finishing her cake."

    "Sachiko was a light eater. She'd taken one bite of her slice and given the rest to Miyako. So Miyako had basically eaten two slices."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0958"
    sachiko "\"Ahaha. That's what having a full stomach feels like. Once your stomach's settled a little, we'll go meet the trio.\""

    show miyako 1 lg school_a l with dict_dissolve_25

    voice "2MI_1129"
    miyako "\"Yes... Please give me a moment.\""

    pause 0.5

    scene white with bg_effect_05
    pause 2.0

    scene bg05ca with bg_effect_25_750
    pause 0.5

    show miyako 1 lg school_a a with Dissolve(0.25)

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0959"
    sachiko "\"Here, take this.\""

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_1130"
    miyako "\"Huh?\""

    "Sachiko handed Miyako a party popper."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0960"
    sachiko "\"Now, charge!\""

    scene black with Dissolve(1.0)

    play sound [se_cracker,se_cracker]
    pause 1.0

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
