#!/usr/bin/env python3
import sys
import datetime

# Premium VS Code Dark+ Color Palette & 100% Italicized Matrix
C_PROMPT = "\033[1;35m"   # Deep Purple for >>>
C_STRING = "\033[3;32m"   # Mint Green for Strings
C_NUMBER = "\033[1;33m"   # Gold/Yellow for Numbers
C_MODE = "\033[1;36m"     # Cyan for Systems
C_ERR = "\033[1;31m"      # Crimson Red for Errors
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
                print(f"{C_MODE}# Pipeline configured: {self.current_mode}{RESET}")
            except:
                print(f"{C_ERR}SyntaxError: Invalid mode format{RESET}")

        elif l.startswith("NOVA.ai_predict"):
            try:
                query = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_MODE}[nova-ai] parsing neural shards...{RESET}")
                q_lower = query.lower()
                if "health" in q_lower or "system" in q_lower:
                    print(f"{C_STRING}AI Response: All matrix nodes are running at 98.4% efficiency.{RESET}")
                elif "weather" in q_lower or "temp" in q_lower:
                    print(f"{C_STRING}AI Response: Climate matrix optimal. No network disruptions predicted.{RESET}")
                else:
                    print(f"{C_STRING}AI Response: Token identified. Pattern matches human sequence.{RESET}")
            except:
                print(f"{C_ERR}RuntimeError: AI Subsystem network drop{RESET}")

        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            try:
                self.variables[var_name] = eval(var_val, {"str": str, "int": int, "float": float}, self.variables)
            except:
                if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                    self.variables[var_name] = var_val[1:-1]
                else:
                    self.variables[var_name] = var_val

        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].rstrip(")")
                global_env = {"str": str, "int": int, "float": float}
                global_env.update(self.variables)
                result = eval(content, global_env, {})
                
                if isinstance(result, (int, float)):
                    print(f"{C_NUMBER}{result}{RESET}")
                else:
                    print(f"{C_STRING}{result}{RESET}")
            except Exception:
                content_clean = content.strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    val = self.variables[content_clean]
                    if isinstance(val, (int, float)):
                        print(f"{C_NUMBER}{val}{RESET}")
                    else:
                        print(f"{C_STRING}{val}{RESET}")
                else:
                    print(f"{C_ERR}RuntimeError: Unresolved token header{RESET}")

    def start_repl(self):
        current_date = datetime.datetime.now().strftime("%b %d %Y, %H:%M:%S")
        print(f"Nova 3.5.0 Core Compiler (tags/master:0bd1ed4, {current_date})")
        print(f"[Clang 16.0.6 (Android Termux Shared Build)] on linux")
        print("Type \"help\", \"copyright\" or \"credits\" for more information.")
        print("Use \"RUN\" on a blank line to execute buffered blocks.\n")
        
        buffer = []
        while True:
            try:
                # प्रॉम्प्ट स्ट्रिंग को कैरेक्टर ओवरलैप से बचाने के लिए एकदम क्लीन रखा
                prompt = f"{C_PROMPT}>>> {RESET}" if not buffer else ""
                user_input = input(prompt)
                
                if user_input.strip() == "exit()":
                    break
                
                if user_input.strip() == "RUN":
                    for block_line in buffer:
                        self.execute_line(block_line)
                    buffer = []
                    continue
                    
                if user_input.strip():
                    buffer.append(user_input)
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    interpreter = NovaEngine()
    interpreter.start_repl()
