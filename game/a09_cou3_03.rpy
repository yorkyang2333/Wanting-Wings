label a09_cou3_03:

    scene bg01ah with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Noon on Saturday. Rin and Hina were alone in the room."

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_1134"
    rin "\"Hm...\""

    "Rin was lying in front of the TV, channel surfing. She finally stopped on a rerun of a variety show."

    "On the screen, ten or so girls were fooling around in the snow. In bikinis."

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_1135"
    rin "\"Bikinis... that's rough.\""

    "It's the middle of winter..."

    "It must have been some segment on the show. From how confident they looked, they must have all been gravure idols or something."

    "The girls moved through a grove of trees before coming upon an open-air hot spring."

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_1136"
    rin "\"Huh~ That's a weird hot spring.\""

    "There were a bunch of hot springs the size of manhole covers, and the girls were each getting in one."

    "The girls excitedly entered the springs. They must have been freezing out there and wanted to warm themselves up as soon as possible."

    "But according to a caption on screen, a couple of the springs were {i}too hot{/i}."

    $ side_image = "rin 1 side pyjama glasses h"

    voice "2RI_1137"
    rin "\"I get it. It's Russian roulette... Going straight from cold to hot would suck.\""

    $ side_image = "hina 1 side pyjama_pjm n"

    voice "2HI_1097"
    hina "\"You know, talking to the TV like that makes you seem like an old man.\""

    "Hina's exasperated voice came from the kitchen."

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_1138"
    rin "\"Huh? Was I talking out loud?\""

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_1098"
    hina "\"Loud enough to hear in here.\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_1139"
    rin "\"Hmm...\""

    play sound se_tin
    pause 2.0

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_1140"
    rin "\"Were you heating something up?\""

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_1099"
    hina "\"Snacks Asou left for us. It's sweet potatoes. You want some?\""

    $ side_image = "rin 1 side pyjama glasses c"

    voice "2RI_1141"
    rin "\"I'll eat anything Fumi made~\""

    $ side_image = "hina 2 side pyjama_pjm e"

    voice "2HI_1100"
    hina "\"Yeah, yeah.\""

    "Hina put two forks on the plate."

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_1101"
    hina "\"You can't eat lying on the floor.\""

    $ side_image = "rin 1 side pyjama glasses c"

    voice "2RI_1142"
    rin "\"Yeah, yeah.\""

    show rin:
        "rin z4 1 lg pyjama glasses b flat"
        alpha 0.0 xcenter 298 ycenter 859
        easein 0.75 alpha 1.0 ycenter 759

    "Rin sluggishly sat up."

    show rin z4 1 lg pyjama glasses b:
        alpha 1.0 xcenter 298 ycenter 759
    with None

    show hina:
        "hina z4 2 lg pyjama_pjm f flat"
        alpha 0.0 xcenter 826
        easein 0.5 alpha 1.0 xcenter 726

    voice "2HI_1102"
    hina "\"That's a lot of skin for a daytime show. I wonder if they get complaints.\""

    show hina z4 2 lg pyjama_pjm f:
        alpha 1.0 xcenter 726
    with None

    "That's what Hina said when she came into the living room and saw the TV."

    show rin z4 1 lg pyjama glasses k with dict_dissolve_25

    voice "2RI_1143"
    rin "\"Complain about every show and we're gonna have a pretty boring world.\""

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_1103"
    hina "\"Nah, I think there should be all kinds of shows on TV. You just don't see girls in swimsuits on TV this early in the day lately.\""

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1144"
    rin "\"What's wrong with girls in swimsuits, anyway? It's just cute, right?\""

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_1104"
    hina "\"It's the commodification of sex or something. I don't know.\""

    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_1145"
    rin "\"Well, if it's a commodity, what's wrong with selling it? It's not just looks, it's smarts or a good singing voice or whatever. Everyone should sell what they're good at, right?\""

    voice "2RI_1145a"
    rin "\"Oh, you can't force someone to, though.\""

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1146"
    rin "\"But you should sell your stamina, Hina.\""

    show hina z4 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1105"
    hina "\"I get what you're saying, but it still pisses me off.\""

    show rin z4 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1147"
    rin "\"Oh, you get it? You're so smart, Hina~\""

    show hina:
        "hina z4 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1106"
    hina "\"Shut up!\""

    show hina z4 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01ah
    show bg_obi
    with bg_effect_05
    pause 0.5

    "Hina and Rin sat in a nice warm room eating snacks while they watched the girls play hot spring Russian roulette."

    show rin 1 lg pyjama glasses b at pos_l
    show hina 2 lg pyjama_pjm d at pos_r
    with Dissolve(0.25)

    voice "2RI_1148"
    rin "\"Guess there's no chance of a nip slip these days.\""

    show hina:
        2.8
        "hina 2 lg pyjama_pjm f" with Dissolve(0.25)

    voice "2HI_1107"
    hina "\"Well, it is the middle of the day. Oh, isn't that girl cute?\""

    show hina 2 lg pyjama_pjm f:
        pass
    with None

    "Hina pointed at one of the girls on screen."

    show rin:
        "rin 1 lg pyjama glasses e" with Dissolve(0.25)
        4.0
        "rin 1 lg pyjama glasses f" with Dissolve(0.25)

    voice "2RI_1149"
    rin "\"The one in the orange suit? Yeah, she's pretty cute. Fumi's cuter, though.\""

    show rin 1 lg pyjama glasses f:
        pass
    with None
    show hina 1 lg pyjama_pjm m with dict_dissolve_25

    voice "2HI_1108"
    hina "\"Guess so.\""

    "She agreed, unfazed by Rin's comment."

    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_1109"
    hina "\"What about the girl in the back, in the blue and white stripes? You like girls with big boobs, right?\""

    show rin:
        "rin 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeTameiki
        7.8
        "rin 1 lg pyjama glasses d" with Dissolve(0.25)

    voice "2RI_1150"
    rin "\"You don't get it. It's not just about size. The shape and texture, whether it matches their face or not... Fumi's boobs get a pass on all those points. They're the best in the world!\""

    show rin 1 lg pyjama glasses d:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1110"
    hina "\"That's pretty impressive. Asou's better than idols, huh?\""

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1151"
    rin "\"You noticed, eh? A non-idol who's cuter than idols. That's like a miracle that only happens once every thousand years.\""

    show hina 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_1111"
    hina "\"Alright, you've stopped making sense.\""

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1152"
    rin "\"And who's the super lucky girl dating this cuter-than-idols beauty? Ready?\""

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    $ voice2("hina","2HI_1112","rin","2RI_1153")
    hina_rin "\"It's Rin Ogata!\"\n\"......\"" (what_rest_indent=0)

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1154"
    rin "\"Join in!\""

    show hina:
        "hina 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1113"
    hina "\"No way!\""

    show hina 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_1155"
    rin "\"But what really gets me about Fumi is...\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1114"
    hina "\"...There's more?\""

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1156"
    rin "\"Her personality's the best!\""

    show hina:
        "hina 1 lg pyjama_pjm h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_1115"
    hina "\"Ah~ Yeah, I really get that. Only Asou could date you.\""

    show hina 1 lg pyjama_pjm h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_1157"
    rin "\"Huh? What's that mean?\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1116"
    hina "\"I'd be throwing punches every day dating you.\""

    "Heheh."

    show rin:
        "rin 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1158"
    rin "\"I'm sorry! I can't go out with you!\""

    show rin 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1117"
    hina "\"I didn't ask!\""

    show hina 1 lg pyjama_pjm g:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama_pjm e with dict_dissolve_25

    voice "2HI_1118"
    hina "\"You should really treat her like your future's at stake, you know. Don't come crying to me if she gets tired of taking care of you all the time.\""

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_1159"
    rin "\"She won't~\""

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_1119"
    hina "\"Where does that confidence even come from?\""

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_1160"
    rin "\"I'm gonna be Fumi's family in the future.\""

    show hina:
        "hina 1 lg pyjama_pjm g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1120"
    hina "\"You mean you're gonna be her dependent!\""

    show hina 1 lg pyjama_pjm g with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared == 1:
        jump a09_comn_05
    else:
        jump a09_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
