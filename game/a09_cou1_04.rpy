label a09_cou1_04:

    scene bg09ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Hina and Miyako had come to the manager's room."

    "Hina started up the laptop on Sachiko's desk and placed a CD in the disc tray, plugging in her MP3 player."

    "There wasn't a computer in their room, so when she wanted to put new music on her player, she had to come here."

    show bg_obi
    show sachiko 1 lg outfit a at pos_l
    show hina 2 lg pyjama_pjm f at pos_r
    with dict_dissolve_50

    voice "2HI_0888"
    hina "\"What program do I use, Sachiko?\""

    voice "2SA_0696"
    sachiko "\"Rin installed something... Oh, here it is.\""

    "She clicked on a musical note icon, and the software started up, reading the data from the CD."

    voice "2SA_0697"
    sachiko "\"Now you just follow the prompts and go through your CDs.\""

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0889"
    hina "\"Okay. Thanks.\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0698"
    sachiko "\"You really listen to some oldies, don't you?\""

    "Sachiko picked up a CD from the stack, which was all western music from the 80s and 90s."

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0890"
    hina "\"Yeah, it's all stuff my dad recommended me. I've got space on my player, so I borrowed a bunch of them over New Year's.\""

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0834"
    miyako "\"They've got dollar prices on them. Are they imported?\""

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0891"
    hina "\"Nah, he bought them over there. Dad was overseas most of the time when he was younger. He's fluent in English!\""

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0835"
    miyako "\"Wow~ That's amazing.\""

    "It's amazing how bad Hina is at English with a dad like that, too."

    show sachiko 1 lg outfit c with dict_dissolve_25

    voice "2SA_0699"
    sachiko "\"How do you fit in listening to just stuff like this? What do you sing at karaoke?\""

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0892"
    hina "\"What do you mean? I sing stuff like this. Here, I'll show y—\""

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0700"
    sachiko "\"That's okay.\""

    "A hasty \"no thank you.\""

    show hina 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0893"
    hina "\"Rude.\""

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0836"
    miyako "\"I like your singing. It's untamed.\""

    "Like an animal?"

    show hina 1 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0894"
    hina "\"You've got a rocker's soul, Miyako.\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0701"
    sachiko "\"Oh yeah. Don't open this folder or this folder or this folder or this folder.\""

    show hina:
        "hina 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0895"
    hina "\"That's a lot! That's everything on the desktop!\""

    show hina 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    hide sachiko with Dissolve(0.25)

    show miyako 2 lg pyjama a at pos_l with dict_dissolve_25

    voice "2MI_0837"
    miyako "\"What's in them? The names sound pretty impressive... 'Amazing!' and 'Spectacle!' and 'Fantastic!'\""

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0702"
    sachiko "\"Well, I'd show you, but Hinacchi would get mad.\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0896"
    hina "\"You will show nothing. The only thing that's not dirty on here is the wallpaper!\""

    "Somewhat unexpectedly, her desktop wallpaper was still the default image."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0703"
    sachiko "\"Well, of course it isn't. I use this computer for work and bring it to meetings and stuff.\""

    show hina 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0897"
    hina "\"It's for work, and you've got this stuff on it?!\""

    "Click."

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0838"
    miyako "\"Wow, there's so many naked ladies~\""

    show hina:
        "hina 1 lg pyjama_pjm h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0898"
    hina "\"She opened one...\""

    show hina 1 lg pyjama_pjm h with None
    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg09ca with bg_effect_05
    pause 0.5

    "........."

    "Hina's music transfer finished, and Miyako began opening all the folders on Sachiko's desktop, beginning with \"Amazing!\" and \"Spectacle!\""

    show bg_obi
    show miyako 1 lg pyjama_a i
    with dict_dissolve_25

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0704"
    sachiko "\"Having fun?\""

    show miyako 1 lg pyjama_a k with dict_dissolve_25

    voice "2MI_0839"
    miyako "\"I don't know, but I just feel like I have to open them all and see what's inside!\""

    "She's lost in the sheer number of files."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0705"
    sachiko "\"You'll be here 'til morning.\""

    hide bg_obi
    hide miyako
    with dict_dissolve_50

    $ side_image = "hina 1 side pyjama_pjm n"

    voice "2HI_0899"
    hina "\"......\""

    "Hina raised her head from where she was leaning against the bed, gathering all her CDs together."

    $ side_image = "hina 2 side pyjama_pjm h"

    voice "2HI_0900"
    hina "\"...Hey, Sachiko?\""

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0706"
    sachiko "\"Y-Yes?\""

    "Sachiko turned around timidly."

    $ side_image = "hina 2 side pyjama_pjm d"

    voice "2HI_0901"
    hina "\"I want to ask you something.\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0707"
    sachiko "\"You're not mad about the porn?\""

    $ side_image = "hina 2 side pyjama_pjm h"

    voice "2HI_0902"
    hina "\"No, just...\""

    "She hesitated for a moment, then..."

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0903"
    hina "\"Sachiko, have you had sex?\""

    show sachiko:
        "sachiko z4 1 lg outfit h" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0708"
    sachiko "\"Gbfh?!\""

    show sachiko z4 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    "Sachiko spluttered at the sudden question."

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0709"
    sachiko "\"...Am I being propositioned?\""

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0904"
    hina "\"I'm not propositioning you!\""

    play sound se_2s_g002

    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0710"
    sachiko "\"Gufh!\""

    show sachiko z4 1 lg outfit d with None
    hide sachiko with dict_dissolve_25

    "Hina threw a pillow that landed a direct hit on Sachiko's face."

    show hina z4 2 lg pyjama_pjm d:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_0905"
    hina "\"Have you, Miyako?\""

    show miyako z4 1 lg pyjama_a g:
        xcenter 298
    with dict_dissolve_25

    voice "2MI_0840"
    miyako "\"Not yet, no~\""

    "The blunt question was met with a blithe answer."

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0841"
    miyako "\"Why do you ask, though?\""

    "She did understand that it wasn't like Hina to ask something like that."

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0906"
    hina "\"I don't know what I should do with Fumi.\""

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0842"
    miyako "\"Haven't you done it a few times already, though?\""

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0907"
    hina "\"Yeah, but... I want to get better at it. I want to make Fumi feel good.\""

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0843"
    miyako "\"I see~\""

    "Sachiko looked somewhat befuddled at the extremely frank conversation the girls were having."

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0908"
    hina "\"But you know all about that stuff, right, Sachiko?\""

    "Naturally, the conversation turned to her."

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0711"
    sachiko "\"O-Of course! Ask me anything!\""

    show hina z4 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0909"
    hina "\"Thanks. I've got a ton of stuff I want to know.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0844"
    miyako "\"I'm interested, too.\""

    $ side_image = "sachiko 2 side outfit i"

    voice "2SA_0712"
    sachiko "\"Uhh, err...\""

    pause 0.5
    scene white with bg_effect_27_750
    pause 1.0

    "—At the same time."

    window hide

    pause 0.5

    scene bg01cg with bg_effect_27_750
    pause 0.5

    play music bgm01

    show fumi z4 2 lg pyjama a:
        xcenter 298
    with dict_dissolve_25

    window auto

    voice "2FU_0741"
    fumi "\"Do you have a minute, Ogata?\""

    "Fumi set some tea on the table and sat down."

    $ side_image = "rin 2 side pyjama g"

    voice "2RI_0874"
    rin "\"Hm? What's with the formality?\""

    show rin:
        "rin z4 2 lg pyjama glasses a flat"
        alpha 0.0 xcenter 726 ycenter 859
        easein 1.0 alpha 1.0 ycenter 759

    "Rin was lying under the table, but she sat up when she saw the serious look on Fumi's face."

    show rin z4 2 lg pyjama glasses a:
        alpha 1.0 xcenter 726 ycenter 759
    with None
    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0742"
    fumi "\"I have something I'd like to know, and you're the only one I trust to ask about it.\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0875"
    rin "\"Well, I'm not sure what I've done to earn this trust, but ask away.\""

    show fumi z4 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0743"
    fumi "\"Thank you. So, the thing is, umm...\""

    show rin:
        "rin z4 1 lg pyjama glasses k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0876"
    rin "\"Uh huh...?\""

    show rin z4 1 lg pyjama glasses k:
        xoffset 0 yoffset 0
    with None

    "Rin sipped her tea, waiting for Fumi to continue."

    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0744"
    fumi "\"Please teach me about sex!\""

    hide rin
    show rin 1 lg pyjama glasses j as rin_1:
        xcenter 772 ycenter 1016
        function LayerShake(20,20,0.3)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_0877"
    rin "\"Bhwh?!\""

    show rin 1 lg pyjama glasses j as rin_1 with None
    hide fumi
    hide rin_1
    with dict_dissolve_50

    "She spit out the tea in her mouth, and spilled the rest from her mug."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01cg with bg_effect_05
    pause 0.5

    show fumi 2 lg pyjama b at pos_l
    show rin 1 lg pyjama glasses g at pos_r
    with dict_dissolve_25

    voice "2FU_0745"
    fumi "\"You should probably change everything under your jacket. Please take it off; I'll wash it.\""

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0878"
    rin "\"Uh, okay.\""

    hide rin with dict_dissolve_25

    "Rin stood and took her pants off."

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0879"
    rin "\"Good thing nothing got on my kimono.\""

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0746"
    fumi "\"...Yes.\""

    show fumi:
        ShakeYes

    "Fumi smiled, taking Rin's track pants from her."

    show fumi 1 lg pyjama b:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2FU_0747"
    fumi "\"Do you have a spare pair?\""

    $ side_image = "rin 2 side pyjama glasses e"

    voice "2RI_0880"
    rin "\"Yeah, I'm good. Anyway, that surprised me. I didn't think you'd ask me that all of a sudden.\""

    show fumi 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0748"
    fumi "\"I'm sorry.\""

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0881"
    rin "\"It's okay. Just gotta get over the shock of hearing the word 'sex' come out of your mouth.\""

    show fumi 1 lg pyjama j with dict_dissolve_25

    voice "2FU_0749"
    fumi "\"I'm sorry, I'm sorry, I'm sorry!\""

    show rin 2 lg pyjama glasses f at pos_r with dict_dissolve_25

    voice "2RI_0882"
    rin "\"Really though, where is this coming from? Oh, you're not propositioning me, are you?\""

    show fumi 2 lg pyjama d with Dissolve(0.25)
    show fumi:
        ShakeNo

    voice "2FU_0750"
    fumi "\"I'm not, I'm not!\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0883"
    rin "\"Ahaha, I'm kidding. You're asking because of Hina, right?\""

    show fumi:
        "fumi 2 lg pyjama h" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0751"
    fumi "\"...Yes. I don't know what to do.\""

    show fumi 2 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0884"
    rin "\"What, you don't want to do it with her?\""

    show fumi 1 lg pyjama g with dict_dissolve_25

    voice "2FU_0752"
    fumi "\"No, that's not it! I want to do it a lot more!\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0885"
    rin "\"A-Ah.\""

    show fumi 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0753"
    fumi "\"But neither of us know the first thing about it...\""

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0754"
    fumi "\"Of course, Hina's trying her hardest, but there must be something I can do, too.\""

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0755"
    fumi "\"So, I came to you because I figured you know a lot about it.\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0886"
    rin "\"......\""

    "Her face was blank. Well, of course it was. This was basically her punishment."

    show rin 2 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0887"
    rin "\"Er, y'see... I don't know that I'd say I know a lot about it... since I've never... done it...\""

    play sound se521
    pause 1.0

    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_0910"
    hina "\"We're back, Fumi, and we brought Sachi—aaah!\""

    show rin 2 lg pyjama glasses a with Dissolve(0.25)
    show rin:
        4.0
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0888"
    rin "\"Oh, hey—wait, what? Ah, N-No, th-this isn't...!!\""

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0911"
    hina "\"CHWAAAAH!!\""

    play sound se_2s_k007

    show fumi 2 lg pyjama d with dict_dissolve_25
    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False
    pause 0.5

    camera
    with None

    scene white with bg_effect_05
    pause 1.5

    scene bg02dg with bg_effect_25_750
    pause 0.5

    play music bgm01

    show sachiko z4 1 lg outfit a:
        xcenter 298
    show rin z4 1 lg pyjama glasses g:
        xcenter 726
    with Dissolve(0.25)

    show rin:
        ShakeTameiki

    voice "2RI_0889"
    rin "\"Ouch... Those guys are really putting me through the wringer today.\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin massaged her cheek."

    voice "2SA_0713"
    sachiko "\"I mean, she sees a pantsless girl about to pounce on her girlfriend... Can't blame her for bringing out the knee, really.\""

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_0890B"
    rin "\"I just spilled some tea and was changing! Don't say 'pantsless'!\""

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "She was no longer pantsless."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0714"
    sachiko "\"Well, what do we do about this?\""

    "Rin and Sachiko had left the others in the living room and were now, of course, discussing..."

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0891B"
    rin "\"You can't just ask me about sex in real life. It's purely in the realm of fiction for me right now.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0715"
    sachiko "\"Hinacchi came at me with the real naked truth about everything. And it's like the more innocent she is, the more guilty I feel.\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0892"
    rin "\"Ugh, I get that.\""

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0716"
    sachiko "\"Anyway, can you really talk specifics with them?\""

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0893"
    rin "\"Not me. I'm pure as an angel.\""

    show sachiko z4 1 lg outfit d with Dissolve(0.25)
    show sachiko:
        ShakeTameiki

    voice "2SA_0717"
    sachiko "\"Physically, maybe. I guess it's like a rookie racer asking for advice from an unlicensed gaming addict.\""

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0894"
    rin "\"Ugh. I'm not really sure, but I get the feeling you just hit the nail on the head, and I don't like it...\""

    show rin z4 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    "One real experience, even if less than perfect, is better than one hundred magnificent descriptions."

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0895"
    rin "\"Then I guess it's up to the experienced Miss Sachiko.\""

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0718"
    sachiko "\"Hey, that's not fair.\""

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0896"
    rin "\"What, you're not going to tell me you're inexperienced? You talk like you're the authority on eros!\""

    show sachiko z4 2 lg outfit h with dict_dissolve_25

    voice "2SA_0719"
    sachiko "\"O-Of course I'm experienced! Super experienced! I'm practically a pro!\""

    "Heheheh."

    show sachiko z4 2 lg outfit j with dict_dissolve_25

    voice "2SA_0720"
    sachiko "\"But what am I supposed to tell them to do? Foreplay?\""

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0897"
    rin "\"When I parted her firmly shut thighs, I found her slit already hot and dripping with honey, twitching...\""

    show sachiko z4 1 lg outfit e
    show rin z4 1 lg pyjama glasses d
    with dict_dissolve_25

    $ voice2("rin","2RI_0898","sachiko","2SA_0721N")
    rin_sachiko "\"Aaaaah!\""

    "They both covered their faces with their hands."

    $ side_image = "miyako 1 side pyjama_a c"

    voice "2MI_0845"
    miyako "\"If they both love each other and speak honestly to each other, won't they find the way that works for them naturally?\""

    show sachiko z4 1 lg outfit h
    show rin z4 1 lg pyjama glasses j
    with dict_dissolve_25
    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    $ voice2("rin","2RI_0899","sachiko","2SA_0722")
    rin_sachiko "\"Waaah?!\""

    camera
    with None

    "Miyako made her way into the farce the two of them were putting on."

    $ side_image = "miyako 1 side pyjama_b b"

    voice "2MI_0846"
    miyako "\"I was just wondering when you were coming back.\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0723"
    sachiko "\"Ah, umm... we're coming.\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01cg with bg_effect_26_750
    pause 0.5

    play music bgm01

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0724"
    sachiko "\"If you both love each other and speak honestly to each other—\""

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_0900"
    rin "\"Whoa, she copied her!\""

    show sachiko 2 lg outfit i with Dissolve(0.25)
    show sachiko:
        2.0
        "sachiko 1 lg outfit i" with Dissolve(0.25)

    voice "2SA_0725"
    sachiko "\"Hey, shut it.\n —Won't you find the way that works for you naturally?\""

    show sachiko 1 lg outfit i:
        pass
    with None
    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0756"
    fumi "\"I see...\""

    "She said, though her face didn't seem to entirely agree."

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0912"
    hina "\"What? What do you mean?\""

    "This one wants details."

    hide sachiko with Dissolve(0.25)

    show fumi z4 2 lg pyjama h:
        xcenter 118
    show hina z4 1 lg pyjama_pjm k behind fumi, sachiko:
        xcenter 383
    show sachiko z4 2 lg outfit i:
        xcenter 852
    with dict_dissolve_25

    voice "2SA_0726"
    sachiko "\"Umm, basically, just talk to each other about it.\""

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0913"
    hina "\"We are talking... aren't we?\""

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0757"
    fumi "\"...We are.\""

    "They weren't the type to keep secrets from each other. They were just going in circles because of their lack of information on the subject."

    show hina z4 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_0914"
    hina "\"Is there like a textbook on sex?\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0727"
    sachiko "\"A textbook, eh...?\""

    $ side_image = "rin 1 side pyjama b"

    voice "2RI_0901"
    rin "\"True, there's plenty of that kind of thing for a man and a woman, but for two women... I don't think I've ever seen one.\""

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0758"
    fumi "\"Really?\""

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0902"
    rin "\"Well, if you're talking numbers—\""

    show sachiko:
        "sachiko z4 2 lg outfit d" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0728"
    sachiko "\"......\""

    show sachiko z4 2 lg outfit d:
        xoffset 0 yoffset 0
    with None

    "Sachiko cleared her throat and elbowed Rin."

    $ side_image = "rin 2 side pyjama d"

    voice "2RI_0903"
    rin "\"Oh...\""

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0915"
    hina "\"Isn't that what the books you two read are like?\""

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0729r2"
    sachiko "\"No, no, no! You can't learn anything from those! They're useless!\""

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_0904"
    rin "\"That's right! In fact, all those will do is give you weird fetishes.\""

    show sachiko z4 1 lg outfit j with dict_dissolve_25
    $ side_image = "rin 1 side pyjama i"

    $ voice2("rin","2RI_0905","sachiko","2SA_0730")
    rin_sachiko "\"Hey, don't point at me!\""

    $ side_image = "miyako 1 side pyjama_a d"

    voice "2MI_0847"
    miyako "\"Ahahaha.\""

    "Miyako laughed while Hina and Fumi merely stared blankly."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
