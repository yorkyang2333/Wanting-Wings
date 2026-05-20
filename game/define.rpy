


define hina = Character(_("Hina"),image="hina",voice_tag="hina")
define rin = Character(_("Rin"),image="rin",voice_tag="rin")
define fumi = Character(_("Fumi"),image="fumi",voice_tag="fumi")
define sachiko = Character(_("Sachiko"),image="sachiko",voice_tag="sachiko")
define miyako = Character(_("Miyako"),image="miyako",voice_tag="miyako")
define etc = Character("etc",voice_tag="etc")
define pa_system = Character(_("PA System"),voice_tag="etc")
define hina_fumi = Character(_("Hina & Fumi"))
define hina_rin = Character(_("Hina & Rin"))
define rin_fumi = Character(_("Fumi & Rin"))
define rin_sachiko = Character(_("Rin & Sachiko"))
define rin_miyako = Character(_("Rin & Miyako"))
define hina_rin_fumi = Character(_("Hina & Rin & Fumi"))
define hina_fumi_sachiko = Character(_("Hina & Fumi & Sachiko"))
define hina_sachiko = Character(_("Hina & Sachiko"))
define fumi_miyako = Character(_("Fumi & Miyako"))
define miyako_sachiko = Character(_("Miyako & Sachiko"))
define hina_rin_fumi_sachiko = Character(_("All{#hina_rin_fumi_sachiko}"))
define hina_rin_fumi_miyako = Character(_("All{#hina_rin_fumi_miyako}"))
define hina_rin_fumi_miyako_sachiko = Character(_("All{#hina_rin_fumi_miyako_sachiko}"))
define namahage_sachiko = Character(_("Namahage"),voice_tag="sachiko")
define namahage_miyako = Character(_("Namahage"),voice_tag="miyako")
define fumi_father = Character(_("Fumi's Father"))
define arthur = Character(_("Arthur"),voice_tag="etc")
define noel = Character(_("Noel"),voice_tag="miyako")

layeredimage fumi 1:

    image_format "images/fumi/{image}.webp"


    always "fumi_1_school" if_any "school_scarf"
    always "fumi_1_pyjama" if_any "pyjama_scarf"


    group body multiple:
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama
        attribute pyjama_scarf
        attribute casual


    group face auto


    always "fumi_1_casual_face_fix_e" if_all ["casual","e"]
    always "fumi_1_casual_face_fix_f" if_all ["casual","f"]
    always "fumi_1_casual_face_fix_j" if_all ["casual","j"]


image fumi 1 lg = LayeredImageProxy("fumi 1",transform=Transform(zoom=0.8,ycenter=1021))

image fumi z3 1 lg = LayeredImageProxy("fumi 1",transform=Transform(zoom=0.77,ycenter=999))

image fumi z4 1 lg = LayeredImageProxy("fumi 1",transform=Transform(zoom=0.565,ycenter=762))

layeredimage fumi 1 sm:

    image_format "images/fumi/{image}.webp"
    ycenter 631


    always "fumi_1_sm_school" if_any "school_scarf"
    always "fumi_1_sm_pyjama" if_any "pyjama_scarf"


    group body multiple:
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama
        attribute pyjama_scarf
        attribute casual


    group face auto


    always "fumi_1_sm_casual_face_fix_e" if_all ["casual","e"]
    always "fumi_1_sm_casual_face_fix_f" if_all ["casual","f"]
    always "fumi_1_sm_casual_face_fix_j" if_all ["casual","j"]

layeredimage fumi 1 side:

    image_format "images/fumi/side/{image}.webp"

    pos (540,315)


    always "fumi_1_side_school" if_any "school_scarf"
    always "fumi_1_side_pyjama" if_any "pyjama_scarf"


    group body multiple:
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama
        attribute pyjama_scarf
        attribute casual


    group face auto


    always "fumi_1_side_casual_face_fix_e" if_all ["casual","e"]
    always "fumi_1_side_casual_face_fix_f" if_all ["casual","f"]
    always "fumi_1_side_casual_face_fix_j" if_all ["casual","j"]

layeredimage fumi 2:

    image_format "images/fumi/{image}.webp"

    always "fumi_2_school" if_any "school_scarf"
    always "fumi_2_pyjama" if_any "pyjama_scarf"


    group body multiple:
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama
        attribute pyjama_scarf
        attribute casual
        attribute curtain


    group face auto

image fumi 2 lg = LayeredImageProxy("fumi 2",transform=Transform(zoom=0.8,ycenter=1021))
image fumi z3 2 lg = LayeredImageProxy("fumi 2",transform=Transform(zoom=0.77,ycenter=999))
image fumi z4 2 lg = LayeredImageProxy("fumi 2",transform=Transform(zoom=0.565,ycenter=762))

layeredimage fumi 2 sm:

    image_format "images/fumi/{image}.webp"
    ycenter 631

    always "fumi_2_sm_school" if_any "school_scarf"
    always "fumi_2_sm_pyjama" if_any "pyjama_scarf"


    group body multiple:
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama
        attribute pyjama_scarf
        attribute casual
        attribute curtain


    group face auto

    always "fumi_2_sm_casual_face_fix_f" if_all ["casual"] if_any ["f","g"]

layeredimage fumi 2 side:

    image_format "images/fumi/side/{image}.webp"

    pos (498,305)

    always "fumi_2_side_school" if_any "school_scarf"
    always "fumi_2_side_pyjama" if_any "pyjama_scarf"


    group body multiple:
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama
        attribute pyjama_scarf
        attribute casual
        attribute curtain


    group face auto

    always "fumi_2_side_casual_face_fix_f" if_all ["casual"] if_any ["f","g"]

layeredimage fumi 3 sm light:

    image_format "images/fumi/{image}.webp"
    xcenter 210
    ycenter 546

    attribute znd
    attribute pyjama

    group face auto

layeredimage fumi 3 sm nightlight:

    image_format "images/fumi/{image}.webp"
    xcenter 210
    ycenter 546

    always "fumi_3_sm_nightlight_pyjama"

    attribute pyjama

    group face auto

layeredimage fumi 3 sm dark:

    image_format "images/fumi/{image}.webp"
    xcenter 210
    ycenter 546

    attribute znd
    attribute pyjama

    group face auto

layeredimage fumi 3 lg light:

    image_format "images/fumi/{image}.webp"
    xcenter 210
    ycenter 546

    attribute znd
    attribute pyjama

    group face auto

layeredimage fumi 3 lg nightlight:

    image_format "images/fumi/{image}.webp"
    xcenter 210
    ycenter 546

    always "fumi_3_lg_nightlight_pyjama"

    attribute pyjama

    group face auto

layeredimage fumi 3 lg dark:

    image_format "images/fumi/{image}.webp"
    xcenter 210
    ycenter 546

    attribute znd
    attribute pyjama

    group face auto

layeredimage rin 1:

    image_format "images/rin/{image}.webp"

    always "rin_1_hair_down" if_any ["school","school_scarf","casual"]
    always "rin_1_school" if_any "school_scarf"
    always "rin_1_pyjama_shirt" if_any "pyjama_b"

    group body multiple:
        attribute hair_down
        attribute hair_up
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama: 
            "rin_1_[rin_pyjama]"
        attribute pyjama_noshirt
        attribute casual

    group face auto

    always "rin_1_casual_face_fix_a" if_all ["casual","a"]
    always "rin_1_casual_face_fix_b" if_all ["casual","b"]
    always "rin_1_casual_face_fix_c" if_all ["casual","c"]
    always "rin_1_casual_face_fix_d" if_all ["casual","d"]
    always "rin_1_casual_face_fix_e" if_all ["casual","e"]
    always "rin_1_casual_face_fix_f" if_all ["casual","f"]
    always "rin_1_casual_face_fix_g" if_all ["casual","g"]
    always "rin_1_casual_face_fix_h" if_all ["casual","h"]
    always "rin_1_casual_face_fix_i" if_all ["casual","i"]
    always "rin_1_casual_face_fix_j" if_all ["casual","j"]
    always "rin_1_casual_face_fix_k" if_all ["casual","k"]

    attribute glasses

image rin 1 lg = LayeredImageProxy("rin 1",transform=Transform(zoom=0.8,ycenter=1016))
image rin z3 1 lg = LayeredImageProxy("rin 1",transform=Transform(zoom=0.77,ycenter=994))
image rin z4 1 lg = LayeredImageProxy("rin 1",transform=Transform(zoom=0.565,ycenter=759))

layeredimage rin 1 sm:

    image_format "images/rin/{image}.webp"
    ycenter 631

    always "rin_1_sm_hair_down" if_any ["school","school_scarf","casual"]
    always "rin_1_sm_hair_up" if_any "pyjama"
    always "rin_1_sm_school" if_any "school_scarf"
    always "rin_1_sm_pyjama_shirt" if_any "pyjama_b"

    group body multiple:
        attribute hair_down
        attribute hair_up
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama:
            "rin_1_sm_[rin_pyjama]"
        attribute pyjama_noshirt
        attribute casual

    group face auto

    always "rin_1_sm_casual_face_fix_a" if_all ["casual","a"]
    always "rin_1_sm_casual_face_fix_b" if_all ["casual","b"]
    always "rin_1_sm_casual_face_fix_c" if_all ["casual","c"]
    always "rin_1_sm_casual_face_fix_d" if_all ["casual","d"]
    always "rin_1_sm_casual_face_fix_e" if_all ["casual","e"]
    always "rin_1_sm_casual_face_fix_f" if_all ["casual","f"]
    always "rin_1_sm_casual_face_fix_g" if_all ["casual","g"]
    always "rin_1_sm_casual_face_fix_h" if_all ["casual","h"]
    always "rin_1_sm_casual_face_fix_i" if_all ["casual","i"]
    always "rin_1_sm_casual_face_fix_j" if_all ["casual","j"]
    always "rin_1_sm_casual_face_fix_k" if_all ["casual","k"]

    attribute glasses

layeredimage rin 1 side:

    image_format "images/rin/side/{image}.webp"

    pos (545,355)

    always "rin_1_side_hair_down" if_any ["school","school_scarf","casual"]
    always "rin_1_side_school" if_any "school_scarf"
    always "rin_1_side_pyjama_shirt" if_any "pyjama_b"

    group body multiple:
        attribute hair_down
        attribute hair_up
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama:
            "rin_1_side_[rin_pyjama]"
        attribute pyjama_noshirt
        attribute casual

    group face auto

    always "rin_1_side_casual_face_fix_a" if_all ["casual","a"]
    always "rin_1_side_casual_face_fix_b" if_all ["casual","b"]
    always "rin_1_side_casual_face_fix_c" if_all ["casual","c"]
    always "rin_1_side_casual_face_fix_d" if_all ["casual","d"]
    always "rin_1_side_casual_face_fix_e" if_all ["casual","e"]
    always "rin_1_side_casual_face_fix_f" if_all ["casual","f"]
    always "rin_1_side_casual_face_fix_g" if_all ["casual","g"]
    always "rin_1_side_casual_face_fix_h" if_all ["casual","h"]
    always "rin_1_side_casual_face_fix_i" if_all ["casual","i"]
    always "rin_1_side_casual_face_fix_j" if_all ["casual","j"]
    always "rin_1_side_casual_face_fix_k" if_all ["casual","k"]

    attribute glasses


layeredimage rin 1 120 pyjama_a glasses:

    image_format "images/rin/{image}.webp"
    ycenter 1684

    always "rin_1_120_pyjama_a"

    group face auto

layeredimage rin 2:

    image_format "images/rin/{image}.webp"

    always "rin_2_hair_down" if_any ["school","school_scarf","casual"]
    always "rin_2_school" if_any "school_scarf"

    group body multiple:
        attribute hair_down
        attribute hair_up
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama:
            "rin_2_[rin_pyjama]"
        attribute casual

    group face auto

    always "rin_2_casual_face_fix_a" if_all ["casual","a"]
    always "rin_2_casual_face_fix_b" if_all ["casual","b"]
    always "rin_2_casual_face_fix_c" if_all ["casual","c"]
    always "rin_2_casual_face_fix_d" if_all ["casual","d"]
    always "rin_2_casual_face_fix_e" if_all ["casual","e"]
    always "rin_2_casual_face_fix_f" if_all ["casual","f"]
    always "rin_2_casual_face_fix_g" if_all ["casual","g"]

    attribute glasses

image rin 2 lg = LayeredImageProxy("rin 2",transform=Transform(zoom=0.8,ycenter=1016))
image rin z3 2 lg = LayeredImageProxy("rin 2",transform=Transform(zoom=0.77,ycenter=994))
image rin z4 2 lg = LayeredImageProxy("rin 2",transform=Transform(zoom=0.565,ycenter=759))

