import sys
import re

class NovaCoreKernel:
    def __init__(self):
        # नोवा के अपने ओरिजिनल कर्नल मोड्स (कोई बाहरी कॉपी नहीं)
        self.active_mode = "Standard"
        self.heap_memory = {}
        
        # नोवा वॉइस AI और एथिकल हैकिंग के नेटिव पैकेजेस का रजिस्टर
        self.loaded_packages = ["nova.voice", "nova.packet_injector"]
        print("⚡ [NOVA COMPILER V2] LLVM Multi-Engine Shard Loaded Successfully.")

    def execute_line(self, line):
        line = line.strip()
        if not line or line.startswith("//"): 
            return

        # 1. FORMAT PROTOCOL: NOVA.mode
        mode_match = re.match(r'NOVA\.mode\("([^"]+)"\)', line)
        if mode_match:
            mode_target = mode_match.group(1)
            self.active_mode = mode_target
            print(f"🔮 [NOVA RUNTIME] Core shifted to internal matrix: {self.active_mode}")
            return

        # 2. FORMAT PROTOCOL: NOVA.allocate (यूनिवर्सल मैमोरी मैनेजर)
        alloc_match = re.match(r'NOVA\.allocate\((.+)\s*=\s*(.+)\)', line)
        if alloc_match:
            var_name = alloc_match.group(1).strip()
            var_value = alloc_match.group(2).strip()
            self.heap_memory[var_name] = {"value": var_value, "mode": self.active_mode}
            print(f"📦 [NOVA MEMORY] Allocated '{var_name}' into secure {self.active_mode} block.")
            return

        # 3. FORMAT PROTOCOL: NOVA.output (डायरेक्ट कर्नल डिस्प्ले बफ़र)
        output_match = re.match(r'NOVA\.output\("([^"]+)"\)', line)
        if output_match:
            payload = output_match.group(1)
            print(f"📟 [NOVA CONSOLE] {payload}")
            return

        # अगर यूजर कुछ गलत लिखता है या हैकिंग/वॉइस का गलत सिंटैक्स डालता है
        print(f"❌ [NOVA SYNTAX ERROR] Unknown token command stream: '{line}'")

# मोबाइल कर्नल कंपाइलर को चालू करना
if __name__ == "__main__":
    kernel = NovaCoreKernel()
    
    # चलो तुम्हारे बनाए असली सिंटैक्स को टेस्ट करते हैं!
    test_nova_script = [
        'NOVA.mode("Speed")',
        'NOVA.allocate(hack_node = "0x7FFF32")',
        'NOVA.output("Nova Engine Broken the Matrix!")',
        'NOVA.mode("Secure")'
    ]
    
    print("\n--- Running Test Nova Core Stream ---")
    for script_line in test_nova_script:
        kernel.execute_line(script_line)
