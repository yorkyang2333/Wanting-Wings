label a08_comn_06:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play music bgm05

    play sound se_2s_f001
    pause 1.0

    show miyako 1 sm pyjama_a a with dict_dissolve_25

    voice "2MI_0351"
    miyako "\"Coming in.\""

    play sound se521
    pause 1.0

    show miyako 2 sm pyjama e with Dissolve(0.25)
    show miyako:
        ShakeSide

    voice "2MI_0352"
    miyako "\"Waph... koff!\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "The moment she opened the door, she choked on the smoke flooding out from the room."

    $ side_image = "sachiko 1 side outfit cigarette h"

    voice "2SA_0194"
    sachiko "\"Oh, sorry.\""

    "Sachiko stood, putting out her cigarette."

    show miyako:
        "miyako 2 sm pyjama f" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0353"
    miyako "\"Koff. I'm okay.\""

    show miyako 2 sm pyjama f:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0195"
    sachiko "\"Sorry. I don't usually smoke in here.\""

    "The snow pretty much rules out the roof."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0196"
    sachiko "\"So, what's up?\""

    show miyako 1 sm pyjama_a b with dict_dissolve_25

    voice "2MI_0354"
    miyako "\"The bath's open.\""

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0197"
    sachiko "\"Gotcha. And how was it?\""

    show miyako 1 sm pyjama_a c with dict_dissolve_25

    voice "2MI_0355"
    miyako "\"It was very nice.\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0198"
    sachiko "\"Good. Oh, let's step outside. You don't want to get the smell on you just after your bath.\""

    show miyako:
        xcenter 512
        easein 0.5 xcenter 732

    play sound se_doorcl
    pause 1.5

    show sachiko 1 sm outfit a at pos_ls with Dissolve(0.25)
    pause 0.5

    show miyako 1 sm pyjama_a g with dict_dissolve_25

    voice "2MI_0356"
    miyako "\"Do cigarettes taste good?\""

    show sachiko 2 sm outfit c with dict_dissolve_25

    voice "2SA_0199"
    sachiko "\"Not really.\""

    show miyako 1 sm pyjama_a e with dict_dissolve_25

    voice "2MI_0357"
    miyako "\"Then why do you smoke them?\""

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0200"
    sachiko "\"I'm just acting tough. Helps with the loneliness, too.\""

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_0358"
    miyako "\"Huh...\""

    "She didn't seem to understand."

    show miyako 1 sm pyjama_a e with dict_dissolve_25

    voice "2MI_0359"
    miyako "\"How long have you been smoking?\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0201"
    sachiko "\"Five years, I guess.\""

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_0360"
    miyako "\"Oh, you started just after you came down, then.\""

    "Miyako was a little surprised at that."

    show miyako 2 sm pyjama c with dict_dissolve_25

    voice "2MI_0361"
    miyako "\"Did the person who invited you smoke?\""

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0202"
    sachiko "\"......\""

    "This time it was Sachiko who was surprised."

    show sachiko 2 sm outfit c with dict_dissolve_25

    voice "2SA_0203"
    sachiko "\"Yeah, I guess.\""

    "It was a vague answer, but not a denial."

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0204"
    sachiko "\"Why did you think that?\""

    show miyako 1 sm pyjama_a c with dict_dissolve_25

    voice "2MI_0362"
    miyako "\"The person who invites you has a big influence on you. That's how it is for me, anyway.\""

    "An innocent smile."

    show sachiko 2 sm outfit e with dict_dissolve_25

    voice "2SA_0205"
    sachiko "\"Nothin' good about my influence.\""

    show miyako 1 sm pyjama_a b with dict_dissolve_25

    voice "2MI_0363"
    miyako "\"You think so?\""

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0206"
    sachiko "\"You can try alcohol and cigarettes for yourself someday, but we've both got to act 'our age.'\""

    show miyako 1 sm pyjama_a c with dict_dissolve_25

    voice "2MI_0364"
    miyako "\"Right.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0207"
    sachiko "\"If she finds out, Hinacchi'll dropkick me again.\""

    show miyako 1 sm pyjama_a b with dict_dissolve_25

    voice "2MI_0365"
    miyako "\"Ahaha. You're a bad adult.\""

    show miyako 1 sm pyjama_a e with dict_dissolve_25

    voice "2MI_0366"
    miyako "\"Was the person who got you smoking a bad adult too?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0208"
    sachiko "\"The worst of the worst.\""

    show miyako 1 sm pyjama_a f with dict_dissolve_25

    voice "2MI_0367"
    miyako "\"You shouldn't have imitated them, then.\""

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "2SA_0209"
    sachiko "\"Ahaha. Well, it's too late now.\""

    "You can't blame other people."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0210"
    sachiko "\"Come on, get back to your room before you catch cold.\""

    show miyako 1 sm pyjama_a b with dict_dissolve_25

    voice "2MI_0368"
    miyako "\"Okay. Good night.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 3.0

    $ side_image = "sachiko 2 side outfit d"

    voice "2SA_0211"
    sachiko "\"...Empty already.\""

    play sound paperround
    pause 1.0

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
