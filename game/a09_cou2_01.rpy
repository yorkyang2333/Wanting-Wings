label a09_cou2_01:



    scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm02

    "Lounging after dinner."

    "Rin was lying on her stomach, reading a book, and Hina was fiddling with her camera as she laid her head down on Rin's back."

    show rin 1 lg pyjama glasses g:
        xcenter 512
        ShakeSide
    with dict_dissolve_25

    voice "2RI_0929"
    rin "\"Urk.\""

    show rin 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0957"
    hina "\"Hm? Am I heavy?\""

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0930"
    rin "\"No, the clasp on your collar stabbed into me.\""

    $ side_image = "hina 1 side pyjama_pjm d"

    voice "2HI_0958"
    hina "\"Wah, sorry.\""

    show rin:
        xcenter 512
        easein 0.5 xcenter 772
    pause 1.0
    show hina:
        "hina 1 lg pyjama_pjm d flat"
        alpha 0.0 xcenter 252 ycenter 1081
        easein 1.0 alpha 1.0 ycenter 981

    "Hina sat up."

    show hina 1 lg pyjama_pjm d:
        alpha 1.0 xcenter 252 ycenter 981
    with None
    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0931"
    rin "\"It doesn't bother you to have it on all the time?\""

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0959"
    hina "\"No, not at all.\""

    show hina:
        ShakeYes2

    "Hina spun the collar around on her neck, changing the position of the clasp."

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_0932"
    rin "\"Make sure nobody sees that thing, okay?\""

    show hina 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0960"
    hina "\"I could say the same to you.\""

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0933"
    rin "\"What do you mean?\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0961"
    hina "\"When you stayed over at my house for New Year's, you left it on the counter in the bathroom.\""

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0934"
    rin "\"Huh? Did I?\""

    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0962"
    hina "\"You did. I didn't know what to tell my mom when she found it. I ended up saying it was Asou's dog Arthur's.\""

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_0935"
    rin "\"...Sorry about that.\""

    show hina 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_0963"
    hina "\"You need to take better care of it. I'm worried you're going to lose it.\""

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0936"
    rin "\"Well, I told you I tend to do that, didn't I?\""

    show hina:
        "hina 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0964"
    hina "\"Which is why you need to be careful! This is really important to both of us.\""

    show hina 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0937"
    rin "\"I think it'd be better if you held on to—\""

    show hina:
        "hina 1 lg pyjama_pjm o" with Dissolve(0.25)
        ShakeNo_4_500

    voice "2HI_0965"
    hina "\"Mmmmmh!\""

    show hina 1 lg pyjama_pjm o:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0938"
    rin "\"What's your deal, honestly? I gave it to you, so shouldn't it be yours now?\""

    "Hina and Rin seemed to have very different approaches to possessions."

    "Rin's pragmatic. She treats a thing as a thing."

    "On the other hand, to Hina, a thing is a physical representation of a feeling."

    "The thing itself is important to her as well, but it's also a vessel for more important things, like memories or promises."

    "This collar, for instance—"

    show hina 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0966"
    hina "\"This collar is the proof that I'm yours, Rin. I want you to treat it like it's me.\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0939"
    rin "\"Heavy...\""

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0967"
    hina "\"Huh? So I'm heavy?\""

    "She didn't get it."

    hide rin
    hide hina
    with dict_dissolve_50

    "Rin put her book down and stood up."

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0968"
    hina "\"Where are you going?\""

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0940"
    rin "\"Bathroom.\""

    $ side_image = "hina 2 side pyjama_pjm a"

    voice "2HI_0969"
    hina "\"I'll come with.\""

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0941"
    rin "\"You don't have to. It's cold. Who's really got the collar here, anyway?\""

    play sound se521
    pause 2.0

    show hina z4 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_0970"
    hina "\"Should I lose weight?\""

    "Hina looked at the door for a bit after Rin left, then turned around."

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0861"
    miyako "\"I don't think you're overweight.\""

    "This one didn't get it either."

    show hina:
        "hina z4 1 lg pyjama_pjm h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0971"
    hina "\"But Rin said I was heavy. Should I go on a diet like you, Asou?\""

    show hina z4 1 lg pyjama_pjm h:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 1 side pyjama j"

    voice "2FU_0800"
    fumi "\"Fgh?!\""

    "Friendly fire to Fumi."

    "Of course, part of the damage she did to herself, as she was in the process of reaching for a cookie."

    show hina:
        xcenter 512
        easein 0.5 xcenter 726
    pause 0.5

    show fumi z4 1 lg pyjama h:
        xcenter 298
    with { "master" : Dissolve(0.3) }

    voice "2FU_0801"
    fumi "\"Ahem... Listen, Natsume.\""

    "Pulling herself together (and putting the cookie back on the tray), Fumi turned to Hina."

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0802"
    fumi "\"When Ogata said 'heavy,' she meant your feelings, not your weight.\""

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0972"
    hina "\"My feelings?\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0803"
    fumi "\"Like... they might be a tiny bit of a load on her, maybe.\""

    "Fumi tried to choose her words carefully, but..."

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0973"
    hina "\"A load... Am I bothering Rin?\""

    "Tears formed in Hina's eyes."

    show fumi:
        "fumi z4 2 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    voice "2FU_0804"
    fumi "\"No, no, no! Not bothering, just, umm...\""

    show fumi z4 2 lg pyjama d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "miyako 1 side pyjama_b e"

    voice "2MI_0862"
    miyako "\"I think your sense of personal space is much smaller than Ogata's is.\""

    "Personal space. A sort of range around a person where they're not comfortable having other people."

    show fumi z4 1 lg pyjama d with dict_dissolve_25

    voice "2FU_0805"
    fumi "\"Yes, that's it! I just mean that different people want to be alone for different amounts of time and can feel constricted by different things!\""

    "Fumi clung desperately to the lifeboat Miyako had tossed her."

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0974"
    hina "\"I guess I get that. I know how Rin was last year.\""

    $ side_image = "miyako 1 side pyjama_b j"

    voice "2MI_0863"
    miyako "\"'I'm not really great in groups.'\""

    "An impromptu impression. It didn't really sound like her, though."

    show hina z4 1 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0975"
    hina "\"Heheh, yeah, that! Did you get a kick out of that?\""

    $ side_image = "miyako 1 side pyjama_b h"

    voice "2MI_0864"
    miyako "\"Yes. Oh, but don't tell Rin.\""

    "Hina's mood improved at that."

    show hina z4 2 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_0976"
    hina "\"Maybe she doesn't like me being too clingy.\""

    show fumi z4 1 lg pyjama b with dict_dissolve_25

    voice "2FU_0806"
    fumi "\"You've only just started going out. You'll have to find the distance that's comfortable to both of you from here on.\""

    show hina z4 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0977"
    hina "\"Thanks. I don't want her to think of me as heavy.\""

    show fumi z4 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0807"
    fumi "\"Don't hold it in too much, okay?\""

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0978"
    hina "\"Yeah, but I don't want to make Rin upset, so I'll do my best to cling to her less.\""

    show fumi z4 2 lg pyjama h with dict_dissolve_25

    voice "2FU_0808"
    fumi "\"...Natsume.\""

    $ side_image = "miyako 1 side pyjama_b c"

    voice "2MI_0865"
    miyako "\"Nom...\""

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0809"
    fumi "\"Ah...\""

    "A cookie."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou2_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
