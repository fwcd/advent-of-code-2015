import re

def apply(rules, start):
    molecules = set()
    for [lhs, rhs] in rules:
        for i in range(len(start) - len(lhs) + 1):
            if start[i:(i + len(lhs))] == lhs:
                new = start[:i] + rhs + start[(i + len(lhs)):]
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

def main():
    with open('resources/day19.txt', 'r') as f:
        [first, start] = [p.strip() for p in f.read().split('\n\n') if p.strip()]
        rules = re.findall(r'(\w+) => (\w+)', first)
        print(f'Part 1: {len(apply(rules, start))}')
        cfg = [[lhs, re.findall('[A-Z][a-z]*', rhs)] for [lhs, rhs] in rules]
        print(to_cnf(cfg, 'e'))

if __name__ == "__main__":
    main()
