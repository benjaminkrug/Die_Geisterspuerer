"""
Maschinelle Vorpruefung fuer den Logik-Pruefplan.

Findet KANDIDATEN, keine Fehler. Jeder Treffer muss im Kontext gelesen werden.
Siehe Dokumentation/Logik_Pruefplan.md, Regel 1.

Verwendung:
    py Scripts/pruefe_logik.py 1          # Band 1
    py Scripts/pruefe_logik.py 1 --alle   # auch die rauschanfaelligen Checks

★ WICHTIG - ERZAEHLERTEXT vs. DIALOG
  Fast alle Checks laufen NUR auf dem Erzaehlertext. Figuren duerfen alles sagen:
  falsche Grammatik, Vermutungen ueber andere, Wiederholungen. Wer den Dialog
  mitprueft, produziert fast nur Fehltreffer (real getestet: der erste
  POV-Treffer in Band 1 war eine Dialogzeile).
"""

import os
import re
import sys
from collections import Counter

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ERLAUBTE_SPRECHVERBEN = {"sagte", "fluesterte", "flüsterte", "rief", "murmelte", "zischte"}
VERDAECHTIGE_SPRECHVERBEN = [
    "keuchte", "hauchte", "schnaubte", "erwiderte", "entgegnete", "stammelte",
    "erklaerte", "erklärte", "bemerkte", "konstatierte", "entfuhr", "presste",
]
# ⚠️ Wortgrenzen sind Pflicht. Ohne \b matcht "Leiche" das Wort "gleichen"
# und "schleichend" - beim ersten Testlauf an Band 1 waren 4 von 6 Treffern
# genau solche Substring-Fehltreffer.
VERBOTENE_BEGRIFFE = [
    r"\bD(ä|ae)mon", r"\bteuflisch", r"\bsatanisch", r"\bH(ö|oe)lle\b", r"\bFluch\b",
    r"\bverflucht", r"\bBestie", r"\bUntot", r"\bZombie", r"\bVampir", r"\bExorz",
    r"\bVerwesung", r"\bLeiche", r"\bKadaver", r"\breines B(ö|oe)se",
    r"\bb(ö|oe)se[rs]? (Geist|Wesen|Macht)",
]
# ⚠️ Dieser Katalog erzeugt FEHL-NEGATIVE, wenn er zu eng ist. Beim Lauf gegen
# Band 2-5 meldete er bis zu 8 Kapitel "ohne Reaktion" - aber Band 4 K3 enthaelt
# "Schatten durfte nicht mit hinein", was ein voellig gueltiger Beat ist.
# Ein gemeldetes Kapitel heisst deshalb NUR: hier nachsehen. Nie: hier fehlt was.
SCHATTEN_REAKTION = (
    r"knurr|Nackenfell|str(ä|ae)ubt|winsel|zog|zerrte|rannte|blieb stehen|weigerte|"
    r"bellte|hob den Kopf|Ohren|dr(ä|ae)ngte|kratzte|heulte|riss sich|leckte|"
    r"schnupperte|zitterte|Krallen|Pfote|Fell|Schnauze|Halsband|sprang|duckte|"
    # nachgetragen 2026-07-18 nach Fehl-negativen:
    r"durfte nicht|blieb (drau(ß|ss)en|zur(ü|ue)ck|liegen|sitzen)|folgte|trottete|"
    r"lief|sah (sie|ihn|zu)|legte sich|schlief|wartete|st(ü|ue)rmte|schnaufte|"
    r"presste|dr(ü|ue)ckte|stupste|jaulte|fiepte|hechelte|witterte|sto(ß|ss)"
)


# ── Textaufbereitung ─────────────────────────────────────────────────────────

def lade(band):
    p = os.path.join(_ROOT, f"Band{band}", "Manuskript",
                     f"Manuskript_Band{band}_Komplett.md")
    if not os.path.exists(p):
        raise SystemExit(f"Nicht gefunden: {p}")
    return open(p, encoding="utf-8").read()


def kapitel(text):
    """[(nr, titel, body), ...]"""
    out = []
    for m in re.finditer(r"^# Kapitel (\d+)\s*[–-]\s*(.+?)$(.*?)(?=^# Kapitel |\Z)",
                         text, re.M | re.S):
        out.append((int(m.group(1)), m.group(2).strip(), m.group(3)))
    return out


def nur_erzaehler(text):
    """Entfernt alle Figurenrede. Siehe Kopfkommentar."""
    text = re.sub(r"[„\"][^“\"]*[“\"]", " ", text)
    return text


def saetze(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text))
            if s.strip()]


