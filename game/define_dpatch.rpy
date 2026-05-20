layeredimage ev07:

    image_format "images/{image}.webp"

    always "ev07"

    group hina:
        attribute hina_a
        attribute hina_b
        attribute hina_c
        attribute hina_d

    group fumi:
        attribute fumi_a
        attribute fumi_b
        attribute fumi_c
        attribute fumi_d

image ev07a = LayeredImage(["ev07","ev07_hina_a","ev07_fumi_a"])
image ev07b = LayeredImage(["ev07","ev07_hina_b","ev07_fumi_a"])
image ev07c = LayeredImage(["ev07","ev07_hina_c","ev07_fumi_b"])
image ev07d = LayeredImage(["ev07","ev07_hina_c","ev07_fumi_c"])
image ev07e = LayeredImage(["ev07","ev07_hina_d","ev07_fumi_d"])


layeredimage ev08:

    image_format "images/{image}.webp"

    always "ev08"

    attribute a

    group hina:
        attribute hina_b
        attribute hina_c
        attribute hina_d
        attribute hina_e

    group rin:
        attribute rin_b
        attribute rin_c

image ev08a = LayeredImage(["ev08","ev08_a"])
image ev08b = LayeredImage(["ev08","ev08_hina_b","ev08_rin_b"])
image ev08c = LayeredImage(["ev08","ev08_hina_c","ev08_rin_b"])
image ev08d = LayeredImage(["ev08","ev08_hina_d","ev08_rin_b"])
image ev08e = LayeredImage(["ev08","ev08_hina_d","ev08_rin_c"])
image ev08f = LayeredImage(["ev08","ev08_hina_e","ev08_rin_b"])

layeredimage ev09:

    image_format "images/{image}.webp"

    always "ev09"

    group fumi:
        attribute fumi_a
        attribute fumi_b
        attribute fumi_c
        attribute fumi_d

    group rin:
        attribute rin_a
        attribute rin_b
        attribute rin_c
        attribute rin_d

image ev09a = LayeredImage(["ev09","ev09_fumi_a","ev09_rin_a"])
image ev09b = LayeredImage(["ev09","ev09_fumi_b","ev09_rin_b"])
image ev09c = LayeredImage(["ev09","ev09_fumi_c","ev09_rin_b"])
image ev09d = LayeredImage(["ev09","ev09_fumi_d","ev09_rin_c"])
image ev09e = LayeredImage(["ev09","ev09_fumi_d","ev09_rin_d"])

image ev10a = Composite((1024,768),(0,0),"images/ev10.webp",(0,0),"images/ev10a.webp")
image ev10b = Composite((1024,768),(0,0),"images/ev10.webp",(0,0),"images/ev10b.webp")
image ev10c = Composite((1024,768),(0,0),"images/ev10.webp",(0,0),"images/ev10c.webp")
image ev10d = Composite((1024,768),(0,0),"images/ev10.webp",(0,0),"images/ev10d.webp")

layeredimage ev11:

    image_format "images/{image}.webp"

    always "ev11"

    group hina:
        attribute hina_a
        attribute hina_b
        attribute hina_c
        attribute hina_d
        attribute hina_e

    group rin:
        attribute rin_a
        attribute rin_b
        attribute rin_c

image ev11a = LayeredImage(["ev11","ev11_hina_a","ev11_rin_b"])
image ev11b = LayeredImage(["ev11","ev11_hina_b","ev11_rin_b"])
image ev11c = LayeredImage(["ev11","ev11_hina_c","ev11_rin_b"])
image ev11d = LayeredImage(["ev11","ev11_hina_d","ev11_rin_a"])
image ev11e = LayeredImage(["ev11","ev11_hina_e","ev11_rin_a"])
image ev11f = LayeredImage(["ev11","ev11_hina_e","ev11_rin_c"])

layeredimage ev12:

    image_format "images/{image}.webp"

    always "ev12"

    attribute hand_a
    attribute hand_b

    group rin:
        attribute rin_a
        attribute rin_b
        attribute rin_c
        attribute rin_d

    group fumi:
        attribute fumi_a
        attribute fumi_b
        attribute fumi_c

