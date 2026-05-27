label a09_comn_10:

    scene bg07ca with Dissolve(0.5)
    pause 1.5

    play music bgm05

    "—Sachiko was once again on the roof."

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0616"
    sachiko "\"......\"" id a09_comn_10_6de14b8a

    "But she wasn't accompanied by her usual cigarettes. Instead, she was tossing beans into her mouth and chewing on those."

    "She should just eat them in her room..."

    play sound se521
    pause 0.5

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0617"
    sachiko "\"...?\"" id a09_comn_10_4f52c4b8

    "The door suddenly swung open. Sachiko glanced in that direction."

    show namahage sm with dict_dissolve_25

    voice "2MI_0715"
    namahage_miyako "\"Any naughty kids around?!\"" id a09_comn_10_ee986e06

    "And who should appear but the namahage."

    show namahage:
        ShakeJump

    voice "2MI_0716"
    namahage_miyako "\"Any crybabies around?!\"" id a09_comn_10_365a2932

    show namahage:
        xoffset 0 yoffset 0
    with None

    "The namahage bellowed, marching forward. But it was a little unsteady on its feet, as if its visibility wasn't great."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0618"
    sachiko "\"Heh...\"" id a09_comn_10_fae7733b

    "Sachiko had frozen, hand extended to the beans, but as the namahage approached, she started chuckling."

    show namahage:
        ShakeJump

    voice "2MI_0717"
    namahage_miyako "\"Rawr!\"" id a09_comn_10_c3541a56

    show namahage:
        xoffset 0 yoffset 0
    with None

    "It was just before her now, raising its knife in the air."

    voice "2MI_0718"
    namahage_miyako "\".........\"" id a09_comn_10_001045dd

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0619"
    sachiko "\"......\"" id a09_comn_10_e0b579ee

    "The namahage stopped, and a moment passed between them."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0620"
    sachiko "\"No, namahage don't say 'rawr' or anything.\"" id a09_comn_10_7995700b

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
    miyako "\"I'm disappointed. You weren't very surprised.\"" id a09_comn_10_5cf7f0d2

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Miyako took the mask off and revealed herself."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0621"
    sachiko "\"Ahaha, sorry.\"" id a09_comn_10_40512467

    show miyako 1 sm pyjama_a e with dict_dissolve_25

    voice "2MI_0720"
    miyako "\"Smoking again?\"" id a09_comn_10_6283daf8

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0622"
    sachiko "\"I would worry about the sparks if I were you. Straw's very flammable.\"" id a09_comn_10_bf005493

    show miyako:
        "miyako 1 sm pyjama_a g" with Dissolve(0.25)
        ShakeJump

    "Miyako backed away from the namahage costume."

    show miyako 1 sm pyjama_a g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0623"
    sachiko "\"Haha, I'm not smoking today. Just eating beans.\"" id a09_comn_10_f703ae3d

    "Sachiko showed her the bag."

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_0721"
    miyako "\"For setsubun? Didn't you already eat your age earlier?\"" id a09_comn_10_15b3e795

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0624"
    sachiko "\"Yeah, but I wanted to eat more.\"" id a09_comn_10_8224c92f

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
    sachiko "\"Now I'm full.\"" id a09_comn_10_a_2b04714d

    "She crumpled up the now-empty bag."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0722"
    miyako "\"You ate a lot.\"" id a09_comn_10_a_c4efc760

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0626"
    sachiko "\"Still, that's only a hundred years or so. It's nowhere near my real age.\"" id a09_comn_10_a_ef65bd34

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0723"
    miyako "\"You'd have to buy up all the beans in town.\"" id a09_comn_10_a_fa8c956d

    voice "2SA_0627"
    sachiko "\"That still wouldn't be enough. You can't count eternity.\"" id a09_comn_10_a_2e27c5cc

    "Only God could do that."

    "Maybe Chuck Norris?"

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0628"
    sachiko "\"If it's just my age on the surface, it's only five beans, though.\"" id a09_comn_10_a_df2873bb

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0724"
    miyako "\"And I could only eat one. That wouldn't be very filling.\"" id a09_comn_10_a_8c2d667b

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0629"
    sachiko "\"......\"" id a09_comn_10_a_3e6a7b09

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0725"
    miyako "\"...?\"" id a09_comn_10_a_0f4a9c5b

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0630"
    sachiko "\"Do you regret throwing away eternity?\"" id a09_comn_10_a_e3fc8502

    show miyako z4 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0726"
    miyako "\"Well, the beans are tasty, but I'm fine just eating one bag.\"" id a09_comn_10_a_c72f6f97

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0631"
    sachiko "\"That's not what I mean. Humans only live a hundred or so years if they're lucky. That's not even the blink of an eye to an angel. It's just too fleeting to exchange eternity for that...\"" id a09_comn_10_a_7b88e2da

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0632"
    sachiko "\"Are you still happy that you became human?\"" id a09_comn_10_a_9a8f82e0

    "Sachiko looked Miyako in the eye."

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0727"
    miyako "\"Yes.\"" id a09_comn_10_a_1dd42091

    "There was no doubt in her words or her expression."

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0728"
    miyako "\"You taught me that there's value in being human.\"" id a09_comn_10_a_b46d40ce

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0633"
    sachiko "\"I did, didn't I?\"" id a09_comn_10_a_b30ab5bd

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0729"
    miyako "\"Do you regret it?\"" id a09_comn_10_a_5ed7be3e

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0634"
    sachiko "\"...I wonder.\"" id a09_comn_10_a_f93ed993

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0730"
    miyako "\"......\"" id a09_comn_10_a_dcabae36

    "Sachiko looked away, but Miyako continued to watch her face."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0635"
    sachiko "\"Just kidding.\"" id a09_comn_10_a_957e10ec

    "Is she strong- or weak-willed?"

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0636"
    sachiko "\"Let's get back inside. Don't forget the namahage.\"" id a09_comn_10_a_927c5891

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0731"
    miyako "\"Okay.\"" id a09_comn_10_a_0ac8c9f1

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
    sachiko "\"Ugh... koff, koff!\"" id a09_comn_10_b_1d3708d1

    show sachiko:
        xoffset 0 yoffset 0
    with None

    "Sachiko choked. The beans must have gone down her windpipe."

    show miyako:
        "miyako z4 1 lg pyjama_a e" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0732"
    miyako "\"Oh, here.\"" id a09_comn_10_b_1e72869e

    show miyako z4 1 lg pyjama_a e:
        xoffset 0 yoffset 0
    with None

    "Miyako took a can out of the pocket of her pajamas."

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0638"
    sachiko "\"Thanks... ginger tea?\"" id a09_comn_10_b_f6151c30

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0733"
    miyako "\"It's warm canned coffee.\"" id a09_comn_10_b_4d34cb94

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
    sachiko "\"Phew... Coffee's best warm!\"" id a09_comn_10_b_0549391f

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0734"
    miyako "\"Ahaha, I was using it as a hand warmer.\"" id a09_comn_10_b_61336d74

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0640"
    sachiko "\"Oh, sorry for drinking it, then.\"" id a09_comn_10_b_e4d18d4f

    show miyako z4 1 lg pyjama_a h with dict_dissolve_25

    voice "2MI_0735"
    miyako "\"That's alright. I brought it for you.\"" id a09_comn_10_b_4a713e07

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0641"
    sachiko "\"Oh... you did?\"" id a09_comn_10_b_6bcff72d

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0736"
    miyako "\"Since you weren't feeling well earlier. I thought it'd help to keep you warm.\"" id a09_comn_10_b_514c105b

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0642"
    sachiko "\"Thanks... really. Sorry.\"" id a09_comn_10_b_0b32362d

    show miyako:
        "miyako z4 1 lg pyjama_a c" with Dissolve(0.25)
        ShakeTameiki

    voice "2MI_0737"
    miyako "\"Well—\"" id a09_comn_10_b_559fc9f8

    show miyako z4 1 lg pyjama_a c:
        xoffset 0 yoffset 0
    with None

    "Miyako picked up the namahage costume."

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0643"
    sachiko "\"You're going down already?\"" id a09_comn_10_b_f1fc1a60

    show miyako z4 1 lg pyjama_b b with dict_dissolve_25

    voice "2MI_0738"
    miyako "\"Yes, before I go on too long.\"" id a09_comn_10_b_c925473b

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0644"
    sachiko "\"Right...\"" id a09_comn_10_b_c0249c2b

    show miyako z4 1 lg pyjama_b h with dict_dissolve_25

    voice "2MI_0739"
    miyako "\"You should come back down soon too, though. Your hand warmer's gone now.\"" id a09_comn_10_b_6a6185b9

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0645"
    sachiko "\"Oh... yeah.\"" id a09_comn_10_b_36a49cf8

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0740"
    miyako "\"Good night.\"" id a09_comn_10_b_56ae3b8c

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0646"
    sachiko "\"Night.\"" id a09_comn_10_b_54233a33

    hide sachiko
    hide miyako
    with Dissolve(0.5)

    play sound se521
    pause 2.0

    "........."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0647"
    sachiko "\"She's such a good girl. I really might fall for her~\"" id a09_comn_10_b_52ea1281

    scene black with Dissolve(1.5)
    scene bg08ca with Dissolve(1.5)
    pause 0.5

    voice "2SA_0648"
    sachiko "\"...Guess it's time.\"" id a09_comn_10_b_64ff81bc

label a09_comn_10_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
