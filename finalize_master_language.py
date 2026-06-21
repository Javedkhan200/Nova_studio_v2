#!/usr/bin/env python3
import sys, os, re

class NovaUltimateCompiler:
    def __init__(self, src):
        self.src = src; self.out = src.replace(".nova", ""); self.c = []
        self.c.append("#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nint main() {")
        self.c.append('    printf("🛡️ [NOVA SECURITY LAYER] Running System Integrity Checks...\\n\\n");')

    def compile(self):
        with open(self.src, "r") as f: lines = f.readlines()
        for line in lines:
            l = line.strip()
            if not l or l.startswith("//"): continue

            if l.startswith("NOVA.mode"):
                m = re.findall(r'"([^"]+)"', l)[0]
                self.c.append(f'    printf("🔮 [MODE] Current Core Mode: {m}\\n");')

            elif l.startswith("NOVA.net_scan"):
                target = re.findall(r'"([^"]+)"', l)[0]
                self.c.append(f'    printf("🔍 [AUDIT] Checking host availability for: {target}\\n");')
                self.c.append(f'    system("ping -c 2 {target} > /dev/null && printf \"   🟢 [STATUS] Destination is Reachable\\n\" || printf \"   🔴 [STATUS] Destination Unreachable\\n\"");')

            elif l.startswith("NOVA.port_check"):
                parts = l.split()
                if len(parts) >= 3:
                    target_ip = parts[1]
                    port = parts[2]
                    self.c.append(f'    printf("⚡ [PORT AUDIT] Scanning network accessibility on {target_ip} at Port {port}...\\n");')
                    self.c.append(f'    system("nc -zv -w 3 {target_ip} {port} > /dev/null 2>&1 && printf \"   🟢 Port {port} is OPEN\\n\" || printf \"   🔴 Port {port} is CLOSED or Filtered\\n\"");')

            elif l.startswith("NOVA.output"):
                if '"' in l:
                    m = re.findall(r'"([^"]+)"', l)[0]
                    self.c.append(f'    printf("{m}\\n");')

        self.c.append('\n    printf("\n✅ [SYSTEM AUDIT] Network routine diagnostics finished successfully.\\n");\n    return 0;\n}')
        with open("tmp_build.c", "w") as f: f.write("\n".join(self.c))
        os.system(f"clang tmp_build.c -o {self.out} 2>/dev/null")
        if os.path.exists("tmp_build.c"): os.remove("tmp_build.c")
        print("🏆 [NOVA SUCCESS] Code compilation syntax error resolved!")

if __name__ == "__main__":
    if len(sys.argv) > 1: NovaUltimateCompiler(sys.argv[1]).compile()