image ev12a = LayeredImage(["ev12","ev12_rin_a"])
image ev12b = LayeredImage(["ev12","ev12_rin_a","ev12_inset","ev12_fumi_a"])
image ev12c = LayeredImage(["ev12","ev12_rin_a","ev12_inset","ev12_fumi_c"])
image ev12d = LayeredImage(["ev12","ev12_hand_a","ev12_rin_b"])
image ev12e = LayeredImage(["ev12","ev12_hand_a","ev12_rin_b","ev12_inset","ev12_fumi_c"])
image ev12f = LayeredImage(["ev12","ev12_hand_a","ev12_hand_b","ev12_rin_c"])
image ev12g = LayeredImage(["ev12","ev12_hand_a","ev12_hand_b","ev12_rin_c","ev12_inset","ev12_fumi_b"])
image ev12h = LayeredImage(["ev12","ev12_hand_a","ev12_hand_b","ev12_rin_c","ev12_inset","ev12_fumi_c"])
image ev12i = LayeredImage(["ev12","ev12_hand_a","ev12_hand_b","ev12_rin_d"])
image ev12j = LayeredImage(["ev12","ev12_hand_a","ev12_hand_b","ev12_rin_d","ev12_inset","ev12_fumi_c"])

layeredimage kimihane_16:

    image_format "images/{image}.webp"

    always "kimihane_16_base1"

    attribute base2
    attribute base3

    group fumi:
        attribute fumi_a
        attribute fumi_b
        attribute fumi_c
        attribute fumi_d

    group rin multiple:
        attribute rin_a
        attribute rin_b
        attribute rin_c
        attribute rin_d
        attribute rin_e
        attribute rin_f
        attribute rin_g

image kimihane_16_a = LayeredImage(["kimihane_16","kimihane_16_fumi_a","kimihane_16_rin_a"])
image kimihane_16_b = LayeredImage(["kimihane_16","kimihane_16_fumi_b","kimihane_16_rin_a"])
image kimihane_16_c = LayeredImage(["kimihane_16","kimihane_16_fumi_b","kimihane_16_rin_b"])
image kimihane_16_d = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_fumi_b","kimihane_16_rin_b"])
image kimihane_16_e = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_fumi_b","kimihane_16_rin_b","kimihane_16_rin_c"])
image kimihane_16_f = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_base3","kimihane_16_fumi_b","kimihane_16_rin_b","kimihane_16_rin_c","kimihane_16_rin_d"])
image kimihane_16_g = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_base3","kimihane_16_fumi_b","kimihane_16_rin_e"])
image kimihane_16_h = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_base3","kimihane_16_fumi_b","kimihane_16_rin_f"])
image kimihane_16_i = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_base3","kimihane_16_fumi_b","kimihane_16_rin_g"])
image kimihane_16_j = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_base3","kimihane_16_fumi_c","kimihane_16_rin_g"])
image kimihane_16_k = LayeredImage(["kimihane_16","kimihane_16_base2","kimihane_16_base3","kimihane_16_fumi_d","kimihane_16_rin_g"])

image kimihane_16_e_zoom = Composite((1024,768),(0,0),"images/kimihane_16_a_zoom.webp",(0,0),"images/kimihane_16_e_zoom.webp")

layeredimage kimikara_12:

    image_format "images/{image}.webp"

    always "kimikara_12"

    group fumi auto
    group hina auto

image kimikara_12_a = LayeredImage(["kimikara_12","kimikara_12_fumi_a","kimikara_12_hina_a"])
image kimikara_12_b = LayeredImage(["kimikara_12","kimikara_12_fumi_b","kimikara_12_hina_b"])
image kimikara_12_c = LayeredImage(["kimikara_12","kimikara_12_fumi_c","kimikara_12_hina_c"])
image kimikara_12_d = LayeredImage(["kimikara_12","kimikara_12_fumi_c","kimikara_12_hina_d"])
image kimikara_12_e = LayeredImage(["kimikara_12","kimikara_12_fumi_d","kimikara_12_hina_c"])
image kimikara_12_f = LayeredImage(["kimikara_12","kimikara_12_fumi_d","kimikara_12_hina_d"])
image kimikara_12_g = LayeredImage(["kimikara_12","kimikara_12_fumi_e","kimikara_12_hina_e"])
image kimikara_12_h = LayeredImage(["kimikara_12","kimikara_12_fumi_f","kimikara_12_hina_f"])
image kimikara_12_i = LayeredImage(["kimikara_12","kimikara_12_fumi_g","kimikara_12_hina_g"])

layeredimage kimikara_13:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2
    attribute base3

    group fumi auto
    group hina auto

