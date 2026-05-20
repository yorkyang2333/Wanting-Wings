label a10_cou2_01:

    scene kimikara_06_d with Dissolve(0.5)
    pause 1.5

    play music bgm05 fadeout 1.0

    "Hina's hand was on Rin's shoulder, fingers trembling with emotion, nails digging into her skin."

    voice "2RI_1305"
    rin "\"Ow...\""

    "Her small cry didn't reach Hina's ears over the pounding of her heart."

    voice "2RI_1306"
    rin "\"Wait... Please, wait...\""

    voice "2HI_1368"
    hina "\"Haah... haah...\""

    scene kimikara_06_e with Dissolve(0.5)

    stop music

    voice "2RI_1307"
    rin "\"Stay!!\""

    voice "2HI_1369"
    hina "\"!!\""

    "She managed to get the word out through her trembling, and Hina stopped."

    "Rin's finger was pointed up right in front of Hina's eyes."

    "She'd unconsciously reacted to the gesture to stop. It was just like Hina had done to Arthur."

    voice "2HI_1370"
    hina "\"Ah...\""

    "She returned to her senses when she saw the band-aid, the beast fading from her eyes."

    scene black with Dissolve(1.0)

    $ voice2("hina","2HI_1371","rin","2RI_1308")
    hina_rin "\"......\""

    play music bgm05 fadein 1.0

    scene kimikara_06_f with Dissolve(0.5)
    pause 1.5

    voice "2HI_1372"
    hina "\"I'm... sorry.\""

    "After a long pause, Hina finally opened her mouth."

    voice "2RI_1309"
    rin "\"Uh, no... I guess I'm... sorry, too.\""

    "Now it looked like Hina was about to cry, and Rin averted her eyes again, unable to look at her."

    voice "2RI_1310"
    rin "\"But, listen, let's do it in our room again, later.\""

    voice "2HI_1373"
    hina "\"...Okay.\""

    "They stood, still looking down."

    scene bg04da with Dissolve(0.5)
    pause 1.5

    show bg_obi with dict_dissolve_25

    $ side_image = "rin 1 side school e"

    voice "2RI_1311"
    rin "\"...Wh-Whoa!\""

    "Rin's knees gave out when she tried to stand, so she ended up bracing against the chalkboard to catch her balance."

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_1374"
    hina "\"Here...\""

    "While Rin was unsteady on her feet, Hina went and picked up the collar, holding it out to her."

    $ side_image = "rin 2 side school e"

    voice "2RI_1312"
    rin "\"...Want to put it on?\""

    voice "2HI_1375"
    hina "\"You decide.\""

    "Rin hesitated for a moment, but decided to put it in her pocket instead. Hina merely watched her wordlessly."

    $ side_image = "rin 2 side school e"

    voice "2RI_1313"
    rin "\"Well... should we get going? Asou and Mikoyan are waiting for us.\""

    voice "2HI_1376"
    hina "\"...Yeah.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