layeredimage rin 2 sm:

    image_format "images/rin/{image}.webp"
    ycenter 631

    always "rin_2_sm_hair_down" if_any ["school","school_scarf","casual"]
    always "rin_2_sm_school" if_any "school_scarf"

    group body multiple:
        attribute hair_down
        attribute hair_up
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama:
            "rin_2_sm_[rin_pyjama]"
        attribute casual

    group face auto

    always "rin_2_sm_casual_face_fix_a" if_all ["casual","a"]
    always "rin_2_sm_casual_face_fix_b" if_all ["casual","b"]
    always "rin_2_sm_casual_face_fix_c" if_all ["casual","c"]
    always "rin_2_sm_casual_face_fix_d" if_all ["casual","d"]
    always "rin_2_sm_casual_face_fix_e" if_all ["casual","e"]
    always "rin_2_sm_casual_face_fix_f" if_all ["casual","f"]
    always "rin_2_sm_casual_face_fix_g" if_all ["casual","g"]

    attribute glasses

layeredimage rin 2 side:

    image_format "images/rin/side/{image}.webp"

    pos (520,348)

    always "rin_2_side_hair_down" if_any ["school","school_scarf","casual"]
    always "rin_2_side_school" if_any "school_scarf"

    group body multiple:
        attribute hair_down
        attribute hair_up
        attribute znd
        attribute school
        attribute school_scarf
        attribute pyjama:
            "rin_2_side_[rin_pyjama]"
        attribute casual
    group face auto

    always "rin_2_side_casual_face_fix_a" if_all ["casual","a"]
    always "rin_2_side_casual_face_fix_b" if_all ["casual","b"]
    always "rin_2_side_casual_face_fix_c" if_all ["casual","c"]
    always "rin_2_side_casual_face_fix_d" if_all ["casual","d"]
    always "rin_2_side_casual_face_fix_e" if_all ["casual","e"]
    always "rin_2_side_casual_face_fix_f" if_all ["casual","f"]
    always "rin_2_side_casual_face_fix_g" if_all ["casual","g"]

    attribute glasses

layeredimage rin 3 sm light:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    attribute pyjama:
        "rin_3_sm_light_[rin_pyjama]"

    group face auto

    attribute glasses

layeredimage rin 3 sm nightlight:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    attribute pyjama:
        "rin_3_sm_nightlight_[rin_pyjama]"
    attribute pyjama_bed_b

    group face auto

layeredimage rin 3 sm dark:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    attribute znd
    attribute pyjama:
        "rin_3_sm_dark_[rin_pyjama]"

    group face auto


layeredimage rin 3 sm dark pyjama_bed_b:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    always "rin_3_sm_dark_pyjama_bed_b"

    group face auto

layeredimage rin 3 lg light:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    attribute pyjama:
        "rin_3_lg_light_[rin_pyjama]"

    group face auto

    attribute glasses


layeredimage rin 3 lg light znd:

    image_format "images/rin/{image}.webp"
    xcenter 198
    ycenter 490

    always "rin_3_lg_light_znd"
    group face auto

    attribute glasses

layeredimage rin 3 lg nightlight:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    attribute pyjama:
        "rin_3_lg_nightlight_[rin_pyjama]"

    group face auto


layeredimage rin 3 lg nightlight pyjama_bed_b:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    always "rin_3_lg_nightlight_pyjama_bed_b"

    group face auto

layeredimage rin 3 lg dark:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    attribute znd
    attribute pyjama:
        "rin_3_lg_dark_[rin_pyjama]"

    group face auto


layeredimage rin 3 lg dark pyjama_bed_b:

    image_format "images/rin/{image}.webp"
    xcenter 686
    ycenter 178

    always "rin_3_lg_dark_pyjama_bed_b"

    group face auto

layeredimage hina 1:

    image_format "images/hina/{image}.webp"

    always "hina_1_znd" if_any "znd_choker"
    always "hina_1_school" if_any ["school_scarf","school_choker"]
    always "hina_1_casual" if_any "casual_choker"
    always "hina_1_pyjama" if_any "pyjama_choker"


    if hina_choker == "_choker":
        "hina_1_pyjama" if_all ["pyjama_pjm"]

    group body multiple:
        attribute znd
        attribute znd_choker
        attribute school
        attribute school_scarf
        attribute school_choker
        attribute pyjama
        attribute pyjama_choker
        attribute pyjama_pjm:
            "hina_1_pyjama[hina_choker]"
        attribute headphones
        attribute casual
        attribute casual_choker
        attribute casual_scarf

    group face auto

    always "hina_1_casual_scarf_face_fix_a" if_all ["casual_scarf","a"]
    always "hina_1_casual_scarf_face_fix_b" if_all ["casual_scarf","b"]
    always "hina_1_casual_scarf_face_fix_c" if_all ["casual_scarf","c"]
    always "hina_1_casual_scarf_face_fix_d" if_all ["casual_scarf","d"]
    always "hina_1_casual_scarf_face_fix_e" if_all ["casual_scarf","e"]
    always "hina_1_casual_scarf_face_fix_f" if_all ["casual_scarf","f"]
    always "hina_1_casual_scarf_face_fix_g" if_all ["casual_scarf","g"]
    always "hina_1_casual_scarf_face_fix_h" if_all ["casual_scarf","h"]
    always "hina_1_casual_scarf_face_fix_i" if_all ["casual_scarf","i"]
    always "hina_1_casual_scarf_face_fix_j" if_all ["casual_scarf","j"]
    always "hina_1_casual_scarf_face_fix_k" if_all ["casual_scarf","k"]
    always "hina_1_casual_scarf_face_fix_l" if_all ["casual_scarf","l"]
    always "hina_1_casual_scarf_face_fix_m" if_all ["casual_scarf","m"]
    always "hina_1_casual_scarf_face_fix_n" if_all ["casual_scarf","n"]
    always "hina_1_casual_scarf_face_fix_o" if_all ["casual_scarf","o"]
    always "hina_1_casual_scarf_face_fix_p" if_all ["casual_scarf","p"]
    always "hina_1_casual_scarf_face_fix_q" if_all ["casual_scarf","q"]

image hina 1 lg = LayeredImageProxy("hina 1",transform=Transform(zoom=0.8,ycenter=981))
image hina z3 1 lg = LayeredImageProxy("hina 1",transform=Transform(zoom=0.77,ycenter=959))
image hina z4 1 lg = LayeredImageProxy("hina 1",transform=Transform(zoom=0.565,ycenter=730))

layeredimage hina 1 sm:

    image_format "images/hina/{image}.webp"
    ycenter 614

    always "hina_1_sm_znd" if_any "znd_choker"
    always "hina_1_sm_school" if_any ["school_scarf","school_choker"]
    always "hina_1_sm_pyjama" if_any "pyjama_choker"
    always "hina_1_sm_casual" if_any "casual_choker"


    if hina_choker == "_choker":
        "hina_1_sm_pyjama" if_all ["pyjama_pjm"]

    group body multiple:
        attribute znd
        attribute znd_choker
        attribute school
        attribute school_scarf
        attribute school_choker
        attribute pyjama
        attribute pyjama_choker
        attribute pyjama_pjm:
            "hina_1_sm_pyjama[hina_choker]"
        attribute headphones
        attribute casual
        attribute casual_choker
        attribute casual_scarf

    group face auto

    always "hina_1_sm_casual_scarf_face_fix_a" if_all ["casual_scarf","a"]
    always "hina_1_sm_casual_scarf_face_fix_b" if_all ["casual_scarf","b"]
    always "hina_1_sm_casual_scarf_face_fix_c" if_all ["casual_scarf","c"]
    always "hina_1_sm_casual_scarf_face_fix_d" if_all ["casual_scarf","d"]
    always "hina_1_sm_casual_scarf_face_fix_e" if_all ["casual_scarf","e"]
    always "hina_1_sm_casual_scarf_face_fix_f" if_all ["casual_scarf","f"]
    always "hina_1_sm_casual_scarf_face_fix_g" if_all ["casual_scarf","g"]
    always "hina_1_sm_casual_scarf_face_fix_h" if_all ["casual_scarf","h"]
    always "hina_1_sm_casual_scarf_face_fix_i" if_all ["casual_scarf","i"]
    always "hina_1_sm_casual_scarf_face_fix_j" if_all ["casual_scarf","j"]
    always "hina_1_sm_casual_scarf_face_fix_k" if_all ["casual_scarf","k"]
    always "hina_1_sm_casual_scarf_face_fix_l" if_all ["casual_scarf","l"]
    always "hina_1_sm_casual_scarf_face_fix_m" if_all ["casual_scarf","m"]
    always "hina_1_sm_casual_scarf_face_fix_n" if_all ["casual_scarf","n"]
    always "hina_1_sm_casual_scarf_face_fix_o" if_all ["casual_scarf","o"]
    always "hina_1_sm_casual_scarf_face_fix_p" if_all ["casual_scarf","p"]
    always "hina_1_sm_casual_scarf_face_fix_q" if_all ["casual_scarf","q"]


layeredimage hina 1 side:

    image_format "images/hina/side/{image}.webp"

    pos (538,271)

    always "hina_1_side_znd" if_any "znd_choker"
    always "hina_1_side_school" if_any ["school_scarf","school_choker"]
    always "hina_1_side_pyjama" if_any "pyjama_choker"
    always "hina_1_side_casual" if_any "casual_choker"


    if hina_choker == "_choker":
        "hina_1_side_pyjama" if_all ["pyjama_pjm"]

    group body multiple:
        attribute znd
        attribute znd_choker
        attribute school
        attribute school_scarf
        attribute school_choker
        attribute pyjama
        attribute pyjama_choker
        attribute pyjama_pjm:
            "hina_1_side_pyjama[hina_choker]"
        attribute headphones
        attribute casual
        attribute casual_scarf

    group face auto

    always "hina_1_side_casual_scarf_face_fix_a" if_all ["casual_scarf","a"]
    always "hina_1_side_casual_scarf_face_fix_b" if_all ["casual_scarf","b"]
    always "hina_1_side_casual_scarf_face_fix_c" if_all ["casual_scarf","c"]
    always "hina_1_side_casual_scarf_face_fix_d" if_all ["casual_scarf","d"]
    always "hina_1_side_casual_scarf_face_fix_e" if_all ["casual_scarf","e"]
    always "hina_1_side_casual_scarf_face_fix_f" if_all ["casual_scarf","f"]
    always "hina_1_side_casual_scarf_face_fix_g" if_all ["casual_scarf","g"]
    always "hina_1_side_casual_scarf_face_fix_h" if_all ["casual_scarf","h"]
    always "hina_1_side_casual_scarf_face_fix_i" if_all ["casual_scarf","i"]
    always "hina_1_side_casual_scarf_face_fix_j" if_all ["casual_scarf","j"]
    always "hina_1_side_casual_scarf_face_fix_k" if_all ["casual_scarf","k"]
    always "hina_1_side_casual_scarf_face_fix_l" if_all ["casual_scarf","l"]
    always "hina_1_side_casual_scarf_face_fix_m" if_all ["casual_scarf","m"]
    always "hina_1_side_casual_scarf_face_fix_n" if_all ["casual_scarf","n"]
    always "hina_1_side_casual_scarf_face_fix_o" if_all ["casual_scarf","o"]
    always "hina_1_side_casual_scarf_face_fix_p" if_all ["casual_scarf","p"]
    always "hina_1_side_casual_scarf_face_fix_q" if_all ["casual_scarf","q"]

layeredimage hina 2:

    image_format "images/hina/{image}.webp"

    always "hina_2_znd" if_any "znd_choker"
    always "hina_2_school" if_any ["school_scarf","school_choker"]
    always "hina_2_pyjama" if_any "pyjama_choker"
    always "hina_2_casual" if_any "casual_choker"


    if hina_choker == "_choker":
        "hina_2_pyjama" if_all ["pyjama_pjm"]

    group body multiple:
        attribute znd
        attribute znd_choker
        attribute school
        attribute school_scarf
        attribute school_choker
        attribute pyjama
        attribute pyjama_choker
        attribute pyjama_pjm:
            "hina_2_pyjama[hina_choker]"
        attribute curtain
        attribute headphones
        attribute casual
        attribute casual_choker
        attribute casual_scarf

    group face auto

    always "hina_2_casual_scarf_face_fix_a" if_all ["casual_scarf","a"]
    always "hina_2_casual_scarf_face_fix_b" if_all ["casual_scarf","b"]
    always "hina_2_casual_scarf_face_fix_c" if_all ["casual_scarf","c"]
    always "hina_2_casual_scarf_face_fix_d" if_all ["casual_scarf","d"]
    always "hina_2_casual_scarf_face_fix_e" if_all ["casual_scarf","e"]
    always "hina_2_casual_scarf_face_fix_f" if_all ["casual_scarf","f"]
    always "hina_2_casual_scarf_face_fix_g" if_all ["casual_scarf","g"]
    always "hina_2_casual_scarf_face_fix_h" if_all ["casual_scarf","h"]
    always "hina_2_casual_scarf_face_fix_i" if_all ["casual_scarf","i"]
    always "hina_2_casual_scarf_face_fix_j" if_all ["casual_scarf","j"]

image hina 2 lg = LayeredImageProxy("hina 2",transform=Transform(zoom=0.8,ycenter=981))
image hina z3 2 lg = LayeredImageProxy("hina 2",transform=Transform(zoom=0.77,ycenter=959))
image hina z4 2 lg = LayeredImageProxy("hina 2",transform=Transform(zoom=0.565,ycenter=730))

