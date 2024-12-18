a,b,c,_,program = [ i.split(": ")[-1] for i in open("17.txt","r").read().splitlines() ]
a,b,c = int(a), int(b), int(c)
program = [ int(i) for i in program.split(",") ]

# part 1

class Computer:
    def __init__(self,A,B,C,program):
        self.A = A
        self.B = B
        self.C = C
        self.pointer = 0
        self.program = program
        self.output = []
        self.run()

    def __str__(self):
        return f"A: {self.A}, B: {self.B}, C: {self.C}, pointer: {self.pointer}"
    
    def get_output(self):
        return ",".join([ str(i) for i in self.output ])

    def combo(self,x):
        if not 0 <= x < 7: raise Exception(f"Invalid combo operand {x}")
        if x <= 3: return x
        if x == 4: return self.A
        if x == 5: return self.B
        if x == 6: return self.C
    
    def adv(self,x): self.A = self.A // (2 ** self.combo(x))

    def bxl(self,x): self.B = self.B ^ x

    def bst(self,x): self.B = self.combo(x) % 8

    def jnz(self,x):
        if self.A != 0: self.pointer = x - 2

    def bxc(self,x): self.B = self.B ^ self.C

    def out(self,x): self.output.append(self.combo(x) % 8)

    def bdv(self,x): self.B = self.A // (2 ** self.combo(x))

    def cdv(self,x): self.C = self.A // (2 ** self.combo(x))

    def instruction(self,opcode,operand):
       if opcode == 0: self.adv(operand)
       elif opcode == 1: self.bxl(operand)
       elif opcode == 2: self.bst(operand)
       elif opcode == 3: self.jnz(operand)
       elif opcode == 4: self.bxc(operand)
       elif opcode == 5: self.out(operand)
       elif opcode == 6: self.bdv(operand)
       elif opcode == 7: self.cdv(operand)
       else: raise Exception(f"Invalid opcode {opcode}")

    def run(self):
        while self.pointer < len(self.program):
            self.instruction(opcode = self.program[self.pointer], operand = self.program[self.pointer+1])
            self.pointer += 2

part1 = Computer(a,b,c,program).get_output()
print(part1)

# part 2

import random

def combine(arr):
    result = 0
    for i,x in enumerate(arr): result = (x << i*3) | result
    return result

class GeneticCandidate:
    def __init__(self, n, parents=None):
        if parents:
            self.chromosomes = self.get_random_child(parents,4)
        else:
            self.chromosomes = self.get_random()

        self.fitness = self.get_fitness()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __str__(self):
        return f"{str(combine(self.chromosomes))}: {str(self.fitness)} {str(self.chromosomes)}"
    
    def get_random(self):
        return [random.randint(0, 7) for _ in range(program_size)]
    
    def get_random_child(self,parents,mutations):
        crossover_point = random.randint(1, program_size-2)
        chromosomes = parents[0].chromosomes[:crossover_point] + parents[1].chromosomes[crossover_point:]
        for i in random.sample(range(0, program_size), mutations): chromosomes[i] = random.randint(0, 7)
        return chromosomes
    
    def get_fitness(self):
        score = 0
        computer = Computer(combine(self.chromosomes),b,c,program)
        if len(computer.output) != program_size: return score
        for i in range(program_size):
            if computer.output[i] == computer.program[i]:
                score += 1
        return score

def get_best_two(candidates):
    best = candidates[0]
    second_best = candidates[1]
    if best < second_best:
        best, second_best = second_best, best
    for i in range(2,pool_size):
        next = candidates[i]
        if next > best:
            best, second_best = next, best
        elif next > second_best:
            second_best = next
    return best, second_best

pool_size = 10000
program_size = len(program)
parents = None

solutions = set()
for i in range(50):
    # print(f"gen {i}")
    candidates = [ GeneticCandidate(program_size,parents) for i in range(pool_size) ]
    parents = get_best_two(candidates)
    for p in parents:
        if p.fitness == 16: solutions.add(combine(p.chromosomes))
    if len(solutions) == 2: break

if solutions:
    part2 = min(solutions)
    print(part2)
else:
    print("Did not find genetic solution for part 2, run again!")
