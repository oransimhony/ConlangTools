# ConlangTools 
Some tools to help oneself while conlanging

# Tools

* [The Generator](#generator)
  * [Generator Example](#generator-example)
  * [Using the Generator](#using-the-generator)

# Generator

Generates texts based on phoneme inventory, syllable structure, syllable length and more.

## Generator Example

Generating a text of 100 words based on these phonemes and syllable structure witha maximum of 3 syllables in a word.

```python
# Configuration Area
sounds = {"C": "m.n.ng.p.b.t.d.k.g.q.qh.'.f.v.s.z.x.gh.xh.rh.h.l.y.wh.w.r", "V": "a.o.e.i.u.aa.ee.ii.oo.uu"}
syllables = ["CV"]
max_number_of_syllables = 3
number_of_words = 100
min_number_of_words_in_sentence = 3
max_number_of_words_in_sentence = 9
# Configuration Area
```

```txt
qhawha ta xiibungu voo'uwoo ngipiiwhii hooxhuu rhuu.
fuu bookuru fo so.
qawhi taawhaa whiite go me xhe whaaxhodaa.
tii'oo xo qhanu fiireeghuu xhiwuu gho 'ooghuu ro?
wa wii hiiqhaqii qhupa ghe ludaa ghuuquu!
guuge noo davi voorhe suuquruu nuqee.
ro so rha yurhofoo.
rhuu whime hii xhuu.
ngaa yoo teehe repe re du?
rhuumuuqa zaa se dedaaquu ghoquunii xhoghizee bo gi whii'o.
ngaava gha whuumii qhuuhoza si?
ta ngiihu ngongasu boo baagefee ya!
gorhiini waayeqe vu vaaqu ti?
whuuxhii nga fee xii piiye mixhima!
whuu peedeeloo whee kee yaa heka sibii da qheepanaa?
fu yanu ride siideengi suu'ee whoo gii!
```

## Using the Generator

Go the the configuration area in `generator.py` (on the top of the file)

Enter the phonemes of the language you want to generate in the `sounds` variable like this:

`"{group letter}": "{phonemes seperated by a .}"`

**Important**: The group letter must be only one letter

Enter the available syllable sturctures into the `syllables` variable, seperated by a `,`

Choose the maximum number of syllables and enter it in `max_number_of_syllables`

Decide on the number of words you want to have in your text and enter it in `number_of_words`

And last but not least, enter the minimum and maximum number of words in `min_number_of_words_per_sentence` and `max_number_of_words_per_sentence`
accordingly

```python
# Configuration Area
sounds = {"C": "m.n.p.t.k", "V": "a.o.u"}
syllables = ["V", "CV", "CVC"]
max_number_of_syllables = 3
number_of_words = 50
min_number_of_words_per_sentence = 3
max_number_of_words_per_sentence = 5
# Configuration Area
```
