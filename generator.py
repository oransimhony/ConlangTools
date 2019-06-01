import random

sounds = {"C": "m.n.ng.p.b.t.d.k.g.q.qh.'.f.v.s.z.x.gh.xh.rh.h.l.y.wh.w.r", "V": "a.o.e.i.u.aa.ee.ii.oo.uu"}
syllables = ["CV"]
lengths = []
max_syllable_length = 3
for i in range(max_syllable_length, 0, -1):
    for j in range(i):
        lengths.append(max_syllable_length - i + 1)


def random_syllable():
    return random.choice(syllables)


def random_word():
    word = ""
    syllable = ""
    number_of_syllables = random.choice(lengths)
    for i in range(number_of_syllables):
        syllable += random_syllable()
    for group in syllable:
        sound = random.choice(sounds[group].split("."))
        word += sound
    return word


def main():
    text = ""
    max_sentence_length = random.randint(3, 9)
    sentence_length = 0
    for i in range(1000):
        text += random_word() + " "
        sentence_length += 1
        if sentence_length > max_sentence_length:
            text = text[:-1] + random.choice([".", ".", ".", ".", "?", "!"]) + "\n"
            sentence_length = 0
            max_sentence_length = random.randint(3, 9)
    if text[-1] == "\n":
        text = text[:-1]
    else:
        text = text[:-1] + random.choice([".", ".", ".", ".", "?", "!"])
    print(text)


if __name__ == '__main__':
    main()
