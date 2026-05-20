label a03_cou2_01:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg04aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm school headphones g at pos_r
    show fumi 1 sm school a at pos_l
    with Dissolve(0.25)

    show hina:
        ShakeYes2

    voice "HIN_0829"
    hina "\"♪Nya nya nya nya nyaaa nya nyaaa, nya nyaa nyaa nyaa, nyaaa nya nya!\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina's cheerful crowing stood out amid the lunchtime hubbub in the classroom."

    "Girls giggled from the nearby seats, but that meant nothing to the headphoned Hina."

    "And Fumi, across from her, was listening with a smile on her face."

    show rin:
        "rin 1 sm school b flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    show fumi:
        "fumi 1 sm school a" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 172
    show hina:
        "hina 1 sm school headphones g" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512
    pause 0.5

    voice "RIN_0640"
    rin "\"Yeesh. Can't they do anything about how crowded the store gets at lunch?\""

    "Rin returned, the straw of a juice box in her mouth, just as the hook of the song hit."

    show hina 1 sm school headphones c with dict_dissolve_25

    voice "HIN_0830"
    hina "\"♪Nya nya nyaa, nyaaa nya nyaa!\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0641"
    rin "\"She's doing it again.\""

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0645"
    fumi "\"Ahahaha.\""

    "Hina didn't appear to have even noticed Rin's return."

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0642"
    rin "\"How long's she been singing?\""

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0646"
    fumi "\"She started right when you left, so probably about ten minutes.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0643"
    rin "\"I'm worried we'll get noise complaints from the neighbors.\""

    "Rin waved at the girls looking their way and laughing."

    show hina 1 sm school headphones h with dict_dissolve_25

    voice "HIN_0831"
    hina "\"♪Nya nyaaa!\""

    "The singing stopped. She must have gotten to the end of the song. Sensing the presence behind her, she took off her headphones and turned around."

    play sound se555

    show hina:
        "hina 1 sm school k" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0832"
    hina "\"Oh, Rin. When'd you get back?\""

    show hina 1 sm school -headphones k:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0644"
    rin "\"A minute ago.\""

    voice "HIN_0833"
    hina "\"You should have said something.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0645"
    rin "\"You wouldn't have heard me with those things on.\""

    show hina:
        "hina 1 sm school b" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0834"
    hina "\"Oh yeah, good timing.\""

    show hina 1 sm school b:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_0646"
    rin "\"Hmm?\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0835"
    hina "\"Can you tell me what that song's lyrics mean?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0647"
    rin "\"Wh—How am I supposed to do that when you don't know what you're singing?\""

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0836"
    hina "\"No, no. With this.\""

    "Hina flipped one of the ear cups of her headphones outwards and put it to her ear."

    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_0648"
    rin "\"Oh, you want me to translate the lyrics?\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0837"
    hina "\"Yeah. You're good at English, right?\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0649"
    rin "\"Well, better than you, at least.\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    show hina 1 lg school b:
        xcenter 668
    show rin 1 lg school e:
        xcenter 384 ycenter 1204
    with Dissolve(0.25)

    "Rin bent down and put her ear to the headphones, and Hina went back to the start of the song on the player."

    voice "RIN_0650"
    rin "\"Ah, this song.\""

    "It must be a pretty famous song. Rin seemed to know what it was just from the intro."

    show hina 1 lg school c with dict_dissolve_25

    voice "HIN_0838"
    hina "\"♪Nya nya nya nyaaa, nya nyaa!\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0651"
    rin "\"Shut up. I can't hear the lyrics.\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_0839"
    hina "\"Oh, sorry.\""

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0652"
    rin "\"Is a rough translation okay? 'I treasure every moment I spend with you. So I want to stay in this moment forever.' Something like that. It's a love song, basically.\""

    show hina 1 lg school d with dict_dissolve_25

    voice "HIN_0840"
    hina "\"Huh? It's that romantic? I thought it was like, 'Let's destroy the giant asteroid! Yeah!'\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_0653"
    rin "\"That's just what the movie's about.\""

    show rin 1 lg school k with dict_dissolve_25

    voice "RIN_0654"
    rin "\"'I don't want to close my eyes. I don't want to sleep. 'Cause I feel like I'd miss you. And I don't want to miss a thing'...\""

    show hina 1 lg school l with dict_dissolve_25

    voice "HIN_0841"
    hina "\"Wow... that's really pretty.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0655"
    rin "\"And this is the hook that you were nya-nya-ing before.\""

    show hina 2 lg school c with dict_dissolve_25

    voice "HIN_0842"
    hina "\"It sounds totally different now that I know what the lyrics are.\""

    "Hina nodded, touched."

    show rin 1 lg school k with dict_dissolve_25

    voice "RIN_0656"
    rin "\"'I don't want to miss one smile. I don't want to miss one kiss. I only want to be with you'...\""

    stop music fadeout 1.0

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_0843"
    hina "\"Thanks, Ri...\""

    "Hina seemed to suddenly notice how close Rin's face was as they shared the headphones, and she stuttered to a halt."

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0657"
    rin "\"Then it's a refrain... Hm? What's up?\""

    "Rin looked blankly at Hina when she noticed the latter's gaze."

    play music bgm01

    show hina 1 lg school l with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "HIN_0844"
    hina "\"Th-Thanks! I get it, that's good!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0658"
    rin "\"Oh?\""

    play sound se118c

    hide rin
    with Dissolve(0.25)

    show hina:
        "hina 2 lg school headphones h" with Dissolve(0.25)
        xcenter 668
        easein 0.25 xcenter 252

    "Hina snatched the headphones back and put them over her own ears again."

    $ side_image = "rin 1 side school i"

    voice "RIN_0659"
    rin "\"That's pretty rude, and I was being so nice, too~\""

    "Rin pouted."

    show hina 2 lg school headphones c with dict_dissolve_25

    voice "HIN_0845"
    hina "\"......\""

    "No one noticed the bashful look on Hina's face."

    $ side_image = "fumi 2 side school d"

    voice "FUM_0647"
    fumi "\"Oh...?\""

    "No one except Fumi, that is."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
