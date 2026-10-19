from logic import *# the file of the logic.py wher the logic and methods is based to run this puzzlefile.

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# A is a knight and  knave - #
#sentence = And(AKnight,AKnave)
knowledge0 = And(
    #TODO:
# let p = a knight and q = knave then since A says and express and tell them A is both then:
   Or(AKnight,AKnave),
 #since A said they are both knight and knave so they can be one of the other a knight and a kn
 
    Implication(AKnight,AKnave)# to set and print only A being a both knight and knave
    #p -----> q
)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #TODO
    # A says A and B are both knave, 
    Or(AKnight,AKnave),# from previous claimed Puzzle 0 
    Or(BKnight,BKnave),
 # Making False concept of A being Knight from his previous claimed.
    Not(And(AKnight,AKnave)),
    Not(And(AKnight,AKnave)),
 # Since A says They are Knave then it is false that A is knight and b being knave

    Implication(AKnight,And(AKnave,BKnave)),# telling the truth of that Aknight they are both knave
    Implication(AKnave, Not(And(AKnave,BKnave))),# telling the lie  of that Aknave that they are both knave
     #p -----> q = T and notp ^ -----> q = F 
 # since A is knight these make his claimed of being a knight false and b being knave and A  being Knave true
 #thus making A is Knave and B is Knight
)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    #TODO
 #the general knowledge claimed in previous
    Or(AKnight,AKnave),# from previous claimed Puzzle 0 nd 1
    Or(BKnight,BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),

 # They are the same kind
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
 # Since B is Knight then A is lying that they are both the same kind
 # B claims they are different kinds( mix of knights and knave )
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
) # since A is lying that they ar both knave then B is knight so B is saying the truth

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
 #TODO
 #General Knowldege of prev puzzle just ADDED FOR C 
 # each person cn be a knight or knave
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    # no same person to have (example a is knight and a is knave)
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave)),
# A is knight or A is knave Then, A is knave not A is knave and A is knight not A is knight.
    Implication(AKnight,Or(AKnight,AKnave)), #Either knave or knight
    Implication(AKnave,Not(Or(AKnight,AKnave))), # Lying if A is neither a Knave or Aknight and either a knave or aknight.
# B says that A said I Am a Knave. ( were not sure if A is saying the truth of what a said that A is knave or B is implying the truth that A says that A is the knave one.)
    Or(Implication(BKnight,Or(Implication(AKnight,AKnave),Implication(AKnave,Not(AKnave)))),#This is imply by the Bknight one is true and one is false
    Or(Implication(BKnave,(Not(Or(Implication(AKnight,AKnave),Implication(AKnave,Not(AKnave)))))))),# This is imply by the Bknave one is false and one is true
# B says stated that C is a knave , C is a added var.
    Implication(BKnight,CKnave), # Bknight says that C is knave (Bknight because in prev B is knight)
    Implication(BKnave,Not(CKnave)),
# C also stated that "A is knight".
    Implication(CKnight,AKnight),
    Implication(CKnave,Not(AKnight))
)
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")

if __name__ == "__main__":
    main()