def zeige(titel, treffer, limit=12, hinweis=""):
    print(f"\n--- {titel} ---")
    if hinweis:
        print(f"    {hinweis}")
    if not treffer:
        print("    keine Treffer")
        return 0
    print(f"    {len(treffer)} Kandidat(en):")
    for t in treffer[:limit]:
        s = t if isinstance(t, str) else str(t)
        print("      * " + s[:150])
    if len(treffer) > limit:
        print(f"      ... und {len(treffer)-limit} weitere")
    return len(treffer)


# ── Checks mit hoher Trefferquote ────────────────────────────────────────────

def check_kapiteltitel_serienweit(band):
    """Doppelte Kapiteltitel ueber ALLE Baende. Realer Fund: 'Der Keller' in B1 und B3."""
    tit = {}
    for b in range(1, 6):
        p = os.path.join(_ROOT, f"Band{b}", "Manuskript", f"Manuskript_Band{b}_Komplett.md")
        if not os.path.exists(p):
            continue
        for nr, t, _ in kapitel(open(p, encoding="utf-8").read()):
            tit.setdefault(t, []).append(f"B{b}K{nr}")
    return [f"{t!r} kommt vor in: {', '.join(v)}" for t, v in tit.items() if len(v) > 1]


def check_zeitangaben(text):
    """Haeufigster Fehler der Reihe (B5: 'zwei Jahre' statt vier Monate, 2x)."""
    tr = []
    for s in saetze(nur_erzaehler(text)):
        if re.search(r"\b(vor|seit|in|nach)\s+\w+\s+(Tag|Woche|Monat|Jahr)en?\b", s) \
           or re.search(r"\b(gestern|vorgestern|damals|letztes Jahr|voriges Jahr)\b", s):
            tr.append(s)
    return tr


def check_zahlen(text):
    """Zahlen, die zusammenpassen muessen (Markierungen, Kreuze, Geister)."""
    return [s for s in saetze(text)
            if re.search(r"\b(zw(ö|oe)lf|elf|zehn|neun|acht|sieben|sechs|f(ü|ue)nf|vier|drei|zwei|\d+)\b"
                         r"[^.!?]{0,45}(Markierung|Kreuz|durchgestrichen|blieben|Geist|Jahre alt)", s)]


def check_sprechverben(text):
    """Ein Sprechverb-Verstoss liegt nur vor, wenn das Verb REDE zuordnet.

    'Nora presste die Lippen zusammen' ist kein Verstoss, 'presste sie' nach
    einer Dialogzeile schon. Deshalb: nur Zeilen mit Anfuehrungszeichen.
    Beim ersten Testlauf an Band 1 waren ohne diesen Filter ~15 von 20
    Treffern normale Handlungsverben.
    """
    tr = []
    for zeile in text.split("\n"):
        if not re.search(r"[„\"]", zeile):
            continue
        for v in VERDAECHTIGE_SPRECHVERBEN:
            if re.search(r"\b" + v + r"\b", zeile):
                tr.append(f"[{v}] {zeile.strip()[:130]}")
    return tr


def check_verbotene_begriffe(text):
    tr = []
    for pat in VERBOTENE_BEGRIFFE:
        for m in re.finditer(r"[^.!?\n]*" + pat + r"[^.!?\n]*[.!?]", text, re.I):
            tr.append(m.group(0).strip())
    return tr


def check_pov(text):
    """Serienregel: nur was Nora wahrnimmt. Innenleben anderer Figuren = Bruch.
    NUR Erzaehlertext - Figuren duerfen ueber andere spekulieren."""
    tr = []
    for s in saetze(nur_erzaehler(text)):
        if re.search(r"\b(Theo|Mama|Papa|Frau [A-Z]\w+|Herr [A-Z]\w+)\s+"
                     r"(dachte|wusste|f(ü|ue)hlte|sp(ü|ue)rte|hoffte|ahnte|verstand|"
                     r"begriff|erinnerte sich|beschloss)\b", s):
            tr.append(s)
    return tr


def check_schatten(text):
    """Pro Kapitel eine REAKTION, nicht nur eine Erwaehnung."""
    fehlt = []
    for nr, titel, body in kapitel(text):
        ok = False
        for s in saetze(body):
            if re.search(r"\bSchatten\b|\b[Hh]und\b", s) and re.search(SCHATTEN_REAKTION, s):
                ok = True
                break
        if not ok:
            fehlt.append(f"K{nr} '{titel}' - keine erkennbare Reaktion")
    return fehlt


def check_cliffhanger(text):
    """Letzten Absatz jedes Kapitels zur Beurteilung ausgeben."""
    out = []
    for nr, titel, body in kapitel(text):
        abs_ = [p.strip() for p in body.split("\n\n")
                if p.strip() and p.strip() not in ("---", "***", "**ENDE**")]
        if abs_:
            out.append(f"K{nr:2d}: {abs_[-1][:120]}")
    return out