layeredimage hina 2 sm:

    image_format "images/hina/{image}.webp"
    ycenter 614

    always "hina_2_sm_znd" if_any "znd_choker"
    always "hina_2_sm_school" if_any ["school_scarf","school_choker"]
    always "hina_2_sm_pyjama" if_any "pyjama_choker"
    always "hina_2_sm_casual" if_any "casual_choker"


    if hina_choker == "_choker":
        "hina_2_sm_pyjama" if_all ["pyjama_pjm"]

    group body multiple:
        attribute znd
        attribute znd_choker
        attribute school
        attribute school_scarf
        attribute school_choker
        attribute pyjama
        attribute pyjama_choker
        attribute pyjama_pjm:
            "hina_2_sm_pyjama[hina_choker]"
        attribute curtain
        attribute headphones
        attribute casual
        attribute casual_choker
        attribute casual_scarf

    group face auto

    always "hina_2_sm_casual_scarf_face_fix_a" if_all ["casual_scarf","a"]
    always "hina_2_sm_casual_scarf_face_fix_b" if_all ["casual_scarf","b"]
    always "hina_2_sm_casual_scarf_face_fix_c" if_all ["casual_scarf","c"]
    always "hina_2_sm_casual_scarf_face_fix_d" if_all ["casual_scarf","d"]
    always "hina_2_sm_casual_scarf_face_fix_e" if_all ["casual_scarf","e"]
    always "hina_2_sm_casual_scarf_face_fix_f" if_all ["casual_scarf","f"]
    always "hina_2_sm_casual_scarf_face_fix_g" if_all ["casual_scarf","g"]
    always "hina_2_sm_casual_scarf_face_fix_h" if_all ["casual_scarf","h"]
    always "hina_2_sm_casual_scarf_face_fix_i" if_all ["casual_scarf","i"]
    always "hina_2_sm_casual_scarf_face_fix_j" if_all ["casual_scarf","j"]

layeredimage hina 2 side:

    image_format "images/hina/side/{image}.webp"

    pos (545,273)

    always "hina_2_side_znd" if_any "znd_choker"
    always "hina_2_side_school" if_any ["school_scarf","school_choker"]
    always "hina_2_side_pyjama" if_any "pyjama_choker"
    always "hina_2_side_casual" if_any "casual_choker"


    if hina_choker == "_choker":
        "hina_2_side_pyjama" if_all ["pyjama_pjm"]

    group body multiple:
        attribute znd
        attribute znd_choker
        attribute school
        attribute school_scarf
        attribute school_choker
        attribute pyjama
        attribute pyjama_choker
        attribute pyjama_pjm:
            "hina_2_side_pyjama[hina_choker]"
        attribute curtain
        attribute headphones
        attribute casual
        attribute casual_scarf

    group face auto

    always "hina_2_side_casual_scarf_face_fix_a" if_all ["casual_scarf","a"]
    always "hina_2_side_casual_scarf_face_fix_b" if_all ["casual_scarf","b"]
    always "hina_2_side_casual_scarf_face_fix_c" if_all ["casual_scarf","c"]
    always "hina_2_side_casual_scarf_face_fix_d" if_all ["casual_scarf","d"]
    always "hina_2_side_casual_scarf_face_fix_e" if_all ["casual_scarf","e"]
    always "hina_2_side_casual_scarf_face_fix_f" if_all ["casual_scarf","f"]
    always "hina_2_side_casual_scarf_face_fix_g" if_all ["casual_scarf","g"]
    always "hina_2_side_casual_scarf_face_fix_h" if_all ["casual_scarf","h"]
    always "hina_2_side_casual_scarf_face_fix_i" if_all ["casual_scarf","i"]
    always "hina_2_side_casual_scarf_face_fix_j" if_all ["casual_scarf","j"]

layeredimage hina 3 sm light:

    image_format "images/hina/{image}.webp"
    xcenter 846
    ycenter 541


    if hina_choker == "_choker":
        "hina_3_sm_light_pyjama"

    always "hina_3_sm_light_pyjama" if_any "pyjama_headphones_pjm"

    group body multiple:
        attribute curtain_znd
        attribute pillow_znd
        attribute pyjama
        attribute pyjama_pjm:
            "hina_3_sm_light_pyjama[hina_choker]"
        attribute pyjama_headphones

        attribute pyjama_headphones_pjm:
            "hina_3_sm_light_pyjama[hina_choker]_headphones"

    group face auto

layeredimage hina 3 sm dark:

    image_format "images/hina/{image}.webp"
    xcenter 846
    ycenter 541

    if hina_choker == "_choker":
        "hina_3_sm_dark_pyjama"

    attribute pyjama
    attribute pyjama_pjm:
        "hina_3_sm_dark_pyjama[hina_choker]"

    group face auto

layeredimage hina 3 lg light:

    image_format "images/hina/{image}.webp"
    xcenter 846
    ycenter 541


    if hina_choker == "_choker":
        "hina_3_lg_light_pyjama"

    group body multiple:
        attribute curtain_znd
        attribute pillow_znd
        attribute pyjama
        attribute pyjama_pjm:
            "hina_3_lg_light_pyjama[hina_choker]"
        attribute pyjama_headphones
        attribute pyjama_headphones_pjm:
            "hina_3_lg_light_pyjama[hina_choker]_headphones"

    group face auto

layeredimage hina 3 lg dark:

    image_format "images/hina/{image}.webp"
    xcenter 846
    ycenter 541

    if hina_choker == "_choker":
        "hina_3_lg_dark_pyjama"

    attribute pyjama
    attribute pyjama_pjm:
        "hina_3_lg_dark_pyjama[hina_choker]"

    group face auto

layeredimage sachiko 1:

    image_format "images/sachiko/{image}.webp"

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

image sachiko 1 lg = LayeredImageProxy("sachiko 1",transform=Transform(zoom=0.8,ycenter=1036))
image sachiko z4 1 lg = LayeredImageProxy("sachiko 1",transform=Transform(zoom=0.565,ycenter=773))

layeredimage sachiko 1 grayscale:

    image_format "images/sachiko_grayscale/{image}.webp"

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

image sachiko 1 grayscale lg = LayeredImageProxy("sachiko 1 grayscale",transform=Transform(zoom=0.8,ycenter=1036))

layeredimage sachiko 1 sm:

    image_format "images/sachiko/{image}.webp"
    ycenter 662

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

layeredimage sachiko 1 grayscale sm:

    image_format "images/sachiko_grayscale/{image}.webp"
    ycenter 662

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

layeredimage sachiko 1 side:

    image_format "images/sachiko/side/{image}.webp"

    pos (543,358)

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

layeredimage sachiko 2:

    image_format "images/sachiko/{image}.webp"
    ycenter 0

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

image sachiko 2 lg = LayeredImageProxy("sachiko 2",transform=Transform(zoom=0.8,ycenter=1036))
image sachiko z4 2 lg = LayeredImageProxy("sachiko 2",transform=Transform(zoom=0.565,ycenter=773))

layeredimage sachiko 2 sm:

    image_format "images/sachiko/{image}.webp"
    ycenter 662

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

layeredimage sachiko 2 side:

    image_format "images/sachiko/side/{image}.webp"
    pos (543,358)

    attribute znd
    attribute outfit

    attribute cigarette

    group face auto

