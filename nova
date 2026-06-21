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

        if l.startswith("NOVA.mode"):
            try:
                mode_name = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                self.current_mode = mode_name
                print(f"🔮 [NOVA] Pipeline Shifted to Mode: {self.current_mode}")
            except:
                print("Syntax Error: Invalid NOVA.mode declaration.")

        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                self.variables[var_name] = var_val[1:-1]
            else:
                try:
                    self.variables[var_name] = eval(var_val, {}, self.variables)
                except:
                    print(f"Runtime Error: Undefined allocation for '{var_name}'")

        elif l.startswith("NOVA.output"):
            try:
                content = l.split("(")[1].split(")")[0].strip()
                if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
                    print(content[1:-1])
                elif content in self.variables:
                    print(self.variables[content])
                else:
                    print(eval(content, {}, self.variables))
            except:
                print("Syntax Error: Invalid NOVA.output syntax.")

    def start_repl(self):
        print("⚡ Nova Language Core Engine v2.1.0 (Interactive Shell)")
        print("👉 Type 'exit()' to close. Type 'RUN' on a new line to execute pasted blocks.\n")
        
        buffer = []
        while True:
            try:
                prompt = f"nova ({self.current_mode}) >>> " if not buffer else "     ... "
                user_input = input(prompt)
                
                if user_input.strip() == "exit()":
                    break
                
                if user_input.strip() == "RUN":
                    print("\n🚀 [Executing Block...]")
                    for block_line in buffer:
                        self.execute_line(block_line)
                    buffer = []
                    print("✅ [Block Execution Finished]\n")
                    continue
                    
                if user_input.strip():
                    buffer.append(user_input)
                else:
                    # सिंगल लाइन एंटर मारने पर अगर बफर खाली है तो तुरंत रन करो
                    if len(buffer) == 1:
                        self.execute_line(buffer[0])
                        buffer = []
            except (KeyboardInterrupt, EOFError):
                print("\nExiting Nova Core.")
                break

if __name__ == "__main__":
    interpreter = NovaInterpreter()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        interpreter.start_repl()
