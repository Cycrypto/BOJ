import sys

def count_words(line):
    cnt = 0
    for tok in line.split():
        for ch in tok:
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
                cnt += 1
                break
    return cnt

def has_holy_grail_subseq(line):
    target = "theholygrail"
    j = 0
    for ch in line.lower():
        if j < len(target) and ch == target[j]:
            j += 1
            if j == len(target):
                return True
    return False

def cap_first_token(tok):
    return tok[:1].upper() + tok[1:] if tok else tok

class TauntBot:
    def __init__(self):
        self.cnt = {}
        self.taunt_alts = (0, 1, 2, 0)
        self.sentence_alts = (0, 1, 2)
        self.modified_noun_alts = (0, 1)
        self.modifier_alts = (0, 1)
        self.present_person = ("steed", "king", "first-born")
        self.past_person = ("mother", "father", "grandmother", "grandfather", "godfather")
        self.nouns = ("hamster", "coconut", "duck", "herring", "newt",
                      "peril", "chicken", "vole", "parrot", "mouse", "twit")
        self.present_verb = (("is",), ("masquerades", "as"))
        self.past_verb = ("was", "personified")
        self.adjectives = ("silly", "wicked", "sordid", "naughty",
                           "repulsive", "malodorous", "ill-tempered")
        self.adverbs = ("conspicuously", "categorically", "positively",
                        "cruelly", "incontrovertibly")

    def _choose(self, sym, options):
        k = self.cnt.get(sym, 0) + 1
        self.cnt[sym] = k
        return options[(k - 1) % len(options)]

    def expand_taunt_units(self):
        alt = self._choose("taunt", self.taunt_alts)
        if alt == 0:
            return [self.expand_sentence()]
        if alt == 1:
            units = self.expand_taunt_units()
            units.append(self.expand_sentence())
            return units
        noun = self.expand_noun()
        return [[noun + "!"]]

    def expand_sentence(self):
        alt = self._choose("sentence", self.sentence_alts)
        if alt == 0:
            return self.expand_past_rel() + self.expand_noun_phrase()
        if alt == 1:
            return self.expand_present_rel() + self.expand_noun_phrase()
        return self.expand_past_rel() + ["a", self.expand_noun()]

    def expand_noun_phrase(self):
        return ["a"] + self.expand_modified_noun()

    def expand_modified_noun(self):
        alt = self._choose("modified-noun", self.modified_noun_alts)
        if alt == 0:
            return [self.expand_noun()]
        return self.expand_modifier() + [self.expand_noun()]

    def expand_modifier(self):
        alt = self._choose("modifier", self.modifier_alts)
        if alt == 0:
            return [self.expand_adjective()]
        return [self.expand_adverb(), self.expand_adjective()]

    def expand_present_rel(self):
        return ["your", self.expand_present_person()] + list(self.expand_present_verb())

    def expand_past_rel(self):
        return ["your", self.expand_past_person(), self.expand_past_verb()]

    def expand_present_person(self):
        return self._choose("present-person", self.present_person)

    def expand_past_person(self):
        return self._choose("past-person", self.past_person)

    def expand_noun(self):
        return self._choose("noun", self.nouns)

    def expand_present_verb(self):
        return self._choose("present-verb", self.present_verb)

    def expand_past_verb(self):
        return self._choose("past-verb", self.past_verb)

    def expand_adjective(self):
        return self._choose("adjective", self.adjectives)

    def expand_adverb(self):
        return self._choose("adverb", self.adverbs)

def format_units_to_line(units):
    tokens = []
    for unit in units:
        if unit:
            unit = list(unit)
            unit[0] = cap_first_token(unit[0])
            tokens.extend(unit)
    return " ".join(tokens)

def main():
    bot = TauntBot()
    lines = sys.stdin.read().splitlines()
    out = []
    for raw in lines:
        clean = " ".join(raw.split())
        out.append(f"Knight: {clean}")
        need = (count_words(raw) + 2) // 3
        done = 0
        if has_holy_grail_subseq(raw):
            out.append("Taunter: (A childish hand gesture).")
            done += 1
        while done < need:
            units = bot.expand_taunt_units()
            out.append("Taunter: " + format_units_to_line(units) + ".")
            done += len(units)
        out.append("")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()