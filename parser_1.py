from lexical import lexical_analyzer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0
        self.error = False

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.consume()
        else:
            self.error = True

    def consume(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def parse(self):
        self.current_token = self.tokens[self.index]
        self.operasi()

        if self.current_token is not None:
            self.error = True

        if self.error:
            return False
        else:
            return True

    def operasi(self):
        self.term()
        self.operasi_loop()

    def operasi_loop(self):
        if self.current_token in [3, 4, 5, 6, 7]:
            self.operator()
            self.term()
            self.operasi_loop()

    def term(self):
        self.faktor()
        self.term_loop()

    def term_loop(self):
        if self.current_token == 4:
            self.operator_minus()
            self.faktor()
            self.term_loop()

    def faktor(self):
        if self.current_token in [1,2]:
            self.operan()
        elif self.current_token == 9:
            self.grup()
        elif self.current_token == 8:
            self.absolut()
        else:
            self.error = True

    def operan(self):
        self.match(self.current_token)

    def grup(self):
        self.match(9)
        self.operasi()
        self.match(10)

    def absolut(self):
        self.match(8)
        self.operasi()
        self.match(8)

    def operator(self):
        if self.current_token in [3, 4, 5, 6, 7]:
            self.match(self.current_token)
        else:
            self.error = True

    def operator_minus(self):
        self.match(4)

    def operator_minus(self):
        self.match(4)

# Formula input
#input_formula = "123 + 234 - 1.234 x | -576 |"

# Analisis leksikal
#output_tokens = lexical_analyzer(input_formula)
#print("Input: ", input_formula)
#print("Output (Lexical):", " ".join(str(token) for token in output_tokens))

# Analisis sintaksis
#parser = Parser(output_tokens)
#print(parser.parse())
