import re

def apply(rules, inp):
    molecules = set()
    for [lhs, rhs] in rules:
        for i in range(len(inp) - len(lhs) + 1):
            if inp[i:(i + len(lhs))] == lhs:
                new = inp[:i] + rhs + inp[(i + len(lhs)):]
                molecules.add(new)
    return molecules

# Transforms a CFG to Chomsky-Normal-Form

def nonterminals(cfg):
    return set([lhs for [lhs, _] in cfg])

def terminals(cfg):
    nons = nonterminals(cfg)
    return set([tok for [_, rhs] in cfg for tok in rhs if tok not in nons])

counter = 0

def fresh_nonterminal():
    global counter
    counter += 1
    return f'__{counter}'

# Eliminate start from right-hand sides
def trans_start(cfg, start):
    s0 = fresh_nonterminal()
    return (s0, cfg + [[s0, [start]]])

# Eliminate rules with nonsolitary terminals
def trans_term(cfg):
    terms = terminals(cfg)
    new = []
    for [lhs, rhs] in cfg:
        new_rhs = []
        for tok in rhs:
            if tok in terms:
                n = fresh_nonterminal()
                new.append([n, [tok]])
                new_rhs.append(n)
            else:
                new_rhs.append(tok)
        new.append([lhs, new_rhs])
    return new

# Eliminate right-hand-sides with more than 2 nonterminals
def trans_bin(cfg):
    new = []
    for [lhs, rhs] in cfg:
        remaining = list(rhs)
        while len(remaining) > 2:
            tok2 = remaining.pop()
            tok1 = remaining.pop()
            n = fresh_nonterminal()
            new.append([n, [tok1, tok2]])
            remaining.append(n)
        new.append([lhs, remaining])
    return new

# We skip epsilon rules, since the given grammars do not contain them

# Eliminate unit rules
def trans_unit(cfg):
    nons = nonterminals(cfg)
    new = []
    for [lhs, rhs] in cfg:
        transitive = rhs
        while len(transitive) == 1 and transitive[0] in nons:
            transitive = [r for [l, r] in cfg if l == transitive[0]][0]
        new.append([lhs, transitive])
    return new

# Convert to Chomsky-Normal-Form
def to_cnf(cfg, start):
    cnf = cfg
    s0, cnf = trans_start(cnf, start)
    cnf = trans_term(cnf)
    cnf = trans_bin(cnf)
    cnf = trans_unit(cnf)
    return (s0, cnf)

# Solves part 2 by parsing the given (tokenized) string using the
# CYK-algorithm and outputting the number of edges in the parse tree
# (all nodes starting with an underscore have been created during CNF
# generation and are not considered in the sum).
def cyk(cnf, inp, start):
    def value(tok):
        return 0 if tok.startswith('__') else 1

    # Source: https://en.wikipedia.org/wiki/CYK_algorithm
    # The table used to store intermediate results
    # Each cell has the type {string: int} where the value
    # represents the sum and key the nonterminal
    table = [[dict() for j in range(len(inp))] for i in range(len(inp))]
    for (i, tok) in enumerate(inp):
        table[0][i] = {lhs: 0 for [lhs, rhs] in cnf if rhs == [tok] or lhs == tok}
    for l in range(2, len(inp) + 1): # length of span
        print('at', l)
        for s in range(1, len(inp) - l + 2): # start of span
            for p in range(1, l): # partition of span
                for [a, rhs] in cnf:
                    if len(rhs) == 2:
                        [b, c] = rhs
                        if b in table[p - 1][s - 1] and c in table[l - p - 1][s + p - 1]:
                            table[l - 1][s - 1][a] = value(a) + table[p - 1][s - 1][b] + table[l - p - 1][s + p - 1][c]
    return 1 + table[-1][0][start]

def main():
    with open('resources/day19.txt', 'r') as f:
        [first, inp] = [p.strip() for p in f.read().split('\n\n') if p.strip()]
        rules = re.findall(r'(\w+) => (\w+)', first)
        print(f'Part 1: {len(apply(rules, inp))}')
        def tokenize(s):
            return re.findall('[A-Z][a-z]*', s)
        cfg = [[lhs, tokenize(rhs)] for [lhs, rhs] in rules]
        start = 'e'
        _, cnf = to_cnf(cfg, inp)
        print(f'Part 2: {cyk(cnf, tokenize(inp), start)}')

if __name__ == "__main__":
    main()
