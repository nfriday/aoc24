input = open("05.txt", "r").read()

rules, pageset = [ i.splitlines() for i in input.split("\n\n") ]
rules = [ rule.split("|") for rule in rules ]
pageset = [ pages.split(",") for pages in pageset ]

# part 1

def in_order(pages,rules):
    for rule in rules:
        try:
            first, second = [ pages.index(j) for j in rule ]
        except ValueError:
            continue

        if first > second: return False
    return True

part1 = sum([ int(pages[len(pages) // 2]) for pages in pageset if in_order(pages, rules) ])
print(part1)

# part 2

def middle_of_ordered_pages(pages,rules):
    valid_rules = [ rule for rule in rules if len([i for i in rule if i in pages]) == len(rule) ]
    
    for page in pages:
        if len([i for i in valid_rules if i[0] == page]) == len(pages) // 2: return int(page)

    raise Exception("if we get here my assumption about the rules is wrong")

part2 = sum([ middle_of_ordered_pages(pages,rules) for pages in pageset if not in_order(pages,rules) ])
print(part2)