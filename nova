#!/usr/bin/env python3
import sys, os, re

class NovaUltimateCompiler:
    def __init__(self, src):
        self.src = src
        self.out = "./" + src.replace(".nova", "")
        self.c = []
        self.c.append("#include <stdio.h>")
        self.c.append("#include <stdlib.h>")
        self.c.append("#include <string.h>")
        self.c.append("int main() {")

    def compile(self):
        if not os.path.exists(self.src):
            print(f"Error: {self.src} not found.")
            return
            
        with open(self.src, "r") as f: lines = f.readlines()
        for line in lines:
            l = line.strip()
            if not l or l.startswith("//"): continue

            if l.startswith("NOVA.mode"):
                continue

            elif l.startswith("NOVA.shell"):
                cmd = re.findall(r'\"([^\"]+)\"', l)[0]
                self.c.append(f'    system("{cmd}");')

            elif l.startswith("NOVA.output"):
                if '"' in l:
                    m = re.findall(r'\"([^\"]+)\"', l)[0]
                    self.c.append(f'    printf("{m}\\n");')

        self.c.append("    return 0;")
        self.c.append("}")
        
        c_file = "tmp_build.c"
        with open(c_file, "w") as f: 
            f.write("\n".join(self.c))
            
        build_res = os.system(f"clang {c_file} -o {self.out} 2>/dev/null")
        if os.path.exists(c_file): 
            os.remove(c_file)
            
        if build_res == 0:
            os.system(f"chmod +x {self.out}")
        else:
            print("Compilation Error.")

if __name__ == "__main__":
    if len(sys.argv) > 1: 
        NovaUltimateCompiler(sys.argv[1]).compile()
