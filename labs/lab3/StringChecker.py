Proteindict_ = {
"AUG" : "Met", "CCG" : "Pro", "CAA" : "Gin",
"UCU" : "Ser", "GUU" : "Val", "CAC" : "His",
"GCA" : "Ala", "CUC" : "Leu", "AUG" : "Met",
"UGU" : "Cys"
}

DNA = True

inputCode = raw_input("Enter a String of DNA, RNA or Protein: ")
#print inputCode.upper()
def DNAStringCheck (inputCode):
    print "DNA: ",
    if inputCode.upper().find("T") == -1:
        print "No"
        DNA = False

    else:
        print "Yes"
        DNA = True

def RNAStringCheck (inputCode):
    print "RNA: ",
    if inputCode.upper().find("U") == -1:
        print "No"

    else:
        print "Yes"

def ProteinStringCheck (inputCode):
    print "Protein: ",
    for c in Proteindict_:
        if inputCode.upper().find(c) == Proteindict_:
            ProteinFinder = False
        else:
            ProteinFinder = True
            break
            if ProteinFinder == True:
                print "Yes"
            #else :
                print "No"


DNAStringCheck(inputCode.upper())
RNAStringCheck(inputCode.upper())
ProteinStringCheck(inputCode.upper())

if DNA == False:
    Protein(inputCode.upper())
#else:
#    print "Protein: "
