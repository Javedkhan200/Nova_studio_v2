#!/usr/bin/env python3
import sys

# Premium VS Code Dark+ Color Palette & 100% Italicized Text
C_PROMPT = "\033[1;35m"   # Deep Purple for >>>
C_STRING = "\033[3;32m"   # Mint Green for Strings
C_NUMBER = "\033[1;33m"   # Gold/Yellow for Numbers
C_MODE = "\033[1;36m"     # Cyan for Mode Changes
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

        # 1. Pure Mode Shift (No AI text, just clean purple/cyan execution)
        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"{C_MODE}pipeline: {self.current_mode}{RESET}")
            except:
                print(f"{C_ERR}SyntaxError: Invalid mode format{RESET}")

        # 2. Testing Mini AI Component (Clean, human-coded output)
        elif l.startswith("NOVA.ai_query"):
            try:
                query = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_STRING}status: query processed successfully.{RESET}")
            except:
                print(f"{C_ERR}RuntimeError: Subsystem timeout{RESET}")

        # 3. Variable Allocation Matrix
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

        # 4. Pure Visual Output Emitter
        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].rstrip(")")
                global_env = {"str": str, "int": int, "float": float}
                global_env.update(self.variables)
                result = eval(content, global_env, {})
                
                # Check if result is number or string to color it accordingly
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
                    print(f"{C_ERR}RuntimeError: Failed to resolve token{RESET}")

    def start_repl(self):
        buffer = []
        while True:
            try:
                # Python-like >>> prompt style
                prompt = f"{C_PROMPT}>>> {RESET}" if not buffer else f"{C_PROMPT}... {RESET}"
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
