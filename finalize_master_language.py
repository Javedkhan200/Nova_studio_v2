#!/usr/bin/env python3
import sys, re

# ANSI Formatting Classes - Premium VS Code & Java Italic Vibe
C_BLUE = "\033[1;34m"
C_CYAN = "\033[1;36m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_RED = "\033[1;31m"
C_MAGENTA = "\033[1;35m"

# ITALIC (Right side leaning text style like Java IDE)
C_ITALIC = "\033[3m"
C_RESET = "\033[0m"

class NovaInterpreter:
    def __init__(self):
        self.variables = {}
        self.current_mode = "Default"

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): 
            return

        # 1. NOVA.mode Parser (With Premium Italic Shift)
        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"{C_MAGENTA}{C_ITALIC}🔮 [NOVA Mode] Pipeline Shifted to: {self.current_mode}{C_RESET}")
            except:
                print(f"{C_RED}Syntax Error: Invalid NOVA.mode declaration.{C_RESET}")

        # 2. Advanced Variable Allocation & Casting Support
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

        # 3. ULTIMATE NOVA.output Engine (Supports dynamic str() conversion & Italic print)
        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].rstrip(")")
                # Injection of safe context mapping (allows str() casting inside nova syntax)
                context_env = {"str": str, "int": int}
                context_env.update(self.variables)
                
                result = eval(content, {}, context_env)
                # Printing in Premium Leaning Italic Green
                print(f"{C_GREEN}{C_ITALIC}{result}{C_RESET}")
            except Exception as e:
                content_clean = content.strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    print(f"{C_GREEN}{C_ITALIC}{self.variables[content_clean]}{C_RESET}")
                else:
                    print(f"{C_RED}Runtime Error: Output syntax expression mismatch.{C_RESET}")

    def start_repl(self):
        print(f"{C_CYAN}⚡ Nova Language Core Engine v2.8.0 (Java-Italic Virtual Environment){C_RESET}")
        print(f"{C_YELLOW}👉 Enter 'exit()' to leave shell. Enter 'RUN' on a fresh line to compile blocks.{C_RESET}\n")
        
        buffer = []
        while True:
            try:
                prompt = f"{C_BLUE}nova ({self.current_mode}) >>> {C_RESET}" if not buffer else "     ... "
                user_input = input(prompt)
                
                if user_input.strip() == "exit()":
                    break
                
                if user_input.strip() == "RUN":
                    print(f"\n{C_CYAN}🚀 [Compiling Nova Script Tokens...]{C_RESET}")
                    for block_line in buffer:
                        self.execute_line(block_line)
                    buffer = []
                    print(f"{C_CYAN}✅ [Script Execution Terminated Successfully]{C_RESET}\n")
                    continue
                    
                if user_input.strip():
                    buffer.append(user_input)
                else:
                    if len(buffer) == 1:
                        self.execute_line(buffer[0])
                        buffer = []
            except (KeyboardInterrupt, EOFError):
                print(f"\n{C_RED}Exiting Core Master Archive.{C_RESET}")
                break

if __name__ == "__main__":
    interpreter = NovaInterpreter()
    interpreter.start_repl()
