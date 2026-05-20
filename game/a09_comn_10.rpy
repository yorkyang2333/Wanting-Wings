label a09_comn_10:

    scene bg07ca with Dissolve(0.5)
    pause 1.5

    play music bgm05

    "—Sachiko was once again on the roof."

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0616"
    sachiko "\"......\""

    "But she wasn't accompanied by her usual cigarettes. Instead, she was tossing beans into her mouth and chewing on those."

    "She should just eat them in her room..."

    play sound se521
    pause 0.5

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0617"
    sachiko "\"...?\""

    "The door suddenly swung open. Sachiko glanced in that direction."

    show namahage sm with dict_dissolve_25

    voice "2MI_0715"
    namahage_miyako "\"Any naughty kids around?!\""

    "And who should appear but the namahage."

    show namahage:
        ShakeJump

    voice "2MI_0716"
    namahage_miyako "\"Any crybabies around?!\""

    show namahage:
        xoffset 0 yoffset 0
    with None

    "The namahage bellowed, marching forward. But it was a little unsteady on its feet, as if its visibility wasn't great."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0618"
    sachiko "\"Heh...\""

    "Sachiko had frozen, hand extended to the beans, but as the namahage approached, she started chuckling."

    show namahage:
        ShakeJump

    voice "2MI_0717"
    namahage_miyako "\"Rawr!\""

    show namahage:
        xoffset 0 yoffset 0
    with None

    "It was just before her now, raising its knife in the air."

    voice "2MI_0718"
    namahage_miyako "\".........\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0619"
    sachiko "\"......\""

    "The namahage stopped, and a moment passed between them."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0620"
    sachiko "\"No, namahage don't say 'rawr' or anything.\""

    show namahage:
        ShakeTameiki
    pause 1.0

    hide namahage
    show miyako 2 sm pyjama c
    with dict_dissolve_25

    show miyako:
        ShakeYes
    pause 0.5

    voice "2MI_0719"
    miyako "\"I'm disappointed. You weren't very surprised.\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Miyako took the mask off and revealed herself."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0621"
    sachiko "\"Ahaha, sorry.\""

    show miyako 1 sm pyjama_a e with dict_dissolve_25

    voice "2MI_0720"
    miyako "\"Smoking again?\""

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0622"
    sachiko "\"I would worry about the sparks if I were you. Straw's very flammable.\""

    show miyako:
        "miyako 1 sm pyjama_a g" with Dissolve(0.25)
        ShakeJump

    "Miyako backed away from the namahage costume."

    show miyako 1 sm pyjama_a g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0623"
    sachiko "\"Haha, I'm not smoking today. Just eating beans.\""

    "Sachiko showed her the bag."

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_0721"
    miyako "\"For setsubun? Didn't you already eat your age earlier?\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0624"
    sachiko "\"Yeah, but I wanted to eat more.\""

    "Sachiko tossed some more beans into her mouth."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg07ca with bg_effect_05
    pause 0.5

    if routes_cleared != 1:
        jump a09_comn_10_a
    else:
        jump a09_comn_10_b