layeredimage miyako 1:

    image_format "images/miyako/{image}.webp"

    always "miyako_1_body_znd_base" if_any ["znd_a","znd_b"]
    always "miyako_1_body_school_base" if_any ["school_a","school_a_sei","school_b","school_b_sei","school_cigarette","school_scarf_a","school_scarf_b","school_scarf_cigarette"]

    if miyako_scarf == "_scarf":
        "miyako_1_body_school_scarf" if_any ["school_a_sei","school_b_sei"]
    always "miyako_1_body_school_scarf" if_any ["school_scarf_a","school_a_sei","school_scarf_b","school_b_sei","school_scarf_cigarette"]
    always "miyako_1_body_pyjama_base" if_any ["pyjama_a","pyjama_b","pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_casual_base" if_any ["casual_a","casual_b"]

    group body:
        attribute znd_a
        attribute znd_b
        attribute school_a

        attribute school_a_sei:
            "miyako_1_body_school[miyako_scarf]_a"
        attribute school_b
        attribute school_b_sei:
            "miyako_1_body_school[miyako_scarf]_b"
        attribute school_cigarette
        attribute school_scarf_a
        attribute school_scarf_b
        attribute school_scarf_cigarette
        attribute pyjama_a
        attribute pyjama_b
        attribute casual_a
        attribute casual_b

    group face auto


    group pyjama_hood:
        attribute pyjama_hood_a:
            "miyako_1_body_pyjama_hood_a"
        attribute pyjama_hood_b:
            "miyako_1_body_pyjama_hood_b"


    always "miyako_1_face_fix_d" if_all "face_d" if_any ["znd_b","school_b","school_b_sei","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_face_fix_f" if_all "face_f" if_any ["znd_b","school_b","school_b_sei","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_face_fix_k" if_all "face_k" if_any ["znd_b","school_b","school_b_sei","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_face_fix_nh" if_all "nh" if_any ["school_scarf_a","school_scarf_cigarette"]

    always "miyako_1_face_fix_sei_k" if_all ["school_a_sei","k"]

    always "miyako_1_body_pyjama_hood_face_fix_a" if_all "face_a" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_b" if_all "face_b" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_c" if_all "face_c" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_d" if_all "face_d" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_e" if_all "face_e" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_f" if_all "face_f" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_g" if_all "face_g" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_h" if_all "face_h" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_i" if_all "face_i" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_j" if_all "face_j" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_k" if_all "face_k" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_body_pyjama_hood_face_fix_l" if_all "face_l" if_any ["pyjama_hood_a","pyjama_hood_b"]

image miyako 1 lg = LayeredImageProxy("miyako 1",transform=Transform(zoom=0.8,ycenter=1021))
image miyako z4 1 lg = LayeredImageProxy("miyako 1",transform=Transform(zoom=0.565,ycenter=757))


image noel 1 lg = LayeredImageProxy("miyako 1",transform=Transform(zoom=0.8,ycenter=1021))

layeredimage miyako 1 sm:

    image_format "images/miyako/{image}.webp"
    ycenter 631

    always "miyako_1_sm_body_znd_base" if_any ["znd_a","znd_b"]
    always "miyako_1_sm_body_school_base" if_any ["school_a","school_a_sei","school_b","school_b_sei","school_scarf_a","school_scarf_b","school_scarf_cigarette"]

    if miyako_scarf == "_scarf":
        "miyako_1_sm_body_school_scarf" if_any ["school_a_sei","school_b_sei"]
    always "miyako_1_sm_body_school_scarf" if_any ["school_scarf_a","school_a_sei","school_scarf_b","school_b_sei","school_scarf_cigarette"]
    always "miyako_1_sm_body_pyjama_base" if_any ["pyjama_a","pyjama_b","pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_casual_base" if_any ["casual_a","casual_b"]

    group body:
        attribute znd_a
        attribute znd_b
        attribute school_a

        attribute school_a_sei:
            "miyako_1_sm_body_school[miyako_scarf]_a"
        attribute school_b
        attribute school_b_sei:
            "miyako_1_sm_body_school[miyako_scarf]_b"
        attribute school_cigarette
        attribute school_scarf_a
        attribute school_scarf_b
        attribute school_scarf_cigarette
        attribute pyjama_a
        attribute pyjama_b
        attribute casual_a
        attribute casual_b

    group face auto

    group pyjama_hood:
        attribute pyjama_hood_a:
            "miyako_1_sm_body_pyjama_hood_a"
        attribute pyjama_hood_b:
            "miyako_1_sm_body_pyjama_hood_b"


    always "miyako_1_sm_face_fix_d" if_all "face_d" if_any ["znd_b","school_b","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_sm_face_fix_f" if_all "face_f" if_any ["znd_b","school_b","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_sm_face_fix_k" if_all "face_k" if_any ["znd_b","school_b","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_sm_face_fix_nh" if_all "nh" if_any ["school_scarf_a","school_scarf_cigarette"]

    always "miyako_1_sm_face_fix_sei_k" if_all ["school_a_sei","k"]

    always "miyako_1_sm_body_pyjama_hood_face_fix_a" if_all "face_a" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_b" if_all "face_b" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_c" if_all "face_c" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_d" if_all "face_d" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_e" if_all "face_e" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_f" if_all "face_f" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_g" if_all "face_g" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_h" if_all "face_h" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_i" if_all "face_i" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_j" if_all "face_j" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_k" if_all "face_k" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_sm_body_pyjama_hood_face_fix_l" if_all "face_l" if_any ["pyjama_hood_a","pyjama_hood_b"]

image noel 1 sm = LayeredImageProxy("miyako 1 sm")

layeredimage miyako 1 side:

    image_format "images/miyako/side/{image}.webp"
    pos (540,315)

    always "miyako_1_side_body_znd_base" if_any ["znd_a","znd_b"]
    always "miyako_1_side_body_school_base" if_any ["school_a","school_a_sei","school_b","school_b_sei","school_scarf_a","school_scarf_b","school_scarf_cigarette"]

    if miyako_scarf == "_scarf":
        "miyako_1_side_body_school_scarf" if_any ["school_a_sei","school_b_sei"]
    always "miyako_1_side_body_school_scarf" if_any ["school_scarf_a","school_a_sei","school_scarf_b","school_b_sei","school_scarf_cigarette"]

    always "miyako_1_side_body_pyjama_base" if_any ["pyjama_a","pyjama_b"]
    always "miyako_1_side_body_pyjama_hood_base" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_casual_base" if_any ["casual_a","casual_b"]

    group body:
        attribute znd_a
        attribute znd_b
        attribute school_a

        attribute school_a_sei:
            "miyako_1_side_body_school[miyako_scarf]_a"
        attribute school_b
        attribute school_b_sei:
            "miyako_1_side_body_school[miyako_scarf]_b"
        attribute school_cigarette
        attribute school_scarf_a
        attribute school_scarf_b
        attribute school_scarf_cigarette
        attribute pyjama_a
        attribute pyjama_b
        attribute casual_a
        attribute casual_b

    group face auto

    group pyjama_hood:
        attribute pyjama_hood_a:
            "miyako_1_side_body_pyjama_hood_a"
        attribute pyjama_hood_b:
            "miyako_1_side_body_pyjama_hood_b"

    group pyjama_hood_face_fix auto


    always "miyako_1_side_face_fix_d" if_all "face_d" if_any ["znd_b","school_b","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_side_face_fix_f" if_all "face_f" if_any ["znd_b","school_b","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]
    always "miyako_1_side_face_fix_k" if_all "face_k" if_any ["znd_b","school_b","school_scarf_b","pyjama_b","pyjama_hood_b","casual_b"]

    always "miyako_1_side_face_fix_sei_k" if_all ["school_a_sei","k"]

    always "miyako_1_side_body_pyjama_hood_face_fix_a" if_all "face_a" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_b" if_all "face_b" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_c" if_all "face_c" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_d" if_all "face_d" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_e" if_all "face_e" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_f" if_all "face_f" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_g" if_all "face_g" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_h" if_all "face_h" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_i" if_all "face_i" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_j" if_all "face_j" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_k" if_all "face_k" if_any ["pyjama_hood_a","pyjama_hood_b"]
    always "miyako_1_side_body_pyjama_hood_face_fix_l" if_all "face_l" if_any ["pyjama_hood_a","pyjama_hood_b"]

image noel 1 side = LayeredImageProxy("miyako 1 side")

layeredimage miyako 2:

    image_format "images/miyako/{image}.webp"

    always "miyako_2_body_school" if_any ["school_sei","school_scarf"]
    if miyako_scarf == "_scarf":
        "miyako_2_body_school_scarf" if_any "school_sei"
    always "miyako_2_body_pyjama_base" if_any ["pyjama","pyjama_hood"]

    group body:
        attribute znd
        attribute school
        attribute school_sei:
            "miyako_2_body_school[miyako_scarf]"
        attribute school_scarf
        attribute cigarette
        attribute pyjama
        attribute casual

    group face auto

    attribute pyjama_hood:
        "miyako_2_body_pyjama_hood"


    always "miyako_2_face_fix_i" if_all ["face_i","school_scarf"]

image miyako 2 lg = LayeredImageProxy("miyako 2",transform=Transform(zoom=0.8,ycenter=1021))
image miyako z4 2 lg = LayeredImageProxy("miyako 2",transform=Transform(zoom=0.565,ycenter=757))

image noel 2 lg = LayeredImageProxy("miyako 2",transform=Transform(zoom=0.8,ycenter=1021))

layeredimage miyako 2 sm:

    image_format "images/miyako/{image}.webp"
    ycenter 631

    always "miyako_2_sm_body_school" if_any ["school_sei","school_scarf"]
    if miyako_scarf == "_scarf":
        "miyako_2_sm_body_school_scarf" if_any "school_sei"
    always "miyako_2_sm_body_pyjama_base" if_any ["pyjama","pyjama_hood"]

    group body:
        attribute znd
        attribute school
        attribute school_sei:
            "miyako_2_sm_body_school[miyako_scarf]"
        attribute school_scarf
        attribute cigarette
        attribute pyjama
        attribute casual

    group face auto

    attribute pyjama_hood:
        "miyako_2_sm_body_pyjama_hood"


    always "miyako_2_sm_face_fix_i" if_all ["face_i","school_scarf"]

image noel 2 sm = LayeredImageProxy("miyako 2 sm")

layeredimage miyako 2 side:

    image_format "images/miyako/side/{image}.webp"
    pos (545,305)

    always "miyako_2_side_body_school" if_any ["school_sei","school_scarf"]
    if miyako_scarf == "_scarf":
        "miyako_2_side_body_school_scarf" if_any "school_sei"
    always "miyako_2_side_body_pyjama_base" if_any ["pyjama","pyjama_hood"]

    group body:
        attribute znd
        attribute school
        attribute school_sei:
            "miyako_2_side_body_school[miyako_scarf]"
        attribute school_scarf
        attribute cigarette
        attribute pyjama
        attribute casual

    group face auto

    attribute pyjama_hood:
        "miyako_2_side_body_pyjama_hood"


    always "miyako_2_side_face_fix_i" if_all ["face_i","school_scarf"]

image noel 2 sm = LayeredImageProxy("miyako 2 side")

layeredimage miyako 3 sm light:

    image_format "images/miyako/{image}.webp"
    xcenter 214
    ycenter 196

    attribute pyjama
    attribute znd

    group face auto

layeredimage miyako 3 sm nightlight:

    image_format "images/miyako/{image}.webp"
    xcenter 214
    ycenter 196

    always "miyako_3_sm_nightlight_pyjama"

    attribute pyjama

    group face auto

layeredimage miyako 3 sm dark:

    image_format "images/miyako/{image}.webp"
    xcenter 214
    ycenter 196

    always "miyako_3_sm_dark_pyjama"

    attribute pyjama

    group face auto

layeredimage miyako 3 lg light:

    image_format "images/miyako/{image}.webp"
    xcenter 214
    ycenter 196

    attribute pyjama
    attribute znd

    group face auto

layeredimage miyako 3 lg nightlight:

    image_format "images/miyako/{image}.webp"
    xcenter 214
    ycenter 196

    always "miyako_3_lg_nightlight_pyjama"

    attribute pyjama

    group face auto

layeredimage miyako 3 lg dark:

    image_format "images/miyako/{image}.webp"
    xcenter 214
    ycenter 196

    always "miyako_3_lg_dark_pyjama"

    attribute pyjama

    group face auto

image namahage lg = Image("etc/namahage lg.webp",ycenter=1037)
image namahage sm = Image("etc/namahage sm.webp",ycenter=683)



image fumi 1 lg pyjama a flat = Flatten("fumi 1 lg pyjama a")
image fumi 1 lg pyjama b flat = Flatten("fumi 1 lg pyjama b")
image fumi 1 lg pyjama e flat = Flatten("fumi 1 lg pyjama e")
image fumi 1 lg pyjama_scarf a flat = Flatten("fumi 1 lg pyjama_scarf a")
image fumi 1 lg school e flat = Flatten("fumi 1 lg school e")
image fumi 1 lg school j flat = Flatten("fumi 1 lg school j")
image fumi 1 lg school_scarf a flat = Flatten("fumi 1 lg school_scarf a")
image fumi 1 lg school_scarf b flat = Flatten("fumi 1 lg school_scarf b")
image fumi 1 lg school_scarf h flat = Flatten("fumi 1 lg school_scarf h")
image fumi 1 lg school_scarf k flat = Flatten("fumi 1 lg school_scarf k")
image fumi 1 sm casual e flat = Flatten("fumi 1 sm casual e")
image fumi 1 sm pyjama a flat = Flatten("fumi 1 sm pyjama a")
image fumi 1 sm pyjama e flat = Flatten("fumi 1 sm pyjama e")
image fumi 1 sm pyjama_scarf h flat = Flatten("fumi 1 sm pyjama_scarf h")
image fumi 1 sm school a flat = Flatten("fumi 1 sm school a")
image fumi 1 sm school h flat = Flatten("fumi 1 sm school h")
image fumi 1 sm school_scarf a flat = Flatten("fumi 1 sm school_scarf a")
image fumi 1 sm school_scarf b flat = Flatten("fumi 1 sm school_scarf b")
image fumi 1 sm school_scarf c flat = Flatten("fumi 1 sm school_scarf c")
image fumi 1 sm school_scarf d flat = Flatten("fumi 1 sm school_scarf d")
image fumi 1 sm school_scarf e flat = Flatten("fumi 1 sm school_scarf e")
image fumi 1 sm school_scarf h flat = Flatten("fumi 1 sm school_scarf h")
image fumi 1 sm school_scarf j flat = Flatten("fumi 1 sm school_scarf j")
image fumi 2 lg pyjama b flat = Flatten("fumi 2 lg pyjama b")
image fumi 2 lg school h flat = Flatten("fumi 2 lg school h")
image fumi z3 1 lg pyjama a flat = Flatten("fumi z3 1 lg pyjama a")
image fumi z3 1 lg pyjama c flat = Flatten("fumi z3 1 lg pyjama c")
image fumi z3 2 lg pyjama c flat = Flatten("fumi z3 2 lg pyjama c")
image fumi z3 2 lg pyjama d flat = Flatten("fumi z3 2 lg pyjama d")
image fumi z3 2 lg pyjama g flat = Flatten("fumi z3 2 lg pyjama g")
image fumi z4 1 lg pyjama a flat = Flatten("fumi z4 1 lg pyjama a")
image fumi z4 2 lg school_scarf d flat = Flatten("fumi z4 2 lg school_scarf d")
image hina 1 lg pyjama a flat = Flatten("hina 1 lg pyjama a")
image hina 1 lg pyjama e flat = Flatten("hina 1 lg pyjama e")
image hina 1 lg pyjama f flat = Flatten("hina 1 lg pyjama f")
image hina 1 lg pyjama h flat = Flatten("hina 1 lg pyjama h")
image hina 1 lg pyjama j flat = Flatten("hina 1 lg pyjama j")
image hina 1 lg pyjama l flat = Flatten("hina 1 lg pyjama l")
image hina 1 lg pyjama n flat = Flatten("hina 1 lg pyjama n")
image hina 1 lg pyjama_pjm d flat = Flatten("hina 1 lg pyjama_pjm d")
image hina 1 lg school c flat = Flatten("hina 1 lg school c")
image hina 1 lg school f flat = Flatten("hina 1 lg school f")
image hina 1 lg school k flat = Flatten("hina 1 lg school k")
image hina 1 lg school_scarf d flat = Flatten("hina 1 lg school_scarf d")
image hina 1 sm pyjama a flat = Flatten("hina 1 sm pyjama a")
image hina 1 sm pyjama d flat = Flatten("hina 1 sm pyjama d")
image hina 1 sm pyjama h flat = Flatten("hina 1 sm pyjama h")
image hina 1 sm pyjama i flat = Flatten("hina 1 sm pyjama i")
image hina 1 sm pyjama j flat = Flatten("hina 1 sm pyjama j")
image hina 1 sm school a flat = Flatten("hina 1 sm school a")
image hina 1 sm school b flat = Flatten("hina 1 sm school b")
image hina 1 sm school c flat = Flatten("hina 1 sm school c")
image hina 1 sm school h flat = Flatten("hina 1 sm school h")
image hina 1 sm school k flat = Flatten("hina 1 sm school k")
image hina 1 sm school_scarf a flat = Flatten("hina 1 sm school_scarf a")
image hina 1 sm school_scarf c flat = Flatten("hina 1 sm school_scarf c")
image hina 1 sm school_scarf e flat = Flatten("hina 1 sm school_scarf e")
image hina 1 sm school_scarf j flat = Flatten("hina 1 sm school_scarf j")
image hina 1 sm school_scarf k flat = Flatten("hina 1 sm school_scarf k")
image hina 1 sm school_scarf l flat = Flatten("hina 1 sm school_scarf l")
image hina 2 lg pyjama a flat = Flatten("hina 2 lg pyjama a")
image hina 2 lg pyjama d flat = Flatten("hina 2 lg pyjama d")
image hina 2 lg pyjama g flat = Flatten("hina 2 lg pyjama g")
image hina 2 lg pyjama h flat = Flatten("hina 2 lg pyjama h")
image hina 2 lg school e flat = Flatten("hina 2 lg school e")
image hina 2 lg school i flat = Flatten("hina 2 lg school i")
image hina 2 lg school_scarf d flat = Flatten("hina 2 lg school_scarf d")
image hina 2 lg school_scarf h flat = Flatten("hina 2 lg school_scarf h")
image hina 2 sm casual a flat = Flatten("hina 2 sm casual a")
image hina 2 sm school d flat = Flatten("hina 2 sm school d")
image hina 2 sm school_scarf a flat = Flatten("hina 2 sm school_scarf a")
image hina z3 1 lg pyjama d flat = Flatten("hina z3 1 lg pyjama d")
image hina z3 1 lg pyjama g flat = Flatten("hina z3 1 lg pyjama g")
image hina z4 2 lg pyjama_pjm f flat = Flatten("hina z4 2 lg pyjama_pjm f")
image hina z4 2 lg school a flat = Flatten("hina z4 2 lg school a")
image kimikara_23_b flat = Flatten("kimikara_23_b")
image miyako 1 lg pyjama_a b flat = Flatten("miyako 1 lg pyjama_a b")
image miyako 1 lg pyjama_a g flat = Flatten("miyako 1 lg pyjama_a g")
image miyako 1 lg pyjama_a k flat = Flatten("miyako 1 lg pyjama_a k")
image miyako 2 lg pyjama c flat = Flatten("miyako 2 lg pyjama c")
image miyako 2 sm school_sei a flat = Flatten("miyako 2 sm school_sei a")
image miyako 2 sm school_sei c flat = Flatten("miyako 2 sm school_sei c")
image miyako z4 1 lg pyjama_a b flat = Flatten("miyako z4 1 lg pyjama_a b")
image miyako z4 1 lg pyjama_a f flat = Flatten("miyako z4 1 lg pyjama_a f")
image miyako z4 2 lg pyjama a flat = Flatten("miyako z4 2 lg pyjama a")
image miyako z4 2 lg pyjama i flat = Flatten("miyako z4 2 lg pyjama i")
image noel 1 lg school_a nb flat = Flatten("noel 1 lg school_a nb")
image noel 1 lg school_a no flat = Flatten("noel 1 lg school_a no")
image noel 1 lg school_scarf_a nc flat = Flatten("noel 1 lg school_scarf_a nc")
image noel 1 lg school_scarf_a nd flat = Flatten("noel 1 lg school_scarf_a nd")
image noel 1 lg school_scarf_cigarette na flat = Flatten("noel 1 lg school_scarf_cigarette na")
image noel 1 lg school_scarf_cigarette nb flat = Flatten("noel 1 lg school_scarf_cigarette nb")
image noel 1 lg school_scarf_cigarette nf flat = Flatten("noel 1 lg school_scarf_cigarette nf")
image noel 1 lg school_scarf_cigarette ng flat = Flatten("noel 1 lg school_scarf_cigarette ng")
image noel 1 lg school_scarf_cigarette nh flat = Flatten("noel 1 lg school_scarf_cigarette nh")
image noel 1 lg school_scarf_cigarette ni flat = Flatten("noel 1 lg school_scarf_cigarette ni")
image noel 1 lg school_scarf_cigarette nj flat = Flatten("noel 1 lg school_scarf_cigarette nj")
image noel 1 lg school_scarf_cigarette nk flat = Flatten("noel 1 lg school_scarf_cigarette nk")
image noel 1 lg school_scarf_cigarette nl flat = Flatten("noel 1 lg school_scarf_cigarette nl")
image noel 1 lg school_scarf_cigarette nm flat = Flatten("noel 1 lg school_scarf_cigarette nm")
image noel 1 lg school_scarf_cigarette nn flat = Flatten("noel 1 lg school_scarf_cigarette nn")
image noel 1 sm school_scarf_cigarette nc flat = Flatten("noel 1 sm school_scarf_cigarette nc")
image noel 1 sm school_scarf_cigarette ne flat = Flatten("noel 1 sm school_scarf_cigarette ne")
image noel 1 sm school_scarf_cigarette nh flat = Flatten("noel 1 sm school_scarf_cigarette nh")
image noel 2 lg school_scarf cigarette nb flat = Flatten("noel 2 lg school_scarf cigarette nb")
image noel 2 lg school_scarf cigarette nc flat = Flatten("noel 2 lg school_scarf cigarette nc")
image rin 1 120 pyjama_a glasses j flat = Flatten("rin 1 120 pyjama_a glasses j")
image rin 1 lg casual i flat = Flatten("rin 1 lg casual i")
image rin 1 lg pyjama a flat = Flatten("rin 1 lg pyjama a")
image rin 1 lg pyjama c flat = Flatten("rin 1 lg pyjama c")
image rin 1 lg pyjama e flat = Flatten("rin 1 lg pyjama e")
image rin 1 lg pyjama f flat = Flatten("rin 1 lg pyjama f")
image rin 1 lg pyjama g glasses flat = Flatten("rin 1 lg pyjama g glasses")
image rin 1 lg pyjama glasses a flat = Flatten("rin 1 lg pyjama glasses a")
image rin 1 lg pyjama glasses b flat = Flatten("rin 1 lg pyjama glasses b")
image rin 1 lg pyjama glasses h flat = Flatten("rin 1 lg pyjama glasses h")
image rin 1 lg pyjama glasses i flat = Flatten("rin 1 lg pyjama glasses i")
image rin 1 lg pyjama glasses j flat = Flatten("rin 1 lg pyjama glasses j")
image rin 1 lg school f flat = Flatten("rin 1 lg school f")
image rin 1 lg school g flat = Flatten("rin 1 lg school g")
image rin 1 lg school i flat = Flatten("rin 1 lg school i")
image rin 1 lg school j flat = Flatten("rin 1 lg school j")
image rin 1 lg school_scarf c flat = Flatten("rin 1 lg school_scarf c")
image rin 1 sm casual c flat = Flatten("rin 1 sm casual c")
image rin 1 sm pyjama a flat = Flatten("rin 1 sm pyjama a")
image rin 1 sm pyjama b flat = Flatten("rin 1 sm pyjama b")
image rin 1 sm pyjama glasses a flat = Flatten("rin 1 sm pyjama glasses a")
image rin 1 sm pyjama glasses b flat = Flatten("rin 1 sm pyjama glasses b")
image rin 1 sm pyjama glasses f flat = Flatten("rin 1 sm pyjama glasses f")
image rin 1 sm pyjama i flat = Flatten("rin 1 sm pyjama i")
image rin 1 sm pyjama j flat = Flatten("rin 1 sm pyjama j")
image rin 1 sm pyjama pyjama_noshirt b flat = Flatten("rin 1 sm pyjama pyjama_noshirt b")
image rin 1 sm pyjama pyjama_noshirt d flat = Flatten("rin 1 sm pyjama pyjama_noshirt d")
image rin 1 sm school a flat = Flatten("rin 1 sm school a")
image rin 1 sm school b flat = Flatten("rin 1 sm school b")
image rin 1 sm school g flat = Flatten("rin 1 sm school g")
image rin 1 sm school h flat = Flatten("rin 1 sm school h")
image rin 1 sm school i flat = Flatten("rin 1 sm school i")
image rin 1 sm school_scarf a flat = Flatten("rin 1 sm school_scarf a")
image rin 1 sm school_scarf b flat = Flatten("rin 1 sm school_scarf b")
image rin 1 sm school_scarf e flat = Flatten("rin 1 sm school_scarf e")
image rin 1 sm school_scarf j flat = Flatten("rin 1 sm school_scarf j")
image rin 2 lg casual c flat = Flatten("rin 2 lg casual c")
image rin 2 lg pyjama a flat = Flatten("rin 2 lg pyjama a")
image rin 2 lg pyjama glasses a flat = Flatten("rin 2 lg pyjama glasses a")
image rin 2 lg pyjama glasses c flat = Flatten("rin 2 lg pyjama glasses c")
image rin 2 lg pyjama glasses g flat = Flatten("rin 2 lg pyjama glasses g")
image rin 2 lg school a flat = Flatten("rin 2 lg school a")
image rin 2 sm school b flat = Flatten("rin 2 sm school b")
image rin 2 sm school_scarf a flat = Flatten("rin 2 sm school_scarf a")
image rin 3 lg light pyjama g flat = Flatten("rin 3 lg light pyjama g")
image rin 3 lg nightlight pyjama_bed_b glasses_c flat = Flatten("rin 3 lg nightlight pyjama_bed_b glasses_c")
image rin z3 1 lg pyjama c flat = Flatten("rin z3 1 lg pyjama c")
image rin z3 1 lg pyjama glasses d flat = Flatten("rin z3 1 lg pyjama glasses d")
image rin z3 1 lg pyjama j flat = Flatten("rin z3 1 lg pyjama j")
image rin z4 1 lg pyjama glasses a flat = Flatten("rin z4 1 lg pyjama glasses a")
image rin z4 1 lg pyjama glasses b flat = Flatten("rin z4 1 lg pyjama glasses b")
image rin z4 1 lg pyjama glasses c flat = Flatten("rin z4 1 lg pyjama glasses c")
image rin z4 1 lg pyjama glasses e flat = Flatten("rin z4 1 lg pyjama glasses e")
image rin z4 1 lg pyjama glasses j flat = Flatten("rin z4 1 lg pyjama glasses j")
image rin z4 2 lg pyjama glasses a flat = Flatten("rin z4 2 lg pyjama glasses a")
image rin z4 2 lg pyjama glasses c flat = Flatten("rin z4 2 lg pyjama glasses c")
image rin z4 2 lg pyjama glasses g flat = Flatten("rin z4 2 lg pyjama glasses g")
image rin z4 2 lg school d flat = Flatten("rin z4 2 lg school d")
image sachiko 1 lg outfit h flat = Flatten("sachiko 1 lg outfit h")
image sachiko 2 sm outfit c flat = Flatten("sachiko 2 sm outfit c")
image sachiko z4 1 lg outfit a flat = Flatten("sachiko z4 1 lg outfit a")
image sachiko z4 1 lg outfit i flat = Flatten("sachiko z4 1 lg outfit i")
image sachiko z4 2 lg outfit cigarette d flat = Flatten("sachiko z4 2 lg outfit cigarette d")





image black = Solid("#000")
image white = Solid("#fff")

layeredimage ev01:

    image_format "images/{image}.webp"

    always "ev01"

    group rin:
        attribute rin_a
        attribute rin_b
        attribute rin_a_glasses
        attribute rin_b_glasses

    group fumi:
        attribute fumi_a
        attribute fumi_b

    group hina:
        attribute hina_a
        attribute hina_b

    attribute hina_headphones

image ev01a = LayeredImage(["ev01","ev01_rin_a","ev01_fumi_a","ev01_hina_a"])
image ev01b = LayeredImage(["ev01","ev01_rin_b","ev01_fumi_a","ev01_hina_a"])
image ev01c = LayeredImage(["ev01","ev01_rin_b","ev01_fumi_a","ev01_hina_b"])


image ev01f = LayeredImage(["ev01","ev01_rin_b","ev01_fumi_b","ev01_hina_b"])
image ev01g = LayeredImage(["ev01","ev01_rin_a_glasses","ev01_fumi_a","ev01_hina_a","ev01_hina_headphones"])
image ev01h = LayeredImage(["ev01","ev01_rin_b_glasses","ev01_fumi_a","ev01_hina_a","ev01_hina_headphones"])


image ev01k = LayeredImage(["ev01","ev01_rin_a_glasses","ev01_fumi_b","ev01_hina_a","ev01_hina_headphones"])

layeredimage ev01_grayscale:

    image_format "images/{image}.webp"

    always "ev01_grayscale"

    group rin:
        attribute rin_a_grayscale
        attribute rin_b_grayscale

    group fumi:
        attribute fumi_a_grayscale
        attribute fumi_b_grayscale

    group hina:
        attribute hina_a_grayscale
        attribute hina_b_grayscale

image ev01a_grayscale = LayeredImage(["ev01_grayscale","ev01_rin_a_grayscale","ev01_fumi_a_grayscale","ev01_hina_a_grayscale"])
image ev01b_grayscale = LayeredImage(["ev01_grayscale","ev01_rin_b_grayscale","ev01_fumi_a_grayscale","ev01_hina_a_grayscale"])
image ev01c_grayscale = LayeredImage(["ev01_grayscale","ev01_rin_b_grayscale","ev01_fumi_a_grayscale","ev01_hina_b_grayscale"])
image ev01f_grayscale = LayeredImage(["ev01_grayscale","ev01_rin_b_grayscale","ev01_fumi_b_grayscale","ev01_hina_b_grayscale"])

image ev02a = Composite((1024,768),(0,0),"images/ev02.webp",(0,0),"images/ev02a.webp")
image ev02b = Composite((1024,768),(0,0),"images/ev02.webp",(0,0),"images/ev02b.webp")
image ev02c = Composite((1024,768),(0,0),"images/ev02.webp",(0,0),"images/ev02c.webp")
image ev02d = Composite((1024,768),(0,0),"images/ev02.webp",(0,0),"images/ev02d.webp")
image ev02e = Composite((1024,768),(0,0),"images/ev02.webp",(0,0),"images/ev02e.webp")

image ev03b = Composite((1024,768),(0,0),"images/ev03a.webp",(0,0),"images/ev03b.webp")
image ev03e = Composite((1024,768),(0,0),"images/ev03c.webp",(0,0),"images/ev03e.webp")

layeredimage ev04:

    image_format "images/{image}.webp"

    always "ev04"

    group hina:
        attribute hina_a
        attribute hina_b
        attribute hina_c
        attribute hina_d
        attribute hina_e

    group fumi:
        attribute fumi_a
        attribute fumi_b
        attribute fumi_c
        attribute fumi_d
        attribute fumi_e
        attribute fumi_f

image ev04a = LayeredImage(["ev04","ev04_hina_a","ev04_fumi_a"])
image ev04b = LayeredImage(["ev04","ev04_hina_a","ev04_fumi_f"])
image ev04c = LayeredImage(["ev04","ev04_hina_b","ev04_fumi_a"])
image ev04d = LayeredImage(["ev04","ev04_hina_b","ev04_fumi_b"])
image ev04e = LayeredImage(["ev04","ev04_hina_c","ev04_fumi_c"])
image ev04f = LayeredImage(["ev04","ev04_hina_d","ev04_fumi_c"])
image ev04g = LayeredImage(["ev04","ev04_hina_e","ev04_fumi_d"])
image ev04h = LayeredImage(["ev04","ev04_hina_e","ev04_fumi_e"])

layeredimage ev06:

    image_format "images/{image}.webp"

    always "ev06"

    group rin:
        attribute rin_a
        attribute rin_b
        attribute rin_c
        attribute rin_d

    group fumi:
        attribute fumi_a
        attribute fumi_b
        attribute fumi_c
        attribute fumi_d

image ev06a = LayeredImage(["ev06","ev06_rin_a","ev06_fumi_a"])
image ev06b = LayeredImage(["ev06","ev06_rin_b","ev06_fumi_a"])
image ev06c = LayeredImage(["ev06","ev06_rin_c","ev06_fumi_a"])
image ev06d = LayeredImage(["ev06","ev06_rin_d","ev06_fumi_a"])
image ev06e = LayeredImage(["ev06","ev06_rin_a","ev06_fumi_b"])
image ev06f = LayeredImage(["ev06","ev06_rin_b","ev06_fumi_b"])
image ev06g = LayeredImage(["ev06","ev06_rin_d","ev06_fumi_b"])
image ev06h = LayeredImage(["ev06","ev06_rin_a","ev06_fumi_c"])
image ev06i = LayeredImage(["ev06","ev06_rin_b","ev06_fumi_c"])
image ev06j = LayeredImage(["ev06","ev06_rin_d","ev06_fumi_d"])

layeredimage kimihane_03:

    image_format "images/{image}.webp"

    always "kimihane_03"

    attribute miyako

    group sachiko auto

image kimihane_03_f = LayeredImage(["kimihane_03","kimihane_03_miyako","kimihane_03_sachiko_a"])
image kimihane_03_g = LayeredImage(["kimihane_03","kimihane_03_miyako","kimihane_03_sachiko_b"])
image kimihane_03_h = LayeredImage(["kimihane_03","kimihane_03_miyako","kimihane_03_sachiko_c"])
image kimihane_03_i = LayeredImage(["kimihane_03","kimihane_03_miyako","kimihane_03_sachiko_e"])
image kimihane_03_j = LayeredImage(["kimihane_03","kimihane_03_miyako","kimihane_03_sachiko_d"])

image kimihane_03_l = LayeredImage(["kimihane_03","kimihane_03_miyako","kimihane_03_sachiko_g"])
image kimihane_03_m = LayeredImage(["kimihane_03","kimihane_03_sachiko_g"])
image kimihane_03_n = LayeredImage(["kimihane_03","kimihane_03_sachiko_h"])



image kimihane_03_r = LayeredImage(["kimihane_03","kimihane_03_sachiko_d"])
image kimihane_03_s = LayeredImage(["kimihane_03","kimihane_03_sachiko_e"])
image kimihane_03_t = LayeredImage(["kimihane_03","kimihane_03_sachiko_f"])

layeredimage kimikara_01:
    image_format "images/{image}.webp"

    always "kimikara_01"

    group fumi auto
    group rin auto
    group hina auto
    group miyako auto

image kimikara_01_aa = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_a","kimikara_01_miyako_a","kimikara_01_hina_a","kimikara_01_rin_a"])
image kimikara_01_ab = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_a"])

image kimikara_01_ad = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_b","kimikara_01_miyako_c","kimikara_01_hina_c","kimikara_01_rin_b"])
image kimikara_01_ae = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_a","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_a"])
image kimikara_01_af = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_a","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_b"])
image kimikara_01_ag = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_c","kimikara_01_rin_b"])
image kimikara_01_ah = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_b","kimikara_01_rin_b"])
image kimikara_01_ai = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_b"])
image kimikara_01_aj = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_b","kimikara_01_miyako_a","kimikara_01_hina_c","kimikara_01_rin_b"])





image kimikara_01_ap = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_a","kimikara_01_miyako_c","kimikara_01_hina_c","kimikara_01_rin_a"])
image kimikara_01_aq = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_a","kimikara_01_fumi_a","kimikara_01_miyako_c","kimikara_01_hina_c","kimikara_01_rin_b"])

image kimikara_01_ba = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_a","kimikara_01_miyako_a","kimikara_01_hina_a","kimikara_01_rin_a"])
image kimikara_01_bb = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_a"])
image kimikara_01_bc = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_a","kimikara_01_miyako_a","kimikara_01_hina_d","kimikara_01_rin_b"])

image kimikara_01_be = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_a","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_a"])
image kimikara_01_bf = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_a","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_b"])
image kimikara_01_bg = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_c","kimikara_01_rin_b"])
image kimikara_01_bh = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_b","kimikara_01_rin_b"])
image kimikara_01_bi = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_a","kimikara_01_rin_b"])
image kimikara_01_bj = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_a","kimikara_01_hina_c","kimikara_01_rin_b"])
image kimikara_01_bk = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_d","kimikara_01_rin_a"])
image kimikara_01_bl = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_b","kimikara_01_hina_d","kimikara_01_rin_b"])
image kimikara_01_bm = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_a","kimikara_01_miyako_b","kimikara_01_hina_d","kimikara_01_rin_a"])
image kimikara_01_bn = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_b","kimikara_01_miyako_a","kimikara_01_hina_d","kimikara_01_rin_a"])
image kimikara_01_bo = LayeredImage(["kimikara_01","kimikara_01_rin_pyjama_b","kimikara_01_fumi_a","kimikara_01_miyako_b","kimikara_01_hina_d","kimikara_01_rin_b"])




image kimikara_02_a = ConditionSwitch(
                                    "persistent.dpatch","kimikara_02d.webp",
                                    "True","kimikara_02.webp"
                                    )
image kimikara_02_b = ConditionSwitch(
                                    "persistent.dpatch",Composite((1024,768),(0,0),"kimikara_02d.webp",(0,0),"kimikara_02d_b.webp"),
                                    "True",Composite((1024,768),(0,0),"kimikara_02.webp",(0,0),"kimikara_02_b.webp")
                                    )

layeredimage kimikara_03:

    image_format "images/{image}.webp"

    always "kimikara_03"

    group miyako auto
    group sachiko auto

image kimikara_03_a = LayeredImage(["kimikara_03","kimikara_03_miyako_a","kimikara_03_sachiko_a"])
image kimikara_03_b = LayeredImage(["kimikara_03","kimikara_03_miyako_b","kimikara_03_sachiko_a"])
image kimikara_03_c = LayeredImage(["kimikara_03","kimikara_03_miyako_a","kimikara_03_sachiko_b"])
image kimikara_03_d = LayeredImage(["kimikara_03","kimikara_03_miyako_b","kimikara_03_sachiko_b"])

layeredimage kimikara_04:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2
    attribute base3

    group fumi auto
    group hina multiple auto
    group chocolate auto

image kimikara_04_a = LayeredImage(["kimikara_04_base1","kimikara_04_fumi_a","kimikara_04_hina_a"])
image kimikara_04_b = LayeredImage(["kimikara_04_base1","kimikara_04_fumi_b","kimikara_04_hina_a"])
image kimikara_04_c = LayeredImage(["kimikara_04_base1","kimikara_04_fumi_b","kimikara_04_hina_b"])
image kimikara_04_d = LayeredImage(["kimikara_04_base1","kimikara_04_fumi_c","kimikara_04_hina_c","kimikara_04_chocolate_a"])
image kimikara_04_e = LayeredImage(["kimikara_04_base1","kimikara_04_fumi_b","kimikara_04_hina_b","kimikara_04_hina_b2","kimikara_04_chocolate_b"])
image kimikara_04_f = LayeredImage(["kimikara_04_base1","kimikara_04_base2","kimikara_04_fumi_b","kimikara_04_hina_d"])
image kimikara_04_g = LayeredImage(["kimikara_04_base1","kimikara_04_base2","kimikara_04_base3","kimikara_04_fumi_d","kimikara_04_hina_e"])
image kimikara_04_h = LayeredImage(["kimikara_04_base1","kimikara_04_fumi_e","kimikara_04_hina_f","kimikara_04_chocolate_b"])

layeredimage kimikara_05:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2

    group fumi auto
    group hina auto

image kimikara_05_a = LayeredImage(["kimikara_05_base1","kimikara_05_hina_a","kimikara_05_fumi_a"])
image kimikara_05_b = LayeredImage(["kimikara_05_base1","kimikara_05_hina_b","kimikara_05_fumi_b"])
image kimikara_05_c = LayeredImage(["kimikara_05_base1","kimikara_05_hina_c","kimikara_05_fumi_c"])
image kimikara_05_d = LayeredImage(["kimikara_05_base1","kimikara_05_hina_d","kimikara_05_fumi_c"])
image kimikara_05_e = LayeredImage(["kimikara_05_base1","kimikara_05_base2","kimikara_05_hina_e"])
image kimikara_05_f = LayeredImage(["kimikara_05_base1","kimikara_05_base2","kimikara_05_hina_f"])

layeredimage kimikara_06:

    image_format "images/{image}.webp"

    always "kimikara_06"

    attribute e1

    group rin auto
    group hina auto

image kimikara_06_a = LayeredImage(["kimikara_06","kimikara_06_hina_a","kimikara_06_rin_a"])
image kimikara_06_b = LayeredImage(["kimikara_06","kimikara_06_hina_a","kimikara_06_rin_b"])
image kimikara_06_c = LayeredImage(["kimikara_06","kimikara_06_hina_b","kimikara_06_rin_c"])
image kimikara_06_d = LayeredImage(["kimikara_06","kimikara_06_hina_a","kimikara_06_rin_c"])
image kimikara_06_e = LayeredImage(["kimikara_06","kimikara_06_e1"])

layeredimage kimikara_07:

    image_format "images/{image}.webp"

    always "kimikara_07"

    group rin auto
    group hina auto

image kimikara_07_a = LayeredImage(["kimikara_07","kimikara_07_hina_a","kimikara_07_rin_a"])
image kimikara_07_b = LayeredImage(["kimikara_07","kimikara_07_hina_a","kimikara_07_rin_b"])
image kimikara_07_c = LayeredImage(["kimikara_07","kimikara_07_hina_b","kimikara_07_rin_a"])
image kimikara_07_d = LayeredImage(["kimikara_07","kimikara_07_hina_c","kimikara_07_rin_c"])
image kimikara_07_e = LayeredImage(["kimikara_07","kimikara_07_hina_d","kimikara_07_rin_d"])
image kimikara_07_f = LayeredImage(["kimikara_07","kimikara_07_hina_d","kimikara_07_rin_a"])
image kimikara_07_g = LayeredImage(["kimikara_07","kimikara_07_hina_d","kimikara_07_rin_b"])
image kimikara_07_h = LayeredImage(["kimikara_07","kimikara_07_hina_c","kimikara_07_rin_d"])
image kimikara_07_i = LayeredImage(["kimikara_07","kimikara_07_hina_b","kimikara_07_rin_d"])

layeredimage kimikara_08:

    image_format "images/{image}.webp"

    always "kimikara_08"

    attribute hand

    group fumi auto
    group rin auto

image kimikara_08_a = LayeredImage(["kimikara_08","kimikara_08_fumi_a","kimikara_08_rin_a"])
image kimikara_08_b = LayeredImage(["kimikara_08","kimikara_08_fumi_b","kimikara_08_rin_b"])
image kimikara_08_c = LayeredImage(["kimikara_08","kimikara_08_fumi_c","kimikara_08_rin_c"])
image kimikara_08_d = LayeredImage(["kimikara_08","kimikara_08_hand","kimikara_08_fumi_d","kimikara_08_rin_d"])
image kimikara_08_e = LayeredImage(["kimikara_08","kimikara_08_hand","kimikara_08_fumi_e","kimikara_08_rin_d"])

image kimikara_09_c = Composite((1024,768),(0,0),"kimikara_09_a.webp",(0,0),"kimikara_09_c.webp")

layeredimage kimikara_10:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2
    attribute base3
    attribute base4

    attribute tree

    group sachiko:
        attribute a
        attribute b
        attribute c
        attribute d
        attribute e
        attribute a_grayscale
        attribute b_grayscale
        attribute c_grayscale
        attribute f_grayscale
        attribute g_grayscale
        attribute h_grayscale

    attribute scarf

    group miyako auto

image kimikara_10_a = LayeredImage(["kimikara_10_base1","kimikara_10_sachiko_a_grayscale"])
image kimikara_10_b = LayeredImage(["kimikara_10_base1","kimikara_10_sachiko_b_grayscale"])
image kimikara_10_c = LayeredImage(["kimikara_10_base1","kimikara_10_sachiko_c_grayscale"])
image kimikara_10_d = LayeredImage(["kimikara_10_base1","kimikara_10_base2","kimikara_10_sachiko_f_grayscale"])
image kimikara_10_e = LayeredImage(["kimikara_10_base1","kimikara_10_base2","kimikara_10_sachiko_g_grayscale"])
image kimikara_10_f = LayeredImage(["kimikara_10_base1","kimikara_10_base2","kimikara_10_sachiko_h_grayscale"])
image kimikara_10_g = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_scarf","kimikara_10_miyako_a"])
image kimikara_10_g_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_miyako_a"])
image kimikara_10_h = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_a"])
image kimikara_10_h_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_miyako_a"])
image kimikara_10_i = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_d","kimikara_10_scarf","kimikara_10_miyako_d"])
image kimikara_10_i_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_d","kimikara_10_miyako_d"])
image kimikara_10_j = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_scarf","kimikara_10_miyako_b"])
image kimikara_10_j_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_miyako_b"])
image kimikara_10_k = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_b"])
image kimikara_10_k_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_miyako_b"])
image kimikara_10_l = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_c","kimikara_10_scarf","kimikara_10_miyako_b"])
image kimikara_10_l_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_c","kimikara_10_miyako_b"])
image kimikara_10_m = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_scarf","kimikara_10_miyako_c"])
image kimikara_10_m_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_miyako_c"])
image kimikara_10_n = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_c"])
image kimikara_10_n_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_miyako_c"])
image kimikara_10_o = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_c","kimikara_10_scarf","kimikara_10_miyako_c"])
image kimikara_10_o_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_c","kimikara_10_miyako_c"])
image kimikara_10_p = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_scarf","kimikara_10_miyako_d"])
image kimikara_10_p_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_a","kimikara_10_miyako_d"])
image kimikara_10_q = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_d"])
image kimikara_10_q_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_miyako_d"])
image kimikara_10_r = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_c","kimikara_10_scarf","kimikara_10_miyako_d"])
image kimikara_10_r_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_c","kimikara_10_miyako_d"])
image kimikara_10_s = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_e","kimikara_10_scarf","kimikara_10_miyako_d"])
image kimikara_10_s_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_e","kimikara_10_miyako_d"])
image kimikara_10_t = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_d","kimikara_10_scarf","kimikara_10_miyako_e"])
image kimikara_10_t_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_d","kimikara_10_miyako_e"])
image kimikara_10_u = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_f"])
image kimikara_10_u_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_b","kimikara_10_miyako_f"])
image kimikara_10_v = LayeredImage(["kimikara_10_base3","kimikara_10_tree","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_c"])
image kimikara_10_w = LayeredImage(["kimikara_10_base3","kimikara_10_tree","kimikara_10_sachiko_b","kimikara_10_scarf","kimikara_10_miyako_d"])
image kimikara_10_x = LayeredImage(["kimikara_10_base3","kimikara_10_base4","kimikara_10_tree","kimikara_10_sachiko_b","kimikara_10_miyako_g"])
image kimikara_10_y = LayeredImage(["kimikara_10_base3","kimikara_10_base4","kimikara_10_tree","kimikara_10_sachiko_b","kimikara_10_miyako_h"])
image kimikara_10_z = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_d","kimikara_10_scarf","kimikara_10_miyako_c"])
image kimikara_10_z_ = LayeredImage(["kimikara_10_base3","kimikara_10_sachiko_d","kimikara_10_miyako_c"])

image kimikara_11_b = Composite((1024,768),(0,0),"images/kimikara_11_a.webp",(0,0),"images/kimikara_11_b.webp")

layeredimage kimikara_19:

    image_format "images/{image}.webp"

    always "kimikara_19_base"
    always "kimikara_19_hina_base2" if_any ["kimikara_19_hina_b","kimikara_19_hina_c","kimikara_19_hina_d"]
    always "kimikara_19_rin_base2" if_any ["kimikara_19_rin_c","kimikara_19_rin_d"]

    group fumi multiple auto
    group rin multiple auto
    group hina multiple auto
    group miyako multiple auto

image kimikara_19_a = LayeredImage(["kimikara_19_base","kimikara_19_fumi_a","kimikara_19_rin_a","kimikara_19_hina_a","kimikara_19_miyako_a"])
image kimikara_19_b = LayeredImage(["kimikara_19_base","kimikara_19_fumi_a","kimikara_19_rin_a","kimikara_19_hina_a","kimikara_19_miyako_b"])
image kimikara_19_c = LayeredImage(["kimikara_19_base","kimikara_19_fumi_a","kimikara_19_rin_a","kimikara_19_hina_a","kimikara_19_miyako_c"])
image kimikara_19_d = LayeredImage(["kimikara_19_base","kimikara_19_fumi_b","kimikara_19_rin_b","kimikara_19_hina_base2","kimikara_19_hina_b","kimikara_19_miyako_d"])
image kimikara_19_e = LayeredImage(["kimikara_19_base","kimikara_19_fumi_b","kimikara_19_rin_b","kimikara_19_hina_base2","kimikara_19_hina_c","kimikara_19_miyako_d"])
image kimikara_19_f = LayeredImage(["kimikara_19_base","kimikara_19_fumi_base2","kimikara_19_fumi_c","kimikara_19_rin_base2","kimikara_19_rin_c","kimikara_19_hina_base2","kimikara_19_hina_d","kimikara_19_miyako_e"])
image kimikara_19_g = LayeredImage(["kimikara_19_base","kimikara_19_fumi_base2","kimikara_19_fumi_c","kimikara_19_rin_base2","kimikara_19_rin_d","kimikara_19_hina_a","kimikara_19_miyako_e"])
image kimikara_19_h = LayeredImage(["kimikara_19_base","kimikara_19_fumi_base2","kimikara_19_fumi_c","kimikara_19_rin_base2","kimikara_19_rin_c","kimikara_19_hina_base2","kimikara_19_hina_d","kimikara_19_miyako_d"])
image kimikara_19_i = LayeredImage(["kimikara_19_base","kimikara_19_fumi_a","kimikara_19_rin_a","kimikara_19_hina_base2","kimikara_19_hina_c","kimikara_19_miyako_b"])

image kimikara_22_b = Composite((1024,768),(0,0),"images/kimikara_22_a.webp",(0,0),"images/kimikara_22_b.webp")

layeredimage kimikara_23:

    image_format "images/{image}.webp"

    always "kimikara_23"

    group sachiko auto
    group miyako auto

image kimikara_23_a = LayeredImage(["kimikara_23","kimikara_23_sachiko_a","kimikara_23_miyako_a"])
image kimikara_23_b = LayeredImage(["kimikara_23","kimikara_23_sachiko_a","kimikara_23_miyako_b"])
image kimikara_23_d = LayeredImage(["kimikara_23","kimikara_23_sachiko_b","kimikara_23_miyako_b"])
image kimikara_23_e = LayeredImage(["kimikara_23","kimikara_23_sachiko_c","kimikara_23_miyako_a"])
image kimikara_23_b_flat = Flatten("kimikara_23_b")

image kimikara_24_b = Composite((1024,768),(0,0),"images/kimikara_24_a.webp",(0,0),"images/kimikara_24_b.webp")

image bg01ab = Composite((1024,768),(0,0),"images/bg01aa.webp",(0,0),"images/bg01ab.webp")
image bg01ad = Composite((1024,768),(0,0),"images/bg01ac.webp",(0,0),"images/bg01ad.webp")
image bg01ag = Composite((1024,768),(0,0),"images/bg01aa.webp",(0,0),"images/bg01ah.webp",(0,0),"images/bg01ag.webp")
image bg01ah = Composite((1024,768),(0,0),"images/bg01aa.webp",(0,0),"images/bg01ah.webp")
image bg01bb = Composite((1024,768),(0,0),"images/bg01ba.webp",(0,0),"images/bg01bb.webp")
image bg01bg = Composite((1024,768),(0,0),"images/bg01ba.webp",(0,0),"images/bg01bh.webp",(0,0),"images/bg01bg.webp")
image bg01bh = Composite((1024,768),(0,0),"images/bg01ba.webp",(0,0),"images/bg01bh.webp")
image bg01cb = Composite((1024,768),(0,0),"images/bg01ca.webp",(0,0),"images/bg01cb.webp")
image bg01cc = Composite((1024,768),(0,0),"images/bg01ca.webp",(0,0),"images/bg01cc_b.webp",(0,0),"images/bg01cc.webp")
image bg01cc_b = Composite((1024,768),(0,0),"images/bg01ca.webp",(0,0),"images/bg01cc_b.webp")
image bg01cd = Composite((1024,768),(0,0),"images/bg01ca.webp",(0,0),"images/bg01cc_b.webp",(0,0),"images/bg01cc.webp",(0,0),"images/bg01cd.webp")
image bg01cg = Composite((1024,768),(0,0),"images/bg01ca.webp",(0,0),"images/bg01ch.webp",(0,0),"images/bg01cg.webp")
image bg01ch = Composite((1024,768),(0,0),"images/bg01ca.webp",(0,0),"images/bg01ch.webp")
image bg01db = Composite((1024,768),(0,0),"images/bg01da.webp",(0,0),"images/bg01db.webp")
image bg01dg = Composite((1024,768),(0,0),"images/bg01da.webp",(0,0),"images/bg01dh.webp",(0,0),"images/bg01dg.webp")
image bg01dh = Composite((1024,768),(0,0),"images/bg01da.webp",(0,0),"images/bg01dh.webp")
image bg02ag = Composite((1024,768),(0,0),"images/bg02aa.webp",(0,0),"images/bg02ag.webp")
image bg02bg = Composite((1024,768),(0,0),"images/bg02aa.webp",(0,0),"images/bg02bg.webp")
image bg02cg = Composite((1024,768),(0,0),"images/bg02aa.webp",(0,0),"images/bg02cg.webp")
image bg02db = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02db.webp")
image bg02dd = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02db.webp",(0,0),"images/bg02de.webp")
image bg02de = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02de.webp")
image bg02bg = Composite((1024,768),(0,0),"images/bg02ba.webp",(0,0),"images/bg02bg.webp")
image bg02dg = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02dg.webp")
image bg02dh = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02dg.webp",(0,0),"images/bg02db.webp")
image bg02di = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02db.webp",(0,0),"images/bg02de.webp",(0,0),"images/bg02dg.webp")
image bg02dj = Composite((1024,768),(0,0),"images/bg02da.webp",(0,0),"images/bg02db.webp",(0,0),"images/bg02de.webp",(0,0),"images/bg02dg.webp",(0,0),"images/bg02dj.webp")
image bg09cb = Composite((1024,768),(0,0),"images/bg09ca.webp",(0,0),"images/bg09cb.webp")
image bg09cc = Composite((1024,768),(0,0),"images/bg09ca.webp",(0,0),"images/bg09cb.webp",(0,0),"images/bg09cc.webp")
image bg10ab = Composite((1024,768),(0,0),"images/bg10aa.webp",(0,0),"images/bg10ab.webp")
image bg10bb = Composite((1024,768),(0,0),"images/bg10ba.webp",(0,0),"images/bg10bb.webp")
image bg10cb = Composite((1024,768),(0,0),"images/bg10ca.webp",(0,0),"images/bg10cb.webp")




image bati:
    "images/bati_01.webp"
    0.012
    "images/bati_02.webp"
    0.012
    "images/bati_03.webp"
    0.012
    "images/bati_04.webp"
    0.012
    "images/bati_05.webp"
    0.012
    Null()

image bati2:
    "images/bati_01.webp"
    0.06
    "images/bati_02.webp"
    0.06
    "images/bati_03.webp"
    0.06
    "images/bati_04.webp"
    0.06
    "images/bati_05.webp"
    0.06
    Null()

image batim:
    "images/batim_01.webp"
    0.06
    "images/batim_02.webp"
    0.06
    "images/batim_03.webp"
    0.06
    "images/batim_04.webp"
    0.06
    "images/batim_05.webp"
    0.06
    Null()


image fumi 1 lg pyjama c grayscale = Transform("images/fumi_1_lg_pyjama_c_grayscale.webp",zoom=0.8,ycenter=1021)
image fumi 1 sm pyjama b grayscale = Transform("images/fumi_1_sm_pyjama_b_grayscale.webp",ycenter=631)
image fumi 1 sm pyjama c grayscale = Transform("images/fumi_1_sm_pyjama_c_grayscale.webp",ycenter=631)
image fumi 1 sm school a grayscale = Transform("images/fumi_1_sm_school_a_grayscale.webp",ycenter=631)
image fumi 1 sm school d grayscale = Transform("images/fumi_1_sm_school_d_grayscale.webp",ycenter=631)
image fumi 1 sm school e grayscale = Transform("images/fumi_1_sm_school_e_grayscale.webp",ycenter=631)
image fumi 1 sm school h grayscale = Transform("images/fumi_1_sm_school_h_grayscale.webp",ycenter=631)
image fumi 1 sm school_scarf a grayscale = Transform("images/fumi_1_sm_school_scarf_a_grayscale.webp",ycenter=631)
image fumi 2 lg pyjama b grayscale = Transform("images/fumi_2_lg_pyjama_b_grayscale.webp",zoom=0.8,ycenter=1021)
image fumi 2 lg pyjama h grayscale = Transform("images/fumi_2_lg_pyjama_h_grayscale.webp",zoom=0.8,ycenter=1021)
image fumi z3 1 lg pyjama c grayscale = Transform("images/fumi_1_lg_pyjama_c_grayscale.webp",zoom=0.77,ycenter=999)
image fumi z3 1 lg school a grayscale = Transform("images/fumi_1_lg_school_a_grayscale.webp",zoom=0.77,ycenter=999)
image fumi z3 1 lg school d grayscale = Transform("images/fumi_1_lg_school_d_grayscale.webp",zoom=0.77,ycenter=999)

image rin 1 lg pyjama glasses b grayscale = Transform("images/rin_1_lg_pyjama_glasses_b_grayscale.webp",zoom=0.8,ycenter=1016)
image rin 1 lg pyjama glasses c grayscale = Transform("images/rin_1_lg_pyjama_glasses_c_grayscale.webp",zoom=0.8,ycenter=1016)
image rin 1 lg pyjama glasses h grayscale = Transform("images/rin_1_lg_pyjama_glasses_h_grayscale.webp",zoom=0.8,ycenter=1016)
image rin 1 lg pyjama glasses j grayscale = Transform("images/rin_1_lg_pyjama_glasses_j_grayscale.webp",zoom=0.8,ycenter=1016)
image rin 1 lg pyjama glasses k grayscale = Transform("images/rin_1_lg_pyjama_glasses_k_grayscale.webp",zoom=0.8,ycenter=1016)
image rin 1 sm pyjama glasses g grayscale = Transform("images/rin_1_sm_pyjama_glasses_g_grayscale.webp",ycenter=631)
image rin 1 sm pyjama glasses i grayscale = Transform("images/rin_1_sm_pyjama_glasses_i_grayscale.webp",ycenter=631)
image rin 1 sm pyjama glasses j grayscale = Transform("images/rin_1_sm_pyjama_glasses_j_grayscale.webp",ycenter=631)
image rin 1 sm school a grayscale = Transform("images/rin_1_sm_school_a_grayscale.webp",ycenter=631)
image rin 1 sm school b grayscale = Transform("images/rin_1_sm_school_b_grayscale.webp",ycenter=631)
image rin 1 sm school g grayscale = Transform("images/rin_1_sm_school_g_grayscale.webp",ycenter=631)
image rin 1 sm school_scarf a grayscale = Transform("images/rin_1_sm_school_scarf_a_grayscale.webp",ycenter=631)
image rin 2 lg pyjama glasses a grayscale = Transform("images/rin_2_lg_pyjama_glasses_a_grayscale.webp",zoom=0.8,ycenter=1016)
image rin z3 1 lg school a grayscale = Transform("images/rin_1_lg_school_a_grayscale.webp",zoom=0.77,ycenter=994)
image rin z3 1 lg school g grayscale = Transform("images/rin_1_lg_school_g_grayscale.webp",zoom=0.77,ycenter=994)

image hina 1 lg pyjama c grayscale = Transform("images/hina_1_lg_pyjama_c_grayscale.webp",zoom=0.8,ycenter=981)
image hina 1 lg pyjama d grayscale = Transform("images/hina_1_lg_pyjama_d_grayscale.webp",zoom=0.8,ycenter=981)
image hina 1 lg pyjama k grayscale = Transform("images/hina_1_lg_pyjama_k_grayscale.webp",zoom=0.8,ycenter=981)
image hina 1 sm pyjama a grayscale = Transform("images/hina_1_sm_pyjama_a_grayscale.webp",ycenter=614)
image hina 1 sm pyjama c grayscale = Transform("images/hina_1_sm_pyjama_c_grayscale.webp",ycenter=614)
image hina 1 sm pyjama k grayscale = Transform("images/hina_1_sm_pyjama_k_grayscale.webp",ycenter=614)
image hina 1 sm school f grayscale = Transform("images/hina_1_sm_school_f_grayscale.webp",ycenter=614)
image hina 1 sm school j grayscale = Transform("images/hina_1_sm_school_j_grayscale.webp",ycenter=614)
image hina 1 sm school k grayscale = Transform("images/hina_1_sm_school_k_grayscale.webp",ycenter=614)
image hina 1 sm school_scarf f grayscale = Transform("images/hina_1_sm_school_scarf_f_grayscale.webp",ycenter=614)
image hina 1 sm school_scarf j grayscale = Transform("images/hina_1_sm_school_scarf_j_grayscale.webp",ycenter=614)
image hina z3 1 lg school h grayscale = Transform("images/hina_1_lg_school_h_grayscale.webp",zoom=0.77,ycenter=959)


transform monochrome:
    matrixcolor SaturationMatrix(0.390625)

image bg10ba_50 = At("images/bg10ba.webp",monochrome)




init python:









    class LayerShake():
        """Class to produce random layer shake ATL transform animations.
        Arguments x and y are halved to produce maximum distance in both
        directions.
        [dmc] The persistent variable layer_shaken is set to true
        here so it is not repeated when the interaction is restarted
        until it is explicitly set to false. Note that this is a
        workaround for API updates in Ren'Py versions after 7.3.5.

        Example:

        camera:
            function LayerShake(20,20,0.25)
        $ persistent.layer_shaken = False
        """
        def __init__(self,x,y,t):
            self.x = x
            self.y = y
            self.t = t
        
        def __call__(self,trans,st,at):
            if persistent.layer_shaken:
                trans.offset = (0,0)
                return 0
            if st < self.t:
                trans.offset = (renpy.random.randint((-self.x // 2),(self.x // 2)),renpy.random.randint((-self.y // 2),(self.y // 2)))
                return 0
            else:
                trans.offset = (0,0)
                persistent.layer_shaken = True
                return None




transform default:
    xoffset 0
    yoffset 0
    xcenter 512

transform pos_l:
    yoffset 0
    xcenter 252

transform pos_ls:
    yoffset 0
    xcenter 292

transform pos_l2:
    yoffset 0
    xcenter 172

transform pos_l2s:
    yoffset 0
    xcenter 192

transform pos_r:
    yoffset 0
    xcenter 772

transform pos_rs:
    yoffset 0
    xcenter 732

transform pos_r2:
    yoffset 0
    xcenter 852

transform pos_r2s:
    yoffset 0
    xcenter 832

transform pos_l2_z3:
    yoffset 0
    xcenter 182

transform pos_r2_z3:
    yoffset 0
    xcenter 842

transform ShakeYes:
    yoffset 0
    ease 0.25 yoffset 20
    ease 0.25 yoffset 0

transform ShakeYes_5_750:
    yoffset 0
    ease 0.375 yoffset 5
    ease 0.375 yoffset 0

transform ShakeYes2:
    yoffset 0
    ease 0.2 yoffset 20
    ease 0.2 yoffset 0
    ease 0.2 yoffset 20
    ease 0.2 yoffset 0

transform ShakeYes2_5_500:
    yoffset 0
    ease 0.25 yoffset 5
    ease 0.25 yoffset 0
    ease 0.25 yoffset 5
    ease 0.25 yoffset 0

transform ShakeNo:
    xoffset 0
    ease 0.25 xoffset 8
    ease 0.25 xoffset 0
    ease 0.25 xoffset 8
    ease 0.25 xoffset 0

transform ShakeNo_2_250:
    xoffset 0
    ease 0.125 xoffset 2
    ease 0.125 xoffset 0
    ease 0.125 xoffset 2
    ease 0.125 xoffset 0

transform ShakeNo_3_500:
    xoffset 0
    ease 0.25 xoffset 3
    ease 0.25 xoffset 0
    ease 0.25 xoffset 3
    ease 0.25 xoffset 0

transform ShakeNo_3_750:
    xoffset 0
    ease 0.375 xoffset 3
    ease 0.375 xoffset 0
    ease 0.375 xoffset 3
    ease 0.375 xoffset 0

transform ShakeNo_4_500:
    xoffset 0
    ease 0.25 xoffset 4
    ease 0.25 xoffset 0
    ease 0.25 xoffset 4
    ease 0.25 xoffset 0

transform ShakeJump:
    yoffset 0
    ease 0.125 yoffset -30
    ease 0.125 yoffset 0

transform ShakeJump2:
    yoffset 0
    ease 0.4 yoffset -30
    ease 0.4 yoffset 0

transform ShakeUji:
    xoffset 0
    ease 0.5 xoffset 10
    ease 0.5 xoffset 0
    ease 0.5 xoffset 10
    ease 0.5 xoffset 0

transform ShakeTameiki:
    xoffset 0
    ease 0.4 yoffset 30
    ease 0.4 yoffset 0

transform ShakeSide:
    xoffset 0 yoffset 0
    ease 0.05 xoffset -10 yoffset 3
    ease 0.05 xoffset 0 yoffset 0
    ease 0.05 xoffset 20 yoffset -5
    ease 0.05 xoffset 0 yoffset 0




init python:


    def QuadraticEaseInOut(p):
        if (p < 0.5):
            return 2 * p * p
        return (-2 * p * p) + (4 * p) - 1

define dict_dissolve_10 = { "master" : Dissolve(0.1) }
define dict_dissolve_25 = { "master" : Dissolve(0.25) }
define dict_dissolve_50 = { "master" : Dissolve(0.5) }
define dict_dissolve_75 = { "master" : Dissolve(0.75) }

define bg_effect_01 = ImageDissolve("tr/bg_effect_01.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_01_1000 = ImageDissolve("tr/bg_effect_01.webp",time=1.0,ramplen=256,reverse=True)
define bg_effect_02 = ImageDissolve("tr/bg_effect_02.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_02_1000 = ImageDissolve("tr/bg_effect_02.webp",time=1.0,ramplen=256,reverse=True)
define bg_effect_05 = ImageDissolve("tr/bg_effect_05.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_06 = ImageDissolve("tr/bg_effect_06.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_07_1000 = ImageDissolve("tr/bg_effect_07.webp",time=1.0,ramplen=256,reverse=True)
define bg_effect_08 = ImageDissolve("tr/bg_effect_08.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_08_1000 = ImageDissolve("tr/bg_effect_08.webp",time=1.0,ramplen=256,reverse=True)
define bg_effect_08_2000 = ImageDissolve("tr/bg_effect_08.webp",time=2.0,ramplen=256,reverse=True)
define bg_effect_09 = ImageDissolve("tr/bg_effect_09.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_10 = ImageDissolve("tr/bg_effect_10.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_11 = ImageDissolve("tr/bg_effect_11.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_12 = ImageDissolve("tr/bg_effect_12.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_12_250 = ImageDissolve("tr/bg_effect_12.webp",time=0.25,ramplen=256,reverse=True)
define bg_effect_13 = ImageDissolve("tr/bg_effect_13.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_13_100 = ImageDissolve("tr/bg_effect_13.webp",time=0.1,ramplen=256,reverse=True)
define bg_effect_14 = ImageDissolve("tr/bg_effect_14.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_17_100 = ImageDissolve("tr/bg_effect_17.webp",time=0.1,ramplen=256,reverse=True)
define bg_effect_17_250 = ImageDissolve("tr/bg_effect_17.webp",time=0.25,ramplen=128,reverse=True)
define bg_effect_17_300 = ImageDissolve("tr/bg_effect_17.webp",time=0.3,ramplen=128,reverse=True)
define bg_effect_17_1000 = ImageDissolve("tr/bg_effect_17.webp",time=1.0,ramplen=256,reverse=True)
define bg_effect_18 = ImageDissolve("tr/bg_effect_18.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_18_100 = ImageDissolve("tr/bg_effect_18.webp",time=0.1,ramplen=256,reverse=True)
define bg_effect_18_250 = ImageDissolve("tr/bg_effect_18.webp",time=0.25,ramplen=128,reverse=True)
define bg_effect_18_1000 = ImageDissolve("tr/bg_effect_18.webp",time=1.0,ramplen=128,reverse=True)
define bg_effect_18_2000 = ImageDissolve("tr/bg_effect_18.webp",time=2.0,ramplen=128,reverse=True)
define bg_effect_21 = ImageDissolve("tr/bg_effect_21.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_24_750 = ImageDissolve("tr/bg_effect_24.webp",time=0.75,ramplen=256,reverse=True)
define bg_effect_25 = ImageDissolve("tr/bg_effect_25.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_25_750 = ImageDissolve("tr/bg_effect_25.webp",time=0.75,ramplen=256,reverse=True)
define bg_effect_25_1000 = ImageDissolve("tr/bg_effect_25.webp",time=1.0,ramplen=256,reverse=True)
define bg_effect_26_750 = ImageDissolve("tr/bg_effect_26.webp",time=0.75,ramplen=256,reverse=True)
define bg_effect_27 = ImageDissolve("tr/bg_effect_27.webp",time=0.5,ramplen=256,reverse=True)
define bg_effect_27_750 = ImageDissolve("tr/bg_effect_27.webp",time=0.75,ramplen=256,reverse=True)
define bg_effect_30_1200 = ImageDissolve("tr/bg_effect_30.webp",time=1.2,ramplen=128,reverse=True,time_warp=QuadraticEaseInOut)
define bg_effect_31_1200 = ImageDissolve("tr/bg_effect_31.webp",time=1.2,ramplen=128,reverse=True,time_warp=QuadraticEaseInOut)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
