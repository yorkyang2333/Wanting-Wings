label a07_comn_07:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show miyako 1 lg pyjama_hood_a a with Dissolve(0.25)

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0094"
    sachiko "\"Dahahaha!\"" id a07_comn_07_cccf7ec6

    "The moment Miyako opened the door and Sachiko saw her, she burst out laughing."

    show miyako 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0060"
    miyako "\"Not again...\"" id a07_comn_07_8103ef0f

    "Miyako was clearly getting tired of this reaction."

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0095"
    sachiko "\"Well, it doesn't get any less funny the more I see it! The door opens and there's a big lion!\"" id a07_comn_07_278616f4

    show miyako 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0061"
    miyako "\"You gave me these pajamas.\"" id a07_comn_07_e3bfe995

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0096"
    sachiko "\"I did good, didn't I?\"" id a07_comn_07_ff04a3c4

    show miyako 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0062"
    miyako "\"......\"" id a07_comn_07_45862143

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0097"
    sachiko "\"Ahaha. Well, come on in. It's cold out there, isn't it?\"" id a07_comn_07_5855e20a

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
    sachiko "\"Here y'go.\"" id a07_comn_07_d60de57f

    show sachiko:
        xoffset 0 yoffset 0
    with None

    "Sachiko held out the printout she'd been entrusted with that evening."

    if routes_cleared == 1:

        show sachiko:
            ShakeYes

        voice "2SA_0099"
        sachiko "\"Oh, this too. Sorry, I forgot to give it to you.\"" id a07_comn_07_1babdac5

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
    miyako "\"Thank you.\"" id a07_comn_07_d03da0f6

    "Miyako took the papers and bowed her head in thanks."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0100"
    sachiko "\"I filled in the guardian section. It's all bullshit, though.\"" id a07_comn_07_29968a30

    show miyako z4 1 lg pyjama_hood_a c with dict_dissolve_25

    voice "2MI_0064"
    miyako "\"Heheh.\"" id a07_comn_07_d33b959d

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0101"
    if persistent.dpatch:
        sachiko "\"So how was your first day at school?\"" id a07_comn_07_690dbb0c
    else:
        sachiko "\"So how was your first day at class?\"" id a07_comn_07_daa0c2d1

    if routes_cleared == 0:
        jump a07_comn_07_c
    else:
        jump a07_comn_07_d

label a07_comn_07_c:

    show miyako z4 2 lg pyjama_hood d with dict_dissolve_25

    voice "2MI_0065"
    miyako "\"We were late.\"" id a07_comn_07_c_61cd6611

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0102"
    sachiko "\"Pretty rock 'n' roll right from Day 1. I'm guessing you were an unexpected element their Rin-shifted schedules couldn't accommodate?\"" id a07_comn_07_c_bd7b994c

    show miyako z4 2 lg pyjama_hood a with dict_dissolve_25

    voice "2MI_0066"
    miyako "\"Were you watching?\"" id a07_comn_07_c_54e79c42

    voice "2SA_0103"
    sachiko "\"I didn't need to. They baby Rin and you sleep a ton.\"" id a07_comn_07_c_adb65060

    show miyako z4 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0067"
    miyako "\"...I'll be more careful tomorrow.\"" id a07_comn_07_c_f5b2e569

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0104"
    if persistent.dpatch:
        sachiko "\"But the school part went okay?\"" id a07_comn_07_c_b41eea05
    else:
        sachiko "\"But the academic part went okay?\"" id a07_comn_07_c_b9e1bef5

    show miyako z4 2 lg pyjama_hood c with dict_dissolve_25

    voice "2MI_0068"
    miyako "\"Yes. But it makes me a little nervous to have so many people looking at me.\"" id a07_comn_07_c_997bffa5

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0105"
    sachiko "\"Well, people don't usually transfer in this time of year. And you're so pretty! It's no wonder you're drawing attention.\"" id a07_comn_07_c_b05af826

    "Heheh."

    voice "2MI_0069"
    miyako "\"I'm used to being the one who does the looking.\"" id a07_comn_07_c_811d7a21

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0106"
    sachiko "\"It's only fair they get a turn, right? That's what it means to have a physical form.\"" id a07_comn_07_c_a514ad0d

    show sachiko:
        ShakeYes

    "Sachiko said, grabbing her mane."

    show sachiko z4 1 lg outfit g:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2SA_0107"
    sachiko "\"You'll get used to it.\"" id a07_comn_07_c_54ae6495

    show miyako z4 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0070"
    miyako "\"......\"" id a07_comn_07_c_057f6ecf

    jump a07_comn_07_e

