label a11_cou4_03:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_03:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09ca with Dissolve(0.25)
    pause 0.75

    "—Night on New Year's."

    play sound se_2s_j002

    "Sachiko was doing the dishes."

    show miyako:
        "miyako 1 lg pyjama_a k flat"
        alpha 0.0 xcenter 512 ycenter 1121
        easein 0.15 alpha 1.0 ycenter 1021

    voice "2MI_1131"
    miyako "\"Hwha?!\"" id a11_cou4_03_fb840934

    show miyako 1 lg pyjama_a k:
        alpha 1.0 ycenter 1021
    with None

    "Miyako, who had been sleeping on the table, suddenly woke up and glanced around."

    play music bgm02 fadein 1.0

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0961"
    sachiko "\"Oh, are you awake?\"" id a11_cou4_03_035abc8d

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_1132"
    miyako "\"Where am I...?\"" id a11_cou4_03_dfa4f0fd

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0962"
    sachiko "\"My room?\"" id a11_cou4_03_8375e944

    "She seemed to be still half-asleep and not very aware yet."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0963"
    sachiko "\"You're so surprised. Were you dreaming?\"" id a11_cou4_03_33e234c6

    show miyako 2 lg pyjama b with dict_dissolve_25

    voice "2MI_1133"
    miyako "\"Dreaming...?\"" id a11_cou4_03_178c7c82

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0964"
    sachiko "\"Oh, it was your first one. Of the year and otherwise.\"" id a11_cou4_03_8d85efc2

    "Angels don't dream. Since they don't sleep."

    "They have knowledge of them, of course, but this must have been her first time experiencing one."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0965"
    sachiko "\"What were you dreaming about?\"" id a11_cou4_03_64bd6e4d

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_1134"
    miyako "\"Umm... we were eating soup.\"" id a11_cou4_03_171d9d90

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0966"
    sachiko "\"No, we were actually just doing that.\"" id a11_cou4_03_33557f17

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_1135"
    miyako "\"I could taste it and smell it.\"" id a11_cou4_03_d66d50f0

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0967"
    sachiko "\"Yeah, 'cause that actually happened.\"" id a11_cou4_03_69b25780

    show miyako 1 lg pyjama_b e with dict_dissolve_25

    voice "2MI_1136"
    miyako "\"Also, there was an eggplant and Mt. Fuji and a hawk.\"" id a11_cou4_03_64d57e20

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0968"
    sachiko "\"Just hitting all the clichés, huh?\"" id a11_cou4_03_76c354f8

    show miyako 1 lg pyjama_b l with dict_dissolve_25

    voice "2MI_1137"
    miyako "\"Huh? That's odd... I can't really remember it anymore. It was so clear a second ago...\"" id a11_cou4_03_dfdf6a99

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0969"
    sachiko "\"That's just what dreams are like.\"" id a11_cou4_03_feb7c8c0

    "Sachiko brought the rest of the dishes over to the sink."

    "......"

    "They continued the conversation over her shoulder as she washed."

    show miyako 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_1138"
    miyako "\"Have you invited anyone other than me?\"" id a11_cou4_03_2bfd45c4

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0970"
    sachiko "\"Nope, just you.\"" id a11_cou4_03_354cbcbe

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_1139"
    miyako "\"Oh.\"" id a11_cou4_03_efd1411a

    "She looked a little relieved (though I'm sure she wasn't aware of it)."

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_1140"
    miyako "\"Why did you invite me?\"" id a11_cou4_03_c6d2e93c

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0971"
    sachiko "\"Just... 'cause, I guess.\"" id a11_cou4_03_06a90b30

    show miyako:
        "miyako 2 lg pyjama b" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_1141"
    miyako "\"Oh.\"" id a11_cou4_03_aa6dc8a7

    show miyako 2 lg pyjama b:
        xoffset 0 yoffset 0
    with None

    "She looked a little disappointed (again, I'm sure she didn't realize)."

    show miyako 2 lg pyjama f with dict_dissolve_25

    voice "2MI_1142"
    miyako "\"Who invited you?\"" id a11_cou4_03_129a2b3a

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0972"
    sachiko "\"Well...\"" id a11_cou4_03_8f14cb7f

    show miyako 2 lg pyjama h with dict_dissolve_25

    "......"

    play sound se_suidouto

    "Sachiko turned off the faucet and turned around."

    show miyako 2 lg pyjama j with dict_dissolve_25

    voice "2MI_1143"
    miyako "\"Zzz...\"" id a11_cou4_03_27b98ebf

    "And Miyako was sleeping again."

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0973"
    sachiko "\"Huh? That was fast!\"" id a11_cou4_03_0d77cd7a

    hide miyako with dict_dissolve_50

    "Sachiko dried her hands, went back to the living room, and sat down next to Miyako."

    show sachiko 2 lg outfit a with dict_dissolve_25

    voice "2SA_0974"
    sachiko "\"You really do sleep a lot.\"" id a11_cou4_03_a340cae3

    "She said, watching Miyako."

    "She'd actually watched her sleep for more time than they'd spent talking since she came down on Christmas."

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_0975"
    sachiko "\"When you came down and I saw your face, I thought you were her.\"" id a11_cou4_03_34210b67

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_0976"
    sachiko "\"But even with the same face, your expressions are completely different. And you're even more unlike her when you talk. You're definitely different people.\"" id a11_cou4_03_4d9d23fc

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0977"
    sachiko "\"...Are coincidences like this even possible?\"" id a11_cou4_03_2cf60876

    show sachiko 2 lg outfit c with dict_dissolve_25

    voice "2SA_0978"
    sachiko "\"I thought there was a reason for it. That somebody out there was playing a hell of a mean joke.\"" id a11_cou4_03_72f0790d

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_0979"
    sachiko "\"......\"" id a11_cou4_03_722c5cc0

    show sachiko 2 lg outfit i with dict_dissolve_25

    voice "2SA_0980"
    sachiko "\"But it's all just coincidence. She doesn't know anything.\"" id a11_cou4_03_80ccaba2

    "Sachiko sighed and stared at Miyako's face."

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0981"
    sachiko "\"They look the same sleeping, though.\"" id a11_cou4_03_7337a65f

    "She couldn't help reaching out and poking her on the cheek."

    play sound se_bati

    show bati at truecenter

    show sachiko:
        "sachiko 1 lg outfit h" with Dissolve(0.25)
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0982"
    sachiko "\"?!\"" id a11_cou4_03_8f6febe5

    show sachiko 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    "But Miyako didn't notice and just kept sleeping."

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "2SA_0983"
    sachiko "\"...Couldn't be.\"" id a11_cou4_03_0ec8ca90

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
