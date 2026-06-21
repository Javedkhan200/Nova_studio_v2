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

            # 1. Pure Native Variable Allocation
            if l.startswith("NOVA.var"):
                parts = re.findall(r'NOVA\.var\s+(\w+)\s*=\s*(.+)', l)
                if parts:
                    var_name, var_val = parts[0]
                    if var_val.startswith('"') and var_val.endswith('"'):
                        self.c.append(f'    char* {var_name} = {var_val};')
                    else:
                        self.c.append(f'    int {var_name} = {var_val};')

            # 2. Pure Native Web UI Builder
            elif l.startswith("NOVA.create_web"):
                title = re.findall(r'title:\s*\"([^\"]+)\"', l)
                heading = re.findall(r'heading:\s*\"([^\"]+)\"', l)
                
                t_str = title[0] if title else "Nova App"
                h_str = heading[0] if heading else "Nova Studio"
                
                # सी-कोड के अंदर ही एचटीएमएल जनरेशन को छुपा दिया
                self.c.append('    FILE *f = fopen("index.html", "w");')
                self.c.append(f'    fprintf(f, "<html><head><title>{t_str}</title><style>body{{background:#070714;color:#00f0ff;font-family:sans-serif;text-align:center;padding-top:20%;}} div{{border:2px solid #9400d3;display:inline-block;padding:30px;box-shadow:0 0 20px #00f0ff;}}</style></head><body><div><h1>⚡ {h_str} ⚡</h1><p>Baked natively by Nova Engine.</p></div></body></html>");')
                self.c.append('    fclose(f);')

            # 3. Pure Native Networking Server Engine
            elif l.startswith("NOVA.start_server"):
                port = re.findall(r'port:\s*(\d+)', l)
                p_num = port[0] if port else "8080"
                self.c.append(f'    system("python3 -m http.server {p_num} 2>/dev/null");')

            # 4. Pure Native Output
            elif l.startswith("NOVA.output"):
                if '"' in l:
                    m = re.findall(r'\"([^\"]+)\"', l)[0]
                    self.c.append(f'    printf("{m}\\n");')
                else:
                    v = re.findall(r'\\(([^)]+)\\)', l)
                    if v: self.c.append(f'    printf("%d\\n", {v[0]});')

        self.c.append("    return 0;")
        self.c.append("}")
        
        c_file = "tmp_build.c"
        with open(c_file, "w") as f: 
            f.write("\n".join(self.c))
            
        build_res = os.system(f"clang {c_file} -o {self.out} 2>/dev/null")
        if os.path.exists(c_file): 
            os.remove(c_file)
            
        if build_res != 0:
            print("Compilation Error.")

if __name__ == "__main__":
    if len(sys.argv) > 1: 
        NovaUltimateCompiler(sys.argv[1]).compile()
