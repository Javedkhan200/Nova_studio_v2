#!/usr/bin/env python3
import sys
import datetime

# Premium Standard Colors (100% Italicized Theme)
C_PROMPT = "\033[3;35m"   # Purple
C_OUT = "\033[3;32m"      # Soft Green
C_SYS = "\033[3;36m"      # Cyan
C_ERR = "\033[3;31m"      # Red
RESET = "\033[0m"

class NovaEngine:
    def __init__(self):
        self.variables = {}
        self.current_mode = "main"

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): 
            return

        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"{C_SYS}pipeline configured: {self.current_mode}{RESET}")
            except:
                print(f"{C_ERR}SyntaxError: Invalid mode format{RESET}")

        elif l.startswith("NOVA.ai_predict"):
            try:
                query = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_SYS}[compiler-ai] evaluating tokens...{RESET}")
                
                # डायनेमिक फ्लेक्सिबल कीवर्ड मैपिंग
                score = self.variables.get("current_score", 0)
                threshold = self.variables.get("model_threshold", 0)
                
                print(f"{C_OUT}Analysis Metrics -> Query: '{query}' | Threshold: {threshold} | Score: {score}{RESET}")
            except:
                print(f"{C_ERR}RuntimeError: Subsystem compute failure{RESET}")

        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            try:
                self.variables[var_name] = eval(var_val, {"__builtins__": __builtins__}, self.variables)
            except:
                if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                    self.variables[var_name] = var_val[1:-1]
                else:
                    self.variables[var_name] = var_val

        elif l.startswith("NOVA.output"):
            try:
                content = l[12:-1].strip()
                global_env = {"__builtins__": __builtins__}
                global_env.update(self.variables)
                result = eval(content, global_env, {})
                print(f"{C_OUT}{result}{RESET}")
            except Exception:
                content_clean = l[12:-1].strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    print(f"{C_OUT}{self.variables[content_clean]}{RESET}")
                else:
                    print(f"{C_ERR}RuntimeError: Unresolved expression token{RESET}")

    def start_repl(self):
        current_date = datetime.datetime.now().strftime("%b %d %Y, %H:%M:%S")
        print(f"Nova 4.0.0 Architecture Core ({current_date})")
        print("[Clang 16.0.6 Native Termux Build] on linux")
        print("Type \"exit()\" to terminate session. Use \"RUN\" to execute blocks.\n")
        
        buffer = []
        while True:
            try:
                # बफ़र फ्लश होने के बाद प्रॉम्प्ट हमेशा फ्रेश लाइन पर री-सेट होगा
                prompt = f"{C_PROMPT}>>> {RESET}" if not buffer else ""
                user_input = input(prompt)
                
                if user_input.strip() == "exit()":
                    break
                
                if user_input.strip() == "RUN":
                    for block_line in buffer:
                        self.execute_line(block_line)
                    buffer = []
                    # एग्जीक्यूशन खत्म होते ही बफ़र पूरी तरह साफ़
                    continue
                    
                if user_input.strip():
                    buffer.append(user_input)
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    interpreter = NovaEngine()
    interpreter.start_repl()
