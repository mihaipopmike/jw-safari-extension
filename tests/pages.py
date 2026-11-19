# Pagini de test scrise de noi (texte inventate), cu structura paginilor WOL reale
def wol_article():
    paras = []
    subs = ['Ce ne învață grădina', 'Cum putem fi răbdători', 'Ce face un prieten bun']
    n = 1
    body = ''
    for si, st in enumerate(subs):
        body += f'<h2 id="h{si}">{st}</h2>'
        for k in range(4):
            body += (f'<p data-pid="{n}" id="p{n}" class="p{n}"><span class="parNum" data-pnum="{n}">{n}</span> '
                     f'Grădinarul răbdător udă plantele în fiecare dimineață și așteaptă liniștit să crească. '
                     f'Prietenii buni își ascultă unii altora problemele și se ajută cu bucurie în zilele grele. '
                     f'Când învățăm ceva nou, ne gândim cum putem folosi lecția în viața de zi cu zi, pas cu pas. '
                     f'Răbdarea ne ajută să rămânem calmi chiar și atunci când lucrurile nu merg cum am vrea noi.</p>')
            n += 1
    return f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lecții din grădină — BIBLIOTECA ONLINE Watchtower</title>
<style>body{{font:17px/1.5 Georgia,serif;margin:0;background:#fff;color:#222}}header.nav{{height:56px;background:#3d3d3d;color:#fff;display:flex;align-items:center;padding:0 16px}}#article{{padding:16px 20px}}</style></head>
<body><header class="nav">wol.jw.org (test)</header><div id="content"><article id="article"><header><h1>Lecții din grădină</h1><p class="pubRefs"><a href="#">CÂNTAREA 44 Bucuria seceratului</a></p></header><p data-pid="90" id="p90">Avraam și Sara au avut încredere, iar Isaac și Iacov au învățat de la ei. Rebeca și Iosif au arătat și ei răbdare. Cântarea 12 Marele Creator ne amintește de bunătate.</p><p data-pid="91" id="p91">Familia a plecat din Ierusalim spre Betleem, apoi a ajuns în Egipt și s-a întors la Nazaret, lângă Marea Galileii, în anul 1914 și apoi în 607 î.e.n., când Regatul lui Dumnezeu și răscumpărarea erau subiectul discuției. (Citește <a class="b" data-bid="1" href="#">Ioan 3:16</a> <a class="b" data-bid="9" href="#">+</a>; <a class="b" data-bid="2" href="#">Psalmul 23:1</a>, <a class="b" data-bid="3" href="#">4</a> <a class="b" data-bid="8" href="#">+</a>.)</p><p class="qu" data-pid="95" id="p95">1. Ce putem învăța din răbdarea grădinarului?</p><p class="qu" data-pid="96" id="p96">2. Cum ne ajută prietenii buni?</p>{body}</article></div></body></html>'''

def wol_bible():
    vs = ''
    words = ['La început a fost liniște peste ape și lumina a apărut pe cer.', 'Pământul era gol, iar vântul trecea ușor peste câmpii.',
             'Apoi s-au ivit ierburi verzi și pomi cu fructe dulci.', 'Păsările au început să zboare deasupra pământului.',
             'Peștii au umplut râurile și mările adânci.', 'Animalele mari și mici s-au răspândit pe dealuri.']
    n = 1; v = 1
    for p in range(6):
        if p == 2: vs += '<h3 class="ss">Zilele de început</h3>'
        if p == 4: vs += '<h3 class="ss">Ziua a șasea</h3>'
        inner = ''
        for k in range(3):
            inner += f'<span class="v" id="v1-1-{v}-1"><a class="vl" href="#">{v}</a> {words[(v-1)%6]} Acesta este un text de test scris pentru verificare, cu câteva cuvinte în plus. </span>'
            v += 1
        vs += f'<p class="sb" data-pid="{n}" id="p{n}">{inner}</p>'; n += 1
    return f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Geneza 1 — BIBLIOTECA ONLINE Watchtower</title>
<style>body{{font:17px/1.5 Georgia,serif;margin:0;background:#fff;color:#222}}header.nav{{height:56px;background:#3d3d3d;color:#fff;display:flex;align-items:center;padding:0 16px}}#article{{padding:16px 20px}}</style></head>
<body><header class="nav">wol.jw.org (test)</header><div id="content"><article id="article"><header><h1>Geneza 1</h1></header>{vs}</article></div></body></html>'''

def jw_video():
    return '''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>O zi la grădina comunității | JW.ORG</title>
<style>body{font:17px/1.5 Georgia,serif;margin:0;background:#fff;color:#222}header.nav{height:56px;background:#3d3d3d;color:#fff;display:flex;align-items:center;padding:0 16px}
#article{padding:16px 20px}.video-js{position:relative;width:100%;aspect-ratio:16/9;border-radius:10px;overflow:hidden;background:linear-gradient(135deg,#5b7a8c,#2c3e4a 60%,#1b2730)}
.video-js::after{content:"";position:absolute;right:12%;top:18%;width:16%;aspect-ratio:1;border-radius:50%;background:rgba(255,220,150,.35)}</style></head>
<body><header class="nav">jw.org (test)</header><article id="article"><h1>O zi la grădina comunității</h1><div class="videoPlayerWrapper"><div class="video-js"><video style="width:100%;height:100%" preload="none"><track kind="subtitles" srclang="ro" label="Română" src="https://www.jw.org/test/sub.vtt"></video></div></div>
<p>Un scurt film de test despre vecini care îngrijesc împreună o grădină.</p></article></body></html>'''

def wol_home():
    def day(date, verse, body, active):
        return f'''<div class="tabContent{' active' if active else ''}" style="{'' if active else 'display:none'}"><header><h2>{date}</h2></header>
<p class="themeScrp"><em>{verse}</em></p><div class="bodyTxt"><p class="sb">{body}</p></div><p><a href="#">Să examinăm Scripturile în fiecare zi – 2026</a></p></div>'''
    b1 = ('Slujitorii auxiliari îndeplinesc o activitate importantă în congregație, iar Pavel i-a apreciat mult pe acești frați loiali din Filipi. '
          'Indiferent de vârstă, mulți frați își îndeplinesc cu bucurie acest rol și se gândesc la iubirea celor din congregație. '
          'Un frate tânăr a fost numit la 18 ani, iar altul a primit numirea după ce a împlinit 50 de ani, și amândoi se bucură de privilegiu. '
          'Dacă ești botezat, ți-ai putea stabili obiectivul de a sluji și tu în acest fel, cu răbdare și cu bucurie, pentru frații tăi.')
    b2 = ('Regele Ezechia a aflat că are o boală gravă și s-a rugat fierbinte la Iehova, iar Iehova i-a ascultat rugăciunea și l-a vindecat. '
          'El a promis și că va salva Ierusalimul din mâinile asirienilor, arătând multă îndurare față de rege și față de popor.')
    return f'''<!doctype html><html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Watchtower – BIBLIOTECĂ ONLINE</title><style>body{{font:17px/1.5 Georgia,serif;margin:0;background:#fff;color:#222}}header.nav{{height:56px;background:#3d3d3d;color:#fff;display:flex;align-items:center;padding:0 16px}}#content{{padding:16px 20px}}</style></head>
<body><header class="nav">wol.jw.org (test)</header><div id="content"><h1>Bun venit!</h1><p>Acesta este un instrument de cercetare a publicațiilor (text de test).</p>
<div id="dailyText">{day('Marți, 3 noiembrie', 'Text de test pentru ziua de ieri. (Fap. 1:8)', b2, False)}{day('Miercuri, 4 noiembrie', 'Este mai multă fericire în a da decât în a primi. (Fap. 20:35)', b1, True)}{day('Joi, 5 noiembrie', 'Text de test pentru ziua de mâine. (2 Regi 20:3)', b2, False)}</div></div></body></html>'''
