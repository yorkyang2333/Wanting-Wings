label a07_cou1_02:

    scene bg11aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "rin 1 side casual a"

    voice "2RI_0165RE"
    rin "\"Hey, Takaoka, you got plans after this?\"" id a07_cou1_02_c0d183a2

    "Rin's question came from behind Miyako."

    "The three girls had been walking a bit behind her, but they caught up when they came to a red light."

    show miyako 1 lg casual_a e at pos_l
    show rin 2 lg casual b at pos_r
    with dict_dissolve_25

    voice "2MI_0172"
    miyako "\"Not really. What about you, Ogata?\"" id a07_cou1_02_05a8f9ed

    voice "2RI_0166RE"
    rin "\"I don't really either.\"" id a07_cou1_02_3e7f76f8

    show miyako 1 lg casual_a b with dict_dissolve_25

    voice "2MI_0173"
    miyako "\"Oh yeah~?\"" id a07_cou1_02_001eb80d

    play sound se_streets

    "......"

    pause 1.0

    "Two cars passed as they stood in silence."

    $ side_image = "hina 2 side casual_scarf f"

    voice "2HI_0174"
    hina "\"Hey...\"" id a07_cou1_02_64a589b6

    show rin 1 lg casual d with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "2RI_0167RE"
    rin "\"If you don't have plans, do you want to hang out with me?\"" id a07_cou1_02_9b04a4d4

    show rin:
        xoffset 0 yoffset 0
    with None

    "She finished her invitation as Hina tried to awkwardly cut in."

    show miyako 2 lg casual a with dict_dissolve_25

    voice "2MI_0174"
    miyako "\"Sure, I don't mind...\"" id a07_cou1_02_20570d5e

    "Head cocked, Miyako looked past Rin to Hina and Fumi."

    hide rin
    hide miyako
    with Dissolve(0.5)

    show fumi 2 sm casual h:
        xcenter 382
    show hina 2 sm casual_scarf f:
        xcenter 642
    with Dissolve(0.25)

    $ side_image = "rin 2 side casual e"

    voice "2RI_0168"
    rin "\"Umm. These two have plans after this. Right?\"" id a07_cou1_02_adf08298

    "She turned back to them and gave them a wink."

    "Hina and Fumi exchanged a look, then:"

    show fumi:
        "fumi 2 sm casual b" with Dissolve(0.25)
        yoffset 0
        ease 0.25 yoffset 15
        ease 0.25 yoffset 0
    show hina:
        "hina 2 sm casual_scarf c" with Dissolve(0.25)
        ShakeYes

    $ voice2("hina","2HI_0175","fumi","2FU_0145")
    hina_fumi "\"Yeah.\"\n\"Yes.\"" (what_rest_indent=0)

    show fumi 2 sm casual b:
        xoffset 0 yoffset 0
    show hina 2 sm casual_scarf c:
        xoffset 0 yoffset 0
    with None

    "They replied together."

    hide fumi
    hide hina
    with Dissolve(0.5)

    show miyako 2 lg casual c at pos_l
    show rin 2 lg casual e at pos_r
    with dict_dissolve_25

    voice "2MI_0175"
    miyako "\"Alright. Thanks for inviting me, Ogata.\"" id a07_cou1_02_81659804

    "Fumi and Hina gave appreciative bows behind Rin. Miyako smiled back at them."

    show rin 1 lg casual k with dict_dissolve_25

    voice "2RI_0169"
    rin "\"G-Great. Let's hang out for about two hours.\"" id a07_cou1_02_1f10171f

    "Fumi and Hina's smiles became a bit strained at the specific nature of her suggestion."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg11aa with bg_effect_05
    pause 0.5

    "........."

    "They walked off, holding hands."

    "Rin watched them with a wry smile, Miyako with a genuine one."

    show miyako 1 sm casual_a b at pos_ls
    show rin 2 sm casual e at pos_rs
    with dict_dissolve_25

    voice "2RI_0170"
    rin "\"Sorry about the kiddos. Don't hold it against them.\"" id a07_cou1_02_14125835

    voice "2MI_0176"
    miyako "\"Of course. I think they're adorable.\"" id a07_cou1_02_2b4b2004

    show rin 2 sm casual b with dict_dissolve_25

    voice "2RI_0171"
    rin "\"Umm... hmm, I guess I should probably tell you. I mean, it's not like it's a secret or anything, but...\"" id a07_cou1_02_64a253fc

    show miyako 1 sm casual_a e with dict_dissolve_25

    voice "2MI_0177"
    miyako "\"You mean about Natsume and Asou?\"" id a07_cou1_02_c83f1c33

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0172"
    rin "\"Uh... yeah. Like... let's see... you know how they're really close?\"" id a07_cou1_02_4f88d670

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0178"
    miyako "\"I suppose so.\"" id a07_cou1_02_23cfa467

    show rin 2 sm casual b with dict_dissolve_25

    voice "2RI_0173"
    rin "\"I guess you could say their closeness isn't really from friendship, per se...\"" id a07_cou1_02_833b1c09

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0179"
    miyako "\"......\"" id a07_cou1_02_46b22abc

    show rin 1 sm casual g with dict_dissolve_25

    voice "2RI_0174"
    rin "\"Oh, but they are definitely friends, it's just, in their case... they're also...\"" id a07_cou1_02_16cdf123

    show rin 1 sm casual h with dict_dissolve_25

    voice "2RI_0175"
    rin "\"You know... the way they like each other is...\"" id a07_cou1_02_3f4b38d8

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0180"
    miyako "\"They're dating, right?\"" id a07_cou1_02_425cc602

    show rin:
        "rin 1 sm casual j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_0176B"
    rin "\"Huh... ah... oh... yeah! You knew?\"" id a07_cou1_02_ae022a9e

    show rin 1 sm casual j:
        xoffset 0 yoffset 0
    with None

    "With how easily what she'd been trying to say was put into words, Rin couldn't help but point at Miyako in surprise."

    show miyako 2 sm casual d with dict_dissolve_25

    voice "2MI_0181"
    miyako "\"Oh... I could just tell.\"" id a07_cou1_02_f273c751

    "The truth was that she'd been watching from the beginning."

    show rin 2 sm casual d with dict_dissolve_25

    voice "2RI_0177"
    rin "\"They're being pretty open about it, but they don't really bring it up to other people.\"" id a07_cou1_02_5fb50429

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0182"
    miyako "\"Even people in heterosexual relationships often don't announce it to other people.\"" id a07_cou1_02_2f68e270

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0178"
    rin "\"Right... So, that kinda thing doesn't bother you, Takaoka?\"" id a07_cou1_02_fd75632b

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0183"
    miyako "\"What thing?\"" id a07_cou1_02_dcb2c9fc

    show rin 2 sm casual d with dict_dissolve_25

    voice "2RI_0179"
    rin "\"You know... how they're both girls.\"" id a07_cou1_02_5929f206

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0184"
    miyako "\"I think they make a very nice couple.\"" id a07_cou1_02_ca8073d3

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0180"
    rin "\"Huh. Guess I didn't need to be worried.\"" id a07_cou1_02_671b58ad

    show rin 1 sm casual k with dict_dissolve_25

    voice "2RI_0181"
    if persistent.dpatch:
        rin "\"Holding hands and hugging and stuff is pretty normal between friends at an all girls' school anyway.\"" id a07_cou1_02_e8b907c6
    else:
        rin "\"Holding hands and hugging and stuff is pretty normal between friends at an all girls' campus anyway.\"" id a07_cou1_02_4df45967

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0185"
    miyako "\"Anything that people in a relationship do is normal.\"" id a07_cou1_02_22248308

    show rin 1 sm casual c with dict_dissolve_25

    voice "2RI_0182"
    rin "\"...Yeah. Thanks.\"" id a07_cou1_02_837886f9

    show rin 1 sm casual d with dict_dissolve_25

    voice "2RI_0183RE"
    rin "\"You're right... They look super innocent, but they're doing more than that, aren't they~? Oh, not that I've seen it or anything.\"" id a07_cou1_02_9e18e720

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0186"
    miyako "\"Ahahaha.\"" id a07_cou1_02_7ee475d9

    "Miyako had."

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0184RE"
    rin "\"So, sorry, but you don't mind hanging out with me for a bit?\"" id a07_cou1_02_0d8cdf3f

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0187"
    miyako "\"Of course not.\"" id a07_cou1_02_57ae38bb

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg11aa with bg_effect_05
    pause 0.5

    "........."

    "......"

    "They walked down the deserted street."

    $ side_image = "miyako 1 side casual_a b"

    voice "2MI_0188"
    miyako "\".........\"" id a07_cou1_02_26528cdb

    $ side_image = "rin 2 side casual a"

    voice "2RI_0185B"
    rin "\"......\"" id a07_cou1_02_28aef9b3

    $ side_image = "miyako 1 side casual_a b"

    voice "2MI_0189"
    miyako "\".........\"" id a07_cou1_02_4d2f1d91

    $ side_image = "rin 1 side casual h"

    voice "2RI_0186B"
    rin "\"......\"" id a07_cou1_02_723d2ffb

    "They strolled without conversation. A fact they clearly had different levels of comfort about."

    "Rin was anxious, trying to find something to say, and Miyako was perfectly comfortable, enjoying the scenery."

    show rin 1 sm casual g at pos_rs with dict_dissolve_25

    voice "2RI_0187"
    rin "\"U-Umm—\"" id a07_cou1_02_fd00e569

    show miyako 1 sm casual_a b at pos_ls with dict_dissolve_25

    voice "2MI_0190"
    miyako "\"Ogata, is this stuffed animal—\"" id a07_cou1_02_140d6773

    "She'd attempted to say something several times, and when she'd finally succeeded, Miyako had spoken up at the same time."

    show miyako 2 sm casual a with dict_dissolve_25

    voice "2MI_0191"
    miyako "\"Oh, I'm sorry.\"" id a07_cou1_02_d172c042

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0188"
    rin "\"No, it wasn't important. You go first.\"" id a07_cou1_02_e3683499

    "Rin looked relieved, in fact."

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0192"
    miyako "\"Okay. Is this stuffed animal from the same line as the ones Asou has in our room?\"" id a07_cou1_02_1de2a8b3

    "Miyako had stopped and was looking at a cart out in front of a small toy shop."

    "The cart did seem to have some familiar stuffed faces on it. All the animals had angel wings on their backs."

    show rin 1 sm casual a with dict_dissolve_25

    voice "2RI_0189"
    rin "\"Let's see... Yeah, looks like these are legit Angel Zoo products.\"" id a07_cou1_02_108dd2da

    "Rin had picked one from the cart and inspected its tag. Very direct, just like her."

    show rin 1 sm casual k with dict_dissolve_25

    voice "2RI_0190"
    rin "\"Good thing Asou's not with us. She'd add these to her collection.\"" id a07_cou1_02_eb572b37

    "She sighed, putting the stuffed animal back."

    show miyako 1 sm casual_a g with dict_dissolve_25

    voice "2MI_0193"
    miyako "\"Do you not like stuffed animals, Ogata?\"" id a07_cou1_02_3f581cf6

    show rin 1 sm casual b with dict_dissolve_25

    voice "2RI_0191"
    rin "\"That's not it. She just has too many. And she just sent a few back home at the end of the year.\"" id a07_cou1_02_5b88be88

    show rin 1 sm casual a with dict_dissolve_25

    voice "2RI_0192"
    rin "\"Asou's usually really mature, but she's childish in the weirdest way sometimes. Like when angels come up, she's all...\"" id a07_cou1_02_7d634c31

    "She brought her hands close together in front of her face, giving herself tunnel vision."

    show rin 1 sm casual k with dict_dissolve_25

    voice "2RI_0193"
    rin "\"And Hina's a little baby, just like she looks. I just worry about leaving the two of them to their own devices, you know?\"" id a07_cou1_02_6ba6ffb5

    show miyako 1 sm casual_a a with dict_dissolve_25

    voice "2MI_0194"
    miyako "\"......\"" id a07_cou1_02_de42ae95

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0194"
    rin "\"...That's not true. I'm the one they're always doing things for. All I can do for them is give them time alone like this.\"" id a07_cou1_02_74f15633

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0195"
    miyako "\"Isn't that enough?\"" id a07_cou1_02_e4916699

    show rin 1 sm casual i with dict_dissolve_25

    voice "2RI_0195"
    rin "\"W-Well, either way, we're not putting more stuffed animals in that room! Otherwise they might claim the beds for their own and the humans will have to sleep on the floor!\"" id a07_cou1_02_4e72d008

    show miyako 2 sm casual c with dict_dissolve_25

    voice "2MI_0196"
    miyako "\"Ahaha. That wouldn't be good.\"" id a07_cou1_02_e19d13b3

    "They laughed, then fell silent for a time."

    show rin 1 sm casual c with dict_dissolve_25

    voice "2RI_0196"
    rin "\"...Anyway, don't worry. I'm sure those two will take care of you too, Takaoka.\"" id a07_cou1_02_817c6540

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0197"
    miyako "\"Yes, I know. They already are.\"" id a07_cou1_02_1501f84f

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0197"
    rin "\"Right. It was the same when they'd just met me...\"" id a07_cou1_02_ad132ecf

    voice "2RI_0198"
    rin "\"I shouldn't be worrying about you. You're a way better communicator than me.\"" id a07_cou1_02_da4595f6

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0198"
    miyako "\"No, I'm happy you're concerned about me.\"" id a07_cou1_02_8174098e

    show rin 2 sm casual d with dict_dissolve_25

    voice "2RI_0199B"
    rin "\"You're all such good girls. Maybe I'm the one who's really just a kid.\"" id a07_cou1_02_89147427

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0199"
    miyako "\"I think you're a good girl too, Rin.\"" id a07_cou1_02_aaa6d64f

    show rin 2 sm casual g with dict_dissolve_25

    voice "2RI_0200"
    rin "\"I am? How's that?\"" id a07_cou1_02_0697b962

    show miyako 1 sm casual_a c with dict_dissolve_25

    voice "2MI_0200"
    miyako "\"You care so much about Asou and Natsume, don't you?\"" id a07_cou1_02_b1042d03

    show rin 1 sm casual g with dict_dissolve_25

    voice "2RI_0201"
    rin "\"...Well, they're my roommates.\"" id a07_cou1_02_7c4258ad

    show miyako 1 sm casual_b b with dict_dissolve_25

    voice "2MI_0201"
    miyako "\"And you're spending time with me, too.\"" id a07_cou1_02_3a7fec3d

    show rin 1 sm casual b with dict_dissolve_25

    voice "2RI_0202"
    rin "\"Well... it's more like killing time, isn't it?\"" id a07_cou1_02_3139a86e

    "Rin averted her eyes."

    show miyako 1 sm casual_b h with dict_dissolve_25
    voice "2MI_0202"
    miyako "\"I hope we can be good friends.\"" id a07_cou1_02_60b65c05

    show rin 2 sm casual e with dict_dissolve_25

    voice "2RI_0203"
    rin "\"...Yeah.\"" id a07_cou1_02_4aac01be

    show miyako 1 sm casual_a b with dict_dissolve_25

    voice "2MI_0203"
    miyako "\"Should we hold hands too?\"" id a07_cou1_02_9cfffd52

    show rin 1 sm casual i with dict_dissolve_25

    voice "2RI_0204"
    rin "\"That's not... I, uhh...\"" id a07_cou1_02_a0d13533

    "Rin hid her hands in her pockets."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_cou1_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
