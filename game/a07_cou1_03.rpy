label a07_cou1_03:

    scene bg02ag with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_doorcl
    pause 0.5

    $ side_image = "fumi 1 side casual d"

    voice "2FU_0146"
    fumi "\"Ugh~ The wind was so cold~ Are you okay, Hina?\""

    "Fumi scrunched up her shoulders as she shut the door."

    show hina z4 1 lg casual_scarf c:
        xcenter 732
    with dict_dissolve_25

    voice "2HI_0176"
    hina "\"I'm invincible when I have your handmade scarf equipped♪\""

    "Hina boasted. I doubt even the North Wind could rip the scarf from this traveler."

    show fumi z4 2 lg casual i:
        xcenter 292
    with dict_dissolve_25

    voice "2FU_0147"
    fumi "\"I just knitted it for practice, so I'm really happy you're wearing it.\""

    show hina z4 2 lg casual_scarf c with dict_dissolve_25

    voice "2HI_0177"
    hina "\"Well, it's warm and cute. Thanks, Fumi♪\""

    "Hina had received the scarf in question at Fumi's house at the end of the year."

    "Fumi had put it around her neck knowing that she would likely underdress if left to her own devices."

    show fumi z4 2 lg casual b with dict_dissolve_25

    voice "2FU_0148"
    fumi "\"I'll never let you catch cold again!\""

    "This time, Fumi was the one boasting. Well, Hina {i}had{/i} given her cause to worry before."

    scene white with bg_effect_12
    pause 1.5

    scene bg01ag with bg_effect_12
    pause 0.5

    show fumi 2 lg casual h at pos_l
    show hina 2 lg casual_scarf b at pos_r
    with dict_dissolve_25

    voice "2HI_0178"
    hina "\"Y-You think Rin's okay?\""

    show fumi 2 lg casual a with dict_dissolve_25

    voice "2FU_0149"
    fumi "\"Hopefully things aren't too awkward with them.\""

    show hina 2 lg casual_scarf h with dict_dissolve_25

    voice "2HI_0179"
    hina "\"I think Takaoka will be fine, but...\""

    show fumi 1 lg casual h with dict_dissolve_25

    voice "2FU_0150"
    fumi "\"...But Ogata might not. She did say not to worry about her.\""

    "That's right. Fumi and Hina had made sure (perhaps too many times) that Rin would be alright on her own with Takaoka."

    "It was Rin who had suggested they go back to the room first, but they knew she was shy, so they couldn't help worrying."

    show hina 1 lg casual_scarf n with dict_dissolve_25

    voice "2HI_0180"
    hina "\"I didn't get what she meant by rest and free time and stuff, though.\""

    show fumi 2 lg casual h with dict_dissolve_25

    voice "2FU_0151"
    fumi "\"Free time?\""

    "Fumi didn't seem to understand either... though, if she had, Hina probably would have sent her flying."

    show hina 2 lg casual_scarf a with dict_dissolve_25

    voice "2HI_0181"
    hina "\"Well, worrying about her now won't do any good.\""

    "These two were always concerned about Rin. Perhaps even more than each other."

    "And Rin seemed to have noticed that."

    show hina:
        "hina 2 lg casual_scarf g" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0182"
    hina "\"And since she gave us this time alone together, we should make the most of it and flirt our hearts out!\""

    show hina 2 lg casual_scarf g:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi 2 lg casual i" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0152"
    fumi "\"Right. We can thank Ogata later.\""

    show fumi 2 lg casual i:
        xoffset 0 yoffset 0
    with None

    "They nodded, looked into each other's eyes, held hands, and embraced."

    show hina 2 lg casual_scarf c with dict_dissolve_25

    voice "2HI_0183"
    hina "\"Fumi... I love you.\""

    show fumi 2 lg casual b with dict_dissolve_25

    voice "2FU_0153"
    fumi "\"Me too... I love you too, Hina.\""

    hide fumi
    hide hina
    with dict_dissolve_50

    "They were alone together in the afternoon living room. The rustling of their clothes, their breathing, their giggles; these sounds came only from the two of them."

    $ side_image = "hina 2 side casual_scarf g"

    voice "2HI_0184"
    hina "\"You smell good.\""

    "Hina had her face buried in Fumi's chest. Because of their height difference, it was inevitable when they hugged."

    $ side_image = "fumi 1 side casual b"

    voice "2FU_0154"
    fumi "\"It's probably my fabric softener.\""

    $ side_image = "hina 2 side casual_scarf c"

    voice "2HI_0185"
    hina "\"I could find you by following this scent.\""

    $ side_image = "fumi 1 side casual i"

    voice "2FU_0155"
    fumi "\"You think so? Lots of people use the same thing.\""

    "Hina should smell the same way, in fact. Their shampoo was different, but they used the same fabric softener."

    $ side_image = "hina 2 side casual_scarf c"

    voice "2HI_0186"
    hina "\"It's different when it comes from you♪\""

    "She gave her a toothy smile."

    "Though there's no reason to think so, I get the feeling she really could do it."

    $ side_image = "hina 1 side casual_scarf m"

    voice "2HI_0187"
    hina "\"Mm...\""

    "Hina stretched up and stole Fumi's lips."

    "Their breath mixed and each of them pushed into the other's mouth with her tongue."

    "Their tongues entwined, and then their breaths separated again into panting."

    $ side_image = "hina 2 side casual_scarf c"

    voice "2HI_0188"
    hina "\"Fumi...\""

    $ side_image = "fumi 1 side casual i"

    voice "2FU_0156"
    fumi "\"Yes...\""

    "They gazed at each other with moist eyes, full of longing."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 3.5

    if persistent.dpatch:
        jump rp_c_scene01
    else:
        "........."
        "......"
        window hide
        pause 1.0
        window auto

label rp_c_scene01_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
