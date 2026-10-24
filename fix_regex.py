import os
import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # We use regex to find the corrupted strings since they always precede specific words in the HTML.
    
    # Call icon: <a href="tel:..." ...>XYZ Call +91
    content = re.sub(r'>[^\s<>]+ Call \+91', '>📞 Call +91', content)
    
    # WhatsApp icon: ...>XYZ WhatsApp Consultation
    content = re.sub(r'>[^\s<>]+ WhatsApp Consultation', '>💬 WhatsApp Consultation', content)
    
    # "Book Your Consultation Today" has folded hands: XYZ Book Your Consultation
    content = re.sub(r'>[^\s<>]+ Book Your Consultation', '>🙏 Book Your Consultation', content)
    
    # Maa Baglamukhi Anushthan card has 🙏
    content = re.sub(r'class="text-3xl mb-3">[^<>]+</div><h3[^>]*>Maa Baglamukhi Anushthan', 'class="text-3xl mb-3">🙏</div><h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Maa Baglamukhi Anushthan', content)
    
    # Kalsarpa Dosh has 🐍
    content = re.sub(r'class="text-3xl mb-3">[^<>]+</div><h3[^>]*>Kalsarpa Dosh Puja', 'class="text-3xl mb-3">🐍</div><h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Kalsarpa Dosh Puja', content)
    
    # Vedic Astrology has ⭐
    content = re.sub(r'class="text-3xl mb-3">[^<>]+</div><h3[^>]*>Vedic Kundali Reading', 'class="text-3xl mb-3">⭐</div><h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Vedic Kundali Reading', content)
    
    # Baglamukhi Havan has 🔥
    content = re.sub(r'class="text-3xl mb-3">[^<>]+</div><h3[^>]*>Baglamukhi Havan', 'class="text-3xl mb-3">🔥</div><h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Baglamukhi Havan', content)
    
    # Online Puja Services has 🌎
    content = re.sub(r'class="text-3xl mb-3">[^<>]+</div><h3[^>]*>Online Puja Services', 'class="text-3xl mb-3">🌎</div><h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Online Puja Services', content)
    
    # Vastu Consultation has 🏠
    content = re.sub(r'class="text-3xl mb-3">[^<>]+</div><h3[^>]*>Vastu Consultation', 'class="text-3xl mb-3">🏠</div><h3 class="font-serif text-lg font-bold text-amber-300 mb-2">Vastu Consultation', content)
    
    # Footer has ©
    content = re.sub(r'>[^<>]*? 2026 Pandit Lakhan Sharma', '>© 2026 Pandit Lakhan Sharma', content)

    # Some blogs have 🛕 for Online Puja Today
    content = re.sub(r'>[^\s<>]+ Book Your Online Puja Today', '>🛕 Book Your Online Puja Today', content)

    # And ⭐ Get Your Kundali Read
    content = re.sub(r'>[^\s<>]+ Get Your Kundali Read by Pandit Lakhan Sharma', '>⭐ Get Your Kundali Read by Pandit Lakhan Sharma', content)

    # And 🔮 for Astrology
    content = re.sub(r'>[^\s<>]+ Vedic Astrology Specialist', '>🔮 Vedic Astrology Specialist', content)

    # Go to Homepage 🏠
    content = re.sub(r'>[^\s<>]+ Go to Homepage', '>🏠 Go to Homepage', content)

    # Book Your Baglamukhi Anushthan 🙏
    content = re.sub(r'>[^\s<>]+ Book Your Baglamukhi Anushthan', '>🙏 Book Your Baglamukhi Anushthan', content)

    if original != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
print("Done regex fix")
