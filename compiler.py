REGISTERS = {
    "r0": "0x00000",
    "r1": "0x00020",
    "r2": "0x00040",
    "r3": "0x00060",
    "r4": "0x00080",
    "r5": "0x000A0",
    "r6": "0x000C0",
    "r7": "0x000E0",
    "r8": "0x00100",
    "r9": "0x00120",
    "r10": "0x00140"
}

OPS = {'ADD': '0001', 'SUB': '0010', 'NEG': '0011', 'SL': '0100', 'OR': '0101', 'B': '0110',
       'CMP': '0111', 'BE': '1000', 'BGE': '1001', 'MOVI': '1010', 'MOV': '1011', 'STR': '1100', 'LDR': '1101'}


def findBranches(text):
    lines = text.split("\n")
    branches = {}
    for (i, l) in enumerate(lines):
        if (":" in l):
            branches[l[:-1]] = i

    return branches


file = open("program.txt")
text = file.read()
BRANCHES = findBranches(text)

lines = text.split("\n")
for (i, l) in enumerate(lines):
    instr = l.split(" ")[0]
    params = "".join(l.split(" ")[1:]).split(",")
    if(not OPS.get(instr)):
        print("OP NOT RECOGNIZED => "+str(i))
        continue
    result = "OP"+OPS[instr]
    for p in params:
        if (p.isnumeric()):
            result += "-I{:08b}".format(int(p))
        elif (type(p) == str and p in REGISTERS.keys()):
            result += "-R{:08b}".format(int(REGISTERS[p], 16))
        elif (type(p) == str):
            result += "-B{:08b}".format(BRANCHES[p])
    print(result)

print()