image kimikara_13_a = LayeredImage(["kimikara_13_base1","kimikara_13_fumi_a","kimikara_13_hina_a"])
image kimikara_13_b = LayeredImage(["kimikara_13_base1","kimikara_13_fumi_a","kimikara_13_hina_b"])
image kimikara_13_c = LayeredImage(["kimikara_13_base1","kimikara_13_fumi_b","kimikara_13_hina_b"])
image kimikara_13_d = LayeredImage(["kimikara_13_base1","kimikara_13_fumi_c","kimikara_13_hina_c"])
image kimikara_13_e = LayeredImage(["kimikara_13_base1","kimikara_13_fumi_d","kimikara_13_hina_d"])
image kimikara_13_f = LayeredImage(["kimikara_13_base1","kimikara_13_base2","kimikara_13_fumi_d","kimikara_13_hina_d"])
image kimikara_13_g = LayeredImage(["kimikara_13_base1","kimikara_13_base2","kimikara_13_fumi_e","kimikara_13_hina_e"])
image kimikara_13_h = LayeredImage(["kimikara_13_base1","kimikara_13_base3","kimikara_13_fumi_f","kimikara_13_hina_f"])

layeredimage kimikara_14:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2
    attribute base3

    group rin auto
    group hina auto

image kimikara_14_a = LayeredImage(["kimikara_14_base1","kimikara_14_rin_a","kimikara_14_hina_a"])
image kimikara_14_b = LayeredImage(["kimikara_14_base1","kimikara_14_rin_b","kimikara_14_hina_a"])
image kimikara_14_c = LayeredImage(["kimikara_14_base1","kimikara_14_rin_b","kimikara_14_hina_b"])
image kimikara_14_d = LayeredImage(["kimikara_14_base1","kimikara_14_base2","kimikara_14_rin_a","kimikara_14_hina_a"])
image kimikara_14_e = LayeredImage(["kimikara_14_base1","kimikara_14_base2","kimikara_14_rin_b","kimikara_14_hina_a"])
image kimikara_14_f = LayeredImage(["kimikara_14_base1","kimikara_14_base2","kimikara_14_rin_b","kimikara_14_hina_b"])
image kimikara_14_g = LayeredImage(["kimikara_14_base1","kimikara_14_base2","kimikara_14_base3","kimikara_14_rin_c","kimikara_14_hina_c"])
image kimikara_14_h = LayeredImage(["kimikara_14_base1","kimikara_14_base2","kimikara_14_base3","kimikara_14_rin_d","kimikara_14_hina_d"])

layeredimage kimikara_15:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2

    attribute b1

    group rin auto
    group hina auto

image kimikara_15_a = LayeredImage(["kimikara_15_base1","kimikara_15_rin_a","kimikara_15_hina_a"])
image kimikara_15_b = LayeredImage(["kimikara_15_base1","kimikara_15_b1"])
image kimikara_15_c = LayeredImage(["kimikara_15_base1","kimikara_15_rin_a","kimikara_15_hina_b"])
image kimikara_15_d = LayeredImage(["kimikara_15_base1","kimikara_15_rin_a","kimikara_15_hina_c"])
image kimikara_15_e = LayeredImage(["kimikara_15_base1","kimikara_15_rin_a","kimikara_15_hina_d"])
image kimikara_15_f = LayeredImage(["kimikara_15_base1","kimikara_15_base2","kimikara_15_rin_d"])
image kimikara_15_g = LayeredImage(["kimikara_15_base1","kimikara_15_base2","kimikara_15_rin_e"])
image kimikara_15_h = LayeredImage(["kimikara_15_base1","kimikara_15_rin_c","kimikara_15_hina_e"])

layeredimage kimikara_16:

    image_format "images/{image}.webp"

    always "kimikara_16"

    group fumi auto
    group rin auto

