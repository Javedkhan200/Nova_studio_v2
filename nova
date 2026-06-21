#!/usr/bin/env python3
import sys

class NovaInterpreter:
    def __init__(self):
        self.variables = {}
        self.current_mode = "Default"

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): 
            return

        # 1. NOVA.mode Method Layer
        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"🔮 [NOVA] Pipeline Shifted to Mode: {self.current_mode}")
            except:
                print("Syntax Error: Invalid NOVA.mode declaration.")

        # 2. Variable Allocation Logic
        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            
            # String parsing
            if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                self.variables[var_name] = var_val[1:-1]
            else:
                # Math evaluation
                try:
                    self.variables[var_name] = eval(var_val, {}, self.variables)
                except:
                    print(f"Runtime Error: Undefined allocation for '{var_name}'")

        # 3. NOVA.output Engine
        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].split(")")[0].strip()
                if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
                    print(content[1:-1])
                elif content in self.variables:
                    print(self.variables[content])
                else:
                    # Direct expression evaluation inside print
                    print(eval(content, {}, self.variables))
            except:
                print("Syntax Error: Invalid NOVA.output syntax.")

    def start_repl(self):
        print("⚡ Nova Language Core Engine v2.0.0 (Interactive Shell)")
        print("👉 Type 'exit()' to close the Nova shell.\n")
        while True:
            try:
                prompt = f"nova ({self.current_mode}) >>> "
                user_input = input(prompt)
                if user_input.strip() == "exit()":
                    break
                self.execute_line(user_input)
            except (KeyboardInterrupt, EOFError):
                print("\nExiting Nova Core.")
                break

    def run_file(self, filename):
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return
        with open(filename, "r") as f:
            for line in f.readlines():
                self.execute_line(line)

if __name__ == "__main__":
    interpreter = NovaInterpreter()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        interpreter.start_repl()
