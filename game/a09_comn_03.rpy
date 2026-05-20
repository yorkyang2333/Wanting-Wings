label a09_comn_03:

    scene bg09ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se_2s_f001
    pause 2.0

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0443"
    sachiko "\"Yeah?\""

    $ side_image = "fumi 1 side pyjama b"

    voice "2FU_0585"
    fumi "\"It's Asou.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0444"
    sachiko "\"Come in~\""

    hide sachiko with Dissolve(0.5)

    play sound se521
    pause 1.5

    show fumi:
        "fumi 1 lg pyjama b flat"
        alpha 0.0 xcenter 612
        easein 0.75 alpha 1.0 xcenter 512
    pause 0.75

    voice "2FU_0586"
    fumi "\"Good evening. Is now a good time?\""

    show fumi 1 lg pyjama b:
        alpha 1.0 xcenter 512

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0445"
    sachiko "\"Yeah, yeah, perfectly fine. Come on in, sit down, sit down.\""

    hide fumi with Dissolve(0.5)

    show fumi z4 1 lg pyjama b:
        xcenter 298
    with dict_dissolve_50

    "Fumi sat down on the stool Sachiko had indicated."

    show sachiko z4 2 lg outfit c:
        xcenter 726
    with dict_dissolve_25

    voice "2SA_0446"
    sachiko "\"Let's see... we'll angle you a little more... this way.\""

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0587"
    fumi "\"...?\""

    "Sachiko made minute adjustments to Fumi's position on the stool."

    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0447"
    sachiko "\"Okay, could you start by undoing two buttons?\""

    show fumi z4 1 lg pyjama e with dict_dissolve_25

    voice "2FU_0588"
    fumi "\"Huh? Huh?\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0448"
    sachiko "\"Don't worry, don't worry~ I'll paint you real pretty!\""

    show fumi:
        "fumi z4 1 lg pyjama j" with Dissolve(0.25)
        ShakeJump

    voice "2FU_0589"
    fumi "\"No! Umm! I'm not here to model!\""

    show fumi z4 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0449"
    sachiko "\"Huh? You're not?\""

    show fumi z4 1 lg pyjama g with dict_dissolve_25

    voice "2FU_0590"
    fumi "\"I'm not!\""

    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0450"
    sachiko "\"Damn.\""

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0591"
    fumi "\"I just had something I wanted to ask you.\""

    show sachiko:
        "sachiko z4 1 lg outfit e" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0451"
    sachiko "\"Perfect! We'll take turns, then. I'm going first! When'd you get your first bra?\""

    show sachiko z4 1 lg outfit e:
        xoffset 0 yoffset 0
    with None
    show fumi z4 1 lg pyjama j with dict_dissolve_25

    voice "2FU_0592"
    fumi "\"That's not what I'm here for!\""

    play sound se521
    pause 1.0

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_0761"
    rin "\"Sachiko, you got a minute?\""

    show fumi z4 1 lg pyjama h
    show sachiko z4 1 lg outfit i
    with dict_dissolve_25

    voice "2SA_0452"
    sachiko "\"Ah, it's Rin.\""

    show fumi:
        xcenter 298
        easein 0.5 xcenter 172
    show sachiko behind fumi, rin:
        xcenter 726
        easein 0.5 xcenter 512
    pause 0.5

    show rin:
        "rin z4 2 lg pyjama glasses g flat"
        alpha 0.0 xcenter 952
        easein 1.0 alpha 1.0 xcenter 852
    pause 1.0

    voice "2RI_0762"
    rin "\"Oh, you've already got a visitor. Are you two busy?\""

    show rin z4 2 lg pyjama glasses g:
        alpha 1.0 xcenter 852
    with None
    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0453"
    sachiko "\"We're having a dirty little girls' night where we share our secrets with each other. The first question is 'when did Foomin get her first bra?'\""

    show rin z4 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0763"
    rin "\"What are you talking about...? So, when was it?\""

    show fumi z4 1 lg pyjama j with Dissolve(0.25)
    show fumi:
        ShakeJump

    voice "2FU_0593"
    fumi "\"It's not a dirty girls' night, and I'm not answering that!\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    $ voice2("rin","2RI_0764","sachiko","2SA_0454")
    rin_sachiko "\"Damn.\""

    show fumi z4 1 lg pyjama g with dict_dissolve_25

    voice "2FU_0594"
    fumi "\"I came to ask Sachiko something.\""

    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0765"
    rin "\"Oh, so did I.\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0455"
    sachiko "\"Something dirty?\""

    show fumi:
        "fumi z4 1 lg pyjama g" with Dissolve(0.25)
        ShakeNo_4_500

    voice "2FU_0595"
    fumi "\"No!\""

    show fumi z4 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None
    play sound se521
    pause 1.0

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0750"
    hina "\"Sachiko, can I ask you something~?\""

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0456"
    sachiko "\"Wow, now Hinacchi's here.\""

    show fumi:
        xcenter 172
        easein 0.5 xcenter 118
    show sachiko:
        xcenter 512
        easein 0.5 xcenter 383
    show rin:
        xcenter 852
        easein 0.5 xcenter 906
    pause 0.5

    show hina behind rin:
        "hina z4 2 lg pyjama_pjm f flat"
        alpha 0.0 xcenter 741
        easein 1.0 alpha 1.0 xcenter 641
    pause 1.0

    voice "2HI_0751"
    hina "\"Wait, what's everybody doing here?\""

    show hina z4 2 lg pyjama_pjm f:
        alpha 1.0 xcenter 641
    with None
    show sachiko z4 1 lg outfit e with dict_dissolve_25

    voice "2SA_0457"
    sachiko "\"A dirty girls' night where we take turns confessing our secrets.\""

    show hina z4 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0752"
    hina "\"What...?\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0458"
    sachiko "\"The first question is about when we got our first bras. I guess it's too soon to ask you that, though.\""

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0753"
    hina "\"I wear a bra!\""

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0459"
    sachiko "\"What kind?\""

    show hina:
        "hina z4 1 lg pyjama_pjm e" with Dissolve(0.25)
        ShakeYes2

    voice "2HI_0754"
    hina "\"This kin—\""

    show hina z4 1 lg pyjama_pjm e:
        xoffset 0 yoffset 0
    with None
    show fumi:
        "fumi z4 1 lg pyjama j" with Dissolve(0.25)
        ShakeJump
        ShakeJump
        ShakeJump
        ShakeJump

    voice "2FU_0596"
    fumi "\"Wah, wah, wah, wah!\""

    show fumi z4 1 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    "Fumi hurriedly prevented Hina from lifting her sweatshirt up."

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0460"
    sachiko "\"So close.\""

    "Sachiko snapped her fingers."

    "...This has happened before, hasn't it?"

    show fumi z4 1 lg pyjama g with dict_dissolve_25

    voice "2FU_0597"
    fumi "\"It's not a dirty girls' night!\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0461"
    sachiko "\"Hmmmph.\""

    "You have no right to be hmphing."

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0755"
    hina "\"Do you have someone you like right now, Sachiko?\""

    "She brought the conversation back on topic with a super direct question. That's Hina for you."

    show sachiko z4 2 lg outfit i with dict_dissolve_25

    voice "2SA_0462"
    sachiko "\"Are you sure this isn't a dirty girls' night?\""

    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0598"
    fumi "\"Please just take the 'dirty' off.\""

    show rin z4 2 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0766"
    rin "\"Have you ever even been in love before?\""

    show sachiko z4 1 lg outfit j with dict_dissolve_25

    voice "2SA_0463"
    sachiko "\"Of course I have! What do you think I am, a robot?! Love installation complete!\""

    "{i}Are{/i} you a robot?"

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0756"
    hina "\"It wasn't just lust?\""

    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0464"
    sachiko "\"Hey, hey, heeey! Foomin, they're being mean!\""

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg pyjama b with dict_dissolve_25

    voice "2FU_0599"
    fumi "\"They usually say nice things about you. Right?\""

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0767"
    rin "\"She's good-looking if you look close enough, but she's an old man on the inside.\""

    show hina z4 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0757"
    hina "\"She's more reliable than you'd think, but she's dirty, too.\""

    show sachiko z4 2 lg outfit i with dict_dissolve_25

    voice "2SA_0465"
    sachiko "\"I dunno if that counts...\""

    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0600"
    fumi "\"Come on, you two~\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0768"
    rin "\"Anyway, getting back on track, are you seeing anyone?\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0466"
    sachiko "\"Does it look like I'm—\""

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0769"
    rin "\"No, it doesn't.\""

    show sachiko z4 1 lg outfit j with dict_dissolve_25

    voice "2SA_0467"
    sachiko "\"If you're just gonna use the question as an excuse to dig at me, then don't ask it! You're just gonna make me sad!\""

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0758"
    hina "\"And there's nobody you like?\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0468"
    sachiko "\"I like you, Hinacchi~!\""

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0759"
    hina "\"Yeah, yeah, whatever!\""

    "Hina dodged out of the way of Sachiko's attempted hug."

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0601"
    fumi "\"There's really no one you have feelings for?\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0469"
    sachiko "\"I have feelings for all cute girls♪\""

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0770"
    rin "\"Yeah, I really can't picture her in love.\""

    show sachiko:
        "sachiko z4 1 lg outfit c" with Dissolve(0.25)
        2.5
        "sachiko z4 1 lg outfit f" with Dissolve(0.25)

    voice "2SA_0470"
    sachiko "\"I'm telling you, I've been in love. The brief realization of a love that wasn't to be, and then an eternal parting—but those feelings became kindling for a flame that burns even now in my breast, never allowing my heart to take another step forward or a step back—\"" (last_what_size=11.5)

    show sachiko z4 1 lg outfit f:
        pass
    with None
    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0470a"
    sachiko "\"I'm quite devoted despite appearances, you know.\""

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0771"
    rin "\"But you're single right now.\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0471"
    sachiko "\"You really show no mercy, huh?\""

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0602"
    fumi "\"Umm, can I ask you about Miyako next?\""

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0472"
    sachiko "\"Hm? She gettin' into trouble?\""

    stop music fadeout 1.0

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0603"
    fumi "\"No, she's a very good girl, but I want to ask what your feelings for her are.\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0772"
    rin "\"Yeah, that.\""

    play music bgm02 fadein 1.0

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0473"
    sachiko "\"My feelings? Well, I fully agree that she's a good girl.\""

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0760"
    hina "\"But what are your feelings for her?\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0474"
    sachiko "\"I told you, I think she's a good—\""

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0604"
    fumi "\"Miyako loves you.\""

    "Fumi interrupted her."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0475"
    sachiko "\"...I love her, too.\""

    "She looked confused for just a second before she answered."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0476"
    sachiko "\"She's family. I'd barely met her before she moved in, though.\""

    show fumi z4 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0605"
    fumi "\"Not that kind of love...\""

    voice "2SA_0477"
    sachiko "\"What other kind of love is there?\""

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0773"
    rin "\"Romantic love.\""

    show sachiko:
        "sachiko z4 1 lg outfit b" with Dissolve(0.25)
        2.8
        "sachiko z4 1 lg outfit j" with Dissolve(0.25)

    voice "2SA_0478"
    sachiko "\"Haha, well, we're cousins—ooh, but maybe that makes it sexier!\""

    show sachiko z4 1 lg outfit j:
        pass
    with None
    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0774"
    rin "\"This isn't a joke.\""

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0606"
    fumi "\"Have you not noticed Miyako's feelings, Sachiko?\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0479"
    sachiko "\"Your feelings are painfully obvious, Foomin—\""

    show fumi z4 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0607"
    fumi "\"I have no romantic feelings for you.\""

    show sachiko z4 1 lg outfit j with dict_dissolve_25

    voice "2SA_0480"
    sachiko "\"Rejected! That hurts!\""

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0775"
    rin "\"She's so dense. I feel sorry for Mikoyan.\""

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0761"
    hina "\"Yeah, but she said she likes her anyway.\""

    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0608"
    fumi "\"You mean because of that.\""

    "Fumi elbowed Hina."

    show sachiko z4 1 lg outfit c
    show fumi z4 2 lg pyjama h
    with dict_dissolve_25

    voice "2FU_0609"
    fumi "\"Miyako is really too much of an angel. She's so gentle and kind.\""

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0776"
    rin "\"And she's beautiful, too. She's a snooze monster, but her sleeping face is angelic! I just saw it when I left the room!\""

    show hina z4 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0762"
    hina "\"She's like an angel, because, umm...\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0777"
    rin "\"...Hina?\""

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0763"
    hina "\"H-Her boobs are big...\""

    show rin:
        "rin z4 1 lg pyjama glasses k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0778"
    rin "\"I'm proud of you for getting that out, Hina.\""

    show rin z4 1 lg pyjama glasses k:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg pyjama_pjm o with Dissolve(0.25)
    show hina:
        ShakeNo_2_250

    voice "2HI_0764"
    hina "\"Ugh...\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0481"
    sachiko "\"Nothing but praise for Mikoyan, huh? Not like me.\""

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None
    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0610"
    fumi "\"Anyway, we're rooting for Miyako!\""

    show hina z4 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0765"
    hina "\"And we won't let you make her cry!\""

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0779"
    rin "\"This is the last chance you're ever gonna get, Sachiko.\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0482"
    sachiko "\"It's pretty soon for this to be my last chance ever, isn't it?\""

    "They all went about it in different ways, but they were trying to back Miyako up."

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0483"
    sachiko "\"I understand well your feelings of friendship, but this is gonna be between me and Miyako.\""

    "She looked exasperated."

    show sachiko z4 2 lg outfit i with dict_dissolve_25

    voice "2SA_0484"
    sachiko "\"I mean, she hasn't actually said anything to {i}me{/i} yet, you know?\""

    show fumi z4 1 lg pyjama h
    show hina z4 1 lg pyjama_pjm d
    show rin z4 1 lg pyjama glasses e
    with dict_dissolve_25

    voice "2FU_0611"
    fumi "\"...Oh.\""

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0485"
    sachiko "\"We can't exactly go over her head on this, can we?\""

    "The three girls all exchanged a glance."

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0766"
    hina "\"...We're sorry.\""

    show rin z4 2 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_0780"
    rin "\"...We got ahead of ourselves.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0486"
    sachiko "\"It's fine. Thanks for looking out for Miyako.\""

    "She gave the three now-quiet girls a pat on the head."

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0612"
    fumi "\"...Sachiko?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0487"
    sachiko "\"Hm?\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0613B"
    fumi "\"If Miyako does tell you her feelings, then—\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0488"
    sachiko "\"It's legal with consent!\""

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0781"
    rin "\"Hina, get her in the knees!\""

    hide hina
    if hina_choker == "":
        show hina_1_150_pyjama_f as hina_1:
            xcenter 654 ycenter 1245
            ShakeYes
    elif hina_choker == "_choker":
        show expression Flatten(Composite((2423,3399),(0,0),"hina_1_150_pyjama_f.webp",(0,0),"hina_1_150_pyjama_choker.webp")) as hina_1:
            xcenter 654 ycenter 1245
            ShakeYes
    with dict_dissolve_25

    voice "2HI_0767"
    hina "\"Chwaaaaah!!\""

    show sachiko:
        "sachiko z4 1 lg outfit h" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0489"
    sachiko "\"Gwaaah!!\""

    play sound se_2s_k006

    hide rin
    hide hina_1
    hide sachiko
    with Dissolve(0.5)

    pause 1.0

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0614"
    fumi "\"......\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg09ca with bg_effect_05
    pause 0.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0490"
    sachiko "\"Good night.\""

    "Sachiko closed her door when the girls left."

    stop music fadeout 1.0

    play sound se521
    pause 2.0

    show sachiko z4 2 lg outfit d with Dissolve(0.5)

    pause 0.5

    voice "2SA_0491"
    sachiko "\"...I'm not an idiot.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
