import json
from .utils import NumberConvertor


class Cardinal(NumberConvertor):
    def __init__(self):
        self._load_static()

    def _load_static(self):
        with open("data/cardinal.json") as f:
            data = json.load(f)

        for k, v in data.items():
            setattr(self, k, v)

        self.cases = [
            "nominative",
            "genitive",
            "dative",
            "accusative",
            "ablative",
            "prepositional",
        ]

    def _add_postfix(self, word: str, prefix: str, list_postfix: list) -> dict:
        result = {}
        for postfix, case in zip(list_postfix, self.cases):
            result[case] = prefix + postfix if postfix else word
        return result

    def get_cases(self, number: int, gender: str = "male") -> list:
        num_str = str(number)

        if word := (self.words | self.exponents).get(num_str):
            if predcal := self.precalculated.get(word):
                if predcal.get("male"):
                    return predcal[gender]
                else:
                    return predcal

            elif number >= 5 and number <= 20 or number == 30:
                prefix = word[0:-1]
                return self._add_postfix(word, prefix, ["", "и", "и", "", "ью", "и"])

            elif number in [40, 90, 100]:
                prefix = word if number == 40 else word[0:-1]
                return self._add_postfix(word, prefix, ["", "а", "а", "", "а", "а"])

            elif number >= 50 and number <= 80:
                prefix = word[0:-1]
                return self._add_postfix(
                    word,
                    prefix,
                    ["ьдесят", "идесяти", "идесяти", "ьдесят", "ьюдесятью", "идесяти"],
                )

            elif number in [300, 400]:
                prefix = word[0:-4]
                list_prefix = ["", "ехсот", "емстам", "", "eмястами", "ехстах"]
                if number == 400:
                    list_prefix[4] = "ьмястами"
                return self._add_postfix(word, prefix, list_prefix)

            elif number >= 500 and number <= 900:
                prefix = word[0:-4]
                return self._add_postfix(
                    word, prefix, ["", "исот", "истам", "", "ьюстами", "истах"]
                )

            elif self.exponents.get(number):
                pass

    def get_case(self, number: int, gender: str, case: str) -> str:
        pass
