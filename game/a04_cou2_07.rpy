label a04_cou2_07:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg02da with Dissolve(0.25)
    pause 0.75

    play music bgm05

    "The date was about to change. The room was dark, and Hina and Fumi were both in bed."

    "Rin, however, was gone."

    show hina 3 sm dark pyjama a:
        xcenter 646
    with dict_dissolve_25

    voice "HIN_1433"
    hina "\"......\""

    "Hina was tossing and turning."

    play sound se521

    "The door quietly opened, and light from the hallway spilled into the room. Footsteps approached."

    $ side_image = "rin 1 side pyjama a"

    voice "RIN_1188"
    rin "\"...You're sleeping by now, right?\""

    "Rin kneeled by Hina's bed and peered down at her face."

    "No response came from Hina. She didn't so much as budge."

    $ side_image = "rin 1 side pyjama c"

    voice "RIN_1189"
    rin "\".........\""

    "Rin smiled contentedly and reached out to stroke Hina's head as if to feel her warmth."

    $ side_image = "rin 1 side pyjama c"

    voice "RIN_1190"
    rin "\"...Good night.\""

    play sound se120a

    "She gave Hina a kiss on the cheek and then climbed up the ladder to her bed."

    show hina 3 sm dark pyjama k with dict_dissolve_25

    voice "HIN_1434"
    hina "\".........\""

    play sound2 se116a

    "When she heard Rin breathing evenly in her sleep, Hina turned to the wall."

    "There were tears on her cheek."

    show hina 3 lg dark pyjama k with dict_dissolve_25

    voice "HIN_1435"
    hina "\"She smelled like cigarettes...\""

    "Hina buried her face in her pillow."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
