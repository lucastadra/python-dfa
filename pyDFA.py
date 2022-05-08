class DFA:

    def __init__(self, s):
        self.s = s
        self.state = ""
        self.q0(s, 0)
        self.valid = self.checkState()

    def q1(self, s, i):
        self.state += "1->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q2(self, s, i):
        self.state += "2->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)
    
    def q3(self, s, i):
        self.state += "3->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)
    
    def q4(self, s, i):
        self.state += "4->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)
    
    def q5(self, s, i):
        self.state += "5->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q6(self, s, i):
        self.state += "6->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q7(self, s, i):
        self.state += "7->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q8(self, s, i):
        self.state += "8->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q9(self, s, i):
        self.state += "9->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q10(self, s, i):
        self.state += "10->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q11(self, s, i):
        self.state += "11->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q12(self, s, i):
        self.state += "12->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q13(self, s, i):
        self.state += "13->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q14(self, s, i):
        self.state += "14->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q15(self, s, i):
        self.state += "15->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q16(self, s, i):
        self.state += "16->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q17(self, s, i):
        self.state += "17->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q18(self, s, i):
        self.state += "18->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q19(self, s, i):
        self.state += "19->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q20(self, s, i):
        self.state += "20->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q21(self, s, i):
        self.state += "21->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q22(self, s, i):
        self.state += "22->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q23(self, s, i):
        self.state += "23->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q24(self, s, i):
        self.state += "24->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q25(self, s, i):
        self.state += "25->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def q26(self, s, i):
        self.state += "26->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1) 

    def q0(self, s, i):
        self.state += "0->"
        # Condition to check end of string
        if (i == len(s)):
            return
        
        if (s[i] == 'a'):
           self. q1(s, i + 1)
        elif (s[i] == 'b'):
           self. q2(s, i + 1)
        elif (s[i] == 'c'):
           self. q3(s, i + 1)
        elif (s[i] == 'd'):
           self. q4(s, i + 1)
        elif (s[i] == 'e'):
           self. q5(s, i + 1)
        elif (s[i] == 'f'):
           self. q6(s, i + 1)
        elif (s[i] == 'g'):
           self. q7(s, i + 1)
        elif (s[i] == 'i'):
           self. q8(s, i + 1)
        elif (s[i] == 'l'):
           self. q9(s, i + 1)
        elif (s[i] == 'r'):
            self.q10(s, i + 1)
        elif (s[i] == 's'):
            self.q11(s, i + 1)
        elif (s[i] == 't'):
            self.q12(s, i + 1)
        elif (s[i] == 'u'):
            self.q13(s, i + 1)
        elif (s[i] == 'v'):
            self.q14(s, i + 1)
        elif (s[i] == 'w'):
            self.q15(s, i + 1)
        elif (s[i] == '_'):
            self.q16(s, i + 1)
        elif (s[i] == 'o'):
            self.q17(s, i + 1)
        elif (s[i] == 'k'):
            self.q18(s, i + 1)
        elif (s[i] == 'h'):
            self.q19(s, i + 1)
        elif (s[i] == 'n'):
            self.q20(s, i + 1)
        elif (s[i] == 'm'):
            self.q21(s, i + 1)
        elif (s[i] == 'x'):
            self.q22(s, i + 1)
        elif (s[i] == 'z'):
            self.q23(s, i + 1)
        elif (s[i] == 'y'):
            self.q24(s, i + 1)
        elif (s[i] == 'p'):
            self.q25(s, i + 1)
        elif (s[i] == 'P'):
            self.q26(s, i + 1)

    def checkState(self):
        string = ""
        # print(self.state)
        if (self.state == '0->1->13->12->17->'): #auto
            string = "auto"
        elif (self.state == '0->2->10->5->1->18->'): #break
            string = "break"
        elif (self.state == '0->3->1->11->5->'):
            string = "case"
        elif (self.state == '0->3->19->1->10->'):
            string = "char"
        elif (self.state == '0->3->17->20->11->12->'):
            string = "const"
        elif (self.state == '0->3->17->20->12->8->20->13->5->'):
            string = "continue"
        elif (self.state == '0->4->5->6->1->13->9->12->'):
            string = "default"
        elif (self.state == '0->4->17->'):
            string = "do"
        elif (self.state == '0->4->17->13->2->9->5->'):
            string = "double"
        elif (self.state == '0->5->9->11->5->'):
            string = "else"
        elif (self.state == '0->5->20->13->21->'):
            string = "enum"
        elif (self.state == '0->5->22->12->5->10->20->'):
            string = "extern"
        elif (self.state == '0->6->9->17->1->12->'):
            string = "float"
        elif (self.state == '0->6->17->10->'):
            string = "for"
        elif (self.state == '0->7->17->12->17->'):
            string = "goto"
        elif (self.state == '0->8->6->'):
            string = "if"
        elif (self.state == '0->8->20->12->'):
            string = "int"
        elif (self.state == '0->9->17->20->7->'):
            string = "long"
        elif (self.state == '0->10->5->7->8->11->12->5->10->'):
            string = "register"
        elif (self.state == '0->10->5->12->13->10->20->'):
            string = "return"
        elif (self.state == '0->11->19->17->10->12->'):
            string = "short"
        elif (self.state == '0->11->8->7->20->5->4->'):
            string = "signed"
        elif (self.state == '0->11->8->23->5->17->6->'):
            string = "sizeof"
        elif (self.state == '0->11->12->1->12->8->3->'):
            string = "static"
        elif (self.state == '0->11->12->10->13->3->12->'):
            string = "struct"
        elif (self.state == '0->11->15->8->12->3->19->'):
            string = "switch"
        elif (self.state == '0->12->24->25->5->4->5->6->'):
            string = "typedef"
        elif (self.state == '0->13->20->8->17->20->'):
            string = "union"
        elif (self.state == '0->13->20->11->8->7->20->5->4->'):
            string = "unsigned"
        elif (self.state == '0->14->17->8->4->'):
            string = "void"
        elif (self.state == '0->14->17->9->1->12->8->9->5->'):
            string = "volatile"
        elif (self.state == '0->15->19->8->9->5->'):
            string = "while"
        elif (self.state == '0->16->26->1->3->18->5->4->'):
            string = "_Packed"
        else:
            return 0
            
        # print (string)
        return string

# Driver Code
if __name__ == "__main__" :
    s = "while"
    dfa = DFA(s)
     