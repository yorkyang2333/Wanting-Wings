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
    sachiko "\"Phew...\"" id a07_comn_10_8d2dc03e

    "She sucked smoke in, looking disgusted, then sighed it out."

    "...You should just quit."

    play sound se521
    pause 2.0

    $ side_image = "sachiko 1 side outfit cigarette a"

    voice "2SA_0135"
    sachiko "\"Ah, it's the lion.\"" id a07_comn_10_c95270a9

    show miyako 2 sm pyjama f at pos_rs with dict_dissolve_25

    voice "2MI_0133"
    miyako "\"R-Roar~?\"" id a07_comn_10_228d54e6

    "The lion attempted."

    show sachiko 1 sm outfit cigarette a at pos_ls with dict_dissolve_25

    voice "2SA_0136"
    if persistent.dpatch:
        sachiko "\"What's up? Nervous about starting your school life?\"" id a07_comn_10_f5a85661
    else:
        sachiko "\"What's up? Nervous about starting academy life?\"" id a07_comn_10_e1088c95

    show miyako 2 sm pyjama d with dict_dissolve_25

    voice "2MI_0134"
    miyako "\"No, I'm not... well, maybe a little.\"" id a07_comn_10_303adbd2

    show sachiko 1 sm outfit cigarette g with dict_dissolve_25

    voice "2SA_0137"
    sachiko "\"You'll be fine. You've got those girls with you.\"" id a07_comn_10_39eabee6

    show miyako 1 sm pyjama_a e with Dissolve(0.25)
    show miyako:
        ShakeYes

    voice "2MI_0135"
    miyako "\"Yes. ...Oh, here.\"" id a07_comn_10_8ba8b18f

    show miyako:
        xoffset 0 yoffset 0
    with None

    "The lion took a can of coffee out of her pocket."

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0138"
    sachiko "\"You're a marsupial lion.\"" id a07_comn_10_cd928315

    "Thylacoleo looks nothing like that."

    show sachiko:
        "sachiko 1 sm outfit cigarette g" with Dissolve(0.25)
        0.5
        "sachiko 1 sm outfit cigarette h" with Dissolve(0.25)
        ShakeSide

    voice "2SA_0139"
    sachiko "\"Thank—cold!\"" id a07_comn_10_ad3c230a

    show sachiko 1 sm outfit cigarette h:
        xoffset 0 yoffset 0
    with None

    "Sachiko yelped when she touched the can."

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_0136"
    miyako "\"The vending machine only had cold ones...\"" id a07_comn_10_6585eb01

    show sachiko 2 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0140"
    sachiko "\"R-Right.\"" id a07_comn_10_a9c6c857

    "She brought that on herself."

    show sachiko 2 sm outfit cigarette e with dict_dissolve_25

    voice "2SA_0141"
    sachiko "\"Guess I'll have this later. Aren't you cold?\"" id a07_comn_10_d597990b

    "They were warm pajamas, but they weren't meant to be worn outside."

    show miyako 2 sm pyjama c with dict_dissolve_25

    voice "2MI_0137"
    miyako "\"I am cold, but I like it.\"" id a07_comn_10_2e3e94fe

    "Even the cutting chill was a fun new experience for her."

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0142"
    sachiko "\"You know, humans catch colds.\"" id a07_comn_10_be7750a6

    "She said sternly."

    show sachiko 1 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0143"
    sachiko "\"I get your excitement, but you've gotta get used to having a human body.\"" id a07_comn_10_2b720890

    "For better and for worse."

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0144"
    sachiko "\"You should learn from your first experience with the cake.\"" id a07_comn_10_b76d5f92

    show miyako 2 sm pyjama e with dict_dissolve_25

    voice "2MI_0138"
    miyako "\"Aaah...\"" id a07_comn_10_575ccadc

    "That struck a chord with her."

    show miyako 1 sm pyjama_a c with dict_dissolve_25

    voice "2MI_0139"
    miyako "\"There's a lot to remember.\"" id a07_comn_10_4b3031fc

    show miyako:
        "miyako 1 sm pyjama_hood_a c" with Dissolve(0.25)
        ShakeYes

    "Miyako said, donning her hood."

    show miyako 1 sm -pyjama_a pyjama_hood_a c:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0145"
    sachiko "\"Not to mention all you'll forget.\"" id a07_comn_10_b6dbd5f9

    show miyako 1 sm pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0140"
    miyako "\"Huh? Forget?\"" id a07_comn_10_d7039378

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0146"
    sachiko "\"Taumata?\"" id a07_comn_10_4c835343

    "Sachiko prompted, instead of answering her question."

    show miyako 2 sm pyjama_hood a with dict_dissolve_25

    voice "2MI_0141"
    miyako "\"Whakatangihangakoa... ua... uo... huh?\"" id a07_comn_10_c47804e2

    "She'd hesitated for a moment, then attempted to continue, however..."

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0147"
    sachiko "\"Can't come up with the rest, right?\"" id a07_comn_10_e74b7a2b

    show miyako:
        "miyako 2 sm pyjama_hood b" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0142"
    miyako "\"...What is this?\"" id a07_comn_10_7f7c5361

    show miyako 2 sm pyjama_hood b:
        xoffset 0 yoffset 0
    with None

    "Miyako looked worriedly at Sachiko. She was confused that she couldn't remember something she should have known."

    show sachiko 2 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0148"
    sachiko "\"That's a {i}human memory{/i}. I told you, you have a human body now, right?\"" id a07_comn_10_d508acfd

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0149"
    sachiko "\"You can only remember what fits up here. It's not stored in the cloud like it was up until now.\"" id a07_comn_10_efef8a5e

    "Sachiko tapped her temple."

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0150"
    sachiko "\"It's not just your capacity, too. The flood of sensation will wash away whatever information you have now.\"" id a07_comn_10_44ffdaee

    show miyako 2 sm pyjama_hood f with dict_dissolve_25

    voice "2MI_0143"
    miyako "\"Flood of sensation?\"" id a07_comn_10_636866a8

    voice "2SA_0151"
    sachiko "\"You were enjoying the sensation of 'cold' before, right? That's a huge amount of data.\"" id a07_comn_10_ed355bfc

    show miyako 2 sm pyjama_hood a with dict_dissolve_25

    voice "2MI_0144"
    miyako "\"......\"" id a07_comn_10_ed1b4304

    "Her face was blank, the information not quite processed yet."

    show sachiko 2 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0152"
    sachiko "\"...Let's see... Can you describe the sensation of 'cold' without using that word?\"" id a07_comn_10_2711893c

    show miyako 1 sm pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0145"
    miyako "\"The chill of the wind... made my skin hurt... and my fingers numb, umm...\"" id a07_comn_10_4cd46f43

    show sachiko 2 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0153"
    sachiko "\"Was that all you felt? It was just a part of the sensation, right? It's impossible to describe the entirety of the experience in words.\"" id a07_comn_10_69a62031

    show sachiko 2 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0154"
    sachiko "\"Let me give you another example. The {i}information{/i} that 'apples taste good' and the {i}sensation{/i} of 'eating a tasty apple' are two pieces of data with wildly different sizes.\"" id a07_comn_10_9c468e27

    show sachiko 2 sm outfit cigarette d with dict_dissolve_25

    voice "2SA_0155"
    sachiko "\"Just knowing something is 'tasty' only takes one word, but you could use an infinite amount of words to describe the sensation after feeling it.\"" id a07_comn_10_c43e6742

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0156"
    sachiko "\"Those sensations you can't describe with words, what someone started calling 'qualia'... that vast amount of data is the flood.\"" id a07_comn_10_c0286499

    voice "2SA_0157"
    sachiko "\"When you came down to earth and started enjoying all those sensations, they started pushing away the information you had.\"" id a07_comn_10_8c6ce991

    show miyako 1 sm pyjama_hood_b l with dict_dissolve_25

    voice "2MI_0146"
    miyako "\"Whakatangi... hanga...\"" id a07_comn_10_4e844662

    show sachiko 2 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0158"
    sachiko "\"Everything you've got in that little head of yours is gonna be overwritten in no time.\"" id a07_comn_10_e3038071

    show sachiko 2 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0159"
    sachiko "\"You won't be able to remember everything like you have up until now. You'll have to {i}remember that you'll forget{/i}.\"" id a07_comn_10_4945b84b

    show sachiko 2 sm outfit cigarette e with dict_dissolve_25

    voice "2SA_0160"
    sachiko "\"But sensation isn't second-hand like the information you had previously, it's something only yours, that you experienced yourself.\"" id a07_comn_10_98955e80

    show sachiko 2 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0161"
    sachiko "\"And the experiences you're going to have are worth enough to trade them for millions of years of information.\"" id a07_comn_10_8c66879e

    show miyako 1 sm pyjama_hood_b e with dict_dissolve_25

    voice "2MI_0147"
    miyako "\"My own history...\"" id a07_comn_10_3c8b4901

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0162"
    sachiko "\"You don't need to remember trilobites, do you?\"" id a07_comn_10_09f039b3

    show miyako 2 sm pyjama_hood e with Dissolve(0.25)
    show miyako:
        ShakeNo_3_750

    voice "2MI_0148"
    miyako "\"Ah...\"" id a07_comn_10_1d224f33

    show miyako:
        xoffset 0 yoffset 0
    with None

    "She scowled. Guess she was never a fan of them."

    show sachiko 1 sm outfit cigarette g with dict_dissolve_25

    voice "2SA_0163"
    sachiko "\"Heheh, well, let me welcome you to the surface again.\"" id a07_comn_10_04ebb589

    show miyako 1 sm pyjama_hood_a b with dict_dissolve_25

    voice "2MI_0149"
    miyako "\"Yes. Thank you for inviting me.\"" id a07_comn_10_a730128a

    "Miyako stared at Sachiko, her eyes sparkling."

    show sachiko 1 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0164"
    sachiko "\"Whoops, that went on a little long. We should—\"" id a07_comn_10_b6841879

    show miyako 1 sm pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0150"
    miyako "\"Please tell me more.\"" id a07_comn_10_5d7bd919

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0165"
    sachiko "\"Ah~, no, I can't. If you stay up here in that any longer, you'll freeze down to your core.'" id a07_comn_10_52cccc72

    show miyako:
        "miyako 2 sm pyjama_hood e" with Dissolve(0.25)
        1.5
        ShakeSide

    voice "2MI_0151"
    miyako "\"I'm not cold... brr.\"" id a07_comn_10_7a1e86d3

    show miyako 2 sm pyjama_hood e:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit cigarette c with dict_dissolve_25

    voice "2SA_0166"
    sachiko "\"You liar, you're shivering. Your breath is white, too.\"" id a07_comn_10_9ef1823d

    show miyako:
        "miyako 2 sm pyjama_hood f" with Dissolve(0.25)
        ShakeYes
        2.0
        ShakeYes

    voice "2MI_0152"
    miyako "\"Hoo... hoo...\"" id a07_comn_10_21a29880

    show miyako 2 sm pyjama_hood f:
        xoffset 0 yoffset 0
    with None

    "She breathed out to see."

    show sachiko 2 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0167"
    sachiko "\"Come on, you can marvel at that later.\"" id a07_comn_10_045ea133

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
    miyako "\"Hya?!\"" id a07_comn_10_51c8368f

    show miyako 1 sm pyjama_hood_a f:
        xoffset 0 yoffset 0
    with None

    "Miyako yelped when Sachiko touched her cheek."

    show sachiko 2 sm outfit cigarette g with dict_dissolve_25

    voice "2SA_0168"
    sachiko "\"Oh, sorry. Guess my hand was colder.\"" id a07_comn_10_e2d6cc9a

    show miyako 1 sm pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0154"
    miyako "\"......\"" id a07_comn_10_6be754bb

    "Her eyes were wide open."

    show sachiko 2 sm outfit cigarette f with dict_dissolve_25

    voice "2SA_0169"
    sachiko "\"Come on, let's go back in.\"" id a07_comn_10_3e2a6efa

    "Sachiko beckoned her after picking up the can of coffee."

    show miyako 1 sm pyjama_hood_a a with dict_dissolve_25

    voice "2MI_0155"
    miyako "\"Will you talk to me again?\"" id a07_comn_10_8eabd2de

    "She was staring again."

    show sachiko 2 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0170"
    sachiko "\"Yeah, she's got some powerful eyes. It's hard to say no to her...\"" id a07_comn_10_e307da0e

    show miyako 1 sm pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0156"
    miyako "\"Did you say something?\"" id a07_comn_10_1cd36223

    show sachiko 1 sm outfit cigarette b with dict_dissolve_25

    voice "2SA_0171"
    sachiko "\"Nah. We can talk however much you want, but that's it for tonight. You can't be late on your first day, right?\"" id a07_comn_10_5561e203

    show miyako 2 sm pyjama_hood h with dict_dissolve_25

    voice "2MI_0157"
    miyako "\"Oh...\"" id a07_comn_10_768e8b0f

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25

    voice "2SA_0172"
    sachiko "\"Go right to sleep as soon as you get back to your room. You sleep a lot already.\"" id a07_comn_10_9aa358c4

    show miyako 2 sm pyjama_hood i with dict_dissolve_25

    voice "2MI_0158"
    miyako "\"Hwaaah...\"" id a07_comn_10_6723589f

    show sachiko 1 sm outfit cigarette h with dict_dissolve_25

    voice "2SA_0173"
    sachiko "\"Get into bed first!\"" id a07_comn_10_89a09cad

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
