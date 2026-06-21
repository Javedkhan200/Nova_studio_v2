#!/usr/bin/env python3
import sys, re

# ANSI Color Codes for VS Code / Termux Premium Theme
C_BLUE = "\033[1;34m"
C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"
C_RESET = "\033[0m"

class NovaInterpreter:
    def __init__(self):
        self.variables = {}
        self.current_mode = "Default"

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): 
            return

        # 1. NOVA.mode Parser
        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"{C_MAGENTA}🔮 [NOVA] Pipeline Shifted to Mode: {self.current_mode}{C_RESET}")
            except:
                print(f"{C_RED}Syntax Error: Invalid NOVA.mode declaration.{C_RESET}")

        # 2. Variable Allocation & Math evaluation
        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            try:
                # Store anything safely by evaluating dynamically
                self.variables[var_name] = eval(var_val, {}, self.variables)
            except:
                # If it's a raw string without quotes, store as string
                if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                    self.variables[var_name] = var_val[1:-1]
                else:
                    self.variables[var_name] = var_val

        # 3. ADVANCED NOVA.output Engine (With Color & Dynamic String Concat)
        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].rstrip(")")
                # Python-like eval to automatically concatenate strings and variables seamlessly
                result = eval(content, {}, self.variables)
                print(f"{C_GREEN}{result}{C_RESET}")
            except Exception as e:
                # Fallback if it's just a simple printed variable or unquoted string
                content_clean = content.strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    print(f"{C_GREEN}{self.variables[content_clean]}{C_RESET}")
                else:
                    print(f"{C_RED}Runtime Error: Output expression execution failed.{C_RESET}")

    def start_repl(self):
        print(f"{C_CYAN}⚡ Nova Language Core Engine v2.5.0 (Color Interactive Shell){C_RESET}")
        print(f"{C_YELLOW}👉 Type 'exit()' to close. Type 'RUN' to execute blocks.{C_RESET}\n")
        
        buffer = []
        while True:
            try:
                prompt = f"{C_BLUE}nova ({self.current_mode}) >>> {C_RESET}" if not buffer else "     ... "
                user_input = input(prompt)
                
                if user_input.strip() == "exit()":
                    break
                
                if user_input.strip() == "RUN":
                    print(f"\n{C_CYAN}🚀 [Executing Block...]{C_RESET}")
                    for block_line in buffer:
                        self.execute_line(block_line)
                    buffer = []
                    print(f"{C_CYAN}✅ [Block Execution Finished]{C_RESET}\n")
                    continue
                    
                if user_input.strip():
                    buffer.append(user_input)
                else:
                    if len(buffer) == 1:
                        self.execute_line(buffer[0])
                        buffer = []
            except (KeyboardInterrupt, EOFError):
                print(f"\n{C_RED}Exiting Nova Core.{C_RESET}")
                break

if __name__ == "__main__":
    interpreter = NovaInterpreter()
    interpreter.start_repl()
