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
        self.c.append('    printf("🛡️ [NOVA SECURITY LAYER] Running System Integrity Checks...\\n\\n");')

    def compile(self):
        if not os.path.exists(self.src):
            print(f"🔴 [ERROR] File {self.src} not found!")
            return
            
        with open(self.src, "r") as f: lines = f.readlines()
        for line in lines:
            l = line.strip()
            if not l or l.startswith("//"): continue

            if l.startswith("NOVA.mode"):
                m = re.findall(r'\"([^\"]+)\"', l)[0]
                self.c.append(f'    printf("🔮 [MODE] Current Core Mode: {m}\\n");')

            elif l.startswith("NOVA.net_scan"):
                target = re.findall(r'\"([^\"]+)\"', l)[0]
                self.c.append(f'    printf("🔍 [AUDIT] Checking host availability for: {target}\\n");')
                # \x22 का जादू - सी कंपाइलर के लिए एकदम क्लीन डबल कोट्स
                self.c.append(f'    system("ping -c 2 {target} > /dev/null && printf \\x22   🟢 [STATUS] Destination is Reachable\\n\\x22 || printf \\x22   🔴 [STATUS] Destination Unreachable\\n\\x22");')

            elif l.startswith("NOVA.port_check"):
                parts = l.split()
                if len(parts) >= 3:
                    target_ip = parts[1].replace('"', '')
                    port = parts[2]
                    self.c.append(f'    printf("⚡ [PORT AUDIT] Scanning network accessibility on {target_ip} at Port {port}...\\n");')
                    # यहाँ भी \x22 की वजह से क्लैंग एकदम परफेक्ट बिल्ड करेगा
                    self.c.append(f'    system("nc -zv -w 3 {target_ip} {port} > /dev/null 2>&1 && printf \\x22   🟢 Port {port} is OPEN\\n\\x22 || printf \\x22   🔴 Port {port} is CLOSED or Filtered\\n\\x22");')

            elif l.startswith("NOVA.output"):
                if '"' in l:
                    m = re.findall(r'\"([^\"]+)\"', l)[0]
                    self.c.append(f'    printf("{m}\\n");')

        self.c.append('    printf("\\n✅ [SYSTEM AUDIT] Network routine diagnostics finished successfully.\\n");')
        self.c.append("    return 0;")
        self.c.append("}")
        
        c_file = "tmp_build.c"
        with open(c_file, "w") as f: 
            f.write("\n".join(self.c))
            
        build_res = os.system(f"clang {c_file} -o {self.out}")
        if os.path.exists(c_file): 
            os.remove(c_file)
            
        if build_res == 0:
            os.system(f"chmod +x {self.out}")
            print(f"🏆 [NOVA SUCCESS] Binary compiled successfully -> {self.out}")
        else:
            print("🔴 [COMPILER ERROR] Clang build failed! String mismatch.")

if __name__ == "__main__":
    if len(sys.argv) > 1: 
        NovaUltimateCompiler(sys.argv[1]).compile()
