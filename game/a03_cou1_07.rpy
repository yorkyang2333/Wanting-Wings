label a03_cou1_07:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg02ba with Dissolve(0.25)
    pause 0.75

    play music bgm05

    show rin 1 sm pyjama glasses h behind hina with Dissolve(0.25)

    voice "RIN_0612"
    rin "\"Mmh... you're going to the doctor's office first thing tomorrow morning.\""

    "It's Sunday, so they're closed today."

    show hina 3 sm light pyjama d with Dissolve(0.25)

    voice "HIN_0784"
    hina "\"Hweh... nah... I'm... totally fine. You're making a big deal of it...\""

    show rin:
        "rin 1 sm pyjama glasses g" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_0613"
    rin "\"You don't get to say that when you have a 102-degree fever. You really are an idiot, and you still caught a cold.\""

    show rin 1 sm pyjama glasses g:
        xoffset 0 yoffset 0
    with None
    show hina 3 sm light pyjama j with dict_dissolve_25

    voice "HIN_0785"
    hina "\"Ugh... I'm not an idiot.\""

    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "RIN_0614"
    rin "\"Shut up. And go to sleep, idiot.\""

    "Rin poked Hina in the forehead."

    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "RIN_0615"
    rin "\"...You're gonna have to go to the hospital if it gets any worse.\""

    show hina 3 sm light pyjama f with dict_dissolve_25

    voice "HIN_0786"
    hina "\"Uh huh...\""

    play sound se521

    hide hina with dict_dissolve_25

    $ side_image = "fumi 1 side school_scarf b"

    voice "FUM_0579"
    fumi "\"I'm back! Sorry I'm late, I'll start dinner right—\""

    play sound se113d

    show fumi behind hina:
        "fumi 1 sm school_scarf j flat"
        alpha 0.0 xcenter 572 ycenter 779
        easein 0.5 alpha 1.0 xcenter 672
    pause 0.5

    show fumi 1 sm school_scarf j:
        alpha 1.0 xcenter 672 ycenter 779
    with None
    show rin 1 sm pyjama glasses b with dict_dissolve_25

    stop sound fadeout 1.0

    voice "FUM_0580"
    fumi "\"H-Hina?! What happened?!\""

    "Fumi ran over, dropping her groceries in the kitchen."

    show hina 3 sm light pyjama i with dict_dissolve_25

    voice "HIN_0787"
    hina "\"Oh, hey... Fumi...\""

    "Hina smiled weakly as Fumi knelt down beside her bed."

    show rin:
        "rin 1 sm pyjama glasses a" with Dissolve(0.25)
        ShakeYes

    voice "RIN_0616"
    rin "\"Uhh, here.\""

    show rin 1 sm pyjama glasses a:
        xoffset 0 yoffset 0
    with None

    "Rin held out to Fumi..."

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0581"
    fumi "\"The angel's feather?\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0617"
    rin "\"To summarize: we opened the window and the feather blew outside, so Hina jumped out after it, barefoot.\""


    show hina:
        "hina 3 sm light pyjama g" with Dissolve(0.25)

    show fumi:
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0582"
    fumi "\"Huh?!\""

    show fumi 1 sm school_scarf j:

        ycenter 779 xoffset 0 yoffset 0
    with None

    "Makes sense she's surprised. She was barefoot. And they {i}are{/i} on the second floor."

    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "RIN_0618"
    rin "\"The feather fluttered all the way into a nearby stream. So what does she do but jump in after it.\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0619"
    rin "\"And... by the time I caught up with her, she was holding the feather, red in the face. The end.\""

    show fumi 1 sm school_scarf h
    show hina 3 sm light pyjama i
    with dict_dissolve_25

    voice "HIN_0788"
    hina "\"Eheheh...\""

    show rin 1 sm pyjama glasses g with dict_dissolve_25

    voice "RIN_0620"
    rin "\"Don't you 'eheheh' me. You weren't at 100%% in the first place, so what were you expecting to happen when you got yourself soaked in this cold?\""

    show hina 3 sm light pyjama f with dict_dissolve_25

    voice "HIN_0789"
    hina "\"...Sorry.\""

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "FUM_0583"
    fumi "\"Hina...\""

    voice "HIN_0790"
    hina "\"The feather got a little dirty... sorry.\""

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "FUM_0584"
    fumi "\"I don't care about that!\""

    "Fumi clutched Hina's hands."

    voice "FUM_0585"
    fumi "\"...Why did you go that far?\""

    show hina 3 sm light pyjama d with dict_dissolve_25

    voice "HIN_0791"
    hina "\"Well, 'cause... it's important to you...\""

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "FUM_0586"
    fumi "\"Your... health is... more important to me.\""

    "Fumi was starting to tear up, but then she gasped."

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0587"
    fumi "\"H-Have you been to the doctor's?\""

    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "RIN_0621"
    rin "\"It's Sunday. Nowhere's open.\""

    show fumi 1 sm school_scarf j with dict_dissolve_25

    voice "FUM_0588"
    fumi "\"What about medicine?\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0622"
    rin "\"I just gave her some I got from Sachiko. But her fever's not going down.\""

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "FUM_0589"
    fumi "\"U-Umm... wh-what should I do?\""

    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "RIN_0623"
    rin "\"Nothing for now, I think.\""

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "FUM_0590"
    fumi "\"But...\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0624"
    rin "\"I know you're worried, but calm down, Asou.\""

    voice "FUM_0591"
    fumi "\"But it's my fault—\""

    show rin 1 sm pyjama glasses g
    show hina 3 sm light pyjama g
    with dict_dissolve_25

    $ voice2("hina","HIN_0792","rin","RIN_0625")
    hina_rin "\"It's not!\""

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "FUM_0592"
    fumi "\"......\""

    show hina 3 sm light pyjama d with dict_dissolve_25

    voice "HIN_0793"
    hina "\"It's not... your fault.\""

    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "RIN_0626"
    rin "\"It's not. This idiot brought it all on herself.\""

    show hina 3 sm light pyjama h with dict_dissolve_25

    voice "HIN_0794"
    hina "\"U... Ungh...\""

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "RIN_0627"
    rin "\"If her fever's not down by tomorrow, I'll get Sachiko to call a doctor.\""

    show rin 1 sm pyjama glasses h with dict_dissolve_25

    voice "RIN_0628"
    rin "\"We can take turns changing this wet towel until then, okay?\""

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0593"
    fumi "\"R-Right! Of course.\""

    show hina 3 sm light pyjama f with dict_dissolve_25

    voice "HIN_0795"
    hina "\"Haha, sorry...\""

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "FUM_0594"
    fumi "\"No...\""

    "Fumi shook her head."

    show hina 3 sm light pyjama i with dict_dissolve_25

    voice "HIN_0796"
    hina "\"I'm a little tired... mind if I sleep?\""

    voice "FUM_0595"
    fumi "\"P-Please... rest well.\""

    show hina 3 sm light pyjama a with dict_dissolve_25

    voice "HIN_0797"
    hina "\"...Good night.\""

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "FUM_0596"
    fumi "\"Good night...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou1_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
