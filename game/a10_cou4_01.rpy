label a10_cou4_01:

    scene bg10bb with Dissolve(0.5)
    pause 1.5

    play music bgm05 fadein 1.0

    play sound se_2s_f008
    pause 1.0

    show sachiko z4 1 lg outfit i:
        xcenter 298
    with Dissolve(0.25)

    "Miyako opened the door to the broadcasting room to find Sachiko inside."

    voice "2SA_0887"
    sachiko "\"Wait, shouldn't you be in class?\""

    show miyako z4 1 lg school_a b:
        xcenter 726
    with dict_dissolve_25

    voice "2MI_1069"
    if persistent.dpatch:
        miyako "\"School's over already.\"" id a10_cou4_01_37aa5c34
    else:
        miyako "\"Class is already over.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0888"
    sachiko "\"Oh, is it that late? Human time sure is fast. Still throws me for a loop sometimes.\""

    "Sachiko said, glancing at her watch."

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0889"
    sachiko "\"So, what are you doing here? You need something in the broadcasting room?\""

    show miyako:
        "miyako z4 1 lg school_a a" with Dissolve(0.25)
        ShakeYes

    voice "2MI_1070"
    miyako "\"I came to return this.\""

    show miyako z4 1 lg school_a a:
        xoffset 0 yoffset 0
    with None

    "Miyako took a journal out of her bag. It was the one she'd taken home with her the last time she was here."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0890"
    sachiko "\"Ah...\""

    "Sachiko took the journal from her."

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1071"
    miyako "\"What are you doing here?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0891"
    sachiko "\"I finished cleaning, so now I'm just reminiscing. Pretty soon, I won't be able to come here, either.\""

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_1072"
    miyako "\"You make it sound like you'll never come back again... You can visit any time you like, can't you?\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0892"
    if persistent.dpatch:
        sachiko "\"Haha, I don't think that's happening. They're pretty strict about suspicious people around schools these days, you know.\"" id a10_cou4_01_86cfb092
    else:
        sachiko "\"Haha, I don't think that's happening. They're pretty strict about suspicious people around campus these days, you know.\""

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_1073"
    miyako "\"Suspicious...? But if you just tell them that you're comi—\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0893"
    sachiko "\"They're gonna get rid of this place soon.\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1074"
    miyako "\"Huh?\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0894"
    sachiko "\"They can't just keep the room unused forever. The broadcasting club shut down after Noel's clubmates graduated, and nobody's used the room since.\""

    "Sachiko flipped through the club journal in her hands to the page with Noel Nakatani on it."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0895"
    sachiko "\"These were the last members of the club. Oh, I was actually next to Noel when they took this picture, you know.\""

    "There were a couple of girls in uniform in the picture. Noel Nakatani was there too, but there was nothing where Sachiko was pointing."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0896"
    sachiko "\"Even after they became seniors and the other members left the club, Noel still hung out in this room a lot. It was like her hideout.\""

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_1075"
    miyako "\"......\""

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0897"
    sachiko "\"She was a real troublemaker, you know~? She'd do her own broadcasts even after the club disbanded.\""

    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_1076"
    miyako "\"...Did she get in trouble?\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0898"
    sachiko "\"Of course she did. So then she'd do them on days off, even though no one was there to hear them.\""

    "Except for Sachiko, of course."

    show miyako z4 1 lg school_b e with dict_dissolve_25

    voice "2MI_1077"
    miyako "\"I wonder if she didn't plan on going to college.\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0899"
    sachiko "\"She probably figured she wouldn't make it to spring.\""

    show miyako z4 2 lg school e with dict_dissolve_25

    voice "2MI_1078"
    miyako "\"...Oh.\""

    "She'd made another comment Miyako didn't know how to respond to."

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_1079"
    miyako "\"Umm, Noel was also an angel before being human, right?\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0900"
    sachiko "\"I dunno, but I don't think so. She didn't believe in angels, anyway. Not until I came down right in front of her, at least.\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0901"
    sachiko "\"...No, maybe she didn't even believe then.\""

    show miyako z4 1 lg school_b e with dict_dissolve_25

    voice "2MI_1080"
    miyako "\"But... how did she invite you, then?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0902"
    sachiko "\"Because she could {i}talk{/i} to me.\""

    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_1081"
    miyako "\"Talk?\""

    show sachiko:
        "sachiko z4 1 lg outfit i" with Dissolve(0.25)
        3.5
        "sachiko z4 2 lg outfit d" with Dissolve(0.25)

    voice "2SA_0903"
    sachiko "\"Though, that's a story for another... No, this is a good time for it, isn't it?\""

    show sachiko z4 2 lg outfit d:
        pass
    with None

    "She almost evaded the question like usual, but decided to be frank instead."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0904"
    sachiko "\"One day, I heard her voice. Right up there.\""

    if persistent.dpatch:
        "Sachiko pointed up above the school." id a10_cou4_01_fd2bda97
    else:
        "Sachiko pointed up above the campus."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0905"
    sachiko "\"Sometimes you can hear people on the ground when you're flying, so it wasn't really surprising or anything, but...\""

    show miyako z4 1 lg school_b a with dict_dissolve_25

    "Miyako nodded."

    voice "2SA_0906"
    sachiko "\"Just on a whim, I responded to her, not intending to be heard, but I got a reply.\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1082"
    miyako "\"But that's... Angels should be the only ones who can see and hear humans. It shouldn't work the other way around.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0907"
    sachiko "\"Right? I couldn't hear you either.\""

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_1083"
    miyako "\"...That's good.\""

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0908"
    sachiko "\"At first I thought it was one of us. I looked up, down, right, left, spun 360 degrees. But there weren't any angels anywhere nearby. There wasn't even a bird in sight. So I went down to where the voice was coming from.\""

    "This time, she pointed down."

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_1084"
    miyako "\"...The broadcasting room. The voice was Noel?\""

    show sachiko z4 1 lg outfit a with Dissolve(0.25)
    show sachiko:
        ShakeYes

    voice "2SA_0909"
    sachiko "\"Indeed.\""

    show sachiko:
        xoffset 0 yoffset 0
    with None

    "She nodded and pulled over an aged device sitting on the edge of the desk."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0910"
    sachiko "\"Check it out, it's a machine to call angels.\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1085"
    miyako "\"Huh...?\""

    voice "2SA_0911"
    sachiko "\"A piece-of-crap radio. It's a Device.\""

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_1086"
    miyako "\"Again... This is the second one.\""

    "It was. The first was Hina's toy camera. There's actually a lot of them, huh?"

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0912"
    sachiko "\"It's basically useless as an actual transceiver. I'm sure Noel knew that too and was just talking into it to fool around.\""

    "So they were essentially doing the same thing."

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1087"
    miyako "\"Did you always talk through this Device?\""

    voice "2SA_0913"
    sachiko "\"Yep. Just like hams.\""

    "\"Hams\" refers to amateur radio operators."

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0914"
    sachiko "\"But the thing barely worked as a Device, either. When it wasn't in the mood, it wouldn't connect for days.\""

    "Which would mean a return to the usual one-way communication."

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0915"
    sachiko "\"Every time that would happen, Noel would give the thing a good whack.\""

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_1088"
    miyako "\"...It does look a little banged up.\""

    "Well, if you don't know how to fix it, what are you gonna do? Who even knows if it was receiving through the antenna or not."

    "...And what was it doing in the broadcasting club room anyway?"

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0916"
    sachiko "\"When she heard my voice, she probably thought it was coming through the air waves. She had no idea I was right next to her when we were talking.\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1089"
    miyako "\"You didn't tell her you were an angel?\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0917"
    sachiko "\"No, I told her that right away. But she thought it was my call sign and busted a gut about it, telling me I had really dorky taste.\""

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_1090"
    miyako "\"Ahaha, that's mean.\""

    "No it's not."

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0918"
    sachiko "\"But that was the start of things between Noel and me.\""

    "Sachiko looked down at the picture in the club journal."

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1091"
    miyako "\"What was Noel like? Was she... sort of unusual?\""

    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0919"
    sachiko "\"She was {i}very{/i} unusual. Stubborn, pushy. A smoker even though she wasn't healthy. She was a troublemaker, and reckless—\""

    "Sachiko rattled off a list."

    show miyako z4 1 lg school_b e with dict_dissolve_25

    voice "2MI_1092"
    miyako "\"And she smiled a lot?\""

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0920"
    sachiko "\"Y-Yeah... How'd you know?\""

    show miyako z4 1 lg school_b b with dict_dissolve_25

    voice "2MI_1093"
    miyako "\"Well, she has a brilliant smile in your painting of her.\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0921"
    sachiko "\"...Yeah. She laughed a lot, and she got mad a lot, too. Actually, she just experienced all her emotions intensely. It was kind of exhausting.\""

    show miyako z4 1 lg school_b c with dict_dissolve_25

    voice "2MI_1094"
    miyako "\"...Heheh.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0922"
    sachiko "\"What?\""

    show miyako z4 1 lg school_a b with dict_dissolve_25

    voice "2MI_1095"
    miyako "\"You're complaining, but you seem to really enjoy talking about her.\""

    show sachiko:
        "sachiko z4 2 lg outfit j" with Dissolve(0.25)
        1.2
        "sachiko z4 2 lg outfit c" with Dissolve(0.25)

    voice "2SA_0923"
    sachiko "\"I guess so... Well, for better or worse, she was just filled with energy. The sheer heat of her was just so novel to me.\""

    show sachiko z4 2 lg outfit c:
        pass
    with None
    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1096"
    miyako "\"She sounds like you.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0924"
    sachiko "\"...I'm just a cheap imitation. It's like I'm doing an impression of her. I told you I got it all from her, right?\""

    "Sachiko smiled, but it was a lonely smile."

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0925"
    sachiko "\"I was empty before I met Noel. Tired of the tedium of eternity, but pitying of the fleeting lives of those on the surface...\""

    show miyako z4 1 lg school_a a with dict_dissolve_25

    voice "2MI_1097"
    miyako "\"I can't imagine that.\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0926"
    sachiko "\"I was an angel who would live eternally, and she was always standing face-to-face with death. We saw the world in completely different ways.\""

    show sachiko z4 2 lg outfit d with dict_dissolve_25

    voice "2SA_0927"
    sachiko "\"'If you don't want it, I'll take your eternity for you'...\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1098"
    miyako "\"Huh?\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0928"
    sachiko "\"That's what she'd say to me whenever I told her about how bored I was.\""

    show miyako z4 2 lg school b with dict_dissolve_25

    voice "2MI_1099"
    miyako "\"...How long did you talk?\""

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0929"
    sachiko "\"It was from summer break until Christmas, so about half a year.\""

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1100"
    miyako "\"Wait, but you came down to earth...\""

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0930"
    sachiko "\"Yep, Christmas Eve. So I was only able to be with her in person that one night.\""

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0931"
    sachiko "\"She got worse as it got colder. And then that Christmas morning, she was gone.\""

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_1101"
    miyako "\"......\""

    show sachiko z4 2 lg outfit e with dict_dissolve_25

    voice "2SA_0932"
    sachiko "\"I... got close to you up on the roof before, right? I came to my senses then because I was remembering that.\""

    show miyako z4 2 lg school f with dict_dissolve_25

    voice "2MI_1102"
    miyako "\"...Oh.\""

    pause 0.5

    window hide
    scene white with Dissolve(0.3)
    pause 0.1

    show kimikara_23_b_flat at truecenter:
        alpha 0.0 zoom 1.12
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein 0.3 zoom 1.0
        2.0
        parallel:
            linear 0.3 alpha 0.0
        parallel:
            easein 0.3 zoom 1.12

    pause 3.6

    scene bg10bb
    show sachiko z4 2 lg outfit f:
        xcenter 298
    show miyako z4 2 lg school f:
        xcenter 726
    with Dissolve(1.0)

    pause 1.0

    window auto

    voice "2SA_0933"
    sachiko "\"Yep. So that's the 'story for another time' I've been playing coy about.\""

    "Sachiko stretched, the folding chair creaking under her."

    show miyako z4 2 lg school c with dict_dissolve_25

    voice "2MI_1103"
    miyako "\"Umm... thank you... for telling me.\""

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0934"
    sachiko "\"I've always regretted not coming down sooner. Why was I so afraid to throw away the eternity I was so bored with?\""

    "Sachiko spoke with a self-deprecating tone as she looked up to the ceiling."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0935"
    sachiko "\"So I think you're really impressive for coming down in just one month.\""

    show miyako z4 2 lg school d with dict_dissolve_25

    voice "2MI_1104"
    miyako "\"...That was because of you.\""

    hide sachiko
    hide miyako
    with dict_dissolve_50

    play sound se_2s_h012

    "Sachiko pushed the chair back and stood up."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0936"
    sachiko "\"Well, I'm gonna get going. You should—\""

    show miyako 1 lg school_a j with dict_dissolve_25

    voice "2MI_1105"
    miyako "\"Umm! Could I stand in?\""

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0937"
    sachiko "\"Stand in?\""

    show miyako 1 lg school_a i with dict_dissolve_25

    voice "2MI_1106"
    miyako "\"For Noel.\""

    show miyako:
        xcenter 512
        easein 0.5 xcenter 252
    pause 0.5

    show sachiko 1 lg outfit i behind miyako at pos_r with Dissolve(0.25)

    voice "2SA_0938"
    sachiko "\"...That's quite a thing to say. You're not scared to do that?\""

    show miyako 1 lg school_a e with dict_dissolve_25

    voice "2MI_1107"
    miyako "\"I'm... not. I just told you the thing I most wanted to tell you right now.\""

    show miyako 1 lg school_a j with dict_dissolve_25

    voice "2MI_1108"
    miyako "\"I'll support you until you can forgive yourself. Like I'm sure Noel would have.\""

    show sachiko:
        "sachiko 2 lg outfit b" with Dissolve(0.25)
        3.5
        "sachiko 2 lg outfit a" with Dissolve(0.25)

    voice "2SA_0939"
    sachiko "\"And what would you do if I said, 'what do you know about Noel'?\""

    show sachiko 2 lg outfit a:
        pass
    with None
    show miyako 1 lg school_a i with dict_dissolve_25

    voice "2MI_1109"
    miyako "\"I don't know. But I do know that I'm the only one who can take her place!\""

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_0940"
    sachiko "\"That's very heroic of you. I'm even more impressed.\""

    show miyako 1 lg school_a j with dict_dissolve_25

    voice "2MI_1110"
    miyako "\"I want to become Noel.\""

    "Ha."

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_0941"
    sachiko "\"...That's very kind of you. But you can't.\""

    "Sachiko shook her head."

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0942"
    sachiko "\"No one can take her place. Especially not you...\""

    "Sachiko put a hand to Miyako's cheek and looked deep into her eyes."

    show miyako 2 lg school d with dict_dissolve_25

    voice "2MI_1111"
    miyako "\"I—\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0943"
    sachiko "\"You need to live for yourself.\""

    "Sachiko pulled away and gave her a pat on the head."

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "2SA_0944"
    sachiko "\"Sorry to invite you and then leave you to fend for yourself~ But it is great down here... That much is true.\""

    show miyako 2 lg school b with dict_dissolve_25

    voice "2MI_1112"
    miyako "\"...Sachiko.\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0945"
    sachiko "\"Hm?\""

    show miyako 1 lg school_a i with dict_dissolve_25

    voice "2MI_1113"
    miyako "\"If I hadn't come down in this form... could you have loved me?\""

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_0946"
    sachiko "\"......\""

    stop music fadeout 1.0

    hide sachiko
    hide miyako
    with dict_dissolve_50

    "Sachiko smiled sadly at her and gave her a gentle kiss."

    "Then she left the room without another word."

    $ side_image = "miyako 2 side school e"

    voice "2MI_1114"
    miyako "\"...Will you not live for {i}yourself{/i}?\""

    "I don't know if her words reached Sachiko or not."

    $ side_image = "miyako 2 side school d"

    voice "2MI_1115"
    miyako "\"......\""

    play sound se_2s_h012

    "Miyako sat down unsteadily in the chair Sachiko had been using."

    play sound se_noize
    pause 1.5

    show miyako 1 lg school_a f:
        xcenter 512
        ShakeSide
    with dict_dissolve_25

    voice "2MI_1116"
    miyako "\"...!\""

    show miyako 1 lg school_a f:
        xoffset 0 yoffset 0
    with None

    "—I've been waiting for you, Lionheart."

    python:
        _last_say_what = ""
        _last_say_who = None
        renpy.choice_for_skipping()

    scene select_back3 with Dissolve(0.5)
    pause 1.5

    menu:
        "■選択肢１枠"((0,273), "menu/btn_select_0701"):
            jump a10_cou4_01_g

label a10_cou4_01_g:

    scene bg10bb
    show miyako 1 lg school_a f
    with Dissolve(0.5)

    play sound howling
    pause 5.0

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.875)
    pause 1.75


    if route2 == 1:
        jump a10_cou1_05
    elif route2 == 2:
        jump a10_cou2_06
    elif route2 == 3:
        jump a10_cou3_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
