label a08_comn_01:

    scene expression "gui/kimikara/mainmenu_ground1.webp"
    show expression "gui/kimikara/title2.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter08 with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg06aa with Dissolve(0.5)
    pause 2.0

    play music bgm01

    show bg_obi
    show hina 1 lg school c with dict_dissolve_25

    voice "2HI_0398"
    hina "\"That was great!\"" id a08_comn_01_d9266134

    $ side_image = "fumi 2 side school g"

    voice "2FU_0390"
    fumi "\"Wow, that was fast.\"" id a08_comn_01_f3e81369

    show hina 1 lg school b with dict_dissolve_25

    voice "2HI_0399"
    hina "\"Well, it's tasty. And we had PE in the morning.\"" id a08_comn_01_bff1df19

    $ side_image = "rin 2 side school a"

    voice "2RI_0434"
    rin "\"Are you chewing?\"" id a08_comn_01_dbc1b422

    show hina 1 lg school q with dict_dissolve_25

    voice "2HI_0400"
    hina "\"I am.\"" id a08_comn_01_b8922d16

    "Hina said, baring her teeth. They were very straight."

    hide hina with Dissolve(0.25)

    show fumi 2 lg school i at pos_l
    show miyako 1 lg school_a e at pos_r
    with dict_dissolve_25

    voice "2FU_0391"
    fumi "\"It makes me happy to see you enjoy my cooking so much.\"" id a08_comn_01_c0c81912

    voice "2MI_0295"
    miyako "\"I should hurry.\"" id a08_comn_01_0ca66a3f

    "Miyako rushed her chopsticks along, her lunch still only half-eaten."

    $ side_image = "rin 1 side school a"

    voice "2RI_0435"
    rin "\"It's more like you savor every bite than you eat slow, Mikoyan.\"" id a08_comn_01_71fcda6b

    show fumi 2 lg school c with dict_dissolve_25

    voice "2FU_0392"
    fumi "\"That makes me happy, too. You don't have to rush, lunch isn't over yet.\"" id a08_comn_01_4f8ebb66

    show miyako 1 lg school_a b with dict_dissolve_25

    voice "2MI_0296"
    miyako "\"Thank you.\"" id a08_comn_01_6864bb67

    hide fumi
    hide miyako
    with Dissolve(0.25)

    show hina 1 lg school a at pos_l
    show rin 2 lg school a at pos_r
    with dict_dissolve_25

    voice "2RI_0436"
    rin "\"Hm? Hina, why'd you leave your meatball? Didn't you like those? Did you drop it?\"" id a08_comn_01_84439e68

    "There was indeed a single meatball left on the lid of Hina's lunchbox."

    show hina 1 lg school p with dict_dissolve_25

    voice "2HI_0401"
    hina "\"Oh, this is an offering.\"" id a08_comn_01_abc249a2

    "Hina stood and headed into the back of the chapel with her lunchbox lid."

    show hina 1 lg school m with dict_dissolve_25

    play sound se_kashiwade

    voice "2HI_0402"
    hina "\"I'll be counting on you again, Miss Angel.\"" id a08_comn_01_c61a9492

    "She left her \"offering\" under the stained glass and clapped her hands."

    show rin 2 lg school e with dict_dissolve_25

    voice "2RI_0437"
    rin "\"Huh? What are you doing?\"" id a08_comn_01_e5d0ab3b

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_0403"
    hina "\"For our proficiency tests. Remember? I asked at the end of last semester and got through my supplementary exams because of it.\"" id a08_comn_01_1877a1e0

    show rin 2 lg school b with dict_dissolve_25

    voice "2RI_0438"
    rin "\"You still don't clap at a chapel.\"" id a08_comn_01_a6f4128b

    show hina 1 lg school d with dict_dissolve_25

    voice "2HI_0404"
    hina "\"What~? I thought we decided it was okay at that shrine.\"" id a08_comn_01_6d0d95e2

    show rin 1 lg school g with dict_dissolve_25

    voice "2RI_0439"
    rin "\"We did not.\"" id a08_comn_01_70411d58

    show hina 1 lg school m with dict_dissolve_25

    voice "2HI_0405"
    hina "\"Well, amen.\"" id a08_comn_01_9f8d5669

    "Hina crossed herself."

    show rin 1 lg school i with dict_dissolve_25

    voice "2RI_0440"
    rin "\"That was sloppy! And we don't cross ourselves at Seiyou.\"" id a08_comn_01_c8e85eb0

    show hina 1 lg school k with dict_dissolve_25

    voice "2HI_0406"
    hina "\"Huh? We don't?\"" id a08_comn_01_3a04a3c8

    show rin 2 lg school c with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "2RI_0441"
    rin "\"Haahh... I feel bad for the angel who has to take this for just one meatball.\"" id a08_comn_01_996a608d

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school f with dict_dissolve_25

    voice "2HI_0407"
    hina "\"It was the best thing in my lunch today. It's the thought that counts!\"" id a08_comn_01_9fdafbc6

    $ side_image = "miyako 1 side school_a c"

    voice "2MI_0297"
    miyako "\"Ahaha, I'm sure an angel is watching.\"" id a08_comn_01_5442b7aa

    "It's convincing coming from her."

    "But they only watch. Angels can't interfere. Offerings won't have any effect."

    "Even if you sacrificed a whole lamb."

    show hina:
        "hina 1 lg school p" with Dissolve(0.25)
        ShakeYes2

    voice "2HI_0408"
    hina "\"Nom, nom. Now I've got it in the bag.\"" id a08_comn_01_62226637

    show hina 1 lg school p:
        xoffset 0 yoffset 0
    with None

    "Hina came back after tossing the meatball in her mouth."

    show rin 2 lg school a with dict_dissolve_25

    voice "2RI_0442"
    rin "\"So you ate it yourself in the end.\"" id a08_comn_01_33da3897

    show hina 1 lg school k with dict_dissolve_25

    voice "2HI_0409"
    hina "\"Well, it'd be a waste not to. You eat the offerings you leave at Buddhist altars too, right?\"" id a08_comn_01_7d3f9dd8

    show rin 2 lg school c with dict_dissolve_25

    voice "2RI_0443"
    rin "\"You're ridiculous.\"" id a08_comn_01_f28466b9

    hide rin
    hide hina
    with dict_dissolve_50

    "Fumi turned to Miyako while Hina and Rin were going at it."

    show fumi 2 lg school b at pos_l
    show miyako 1 lg school_a b at pos_r
    with dict_dissolve_25

    voice "2FU_0393RE"
    fumi "\"There are a lot of angel sightings at Seiyou, and most of them happen in this chapel.\"" id a08_comn_01_0afb7eaf

    show miyako 2 lg school c with dict_dissolve_25

    voice "2MI_0298"
    miyako "\"Is that right? I've never seen one.\"" id a08_comn_01_c4c96246

    show fumi 1 lg school c with dict_dissolve_25

    voice "2FU_0394"
    fumi "\"Ahaha, neither have I. But there's still time before graduation! It could still happen!\"" id a08_comn_01_5c99be2a

    "An oblivious exchange."

    "Miyako had obviously met other angels, just never in this chapel."

    hide fumi
    hide miyako
    with Dissolve(0.25)

    show hina 2 lg school d at pos_l
    show rin 2 lg school a at pos_r
    with dict_dissolve_25

    voice "2RI_0444"
    rin "\"If they show up in this chapel a lot, you should just put a camera in here.\"" id a08_comn_01_bd50c30e

    "Like they're cryptids or something..."

    show rin 2 lg school g with dict_dissolve_25

    voice "2RI_0445"
    rin "\"Your dad must have a camera like that, right, Hina?\"" id a08_comn_01_1e87c9a7

    voice "2HI_0410"
    hina "\"......\"" id a08_comn_01_c7cad6b9

    show rin 2 lg school a with dict_dissolve_25

    voice "2RI_0446"
    rin "\"Hina?\"" id a08_comn_01_9fd0eb75

    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_0411"
    hina "\"My sister went here...\"" id a08_comn_01_c099e344

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_0447"
    rin "\"Oh, the one with the huge boobs?\"" id a08_comn_01_a1adca31

    show hina 1 lg school j with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "2HI_0412"
    hina "\"...Ugh.\"" id a08_comn_01_f4a172fa

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 1 side school d"

    voice "2FU_0395"
    fumi "\"Your mother also went to Seiyou, right?\"" id a08_comn_01_b75a3101

    show rin 1 lg school f with dict_dissolve_25

    voice "2RI_0448"
    rin "\"Oh, the one with the huge boobs!\"" id a08_comn_01_8fd0925f

    show hina:
        "hina 1 lg school g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0413"
    hina "\"Gah, shut up about their boobs!\"" id a08_comn_01_743aa70f

    show hina 1 lg school g:
        xoffset 0 yoffset 0
    with None

    "When they'd slept over at Hina's house, they'd met her mother and sister, who were considerably more well-endowed than Hina."

    "This had greatly amused Rin, who hadn't missed an opportunity since to bring it up and ruin Hina's mood."

    show rin 1 lg school i with dict_dissolve_25

    voice "2RI_0449"
    rin "\"How did only Hina end up like this... a mutation?\"" id a08_comn_01_f692c4c9

    show hina:
        "hina 1 lg school f" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0414"
    hina "\"Gaaah!\"" id a08_comn_01_4b0faa95

    show hina 1 lg school f with None
    hide rin
    hide hina
    with dict_dissolve_25

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    "Hina leapt at her."

    camera
    with None

    $ side_image = "fumi 1 side school d"

    voice "2FU_0396RE"
    fumi "\"Now, now...\"" id a08_comn_01_08f587d4

    "The huge boobs attempted to mediate."

    show rin:
        "rin 1 lg school f flat"
        alpha 0.0 xcenter 772 ycenter 1116
        easein 0.5 alpha 1.0 ycenter 1016

    voice "2RI_0450"
    rin "\"Please, continue!\"" id a08_comn_01_8a18bb82

    show rin 1 lg school f:
        alpha 1.0 xcenter 772 ycenter 1016
    with None

    show hina:
        "hina 1 lg school f flat"
        alpha 0.0 xcenter 252 ycenter 1081
        easein 0.5 alpha 1.0 ycenter 981

    voice "2HI_0415"
    hina "\"You don't need to hear it!\"" id a08_comn_01_a080902f

    show hina 1 lg school f:
        alpha 1.0 xcenter 252 ycenter 981
    with None

    $ side_image = "miyako 1 side school_b e"

    voice "2MI_0299"
    miyako "\"I'd really like to hear it.\"" id a08_comn_01_db04ce9c

    show rin 1 lg school d with dict_dissolve_25

    voice "2RI_0451"
    rin "\"And I—\"" id a08_comn_01_fbaec3c7

    $ side_image = "fumi 1 side school g"

    voice "2FU_0397"
    fumi "\"No.\"" id a08_comn_01_0bef74ee

    "Fumi stopped Rin from making another comment."

    show hina:
        "hina 1 lg school n" with Dissolve(0.25)
        ShakeTameiki
        0.9
        "hina 1 lg school e" with Dissolve(0.25)

    voice "2HI_0416"
    hina "\"Haah... Well, my sister's friend's friend saw an angel in this chapel.\"" id a08_comn_01_08ba3d49

    show hina 1 lg school e:
        xoffset 0 yoffset 0
    with None

    $ side_image = "fumi 2 side school i"

    voice "2FU_0398"
    fumi "\"Waaah!!\"" id a08_comn_01_ace55896

    "Naturally, Fumi was very excited to hear this."

    $ side_image = "miyako 2 side school a"

    voice "2MI_0300"
    miyako "\"When was that?\"" id a08_comn_01_7fd58746

    show hina 2 lg school e
    show rin 1 lg school b
    with dict_dissolve_25

    voice "2HI_0417"
    hina "\"Hmm, my sister's six years older than me, and it was in her second year, so... five years ago, I guess.\"" id a08_comn_01_532fc406

    $ side_image = "miyako 1 side school_a i"

    voice "2MI_0301"
    miyako "\"Then it wasn't me.\"" id a08_comn_01_2f9ae2e3

    $ side_image = "fumi 2 side school c"

    voice "2FU_0399"
    fumi "\"So?\"" id a08_comn_01_b31e0cde

    show hina 2 lg school d with dict_dissolve_25

    voice "2HI_0418"
    hina "\"That girl had a friend in the hospital, and she was here praying for her recovery. And that's when the angel showed up.\"" id a08_comn_01_92dd2745

    $ side_image = "fumi 2 side school i"

    voice "2FU_0400"
    fumi "\"Oh, wow!\"" id a08_comn_01_12241254

    show hina 1 lg school k with dict_dissolve_25

    voice "2HI_0419"
    hina "\"But my sister didn't believe it when she heard. She said it was just that girl's imagination.\"" id a08_comn_01_5cdefd34

    show rin 1 lg school h with dict_dissolve_25

    voice "2RI_0452"
    rin "\"If you ask me, it's already pretty suspicious when it's coming from a friend of a friend.\"" id a08_comn_01_7e9eef6d

    $ side_image = "fumi 1 side school h"

    voice "2FU_0401"
    fumi "\"Ugh...\"" id a08_comn_01_ec6e297c

    show hina 1 lg school m with dict_dissolve_25

    voice "2HI_0420"
    hina "\"True. But it was a rumor throughout the whole class at the time.\"" id a08_comn_01_7f50eed3

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_0453"
    rin "\"Couldn't it have been a ghost she saw instead of an angel?\"" id a08_comn_01_9b0d3be5

    show hina 1 lg school d with dict_dissolve_25

    voice "2HI_0421"
    hina "\"Don't say things like that~\"" id a08_comn_01_f40b1626

    "She wasn't fond of ghosts."

    show rin 1 lg school f with dict_dissolve_25

    voice "2RI_0454"
    rin "\"In this very chapel...\"" id a08_comn_01_274b819d

    show hina:
        "hina 1 lg school g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "2HI_0422"
    hina "\"Stop it!\"" id a08_comn_01_5379505d

    show hina 1 lg school g:
        xoffset 0 yoffset 0
    with None

    stop music fadeout 1.0
    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg06aa
    show bg_obi
    with bg_effect_05

    play sound se030a

    pause 1.0

    play music bgm02 fadein 1.0

    "The bell rang and the four of them started cleaning up their lunches."

    $ side_image = "miyako 1 side school_a e"

    voice "2MI_0302"
    miyako "\"What happened to the friend in the hospital, anyway?\"" id a08_comn_01_6e94604c

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_0423"
    hina "\"Ah, she passed away right after that, I guess. I heard her name from my sister... what was it, again?\"" id a08_comn_01_3ddfb09f

    $ side_image = "miyako 2 side school b"

    voice "2MI_0303"
    miyako "\"Is that so...\"" id a08_comn_01_f9925bad

    $ side_image = "rin 2 side school a"

    voice "2RI_0455B"
    rin "\"Fabricated true stories always have little details like that, don't they?\"" id a08_comn_01_af728e47

    $ side_image = "fumi 2 side school d"

    voice "2FU_0402"
    fumi "\"I believe!\"" id a08_comn_01_2e98c6af

    $ side_image = "rin 2 side school e"

    voice "2RI_0456"
    rin "\"But if she passed away, doesn't that mean praying didn't do anything? Asking the angel was—\"" id a08_comn_01_00a7454f

    show hina 1 lg school g with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "2HI_0424"
    hina "\"Hey, don't jinx my proficiency tests.\"" id a08_comn_01_0cd7c050

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "fumi 1 side school d"

    voice "2FU_0403"
    fumi "\"Ahaha. Let's make sure we study, too.\"" id a08_comn_01_28f05e95

    $ side_image = "rin 1 side school k"

    voice "2RI_0457"
    rin "\"Yeah, yeah. The bell's gonna ring~\"" id a08_comn_01_3856b83f

    hide bg_obi
    hide hina
    with dict_dissolve_50

    "The four of them headed out of the chapel."

    pause 0.25

    show miyako 2 sm school d with Dissolve(0.5)
    pause 0.5

    voice "2MI_0304"
    miyako "\"I'm sorry.\"" id a08_comn_01_93fe7d5a

    $ side_image = "fumi 2 side school h"

    voice "2FU_0404"
    fumi "\"?\"" id a08_comn_01_8c898e44

    "—It's not your fault."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a08_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
