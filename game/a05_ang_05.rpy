label a05_ang_05:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_05:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg01ca_grayscale with Dissolve(0.375)
    pause 1.125

    play music bgm05

    "From that day on, I was a part of their life."

    "Of course, they couldn't see me, so I just silently watched them."

    show hina z4 1 lg pyjama h grayscale:
        alpha 0.0 xcenter 270 ycenter 805
        linear 0.25 alpha 1.0
    show fumi z3 1 lg pyjama c grayscale:
        alpha 0.0 xcenter 852
        easein 0.5 alpha 1.0 xcenter 842
    show rin z4 1 lg pyjama b grayscale behind hina, fumi:
        alpha 0.0 xcenter 477 ycenter 831
        linear 0.25 alpha 1.0
    pause 0.5

    show hina z4 1 lg pyjama h grayscale at pos_l2:
        alpha 1.0 xcenter 270 ycenter 805
    show fumi z3 1 lg pyjama c grayscale:
        alpha 1.0 xcenter 842
    show rin z4 1 lg pyjama b grayscale behind hina, fumi:
        alpha 1.0 xcenter 477 ycenter 831
    with None
    camera:
        function LayerShake(10,0,0.5)
    $ persistent.layer_shaken = False

    "Whoops."

    camera
    with None

    "Fumi walked through me, bringing mugs from the kitchen."

    hide fumi with Dissolve(0.25)

    show fumi z4 1 lg pyjama c grayscale:
        xcenter 683 ycenter 833
    with Dissolve(0.25)

    play sound se009c

    voice "FUM_0065"
    fumi "\"Here you are.\""

    "Not only was I invisible to them, we also couldn't bump into each other."

    "And it wasn't just our bodies. We angels could in no way interact with the physical world."

    "I sat down next to the three of them, tuning in to their conversation."

    scene black with Dissolve(0.375)
    pause 1.175


    scene ev01a_grayscale with bg_effect_25_1000
    pause 0.5

    voice "FUM_0069"
    fumi "\"You always look like you're having fun when you've got that camera in your hands, Natsume.\""

    "She's right about that. Hina's eyes sparkle like a child with a favorite toy."

    scene ev01b_grayscale with Dissolve(0.5)

    voice "HIN_0090"
    hina "\"Yeah. I've always felt relaxed holding it.\""

    voice "FUM_0070"
    fumi "\"Your father's a photographer, right?\""

    voice "HIN_0091"
    hina "\"Yep. He's a nature photographer, so he takes pictures of flowers and trees and stuff.\""

    voice "FUM_0071"
    fumi "\"Do you like nature photography too?\""

    voice "HIN_0092"
    hina "\"I wouldn't say I've got a preference. I take pictures of whatever I feel like.\""

    voice "FUM_0072"
    fumi "\"It does seem that way.\""

    "Fumi looked over to Hina's desk."

    "I got up and went to see."

    scene ev01c_grayscale with Dissolve(0.5)

    voice "HIN_0104"
    hina "\"Rin, what's that?\""

    "While I was looking at the pictures, Hina spoke up."

    "She was pointing at a package on Rin's desk—one she'd furtively accepted from Sachiko earlier."

    voice "RIN_0100"
    rin "\"I'll give you three choices, then. If you get it right, I'll give it to you."

    voice "HIN_0105"
    hina "\"Huh? Seriously?\""

    voice "RIN_0101"
    rin "\"1. My allowance.\n2. A super difficult book.\n3. A brick.\""

    "I picked up the package to see what was inside."

    "In reality, though, it didn't budge in the slightest. All I had touched was {i}probability{/i}."

    "I won't go into too complicated an explanation. Just think of it like this: though we angels are not able to move things, we are able to comprehend them."

    "I got a glimpse at the answer before the other two."

    "...Hmm."

    "To be precise, it's none of the three options she gave."

    "The package does indeed contain a book, but it's more \"inappropriate\" than \"difficult.\""

    "What is that woman giving an impressionable girl?"

    scene ev01f_grayscale with Dissolve(0.5)

    voice "FUM_0076"
    fumi "\"#3 would be pretty scary.\""

    voice "RIN_0102"
    rin "\"Is 3 your final answer, Asou?\""

    voice "FUM_0077"
    fumi "\"Huh? Huh?\""

    voice "HIN_0106"
    hina "\"What would I want a brick for?\""

    voice "RIN_0103"
    rin "\"Build your house with 'em and you'll be safe from wolves.\""

    voice "HIN_0107"
    hina "\"I won't have that problem!\""

    "The girls joked with each other. None of them cared what the correct answer was."

    scene black with Dissolve(0.375)
    pause 1.175

    scene bg01ca_grayscale with Dissolve(0.25)
    pause 1.25

    "I took a look around the merry room."

    "Cameras, books, stuffed animals..."

    "There are all sorts of things in this room. And each one of them is bursting with the breath of life."

    "The more attached the girls are to these items, the brighter they shine in my eyes."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a05_ang_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
