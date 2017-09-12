inputCode = raw_input("Input DNA String containing the letters 'ACGT': ")

inputCode = inputCode.upper()

replaced_inputCode = inputCode.replace('T', 'a', 1000)
replaced_inputCode_2 = replaced_inputCode.replace('A', 't', 1000)
replaced_inputCode_3 = replaced_inputCode_2.replace('G', 'c',1000)
replaced_inputCode_4 = replaced_inputCode_3.replace('C', 'g', 1000)
print replaced_inputCode_4[::-1].upper()
