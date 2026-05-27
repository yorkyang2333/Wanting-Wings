label a01_comn_08:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene ev01g with Dissolve(0.5)

    play music bgm01

    voice "HIN_0163"
    hina "\"♪Nyaga nyaga! Nya, nya nya nya!\"" id a01_comn_08_250ae126

    voice "RIN_0155"
    rin "\"......\"" id a01_comn_08_41e64005

    voice "HIN_0164"
    hina "\"♪Nya nya nya nya! Nya, nya nya nya!\"" id a01_comn_08_e9a5a02e

    scene ev01h with Dissolve(0.5)

    voice "RIN_0156"
    rin "\"...Ahem.\"" id a01_comn_08_3184a007

    scene ev01k with Dissolve(0.5)

    voice "FUM_0117"
    fumi "\"...Ah...\"" id a01_comn_08_898af7f5

    voice "HIN_0165"
    hina "\"♪Nyaga nyaga! Nya, nya nya nya!\"" id a01_comn_08_36201f7e

    voice "RIN_0157"
    rin "\"...Shut up...\"" id a01_comn_08_9d336466

    voice "FUM_0118"
    fumi "\"...Ah, ah...\"" id a01_comn_08_434cb471

    voice "HIN_0166"
    hina "\"♪Nyaa nyaa nyaa nya, nya nya nyaa nyaa!\"" id a01_comn_08_137a6583

    voice "RIN_0158"
    rin "\"Shut up!\"" id a01_comn_08_6beead7f

    voice "HIN_0167"
    hina "\"♪Nyaga nyaga! Nya, nya nya nya!\"" id a01_comn_08_c1d16f8e

    voice "FUM_0119"
    fumi "\"Ah... aaah...\"" id a01_comn_08_759b1058

    voice "RIN_0159"
    rin "\"...Phew.\"" id a01_comn_08_775c3c75

    voice "FUM_0120"
    fumi "\"O... Ogata?\"" id a01_comn_08_1aad7f14

    scene bg01ca with Dissolve(0.25)

    show hina 1 sm pyjama headphones g
    show rin 1 sm pyjama h glasses at pos_l2
    show fumi 1 sm pyjama d at pos_r2
    with Dissolve(0.25)

    voice "RIN_0160"
    rin "\"Hey, Gian.\"" id a01_comn_08_6128f8e0

    play sound se555

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        function LayerShake(15,15,0.1)
    $ persistent.layer_shaken = False

    voice "HIN_0168"
    hina "\"Wah?!\"" id a01_comn_08_f8e2c6cc

    show hina 1 sm pyjama l -headphones:
        xoffset 0 yoffset 0
    with None

    "Rin yanked the headphones from Hina's head, and she spun around in surprise."

    show rin 1 sm pyjama h glasses with dict_dissolve_25

    voice "RIN_0161"
    rin "\"Shut up.\"" id a01_comn_08_72d35e8b

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0169"
    hina "\"Oh, was it too loud?\"" id a01_comn_08_0093198f

    voice "RIN_0162"
    rin "\"Yeah, your singing was.\"" id a01_comn_08_93992ec7

    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0170"
    hina "\"Huh?\"" id a01_comn_08_ce86310c

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0121"
    fumi "\"Did you not know you were singing out loud?\"" id a01_comn_08_1dd8c182

    show hina 1 sm pyjama l with dict_dissolve_25

    voice "HIN_0171"
    hina "\"Huh? No way. Was I really?!\"" id a01_comn_08_6cbd5c4a

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0122"
    fumi "\"Quite enthusiastically.\"" id a01_comn_08_3d0a040f

    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0172"
    hina "\"Hyaaa~ That's kind of embarrassing.\"" id a01_comn_08_a0a55c7f

    show rin 1 sm pyjama a glasses with dict_dissolve_25

    voice "RIN_0163"
    rin "\"You suck at singing.\"" id a01_comn_08_12508e5f

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0173"
    hina "\"Wha?! Not even my parents ever told me that!\"" id a01_comn_08_0ecaa50a

    show hina 1 sm pyjama l:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0123"
    fumi "\"Ah... ahahaha... You have a very cute voice, though.\"" id a01_comn_08_4fa8f9c9

    if route1 == 3:
        jump a01_comn_08_end
    else:
        python:
            _last_say_what = ""
            _last_say_who = None
            renpy.choice_for_skipping()

        stop music fadeout 2.0
        scene black with Dissolve(0.5)
        pause 1.5

        scene select_back with Dissolve(0.5)
        pause 1.5


        menu:
            "日記"((713, 344), "menu/btn_select_0201"):
                $ hina_fumi_score += 1
                jump a01_comn_08_a
            "ヘッドフォン"((245, 551), "menu/btn_select_0202"):
                $ rin_hina_score += 1
                jump a01_comn_08_b

