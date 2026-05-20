label a01_comn_08:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene ev01g with Dissolve(0.5)

    play music bgm01

    voice "HIN_0163"
    hina "\"♪Nyaga nyaga! Nya, nya nya nya!\""

    voice "RIN_0155"
    rin "\"......\""

    voice "HIN_0164"
    hina "\"♪Nya nya nya nya! Nya, nya nya nya!\""

    scene ev01h with Dissolve(0.5)

    voice "RIN_0156"
    rin "\"...Ahem.\""

    scene ev01k with Dissolve(0.5)

    voice "FUM_0117"
    fumi "\"...Ah...\""

    voice "HIN_0165"
    hina "\"♪Nyaga nyaga! Nya, nya nya nya!\""

    voice "RIN_0157"
    rin "\"...Shut up...\""

    voice "FUM_0118"
    fumi "\"...Ah, ah...\""

    voice "HIN_0166"
    hina "\"♪Nyaa nyaa nyaa nya, nya nya nyaa nyaa!\""

    voice "RIN_0158"
    rin "\"Shut up!\""

    voice "HIN_0167"
    hina "\"♪Nyaga nyaga! Nya, nya nya nya!\""

    voice "FUM_0119"
    fumi "\"Ah... aaah...\""

    voice "RIN_0159"
    rin "\"...Phew.\""

    voice "FUM_0120"
    fumi "\"O... Ogata?\""

    scene bg01ca with Dissolve(0.25)

    show hina 1 sm pyjama headphones g
    show rin 1 sm pyjama h glasses at pos_l2
    show fumi 1 sm pyjama d at pos_r2
    with Dissolve(0.25)

    voice "RIN_0160"
    rin "\"Hey, Gian.\""

    play sound se555

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        function LayerShake(15,15,0.1)
    $ persistent.layer_shaken = False

    voice "HIN_0168"
    hina "\"Wah?!\""

    show hina 1 sm pyjama l -headphones:
        xoffset 0 yoffset 0
    with None

    "Rin yanked the headphones from Hina's head, and she spun around in surprise."

    show rin 1 sm pyjama h glasses with dict_dissolve_25

    voice "RIN_0161"
    rin "\"Shut up.\""

    show hina 1 sm pyjama k with dict_dissolve_25

    voice "HIN_0169"
    hina "\"Oh, was it too loud?\""

    voice "RIN_0162"
    rin "\"Yeah, your singing was.\""

    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0170"
    hina "\"Huh?\""

    show fumi 1 sm pyjama a with dict_dissolve_25

    voice "FUM_0121"
    fumi "\"Did you not know you were singing out loud?\""

    show hina 1 sm pyjama l with dict_dissolve_25

    voice "HIN_0171"
    hina "\"Huh? No way. Was I really?!\""

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0122"
    fumi "\"Quite enthusiastically.\""

    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0172"
    hina "\"Hyaaa~ That's kind of embarrassing.\""

    show rin 1 sm pyjama a glasses with dict_dissolve_25

    voice "RIN_0163"
    rin "\"You suck at singing.\""

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0173"
    hina "\"Wha?! Not even my parents ever told me that!\""

    show hina 1 sm pyjama l:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama d with dict_dissolve_25

    voice "FUM_0123"
    fumi "\"Ah... ahahaha... You have a very cute voice, though.\""

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
    hina "\"I'm kinda impressed by you, Asou.\""

    voice "FUM_0124"
    fumi "\"Wh-What brought that on?\""

    voice "HIN_0175"
    hina "\"I mean, you write in your diary every day, right?\""

    voice "FUM_0125"
    fumi "\"Well... yes, I do.\""

    voice "HIN_0176"
    hina "\"Even when it's wet and cold?\""

    voice "FUM_0126"
    fumi "\"Even when I have a cold.\""

    voice "RIN_0164"
    rin "\"Yikes, was that a joke?\""

    voice "FUM_0127"
    fumi "\"Eheheh.\""

    voice "HIN_0177"
    hina "\"That's really impressive, Asou!\""

    voice "FUM_0128"
    fumi "\"I don't think it's anything that incredible.\""

    voice "HIN_0178"
    hina "\"I wouldn't even know what to write every day.\""

    voice "FUM_0129"
    fumi "\"You just write whatever. Something that happened that day, or a thought that you had.\""

    voice "HIN_0179"
    hina "\"Hmm...\""

    voice "RIN_0165"
    rin "\"When you had to keep a summer diary for school, you always just did it all on the last day, didn't you?\""

    voice "HIN_0180"
    hina "\"What? How did you know that?\""

    jump a01_comn_08_end

label a01_comn_08_b:

    play music bgm01

    scene white with Dissolve(0.75)
    pause 0.75
    scene ev01h with bg_effect_25
    pause 0.5

    voice "RIN_0166"
    rin "\"What the heck are you always listening to anyway, Hina?\""

    voice "HIN_0181"
    hina "\"Heheh, western stuff.\""

    voice "RIN_0167"
    rin "\"What's with the smirk? I was looking for, like, an artist name or something.\""

    voice "HIN_0182"
    hina "\"Umm, I dunno who they are.\""

    voice "RIN_0168"
    rin "\"You're listening to bands you don't know?\""

    voice "HIN_0183"
    hina "\"It's just stuff my dad gave me.\""

    voice "RIN_0169"
    rin "\"I didn't know you were good at English?\""

    voice "HIN_0184"
    hina "\"Nuh-uh. Not at all. So I've got no idea what they're singing about.\""

    voice "RIN_0170"
    rin "\"Do you know the genre, at least?\""

    voice "HIN_0185"
    hina "\"Heheh, heheh, rock 'n' roll!\""

    voice "RIN_0171"
    rin "\"I seriously don't get why you're so smug about it.\""

    voice "FUM_0130"
    fumi "\"Ahahahaha.\""

    voice "RIN_0172"
    rin "\"Lemme hear.\""

    "Hina handed the headphones to Rin."

    voice "RIN_0173"
    rin "\"A CD player in this day and age? You must have taken real good care of this thing.\""

    voice "HIN_0186"
    hina "\"I just bought the headphones last year, though.\""

    "Rin looked the CD player over curiously, then put the headphones on."

    voice "FUM_0131"
    fumi "\"Did your dad give you the CD player, too?\""

    voice "HIN_0187"
    hina "\"Yep. It's pretty old now, though, so it doesn't work great.\""

    voice "RIN_0174"
    rin "\"...When's this song from?\""

    voice "HIN_0188"
    hina "\"It was popular when my dad was younger.\""

    voice "FUM_0132"
    fumi "\"A golden oldie? Can I hear it too, after Ogata?\""

    voice "HIN_0189"
    hina "\"Yeah, it's really cool. I dunno what they're saying, though.\""

    voice "RIN_0175"
    rin "\"I know the hook of this, though. I think it was in a commercial a little bit ago. Something about a mom forgetting to buy instant ramen for her son when he's up late studying or some such.\""

    voice "HIN_0190"
    hina "\"Huh?! That's what this song is about? Even though it sounds so cool?\""

    voice "RIN_0176"
    rin "\"No, I think they changed the lyrics for the commercial. They're singing about something else in this.\""

    voice "HIN_0191"
    hina "\"Oh, good~\""

    voice "RIN_0177"
    rin "\"But more importantly...\""

    voice "HIN_0192"
    hina "\"What?\""

    voice "RIN_0178"
    rin "\"How did hard rock like this turn into whatever sick animal impression you were doing earlier?\""

    voice "HIN_0193"
    hina "\"Nyanya?\""

    jump a01_comn_08_end

label a01_comn_08_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause 2.0

    jump a01_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
