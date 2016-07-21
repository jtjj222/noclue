#!/usr/bin/python3

import sys
import binascii

def readCharInput():
    """Reads a single character from stdin. Note that you 
       have to press enter before any input is recognized"""
    return sys.stdin.read(1)


class BrainfuckProgram:
    def __init__(self, program):
        self.program = program
        
        self.memory = bytearray(1)
        
        # The program counter / instruction pointer
        self.pc = 0
        
        # Data counter
        self.dc = 0
    
    def run(self):
        while self.pc < len(self.program):
            c = self.program[self.pc]
            
            # See full command reference at https://en.wikipedia.org/wiki/Brainfuck
            if c == ">": 
                self.dc += 1
            elif c == "<": 
                self.dc -= 1
            elif c == "+": 
                # We wrap around memory (i.e, if value is 0, and we subtract one, it becomes 255)
                self.memory[self.dc] = (int(self.memory[self.dc]) + 1) % 255
            elif c == "-": 
                self.memory[self.dc] = (int(self.memory[self.dc]) - 1) % 255
            elif c == ".": 
                # ord/chr convert between an ascii int and a character
                print(chr(self.memory[self.dc]), end="")
            elif c == ",": 
                self.memory[self.dc] = ord(readCharInput())
            elif c == "[": 
                if self.memory[self.dc] == 0:
                    self.jump_forward()
            elif c == "]": 
                if self.memory[self.dc] != 0:
                    self.jump_back()
            
            self.pc += 1
            
            # Verify our state after each command so we can trace back errors
            self.verify_state()
            
            # Useful for debugging
            # print(self)

    def verify_state(self):
        if self.dc >= len(self.memory):
            # Allocate more memory for our program
            self.memory.extend([0] * (self.dc + 1 - len(self.memory)))
        
        if self.dc < 0:
            raise ValueError("Data pointer is out of bounds", self)
        
        if self.pc < 0:
            raise ValueError("Instruction pointer is out of bounds", self)
    
    def jump_forward(self):
        """When we see [, we jump to just after the matching nested ]"""
        depth = 1
        new_pc = self.pc + 1
        while new_pc < len(self.program):
            if self.program[new_pc] == "[":
                depth += 1
            elif self.program[new_pc] == "]":
                depth -= 1
                if depth == 0:
                    # Remember that the pc is incremented after this instruction
                    self.pc = new_pc
                    return
            new_pc += 1
        
        raise ValueError("No matching ] found for [ at {0}".format(self))
    
    def jump_back(self):
        """When we see ], we jump back to just after the matching nested ["""
        depth = 1
        new_pc = self.pc - 1
        while new_pc > 0:
            if self.program[new_pc] == "]":
                depth += 1
            elif self.program[new_pc] == "[":
                depth -= 1
                if depth == 0:
                    self.pc = new_pc
                    return
            new_pc -= 1
        
        raise ValueError("No matching ] found for [ at {0}".format(self))
    
    def __str__(self):
        """Give a human-readable representation of our current state"""
        
        dump = "pc:{0} dc:{1} \nMemory Dump:\n".format(self.pc, self.dc)
        
        for i in range(0, len(self.memory), 20):
            dump += "{0:05d} -- ".format(i)
            dump += binascii.hexlify(self.memory[i:i+20]).decode('ascii')
            dump += "\n"
        
        return dump


def main():
    if (len(sys.argv) == 2):
        # The with statement in python automatically closes 
        # the file when we are done with it. You should always
        # close resources from the OS when you are done with them
        with open(sys.argv[1], 'r') as file:
            program = BrainfuckProgram(file.read())
            program.run()
    else:
        print("usage:", sys.argv[0], "[filename]")
        sys.exit(1)

main()