def check_wiederholte_saetze(text):
    """Woertlich identische Saetze ab 8 Woertern."""
    z = Counter(s for s in saetze(text) if len(s.split()) >= 8)
    return [f"{n}x: {s[:120]}" for s, n in z.items() if n > 1]


def check_vierte_wand(text):
    """★ Figuren oder Erzaehler sprechen ueber die BUECHER, in denen sie vorkommen.

    Realer Fund 2026-07-18: In Band 4 stand SECHS MAL "vier Baende" - Nora,
    Theo, Frau Silber und zweimal der Erzaehler. Alle im emotionalen Hoehepunkt
    (Wiederbegegnung mit Silber). Mit dem Buch in den Druck gegangen.

    ⚠️ Suche MUSS case-insensitive sein: vier der sechs Treffer waren
    kleingeschrieben mitten im Satz, zwei grossgeschrieben am Satzanfang
    ("Vier Baende lang war Frau Silber ..."). Ein case-sensitives Muster fand
    beim ersten Lauf nur vier von sechs.

    ★★ ZWEITER FUND 2026-07-18, beim Lese-Durchgang: Band 4 K16 enthielt eine
    SIEBTE Stelle - "dort, wo seit Band drei ein Satz stand". Das Muster oben
    hat sie NICHT gefunden, weil es Plural ("Baende") oder eine Ziffer
    ("Band 3") verlangte. Hier stand SINGULAR + ausgeschriebene Zahl.
    Gefunden hat sie das Lesen, nicht das Skript.

    ⚠️ Das ist der dritte Fall derselben Art in diesem Projekt (vorher:
    Gross-/Kleinschreibung, dann fehlende Wortgrenze bei \\bLeiche, die
    "gleichen" traf). **Die Suche ist immer enger als die Sprache** - dieser
    Check ersetzt den Lese-Durchgang nicht, er verkuerzt ihn nur.

    ⚠️ FEHLALARM, der NICHT gemeldet werden darf: Band 2 K04 hat
    "Nora zog den Band 1880-1895 heraus" - ein Archivband. Deshalb sind beim
    Singular nur die Zahlwoerter eins..fuenf erlaubt, keine Ziffernfolgen.
    """
    muster = (r"\b(?:vier|drei|zwei|f(?:ü|ue)nf|\d+)\s+B(?:ä|ae)nde\b"
              r"|\bB(?:ä|ae)nde lang\b"
              r"|\bNach \w+ B(?:ä|ae)nden\b"
              r"|\bin diesem Buch\b|\bder Leser\b|\bdieses Kapitel\b"
              r"|\bn(?:ä|ae)chste[nr]? Band\b"
              # -- ab hier neu (Fund 2026-07-18) --
              r"|\bB(?:a|ä)nd(?:e|en)?\s+(?:ein|eins|zwei|drei|vier|f(?:ü|ue)nf)\b"
              r"|\bseit Band\b|\bdiese[rm]? (?:Reihe|Serie)\b"
              # ★ ZWEITER Fund am selben Tag: 'seit dem ersten Band' (B4 K12) -
              #   Ordinal VOR Band/Buch, mit Praeposition/Artikel dazwischen.
              #   Das Muster oben (nur 'im ... Band') hatte es verpasst.
              #   Faengt NICHT 'Band 1' (Titelei) oder 'Band 1880' (Archiv),
              #   weil hier ein AUSGESCHRIEBENES Ordinal + Praeposition noetig ist.
              r"|\b(?:im|in|seit|aus|nach|vor|beim)\s+(?:dem\s+)?"
              r"(?:erste[srnm]?|zweite[srnm]?|dritte[srnm]?|vierte[srnm]?"
              r"|f(?:ü|ue)nfte[srnm]?|letzte[srnm]?)\s+(?:Band|Buch)\b")
    tr = []
    for m in re.finditer(r"[^.!?\n]{0,90}(?:" + muster + r")[^.!?\n]{0,70}[.!?]",
                         text, re.I):
        tr.append(m.group(0).strip())
    return tr


# ── Checks mit niedriger Trefferquote (nur mit --alle) ───────────────────────

def check_wort_echo(text):
    """⚠️ RAUSCHEN. An Band 1 getestet: 9 Treffer, ALLE bewusste Anapher
    ('einen Moment - einen einzigen, kurzen Moment'). Fast nur Fehltreffer."""
    tr = []
    for s in saetze(nur_erzaehler(text)):
        w = [x.lower() for x in re.findall(r"[A-Za-zÄÖÜäöüß]{6,}", s)]
        d = [x for x in set(w) if w.count(x) > 1]
        if d:
            tr.append(f"{d} :: {s[:110]}")
    return tr


