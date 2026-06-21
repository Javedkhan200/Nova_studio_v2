#!/usr/bin/env python3
import sys

# Premium VS Code Standard Colors & Font Style Matrix
FONT_SHELL = "\033[3;36m"     # Italic Bright Cyan for Prompts
FONT_OUT = "\033[3;32m"       # Italic Soft Mint Green for User Output
FONT_SYS = "\033[3;33m"       # Italic Gold for System Messages
FONT_ERR = "\033[3;31m"       # Italic Crimson Red for Failures
RESET = "\033[0m"

class NovaInterpreter:
    def __init__(self):
        self.variables = {}
        self.current_mode = "main"

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): 
            return

        # 1. Native Mode Parser
        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"{FONT_SYS}[nova-core] mode initialized: {self.current_mode}{RESET}")
            except:
                print(f"{FONT_ERR}SyntaxError: Invalid mode declaration{RESET}")

        # 2. Variable Allocation Engine
        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            try:
                self.variables[var_name] = eval(var_val, {"str": str, "int": int}, self.variables)
            except:
                if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                    self.variables[var_name] = var_val[1:-1]
                else:
                    self.variables[var_name] = var_val

        # 3. Native Output Engine
        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].rstrip(")")
                context_env = {"str": str, "int": int}
                context_env.update(self.variables)
                
                result = eval(content, {}, context_env)
                print(f"{FONT_OUT}{result}{RESET}")
            except Exception:
                content_clean = content.strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    print(f"{FONT_OUT}{self.variables[content_clean]}{RESET}")
                else:
                    print(f"{FONT_ERR}RuntimeError: Failed to resolve expression token{RESET}")

    def start_repl(self):
        print(f"{FONT_SYS}Nova Core Environment [Version 2.9.0]{RESET}")
        print(f"{FONT_SYS}Interactive REPL instance initialized. Use 'RUN' to compile.{RESET}\n")
        
        buffer = []
        while True:
            try:
                prompt = f"{FONT_SHELL}nova@{self.current_mode} > {RESET}" if not buffer else f"{FONT_SHELL}     ... {RESET}"
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
                else:
                    if len(buffer) == 1:
                        self.execute_line(buffer[0])
                        buffer = []
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    interpreter = NovaInterpreter()
    interpreter.start_repl()
