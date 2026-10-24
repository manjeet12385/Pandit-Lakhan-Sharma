import os
import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Pune specific
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>', 'class="text-3xl mb-3">🙏</div>', content, count=1)
    # Actually wait, they have different icons. 
    # Pune icons in order: 🙏, 🐍, ⭐, 🔥, 🌎, 🏠
    # Instead of direct string replacement, I'll use re.sub with exact context if possible.
    # Let's just replace them based on the heading that follows them in Pune:
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>\s*<h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Maa Baglamukhi Anushthan', 'class="text-3xl mb-3">🙏</div>\n        <h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Maa Baglamukhi Anushthan', content)
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>\s*<h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Kalsarpa Dosh Puja', 'class="text-3xl mb-3">🐍</div>\n        <h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Kalsarpa Dosh Puja', content)
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>\s*<h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Vedic Kundali Reading', 'class="text-3xl mb-3">⭐</div>\n        <h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Vedic Kundali Reading', content)
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>\s*<h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Baglamukhi Havan', 'class="text-3xl mb-3">🔥</div>\n        <h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Baglamukhi Havan', content)
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>\s*<h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Online Puja Services', 'class="text-3xl mb-3">🌎</div>\n        <h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Online Puja Services', content)
    content = re.sub(r'class="text-3xl mb-3">[^\w<>\s]*</div>\s*<h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Vastu Consultation', 'class="text-3xl mb-3">🏠</div>\n        <h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Vastu Consultation', content)
    
    # Hyderabad specific
    content = re.sub(r'>[^\w<>\s]* WhatsApp</a>', '>💬 WhatsApp</a>', content)
    
    # 404 specific
    content = re.sub(r'<div class="symbol">[^\w<>\s]*</div>', '<div class="symbol">🔱</div>', content)
    content = re.sub(r'>[^\w<>\s]* Go to Homepage', '>🏠 Go to Homepage', content)
    content = re.sub(r'>[^\w<>\s]* Contact on WhatsApp', '>💬 Contact on WhatsApp', content)
    content = re.sub(r'>[^\w<>\s]* Quick Links', '>🙏 Quick Links', content)

    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed remnants {file}")
