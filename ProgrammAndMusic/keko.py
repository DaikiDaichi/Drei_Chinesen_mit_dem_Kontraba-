import playsound


def ersetzterText(zeichenAlt, zeichenNeu, text):
    textNeu = ''
    for zeichen in text:
        if zeichen == zeichenAlt:
            textNeu = textNeu + zeichenNeu
        else:
            textNeu = textNeu + zeichen
    return textNeu


def ersetzterText_v2xd(zeichenAlt, zeichenNeu, text):
    textNeu = ''
    skipnext = False
    for i in range(len(text)):
        if skipnext:
            skipnext = False
            continue
        if i + 1 >= len(text):
            continue
        a = text[i] + text[i + 1]
        if a == zeichenAlt:
            skipnext = True
            textNeu = textNeu + zeichenNeu
        else:
            textNeu = textNeu + text[i]
    return textNeu


# ======================================================================================================================

text = "Drei Chinesen mit dem Kontrabaß.\n" \
       "Saßen auf der Straße und erzählten sich was. Da kam ein Polizist:\n" \
       "Ja was ist denn das?\n" \
       "Drei Chinesen mit dem Kontrabaß."

# ======================================================================================================================

vokale = ("a", "e", "i", "o", "u")

for i in vokale:
    print(text, "\n")
    text = ersetzterText("e", i, text)
    text = ersetzterText("i", i, text)
    text = ersetzterText("ä", i, text)
    text = ersetzterText("a", i, text)
    text = ersetzterText("u", i, text)
    text = ersetzterText("o", i, text)

    if i + i in text:
        text = ersetzterText_v2xd(i + i, i, text)

playsound.playsound("Musik-Konta/Drei Chinesen mit dem Kontrabass - Kinderlieder zum Mitsingen _ Sing Kinderlieder.mp3")
