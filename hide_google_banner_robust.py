import glob

css_to_add = """
<style>
/* Robust Google Translate Hide */
body { top: 0 !important; }
.skiptranslate iframe { display: none !important; visibility: hidden !important; height: 0 !important; }
#goog-gt-tt { display: none !important; }
.goog-te-banner-frame { display: none !important; visibility: hidden !important; }
body { position: static !important; }
</style>
"""

html_files = glob.glob("*.html")
count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "/* Robust Google Translate Hide */" not in content:
        content = content.replace("</head>", css_to_add + "\n</head>")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files.")
