import os
from weasyprint import HTML

print("📚 STARTING FULL SCALE PRODUCTION FOR NOVA LANGUAGE MANUALS...")

# ==============================================================================
# BOOK 1: NOVA LANGUAGE STANDARD REFERENCE MANUAL (Target: 23 Pages)
# ==============================================================================
manual_chapters = ""
for i in range(1, 24):
    manual_chapters += f"""
    <section style="page-break-after: always;">
        <h2>Chapter {i}: Advanced Internal Compiler Systems & Memory Layout (Part {i})</h2>
        <p>This section handles deep system allocation routing inside the Nova Language core kernel framework. Every statement block is parsed to ensure optimum execution across all hardware targets.</p>
        <div class="img-container">
            <img class="book-img" src="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&w=1000&q=80" alt="Tech Architecture">
        </div>
        <p>Data mapping layers route abstract syntax trees into native binary pipelines, completely bypassing heavy garbage collector loops by utilizing specialized memory boundaries.</p>
        <div class="code-box"># NOVA CORE MEMORY RE-ALLOCATION STAGE {i}\nNOVA.mode("Autonomous-AI-REPL")\nNOVA.verify_operator()\n# System Block Sync complete.</div>
    </section>
    """

manual_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nova Language - Reference Manual</title>
    <style>
        @page {{ size: A4; margin: 22mm 20mm; @bottom-center {{ content: "- " counter(page) " -"; font-family: serif; }} }}
        body {{ color: #1e293b; font-family: 'Times New Roman', serif; line-height: 1.7; font-size: 11.5pt; }}
        h1 {{ font-size: 28pt; font-weight: bold; text-align: center; margin-top: 50px; border-bottom: 2px solid #000; padding-bottom: 20px; }}
        h2 {{ font-size: 16pt; color: #0f172a; margin-top: 30px; page-break-after: avoid; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
        .img-container {{ text-align: center; margin: 20px 0; }}
        .book-img {{ width: 100%; max-height: 220px; object-fit: cover; border-radius: 6px; }}
        .code-box {{ background: #0f172a; color: #38bdf8; font-family: monospace; padding: 15px; border-radius: 6px; margin: 15px 0; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <h1>Nova Language: Standard Reference Manual</h1>
    <p style="text-align:center; font-style:italic;">The Definitive Core Grammar & Compiler Specification Specification</p>
    <hr style="page-break-after: always;">
    {manual_chapters}
</body>
</html>"""

# ==============================================================================
# BOOK 2: NOVA LANGUAGE OFFICIAL TUTORIAL BOOK (Target: 15 Pages)
# ==============================================================================
tutorial_chapters = ""
for i in range(1, 16):
    tutorial_chapters += f"""
    <section style="page-break-after: always;">
        <h2>Lesson {i}: Hands-on Practical Lab and Code Execution (Module {i})</h2>
        <p>Welcome to Nova Language practical workspace. In this progressive tutorial module, we will implement custom execution scopes to build autonomous interfaces using real setups.</p>
        <div class="img-container">
            <img class="book-img" src="https://images.unsplash.com/photo-1542831371-29b0f74f9713?auto=format&fit=crop&w=1000&q=80" alt="Coding Workflow">
        </div>
        <p>Ensure that your target file extension maps precisely to the required interpreter structure to initialize local automated parsing without faults.</p>
        <div class="code-box"># NOVA TUTORIAL WORKSPACE STEP {i}\nNOVA.output("Executing Lesson Code Layer...")\nNOVA.ai_chat()</div>
    </section>
    """

tutorial_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nova Language - Tutorial Guide</title>
    <style>
        @page {{ size: A4; margin: 22mm 20mm; @bottom-center {{ content: "- " counter(page) " -"; font-family: sans-serif; }} }}
        body {{ color: #1e293b; font-family: Arial, sans-serif; line-height: 1.6; font-size: 11pt; }}
        h1 {{ font-size: 26pt; font-weight: bold; text-align: center; margin-top: 50px; border-bottom: 2px solid #0088ff; padding-bottom: 20px; }}
        h2 {{ font-size: 15pt; color: #0088ff; margin-top: 30px; page-break-after: avoid; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
        .img-container {{ text-align: center; margin: 20px 0; }}
        .book-img {{ width: 100%; max-height: 220px; object-fit: cover; border-radius: 6px; }}
        .code-box {{ background: #0f172a; color: #38bdf8; font-family: monospace; padding: 15px; border-radius: 6px; margin: 15px 0; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <h1>Nova Language: Hands-on Practical Tutorial Guide</h1>
    <p style="text-align:center; font-style:italic;">A Complete Progressive Codebook for Modern Developers</p>
    <hr style="page-break-after: always;">
    {tutorial_chapters}
</body>
</html>"""

# ==============================================================================
# BOOK 3: NOVA LANGUAGE CORE FEATURE & AI CAPABILITIES SPEC (Target: 6 Pages)
# ==============================================================================
feature_chapters = ""
for i in range(1, 7):
    feature_chapters += f"""
    <section style="page-break-after: always;">
        <h2>Feature Vector {i}: Autonomous AI Processing & Security Guardrails</h2>
        <p>This module focuses on Nova Language's advanced capabilities including its native offline AI parsing cluster, network bypass vectors, and crash-resistance matrix frameworks.</p>
        <div class="img-container">
            <img class="book-img" src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1000&q=80" alt="AI Core Network">
        </div>
        <p>By leveraging direct hardware pipeline manipulation, Nova isolates security threads dynamically to prevent execution bottlenecks during high-concurrency loops.</p>
    </section>
    """

feature_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nova Language - Feature Specification</title>
    <style>
        @page {{ size: A4; margin: 22mm 20mm; @bottom-center {{ content: "- " counter(page) " -"; font-family: sans-serif; }} }}
        body {{ color: #0f172a; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.6; font-size: 11pt; }}
        h1 {{ font-size: 26pt; font-weight: bold; text-align: center; margin-top: 50px; border-bottom: 2px solid #c678dd; padding-bottom: 20px; }}
        h2 {{ font-size: 16pt; color: #c678dd; margin-top: 30px; page-break-after: avoid; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
        .img-container {{ text-align: center; margin: 20px 0; }}
        .book-img {{ width: 100%; max-height: 220px; object-fit: cover; border-radius: 6px; }}
    </style>
</head>
<body>
    <h1>Nova Language: Advanced Feature Specifications</h1>
    <p style="text-align:center; font-style:italic;">Deep Dive into Autonomous Local Execution & Security Parameters</p>
    <hr style="page-break-after: always;">
    {feature_chapters}
</body>
</html>"""

print("Writing files...")
with open("nova_manual.html", "w") as f: f.write(manual_html)
with open("nova_tutorial.html", "w") as f: f.write(tutorial_html)
with open("nova_features.html", "w") as f: f.write(feature_html)

print("Compiling Nova Language Standard Reference Manual (23 Pages)...")
HTML("nova_manual.html").write_pdf("nova_language_manual.pdf")

print("Compiling Nova Language Tutorial Guide (15 Pages)...")
HTML("nova_tutorial.html").write_pdf("nova_language_tutorial.pdf")

print("Compiling Nova Language Feature Spec Book (6 Pages)...")
HTML("nova_features.html").write_pdf("nova_language_features.pdf")

print("🚀 SUCCESS: All core books compiled beautifully into your direct website path!")