label a09_comn_10_a:

    show miyako z4 1 lg pyjama_a a:
        xcenter 298
    show sachiko z4 1 lg outfit g:
        xcenter 726
    with dict_dissolve_25

    voice "2SA_0625"
    sachiko "\"Now I'm full.\""

    "She crumpled up the now-empty bag."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0722"
    miyako "\"You ate a lot.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0626"
    sachiko "\"Still, that's only a hundred years or so. It's nowhere near my real age.\""

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0723"
    miyako "\"You'd have to buy up all the beans in town.\""

    voice "2SA_0627"
    sachiko "\"That still wouldn't be enough. You can't count eternity.\""

    "Only God could do that."

    "Maybe Chuck Norris?"

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0628"
    sachiko "\"If it's just my age on the surface, it's only five beans, though.\""

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0724"
    miyako "\"And I could only eat one. That wouldn't be very filling.\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0629"
    sachiko "\"......\""

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0725"
    miyako "\"...?\""

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0630"
    sachiko "\"Do you regret throwing away eternity?\""

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0726"
    miyako "\"Well, the beans are tasty, but I'm fine just eating one bag.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0631"
    sachiko "\"That's not what I mean. Humans only live a hundred or so years if they're lucky. That's not even the blink of an eye to an angel. It's just too fleeting to exchange eternity for that...\""

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0632"
    sachiko "\"Are you still happy that you became human?\""

    "Sachiko looked Miyako in the eye."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0727"
    miyako "\"Yes.\""

    "There was no doubt in her words or her expression."

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0728"
    miyako "\"You taught me that there's value in being human.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0633"
    sachiko "\"I did, didn't I?\""

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0729"
    miyako "\"Do you regret it?\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0634"
    sachiko "\"...I wonder.\""

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0730"
    miyako "\"......\""

    "Sachiko looked away, but Miyako continued to watch her face."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0635"
    sachiko "\"Just kidding.\""

    "Is she strong- or weak-willed?"

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0636"
    sachiko "\"Let's get back inside. Don't forget the namahage.\""

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0731"
    miyako "\"Okay.\""

    jump a09_comn_10_end

label a09_comn_10_b:

    show miyako z4 1 lg pyjama_a a:
        xcenter 298
    show sachiko z4 1 lg outfit d:
        xcenter 726
        ShakeSide
        0.3
        ShakeYes2

    voice "2SA_0637"
    sachiko "\"Ugh... koff, koff!\""

    show sachiko:
        xoffset 0 yoffset 0
    with None

    "Sachiko choked. The beans must have gone down her windpipe."

    show miyako:
        "miyako z4 1 lg pyjama_a e" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0732"
    miyako "\"Oh, here.\""

    show miyako z4 1 lg pyjama_a e:
        xoffset 0 yoffset 0
    with None

    "Miyako took a can out of the pocket of her pajamas."

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0638"
    sachiko "\"Thanks... ginger tea?\""

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0733"
    miyako "\"It's warm canned coffee.\""

    play sound se_kanopen
    show sachiko:
        "sachiko z4 1 lg outfit i" with Dissolve(0.25)
        ShakeYes

    pause 2.0

    show sachiko z4 1 lg outfit i:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0639"
    sachiko "\"Phew... Coffee's best warm!\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0734"
    miyako "\"Ahaha, I was using it as a hand warmer.\""

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0640"
    sachiko "\"Oh, sorry for drinking it, then.\""

    show miyako z4 1 lg pyjama_a h with dict_dissolve_25

    voice "2MI_0735"
    miyako "\"That's alright. I brought it for you.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0641"
    sachiko "\"Oh... you did?\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0736"
    miyako "\"Since you weren't feeling well earlier. I thought it'd help to keep you warm.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0642"
    sachiko "\"Thanks... really. Sorry.\""

    show miyako:
        "miyako z4 1 lg pyjama_a c" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0737"
    miyako "\"Well—\""

    show miyako z4 1 lg pyjama_a c:
        xoffset 0 yoffset 0
    with None

    "Miyako picked up the namahage costume."

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0643"
    sachiko "\"You're going down already?\""

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0738"
    miyako "\"Yes, before I go on too long.\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0644"
    sachiko "\"Right...\""

    show miyako z4 1 lg pyjama_b h with dict_dissolve_25

    voice "2MI_0739"
    miyako "\"You should come back down soon too, though. Your hand warmer's gone now.\""

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0645"
    sachiko "\"Oh... yeah.\""

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0740"
    miyako "\"Good night.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0646"
    sachiko "\"Night.\""

    hide sachiko
    hide miyako
    with Dissolve(0.5)

    play sound se521
    pause 2.0

    "........."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0647"
    sachiko "\"She's such a good girl. I really might fall for her~\""

    scene black with Dissolve(1.5)
    scene bg08ca with Dissolve(1.5)
    pause 0.5

    voice "2SA_0648"
    sachiko "\"...Guess it's time.\""

label a09_comn_10_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
