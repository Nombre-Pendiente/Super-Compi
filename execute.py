import sys
import compilador.helpers.file_parser
from compilador.helpers.file_parser import *
import compilador.vm.virtual_machine
from compilador.vm.virtual_machine import *
import game_engine.engine
from game_engine.engine import *


class Executer(object):
    def __init__(self, running_file):
        self.running_file = running_file
        self.data = parser_file(running_file)
        self.quads = self.data["q"]
        self.pretty_quads = self.data["str"]
        self.function_table = self.data["ft"]

    def __print_quads(self, pre_quads):
        if pre_quads:
            print("Program Quads before assignations:")
            print("-------------------------------------")
            print(self.pretty_quads)
        else:
            print("Program Quads after assignations:")
            for q in self.quads:
                print("--{}----------------------------------".format(q))
                self.quads[q].print_quad()
            print("-------------------------------------")

    def __print_instructions(self, instructions):
        print("\nResulting Instructions:")
        print("-------------------------------------")
        Instruction.print_instructions(instructions)

    def __print_running(self):
        print("Running: {}".format(self.running_file))
        print("-------------------------------------")

    def __load_level_one(self, instructions):
        characters = {
            "pepe": Character(0, 0, 50, 50, 50),
        }

        Engine.start(characters, instructions, "one")

    def __load_level_two(self, instructions):
        characters = {
            "dinoAdrian": Character(0, 400, 50, 50, 50),
            "rositaFresita": Character(0, 300, 50, 50, 50),
        }

        Engine.start(characters, instructions, "two")

    def run(self, **kwargs):
        if kwargs.get("print_pre_quads"):
            self.__print_quads(True)

        vm = VirtualMachine(3000, 1000, 6000, self.function_table)
        # vm.quadruple_direction_allocator(self.quads)

        if kwargs.get("print_post_quads"):
            self.__print_quads(False)

        if kwargs.get("print_post_quads"):
            self.__print_quads(False)

        if kwargs.get("print_running"):
            self.__print_running()

        instructions = vm.run(self.quads)

        if kwargs.get("print_instructions"):
            self.__print_instructions(instructions)

        if (kwargs.get("run_game") or kwargs.get("play_level")) and len(instructions):

            if 1 in [kwargs.get("run_game"), kwargs.get("play_level")]:
                print("helloasd")
                self.__load_level_one(instructions)
            elif 2 in [kwargs.get("run_game"), kwargs.get("play_level")]:
                self.__load_level_two(instructions)

        return instructions
