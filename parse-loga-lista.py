from __future__ import annotations

import csv
import os
import re
from typing import Optional


LANGUAGES = ["Engle", "Frans", "Espanya", "Arab", "Hindu", "putung Han", "Nipon"]

WARNINGS: list[Warning] = []


def parse_loga_liste():
    # read the CSV file
    entries = {}
    with open("loga-lista.csv", newline="", encoding="utf-8") as source_file:
        reader = csv.DictReader(source_file, delimiter=',', quotechar='"')
        for row in reader:
            word = row["Unia"].replace("-", "")
            if len(word) > 0 and "?" not in row["Unia"]:
                if word in entries:
                    WARNINGS.append(Warning(10, f'there are two entries for "{word}"'))
                    continue
                entries[row["Unia"]] = row

    # add any parents that aren't explicitly listed
    for word in list(entries.keys()):
        for link in entries[word]["linke"].split(","):
            if is_subword(link, word) and link.replace("-", "") not in entries:
                entries[link.replace("-", "")] = {
                    "Unia": link, "mara-du": entries[word]["mara-du"],
                    "genus": "", "loga-asal": "", "Latine": "", "linke": "",
                    **{language: "" for language in LANGUAGES}
                }
                entries[word]["mara-du"] = 3

    # parse the raw entries and build a word object
    words: dict[str, dict[str, Word]] = {language: {} for language in LANGUAGES}
    for word in entries.keys():
        row = entries[word]
        frequency_class = row["mara-du"]
        pronunciation = infer_pronunciation(word)
        etymology = format_etymology(word, row["loga-asal"])
        parent, children, synonyms = interpret_links(word, row["linke"].split(","))
        word = word.replace("-", "")
        for language in LANGUAGES:
            definitions = parse_definitions(row[language])
            words[language][word] = Word(
                word, frequency_class, pronunciation, etymology,
                parent, children, synonyms,
                definitions)

    # post-process and write the output CSV files
    os.makedirs("generated", exist_ok=True)
    for language in LANGUAGES:
        words[language] = postprocess_dictionary(words[language])

        with open(f"generated/loga-lista-{language.lower().replace(' ', '-')}.csv", "w", newline="", encoding="utf-8") as out_file:
            writer = csv.writer(out_file, delimiter=",", quotechar='"')
            writer.writerow(["Unia", "esfono", "logaasal", "korte forma", "long forma", "sammana", "mana..."])
            for word in words[language].values():
                writer.writerow([
                    word.unia,
                    word.pronunciation,
                    word.etymology,
                    word.parent if word.parent is not None else "",
                    ",".join(word.children),
                    ",".join(word.synonyms),
                    *[f'{part_of_speech},"{definition}"' for part_of_speech, definition in word.definitions],
                ])

    for warning in sorted(WARNINGS)[:36]:
        print("Warning:", warning.message)


