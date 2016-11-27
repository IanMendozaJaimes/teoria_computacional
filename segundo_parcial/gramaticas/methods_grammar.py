class grammar(object):
    def __init__(self):
        super(grammar, self).__init__()
        self.steps = ['B']
        self.temp_string = ''

    def derivate_string(self, string='', expression='B'):
        if string == '':
            if expression[:1] == 'B':
                self.steps.append( self.temp_string)
                return ''
            elif expression[:1] == 'R':
                self.steps.append(self.temp_string + expression)
                return '' + expression

        if string[:1] == '(':
            self.temp_string = self.temp_string + '('
            if expression[:1] == 'B':
                self.steps.append( self.temp_string+ expression.replace('B', 'RB', 1))
                return '(' + self.derivate_string(string[1:], expression.replace('B', 'RB', 1))
            elif expression[:1] == 'R':
                self.steps.append( self.temp_string + expression.replace('R', 'RR', 1))
                return '(' + self.derivate_string(string[1:], expression.replace('R', 'RR', 1))

        if string[:1] == ')':
            if expression[:1] == 'R':
                self.temp_string = self.temp_string + ')'
                self.steps.append(self.temp_string + expression[1:])
                return ')' + self.derivate_string(string[1:], expression[1:])
            else:
                self.steps.append(self.temp_string + expression)
                return '' + expression


    def print_derivation():
        pass
