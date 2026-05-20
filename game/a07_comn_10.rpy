label a07_comn_10:

    scene black with Dissolve(0.5)
    pause 1.5

    if persistent.dpatch:
        "—The night before the first day of school." id a07_comn_10_ff58e9ec
    else:
        "—The night before the first day of class."

    play music bgm02

    scene bg07ca with Dissolve(0.5)
    pause 2.0

    play sound se_tabaco
    pause 0.5

    $ side_image = "sachiko 1 side outfit cigarette i"

    voice "2SA_0134"
    sachiko "\"Phew...\""

    "She sucked smoke in, looking disgusted, then sighed it out."

    "...You should just quit."

    play sound se521
    pause 2.0

    $ side_image = "sachiko 1 side outfit cigarette a"

    voice "2SA_0135"
    sachiko "\"Ah, it's the lion.\""

    show miyako 2 sm pyjama f at pos_rs with dict_dissolve_25

    voice "2MI_0133"
    miyako "\"R-Roar~?\""

    "The lion attempted."

    show sachiko 1 sm outfit cigarette a at pos_ls with dict_dissolve_25

    voice "2SA_0136"
    if persistent.dpatch:
        sachiko "\"What's up? Nervous about starting your school life?\"" id a07_comn_10_f5a85661
    else:
        sachiko "\"What's up? Nervous about starting academy life?\""

    show miyako 2 sm pyjama d with dict_dissolve_25

    voice "2MI_0134"
    miyako "\"No, I'm not... well, maybe a little.\""

    show sachiko 1 sm outfit cigarette g with dict_dissolve_25

    voice "2SA_0137"
    sachiko "\"You'll be fine. You've got those girls with you.\""

    show miyako 1 sm pyjama_a e with Dissolve(0.25)
    show miyako:
        ShakeYes

    voice "2MI_0135"
    miyako "\"Yes. ...Oh, here.\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "The lion took a can of coffee out of her pocket."

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0138"
    sachiko "\"You're a marsupial lion.\""

    "Thylacoleo looks nothing like that."

    show sachiko:
        "sachiko 1 sm outfit cigarette g" with Dissolve(0.25)
        0.5
        "sachiko 1 sm outfit cigarette h" with Dissolve(0.25)
        ShakeSide

    voice "2SA_0139"
    sachiko "\"Thank—cold!\""

    show sachiko 1 sm outfit cigarette h:
        xoffset 0 yoffset 0
    with None

    "Sachiko yelped when she touched the can."

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_0136"
    miyako "\"The vending machine only had cold ones...\""

    show sachiko 2 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0140"
    sachiko "\"R-Right.\""

    "She brought that on herself."

    show sachiko 2 sm outfit cigarette e with dict_dissolve_25

    voice "2SA_0141"
    sachiko "\"Guess I'll have this later. Aren't you cold?\""

    "They were warm pajamas, but they weren't meant to be worn outside."

    show miyako 2 sm pyjama c with dict_dissolve_25

    voice "2MI_0137"
    miyako "\"I am cold, but I like it.\""

    "Even the cutting chill was a fun new experience for her."

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0142"
    sachiko "\"You know, humans catch colds.\""

    "She said sternly."

    show sachiko 1 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0143"
    sachiko "\"I get your excitement, but you've gotta get used to having a human body.\""

    "For better and for worse."

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0144"
    sachiko "\"You should learn from your first experience with the cake.\""

    show miyako 2 sm pyjama e with dict_dissolve_25

    voice "2MI_0138"
    miyako "\"Aaah...\""

    "That struck a chord with her."

    show miyako 1 sm pyjama_a c with dict_dissolve_25

    voice "2MI_0139"
    miyako "\"There's a lot to remember.\""

    show miyako:
        "miyako 1 sm pyjama_hood_a c" with Dissolve(0.25)
        ShakeYes

    "Miyako said, donning her hood."

    show miyako 1 sm -pyjama_a pyjama_hood_a c:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0145"
    sachiko "\"Not to mention all you'll forget.\""

    show miyako 1 sm pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0140"
    miyako "\"Huh? Forget?\""

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0146"
    sachiko "\"Taumata?\""

    "Sachiko prompted, instead of answering her question."

    show miyako 2 sm pyjama_hood a with dict_dissolve_25

    voice "2MI_0141"
    miyako "\"Whakatangihangakoa... ua... uo... huh?\""

    "She'd hesitated for a moment, then attempted to continue, however..."

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0147"
    sachiko "\"Can't come up with the rest, right?\""

    show miyako:
        "miyako 2 sm pyjama_hood b" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0142"
    miyako "\"...What is this?\""

    show miyako 2 sm pyjama_hood b:
        xoffset 0 yoffset 0
    with None

    "Miyako looked worriedly at Sachiko. She was confused that she couldn't remember something she should have known."

    show sachiko 2 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0148"
    sachiko "\"That's a {i}human memory{/i}. I told you, you have a human body now, right?\""

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0149"
    sachiko "\"You can only remember what fits up here. It's not stored in the cloud like it was up until now.\""

    "Sachiko tapped her temple."

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0150"
    sachiko "\"It's not just your capacity, too. The flood of sensation will wash away whatever information you have now.\""

    show miyako 2 sm pyjama_hood f with dict_dissolve_25

    voice "2MI_0143"
    miyako "\"Flood of sensation?\""

    voice "2SA_0151"
    sachiko "\"You were enjoying the sensation of 'cold' before, right? That's a huge amount of data.\""

    show miyako 2 sm pyjama_hood a with dict_dissolve_25

    voice "2MI_0144"
    miyako "\"......\""

    "Her face was blank, the information not quite processed yet."

    show sachiko 2 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0152"
    sachiko "\"...Let's see... Can you describe the sensation of 'cold' without using that word?\""

    show miyako 1 sm pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0145"
    miyako "\"The chill of the wind... made my skin hurt... and my fingers numb, umm...\""

    show sachiko 2 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0153"
    sachiko "\"Was that all you felt? It was just a part of the sensation, right? It's impossible to describe the entirety of the experience in words.\""

    show sachiko 2 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0154"
    sachiko "\"Let me give you another example. The {i}information{/i} that 'apples taste good' and the {i}sensation{/i} of 'eating a tasty apple' are two pieces of data with wildly different sizes.\""

    show sachiko 2 sm outfit cigarette d with dict_dissolve_25

    voice "2SA_0155"
    sachiko "\"Just knowing something is 'tasty' only takes one word, but you could use an infinite amount of words to describe the sensation after feeling it.\""

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0156"
    sachiko "\"Those sensations you can't describe with words, what someone started calling 'qualia'... that vast amount of data is the flood.\""

    voice "2SA_0157"
    sachiko "\"When you came down to earth and started enjoying all those sensations, they started pushing away the information you had.\""

    show miyako 1 sm pyjama_hood_b l with dict_dissolve_25

    voice "2MI_0146"
    miyako "\"Whakatangi... hanga...\""

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0158"
    sachiko "\"Everything you've got in that little head of yours is gonna be overwritten in no time.\""

    show sachiko 2 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0159"
    sachiko "\"You won't be able to remember everything like you have up until now. You'll have to {i}remember that you'll forget{/i}.\""

    show sachiko 2 sm outfit cigarette e with dict_dissolve_25

    voice "2SA_0160"
    sachiko "\"But sensation isn't second-hand like the information you had previously, it's something only yours, that you experienced yourself.\""

    show sachiko 2 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0161"
    sachiko "\"And the experiences you're going to have are worth enough to trade them for millions of years of information.\""

    show miyako 1 sm pyjama_hood_b e with dict_dissolve_25

    voice "2MI_0147"
    miyako "\"My own history...\""

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0162"
    sachiko "\"You don't need to remember trilobites, do you?\""

    show miyako 2 sm pyjama_hood e with Dissolve(0.25)
    show miyako:
        ShakeNo_3_750

    voice "2MI_0148"
    miyako "\"Ah...\""

    show miyako:
        xoffset 0 yoffset 0
    with None

    "She scowled. Guess she was never a fan of them."

    show sachiko 1 sm outfit cigarette g with dict_dissolve_25

    voice "2SA_0163"
    sachiko "\"Heheh, well, let me welcome you to the surface again.\""

    show miyako 1 sm pyjama_hood_a b with dict_dissolve_25

    voice "2MI_0149"
    miyako "\"Yes. Thank you for inviting me.\""

    "Miyako stared at Sachiko, her eyes sparkling."

    show sachiko 1 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0164"
    sachiko "\"Whoops, that went on a little long. We should—\""

    show miyako 1 sm pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0150"
    miyako "\"Please tell me more.\""

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0165"
    sachiko "\"Ah~, no, I can't. If you stay up here in that any longer, you'll freeze down to your core.'"

    show miyako:
        "miyako 2 sm pyjama_hood e" with Dissolve(0.25)
        1.5
        ShakeSide

    voice "2MI_0151"
    miyako "\"I'm not cold... brr.\""

    show miyako 2 sm pyjama_hood e:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0166"
    sachiko "\"You liar, you're shivering. Your breath is white, too.\""

    show miyako:
        "miyako 2 sm pyjama_hood f" with Dissolve(0.25)
        ShakeYes
        2.0
        ShakeYes

    voice "2MI_0152"
    miyako "\"Hoo... hoo...\""

    show miyako 2 sm pyjama_hood f:
        xoffset 0 yoffset 0
    with None

    "She breathed out to see."

    show sachiko 2 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0167"
    sachiko "\"Come on, you can marvel at that later.\""

    "Sachiko threw the butt of her cigarette in a pocket ashtray and reached out to Miyako."

    play sound se_bati
    show bati:
        xcenter 742 ycenter 384
    pause 0.15
    hide bati

    show miyako:
        "miyako 1 sm pyjama_hood_a f" with Dissolve(0.25)
        ShakeJump

    voice "2MI_0153"
    miyako "\"Hya?!\""

    show miyako 1 sm pyjama_hood_a f:
        xoffset 0 yoffset 0
    with None

    "Miyako yelped when Sachiko touched her cheek."

    show sachiko 2 sm outfit cigarette g with dict_dissolve_25

    voice "2SA_0168"
    sachiko "\"Oh, sorry. Guess my hand was colder.\""

    show miyako 1 sm pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0154"
    miyako "\"......\""

    "Her eyes were wide open."

    show sachiko 2 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0169"
    sachiko "\"Come on, let's go back in.\""

    "Sachiko beckoned her after picking up the can of coffee."

    show miyako 1 sm pyjama_hood_a a with dict_dissolve_25

    voice "2MI_0155"
    miyako "\"Will you talk to me again?\""

    "She was staring again."

    show sachiko 2 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0170"
    sachiko "\"Yeah, she's got some powerful eyes. It's hard to say no to her...\""

    show miyako 1 sm pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0156"
    miyako "\"Did you say something?\""

    show sachiko 1 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0171"
    sachiko "\"Nah. We can talk however much you want, but that's it for tonight. You can't be late on your first day, right?\""

    show miyako 2 sm pyjama_hood h with dict_dissolve_25

    voice "2MI_0157"
    miyako "\"Oh...\""

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0172"
    sachiko "\"Go right to sleep as soon as you get back to your room. You sleep a lot already.\""

    show miyako 2 sm pyjama_hood i with dict_dissolve_25

    voice "2MI_0158"
    miyako "\"Hwaaah...\""

    show sachiko 1 sm outfit cigarette h with dict_dissolve_25

    voice "2SA_0173"
    sachiko "\"Get into bed first!\""

    hide miyako
    hide sachiko
    with dict_dissolve_50

    "Sachiko headed for the door and Miyako followed."

    pause 0.5
    scene bg08ca with Dissolve(0.5)
    pause 1.5

    "........."

    "......"

    "There was that spark again."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
