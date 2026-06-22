#!/usr/bin/env python3
import sys
import datetime
import re

C_PROMPT = "\033[3;35m"   # Italic Purple
C_OUT = "\033[3;32m"      # Italic Soft Green
C_ERR = "\033[1;31m"      # Red
RESET = "\033[0m"

class NovaV10Engine:
    def __init__(self):
        self.variables = {}
        self.current_mode = "main"
        self.operator_age = 16
        self.ai_cores = {
            "core-01": "Sys-Architect",
            "core-02": "Neural-NLP",
            "core-03": "UI-Grid-Renderer",
            "core-04": "Fusion-Security"
        }

    def trigger_ollama_pipeline(self, prompt_stream):
        p_lower = prompt_stream.lower()
        if "compile" in p_lower or "os" in p_lower:
            print(f"{C_OUT}core-service: {self.ai_cores['core-01']} target verification active.{RESET}")
        elif "solve" in p_lower or "math" in p_lower:
            print(f"{C_OUT}core-service: {self.ai_cores['core-02']} tensor operation active.{RESET}")
        elif "gui" in p_lower or "render" in p_lower:
            print(f"{C_OUT}core-service: {self.ai_cores['core-03']} buffer canvas active.{RESET}")
        else:
            print(f"{C_OUT}core-service: {self.ai_cores['core-04']} stream audit active.{RESET}")

    def execute_line(self, line):
        l = line.strip()
        if not l or l.startswith("//"): return
        if l.startswith("NOVA.mode"):
            try: self.current_mode = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
            except: print(f"{C_ERR}SyntaxError: Invalid mode layer{RESET}")
        elif l.startswith("NOVA.verify_operator"):
            print(f"{C_OUT}operator-service: status active [age: {self.operator_age}]{RESET}")
        elif l.startswith("NOVA.compile_os"):
            try:
                target = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_OUT}build successful: {target}{RESET}")
            except: print(f"{C_ERR}CompilerError: Target architecture conflict{RESET}")
        elif l.startswith("NOVA.render_gui"):
            try:
                style = l.split("(")[1].split(")")[0].replace('"', '').replace("'", "")
                print(f"{C_OUT}window initialized: {style}{RESET}")
            except: print(f"{C_ERR}RenderError: Buffer allocation failure{RESET}")
        elif l.startswith("NOVA.solve"):
            try:
                expression = l.split("(")[1].rstrip(")")
                result = eval(expression, {"__builtins__": __builtins__}, self.variables)
                print(f"{C_OUT}math-service: {result}{RESET}")
            except Exception as e: print(f"{C_ERR}MathError: {e}{RESET}")
        elif "=" in l and not l.startswith("NOVA."):
            parts = l.split("=")
            var_name = parts[0].strip()
            var_val = parts[1].strip()
            try: self.variables[var_name] = eval(var_val, {"__builtins__": __builtins__}, self.variables)
            except:
                if (var_val.startswith('"') and var_val.endswith('"')) or (var_val.startswith("'") and var_val.endswith("'")):
                    self.variables[var_name] = var_val[1:-1]
                else: self.variables[var_name] = var_val
        elif l.startswith("NOVA.output"):
            try:
                content = l[12:-1].strip()
                if "+" in content and ('"' in content or "'" in content):
                    for var in list(self.variables.keys()):
                        if f"str({var})" in content: content = content.replace(f"str({var})", f"{{{var}}}")
                        elif var in content and not f'"{var}"' in content and not f"'{var}'" in content:
                            content = re.sub(r'\b' + var + r'\b', f"{{{var}}}", content)
                    content = content.replace("+", "").replace('"', '').replace("'", "").strip()
                    content = f'f"{content}"'
                result = eval(content, {"__builtins__": __builtins__}, self.variables)
                print(f"{C_OUT}{result}{RESET}")
            except:
                content_clean = l[12:-1].strip().replace('"', '').replace("'", "")
                if content_clean in self.variables: print(f"{C_OUT}{self.variables[content_clean]}{RESET}")
                else: print(f"{C_ERR}RuntimeError: Unresolved token symbol{RESET}")

    def start_repl(self):
        # Exact Python Standard Vibe Header
        current_date = datetime.datetime.now().strftime("%b %d %Y, %H:%M:%S")
        print(f"Nova 10.0.0 Core Compiler Core (production/stable, {current_date})")
        print("[Clang 16.0.6 (Android Termux Shared Build)] on linux")
        print("Type \"help\", \"copyright\" or \"credits\" for more information.")
        print("Use \"RUN\" on a blank line to execute buffered blocks.\n")
        buffer = []
        while True:
            try:
                prompt = f"{C_PROMPT}>>> {RESET}" if not buffer else ""
                user_input = input(prompt)
                if user_input.strip() == "exit()": break
                if user_input.strip() == "AI_TEST":
                    if buffer:
                        raw_block = "\n".join(buffer)
                        self.trigger_ollama_pipeline(raw_block)
                        for block_line in buffer: self.execute_line(block_line)
                        buffer = []
                    else: print(f"{C_ERR}Buffer empty.{RESET}")
                    continue
                if user_input.strip() == "RUN":
                    for block_line in buffer: self.execute_line(block_line)
                    buffer = []
                    continue
                if user_input.strip(): buffer.append(user_input)
            except (KeyboardInterrupt, EOFError): break

if __name__ == "__main__":
    interpreter = NovaV10Engine()
    interpreter.start_repl()
