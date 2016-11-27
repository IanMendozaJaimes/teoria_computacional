class states_tree(object):
    def __init__(self, datum, stack):
        self.datum = datum
        self.stack = list()
        self.left_child = None
        self.middle_child = None
        self.right_child = None

        self.stack = stack[:]
        self.stack.append(datum)


    def generate_tree(self):
        #left child
        if self.datum[1] != 0 and self.datum[2] != 0:
            new_datum = [self.datum[0]+2, self.datum[1]-1, self.datum[2]-1]
            if not self.compare_states(new_datum):
                self.left_child = states_tree(new_datum, self.stack)
                self.left_child.generate_tree()
            else:
                self.left_child = states_tree(new_datum, self.stack)


        #middle child
        if self.datum[0] != 0 and self.datum[2] != 0:
            new_datum = [self.datum[0]-1, self.datum[1]+2, self.datum[2]-1]
            if not self.compare_states(new_datum):
                self.middle_child = states_tree(new_datum, self.stack)
                self.middle_child.generate_tree()
            else:
                self.middle_child = states_tree(new_datum, self.stack)


        #right child
        if self.datum[0] != 0 and self.datum[1] != 0:
            new_datum = [self.datum[0]-1, self.datum[1]-1, self.datum[2]+2]
            if not self.compare_states(new_datum):
                self.right_child = states_tree(new_datum, self.stack)
                self.right_child.generate_tree()
            else:
                self.right_child = states_tree(new_datum, self.stack)


    def compare_states(self, datum):
        for x in self.stack:
            if x == datum:
                return True

        return False


    def imprimir_arbol(self):
        con = 0
        if self.left_child != None:
            self.left_child.imprimir_arbol()
        else:
            con = con + 1

        if self.middle_child != None:
            self.middle_child.imprimir_arbol()
        else:
            con = con + 1

        if self.right_child != None:
            self.right_child.imprimir_arbol()
        else:
            con = con + 1

        if con == 3:
            print('path',self.stack)

#[datum[], datum[], datum[]]
