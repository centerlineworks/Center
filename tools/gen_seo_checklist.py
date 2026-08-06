import io, os, re, sys
base = os.path.dirname(os.path.abspath(__file__))
def b64(n):
    return open(os.path.join(base, n + '.b64')).read().strip()
tpl = open(os.path.join(base, 'seo_page.html'), encoding='utf-8').read()
tpl = tpl.replace('__ARCHIVO__', b64('archivo')).replace('__FRAUNCES__', b64('fraunces'))
out = os.path.join(base, 'seo-checklist.html')
open(out, 'w', encoding='utf-8').write(tpl)
print('wrote', out, len(tpl)//1024, 'KB')
