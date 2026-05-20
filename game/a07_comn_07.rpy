label a07_comn_07:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show miyako 1 lg pyjama_hood_a a with Dissolve(0.25)

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0094"
    sachiko "\"Dahahaha!\""

    "The moment Miyako opened the door and Sachiko saw her, she burst out laughing."

    show miyako 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0060"
    miyako "\"Not again...\""

    "Miyako was clearly getting tired of this reaction."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0095"
    sachiko "\"Well, it doesn't get any less funny the more I see it! The door opens and there's a big lion!\""

    show miyako 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0061"
    miyako "\"You gave me these pajamas.\""

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0096"
    sachiko "\"I did good, didn't I?\""

    show miyako 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0062"
    miyako "\"......\""

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0097"
    sachiko "\"Ahaha. Well, come on in. It's cold out there, isn't it?\""

    "Sachiko beckoned Miyako in, wiping her eyes."

    play sound se521

    scene white with bg_effect_12
    pause 1.0

    scene bg09ca with bg_effect_12
    pause 0.5

    show sachiko 1 lg outfit a with Dissolve(0.25)
    show sachiko:
        ShakeYes

    voice "2SA_0098"
    sachiko "\"Here y'go.\""

    show sachiko:
        xoffset 0 yoffset 0
    with None

    "Sachiko held out the printout she'd been entrusted with that evening."

    if routes_cleared == 1:

        show sachiko:
            ShakeYes

        voice "2SA_0099"
        sachiko "\"Oh, this too. Sorry, I forgot to give it to you.\""

        show sachiko:
            xoffset 0 yoffset 0
        with None

        "The transfer paperwork mentioned this morning."

    hide sachiko with Dissolve(0.5)

    show sachiko z4 1 lg outfit a:
        xcenter 298
    show miyako z4 1 lg pyjama_hood_a b:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0063"
    miyako "\"Thank you.\""

    "Miyako took the papers and bowed her head in thanks."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0100"
    sachiko "\"I filled in the guardian section. It's all bullshit, though.\""

    show miyako z4 1 lg pyjama_hood_a c with dict_dissolve_25

    voice "2MI_0064"
    miyako "\"Heheh.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0101"
    if persistent.dpatch:
        sachiko "\"So how was your first day at school?\"" id a07_comn_07_690dbb0c
    else:
        sachiko "\"So how was your first day at class?\""

    if routes_cleared == 0:
        jump a07_comn_07_c
    else:
        jump a07_comn_07_d

label a07_comn_07_c:

    show miyako z4 2 lg pyjama_hood d with dict_dissolve_25

    voice "2MI_0065"
    miyako "\"We were late.\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0102"
    sachiko "\"Pretty rock 'n' roll right from Day 1. I'm guessing you were an unexpected element their Rin-shifted schedules couldn't accommodate?\""

    show miyako z4 2 lg pyjama_hood a with dict_dissolve_25

    voice "2MI_0066"
    miyako "\"Were you watching?\""

    voice "2SA_0103"
    sachiko "\"I didn't need to. They baby Rin and you sleep a ton.\""

    show miyako z4 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0067"
    miyako "\"...I'll be more careful tomorrow.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0104"
    if persistent.dpatch:
        sachiko "\"But the school part went okay?\"" id a07_comn_07_c_b41eea05
    else:
        sachiko "\"But the academic part went okay?\""

    show miyako z4 2 lg pyjama_hood c with dict_dissolve_25

    voice "2MI_0068"
    miyako "\"Yes. But it makes me a little nervous to have so many people looking at me.\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0105"
    sachiko "\"Well, people don't usually transfer in this time of year. And you're so pretty! It's no wonder you're drawing attention.\""

    "Heheh."

    voice "2MI_0069"
    miyako "\"I'm used to being the one who does the looking.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0106"
    sachiko "\"It's only fair they get a turn, right? That's what it means to have a physical form.\""

    show sachiko:
        ShakeYes

    "Sachiko said, grabbing her mane."

    show sachiko z4 1 lg outfit g:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2SA_0107"
    sachiko "\"You'll get used to it.\""

    show miyako z4 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0070"
    miyako "\"......\""

    jump a07_comn_07_e

label a07_comn_07_d:

    show miyako z4 2 lg pyjama_hood c with dict_dissolve_25

    voice "2MI_0071"
    miyako "\"The principal excused our tardiness.\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0108"
    sachiko "\"That was nice of her.\""

    show miyako z4 2 lg pyjama_hood a with dict_dissolve_25

    voice "2MI_0072"
    miyako "\"Does she always wait at the gate in the morning?\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0109"
    sachiko "\"Nah. She was probably there to get a look at her new student.\""

    show miyako z4 1 lg pyjama_hood_b g with dict_dissolve_25

    voice "2MI_0073"
    miyako "\"A look... I suppose so. She did stare a little.\""

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0110"
    sachiko "\"Did she say something?\""

    show miyako z4 1 lg pyjama_hood_b e with dict_dissolve_25

    voice "2MI_0074"
    miyako "\"Not really. There was a strange look on her face, though.\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0111"
    sachiko "\"I see. Well, she is an old lady.\""

    stop music fadeout 1.0

    jump a07_comn_07_e

