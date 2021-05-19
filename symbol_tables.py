import collections
from printer import *
from symbol import *
import symbol


class VariableTable(object):
    def __init__(self):
        self.variables = {}

    def reset_functionTable(self):
        self.variables = {}

    def set_variable(self, symbol, value):
        self.variables[symbol.name] = [symbol.type, value]

    def get_variable_type(self, name):
        return self.variables[name][0]

    def get_var_symbol(self, name):
        return Symbol(name, self.variables[name][0])

    def get_size(self):
        return len(self.variables)

    def lookup_variable(self, name):
        if name in self.variables:
            return True
        else:
            return False

    def print_VariableTable(self):
        print(get_vartable_formatted(self.variables))


class FunctionTable(object):
    def __init__(self):
        self.functions = {}

    def reset_functionTable(self):
        self.functions = {}

    def set_function(self, name, type, parameters, variable_table):
        self.functions[name] = {
            "t": (
                symbol.Symbol.type_dictionary[type]
                if type in symbol.Symbol.type_dictionary
                else None
            ),
            "p": parameters,
            "s": 0,
            "vt": variable_table,
        }

    def set_function_variable_table_at(self, name):
        self.functions[name]["vt"] = VariableTable()
        for symbol in self.functions[name]["p"]:
            self.functions[name]["vt"].set_variable(symbol, None)

    def set_function_size_at(self, name):
        self.functions[name]["s"] = self.functions[name]["vt"].get_size()

    def get_function(self, name):
        return self.functions[name]

    def get_function_type(self, name):
        return self.functions[name]["t"]

    def get_function_parameters(self, name):
        return self.functions[name]["p"]

    def get_function_size(self, name):
        return self.functions[name]["s"]

    def get_function_variable_table(self, name):
        return self.functions[name]["vt"]

    def erase_function_variable_table(self, name):
        del self.functions[name]["vt"]
        self.functions[name]["vt"] = None

    def lookup_function(self, name):
        if name in self.functions:
            return True
        else:
            return False

    def print_FuncTable(self):
        print(get_functable_formatted(self.functions))


class State(object):
    def __init__(self, table=None, opt=None):
        self.table = table
        self.opt = opt

    def set_state(self, table, opt=None):
        self.table = table
        self.opt = opt


class StateTable(object):
    def __init__(self):
        self.states = []

    def reset_states(self):
        self.states = []

    def push_state(self, state):
        self.states.append(state)

    def get_curr_state(self):
        return self.states[-1]

    def get_curr_state_table(self):
        return self.states[-1].table

    def get_curr_state_opt(self):
        return self.states[-1].opt

    def set_curr_state_opt(self, opt):
        self.states[-1].opt = opt

    def remove_curr_state_opt(self):
        self.states[-1].opt = None

    def pop_curr_state(self):
        self.states.pop()

    def get_and_pop(self):
        s = self.get_curr_state()
        self.pop_curr_state()
        return s

    def get_global_table(self):
        return self.states[0].table

    def isEmpty(self):
        return self.states.count() == 0

    def isValidState(self, state, functiontable):
        otherValidStates = ["funcD", "noVar", "as_on"]
        if not state.isEmpty():
            if state.table not in functiontable.keys():
                if state.table not in otherValidStates:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False

    def print_StateTable(self):
        print(get_statetable_formatted(self.states))
