# How does it work?

# phonology

the phonology will be largely the same as in Pandunia 2.0 but for some modifications.

- I'm allowing all consonants besides voiced obstruents at the end of a syllable.
- I'm forbidding **eu** and replacing all instances with **yu** or **eo**.
- I'm allowing the clusters **kn** and **gn** for **tekni**, **magnete**, and **jagna**.
- I'm merging **s** with **sh** and **z** with **j**, and changing **ch** to **c**.  this removes the need for digraphs. (or maybe I should lean into digraphs and spell **j** as **zh** (or just do the normal thing and merge sh~ch into ⟨c⟩))
- I'm calling **ng** a consonant.

|           | labial  | coronal    | palatal           | dorsal | 
|-----------|---------|------------|-------------------|--------|
| nasal     | m       |            |                   | ng     |
| stop      | p b     | t d        | c (t͡ʃ~ʃ) j (d͡ʒ~ʒ) | k g    |
| fricative | f       | s z (z~d͡z) |                   | h      |
| glide     | v (w~v) | l r (r~ɹ)  | y (j)             |        |

|       | front | back |
|-------|-------|------|
| close | i     | u    |
| mid   | e     | o    |
| open  | a     |      |

## phonotactics

a syllable is CVC or PLVC.  restrictions apply to medial CC clusters:
- they must differ in manner of articulation (no fricative+fricative, stop+stop, nasal+nasal, or liquid+liquid).
- if the first is a stop, they must differ in place of articulation (or maybe not, I haven't decided)
- if the first is a nasal and the second is a stop, they must agree in place of articulation
- if both are obstruents, they must agree in voicing.
- where three consonants appear in a row, the first one must be a nasal or voiceless fricative

restrictions also apply to the coda consonant.
- it must not be a voiced obstruent
- it must not be a semivowel

also, "y" may not be adjacent to "i", nor "v" adjacent to "u".
all vowel sequences are allowd, but "ei" and "ou" may only be at the end of a word, and "eu" is actually forbidden.
an open or mid vowel followd by a close vowel should ideally be pronounced as a diphthong.
since they will naturally
a syllable can't start with "tl" or "dl".

obviously, any proper name has laxer rules.  it has no phonotactic constraints, including bonus characters.
but semivowels should still be spelld via normal conventions if the source language doesn't use the latin alphabet

Bonus characters: ts (t͡s), tl (t͡ɬ), dl (d͡ɮ), gh (ɣ), th (θ), dh (ð), ' (ʔ), kc (k͡ǀ), gc (ɡ͡ǀ), kx (k͡ǁ), gx (ɡ͡ǁ), kq (k͡ǃ), gq (ɡ͡ǃ), á, é, í, ó, ú (stress)

## stress

Stress falls on the last heavy syllable if such a syllable exists?
Otherwise, it falls on the first syllable?

/gé.o/
/pu.táu̯/
/kris.tál/
/dú.ni.a/
/ká.ri.bu/
/res.to.rán/

## spelling conventions

The following tables describe the standard transcription style of Nibasa.
This is how new words should be respelld when added to the dictionary.
Note that these rules are neither fast nor hard,
and there may be variations when a word comes from a different source,
or from a combination of several.

### Latin

| zi (fon) | tarjum | misal |
|----------|--------|-------|
| c (hard)| k    | |
| c (soft)| s    | |
| ch (kʰ) | k    | |
| g (hard)| g    | |
| g (soft)| g    | |
| i (i~j) | i    | |
| j (j)   | j    | |
| ph (pʰ) | f    | |
| qu (kʷ) | ku?  | |
| s (s)   | s    | |
| s (z)   | z    | |
| th (tʰ) | t    | |
| u (u~w) | u    | |
| v (w)   | v    | |
| x (ks)  | ks   | |
| y (y)   | i    | |
| -um     | -o\* | fero |
| -ium    | -i\*\* | imperi |
| -us     | -o\* | |
| -ius    | -i   | |
| -a      | -a\* | |
| -ia     | -i\*\*\* | famili |
<!-- | -ition  | -i   | |
| -ation  | -a   | dona |
| -ktion  | -k   | frik |
| -ssion  | -t   | tras-mis |
| -sion   | -di  | in-kluz? | -->

\* Nouns describing people and adjectives all take "-e" instead of "-a" or "-o".
\*\* The names of chemical elements for which the "-ium" is universal are suffixed with the dedicated morpheme "ium".
\*\*\* Feminine or Greek "-i" is expanded to "-ia" for words representing places that would otherwise be two syllables.

Generally, "c" is soft when followed by "i", "e", or "y" and hard otherwise.
However, note that Nibasa treats "c" as hard if it derives from a Greek "κ".

Generic suffixes may be omitted entirely if they have been lost in Spanish and Portuguese.


### English

Note that these rules only apply for words that originate from English.
Most words shared between Nibasa and English originally come from Latin, which has its rules above.

| zi (fon) | tarjum | misal |
|----------|--------|-------|
| c (k)   | k    | |
| c (s)   | s    | |
| ch (t͡ʃ) | c    | |
| g (ɡ)   | g    | |
| g (d͡ʒ)  | j    | |
| qu (kw) | ku   | |
| s (s)   | s    | |
| s (z)   | z    | |
| sh (ʃ)  | c?   | |
| th (θ)  | | |
| th (ð)  | | |
| v (v)   | v    | |
| w (w)   | v    | |
| x (ks)  | ks   | |
| a (æ)   | a    | |
| a (ɑ)   | a    | |
| a (eɪ)  | e    | |
| au (ɔ)  | o    | |
| e (ɛ)   | e    | |
| e (iː)  | i    | |
| i (ɪ)   | i    | |
| i (aɪ)  | ai   | |
| o (ɒ)   | o    | |
| o (oʊ)  | o    | |
| oo (uː) | u    | |
| ou (aʊ) | au   | |
| u (ʌ)   | avoid this one at all costs | |
| u (ʊ)   | u    | |
| u (juː) | yu   | |

### Arabic

| zi (fon) | tarjum | misal |
|----------|--------|-------|
| ج (d͡ʒ)  | j    | |
| ه (h)   | h    | |
| ح (ħ)   | h    | |
| ط (tˤ)  | t    | |
| ع (ʕ)   | siro | |
| ص (sˤ)  | s    | |
| ق (q)   | k    | |
| ش (ʃ)   | c    | |
| ث (θ)   | s    | |
| خ (x)   | h    | |
| ذ (ð)   | z    | |
| ض (dˤ)  | d    | |
| ظ (zˤ)  | z    | |
| غ (ɣ)   | g    | |
| ء (ʔ)   | siro | |
| ة-(-at)   | a\* | |

\* a "t" is included in the transliterated word if it would otherwise only be two letters long (e.g. "sat").
Verbs and adverbs should be converted to adjectives or nouns before being transliterated.
Adjectives and nouns describing people are transcribed as feminine.

### Sanskrit

| zi (fon) | tarjum | misal |
|----------|--------|-------|
| (bʰ)    | b    ||
| (p)     | p    ||
| (dʰ)    | d    ||
| (t)     | t    ||
| (ɖʰ)    | d    ||
| (ʈ)     | t    ||
| (d͡ʒʰ)   | j    ||
| (t͡ʃ)    | c    ||
| (ɡʰ)    | g    ||
| (k)     | t    ||
| (ʃ)     | s    ||
|

### Chinese

This table is based on Mandarin, since it's by far the most spoken chinese language,
but the transcription style is based on a consideration of all chinese and Chinese-derived languages.
That, in addition to a desire to maintain spelling, is why retroflex consonants are transcribed as alveolar,
and tenuis occlusive obstruents are transcribed as voiced.
For palatal consonants and final nasals, the spelling depends on the conservative pronunciation,
which is however it's pronounced in Cantonese.

Note that this table does not include stop codas, which are maintained from Old Chinese.

| zi (fon) | tarjum | misal |
|----------|--------|-------|
| b (p)    | b      |       |
| d (t)    | d      |       |
| g (k)    | g      |       |
| h (x)    | h      |       |
| j (k)    | k      |       |
| j (t͡s)   | j      |       |
| q (kʰ)   | k      |       |
| q (t͡sʰ)  | c      |       |
| x (x)    | h      |       |
| x (s)    | s      |       |
| zh (d͡ʐ)  | z      |       |
| ch (t͡ʂʰ) | c      |       |
| sh (ʂ)   | s      |       |
| r (ɻ)    |        |       |
| z (t͡s)   | z      |       |
| c (t͡sʰ)  | c      |       |
| w (w)    | v      |       |

| zi (fon) | tarjum | zi (fon) | tarjum |
| i (ɻ)    |        | i (i)    |        |
| u (u)    |        | ü (y)    |        |
| e (ə)    |        | ie (je)  |        |
| ue (wo)  |        | üe (ɥə)  |        |
| a (a)    |        | ia (ja)  |        |
| ua (wa)  |        |          |        |
| ei (ej)  |        |          |        |
| ui (wej) |        |          |        |
| ai (aj)  |        |          |        |
| uai (waj)|        |          |        |
| ou (ow)  |        | iu (jow) |        |
| ao (aw)  |        | iao (jaw)|        |
| en (ən)  |        | in (in)  |        |
| un (wən) |        | ün (yn)  |        |
| an (an)  |        | ian (jen)|        |
| uan (wan)|        | üan (ɥen)|        |
| eng (əŋ) |        | ing (iŋ) |        |
| ang (aŋ) |        | ianɡ (jaŋ)|       |
| uanɡ (waŋ)|       |          |        |
| ong (uŋ) |        | iong (juŋ)|       |

Some rimes change their vowel to mark the tone in Mandarin

| Cmn.    | Asa. (T1) | Asa. (T2) | Asa. (T3) | Asa. (T4) |
|---------|------|
| en (ən) | part   e  | part  e   | powder o  | o
| en (əm)
| ong (uŋ)| center u  | center u | species o  | species o

# grammar

the grammar will be isolating and use SOV word order, with postpositions to mark nouns instead of articles or word endings.
There will be seven postpositions total:
- ga (nominative)
- ro (accusative)
- do (dative, also marks adverbs)
- ze (ablative)
- na (locative)
- e (instrumental, also additive conjunction)
- o (also alternate conjunction)

- there is no definite article **la** (all nouns are markd by postpositions (tho maybe I should use **al** for this anyway)).
- there is no relative pronoun **jo** or content clause marker **ki** (both are indicated by **di**).
- there is no possessive preposition **da** (only the postposition **di** is needed).
- there is no passive auxiliary **be** (the subject and object are marked with postpositions, so they can be swapd around freely).

in addition, many words that were necessarily function words in Pandunia 2.0 are effectively content words in Nibasa, so you don't need to know their part of speech to parse a sentence.  this includes
- pronouns **mi**, **tu**, and **ye**, which are just normal nouns (**se** merges with **auto**)
- demonstratives **ni**, **go**, **yo**, and **ke**, and quantifiers **un**, **yo**, **eni**, **pan**, which are just adjectives that can also function as nouns (**poli** merges with **ba**)
- auxiliary verbs **si**, **fa**, which are just normal verbs as well as common suffixes (**si** merges with **ta** and **fa** merges with **karma**).

the two main auxiliary verbs will be **ta** and **fa**.  **ta** means "to be", and is used to indicate states, existence, and the progressive aspect.  **fa** means "do", and is used to indicate changes of state, action, and the perfective aspect.

Nibasa verbs are all ambitransitive, so grammatical voice is usually simply implied.
for instance, "" can mean either "cause " or "receive "...
however, there are a handful of suffixes that can indicate voice explicitly: **-fa** is causative, **-get** is passive, **auto-** is reflexive, and **unalo-** is reciprocal.

the three tenses will be **le** (past), **zai** (present), and **sha** (future).  these will most typically be used as adverbs, but can also go at the end of the main verb like **ti** and **fa**.  the suffix **le** in particular is useful for using verbs as adjectives.

the affirmative, negative, and interrogative particles "ya", "no", and "ke" can go before or after the verb.  before is more common.  same as the tense particles.  auxiliary verbs such as "abil" and "amir" must go after.

The basic sentence structures will look like this:

there is an N.
N ga ta.

N1 is N2.  
N1 ga N2 ta.

N1 has N2.  
N1 di N2 ga ta.

N1 V.  
N1 ga V.

N1 V N2.  
N1 ga N2 ro V.

Interrogatives are formed by placing "ke" rite before or after the verb.

