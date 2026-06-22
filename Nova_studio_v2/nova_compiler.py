import sys
import re
import os

class NovaFinalCompiler:
    def __init__(self, source_file):
        self.source_file = source_file
        self.binary_name = source_file.replace(".nova", "")
        self.c_source = []
        
        # असली प्रोग्रामिंग लैंग्वेज के कर्नल हेडर
        self.c_source.append("#include <stdio.h>")
        self.c_source.append("#include <stdlib.h>")
        self.c_source.append("#include <string.h>")
        self.c_source.append("int main() {")

    def compile(self, target_os="local"):
        if not os.path.exists(self.source_file):
            print(f"❌ [NOVA ERROR] {self.source_file} missing.")
            return

        with open(self.source_file, "r") as f:
            lines = f.readlines()

        print(f"🚀 [NOVA ENGINE] Transforming tokens for {self.source_file}...")

        for line in lines:
            line = line.strip()
            if not line or line.startswith("//"):
                continue

            # 1. वास्तविक वेरिएबल एलोकेशन (Memory Allocation)
            alloc_match = re.match(r'NOVA\.allocate\((.+)\s*=\s*"([^"]+)"\)', line)
            if alloc_match:
                var_name = alloc_match.group(1).strip()
                var_value = alloc_match.group(2).strip()
                self.c_source.append(f'    char* {var_name} = "{var_value}";')
                continue

            # 2. वास्तविक कंसोल आउटपुट (Direct Console Output)
            output_match = re.match(r'NOVA\.output\("([^"]+)"\)', line)
            if output_match:
                payload = output_match.group(1)
                self.c_source.append(f'    printf("%s\\n", "{payload}");')
                continue

            # 3. पैकेज लिंकिंग प्रोटोकॉल
            package_match = re.match(r'NOVA\.package\("([^"]+)"\)', line)
            if package_match:
                pkg = package_match.group(1)
                self.c_source.append(f'    // Node link: {pkg}')
                continue

        self.c_source.append("    return 0;")
        self.c_source.append("}")

        # इंटरमीडिएट कोड जेनरेशन
        temp_c = "nova_out.c"
        with open(temp_c, "w") as f:
            f.write("\n".join(self.c_source))

        # ओएस के आधार पर कंपाइलर फ्लैग्स तय करना
        cmd = f"clang {temp_c} -o {self.binary_name}"
        if target_os == "windows":
            cmd = f"clang {temp_c} --target=x86_64-pc-windows-gnu -o {self.binary_name}.exe"
        elif target_os == "linux":
            cmd = f"clang {temp_c} --target=x86_64-unknown-linux-gnu -o {self.binary_name}.bin"

        status = os.system(cmd)
        if os.path.exists(temp_c):
            os.remove(temp_c)

        if status == 0:
            print(f"✅ [SUCCESS] Native standalone output ready for target: [{target_os}]")
        else:
            print("❌ [ERROR] Compilation failed due to target toolception.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nova_compiler.py <file.nova> [local/windows/linux]")
    else:
        target = sys.argv[2] if len(sys.argv) > 2 else "local"
        compiler = NovaFinalCompiler(sys.argv[1])
        compiler.compile(target)

