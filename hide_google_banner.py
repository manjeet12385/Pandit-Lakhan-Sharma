import os
import glob

css_to_add = """
<style>
/* Hide Google Translate Banner and Reset Body Top */
.goog-te-banner-frame.skiptranslate { display: none !important; }
body { top: 0px !important; }
.goog-tooltip { display: none !important; }
.goog-tooltip:hover { display: none !important; }
.goog-text-highlight { background-color: transparent !important; border: none !important; box-shadow: none !important; }
</style>
"""

html_files = glob.glob("*.html")

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* Hide Google Translate Banner" not in content:
        if "</head>" in content:
            content = content.replace("</head>", css_to_add + "</head>")
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            
print(f"Updated {count} HTML files.")