image kimikara_16_a = LayeredImage(["kimikara_16","kimikara_16_fumi_a","kimikara_16_rin_a"])
image kimikara_16_b = LayeredImage(["kimikara_16","kimikara_16_fumi_a","kimikara_16_rin_b"])
image kimikara_16_c = LayeredImage(["kimikara_16","kimikara_16_fumi_b","kimikara_16_rin_a"])
image kimikara_16_d = LayeredImage(["kimikara_16","kimikara_16_fumi_c","kimikara_16_rin_b"])
image kimikara_16_e = LayeredImage(["kimikara_16","kimikara_16_fumi_d","kimikara_16_rin_c"])
image kimikara_16_f = LayeredImage(["kimikara_16","kimikara_16_fumi_e","kimikara_16_rin_a"])
image kimikara_16_g = LayeredImage(["kimikara_16","kimikara_16_fumi_a","kimikara_16_rin_e"])
image kimikara_16_h = LayeredImage(["kimikara_16","kimikara_16_fumi_c","kimikara_16_rin_c"])
image kimikara_16_i = LayeredImage(["kimikara_16","kimikara_16_fumi_e","kimikara_16_rin_c"])
image kimikara_16_j = LayeredImage(["kimikara_16","kimikara_16_fumi_d","kimikara_16_rin_a"])
image kimikara_16_k = LayeredImage(["kimikara_16","kimikara_16_fumi_c","kimikara_16_rin_e"])
image kimikara_16_l = LayeredImage(["kimikara_16","kimikara_16_fumi_e","kimikara_16_rin_d"])
image kimikara_16_m = LayeredImage(["kimikara_16","kimikara_16_fumi_c","kimikara_16_rin_d"])
image kimikara_16_n = LayeredImage(["kimikara_16","kimikara_16_fumi_b","kimikara_16_rin_b"])
image kimikara_16_o = LayeredImage(["kimikara_16","kimikara_16_fumi_d","kimikara_16_rin_e"])

layeredimage kimikara_17:

    image_format "images/{image}.webp"

    attribute base1
    attribute base2
    attribute base3

    group fumi auto
    group rin auto

image kimikara_17_a = LayeredImage(["kimikara_17_base1","kimikara_17_fumi_a","kimikara_17_rin_a"])
image kimikara_17_b = LayeredImage(["kimikara_17_base1","kimikara_17_fumi_b","kimikara_17_rin_a"])
image kimikara_17_c = LayeredImage(["kimikara_17_base1","kimikara_17_fumi_a","kimikara_17_rin_b"])
image kimikara_17_d = LayeredImage(["kimikara_17_base1","kimikara_17_fumi_c","kimikara_17_rin_c"])
image kimikara_17_e = LayeredImage(["kimikara_17_base1","kimikara_17_base2","kimikara_17_fumi_d","kimikara_17_rin_d"])
image kimikara_17_f = LayeredImage(["kimikara_17_base1","kimikara_17_base2","kimikara_17_base3","kimikara_17_fumi_e","kimikara_17_rin_e"])

layeredimage kimikara_18:

    image_format "images/{image}.webp"

    always "kimikara_19_base1"

    attribute base2
    attribute base3
    attribute base4
    attribute base5

    group sachiko auto
    group miyako auto

image kimikara_18_a = LayeredImage(["kimikara_18_base1","kimikara_18_sachiko_a","kimikara_18_miyako_a"])
image kimikara_18_b = LayeredImage(["kimikara_18_base1","kimikara_18_sachiko_b","kimikara_18_miyako_a"])
image kimikara_18_c = LayeredImage(["kimikara_18_base1","kimikara_18_sachiko_c","kimikara_18_miyako_a"])
image kimikara_18_d = LayeredImage(["kimikara_18_base1","kimikara_18_sachiko_d","kimikara_18_miyako_a"])
image kimikara_18_e = LayeredImage(["kimikara_18_base1","kimikara_18_sachiko_d","kimikara_18_miyako_b"])
image kimikara_18_f = LayeredImage(["kimikara_18_base1","kimikara_18_base2","kimikara_18_sachiko_a","kimikara_18_miyako_a"])
image kimikara_18_g = LayeredImage(["kimikara_18_base1","kimikara_18_base2","kimikara_18_sachiko_b","kimikara_18_miyako_c"])
image kimikara_18_h = LayeredImage(["kimikara_18_base1","kimikara_18_base2","kimikara_18_base3","kimikara_18_sachiko_b","kimikara_18_miyako_b"])
image kimikara_18_i = LayeredImage(["kimikara_18_base1","kimikara_18_base2","kimikara_18_base3","kimikara_18_base4","kimikara_18_sachiko_e"])
image kimikara_18_j = LayeredImage(["kimikara_18_base1","kimikara_18_base2","kimikara_18_base3","kimikara_18_sachiko_f","kimikara_18_miyako_b"])
image kimikara_18_k = LayeredImage(["kimikara_18_base1","kimikara_18_base2","kimikara_18_base3","kimikara_18_base5","kimikara_18_sachiko_g","kimikara_18_miyako_d"])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
