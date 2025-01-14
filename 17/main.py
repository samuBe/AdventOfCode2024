class Computer:

    def __init__(self, A, B, C, instructions):

        self.A = A
        self.B = B
        self.C = C
        self.instructions = instructions
        self.ip = 0
        

    def __repr__(self):
        return f"A: {self.A},\nB: {self.B},\nC: {self.C},\nIP: {self.ip}"

    def run(self):

        output = []

        while self.ip < len(self.instructions):
            print(self)
            opcode = self.instructions[self.ip]
            literal_operand = self.instructions[self.ip + 1]
            combo_operand = literal_operand
            if literal_operand > 3:
                match literal_operand:
                    case 4:
                        combo_operand = self.A
                    case 5:
                        combo_operand = self.B
                    case 6:
                        combo_operand = self.C

            match opcode:
                case 0:
                    self.A = int(self.A / (2 ** combo_operand))
                case 1:
                    self.B = literal_operand ^ self.B
                case 2:
                    self.B = combo_operand % 8
                case 3:
                    if self.A != 0:
                        self.ip = literal_operand
                        continue
                case 4:
                    self.B = self.C ^ self.B
                case 5:
                    output.append(combo_operand % 8)
                case 6:
                    self.B = int(self.A / (2 ** combo_operand))
                case 7:
                    self.C = int(self.A / (2 ** combo_operand))

            self.ip += 2
        return output


fname = "input.txt"
with open(fname) as f:
    lines = f.readlines()
    _, A = lines[0].split(":")
    A = int(A)
    _, B = lines[1].split(":")
    B = int(B)
    _, C = lines[2].split(":")
    C = int(C)
    _, instructions = lines[4].split(":")
    instructions = list(map(int, instructions.strip().split(',')))
    print(A, B, C, instructions)

    c = Computer(A, B, C, instructions)

    out = c.run()
    print(','.join(map(str, out)))