def infer_pronunciation(word: str) -> str:
    # spell out numbers
    replacements = [
        (19, "deka-tisa"),
    ]
    for old, new in replacements:
        word = word.replace(str(old), "-" + new + "-")

    # ignore case
    word = word.lower()
    # remove anything in parentheses
    word = re.sub(r"\s*\(.*\)\s*", "", word)
    
    if len(word) == 0:
        return ""

    # handle each root separately
    if " " in word:
        return " ".join(infer_pronunciation(subword) for subword in word.split(" "))

    # apply this special rule that makes ng easier to pronounce
    word = re.sub(r"([aiueoáíúéó])ng([aiueoáíúéó])", r"\1ngg\2", word)
    word = re.sub(r"nk", r"ngk", word)
    # start by treating each letter as potentially a multi-letter string
    letters = [letter for letter in word]
    # consolidate digraphs
    replacements = [
        ("hng", "ŋ̊"),
        ("ng", "ŋ"),
        ("zh", "d͡ʒ"), ("sh", "ʃ"),
        ("gh", "ɣ"), ("th", "θ"), ("dh", "ð"),
        ("hl", "ɬ"), ("hm", "m̥"), ("hn", "n̥"), ("hr", "r̥"),
        ("ts", "t͡s"),
        ("kc", "k͡|"), ("gc", "g͡|"), ("q", "k͡ǃ"), ("gq", "g͡ǃ"),
        ("x", "k͡ǁ"), ("gx", "g͡ǁ"), ("pc", "k͡ʘ"), ("bc", "g͡ʘ"),
        ("ai", "ai̯"), ("ao", "au̯"), ("ei", "ei̯"), ("eu", "eu̯"), ("oi", "oi̯"), ("ou", "ou̯"),
        ("ái", "ái̯"), ("áo", "áu̯"), ("éi", "éi̯"), ("éu", "éu̯"), ("ói", "ói̯"), ("óu", "óu̯"),
        ("c", "t͡ʃ"),
    ]
    for old, _ in replacements:
        for i in range(len(letters) - len(old), -1, -1):
            if letters[i:i + len(old)] == [letter for letter in old]:
                letters = letters[:i] + [old] + letters[i + len(old):]
    # remove any apostrophes that were probably only there to split digraphs, and hyphens
    for i in range(len(letters) - 3, -1, -1):
        if letters[i + 1] == "'" and letters[i][-1] in "zsgtdlmnkgpb" and letters[i][0] in "ghscqx":
            letters = letters[:i + 1] + letters[i + 2:]
    # also remove all hyphens
    for i in range(len(letters) - 1, -1, -1):
        if letters[i] == "-":
            letters = letters[:i] + letters[i + 1:]
    # then apply the replacements
    for old, new in replacements:
        for i in range(len(letters)):
            if letters[i] == old:
                letters[i] = new
    # change some apostraphes to ejectives
    for i in range(len(letters) - 2, -1, -1):
        if letters[i][-1] in "ptkfsʃhɬ|ǁǃʘ" and letters[i + 1] == "'":
            letters = letters[:i] + [letters[i] + "ʼ"] + letters[i + 2:]
    # finally, change remaining apostrophes to glottal stops
    for i in range(len(letters)):
        if letters[i] == "'":
            letters[i] = "ʔ"

    nuclei = [i for i in range(len(letters)) if letters[i][0] in "aeiouáéíóú"]
    if len(nuclei) == 0:
        if len(letters) > 1:
            raise ValueError(f'the word "{word}" has no vowels.')
        else:
            return letters[0]
    syllable_breaks = [0]
    for j in range(1, len(nuclei)):
        syllable_breaks.append((nuclei[j - 1] + nuclei[j] + 1)//2)
    syllable_breaks.append(len(letters))
    syllables = []
    for j in range(len(nuclei)):
        syllables.append("".join(letters[syllable_breaks[j]:syllable_breaks[j + 1]]))
    # place the stress if there is none and there are multiple syllables
    if len(nuclei) > 1 and not re.search(r"[áéíóú]", "".join(syllables)):
        if syllables[-1][-1] in "aeiou":
            stress = -2
        else:
            stress = -1
        for i in range(len(syllables[stress])):
            if syllables[stress][i] in "aeiou":
                stressed_vowel = syllables[stress][i].replace("a", "á").replace("e", "é").replace("i", "í").replace("o", "ó").replace("u", "ú")
                syllables[stress] = syllables[stress][:i] + stressed_vowel + syllables[stress][i + 1:]
                break
    # finally, use periods for syllable breaks
    return ".".join(syllables)


def format_etymology(word: str, etymology: str) -> str:
    if len(etymology) > 0:
        return etymology
    elif "-" in word:
        return word.replace("-", " + ")
    else:
        WARNINGS.append(Warning(4, f'"{word}" has no etymology'))
        return ""


def interpret_links(word: str, links: list[str]) -> tuple[Optional[str], list[str], list[str]]:
    """ get the parent word, if any, the children words, and any unrelated synonyms """
    parent = None
    children = []
    synonyms = []
    for link in links:
        link = link.replace("-", "")
        if link == "":
            continue
        elif is_subword(link, word):  # substrings are interpreted as parents (common shortenings)
            if parent is not None:
                WARNINGS.append(Warning(5, f'"{word}" has multiple parents.'))
            parent = link
        elif is_subword(word, link):  # superstrings are interpreted as lengthenings
            children.append(link)
        else:
            synonyms.append(link)
    return parent, children, synonyms


def parse_definitions(definitions_str: str) -> list[tuple[str, str]]:
    """ get the full list of definitions with their parts of speech """
    if len(definitions_str) == 0:
        return []

    definitions: list[tuple[str, str]] = []  # list of part-of-speech/translation pairs
    for definition in definitions_str.split("; "):
        pos_extraction = re.fullmatch(r"^([^\s]+\.) (.+)", definition)
        if pos_extraction is not None:
            part_of_speech, translation = pos_extraction.groups()
        else:
            if len(definitions) > 0:
                part_of_speech = definitions[-1][0]
            else:
                WARNINGS.append(Warning(1, f'"{definition}" has no part of speech'))
                part_of_speech = "n."
            translation = definition
        definitions.append((part_of_speech, translation))
    return definitions


def postprocess_dictionary(words: dict[str, Word]) -> dict[str, Word]:
    """
    go thru the dicitonary and make sure all compound words are based on real roots,
    make sure all links are bidirectional, fill in any definitions given implicitly thru children,
    put lists in a consistent order, make sure verbs are formatted correctly,
    and localize/validate the origin language and part of speech names.
    """
    for word in words.values():
        # make links bidirectional
        if word.parent is not None:
            if word.unia not in words[word.parent].children:
                words[word.parent].children.append(word.unia)
        for child in word.children:
            words[child].parent = word.unia
        for synonym in word.synonyms:
            if word.unia not in words[synonym].synonyms:
                words[synonym].synonyms.append(word.unia)

        # check compound etymologies
        if " + " in word.etymology:
            for component in word.etymology.split(" + "):
                if component not in words:
                    WARNINGS.append(Warning(3, f'the compound "{word}" is based on the root "{component}", which does not seem to exist'))

    for word in words.values():
        # include implicit definitions
        for child in word.children:
            word.definitions += words[child].definitions
        # sort definitions
        word.definitions = sorted(word.definitions)

    # remove words with no definitions
    words = {key: word for key, word in words.items() if word.definitions}

    return words


def is_subword(subword: str, superword: str) -> bool:
    if subword == "":
        return False
    subword = re.split(r"[- ]", subword)
    superword = re.split(r"[- ]", superword)
    if len(subword) >= len(superword):
        return False
    for subword_component in subword:
        if subword_component not in superword:
            return False
    return True


class Word:
    def __init__(
        self, unia: str, frequency_class: int, pronunciation: str, etymology: str,
        parent: Optional[str], children: list[str], synonyms: list[str],
        definitions: list[tuple[str, str]]
    ):
        self.unia = unia
        self.frequency_class = frequency_class
        self.pronunciation = pronunciation
        self.etymology = etymology
        self.parent = parent
        self.children = children
        self.synonyms = synonyms
        self.definitions = definitions


class Warning:
    def __init__(self, severity: int, message: str):
        self.severity = severity
        self.message = message

    def __lt__(self, other):
        return self.severity > other.severity


if __name__ == "__main__":
    parse_loga_liste()
