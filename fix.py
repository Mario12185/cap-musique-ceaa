import os, glob, re
FIXES = {
    'Ã©': 'é', 'Ã¨': 'è', 'Ã ': 'à', 'Ã´': 'ô', 'Ã§': 'ç', 'Ãª': 'ê', 'Ã«': 'ë',
    'Ã¯': 'ï', 'Ã¹': 'ù', 'Ã¢': 'â', 'Ã®': 'î', 'Ã¶': 'ö', 'Ã»': 'û', 'Ã¼': 'ü',
    'Ã‰': 'É', 'Ãˆ': 'È', 'Ã€': 'À', 'Ã„': 'Ä', 'Ã‹': 'Ë', 'ÃŽ': 'Î', 'Ã"': 'Ó',
    'Ã–': 'Ö', 'Ã™': 'Ù', 'Ãš': 'Ú', 'Ãœ': 'Ü', 'ÃŸ': 'ß', 'Ã¡': 'á', 'Ãº': 'ú',
    'ÃƒÂ©': 'é', 'ÃƒÂ¨': 'è', 'ÃƒÂ ': 'à', 'ÃƒÂ´': 'ô', 'ÃƒÂ§': 'ç', 'ÃƒÂª': 'ê',
    'ÃƒÂ«': 'ë', 'Ã¢â‚¬': '', 'Ã‚Â': '', 'Ãƒ': '', 'Å"': 'œ'
}
for f in glob.glob('**/*.html', recursive=True):
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as h: t = h.read()
        orig = t
        for b,g in FIXES.items(): t = t.replace(b,g)
        t = re.sub(r'<meta[^>]*charset[^>]*>','',t,flags=re.IGNORECASE)
        t = t.replace('<head>','<head><meta charset="UTF-8">',1)
        if t != orig:
            with open(f, 'w', encoding='utf-8', newline='') as h: h.write(t)
            print('✅', os.path.basename(f))
    except Exception as e: print('❌', f, e)
print('🎉 ENCODAGE CORRIGÉ')