label a07_comn_07_d:

    show miyako z4 2 lg pyjama_hood c with dict_dissolve_25

    voice "2MI_0071"
    miyako "\"The principal excused our tardiness.\"" id a07_comn_07_d_571179c5

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0108"
    sachiko "\"That was nice of her.\"" id a07_comn_07_d_571e0cbf

    show miyako z4 2 lg pyjama_hood a with dict_dissolve_25

    voice "2MI_0072"
    miyako "\"Does she always wait at the gate in the morning?\"" id a07_comn_07_d_bbfecd44

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0109"
    sachiko "\"Nah. She was probably there to get a look at her new student.\"" id a07_comn_07_d_11c1b6d0

    show miyako z4 1 lg pyjama_hood_b g with dict_dissolve_25

    voice "2MI_0073"
    miyako "\"A look... I suppose so. She did stare a little.\"" id a07_comn_07_d_2e62621e

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0110"
    sachiko "\"Did she say something?\"" id a07_comn_07_d_4d5273cf

    show miyako z4 1 lg pyjama_hood_b e with dict_dissolve_25

    voice "2MI_0074"
    miyako "\"Not really. There was a strange look on her face, though.\"" id a07_comn_07_d_a24ad555

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0111"
    sachiko "\"I see. Well, she is an old lady.\"" id a07_comn_07_d_6c362a0b

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
    miyako "\"It's all thanks to you.\"" id a07_comn_07_e_8ff14971

    voice "2SA_0112"
    sachiko "\"Well, I invited you, so it's only right I help you out now that you're here.\"" id a07_comn_07_e_d8388017

    show miyako z4 1 lg pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0076"
    miyako "\"Umm, can I ask you something?\"" id a07_comn_07_e_f2e909f7

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0113"
    sachiko "\"Hm? You want to know my measurements?\"" id a07_comn_07_e_7a655169

    show miyako z4 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0077"
    miyako "\"...No. How long have you been here?\"" id a07_comn_07_e_24e346ff

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0114"
    sachiko "\"Mm, about five years. You were there when I told Fumi, weren't you?\"" id a07_comn_07_e_6154f2fc

    show miyako z4 2 lg pyjama_hood a with dict_dissolve_25

    voice "2MI_0078"
    miyako "\"Oh, I should have specified. Not here at the dorm, but here on the surface.\"" id a07_comn_07_e_bd5f517e

    show miyako:
        ShakeYes

    "She spread her arms for the first \"here,\" then pointed down for the second. What lively gestures."

    show miyako:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0115"
    sachiko "\"Ah, how long have I been human?\"" id a07_comn_07_e_df84162f

    "Miyako nodded."

    show miyako z4 2 lg pyjama_hood b with dict_dissolve_25

    voice "2MI_0079"
    miyako "\"I was wondering how long it takes to be like you are now.\"" id a07_comn_07_e_c93db6c6

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0116"
    sachiko "\"What do you mean?\"" id a07_comn_07_e_4944b921

    show miyako z4 1 lg pyjama_hood_a a with dict_dissolve_25

    voice "2MI_0080"
    miyako "\"Well, you're very human-like.\"" id a07_comn_07_e_dddff9b6

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0117"
    sachiko "\"I'm just getting by on experience. Luckily, I had plenty of time to practice. And you'll—\"" id a07_comn_07_e_9ed83ca4

    show miyako z4 1 lg pyjama_hood_b j with dict_dissolve_25

    voice "2MI_0081"
    miyako "\"A hundred years? Two hundred?\"" id a07_comn_07_e_c235d723

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0118"
    sachiko "\"What am I, a witch? Human bodies age, remember?\"" id a07_comn_07_e_d3c39d62

    show miyako z4 1 lg pyjama_hood_b e with dict_dissolve_25

    voice "2MI_0082"
    miyako "\"Then... fifty years?\"" id a07_comn_07_e_6cdb13fd

    show sachiko:
        "sachiko z4 2 lg outfit d" with Dissolve(0.25)
        ShakeYes_5_750

    voice "2SA_0119"
    sachiko "\"...Five years.\"" id a07_comn_07_e_68547670

    show sachiko z4 2 lg outfit d:
        xoffset 0 yoffset 0
    with None
    show miyako z4 1 lg pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0083"
    miyako "\"......\"" id a07_comn_07_e_3d06457e

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0120"
    sachiko "\"Do I look that old?\"" id a07_comn_07_e_a5c5d1c2

    show miyako:
        "miyako z4 1 lg pyjama_hood_a f" with Dissolve(0.25)
        ShakeJump

    voice "2MI_0084"
    miyako "\"Oh!\"" id a07_comn_07_e_e39e3561

    show miyako z4 1 lg pyjama_hood_a f:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0121"
    sachiko "\"What?\"" id a07_comn_07_e_6aa4a040

    show miyako z4 1 lg pyjama_hood_a d with dict_dissolve_25

    voice "2MI_0085"
    miyako "\"You must have found it here!\"" id a07_comn_07_e_f745aa87

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0122"
    sachiko "\"So where's 'here' now?\"" id a07_comn_07_e_2f651016

    show miyako z4 2 lg pyjama_hood c with dict_dissolve_25

    voice "2MI_0086"
    if persistent.dpatch:
        miyako "\"I'm sorry, I did it again... Umm, the school.\"" id a07_comn_07_e_7b0d9164
    else:
        miyako "\"I'm sorry, I did it again... Umm, the campus.\"" id a07_comn_07_e_b009ee02

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0123"
    sachiko "\"And what did I find?\"" id a07_comn_07_e_ab7002ae

    show miyako z4 1 lg pyjama_hood_a b with dict_dissolve_25

    voice "2MI_0087"
    miyako "\"Something special enough to trade for your wings!\"" id a07_comn_07_e_dd81590b

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0124"
    sachiko "\"Why do you say that?\"" id a07_comn_07_e_83bfefbe

    show miyako z4 1 lg pyjama_hood_b b with dict_dissolve_25

    voice "2MI_0088"
    miyako "\"You started taking care of this dorm and came down to earth at the same time, five years ago. So the reason you did was here!\"" id a07_comn_07_e_640b8bde

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0125"
    sachiko "\"What if it was just a coincidence? And what are you so excited about?\"" id a07_comn_07_e_832ff93e

    show miyako z4 1 lg pyjama_hood_a c with dict_dissolve_25

    voice "2MI_0089"
    miyako "\"I just thought we were the same and that made me happy!\"" id a07_comn_07_e_a82585a1

    voice "2SA_0126"
    sachiko "\"I can't say I get it, really...\"" id a07_comn_07_e_907fc1b8

    show miyako z4 1 lg pyjama_hood_a g with dict_dissolve_25

    voice "2MI_0090"
    miyako "\"Was it love that you watched, too?\"" id a07_comn_07_e_d3405be8

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0127"
    sachiko "\".........\"" id a07_comn_07_e_07ec276b

    show miyako z4 1 lg pyjama_hood_a e with dict_dissolve_25

    voice "2MI_0091"
    miyako "\"......\"" id a07_comn_07_e_33d4cc4b

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0128"
    sachiko "\"Haha, coulda been. I don't remember.\"" id a07_comn_07_e_307cebb0

    show miyako z4 2 lg pyjama_hood f with dict_dissolve_25

    voice "2MI_0092"
    miyako "\"What~?\"" id a07_comn_07_e_2778da0a

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0129"
    sachiko "\"Alright, it's getting late. You're trying to get up on time tomorrow, right?\"" id a07_comn_07_e_0a5f8e6d

    show miyako z4 2 lg pyjama_hood e with dict_dissolve_25

    voice "2MI_0093"
    miyako "\"...Oh, yes.\"" id a07_comn_07_e_14512ef9

    scene white with bg_effect_11

    play sound se521

    pause 1.0

    scene bg05ca with bg_effect_11
    pause 0.5

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0130"
    sachiko "\"Good night.\"" id a07_comn_07_e_d4b20143

    "Sachiko sent Miyako back to her room."

    $ side_image = "miyako 2 side pyjama_hood i"

    voice "2MI_0094"
    miyako "\"Hwaahh...\"" id a07_comn_07_e_5c25b2a8

    "And as soon as they parted, Miyako yawned hugely."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0131"
    sachiko "\"Yep, out of juice.\"" id a07_comn_07_e_d72e4298

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0132"
    sachiko "\"......\"" id a07_comn_07_e_bfe90c2f

    hide sachiko with Dissolve(0.5)

    play sound se_doorcl

    pause 0.25

    scene white with Dissolve(0.25)
    pause 1.25

    scene bg08ca with Dissolve(0.375)
    pause 1.625

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0133"
    sachiko "\"I did see something special. Something I'll never forget, for the rest of my life.\"" id a07_comn_07_e_38395317

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
