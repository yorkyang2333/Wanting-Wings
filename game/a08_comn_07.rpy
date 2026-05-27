label a08_comn_07:

    if route2 == 1:
        scene bg01cg with Dissolve(0.5)
    else:
        scene bg01ch with Dissolve(0.5)
    pause 1.5

    play music bgm01

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0369"
    miyako "\"I'm back.\"" id a08_comn_07_dfb9bede

    "Hina and Fumi were in the living room. Was Rin brushing her teeth?"

    show miyako:
        "miyako 2 lg pyjama c flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    $ side_image = "fumi 1 side pyjama a"

    voice "2FU_0442"
    fumi "\"Welcome back. You didn't catch a chill, did you?\"" id a08_comn_07_be586d2f

    show miyako 2 lg pyjama c:
        alpha 1.0 xcenter 512
    with None
    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0370"
    miyako "\"I'm alright. Sachiko said the same thing and made me come back.\"" id a08_comn_07_c8bd14b0

    $ side_image = "fumi 2 side pyjama b"

    voice "2FU_0443"
    fumi "\"You go to Sachiko's room every night, huh?\"" id a08_comn_07_d18a061c

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0371"
    miyako "\"Yes. I give her a report every day.\"" id a08_comn_07_67eff6ba

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0495"
    hina "\"Is there stuff to say every day?\"" id a08_comn_07_1a5bc8e6

    "So says the girl who doesn't keep a diary."

    show miyako 1 lg pyjama_a d with dict_dissolve_25

    voice "2MI_0372"
    miyako "\"There is! I never get to say everything that I want to.\"" id a08_comn_07_d7a17500

    $ side_image = "fumi 2 side pyjama i"

    voice "2FU_0444"
    fumi "\"I understand!\"" id a08_comn_07_10b60811

    "Says the one who does keep a diary."

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_0496"
    hina "\"Snff... Was she smoking?\"" id a08_comn_07_06e89aa5

    "Hina sniffed. It's impressive that she can tell from there."

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0373"
    miyako "\"Oh, I'm sorry. I'll use the spray.\"" id a08_comn_07_9b131e83

    show miyako:
        "miyako 1 lg pyjama_a g flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612

    "Miyako went over to the entrance to get a deodorizer."

    hide miyako with None
    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0497"
    hina "\"It's not your fault, Miyako. It's 'cause she's a bad adult who smokes in a student dorm.\"" id a08_comn_07_b676ad9d

    $ side_image = "miyako 2 side pyjama c"

    voice "2MI_0374"
    miyako "\"She just couldn't use the roof today because of the snow.\"" id a08_comn_07_869cac2a

    $ side_image = "fumi 1 side pyjama c"

    voice "2FU_0445"
    fumi "\"Heh.\"" id a08_comn_07_6dc51bbf

    $ side_image = "hina 1 side pyjama_pjm e"

    voice "2HI_0498"
    hina "\"If she ever tries to get you to smoke, you've gotta say no, okay?!\"" id a08_comn_07_f6df2445

    show miyako:
        "miyako 2 lg pyjama c flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    voice "2MI_0375"
    miyako "\"I will. It's okay, though. She said if she did that, you'd dropkick her.\"" id a08_comn_07_1a1204ed

    show miyako 2 lg pyjama c:
        alpha 1.0 xcenter 512
    with None
    $ side_image = "hina 1 side pyjama_pjm p"

    voice "2HI_0499"
    hina "\"So she's not a total idiot.\"" id a08_comn_07_295406b4

    "The three girls' laughter echoed through the room."

    play sound se521
    pause 1.0

    show miyako:
        xcenter 512
        easein 0.5 xcenter 252
    pause 0.5

    show rin:
        "rin 2 lg pyjama glasses g flat"
        alpha 0.0 xcenter 832
        easein 1.0 alpha 1.0 xcenter 732

    voice "2RI_0525"
    rin "\"What's going on? Hina dropkicked Sachiko?\"" id a08_comn_07_dd390105

    show rin 2 lg pyjama glasses g:
        alpha 1.0 xcenter 732
    with None

    "That's when Rin got back."

    $ side_image = "hina 1 side pyjama_pjm e"

    voice "2HI_0500"
    hina "\"Not yet.\"" id a08_comn_07_bb448514

    $ side_image = "fumi 1 side pyjama a"

    voice "2FU_0446"
    fumi "\"But she will if Sachiko tries to get Miyako to smoke.\"" id a08_comn_07_874c7877

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0376"
    miyako "\"She hasn't, though.\"" id a08_comn_07_0f81e436

    show rin 1 lg pyjama glasses k with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "2RI_0526"
    rin "\"I get it...\"" id a08_comn_07_2aeb4c18

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin looked disappointed."

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0501"
    hina "\"I don't kick people for no reason!\"" id a08_comn_07_fbc103d3

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0527"
    rin "\"What? You kick me all the time.\"" id a08_comn_07_ce050c30

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0502"
    hina "\"Because. I. Have. Reason. To!\"" id a08_comn_07_153fa6c5

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0528"
    rin "\"Like blowing off steam?\"" id a08_comn_07_f6d21bf7

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0503"
    hina "\"Am I some kind of thug?!\"" id a08_comn_07_0bbcb393

    show rin 2 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0529"
    rin "\"Be careful, Mikoyan. Piss off the RA and you'll get a roundhouse kick.\"" id a08_comn_07_acdc0706

    show miyako 1 lg pyjama_a c with dict_dissolve_25

    voice "2MI_0377"
    miyako "\"Okay, got it.\"" id a08_comn_07_e8e3abd3

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0504"
    hina "\"I'm not a tyrant! And that's a different kind of kick!\"" id a08_comn_07_9e485f85

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "2RI_0530"
    rin "\"She rules by violence. Her reign of terror's scary, huh, Mikoyan?\"" id a08_comn_07_eb094a9e

    $ side_image = "hina 1 side pyjama_pjm j"

    voice "2HI_0505"
    hina "\"Fine, if you want me to kick you so bad, I will!\"" id a08_comn_07_43839dce

    $ side_image = "fumi 1 side pyjama c"

    voice "2FU_0447"
    fumi "\"Ahahaha.\"" id a08_comn_07_232ea04d

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0531"
    rin "\"Have you gotten used to living here, Mikoyan?\"" id a08_comn_07_c1fac0b7

    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0506"
    hina "\"Ah, hey!\"" id a08_comn_07_e9c9f57b

    show miyako 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0378"
    miyako "\"Yes, thanks to all of you.\"" id a08_comn_07_c68d5c38

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0532"
    rin "\"Communal living's pretty rough. You gotta always keep the people you're living with in mind.\"" id a08_comn_07_da15e3df

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0533"
    rin "\"But I don't want it to be like that here. Go ahead and ask us if there's anything you need. Since our RA is prone to violence, you know.\"" id a08_comn_07_542a6aa9

    show miyako 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0379"
    miyako "\"Rin.\"" id a08_comn_07_8e11053a

    $ side_image = "hina 1 side pyjama_pjm c"

    voice "2HI_0507"
    hina "\"Pfft.\"" id a08_comn_07_993ffaf4

    "But instead of dropkicking her, Hina just burst out laughing."

    $ side_image = "fumi 1 side pyjama c"

    voice "2FU_0448"
    fumi "\"Heheh.\"" id a08_comn_07_d65d059b

    "Fumi laughed along with her."

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0380"
    miyako "\"?\"" id a08_comn_07_e6f4054e

    "Miyako could only stare blankly at the two of them."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0534"
    rin "\"What? You're kinda freaking me out.\"" id a08_comn_07_dc54c90c

    hide miyako
    with Dissolve(0.25)

    show hina lg 1 pyjama_pjm p at pos_l with dict_dissolve_25

    voice "2HI_0508"
    hina "\"I just think it's heartwarming how you've grown.\"" id a08_comn_07_88ee3c49

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0381"
    miyako "\"Grown?\"" id a08_comn_07_efec0421

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0535"
    rin "\"What? I've always been like this.\"" id a08_comn_07_b7847e08

    $ side_image = "fumi 1 side pyjama i"

    voice "2FU_0449"
    fumi "\"Always...\"" id a08_comn_07_f9732690

    "She was trying not to laugh."

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0536"
    rin "\"You too?!\"" id a08_comn_07_4ba036dd

    $ side_image = "miyako 1 side pyjama_a e"

    voice "2MI_0382"
    miyako "\"Is this a secret only Hina and Fumi know?\"" id a08_comn_07_265af127

    show hina 2 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0509"
    hina "\"No, it's not a secret. It's just, Rin was pretty bad when she first moved in.\"" id a08_comn_07_1834b443

    "Fumi was still giggling."

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0537"
    rin "\"Ah!!\"" id a08_comn_07_7f207a92

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin paled, catching on."

    $ side_image = "miyako 1 side pyjama_a g"

    voice "2MI_0383"
    miyako "\"Bad?\"" id a08_comn_07_c632e7d8

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0538"
    rin "\"H-Hey, w-we don't have to talk about this anymore.\"" id a08_comn_07_b30db54a

    show hina 1 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0510"
    hina "\"We haven't even started talking about it.\"" id a08_comn_07_6688a63a

    show rin 1 lg pyjama glasses j with dict_dissolve_25

    voice "2RI_0539"
    rin "\"Then we don't need to start!\"" id a08_comn_07_5c66df2e

    show hina 2 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0511"
    hina "\"There are no secrets between roommates. So, Miyako—\"" id a08_comn_07_8481bb36

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0384"
    miyako "\"Yes?\"" id a08_comn_07_0bf86d0e

    "Miyako leaned forward."

    hide rin
    show expression "rin_1_160_[rin_pyjama]_glasses_j":
        xcenter 552 ycenter 1869
        function LayerShake(50,50,1.0)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_0540"
    rin "\"Stooop!\"" id a08_comn_07_61499836

    show expression "rin_1_160_[rin_pyjama]_glasses_j":
        xcenter 552 ycenter 1869 xoffset 0 yoffset 0
    with None

    stop music fadeout 1.0

    scene white with bg_effect_21
    pause 1.5

    "—Last April. Move-in day."

    pause 0.5

    scene bg05aa
    show bg_ef_01 zorder 2
    with bg_effect_21
    pause 1.0

    play music bgm06

    show fumi 2 sm school c at pos_ls
    show hina 2 sm school a at pos_rs
    with dict_dissolve_25

    voice "2HI_0512"
    hina "\"Nice to meet you. I'm Hina Natsume.\"" id a08_comn_07_04b6a769

    voice "2FU_0450"
    fumi "\"It's nice to meet you. My name is Fumi Asou.\"" id a08_comn_07_82135f31

    "The two bowed meekly to each other in front of the door."

    show hina 2 sm school a with dict_dissolve_25

    voice "2HI_0513"
    hina "\"I'm kind of nervous. This is my first time living in a dorm.\"" id a08_comn_07_0899de62

    show fumi 2 sm school b with dict_dissolve_25

    voice "2FU_0451"
    if persistent.dpatch:
        fumi "\"Me too. So, why did you pick this school, Natsume?\"" id a08_comn_07_df386d37
    else:
        fumi "\"Me too. So, why did you pick this academy, Natsume?\"" id a08_comn_07_9dc90605

    show hina 2 sm school b with dict_dissolve_25

    voice "2HI_0514"
    hina "\"Well... My mom and my sister went here. What about you, Asou?\"" id a08_comn_07_1fe083b0

    show fumi 2 sm school i with dict_dissolve_25

    voice "2FU_0452"
    fumi "\"The uniforms are just so cute. I've always wanted to wear one every time I saw them, ever since I was little.\"" id a08_comn_07_3eaba2b5

    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_0515"
    hina "\"Every time you saw them?\"" id a08_comn_07_73a76114

    show fumi 2 sm school c with dict_dissolve_25

    voice "2FU_0453"
    if persistent.dpatch:
        fumi "\"I actually live really close to the school. I'm not even far enough to take the train.\"" id a08_comn_07_3744f1fa
    else:
        fumi "\"I actually live really close to the campus. I'm not even far enough to take the train.\"" id a08_comn_07_29ba7408

    show hina 1 sm school a with dict_dissolve_25

    voice "2HI_0516"
    hina "\"That's pretty close. You could probably commute from there.\"" id a08_comn_07_d21887c2

    show fumi 1 sm school i with dict_dissolve_25

    voice "2FU_0454"
    fumi "\"Yes, but I wanted to live in a dorm. I'm not very responsible, so I was hoping to fix that.\"" id a08_comn_07_b5669991

    show hina 1 sm school k with dict_dissolve_25

    voice "2HI_0517"
    hina "\"Well, you look responsible.\"" id a08_comn_07_c835081f

    show fumi 1 sm school d with dict_dissolve_25

    voice "2FU_0455"
    fumi "\"I hope you'll still think that when we're living together.\"" id a08_comn_07_cfac9779

    show hina 1 sm school c with dict_dissolve_25

    voice "2HI_0518"
    hina "\"Ahahaha. I hope so too.\"" id a08_comn_07_b9b4e6d3

    show fumi 2 sm school i with dict_dissolve_25

    voice "2FU_0456"
    fumi "\"Heheh. I'll do my best.\"" id a08_comn_07_258f9482

    show hina 1 sm school b with dict_dissolve_25

    voice "2HI_0519"
    hina "\"I'm glad you're easy to talk to.\"" id a08_comn_07_a0668896

    show fumi 2 sm school b with dict_dissolve_25

    voice "2FU_0457"
    fumi "\"I feel the same way.\"" id a08_comn_07_f2ea2943

    show hina 2 sm school a with Dissolve(0.25)
    show hina:
        ShakeYes

    voice "2HI_0520"
    hina "\"I'm looking forward to the next three years.\"" id a08_comn_07_3f34ac23

    show hina:
        xoffset 0 yoffset 0
    with None
    show fumi 2 sm school i with Dissolve(0.25)
    show fumi:
        ShakeYes

    voice "2FU_0458"
    fumi "\"I am, too.\"" id a08_comn_07_de16bd7a

    show fumi:
        xoffset 0 yoffset 0
    with None

    "They shook hands."

    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_0521"
    hina "\"Come to think of it, it's a three-person room, right?\"" id a08_comn_07_c8be024f

    show fumi 2 sm school g with dict_dissolve_25

    voice "2FU_0459"
    fumi "\"Yes, that's what I've heard.\"" id a08_comn_07_4ffc383a

    $ side_image = "rin 1 side school i"

    voice "2RI_0541"
    rin "\"I didn't hear that!\"" id a08_comn_07_622cbce7

    show fumi 1 sm school e
    show hina 1 sm school k
    with dict_dissolve_25

    "Hina and Fumi turned toward the door at the voice."

    hide fumi
    hide hina
    with Dissolve(0.5)

    pause 0.5

    show sachiko 2 sm outfit c at pos_ls
    show rin 1 sm school i at pos_rs
    with dict_dissolve_25

    voice "2SA_0212"
    sachiko "\"That's strange. They should have sent paperwork to your parents.\"" id a08_comn_07_b01b7136

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_0542"
    rin "\"...That paperwork's probably in Europe right now.\"" id a08_comn_07_f16669c3

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0213"
    sachiko "\"Huh... Well, you'll be in a three-person room, Ogata.\"" id a08_comn_07_a0d42679

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_0543"
    rin "\"I'm telling you, that's not gonna work for me.\"" id a08_comn_07_35d97e1c

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0214"
    sachiko "\"Well, I dunno what to tell you. It's not like we even have singles~\"" id a08_comn_07_71758f24

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_0544"
    rin "\"I can't live with people I don't know...\"" id a08_comn_07_d7eebf50

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0215"
    sachiko "\"Oh, are you two Natsume and Asou?\"" id a08_comn_07_dadc0073

    "Sachiko found Hina and Fumi standing in front of the room."

    $ side_image = "side/hina_fumi_school_sozai01.webp"

    $ voice2("hina","2HI_0522","fumi","2FU_0460")
    hina_fumi "\"Yes.\""

    voice "2SA_0216"
    sachiko "\"Great. I'll introduce you to your third roommate. This is Rin Ogata.\"" id a08_comn_07_bab170b5

    $ side_image = "hina 1 side school p"

    voice "2HI_0523"
    hina "\"Nice to meet you, Ogata. I'm Hina Natsume.\"" id a08_comn_07_48fdf700

    $ side_image = "fumi 1 side school c"

    voice "2FU_0461"
    fumi "\"Fumi Asou. It's nice to meet you.\"" id a08_comn_07_d6cad1f4

    show rin 1 sm school i with Dissolve(0.25)
    show rin:
        yoffset 0
        ease 0.25 yoffset 2
        ease 0.25 yoffset 0

    voice "2RI_0545"
    rin "\"......\"" id a08_comn_07_2a10bff5

    "Rin bowed to them so slightly it was almost imperceptible."

    show sachiko 2 sm outfit d with dict_dissolve_25

    voice "2SA_0217"
    sachiko "\"Hmm~\"" id a08_comn_07_b3f3450a

    "Sachiko scratched her temple."

    $ side_image = "hina 1 side school k"

    voice "2HI_0524"
    hina "\"What's wrong?\"" id a08_comn_07_9d69d1c5

    show sachiko 2 sm outfit f with dict_dissolve_25

    voice "2SA_0218"
    sachiko "\"Guess she didn't know it was a triple room... She's a little miffed about it.\"" id a08_comn_07_b83152c3

    $ side_image = "hina 1 side school k"

    voice "2HI_0525"
    hina "\"Are there no other rooms?\"" id a08_comn_07_886f01be

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "2SA_0219"
    sachiko "\"Nope. All the dorms are full this year.\"" id a08_comn_07_21849542

    hide sachiko with Dissolve(0.25)

    show fumi 2 sm school b:
        xcenter 192
    show hina 1 sm school a:
        xcenter 402
    with dict_dissolve_25

    voice "2HI_0526"
    hina "\"Well, I guess you're stuck with us, Ogata.\"" id a08_comn_07_35469246

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_0546"
    rin "\"......\"" id a08_comn_07_f0f18c22

    show hina 1 sm school n with dict_dissolve_25

    voice "2HI_0527"
    hina "\"Communal living's pretty rough. You gotta always keep the people you're living with in mind.\"" id a08_comn_07_ec26360c

    show hina 1 sm school p with dict_dissolve_25

    voice "2HI_0528"
    hina "\"But I don't want it to be like that here. You can ask us if there's anything you need.\"" id a08_comn_07_bc2990b6

    "Hina said, holding her hand out."

    show fumi:
        "fumi 2 sm school i" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0462"
    fumi "\"Yes, think of it as an opportunity.\"" id a08_comn_07_3729753b

    show fumi 2 sm school i:
        xoffset 0 yoffset 0
    with None

    "Fumi nodded at Hina's words and held her hand out too."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0220"
    sachiko "\"See, they're good girls.\"" id a08_comn_07_fc8170a8

    show rin 1 sm school h with dict_dissolve_25

    voice "2RI_0547RE"
    rin "\"...I'm not really great in groups.\"" id a08_comn_07_e76f3652

    show rin:
        "rin 1 sm school h flat"
        alpha 1.0 xcenter 732
        easeout 0.5 alpha 0.0 xcenter 632
    pause 0.5
    hide rin with None

    play sound se521
    pause 0.5

    "Rin averted her eyes and went past them into the room without shaking their hands."

    show fumi 2 sm school h
    show hina 1 sm school k
    with dict_dissolve_25

    $ voice2("hina","2HI_0529","fumi","2FU_0463")
    hina_fumi "\".........\""

    "Hina and Fumi exchanged a look."

    scene white with bg_effect_21
    pause 1.5

    if route2 == 1:
        scene bg01cg with bg_effect_21
    else:
        scene bg01ch with bg_effect_21
    pause 0.5

    show expression "rin_1_160_[rin_pyjama]_glasses_j" as rin_1:
        xcenter 552 ycenter 1869
        function LayerShake(50,50,1.0)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_0548"
    rin "\"Gyaaaaaaa!!\"" id a08_comn_07_6a0e148f

    show expression "rin_1_160_[rin_pyjama]_glasses_j" as rin_1:
        xcenter 552 ycenter 1869 xoffset 0 yoffset 0
    with None

    "Rin screamed in embarrassment. There was too much she could think of."

    hide rin_1 with Dissolve(0.25)

    show hina 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0530"
    hina "\"I'm not really great in groups.\"" id a08_comn_07_deeac992

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0549"
    rin "\"Eek!\"" id a08_comn_07_dbb02f24

    show hina 2 lg pyjama_pjm g with dict_dissolve_25

    voice "2HI_0531"
    hina "\"I'm not really great in groups.\"" id a08_comn_07_4ca20167

    "Rin clutched her head and writhed on the floor as Fumi and Miyako laughed. Then Hina twisted the knife."

    $ side_image = "rin 1 side pyjama glasses j"

    voice "2RI_0550"
    rin "\"Kill me! Just kill me!\"" id a08_comn_07_3a46a5eb

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a08_cou1_02
    elif route2 == 2:
        jump a08_cou2_02
    elif route2 == 3:
        jump a08_cou3_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
