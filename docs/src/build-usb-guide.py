"""Builds docs/USB-Install-Guide.pdf from USB-Install-Guide.md.

    python3 docs/src/build-usb-guide.py      (needs the "markdown" package and Google Chrome or Chromium)
"""
import os, re, shutil, subprocess, sys, markdown

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPO = "https://github.com/CKOCI13/Nomadic-D1-and-D2-monitor-on-Victron-Cerbo-GX-MK2/blob/main/"

md = open(os.path.join(ROOT, "USB-Install-Guide.md"), encoding="utf-8").read()
md = "\n".join(l for l in md.splitlines() if "Printable version" not in l)   # the PDF doesn't link to itself
md = md.replace("- [ ] ", "- ☐ ")
md = re.sub(r"\]\((?!https?://)([^)]+)\)", lambda m: "](" + REPO + m.group(1) + ")", md)  # links work from paper/PDF
body = markdown.markdown(md, extensions=["tables"])

css = """
@page { size: Letter; margin: 0.6in 0.65in; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10.5pt; line-height: 1.4; color: #1a1a1a; }
h1 { font-size: 19pt; color: #0b4f8a; border-bottom: 3px solid #0b4f8a; padding-bottom: 4px; margin: 0 0 8px; }
h2 { font-size: 13.5pt; color: #0b4f8a; margin: 16px 0 6px; break-after: avoid; }
p, li { margin: 4px 0; }
ul { padding-left: 20px; }
li { list-style: none; } ol li { list-style: decimal; }
ul > li:not(:has(> input))::before { content: ""; }
blockquote { margin: 8px 0; padding: 6px 12px; background: #eef5fb; border-left: 4px solid #0b4f8a; }
blockquote p { margin: 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0; break-inside: avoid; }
th, td { border: 1px solid #b8c4ce; padding: 5px 7px; text-align: left; vertical-align: top; }
th { background: #e3edf5; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9.2pt; background: #f1f3f5; padding: 0 3px; border-radius: 3px; }
a { color: #0b4f8a; }
hr { border: 0; border-top: 1px solid #ccd5dc; margin: 12px 0; }
sub { color: #666; }
"""
# Plain bullets for lists that aren't checklists
html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>USB Install Guide</title><style>{css}</style></head><body>{body}</body></html>"
html = html.replace("<li>", "<li>• ").replace("<li>• ☐", "<li>☐")
html = re.sub(r"<ol>(.*?)</ol>", lambda m: "<ol>" + m.group(1).replace("<li>• ", "<li>") + "</ol>", html, flags=re.S)

tmp = os.path.join(ROOT, "docs", "src", "_usb-guide.html")
open(tmp, "w", encoding="utf-8").write(html)
chrome = next((c for c in ("google-chrome", "chromium", "chromium-browser") if shutil.which(c)), None)
if not chrome:
    sys.exit("Needs Google Chrome or Chromium")
out = os.path.join(ROOT, "docs", "USB-Install-Guide.pdf")
subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                "--print-to-pdf=" + out, "file://" + tmp], check=True, capture_output=True)
os.remove(tmp)
print("Made", out)