label a01_comn_08_a:

    play music bgm01

    scene white with Dissolve(0.75)
    pause 0.75
    scene ev01a with bg_effect_25
    pause 0.5

    voice "HIN_0174"
    hina "\"I'm kinda impressed by you, Asou.\"" id a01_comn_08_a_7ebea607

    voice "FUM_0124"
    fumi "\"Wh-What brought that on?\"" id a01_comn_08_a_79fa79c6

    voice "HIN_0175"
    hina "\"I mean, you write in your diary every day, right?\"" id a01_comn_08_a_dda82935

    voice "FUM_0125"
    fumi "\"Well... yes, I do.\"" id a01_comn_08_a_16a636eb

    voice "HIN_0176"
    hina "\"Even when it's wet and cold?\"" id a01_comn_08_a_9c1e8aa3

    voice "FUM_0126"
    fumi "\"Even when I have a cold.\"" id a01_comn_08_a_e24bfd4e

    voice "RIN_0164"
    rin "\"Yikes, was that a joke?\"" id a01_comn_08_a_443199c5

    voice "FUM_0127"
    fumi "\"Eheheh.\"" id a01_comn_08_a_83276ad8

    voice "HIN_0177"
    hina "\"That's really impressive, Asou!\"" id a01_comn_08_a_51dfa573

    voice "FUM_0128"
    fumi "\"I don't think it's anything that incredible.\"" id a01_comn_08_a_69df2510

    voice "HIN_0178"
    hina "\"I wouldn't even know what to write every day.\"" id a01_comn_08_a_b034f09a

    voice "FUM_0129"
    fumi "\"You just write whatever. Something that happened that day, or a thought that you had.\"" id a01_comn_08_a_1840daca

    voice "HIN_0179"
    hina "\"Hmm...\"" id a01_comn_08_a_965a0c05

    voice "RIN_0165"
    rin "\"When you had to keep a summer diary for school, you always just did it all on the last day, didn't you?\"" id a01_comn_08_a_4e26ee3a

    voice "HIN_0180"
    hina "\"What? How did you know that?\"" id a01_comn_08_a_0c74f938

    jump a01_comn_08_end

label a01_comn_08_b:

    play music bgm01

    scene white with Dissolve(0.75)
    pause 0.75
    scene ev01h with bg_effect_25
    pause 0.5

    voice "RIN_0166"
    rin "\"What the heck are you always listening to anyway, Hina?\"" id a01_comn_08_b_607bb924

    voice "HIN_0181"
    hina "\"Heheh, western stuff.\"" id a01_comn_08_b_85c06d4b

    voice "RIN_0167"
    rin "\"What's with the smirk? I was looking for, like, an artist name or something.\"" id a01_comn_08_b_e98dbdb8

    voice "HIN_0182"
    hina "\"Umm, I dunno who they are.\"" id a01_comn_08_b_aa9633cd

    voice "RIN_0168"
    rin "\"You're listening to bands you don't know?\"" id a01_comn_08_b_ec4af32e

    voice "HIN_0183"
    hina "\"It's just stuff my dad gave me.\"" id a01_comn_08_b_2388ff50

    voice "RIN_0169"
    rin "\"I didn't know you were good at English?\"" id a01_comn_08_b_21ec96c4

    voice "HIN_0184"
    hina "\"Nuh-uh. Not at all. So I've got no idea what they're singing about.\"" id a01_comn_08_b_0fd9ea80

    voice "RIN_0170"
    rin "\"Do you know the genre, at least?\"" id a01_comn_08_b_60c55488

    voice "HIN_0185"
    hina "\"Heheh, heheh, rock 'n' roll!\"" id a01_comn_08_b_362b99f0

    voice "RIN_0171"
    rin "\"I seriously don't get why you're so smug about it.\"" id a01_comn_08_b_8a567e86

    voice "FUM_0130"
    fumi "\"Ahahahaha.\"" id a01_comn_08_b_645ce97d

    voice "RIN_0172"
    rin "\"Lemme hear.\"" id a01_comn_08_b_c6674bf3

    "Hina handed the headphones to Rin."

    voice "RIN_0173"
    rin "\"A CD player in this day and age? You must have taken real good care of this thing.\"" id a01_comn_08_b_370f12e4

    voice "HIN_0186"
    hina "\"I just bought the headphones last year, though.\"" id a01_comn_08_b_62b3493b

    "Rin looked the CD player over curiously, then put the headphones on."

    voice "FUM_0131"
    fumi "\"Did your dad give you the CD player, too?\"" id a01_comn_08_b_01c89271

    voice "HIN_0187"
    hina "\"Yep. It's pretty old now, though, so it doesn't work great.\"" id a01_comn_08_b_06d2da46

    voice "RIN_0174"
    rin "\"...When's this song from?\"" id a01_comn_08_b_ad45dbf2

    voice "HIN_0188"
    hina "\"It was popular when my dad was younger.\"" id a01_comn_08_b_ae714775

    voice "FUM_0132"
    fumi "\"A golden oldie? Can I hear it too, after Ogata?\"" id a01_comn_08_b_ddee0385

    voice "HIN_0189"
    hina "\"Yeah, it's really cool. I dunno what they're saying, though.\"" id a01_comn_08_b_e1558486

    voice "RIN_0175"
    rin "\"I know the hook of this, though. I think it was in a commercial a little bit ago. Something about a mom forgetting to buy instant ramen for her son when he's up late studying or some such.\"" id a01_comn_08_b_28b00315

    voice "HIN_0190"
    hina "\"Huh?! That's what this song is about? Even though it sounds so cool?\"" id a01_comn_08_b_a19061ca

    voice "RIN_0176"
    rin "\"No, I think they changed the lyrics for the commercial. They're singing about something else in this.\"" id a01_comn_08_b_70ff8311

    voice "HIN_0191"
    hina "\"Oh, good~\"" id a01_comn_08_b_4c259790

    voice "RIN_0177"
    rin "\"But more importantly...\"" id a01_comn_08_b_d38a3c7f

    voice "HIN_0192"
    hina "\"What?\"" id a01_comn_08_b_74dd2653

    voice "RIN_0178"
    rin "\"How did hard rock like this turn into whatever sick animal impression you were doing earlier?\"" id a01_comn_08_b_07b48f09

    voice "HIN_0193"
    hina "\"Nyanya?\"" id a01_comn_08_b_c49dd79d

    jump a01_comn_08_end

label a01_comn_08_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause 2.0

    jump a01_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
