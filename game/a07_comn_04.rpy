label a07_comn_04:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play sound se030a

    play music bgm01

    show fumi 2 sm school b at pos_l2
    show miyako 1 sm school_a b
    show rin 1 sm school c at pos_r2
    with dict_dissolve_25

    voice "2FU_0053"
    fumi "\"Good job getting through your first day.\""

    voice "2MI_0028"
    miyako "\"Thank you. It was a lot of fun.\""

    voice "2RI_0070"
    rin "\"Everyone was staring at you. Even the teachers.\""

    "True."

    show miyako 2 sm school c with dict_dissolve_25

    voice "2MI_0029"
    miyako "\"I'm still not used to people looking at me.\""

    show fumi 2 sm school h with dict_dissolve_25

    voice "2FU_0054"
    fumi "\"?\""

    show rin 2 sm school g with dict_dissolve_25

    voice "2RI_0071"
    rin "\"Was it like this where you were before?\""

    show miyako 2 sm school f with dict_dissolve_25

    voice "2MI_0030"
    miyako "\"Well...\""

    $ side_image = "hina 1 side school c"

    voice "2HI_0076"
    hina "\"I'm back!\""

    hide fumi
    hide rin
    hide miyako
    with dict_dissolve_50

    "And that's when Hina came back."

    show hina 1 sm school b at pos_ls
    show miyako 2 sm school c at pos_rs
    with dict_dissolve_25

    voice "2MI_0031"
    miyako "\"H-Hello!\""

    show hina 1 sm school k with dict_dissolve_25

    voice "2HI_0077"
    hina "\"H-Hm? I got your printout.\""

    show miyako 1 sm school_a b with dict_dissolve_25

    voice "2MI_0032"
    miyako "\"Thank you.\""

    hide miyako
    with Dissolve(0.5)

    show rin 2 sm school a at pos_rs with dict_dissolve_25

    voice "2RI_0072"
    rin "\"What printout?\""

    show hina 1 sm school f with dict_dissolve_25

    voice "2HI_0078"
    hina "\"The one you {i}never actually turned in{/i}, Rin!\""

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_0073"
    rin "\"You shouldn't hold grudges.\""

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_0079"
    hina "\"We have to turn in our second year course selections soon, so you'd {i}better{/i} turn that one in on time!\""

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_0074"
    rin "\"It's after proficiency tests, so we've got some time, right?\""

    show hina 1 sm school f with dict_dissolve_25

    voice "2HI_0080"
    hina "\"I'm giving you ample warning!\""

    show rin 1 sm school a with dict_dissolve_25

    voice "2RI_0075"
    rin "\"Science or arts. Which one are you picking, Hina?\""

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_0081"
    hina "\"I'm picking science. Whatever I have to do to get away from English. What about you, Rin?\""

    show rin 1 sm school k with dict_dissolve_25

    voice "2RI_0076"
    rin "\"I'm good at both, so I dunno~\""

    show hina 1 sm school j with dict_dissolve_25

    voice "2HI_0082"
    hina "\"Ugh...\""

    show hina 1 sm school f with dict_dissolve_25

    voice "2HI_0083"
    hina "\"Oh, and it's not just about classes. There are career questions, too.\""

    show rin 1 sm school e with dict_dissolve_25

    voice "2RI_0077"
    rin "\"Now {i}that{/i}, I forgot about.\""

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0084"
    hina "\"I thought so. Think about it, okay?\""

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None
    show rin 2 sm school a with dict_dissolve_25

    voice "2RI_0078"
    rin "\"My career... eh?\""

    show hina 1 sm school a with dict_dissolve_25

    voice "2HI_0085"
    hina "\"I've got an answer for that one, too.\""

    show rin 1 sm school b with dict_dissolve_25

    voice "2RI_0079"
    rin "\"Hmm...\""

    "Hina's face was proud, where Rin's looked forlorn."

    hide rin
    hide hina
    with Dissolve(0.5)

    show fumi 2 sm school h at pos_ls
    show miyako 1 sm school_a e at pos_rs
    with dict_dissolve_25

    voice "2FU_0055"
    fumi "\"You need a guardian's signature on that printout. Are you going to mail it home?\""

    show miyako 1 sm school_a g with dict_dissolve_25

    voice "2MI_0033"
    miyako "\"I... suppose so.\""

    "Miyako looked over the sheet after Fumi pointed that out."

    $ side_image = "rin 2 side school g"

    voice "2RI_0080"
    rin "\"You could probably ask Sachiko.\""

    show fumi 2 sm school g with dict_dissolve_25

    voice "2FU_0056"
    fumi "\"Oh, that's right.\""

    $ side_image = "rin 1 side school a"

    voice "2RI_0081"
    rin "\"Even she should count as a stand-in guardian.\""

    $ side_image = "hina 1 side school n"

    voice "2HI_0086"
    hina "\"Harsh.\""

    show miyako 2 sm school c with dict_dissolve_25

    voice "2MI_0034"
    miyako "\"Haha. I'll ask when we get back.\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "2FU_0057"
    fumi "\"Let's do our shopping before it gets dark and go home, then.\""

    $ side_image = "hina 1 side school p"

    voice "2HI_0087"
    hina "\"Yeah. We've gotta get Miyako some shampoo and conditioner.\""

    "She'd been using sample bottles they had in their room, but those had run out last night."

    show fumi 2 sm school c with dict_dissolve_25

    voice "2FU_0058"
    fumi "\"Did you like any of the ones you tried?\""

    show miyako 2 sm school a with dict_dissolve_25

    voice "2MI_0035"
    miyako "\"Hmm~ I'm not really sure.\""

    show fumi 2 sm school h with dict_dissolve_25

    voice "2FU_0059"
    fumi "\"Your hair is soft and wavy... of the three of us, it's probably closest to mine. Want to try the brand that I use?\""

    show miyako 1 sm school_a b with Dissolve(0.25)
    show miyako:
        ShakeYes

    voice "2MI_0036"
    miyako "\"Yes, that sounds good.\""

    show miyako:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school d with dict_dissolve_25

    voice "2FU_0060"
    fumi "\"It'd be better if we could find what you used before... They don't sell it in Japan, you said?\""

    show miyako 2 sm school f with dict_dissolve_25

    voice "2MI_0037"
    miyako "\"Umm, err, yes.\""

    $ side_image = "rin 1 side school f"

    voice "2RI_0082"
    rin "\"Well, some of us here use body wash top to bottom, so...\""

    $ side_image = "hina 1 side school g"

    voice "2HI_0088"
    hina "\"I told you, I don't!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
