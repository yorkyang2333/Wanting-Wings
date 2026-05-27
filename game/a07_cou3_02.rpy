label a07_cou3_02:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "hina 2 side casual_scarf a"

    voice "2HI_0350"
    hina "\"Well, it's pretty nice out. Want to walk a bit more?\"" id a07_cou3_02_b32664ff

    "Hina asked Miyako at a red light."

    show miyako 1 lg casual_a b at pos_l
    show hina 2 lg casual_scarf a at pos_r
    with dict_dissolve_25

    voice "2MI_0258"
    miyako "\"Sure, that sounds nice.\"" id a07_cou3_02_5061c5c8

    $ side_image = "rin 2 side casual c"

    voice "2RI_0327"
    rin "\"What~? It's cold, I don't wanna.\"" id a07_cou3_02_88c240ef

    show hina 1 lg casual_scarf j with dict_dissolve_25

    voice "2HI_0351"
    hina "\"I didn't invite you. Shoo, go home.\"" id a07_cou3_02_5bf9d084

    $ side_image = "fumi 2 side casual h"

    voice "2FU_0275"
    fumi "\"I—\"" id a07_cou3_02_e4bf9cd7

    show hina 1 lg casual_scarf a with dict_dissolve_25

    voice "2HI_0352"
    hina "\"Take Rin home, Asou?\"" id a07_cou3_02_994eac95

    $ side_image = "fumi 2 side casual g"

    voice "2FU_0276"
    fumi "\"Ah...\"" id a07_cou3_02_1c142620

    $ side_image = "rin 1 side casual i"

    voice "2RI_0328"
    rin "\"Hey, isn't that a little mean?\"" id a07_cou3_02_697966ce

    $ side_image = "fumi 1 side casual c"

    voice "2FU_0277"
    fumi "\"Okay!\"" id a07_cou3_02_7a1128c4

    $ side_image = "rin 1 side casual g"

    voice "2RI_0329"
    rin "\"Huh? Okay? Wasn't she a little mean to me?\"" id a07_cou3_02_9fcea893

    $ side_image = "fumi 1 side casual h"

    voice "2FU_0278"
    fumi "\"...Rin?\"" id a07_cou3_02_57b31e9d

    "Fumi sighed and pulled Rin's sleeve so she'd bend down, then whispered in her ear."

    $ side_image = "rin 2 side casual f"

    voice "2RI_0330"
    rin "\"Huh? ...Oh... okay... we'll go home.\"" id a07_cou3_02_c78b80fe

    "She mumbled."

    show hina 2 lg casual_scarf f with dict_dissolve_25

    voice "2HI_0353"
    hina "\"Takaoka and I will hang out for about two hours, I think...\"" id a07_cou3_02_9bd67ade

    "Hina shot a look at Miyako, who nodded her agreement."

    $ side_image = "fumi 1 side casual b"

    voice "2FU_0279"
    fumi "\"Got you. —Let's go, Rin?\"" id a07_cou3_02_a845fbfd

    $ side_image = "rin 2 side casual g"

    voice "2RI_0331"
    rin "\"...Yeah.\"" id a07_cou3_02_b3634367

    show miyako 1 lg casual_a c with dict_dissolve_25

    voice "2MI_0259"
    miyako "\"See you later.\"" id a07_cou3_02_856562a6

    "Fumi and Miyako waved at each other."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg11aa with bg_effect_05
    pause 0.5

    "......"

    show miyako 1 sm casual_a b at pos_ls
    show hina 1 sm casual_scarf n at pos_rs
    with Dissolve(0.25)

    show hina:
        ShakeTameiki

    voice "2HI_0354"
    hina "\"Sorry for deciding without asking you.\"" id a07_cou3_02_6710fc31

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina turned to Miyako after watching Fumi and Rin leave."

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0355"
    hina "\"We'll get cold talking out here. I hope there's a coffee shop open somewhere, but it is a holiday...\"" id a07_cou3_02_c1d204db

    "This was a town with no Starbucks."

    voice "2MI_0260"
    miyako "\"Oh, the cold doesn't bother me all that much.\"" id a07_cou3_02_8f528c08

    show hina 2 sm casual_scarf a with dict_dissolve_25

    voice "2HI_0356"
    hina "\"Really? Same here. Wanna walk and talk, then? I'll show you around town.\"" id a07_cou3_02_c200ef05

    "The two hardy girls walked off."

    show hina 2 sm casual_scarf b with dict_dissolve_25

    voice "2HI_0357"
    hina "\"I imagine you've noticed, but those two—\"" id a07_cou3_02_7ff99a15

    show miyako 1 sm casual_b h with dict_dissolve_25

    voice "2MI_0261"
    miyako "\"They're very close, aren't they?\"" id a07_cou3_02_c254f219

    "Miyako smiled. The two of them were on the same page."

    show hina 2 sm casual_scarf a with dict_dissolve_25

    voice "2HI_0358"
    hina "\"Yeah, so... I wanted to give them some time alone.\"" id a07_cou3_02_fa343448

    show miyako:
        "miyako 1 sm casual_a b" with Dissolve(0.25)
        ShakeYes

    voice "2MI_0262"
    miyako "\"Yes, I agree.\"" id a07_cou3_02_e83db10e

    show miyako 1 sm casual_a b:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm casual_scarf p with dict_dissolve_25

    voice "2HI_0359"
    hina "\"Eheh. So you don't mind hanging out with me?\"" id a07_cou3_02_eca01e4a

    show miyako 1 sm casual_a h with dict_dissolve_25

    voice "2MI_0263"
    miyako "\"I'm happy to.\"" id a07_cou3_02_4f305eb5

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0360"
    hina "\"Well... I said I'd show you around, but most of the stores are closed.\"" id a07_cou3_02_e41efe14

    "There wasn't much point keeping a store open on holidays in a residential town like this."

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0264"
    miyako "\"I'm glad I got an opportunity to chat with you like this, Natsume.\"" id a07_cou3_02_51387df2

    show hina 2 sm casual_scarf a with dict_dissolve_25

    voice "2HI_0361"
    hina "\"So am I. ...You're a good person, Takaoka.\"" id a07_cou3_02_41e46182

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0265"
    miyako "\"Do you think so?\"" id a07_cou3_02_d0d04bb0

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0362"
    hina "\"I feel like you're already looking out for us even though you only just came.\"" id a07_cou3_02_f7c9d2f1

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0266"
    miyako "\"It's alright. I like seeing how close they are.\"" id a07_cou3_02_395a4171

    show hina 2 sm casual_scarf b with dict_dissolve_25

    voice "2HI_0363"
    hina "\"Yeah, I do, too. It's just... you know, they're at that age...\"" id a07_cou3_02_3fdb9a71

    "Hina suggested."

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0267"
    miyako "\"Ah, I suppose so.\"" id a07_cou3_02_437fdceb

    "Miyako understood."

    show hina 1 sm casual_scarf n with dict_dissolve_25

    voice "2HI_0364"
    hina "\"I'm supposed to keep an eye on things as the RA, but...\"" id a07_cou3_02_8f25bdd3

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0268"
    miyako "\"You don't want to restrict them too much.\"" id a07_cou3_02_bf4f11d1

    show hina:
        "hina 1 sm casual_scarf h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0365"
    hina "\"Right. Sorry, I'll probably end up asking for your help more in the future.\"" id a07_cou3_02_32bbe50b

    show hina 1 sm casual_scarf h:
        xoffset 0 yoffset 0
    with None
    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0269"
    miyako "\"Please don't hesitate to.\"" id a07_cou3_02_3da5423a

    show hina 2 sm casual_scarf e with dict_dissolve_25

    voice "2HI_0366"
    hina "\"It's just, I feel kind of awkward about it.\"" id a07_cou3_02_8e5ec94b

    show miyako 1 sm casual_a e with dict_dissolve_25

    voice "2MI_0270"
    miyako "\"Hm?\"" id a07_cou3_02_2accbdc4

    show hina 2 sm casual_scarf d with dict_dissolve_25

    voice "2HI_0367"
    hina "\"Oh, once, I caught them in the middle of the act... You just... wouldn't expect them to do that in the chapel, right?\"" id a07_cou3_02_5340e33c

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0271"
    miyako "\"Ah...\"" id a07_cou3_02_cc2e873f

    "She couldn't very well say, \"Yes, I saw that, too.\""

    show hina 1 sm casual_scarf n with dict_dissolve_25

    voice "2HI_0368"
    hina "\"After that, they started acting closer in public, like they weren't restraining themselves anymore.\"" id a07_cou3_02_ed31744c

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0369"
    hina "\"Even in front of you. Asou's still holding back, but Rin's all over her.\"" id a07_cou3_02_7711b203

    show miyako 1 sm casual_a e with dict_dissolve_25

    voice "2MI_0272"
    miyako "\"It doesn't bother me.\"" id a07_cou3_02_0701e92c

    show hina 1 sm casual_scarf n with dict_dissolve_25

    voice "2HI_0370"
    hina "\"It doesn't bother me either, when they're just flirting.\"" id a07_cou3_02_629c9bb0

    show hina 1 sm casual_scarf h with dict_dissolve_25

    voice "2HI_0371"
    hina "\"I just feel like Rin's a little dependent on Asou. Which I guess she's kinda always been, but it's hard to watch sometimes.\"" id a07_cou3_02_349f34c9

    voice "2HI_0372"
    hina "\"And Asou's Asou, so she babies Rin. Maybe I shouldn't, but I worry...\"" id a07_cou3_02_986a00a9

    show hina 1 sm casual_scarf m with dict_dissolve_25

    voice "2HI_0373"
    hina "\"...But, like, I get it. Rin's not used to having someone to rely on, since her parents haven't really been around since she was little.\"" id a07_cou3_02_98da1efd

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0273"
    miyako "\"......\"" id a07_cou3_02_801ce491

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0374"
    hina "\"What?\"" id a07_cou3_02_45fcdafa

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0274"
    miyako "\"You really care a lot about them, huh?\"" id a07_cou3_02_eeb34389

    show hina 2 sm casual_scarf c with dict_dissolve_25

    voice "2HI_0375"
    hina "\"Ah, yeah... They're my best friends. I want to stay close to them as long as I can.\"" id a07_cou3_02_19203379

    voice "2MI_0275"
    miyako "\"......\"" id a07_cou3_02_ecfc8d1a

    "She can use a phrase like \"best friends\" with complete honesty. She really is a strong girl."

    show hina 1 sm casual_scarf k with dict_dissolve_25

    voice "2HI_0376"
    hina "\"Oh, sorry, you mind?\"" id a07_cou3_02_2f4df472

    "Hina suddenly stopped."

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0276"
    miyako "\"Hm?\"" id a07_cou3_02_c6646453

    "And she took a small box out of her pocket. It was her special toy camera."

    show hina 1 sm casual_scarf a with dict_dissolve_25

    voice "2HI_0377"
    hina "\"I want to take a picture here. It's bustling with color, after all.\"" id a07_cou3_02_7b5d926e

    "It was a small toy store, the only business on the street still open for the holiday."

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0277"
    miyako "\"It is. All the other stores have their shutters down, just this one is bustling.\"" id a07_cou3_02_ce678665

    "Miyako's eyes were sparkling when she turned back to Hina."

    hide hina
    hide miyako
    with Dissolve(0.5)

    pause 0.5

    play sound2 se061

    "Hina darted around, snapping pictures."

    $ side_image = "hina 1 side casual_scarf a"

    voice "2HI_0378"
    hina "\"Is that a new one of the stuffed animals Asou collects, you think?\"" id a07_cou3_02_aaeac975

    "There was a cart outside the shop and some familiar-looking stuffed animals lined up on it."

    $ side_image = "miyako 1 side casual_a b"

    voice "2MI_0278"
    miyako "\"They do look alike, now that you mention it.\"" id a07_cou3_02_c5be9fa9

    "Miyako picked one of them up."

    $ side_image = "hina 1 side casual_scarf c"

    voice "2HI_0379"
    hina "\"Takaoka, over here!\"" id a07_cou3_02_53fb3407

    play sound2 se061

    show miyako 1 lg casual_a f with Dissolve(0.25)
    show miyako:
        ShakeSide

    voice "2MI_0279"
    miyako "\"?!\"" id a07_cou3_02_298a41d6

    show miyako:
        xoffset 0 yoffset 0
    with None

    "Miyako's eyes went wide when the camera was pointed at her."

    $ side_image = "hina 1 side casual_scarf d"

    voice "2HI_0380"
    hina "\"Oh, sorry. Do you not like having your picture taken?\"" id a07_cou3_02_68c51252

    show miyako 2 lg casual a with dict_dissolve_25

    voice "2MI_0280"
    miyako "\"N-No... I was just surprised.\"" id a07_cou3_02_c622c1d1

    "She was still thinking like an angel. Even though now, she {i}should{/i} show up in pictures."

    $ side_image = "hina 2 side casual_scarf a"

    voice "2HI_0381"
    hina "\"Then, can I take another? Smile this time♪\"" id a07_cou3_02_2c84d227

    show miyako 1 lg casual_a b with dict_dissolve_25

    voice "2MI_0281"
    miyako "\"Oh, okay.\"" id a07_cou3_02_a6a03684

    show miyako 1 lg casual_b h with Dissolve(0.25)

    play sound2 se061

    "This time she smiled. It was a little awkward, though."

    $ side_image = "hina 1 side casual_scarf c"

    voice "2HI_0382"
    hina "\"Thanks. I'll show 'em to you next time I get them developed.\"" id a07_cou3_02_00ce8a20

    show miyako 1 lg casual_a g with dict_dissolve_25

    voice "2MI_0282"
    miyako "\"Umm, can I see that camera?\"" id a07_cou3_02_a008a95d

    $ side_image = "hina 1 side casual_scarf a"

    voice "2HI_0383"
    hina "\"Yeah, sure. It's just a normal toy camera, though.\"" id a07_cou3_02_7cd6c743

    hide miyako with dict_dissolve_50

    "Miyako took the camera."

    $ side_image = "miyako 1 side casual_a e"

    voice "2MI_0283"
    miyako "\"So this is...\"" id a07_cou3_02_637d58c5

    "She turned it, looking at it from different angles."

    show hina 1 sm casual_scarf k at pos_rs with dict_dissolve_25

    voice "2HI_0384"
    hina "\"It's what? Is this your first time seeing a toy camera?\"" id a07_cou3_02_90ff099c

    show miyako 1 sm casual_b e at pos_ls with dict_dissolve_25

    voice "2MI_0284"
    miyako "\"There's nothing unusual about it, is there?\"" id a07_cou3_02_e38cd6fe

    show hina 2 sm casual_scarf a with dict_dissolve_25

    voice "2HI_0385"
    hina "\"Yeah. Like I said, it's just a normal one.\"" id a07_cou3_02_6dcec7b9

    show miyako 1 sm casual_b i with dict_dissolve_25

    voice "2MI_0285"
    miyako "\"How strange...\"" id a07_cou3_02_80dc498a

    show hina 2 sm casual_scarf c with dict_dissolve_25

    voice "2HI_0386"
    hina "\"You're a little strange, too, Takaoka...\"" id a07_cou3_02_cc685273

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0387"
    hina "\"Hey, Takaoka...\"" id a07_cou3_02_214afa77

    show miyako 1 sm casual_b e with dict_dissolve_25

    voice "2MI_0286"
    miyako "\"Yes?\"" id a07_cou3_02_4cec0653

    "Miyako was still fervently examining the camera."

    show hina 2 sm casual_scarf d with dict_dissolve_25

    voice "2HI_0388"
    hina "\"...You believe in angels, right?\"" id a07_cou3_02_c223dc92

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0288"
    miyako "\"...Yes.\"" id a07_cou3_02_66187a21

    "She stopped fiddling with the camera and looked up."

    show hina 2 sm casual_scarf e with dict_dissolve_25

    voice "2HI_0389"
    hina "\"Umm... well...\"" id a07_cou3_02_6e1a138c

    "Hina hesitated."

    voice "2MI_0287"
    miyako "\"......\"" id a07_cou3_02_7a3d8218

    "Miyako waited serenely for Hina to get the words out."

    show hina 1 sm casual_scarf m with dict_dissolve_25

    voice "2HI_0390"
    hina "\"I... took a picture of an angel with that camera.\"" id a07_cou3_02_e0e8a7fc

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0289"
    miyako "\"Ah...\"" id a07_cou3_02_59fa1d93

    show hina 2 sm casual_scarf f with dict_dissolve_25

    voice "2HI_0391"
    hina "\"It was a long time ago. When I was little. I got the camera as a Christmas present—\"" id a07_cou3_02_d4aca1e7

    "Hina spoke like a dam had burst. She told the story of the angel eating the strawberry off of her cake on that Christmas night."

    "Her story wasn't organized particularly well, but her words were passionate, and Miyako listened patiently until the end."

    "......"

    show hina 2 sm casual_scarf b with dict_dissolve_25

    voice "2HI_0392"
    hina "\"I'm sorry... for going on about something so weird all of a sudden.\"" id a07_cou3_02_8a322173

    show miyako 2 sm casual c with dict_dissolve_25

    "Miyako merely shook her head."

    voice "2HI_0393"
    hina "\"I just thought you might believe me, so...\"" id a07_cou3_02_a8eabab9

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0290"
    miyako "\"Of course I believe you.\"" id a07_cou3_02_0f51e1fe

    "She looked her straight in the eye and said that. Well, of course she did. She knows who that angel was, after all."

    show hina 2 sm casual_scarf c with dict_dissolve_25

    voice "2HI_0394"
    hina "\"I've always kept it a secret... but I wanted to tell someone.\"" id a07_cou3_02_105dacab

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0291"
    miyako "\"I'm glad you told me.\"" id a07_cou3_02_1a895e50

    show hina 2 sm casual_scarf g with dict_dissolve_25

    voice "2HI_0395"
    hina "\"Thanks. I'm glad I did, too.\"" id a07_cou3_02_9f1c5af5

    "Hina's face lit up when Miyako accepted her story as truth."

    show hina 1 sm casual_scarf c with dict_dissolve_25

    voice "2HI_0396"
    hina "\"When we get back... I'll show you the picture!\"" id a07_cou3_02_d0234347

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0292"
    miyako "\"...Alright.\"" id a07_cou3_02_dfe5ed54

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    "Hina walked off, but Miyako was still standing there. She was happy."

    "She knew that Hina sometimes snuck her album out to look at it, and she'd peeked at the picture from behind her back before, too."

    "That was when she was watching the room as an angel, of course."

    "What mattered to her wasn't Hina's story or her proof, but that she'd opened up about something important to her."

    $ side_image = "hina 1 side casual_scarf k"

    voice "2HI_0397"
    hina "\"Takaokaaa?\"" id a07_cou3_02_2893bfca

    $ side_image = "miyako 1 side casual_a b"

    voice "2MI_0293"
    miyako "\"Yes, I'm coming.\"" id a07_cou3_02_bb49820f

    "Miyako hurried to follow Hina."

    $ side_image = "miyako 2 side casual c"

    voice "2MI_0294"
    miyako "\"They do exist... Angels.\"" id a07_cou3_02_d42e6e55

    "She suddenly pointed the camera my way."

    "...Whoops."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_cou3_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
