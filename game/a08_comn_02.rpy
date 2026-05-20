label a08_comn_02:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm01

    if persistent.dpatch:
        "After school. There was a gaggle of girls around Fumi's desk." id a08_comn_02_c077e2c0
    else:
        "After class. There was a gaggle of girls around Fumi's desk."

    "Rin and Miyako looked on from a little ways away."

    show hina 1 lg school k at pos_l
    show rin 1 lg school a at pos_r
    with dict_dissolve_25

    voice "2HI_0425"
    hina "\"Hm? What's going on over there?\""

    "Hina joined them after returning from the faculty room."

    voice "2RI_0458"
    rin "\"Valentine chocolate recipe class.\""

    show hina:
        "hina 1 lg school a" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0426"
    hina "\"Ah, I see.\""

    show hina 1 lg school a:
        xoffset 0 yoffset 0
    with None

    "Hina understood right away."

    show rin 2 lg school a with dict_dissolve_25

    voice "2RI_0459"
    rin "\"Everyone knows she lives at a bakery, her dad's a patissier, and she's a great cook. Of course she's got students lining up.\""

    show hina 2 lg school g with dict_dissolve_25

    voice "2HI_0427"
    hina "\"Haha, she could charge tuition. Isn't it a little early, though? It's still January.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "2RI_0460"
    rin "\"Well, it's the preparation that's fun with events like this... probably.\""

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_0428"
    hina "\"Hmm.\""

    if persistent.dpatch:
        "The prelude to Valentine's Day. Even though it's a girls' school? Or maybe this is the sort of scene you'd {i}only{/i} see at a girls' school." id a08_comn_02_2269b5d9
    else:
        "The prelude to Valentine's Day. Even though it's a girls' school? Or maybe this is the sort of scene you'd {i}only{/i} see at an all-girls' campus."

    if routes_cleared != 0:
        jump a08_comn_02_a
    else:
        jump a08_comn_02_b

label a08_comn_02_a:

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_0461"
    rin "\"Come to think of it, what took you so long?\""

    show hina 1 lg school k with dict_dissolve_25

    voice "2HI_0429"
    hina "\"Ah, I just got asked to put away the mic from the auditorium.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "2RI_0462"
    rin "\"Hm? It didn't get put away after class?\""

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_0430"
    hina "\"Actually, the mic in the auditorium wasn't working, so they had to grab one from the broadcasting room.\""

    show rin 1 lg school e with dict_dissolve_25

    voice "2RI_0463"
    rin "\"And you had to put it back. So you swung by the broadcasting room?\""

    show hina 1 lg school n with dict_dissolve_25

    voice "2HI_0431"
    hina "\"No... I haven't yet.\""

    "She was hesitating to say something."

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_0432"
    hina "\"Once Fumi's class is over, do you want to go together?\""

    show rin 1 lg school h with dict_dissolve_25

    voice "2RI_0464"
    rin "\"I don't mind, but this looks like it's gonna take a while. You could go now and—\""

    show hina 2 lg school b with dict_dissolve_25

    voice "2HI_0433"
    hina "\"I'd be bored if I went by myself! Don't they say the more the merrier?\""

    show rin 2 lg school g with dict_dissolve_25

    voice "2RI_0465"
    rin "\"For just taking a microphone back to the broadcasting... oh.\""

    "Rin had a realization."

    show rin 1 lg school f with dict_dissolve_25

    voice "2RI_0466"
    rin "\"Ahh, there was a rumor about the broadcasting room being haunted, wasn't there?\""

    show hina 1 lg school o with Dissolve(0.25)
    show hina:
        ShakeNo

    voice "2HI_0434"
    hina "\"Waaah, don't say that~\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school k with dict_dissolve_25

    voice "2RI_0467"
    if persistent.dpatch:
        rin "\"People sometimes hear a voice from the broadcasting room trying to say something. And it goes out to the whole school through the speakers...\"" id a08_comn_02_a_128a8310
    else:
        rin "\"People sometimes hear a voice from the broadcasting room trying to say something. And it goes out to the whole campus through the speakers...\""

    show hina:
        "hina 1 lg school g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0435"
    hina "\"Gyaaaaa!!\""

    show hina 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "Haunted school broadcasts, eh?"

label a08_comn_02_b:

    hide hina with Dissolve(0.5)

    show miyako 1 lg school_a b at pos_l with dict_dissolve_25

    voice "2MI_0305"
    miyako "\"......\""

    show rin 2 lg school a with dict_dissolve_25

    voice "2RI_0468"
    rin "\"What's up, Mikoyan?\""

    show miyako 1 lg school_a c with dict_dissolve_25

    voice "2MI_0306"
    miyako "\"I kind of like this restless energy.\""

    show rin 2 lg school g with dict_dissolve_25

    voice "2RI_0469"
    rin "\"Y-You do?\""

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_0307"
    miyako "\"Doesn't it feel like it might start smelling sweet in here?\""

    "Miyako took a deep breath."

    $ side_image = "hina 2 side school f"

    voice "2HI_0436"
    hina "\"Like chocolate?\""

    show rin 1 lg school g with dict_dissolve_25

    voice "2RI_0470"
    rin "\"Now that, it's a bit early for.\""

    "Miyako was sensing life in the pre-Valentine's classroom air."

    "It was probably close to the sensation she felt observing the three girls as an angel."

    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0471"
    rin "\"By the way, have you ever given or gotten chocolate, Mikoyan?\""

    show miyako 2 lg school c with dict_dissolve_25

    voice "2MI_0308"
    miyako "\"I haven't~ It's my first Valentine's.\""

    $ side_image = "hina 2 side school e"

    voice "2HI_0437"
    hina "\"Was she in a country that doesn't celebrate Valentine's Day?\""

    show rin 1 lg school h with dict_dissolve_25

    voice "2RI_0472"
    rin "\"Like Saudi Arabia or something?\""

    $ side_image = "hina 2 side school f"

    voice "2HI_0438"
    hina "\"Wait, really?\""

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_0473"
    rin "\"They have capital punishment, too.\""

    $ side_image = "hina 1 side school d"

    voice "2HI_0439"
    hina "\"Whaaat?!\""

    show miyako 2 lg school a with dict_dissolve_25

    voice "2MI_0309"
    miyako "\"Hm?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a08_cou1_01
    elif route2 == 2:
        jump a08_cou2_01
    elif route2 == 3:
        jump a08_cou3_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
