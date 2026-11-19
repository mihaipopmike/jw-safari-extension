# Testele extensiei JW Safari (6.1.6, pasul 3 din audit) – rulează extensia într-un Safari simulat (Chromium, dimensiuni iPhone și iPad).
# Folosire:  python3 tests/test_extensie.py JW_Safari_Extension.user.js
# Fiecare verificare spune „ok” sau „GREȘIT”; la sfârșit, codul de ieșire e 1 dacă a picat ceva.
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import *
SCRIPT = sys.argv[1] if len(sys.argv) > 1 else 'JW_Safari_Extension.user.js'
FAIL = []
def check(name, cond, extra=''):
    print(('ok      ' if cond else 'GREȘIT  ') + name + (('  · ' + str(extra)) if extra else '')); (None if cond else FAIL.append(name))
def tile(page, k):
    page.evaluate(f'(()=>{{const R={R}; if(!R.querySelector(".sheet.menu")) R.querySelector(".fab").click();}})()'); page.wait_for_timeout(900)
    page.evaluate(f'(()=>{{const t=[...{R}.querySelectorAll(".sheet.menu .tile")].find(t=>t.dataset.k==="{k}"); t && t.click();}})()')
def close(page): page.evaluate(f'(()=>{{const c={R}.querySelector(".sheet .head .circ[aria-label=\'Închide\']"); c && c.click();}})()'); page.wait_for_timeout(700)
HIT = f'''(()=>{{ const R={R}; const sh=[...R.querySelectorAll('.sheet')].filter(x=>x.getAttribute('aria-hidden')!=='true').pop() || R;
  const els=[...sh.querySelectorAll('button, [role=button]')].filter(e=>{{const r=e.getBoundingClientRect(); return !e.closest('svg') && r.width>0 && r.top>0 && r.bottom<innerHeight;}});
  return els.filter(e=>{{const r=e.getBoundingClientRect(), cx=r.left+r.width/2, cy=r.top+r.height/2; let ok=0;
    for (const [dx,dy] of [[0,-21],[0,21],[-21,0],[21,0]]) {{ const t=R.elementFromPoint(cx+dx,cy+dy); if (t && (t===e || e.contains(t))) ok++; }} return ok<3; }}).length; }})()'''
with sync_playwright() as p:
    for dev in ('iphone', 'ipad'):
        b, ctx, page, logs = open_page(p, SCRIPT, dev=dev, extra={'hints': {'sumSwipe': 1}}); page.wait_for_timeout(1200)
        check(f'{dev}: butonul JW apare', page.evaluate(f'!!{R}.querySelector(".fab")'))
        page.evaluate(f'{R}.querySelector(".fab").click()'); page.wait_for_timeout(900)
        check(f'{dev}: fereastra principală are plăci', page.evaluate(f'{R}.querySelectorAll(".sheet.menu .tile").length') >= 6)
        check(f'{dev}: ținte de atingere de 44 px (fereastra principală)', page.evaluate(HIT) == 0, page.evaluate(HIT))
        page.evaluate(f'{R}.querySelector(".sheet.menu .head .circ[aria-label=\'Ajutor\']").click()'); page.wait_for_timeout(400)
        page.mouse.click(60, 200); page.wait_for_timeout(300)
        check(f'{dev}: ajutorul („?”) se închide la atingere', page.evaluate(f'{R}.querySelectorAll(".hpov").length') == 0)
        close(page)
        tile(page, 'sum'); page.wait_for_timeout(7000)
        s = page.evaluate(f'''(()=>{{const s={R}.querySelector('.sheet.smsum'); return s ? [s.querySelectorAll('li.smit').length, s.querySelectorAll('.smwvh,.smwvlay').length, !s.querySelector('.sminfo').hidden] : null}})()''')
        check(f'{dev}: Rezumatul arată ideile după val', bool(s) and s[0] > 0 and s[1] == 0, s)
        check(f'{dev}: informațiile de jos apar după val', bool(s) and s[2])
        check(f'{dev}: firul de navigare („Unelte”) în antet', page.evaluate(f'(({R}.querySelector(".sheet .head .crumbs")||{{}}).textContent||"").includes("Unelte")'))
        close(page)
        tile(page, 'map'); page.wait_for_timeout(3500)
        check(f'{dev}: Locuri arată harta', page.evaluate(f'!!{R}.querySelector(".sheet .mtmap.ready, .sheet .mtmap img, .sheet .mtmap svg")'))
        page.evaluate(f'(()=>{{const e={R}.querySelector(".mtexp"); e && e.click();}})()'); page.wait_for_timeout(2500)
        check(f'{dev}: harta extinsă are panoul locurilor', page.evaluate(f'!!{R}.querySelector(".sheet.mtfull .mtpanel")'))
        close(page)
        tile(page, 'time'); page.wait_for_timeout(3500)
        check(f'{dev}: Cronologie arată anii', page.evaluate(f'{R}.querySelectorAll(".sheet .mtrow").length') > 0)
        close(page)
        check(f'{dev}: nicio eroare JavaScript', not page.evaluate('window.__errs'), page.evaluate('window.__errs'))
        b.close()
print('\n' + ('TOATE TESTELE AU TRECUT' if not FAIL else f'{len(FAIL)} TESTE AU PICAT'))
sys.exit(1 if FAIL else 0)
