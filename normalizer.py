from sys import exit as Die
try:
    import sys
    import json
except ImportError as err:
    Die(err)


class Normalizer:

    def algorithm(self, alg, language):
        with open('solve-manual.json') as f:
            manual = json.load(f)
        solution = []
        for notation in alg.split(' '):
            solution.append(manual[language][notation])
        return solution


normalize = Normalizer()
