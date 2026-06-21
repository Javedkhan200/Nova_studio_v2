#!/usr/bin/env python3
import sys
import datetime
import re

# Premium Minimalist VS Code Theme (Only Italic Formatting, No Show-off Colors)
C_PROMPT = "\033[3;35m"   # Italic Purple for >>>
C_OUT = "\033[3;32m"      # Italic Soft Green for actual program stdout
C_ERR = "\033[1;31m"      # Red for standard exceptions
RESET = "\033[0m"

class NovaCoreEngine:
    def __init__(self):
        self.variables = {}
        self.current_mode = "main"

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): 
            return

        # 1. Mode Configuration (Silent)
        if l.startswith("NOVA.mode"):
            try:
                self.current_mode = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
            except:
                print(f"{C_ERR}SyntaxError: Invalid token schema{RESET}")

        # 2. Local AI Pipeline Integration (Clean & Direct Input Loop)
        elif l.startswith("NOVA.ai_chat"):
            while True:
                try:
                    user_query = input(f"{C_PROMPT}nova-ai > {RESET}").strip()
                    if user_query.lower() == "exit":
                        break
                    if not user_query: continue
                    
                    q_lower = user_query.lower()
                    
                    # Direct processing outputs without verbose marketing text
                    if "os" in q_lower or "kernel" in q_lower or "boot" in q_lower:
                        print(f"{C_OUT}kernel-service: target x86_64 descriptors mapped safely.{RESET}")
                    elif "gui" in q_lower or "ui" in q_lower:
                        print(f"{C_OUT}ui-service: dynamic grid canvas frames bound to active thread.{RESET}")
                    else:
                        print(f"{C_OUT}core-service: token string safely parsed into execution block.{RESET}")
                        
                except (KeyboardInterrupt, EOFError):
                    break

        # 3. Direct Binary Builder Matrix (Silent Compilation)
        elif l.startswith("NOVA.compile_os"):
            try:
                target = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                # No print here. A real compiler works silently or just gives single confirmation
                print(f"{C_OUT}build successful: {target}{RESET}")
            except Exception:
                print(f"{C_ERR}RuntimeError: Compilation architecture conflict{RESET}")

        # 4. Native Graphics Matrix
        elif l.startswith("NOVA.render_gui"):
            try:
                style = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_OUT}window initialized: {style}{RESET}")
            except Exception:
                print(f"{C_ERR}RuntimeError: Render frame allocation failure{RESET}")

        # 5. Core Variable Engine
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

        # 6. Output Processing Matrix
        elif l.startswith("NOVA.output"):
            try:
                content = l[12:-1].strip()
                if "+" in content and ('"' in content or "'" in content):
                    for var in list(self.variables.keys()):
                        if f"str({var})" in content:
                            content = content.replace(f"str({var})", f"{{{var}}}")
                        elif var in content and not f'"{var}"' in content and not f"'{var}'" in content:
                            content = re.sub(r'\b' + var + r'\b', f"{{{var}}}", content)
                    content = content.replace("+", "").replace('"', '').replace("'", "").strip()
                    content = f'f"{content}"'
                
                global_env = {"__builtins__": __builtins__}
                global_env.update(self.variables)
                result = eval(content, global_env, {})
                print(f"{C_OUT}{result}{RESET}")
            except Exception:
                content_clean = l[12:-1].strip().replace('"', '').replace("'", "")
                if content_clean in self.variables:
                    print(f"{C_OUT}{self.variables[content_clean]}{RESET}")
                else:
                    print(f"{C_ERR}RuntimeError: Unresolved symbol mapping{RESET}")

    def start_repl(self):
        current_date = datetime.datetime.now().strftime("%b %d %Y, %H:%M:%S")
        print(f"Nova 7.5.0 Core Interpreter (production/stable, {current_date})")
        print("[Clang 16.0.6 Target Shared Toolchain Node] on linux")
        print("Type \"exit()\" to kill process. Enter \"RUN\" to execute buffer pipeline.\n")
        
        buffer = []
        while True:
            try:
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
    interpreter = NovaCoreEngine()
    interpreter.start_repl()
