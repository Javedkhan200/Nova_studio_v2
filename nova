#!/usr/bin/env python3
import sys

# Ultimate VS Code Premium Theme Matrix (100% Italicized)
C_PROMPT = "\033[3;36m"   # Cyan
C_OUT = "\033[3;32m"      # Soft Green
C_SYS = "\033[3;33m"      # Gold
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

        # 1. Mode Parsing
        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"{C_SYS}[core] mode: {self.current_mode}{RESET}")
            except:
                print(f"{C_ERR}SyntaxError: Invalid mode format{RESET}")

        # 2. Testing Mini AI Component inside Nova Syntax
        elif l.startswith("NOVA.ai_query"):
            try:
                query = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_SYS}[nova-ai] processing: {query}{RESET}")
                print(f"{C_OUT}[nova-ai] status: core systems optimal. memory segments clean.{RESET}")
            except:
                print(f"{C_ERR}RuntimeError: AI subsystem failure{RESET}")

        # 3. Variable Engine
        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            try:
                # Execution with isolated scope support
                self.variables[var_name] = eval(var_val, {"str": str, "int": int, "float": float}, self.variables)
            except:
                if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                    self.variables[var_name] = var_val[1:-1]
                else:
                    self.variables[var_name] = var_val

        # 4. Pure Output Emitter (Allows dynamic casting)
        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].rstrip(")")
                global_env = {"str": str, "int": int, "float": float}
                global_env.update(self.variables)
                result = eval(content, global_env, {})
                print(f"{C_OUT}{result}{RESET}")
            except Exception:
                content_clean = content.strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    print(f"{C_OUT}{self.variables[content_clean]}{RESET}")
                else:
                    print(f"{C_ERR}RuntimeError: Mismatched expression token{RESET}")

    def start_repl(self):
        print(f"{C_SYS}Nova Environment [Version 3.0.0]{RESET}")
        print(f"{C_SYS}All channels stabilized. Enter 'RUN' to execute blocks.{RESET}\n")
        
        buffer = []
        while True:
            try:
                # @ हटाकर प्योर नोवा लिनक्स स्टाइल प्रॉम्प्ट लॉक किया
                prompt = f"{C_PROMPT}nova ({self.current_mode}) > {RESET}" if not buffer else f"{C_PROMPT}     ... {RESET}"
                user_input = input(prompt)
                
                if user_input.strip() == "exit()":
                    break
                
                if user_input.strip() == "RUN":
                    for block_line in buffer:
                        self.execute_line(block_line)
                    buffer = []
                    continue
                    
                # खाली लाइनों को बफर में नहीं जोड़ेंगे ताकि ऑटो-पेस्ट ट्रिगर न हो
                if user_input.strip():
                    buffer.append(user_input)
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    interpreter = NovaEngine()
    interpreter.start_repl()
