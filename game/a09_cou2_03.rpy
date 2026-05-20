label a09_cou2_03:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Sunday afternoon. Hina and Rin strolled through town."

    show hina z4 1 lg casual_scarf a:
        xcenter 298
    show rin z4 1 lg casual k:
        xcenter 726
    with Dissolve(0.25)

    show rin:
        ShakeTameiki

    voice "2RI_0954"
    rin "\"Whew...\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin sighed, some fatigue in her expression."

    show hina z4 1 lg casual_scarf k with dict_dissolve_25

    voice "2HI_0992"
    hina "\"Tired?\""

    "Hina looked up when she heard the sigh."

    show rin:
        "rin z4 1 lg casual b" with Dissolve(0.25)
        0.8
        "rin z4 1 lg casual j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_0955"
    rin "\"A little... wah!\""

    show rin z4 1 lg casual j:
        xoffset 0 yoffset 0
    with None

    "Rin lost her balance at a sudden tug on her arm."

    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff!\""

    "She'd staggered because of a dog. The Asous' dog, Arthur. He was an almost fully-grown golden retriever, so he was pretty big."

    show hina:
        "hina z4 1 lg casual_scarf a" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0993"
    hina "\"Not that way, Arthur. Your house is this way.\""

    show hina z4 1 lg casual_scarf a:
        xoffset 0 yoffset 0
    with None

    "Arthur obediently returned to their original route."

    "Rin had to jog a little to keep up with the tugging on the leash."

    show rin z4 2 lg casual d with dict_dissolve_25

    voice "2RI_0956"
    rin "\"...I'm kinda sorry about this.\""

    show hina z4 1 lg casual_scarf k with dict_dissolve_25

    voice "2HI_0994"
    hina "\"Hm? About what?\""

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0957"
    rin "\"Well, we were supposed to be going on a date, but we just ended up walking Arthur instead.\""

    show hina z4 2 lg casual_scarf a with dict_dissolve_25

    voice "2HI_0995"
    hina "\"Oh, that? I was the one who told Asou we didn't mind.\""

    "She'd asked them to walk the dog since their bakery was so busy."

    show rin z4 2 lg casual b with dict_dissolve_25

    voice "2RI_0958"
    rin "\"I actually had a lot of stuff planned, though. Go there, stop by that store...\""

    "Rin was the type to start with the superficial trappings and go from there."

    show hina z4 2 lg casual_scarf g with dict_dissolve_25

    voice "2HI_0996"
    hina "\"Eheh, you planned stuff? That makes me happy enough.\""

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0959"
    rin "\"Y-Yeah...\""

    "Hina's innocent smile was too much for her."

    show hina z4 1 lg casual_scarf c with dict_dissolve_25

    voice "2HI_0997"
    hina "\"And I had fun walking Arthur, too♪\""

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0960"
    rin "\"It was the first time I ever played with a dog in a park.\""

    show hina z4 1 lg casual_scarf b with dict_dissolve_25

    voice "2HI_0998"
    hina "\"And Arthur's so smart. He's really good at fetch, isn't he?\""

    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff!\""

    show rin z4 2 lg casual a with dict_dissolve_25

    voice "2RI_0961"
    rin "\"Yeah, he's smart, but I'm more impressed with your stamina.\""

    show hina z4 1 lg casual_scarf k with dict_dissolve_25

    voice "2HI_0999"
    hina "\"You are?\""

    show rin z4 2 lg casual e with dict_dissolve_25

    voice "2RI_0962"
    rin "\"I mean, I was throwing the ball for Arthur, but you went running right with him. You probably moved around the same amount he did.\""

    show hina z4 2 lg casual_scarf b with dict_dissolve_25

    voice "2HI_1000"
    hina "\"Ahaha, I couldn't help it~\""

    show rin z4 1 lg casual a with dict_dissolve_25

    voice "2RI_0963"
    rin "\"It was like I had two dogs with me. A retriever and a mini shiba.\""

    show hina z4 2 lg casual_scarf d with dict_dissolve_25

    voice "2HI_1001"
    hina "\"Don't say 'mini.'\""

    "So she doesn't mind being called a shiba inu. Well, she does consider herself to be Rin's dog."

    show rin z4 1 lg casual b with dict_dissolve_25

    voice "2RI_0964"
    rin "\"Come to think of it, I heard shibas have the closest DNA to wolves out of all dogs.\""

    show hina z4 2 lg casual_scarf a with dict_dissolve_25

    voice "2HI_1002"
    hina "\"Wolves, huh? That's kinda cool.\""

    show rin z4 1 lg casual k with dict_dissolve_25

    voice "2RI_0965B"
    rin "\"I think it's kinda scary.\""

    $ side_image = "side/arthur.webp"

    voice "2AR_0001"
    arthur "\"Ruff, ruff!\""

    show rin:
        "rin z4 1 lg casual j" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_0966"
    rin "\"Waaah!\""

    show rin z4 1 lg casual j:
        xoffset 0 yoffset 0
    with None

    "Arthur yanked on the leash again. A dog on the other side of the street had gotten his attention."

    show rin:
        ShakeSide

    voice "2RI_0967"
    rin "\"W-Wait, stop!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin pleaded, at the mercy of the large dog's considerable strength."

    show hina z4 2 lg casual_scarf f with dict_dissolve_25

    voice "2HI_1003"
    hina "\"Give it here.\""

    "Hina held out her hand for the leash."

    show rin z4 1 lg casual g with dict_dissolve_25

    voice "2RI_0968"
    rin "\"Huh? Won't he pull you after him?\""

    "Naturally, she'd think that, given that she was having so much trouble at her height."

    show hina:
        "hina z4 2 lg casual_scarf a" with Dissolve(0.25)
        ShakeYes

    voice "2HI_1004"
    hina "\"I'll be fine.\""

    show hina z4 2 lg casual_scarf a:
        xoffset 0 yoffset 0
    with None

    "But Hina took the leash from Rin with full confidence."

    show hina z4 1 lg casual_scarf f with dict_dissolve_25

    voice "2HI_1005"
    hina "\"Stay!\""

    "She gave a tug on the leash to get Arthur's attention, then commanded him with her finger up."

    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff!\""

    "Arthur obeyed instantly, contrary to Rin's expectations."

    show rin z4 1 lg casual e with dict_dissolve_25

    voice "2RI_0969"
    rin "\"Huh?\""

    show hina z4 1 lg casual_scarf e with dict_dissolve_25

    voice "2HI_1006"
    hina "\"Good boy, Arthur. Down!\""

    "Arthur crouched down, and Hina handed the leash back to Rin."

    show hina z4 1 lg casual_scarf a with dict_dissolve_25

    voice "2HI_1007"
    hina "\"You're too nervous. Arthur gets confused since you're all scared when you interact with him.\""

    show rin z4 1 lg casual i with dict_dissolve_25

    voice "2RI_0970"
    rin "\"R-Right.\""

    "Since wolves lived in packs and dogs inherited many of their traits, they too had a sort of familial hierarchy and wouldn't obey someone lower than them on that hierarchy."

    "Arthur had obeyed Hina because he'd judged her to be a higher rank than him due to her firm attitude, but since Rin was irresolute when interacting with him, he wasn't sure where to place her on the hierarchy."

    show hina z4 2 lg casual_scarf a with dict_dissolve_25

    voice "2HI_1008"
    hina "\"We had a big dog once at my house, so I got a lot of practice then.\""

    voice "2RI_0971"
    rin "\"I see...\""

    "Rin still looked a little nervous. Well, she was shy. That probably applied to dogs as much as it did to humans."

    show hina z4 1 lg casual_scarf a with dict_dissolve_25

    voice "2HI_1009"
    hina "\"But Arthur's really sweet and really nice.\""

    "Hina ran her hand over Arthur's back."

    $ side_image = "side/arthur.webp"

    voice "2AR_0002"
    arthur "\"Ruff!\""

    show rin z4 1 lg casual b with dict_dissolve_25

    voice "2RI_0972"
    rin "\"Are you smart too?\""

    show hina z4 1 lg casual_scarf p with dict_dissolve_25

    voice "2HI_1010"
    hina "\"Of course I am!\""

    show rin z4 1 lg casual a with dict_dissolve_25

    voice "2RI_0973"
    rin "\"Shake.\""

    show hina:
        "hina z4 1 lg casual_scarf b" with Dissolve(0.25)
        ShakeYes

    voice "2HI_1011"
    hina "\"Yep.\""

    show hina z4 1 lg casual_scarf b:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0974"
    rin "\"Other hand.\""

    show hina:
        ShakeYes

    voice "2HI_1012"
    hina "\"Yep.\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina placed her hands on Rin's right away."

    show rin z4 1 lg casual h with dict_dissolve_25

    voice "2RI_0975"
    rin "\"Stand. Spin.\""

    show hina:
        "hina z4 1 lg casual_scarf c" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1013"
    hina "\"Toryarya~\""

    show hina z4 1 lg casual_scarf c:
        xoffset 0 yoffset 0
    with None
    hide hina with dict_dissolve_25

    "Hina jumped up and ran around Rin."

    show rin z4 2 lg casual f with dict_dissolve_25

    voice "2RI_0976"
    rin "\"Down—no, that would get your clothes dirty, so stay!\""

    $ side_image = "hina 1 side casual_scarf k"

    voice "2HI_1014"
    hina "\"Oop...\""

    "Hina carried out whatever ridiculous command Rin gave her, which actually just made Rin flustered."

    show hina z4 1 lg casual_scarf a:
        xcenter 298
    with dict_dissolve_25

    voice "2HI_1015"
    hina "\"So? Am I smart?\""

    "She said with a proud smile."

    show rin z4 1 lg casual b with dict_dissolve_25

    voice "2RI_0977"
    rin "\"Sure... I'm pretty surprised you're actually doing all of it, though.\""

    show hina z4 2 lg casual_scarf c with Dissolve(0.25)
    show hina:
        ShakeYes

    voice "2HI_1016"
    hina "\"Well, I've got this on now.\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina pulled her collar and flashed the choker she had on underneath it."

    show rin z4 2 lg casual d with dict_dissolve_25

    voice "2RI_0978"
    rin "\"...Ah, yeah.\""

    show hina z4 1 lg casual_scarf k with dict_dissolve_25

    voice "2HI_1017"
    hina "\"Hm? What is it?\""

    show rin z4 1 lg casual d with dict_dissolve_25

    voice "2RI_0979"
    rin "\"Bang!\""

    "She shot a finger gun at Hina."

    show hina:
        "hina z4 1 lg casual_scarf g" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2HI_1018"
    hina "\"Gwaaah!\""

    show hina z4 1 lg casual_scarf g:
        xoffset 0 yoffset 0
    with None
    $ side_image = "side/arthur.webp"

    voice "2AR_0001"
    arthur "\"Arf, arf~\""

    hide hina with dict_dissolve_50

    "Hina and Arthur both spun around like they'd been shot."

    show rin z4 1 lg casual b with dict_dissolve_25

    voice "2RI_0980"
    rin "\"......\""

    "From the muzzle of the gun came not smoke, but a band-aid that was starting to peel off."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou2_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