label a07_comn_07_e:

    scene white with bg_effect_05
    pause 1.5

    scene bg09ca with bg_effect_05
    pause 0.5

    play music bgm02 fadein 1.0

    if persistent.dpatch:
        "Miyako reported in great detail about all the discoveries of her first day at school and how fulfilling it was, and Sachiko listened happily." id a07_comn_07_e_81014aa8
    else:
        "Miyako reported in great detail about all the discoveries of her first day on campus and how fulfilling it was, and Sachiko listened happily."

    show sachiko z4 1 lg outfit a:
        xcenter 298
    show miyako z4 1 lg pyjama_hood_a b:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_0075"
    miyako "\"It's all thanks to you.\""

    voice "2SA_0112"
    sachiko "\"Well, I invited you, so it's only right I help you out now that you're here.\""

    show miyako z4 1 lg pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0076"
    miyako "\"Umm, can I ask you something?\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0113"
    sachiko "\"Hm? You want to know my measurements?\""

    show miyako z4 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0077"
    miyako "\"...No. How long have you been here?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0114"
    sachiko "\"Mm, about five years. You were there when I told Fumi, weren't you?\""

    show miyako z4 2 lg pyjama_hood a with dict_dissolve_25

    voice "2MI_0078"
    miyako "\"Oh, I should have specified. Not here at the dorm, but here on the surface.\""

    show miyako:
        ShakeYes

    "She spread her arms for the first \"here,\" then pointed down for the second. What lively gestures."

    show miyako:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0115"
    sachiko "\"Ah, how long have I been human?\""

    "Miyako nodded."

    show miyako z4 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0079"
    miyako "\"I was wondering how long it takes to be like you are now.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0116"
    sachiko "\"What do you mean?\""

    show miyako z4 1 lg pyjama_hood_a a with dict_dissolve_25

    voice "2MI_0080"
    miyako "\"Well, you're very human-like.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0117"
    sachiko "\"I'm just getting by on experience. Luckily, I had plenty of time to practice. And you'll—\""

    show miyako z4 1 lg pyjama_hood_b j with dict_dissolve_25

    voice "2MI_0081"
    miyako "\"A hundred years? Two hundred?\""

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0118"
    sachiko "\"What am I, a witch? Human bodies age, remember?\""

    show miyako z4 1 lg pyjama_hood_b e with dict_dissolve_25

    voice "2MI_0082"
    miyako "\"Then... fifty years?\""

    show sachiko:
        "sachiko z4 2 lg outfit d" with Dissolve(0.25)
        ShakeYes_5_750

    voice "2SA_0119"
    sachiko "\"...Five years.\""

    show sachiko z4 2 lg outfit d:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0083"
    miyako "\"......\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0120"
    sachiko "\"Do I look that old?\""

    show miyako:
        "miyako z4 1 lg pyjama_hood_a f" with Dissolve(0.25)
        ShakeJump

    voice "2MI_0084"
    miyako "\"Oh!\""

    show miyako z4 1 lg pyjama_hood_a f:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0121"
    sachiko "\"What?\""

    show miyako z4 1 lg pyjama_hood_a d with dict_dissolve_25

    voice "2MI_0085"
    miyako "\"You must have found it here!\""

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0122"
    sachiko "\"So where's 'here' now?\""

    show miyako z4 2 lg pyjama_hood c with dict_dissolve_25

    voice "2MI_0086"
    if persistent.dpatch:
        miyako "\"I'm sorry, I did it again... Umm, the school.\"" id a07_comn_07_e_7b0d9164
    else:
        miyako "\"I'm sorry, I did it again... Umm, the campus.\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0123"
    sachiko "\"And what did I find?\""

    show miyako z4 1 lg pyjama_hood_a b with dict_dissolve_25

    voice "2MI_0087"
    miyako "\"Something special enough to trade for your wings!\""

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0124"
    sachiko "\"Why do you say that?\""

    show miyako z4 1 lg pyjama_hood_b b with dict_dissolve_25

    voice "2MI_0088"
    miyako "\"You started taking care of this dorm and came down to earth at the same time, five years ago. So the reason you did was here!\""

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0125"
    sachiko "\"What if it was just a coincidence? And what are you so excited about?\""

    show miyako z4 1 lg pyjama_hood_a c with dict_dissolve_25

    voice "2MI_0089"
    miyako "\"I just thought we were the same and that made me happy!\""

    voice "2SA_0126"
    sachiko "\"I can't say I get it, really...\""

    show miyako z4 1 lg pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0090"
    miyako "\"Was it love that you watched, too?\""

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0127"
    sachiko "\".........\""

    show miyako z4 1 lg pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0091"
    miyako "\"......\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0128"
    sachiko "\"Haha, coulda been. I don't remember.\""

    show miyako z4 2 lg pyjama_hood f with dict_dissolve_25

    voice "2MI_0092"
    miyako "\"What~?\""

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0129"
    sachiko "\"Alright, it's getting late. You're trying to get up on time tomorrow, right?\""

    show miyako z4 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0093"
    miyako "\"...Oh, yes.\""

    scene white with bg_effect_11

    play sound se521

    pause 1.0

    scene bg05ca with bg_effect_11
    pause 0.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0130"
    sachiko "\"Good night.\""

    "Sachiko sent Miyako back to her room."

    $ side_image = "miyako 2 side pyjama_hood i"

    voice "2MI_0094"
    miyako "\"Hwaahh...\""

    "And as soon as they parted, Miyako yawned hugely."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0131"
    sachiko "\"Yep, out of juice.\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0132"
    sachiko "\"......\""

    hide sachiko with Dissolve(0.5)

    play sound se_doorcl

    pause 0.25

    scene white with Dissolve(0.25)
    pause 1.25

    scene bg08ca with Dissolve(0.375)
    pause 1.625

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0133"
    sachiko "\"I did see something special. Something I'll never forget, for the rest of my life.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
