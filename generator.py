import random

# Configuration Area
sounds = {"C": "m.n.ng.p.b.t.d.k.g.q.qh.'.f.v.s.z.x.gh.xh.rh.h.l.y.wh.w.r", "V": "a.o.e.i.u.aa.ee.ii.oo.uu"}
syllables = ["CV"]
max_number_of_syllables = 3
number_of_words = 100
min_number_of_words_per_sentence = 3
max_number_of_words_per_sentence = 9
# Configuration Area


lengths = []


def init():
    for i in range(max_number_of_syllables, 0, -1):
        for j in range(i):
            lengths.append(max_number_of_syllables - i + 1)


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


def get_sentence_length():
    return random.randint(min_number_of_words_per_sentence, max_number_of_words_per_sentence)


def create_text():
    text = ""
    max_sentence_length = get_sentence_length()
    sentence_length = 0
    for i in range(number_of_words):
        text += random_word() + " "
        sentence_length += 1
        if sentence_length > max_sentence_length:
            text = text[:-1] + random.choice([".", ".", ".", ".", "?", "!"]) + "\n"
            sentence_length = 0
            max_sentence_length = get_sentence_length()
    if text[-1] == "\n":
        text = text[:-1]
    else:
        text = text[:-1] + random.choice([".", ".", ".", ".", "?", "!"])
    return text


def main():
    init()
    text = create_text()
    print(text)


if __name__ == '__main__':
    main()
