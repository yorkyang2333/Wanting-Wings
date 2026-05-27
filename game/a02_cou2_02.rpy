label a02_cou2_02:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01cc with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin z3 1 lg pyjama glasses b behind hina at pos_r2_z3
    show hina z3 1 lg pyjama b
    show fumi z3 2 lg pyjama b behind hina at pos_l2_z3
    with Dissolve(0.25)

    voice "RIN_0435"
    rin "\"Do we have a corkscrew?\"" id a02_cou2_02_33b5fd27

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0412"
    fumi "\"Oh, there was one in the bag.\"" id a02_cou2_02_bc45863d

    show rin z3 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0436"
    rin "\"Ahaha. After the first mistake, your dad was really on top of things, huh?\"" id a02_cou2_02_163878e7

    "Rin took the corkscrew from Fumi and stabbed it into a bottle wrapped in shiny foil."

    "It even had a little Christmas wreath on it."

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0594"
    hina "\"What's that?\"" id a02_cou2_02_d778a7e7

    "Hina glanced over, chewing on a Santa made of sugar."

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0437"
    rin "\"Dom Perignon.\"" id a02_cou2_02_a3b279c4

    voice "HIN_0595"
    hina "\"What's that?\"" id a02_cou2_02_b5b7984c

    show fumi z3 2 lg pyjama f with dict_dissolve_25

    voice "FUM_0413"
    fumi "\"It's really expensive alcohol, but that's not what this is.\"" id a02_cou2_02_3c014cb1

    show rin z3 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0438"
    rin "\"It's non-alcoholic champagne. A necessity for a kiddy Christmas party like this.\"" id a02_cou2_02_ba1b66d6

    show hina z3 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0597"
    hina "\"It's my birthday party!\"" id a02_cou2_02_3cba524c

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0414"
    fumi "\"Oh, can you get the cork?\"" id a02_cou2_02_c3996a6a

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0439"
    rin "\"I'll be careful not to make a mess~\"" id a02_cou2_02_7fc7a794

    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0598"
    hina "\"Hey, don't point the business end of that thing at me!\"" id a02_cou2_02_2bd6fc21

    play sound cork

    "Hina was clearly nervous, but Rin removed the cork skillfully and quietly."

    show rin z3 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0440"
    rin "\"Gimme your cup.\"" id a02_cou2_02_a569d1a3

    show hina z3 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0599"
    hina "\"I've never had this before.\"" id a02_cou2_02_e61a1b56

    play sound se008a

    "Hina watched the small bubbles pop in her cup with great interest."

    stop sound fadeout 1.0

    "Next, Rin poured for Fumi."

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0415"
    fumi "\"Here, you should have some, too.\"" id a02_cou2_02_f5b2e4fc

    play sound se008a

    "Fumi took the bottle and poured for Rin."

    stop sound fadeout 1.0

    show rin z3 1 lg pyjama glasses f with dict_dissolve_25

    voice "RIN_0441"
    rin "\"You free tonight, babe?\"" id a02_cou2_02_bd939011

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0416"
    fumi "\"Enough with that.\"" id a02_cou2_02_48acbe9d

    "Fumi slapped the hand Rin had grabbed her with, and Rin laughed, bringing the cup to her mouth."

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0442"
    rin "\"Oh, this is real champagne.\"" id a02_cou2_02_417a9b43

    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0417"
    fumi "\"Oh, you're right...\"" id a02_cou2_02_62925287

    "The two exchanged a glance after both taking a sip."

    show fumi z3 1 lg pyjama g with dict_dissolve_25

    voice "FUM_0418"
    fumi "\"Another mistake of my father's, I suppose... Oh, how scatterbrained can he be?\"" id a02_cou2_02_de9e13dc

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0443"
    rin "\"Hina, this is alcho—\"" id a02_cou2_02_bba4cf5c

    stop music fadeout 1.0

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0600"
    hina "\"Ahahahahahahahahaha!\"" id a02_cou2_02_c515b776

    show rin:
        "rin z3 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeSide

    show fumi:
        "fumi z3 1 lg pyjama e" with Dissolve(0.25)
        ShakeJump

    $ voice2("rin","RIN_0444","fumi","FUM_0419")
    rin_fumi "\"?!\""

    show rin z3 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    show fumi z3 1 lg pyjama e:
        xoffset 0 yoffset 0
    with None

    play music bgm01

    "Jovial laughter filled the room."

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_0601"
    hina "\"This is so much fun!\"" id a02_cou2_02_9dfb08df

    "The two spun around to find a glassy-eyed Hina."

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0420"
    fumi "\"She's not—\"" id a02_cou2_02_6dd945ac

    show rin z3 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0445"
    rin "\"Already plastered?\"" id a02_cou2_02_306df06d

    voice "HIN_0602"
    hina "\"Oookaaay! Le'ss drink all night long!\"" id a02_cou2_02_51149bf6

    "Hina threw her cup back."

    show rin z3 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_0446"
    rin "\"All that from one sip, eh?\"" id a02_cou2_02_990ef705

    "Rin took the cup from Hina."

    show hina:
        "hina z3 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0603"
    hina "\"Hey, what're you doing?! Give that back!\"" id a02_cou2_02_bfbfe5f2

    show hina z3 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None

    "Hina reached up and flailed her arms against Rin, trying to get the cup back, but she couldn't win against the height difference."

    show rin z3 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0447"
    rin "\"Well, what shall we do about this?\"" id a02_cou2_02_5af43810

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0421"
    fumi "\"Hmm...\"" id a02_cou2_02_0a1fb7d2

    "They exchanged another glance."

    show hina z3 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0604"
    hina "\"Phyaaa!\"" id a02_cou2_02_d02ad90f

    "Hina was spinning around, the top of her head held down by Rin."

    show rin z3 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0448"
    rin "\"How about you go get Sachiko to dispose of the bottle, Asou?\"" id a02_cou2_02_a597bde0

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0422"
    fumi "\"Oh, okay.\"" id a02_cou2_02_3d89f68a

    show fumi:
        "fumi z3 2 lg pyjama g flat"
        alpha 1.0 xcenter 182
        easeout 0.5 alpha 0.0 xcenter 282
    pause 0.5

    hide fumi with None
    show hina z3 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0605"
    hina "\"Hey, what're you two whishpering about?!\"" id a02_cou2_02_a0d7bed4

    "Fumi rushed out of the room, cradling the bottle like it was a bomb."


    show hina:
        "hina z3 1 lg pyjama l" with Dissolve(0.25)
        zoom 1.0 xcenter 512 ycenter 959
        easein 0.25 zoom 1.039 xcenter 252 ycenter 981
    show rin:
        "rin z3 2 lg pyjama glasses c" with Dissolve(0.25)
        zoom 1.0 xcenter 842 ycenter 994
        easein 0.25 zoom 1.039 xcenter 772 ycenter 1016

    voice "RIN_0449"
    rin "\"Hey. You don't need to go after her.\"" id a02_cou2_02_130ad0ab


    show hina -z3 1 lg pyjama l at pos_l:
        zoom 1.0 xcenter 252 ycenter 981
    show rin -z3 2 lg pyjama glasses c at pos_r:
        zoom 1.0 xcenter 772 ycenter 1016
    with None

    show hina:
        "hina 2 lg pyjama j" with Dissolve(0.25)
        zoom 1.0 xcenter 252 ycenter 981
        ShakeSide

    voice "HIN_0607"
    hina "\"Mgyuh!\"" id a02_cou2_02_5918d176

    show hina 2 lg pyjama j:
        xoffset 0 yoffset 0
    with None

    "Hina made a strangled noise when Rin grabbed her hood to stop her."

    show hina:
        "hina 1 lg pyjama g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0608"
    hina "\"Ngyaaa! Lemme gooo! Meanie! Pervert! I'll sue you!\"" id a02_cou2_02_559d0bba

    show hina 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None

    "No matter how much she struggled, the difference in their builds proved an insurmountable obstacle."

    voice "RIN_0450"
    rin "\"You're a real lightweight, huh?\"" id a02_cou2_02_05aec258

    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0609"
    hina "\"Stop treating me like a kid!\"" id a02_cou2_02_9e86dff1

    show rin 2 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0451"
    rin "\"I don't think that really qualifies.\"" id a02_cou2_02_b7abc535

    "Hina shrugged off Rin's hand and plopped down on the floor."

    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0610"
    hina "\"You aaalways treat me like a kid! But you know what?! We're the same age! The. Same. Age!" id a02_cou2_02_235390de

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0452"
    rin "\"I know.\"" id a02_cou2_02_c309b863

    show hina 1 lg pyjama g with dict_dissolve_25

    voice "HIN_0611"
    hina "\"I bet you only think of me like, 'Oh, Hina from next door's chasing a dragonfly again. What a little rascal,' don't you?!\"" id a02_cou2_02_b7d3a173

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0453"
    rin "\"Sorry, I'm a little lost here.\"" id a02_cou2_02_896dfe9d

    show hina 1 lg pyjama h with dict_dissolve_25

    voice "HIN_0612"
    hina "\"I know I'm all short, and I'm not smart, and I didn't have a fancy upbringing like you~\"" id a02_cou2_02_075a6dc4

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_0454"
    rin "\"...Now she's ranting.\"" id a02_cou2_02_62831de1

    stop music fadeout 1.0

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0613"
    hina "\"I wish I were super pretty like you, Rin.\"" id a02_cou2_02_972586d3

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    play music bgm02

    voice "RIN_0455"
    rin "\"Pretty, eh? Well, thanks for that.\"" id a02_cou2_02_5a3d0139

    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0614"
    hina "\"Don't gimme that~! You're so pretty, but you're a total slob! It's such a waste! Why do you squander it like that?!\"" id a02_cou2_02_a7f39df3

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0456"
    rin "\"Umm... because I don't have a practical use for it, I suppose?\"" id a02_cou2_02_e3a78dac

    voice "HIN_0615"
    hina "\"I don't want excuses! Sit up straight!\"" id a02_cou2_02_f1222804

    show hina 2 lg pyjama d with dict_dissolve_25

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_0457"
    rin "\"Ah, okay. Sorry.\"" id a02_cou2_02_a27627cd

    show hina:
        "hina 2 lg pyjama d flat"
        alpha 1.0 xcenter 252 ycenter 981
        easeout 0.5 alpha 0.0 ycenter 1081
    pause 0.5

    hide hina with None

    $ side_image = "hina 2 side pyjama h"

    voice "HIN_0616"
    hina "\"...Like, why'd you quit doing ballet?\"" id a02_cou2_02_83f18670

    "Hina asked abruptly, looking down."

    show rin:
        "rin 1 lg pyjama glasses b" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512

    voice "RIN_0458"
    rin "\"'Cause I got... no, that wasn't why.\"" id a02_cou2_02_ad55c61d

    show rin 1 lg pyjama glasses b:
        xcenter 512
    with None

    voice "RIN_0459"
    rin "\"You're supposed to be tall to do ballet. But there wasn't a boy in my class at my height who could pair up with me...\"" id a02_cou2_02_8a472ce2

    "Rin's words stopped for a moment there."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0460"
    rin "\"Ahh, I guess that's just another excuse.\"" id a02_cou2_02_f91b93ae

    "Rin scratched her head."

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0461"
    rin "\"There was nobody to watch me.\"" id a02_cou2_02_42a1f97e

    "Rin's tone was self-deprecating as she downed the champagne from the cup she'd taken from Hina."

    show rin 2 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0462"
    rin "\"This might surprise you, but I was the one who said I wanted to do ballet. And it was because I saw a friend get praised by her parents at a recital and got jealous.\"" id a02_cou2_02_5b1ed4d6

    voice "RIN_0463"
    rin "\"I practiced as hard as I could. Thought my parents would praise me if I could dance well.\"" id a02_cou2_02_c4c24f6b

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0464"
    rin "\"But when I actually had recitals, my parents barely showed. It just started feeling more and more pointless.\"" id a02_cou2_02_90ea7da1

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0465"
    rin "\"And I was pretty good at it, you know? I won a prize at a contest once, and when I said I was quitting, my coach tried really hard to get me to stay...\"" id a02_cou2_02_cab47b37

    $ side_image = "hina 1 side pyjama m"

    voice "HIN_0617"
    hina "\"Mmh... mmh...\"" id a02_cou2_02_ac97522f

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    "Hina's head had drooped at some point and she was snoring quietly."

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0466"
    rin "\"...And that was my monologue.\"" id a02_cou2_02_71fb3f95

    "Rin smiled bitterly and ran a hand through her hair."

    show rin:
        "rin 2 lg pyjama glasses c" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0467"
    rin "\"Geez, guess I'll get a blanket.\"" id a02_cou2_02_3b705471

    show rin 2 lg pyjama glasses c:
        xoffset 0 yoffset 0
    with None

    "Rin was on her way to the bedroom, when..."

    $ side_image = "hina 1 side pyjama m"

    voice "HIN_0618"
    hina "\"I'm watching.\"" id a02_cou2_02_ac56056c

    show rin 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0468"
    rin "\"Huh?\"" id a02_cou2_02_02148a53

    $ side_image = "hina 1 side pyjama h"

    voice "HIN_0619"
    hina "\"I'm really~ proud of you, Rin~\"" id a02_cou2_02_31252d08

    voice "RIN_0469"
    rin "\"Th... Thanks.\"" id a02_cou2_02_0ec6b416

    $ side_image = "hina 1 side pyjama m"

    voice "HIN_0620"
    hina "\"Mm... nnh...\"" id a02_cou2_02_3ae81a88

    "Hina rolled over onto her side without answering."

    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0470"
    rin "\"...Sleep talking?\"" id a02_cou2_02_8363ccb3

    "Again, no answer came from Hina, except for comfortable snoring."

    play sound se521

    pause 0.5

    show fumi:
        "fumi 1 lg pyjama e flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    pause 0.5

    show fumi 1 lg pyjama e with None

    voice "FUM_0423"
    fumi "\"Oh? Natsume fell asleep?\"" id a02_cou2_02_e361db40

    "That's when Fumi came back."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0471"
    rin "\"She's so much trouble...\"" id a02_cou2_02_249ef968

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0424"
    fumi "\"I'll get a blanket.\"" id a02_cou2_02_5ee9731e

    show fumi:
        "fumi 1 lg pyjama a flat"
        alpha 1.0 xcenter 852
        easeout 0.5 alpha 0.0 xcenter 952
    pause 0.5

    hide fumi with None
    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0472"
    rin "\"Yeah, thanks.\"" id a02_cou2_02_acfbd7f5

    "Rin sat down next to Hina and stroked her hair tenderly."

    voice "RIN_0473"
    rin "\"...I'll do my best.\"" id a02_cou2_02_b59c8c39

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