def check_pronomen(text):
    """Mehrere maennliche Figuren + Pronomen im selben Satz."""
    tr = []
    for s in saetze(nur_erzaehler(text)):
        if len(re.findall(r"\b(Theo|Schatten|Brenner|Papa|Herr [A-Z]\w+)\b", s)) >= 2 \
           and re.search(r"\b(er|ihn|ihm)\b", s):
            tr.append(s)
    return tr


def check_tageszeit(text):
    """Zu viele verschiedene Tageszeiten in einem Kapitel."""
    tr = []
    for nr, titel, body in kapitel(text):
        z = set(re.findall(r"\b(Morgen|Vormittag|Mittag|Nachmittag|Abend|Nacht|"
                           r"Mitternacht|D(ä|ae)mmerung)\b", body))
        z = {x[0] if isinstance(x, tuple) else x for x in z}
        if len(z) >= 4:
            tr.append(f"K{nr}: {sorted(z)}")
    return tr


# ── Hauptlauf ────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        raise SystemExit("Verwendung: py Scripts/pruefe_logik.py <band> [--alle]")
    band = int(sys.argv[1])
    alle = "--alle" in sys.argv
    text = lade(band)

    print("=" * 78)
    print(f"LOGIK-VORPRUEFUNG - Band {band}   ({len(kapitel(text))} Kapitel, "
          f"{len(text.split()):,} Woerter)")
    print("=" * 78)
    print("Alle Treffer sind KANDIDATEN. Jeden im Kontext lesen (Regel 1).")

    print("\n\n########## HOHE TREFFERQUOTE - hier zuerst schauen ##########")
    n = 0
    n += zeige("1. Doppelte Kapiteltitel (serienweit)",
               check_kapiteltitel_serienweit(band),
               hinweis="Realer Fund: 'Der Keller' in B1 UND B3.")
    n += zeige("2. Zeitangaben", check_zeitangaben(text),
               hinweis="Gegen die Serien-Zeitlinie pruefen. Haeufigster Fehler der Reihe.")
    n += zeige("3. Zahlen, die zusammenpassen muessen", check_zahlen(text))
    n += zeige("4. Verdaechtige Sprechverben", check_sprechverben(text),
               hinweis="Pruefen: wirklich Sprechverb oder eigenstaendiger Handlungssatz?")
    n += zeige("5. Verbotene Begriffe (Content-Grenzen)", check_verbotene_begriffe(text),
               hinweis="Im Kontext lesen - 'Kein Blut, kein Feuer' BENENNT die Grenze.")
    n += zeige("6. POV-Bruch (Innenleben anderer Figuren)", check_pov(text),
               hinweis="Nur Erzaehlertext. Serienregel: nur was Nora wahrnimmt.")
    n += zeige("7. Kapitel ohne Schatten-REAKTION", check_schatten(text))
    n += zeige("8. Woertlich wiederholte Saetze", check_wiederholte_saetze(text),
               hinweis="Manche sind gewollte Callbacks - nicht blind streichen.")
    n += zeige("9. >> VIERTE WAND (Meta-Sprache)", check_vierte_wand(text),
               hinweis="Realer Fund: 6x 'vier Baende' in Band 4, im Druck. "
                       "Fehlalarme moeglich: 'Baende' in einer Bibliothek, "
                       "ein erfundener Buchtitel als Witz - im Kontext lesen.")

    print("\n\n########## ZUR BEURTEILUNG (kein Fehler an sich) ##########")
    zeige("9. Kapitel-Schlusssaetze (Cliffhanger-Pflicht)", check_cliffhanger(text),
          limit=30)

    if alle:
        print("\n\n########## NIEDRIGE TREFFERQUOTE - viel Rauschen ##########")
        zeige("10. Wort-Echo im Satz", check_wort_echo(text), limit=8,
              hinweis="⚠️ An Band 1 waren ALLE 9 Treffer bewusste Anapher. Vorsicht.")
        zeige("11. Pronomen-Ambiguitaet", check_pronomen(text), limit=8)
        zeige("12. Tageszeit-Sprünge", check_tageszeit(text), limit=8)
    else:
        print("\n\n(Die rauschanfaelligen Checks 10-12 laufen nur mit --alle.)")

    print("\n" + "=" * 78)
    print(f"{n} Kandidaten in den Checks mit hoher Trefferquote.")
    print("Naechster Schritt: Befundliste anlegen, jeden Treffer im Kontext lesen,")
    print("einstufen (rot/orange/gelb/weiss) - siehe Dokumentation/Logik_Pruefplan.md.")


if __name__ == "__main__":
    main()
