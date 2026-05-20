label a08_comn_13:

    scene bg09cc with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "With the soup put away, the hotpot party was nearing its end."

    "All was well with the lovers, and their dear friend was by their side."

    "A little ways away, the two former angels watched over them warmly."

    show bg_obi
    show sachiko z4 1 lg outfit a:
        xcenter 298
    show miyako z4 1 lg pyjama_a b:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0461"
    miyako "\"Are you drunk?\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0329"
    sachiko "\"A little. Can you tell?\""

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0462"
    miyako "\"You seem to be enjoying yourself a lot.\""

    "Sachiko was tipsy. Pretty impressive considering she'd put away half a bottle of sake by herself."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0330"
    sachiko "\"The booze is good, but I'm also just enjoying watching those girls.\""

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0463"
    miyako "\"Ah...\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0331"
    sachiko "\"They're so stupid, right?\""

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0464"
    miyako "\"Stupid? ...Are they?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0332"
    sachiko "\"They laugh and cry over the most trivial things. They spend every day going through so many emotions.\""

    voice "2SA_0333"
    sachiko "\"But no matter how trivial it seems from the outside, to them, it's all so serious.\""

    voice "2SA_0334"
    sachiko "\"They're the protagonists of a super sweet, slightly bitter story right now, and they can't see anything outside of it. They're each other's entire world right now.\""

    show miyako z4 1 lg pyjama_a i with dict_dissolve_25

    voice "2MI_0465"
    miyako "\"......\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0335"
    sachiko "\"Just a drunk poem. Don't take it too seriously.\""

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0466"
    miyako "\"No...\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0336"
    sachiko "\"Anyway, when you're in love, your head gets completely full of that person, and you suddenly forget about everything else.\""

    show miyako z4 1 lg pyjama_a i with dict_dissolve_25

    voice "2MI_0467"
    miyako "\"The flood of sensation...\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0337"
    sachiko "\"Yep. Major flooding. Love is a natural disaster, baby♪\""

    voice "2MI_0468"
    miyako "\"......\""

    "Miyako stared at the couple once again."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0338"
    sachiko "\"Are you jealous?\""

    show miyako z4 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0469"
    miyako "\"I suppose so. I'd like to experience it for myself at least once.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0339"
    sachiko "\"You're so cute, you'll find someone in no time.\""

    "—Whose heart did that stake stab?"

    show miyako z4 2 lg pyjama f with dict_dissolve_25

    voice "2MI_0470"
    miyako "\"Have you—\""

    hide sachiko
    show sachiko 1 lg outfit g as sachiko_1
    with dict_dissolve_25

    voice "2SA_0340"
    sachiko "\"You show-offs! How dare you!!\""

    hide bg_obi
    hide sachiko_1
    hide miyako
    with dict_dissolve_50

    "Sachiko jumped on the three girls as if to avoid Miyako's question."

    play audio se_2s_g001
    play audio se_2s_g004
    play audio se_2s_e013

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0582"
    rin "\"Whoa! What?!\""

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "hina 1 side pyjama_pjm d"

    voice "2HI_0570"
    hina "\"You smell like booze!\""

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "fumi 1 side pyjama j"

    voice "2FU_0493"
    fumi "\"Aaah! Who's touching me there?\""

    camera
    with None

    $ side_image = "sachiko 1 side outfit e"

    voice "2SA_0341"
    sachiko "\"Heheheheh.\""

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0571"
    hina "\"HEY!\""

    play sound kickingbox

    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    "In all the chaos, Hina's leg bumped a shelf."

    camera
    with None

    "Something square tumbled down from the shelf. It was a canvas."

    play sound canbas

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0342"
    sachiko "\"Oww?!\""

    "The canvas bounced off Sachiko's back, flipped over itself a few times, and arrived at Miyako's knees."

    show miyako 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0471"
    miyako "\"......\""

    "Miyako picked up the canvas and turned it over."

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0343"
    sachiko "\"Ah, no, you can't look at that one!\""

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0472"
    miyako "\"Huh...?\""

    "But she was too late. The canvas had already been revealed."

    "It was the portrait of a girl in a uniform."

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0473"
    miyako "\"Is this... me?\""

    "Miyako turned the painting to the pile of the four girls."

    hide miyako with Dissolve(0.5)

    show fumi z4 2 lg pyjama g:
        xcenter 118
    show sachiko z4 2 lg outfit d behind fumi, hina:
        xcenter 383
    show hina z4 1 lg pyjama_pjm k:
        xcenter 641
    show rin z4 1 lg pyjama glasses e:
        xcenter 906
    with Dissolve(0.5)

    voice "2HI_0572"
    hina "\"It's Miyako!\""

    voice "2SA_0344"
    sachiko "\"Uh oh...\""

    "It was almost certain that the girl on the canvas and the girl holding it were the same person."

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "2FU_0494"
    fumi "\"That's a very nice smile.\""

    "The girl in the painting had a brilliant smile on her face."

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0583"
    rin "\"That's pretty intense...\""

    "Compared to the paintings they'd all been looking at before, this one had been given a very different touch."

    "It was rough, and a lot more simple, but because of that, there was much more emotion in it."

    show sachiko z4 2 lg outfit g with dict_dissolve_25

    voice "2SA_0345"
    sachiko "\"No... Umm, that's just...\""

    "Sachiko was flustered."

    show fumi 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0495"
    fumi "\"You didn't know about this painting, Miyako?\""

    show hina 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0573"
    hina "\"You didn't model for it?\""

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_0474"
    miyako "\"Oh, no...\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0584"
    rin "\"So she got secret pictues of you? Criminal!\""

    show sachiko z4 1 lg outfit j with dict_dissolve_25

    voice "2SA_0346"
    sachiko "\"I did not! I painted it from memory!\""

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0585"
    rin "\"So you've looked at Mikoyan so much you can paint her from memory, eh?\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0347"
    sachiko "\"......\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0586"
    rin "\"I bet in your imagination, it's a nude—\""

    show sachiko:
        "sachiko z4 1 lg outfit j" with Dissolve(0.25)
        ShakeJump

    voice "2SA_0348"
    sachiko "\"It's not a nude, right?!\""

    show sachiko z4 1 lg outfit j:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0587"
    rin "\"Oh, I guess you're right.\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0574"
    hina "\"You haven't imagined it?\""

    show sachiko:
        ShakeJump

    voice "2SA_0349"
    sachiko "\"I can imagine, can't I?!\""

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0575"
    hina "\"You can't!\""

    show sachiko:
        ShakeJump

    voice "2SA_0350"
    sachiko "\"I have freedom of thought and belief!\""

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "2FU_0496"
    fumi "\"It's a little unfair that you've only painted Miyako, though~\""

    "Fumi was sharp as usual."

    show fumi 2 lg pyjama e with dict_dissolve_25

    voice "2FU_0497"
    fumi "\"Do you sense something bittersweet about this?\""

    show sachiko:
        "sachiko z4 1 lg outfit f" with Dissolve(0.25)
        ShakeNo

    voice "2SA_0351"
    sachiko "\"I-I'll paint you anytime you want, Foomin.\""

    show sachiko z4 1 lg outfit f:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg pyjama f with dict_dissolve_25

    voice "2FU_0498"
    fumi "\"No nudes, please.\""

    hide fumi
    hide sachiko
    hide hina
    hide rin
    with dict_dissolve_50

    "Sachiko's response was so unusual for her that the three couldn't help mocking her."

    show miyako 2 lg pyjama c with dict_dissolve_25

    voice "2MI_0475"
    miyako "\".........\""

    "But Miyako looked a little happy, holding the canvas to her chest."

    if routes_cleared >= 2:
        jump a08_comn_13_a
    else:
        jump a08_comn_13_b

label a08_comn_13_a:

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0476"
    miyako "\"...Huh?\""

    "She noticed some small writing on the back of the canvas."

    "And then gasped."

    jump a08_comn_13_b

label a08_comn_13_b:

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0477"
    miyako "\"Ah...\""

    $ side_image = "sachiko 2 side outfit h"

    voice "2SA_0352"
    sachiko "\"Alright, I'm confiscating that!\""

    "Sachiko grabbed the canvas hurriedly, face red, and put it back on the shelf."

    show miyako 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0478"
    miyako "\"......\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
