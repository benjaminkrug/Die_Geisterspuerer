#!/usr/bin/env python3
"""
Konvertiert ae/oe/ue -> ae/oe/ue + ss -> ss in allen CYOA-Markdown-Dateien.

Reihenfolge:
1. ae -> ae (blanket)
2. oe -> oe (blanket)
3. ue -> ue (mit Lookbehind: nicht nach 'a', 'e' oder 'q')
4. Grossbuchstaben: Ae->Ae, Oe->Oe, Ue->Ue
5. False-Positive-Korrekturen (zuerst, quer, geuebt, malformed)
6. ss -> ss (einfache String-Ersetzung, kompoundsicher)
"""

import os
import re
import sys

# Projektverzeichnis
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.join(_SCRIPT_DIR, "..")
V2_DIR = os.path.join(_PROJECT_ROOT, "Band1", "CYOA", "v2")
FRONTMATTER = os.path.join(_PROJECT_ROOT, "Band1", "CYOA", "frontmatter.md")


def convert_umlauts(text):
    """Konvertiert ae/oe/ue -> ae/oe/ue im Text."""
    changes = 0
    original = text

    # 1. ae -> ae (blanket, da keine False Positives)
    # Aber Ae am Wortanfang -> Ae
    text = re.sub(r'Ae(?=[a-z\u00e4\u00f6\u00fc])', '\u00c4', text)
    text = text.replace('ae', '\u00e4')

    # 2. oe -> oe (blanket, da keine False Positives)
    text = re.sub(r'Oe(?=[a-z\u00e4\u00f6\u00fc])', '\u00d6', text)
    text = text.replace('oe', '\u00f6')

    # 3. ue -> ue (mit Lookbehind: NICHT nach a, e oder q)
    # Schuetzt: Feuer, teuer, Abenteuer, neuer, Mauer, Bauer, Schauer, quer
    text = re.sub(r'(?<![aeqAEQ])Ue(?=[a-z\u00e4\u00f6\u00fc])', '\u00dc', text)
    text = re.sub(r'(?<![ae\u00e4AE\u00c4qQ])ue', '\u00fc', text)

    changes = sum(1 for a, b in zip(original, text) if a != b)
    return text, changes


def fix_false_positives(text):
    """Korrigiert bekannte False Positives und malformed conversions."""
    fixes = [
        # Malformed: extra Buchstabe vor Umlaut (pre-existing Tippfehler)
        ('ko\u00f6nnte', 'k\u00f6nnte'),
        ('Ko\u00f6nnte', 'K\u00f6nnte'),
        ('bo\u00f6ser', 'b\u00f6ser'),
        ('Bo\u00f6ser', 'B\u00f6ser'),
        ('Kr\u00e4achzen', 'Kr\u00e4chzen'),
        ('kr\u00e4achzen', 'kr\u00e4chzen'),
        ('Ger\u00e4ausche', 'Ger\u00e4usche'),
        ('ger\u00e4ausche', 'ger\u00e4usche'),

        # False Positive ue->ue: "zuerst" (zu + erst, kein Umlaut)
        ('z\u00fcrst', 'zuerst'),
        ('Z\u00fcrst', 'Zuerst'),

        # False Positive ue->ue: "quer" (kein Umlaut)
        ('q\u00fcr', 'quer'),
        ('Q\u00fcr', 'Quer'),

        # Verpasste ue->ue: "geuebt" -> "ge\u00fcbt" (eue-Lookbehind hat es blockiert)
        ('geuebt', 'ge\u00fcbt'),
        ('Geuebt', 'Ge\u00fcbt'),
    ]
    changes = 0
    for old, new in fixes:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changes += count
    return text, changes


def convert_ss_to_sz(text):
    """Umfassende ss -> ss Konvertierung mit einfacher String-Ersetzung.

    Verwendet str.replace() statt Regex. Die Reihenfolge ist so gewaehlt,
    dass laengere Muster vor kuerzeren kommen (innerhalb einer Familie).
    Compound-Woerter werden automatisch erfasst, da str.replace() auch
    Teilstrings innerhalb von Woertern findet.

    Regel: ss nach langem Vokal oder Diphthong -> ss.
    ss nach kurzem Vokal bleibt ss (dass, muss, Schloss, etc.).
    """

    # Jedes Tupel: (alt, neu)
    # WICHTIG: Laengere Muster zuerst innerhalb derselben Wurzel!
    replacements = [
        # ===== sa\u00df (Praeteritum von sitzen, langes a) =====
        ('Sass', 'Sa\u00df'),
        ('sass', 'sa\u00df'),

        # ===== lie\u00df Familie (Praeteritum von lassen, Diphthong ie) =====
        ('hinterliessen', 'hinterlie\u00dfen'),
        ('hinterliess', 'hinterlie\u00df'),
        ('Hinterliess', 'Hinterlie\u00df'),
        ('verliessen', 'verlie\u00dfen'),
        ('verliess', 'verlie\u00df'),
        ('Verliess', 'Verlie\u00df'),
        ('\u00fcberliessen', '\u00fcberlie\u00dfen'),
        ('\u00fcberliess', '\u00fcberlie\u00df'),
        ('zur\u00fcckliess', 'zur\u00fccklie\u00df'),
        ('Liessen', 'Lie\u00dfen'),
        ('liessen', 'lie\u00dfen'),
        ('Liess', 'Lie\u00df'),
        ('liess', 'lie\u00df'),

        # ===== Stra\u00dfe Familie =====
        ('Strassen', 'Stra\u00dfen'),
        ('strassen', 'stra\u00dfen'),
        ('Strasse', 'Stra\u00dfe'),
        ('strasse', 'stra\u00dfe'),

        # ===== gro\u00df Familie =====
        # gr\u00f6ss- Formen (Komparativ/Superlativ mit Umlaut)
        ('Gr\u00f6ssten', 'Gr\u00f6\u00dften'),
        ('gr\u00f6ssten', 'gr\u00f6\u00dften'),
        ('Gr\u00f6ssere', 'Gr\u00f6\u00dfere'),
        ('gr\u00f6ssere', 'gr\u00f6\u00dfere'),
        ('Gr\u00f6sser', 'Gr\u00f6\u00dfer'),
        ('gr\u00f6sser', 'gr\u00f6\u00dfer'),
        ('Gr\u00f6ssen', 'Gr\u00f6\u00dfen'),
        ('gr\u00f6ssen', 'gr\u00f6\u00dfen'),
        ('Gr\u00f6sse', 'Gr\u00f6\u00dfe'),
        ('gr\u00f6sse', 'gr\u00f6\u00dfe'),
        # gross- Formen (Positiv)
        ('Grossen', 'Gro\u00dfen'),
        ('grossen', 'gro\u00dfen'),
        ('Grosser', 'Gro\u00dfer'),
        ('grosser', 'gro\u00dfer'),
        ('Grosses', 'Gro\u00dfes'),
        ('grosses', 'gro\u00dfes'),
        ('Grosse', 'Gro\u00dfe'),
        ('grosse', 'gro\u00dfe'),
        ('Gross', 'Gro\u00df'),
        ('gross', 'gro\u00df'),

        # ===== wei\u00df Familie (Farbe + wissen, Diphthong ei) =====
        ('Weissen', 'Wei\u00dfen'),
        ('weissen', 'wei\u00dfen'),
        ('Weisser', 'Wei\u00dfer'),
        ('weisser', 'wei\u00dfer'),
        ('Weisses', 'Wei\u00dfes'),
        ('weisses', 'wei\u00dfes'),
        ('Weisse', 'Wei\u00dfe'),
        ('weisse', 'wei\u00dfe'),
        ('Weisst', 'Wei\u00dft'),
        ('weisst', 'wei\u00dft'),
        ('Weiss', 'Wei\u00df'),
        ('weiss', 'wei\u00df'),

        # ===== hei\u00df Familie (Diphthong ei) =====
        ('Heissen', 'Hei\u00dfen'),
        ('heissen', 'hei\u00dfen'),
        ('Heisst', 'Hei\u00dft'),
        ('heisst', 'hei\u00dft'),
        ('Heisse', 'Hei\u00dfe'),
        ('heisse', 'hei\u00dfe'),
        ('Heiss', 'Hei\u00df'),
        ('heiss', 'hei\u00df'),

        # ===== Fu\u00df Familie (langes u) =====
        ('Fussabdr\u00fcck', 'Fu\u00dfabdr\u00fcck'),
        ('Fussend', 'Fu\u00dfend'),
        ('Fussspuren', 'Fu\u00dfspuren'),
        ('Fussstapfen', 'Fu\u00dfstapfen'),
        ('Kinderf\u00fcsse', 'Kinderf\u00fc\u00dfe'),
        ('Kindf\u00fcsse', 'Kindf\u00fc\u00dfe'),
        ('kindf\u00fcsse', 'kindf\u00fc\u00dfe'),
        ('F\u00fcssen', 'F\u00fc\u00dfen'),
        ('f\u00fcssen', 'f\u00fc\u00dfen'),
        ('F\u00fcsse', 'F\u00fc\u00dfe'),
        ('f\u00fcsse', 'f\u00fc\u00dfe'),
        ('Fuss', 'Fu\u00df'),
        ('fuss', 'fu\u00df'),

        # ===== s\u00fc\u00df Familie (langes \u00fc) =====
        ('S\u00fcsses', 'S\u00fc\u00dfes'),
        ('s\u00fcsses', 's\u00fc\u00dfes'),
        ('S\u00fcssen', 'S\u00fc\u00dfen'),
        ('s\u00fcssen', 's\u00fc\u00dfen'),
        ('S\u00fcsse', 'S\u00fc\u00dfe'),
        ('s\u00fcsse', 's\u00fc\u00dfe'),
        ('S\u00fcss', 'S\u00fc\u00df'),
        ('s\u00fcss', 's\u00fc\u00df'),

        # ===== ...m\u00e4\u00dfig (langes \u00e4) =====
        ('Gleichm\u00e4ssiges', 'Gleichm\u00e4\u00dfiges'),
        ('gleichm\u00e4ssiges', 'gleichm\u00e4\u00dfiges'),
        ('Gleichm\u00e4ssig', 'Gleichm\u00e4\u00dfig'),
        ('gleichm\u00e4ssig', 'gleichm\u00e4\u00dfig'),
        ('Regelm\u00e4ssig', 'Regelm\u00e4\u00dfig'),
        ('regelm\u00e4ssig', 'regelm\u00e4\u00dfig'),
        ('M\u00e4ssig', 'M\u00e4\u00dfig'),
        ('m\u00e4ssig', 'm\u00e4\u00dfig'),

        # ===== schlie\u00dfen Familie (Diphthong ie) =====
        ('Schliesslich', 'Schlie\u00dflich'),
        ('schliesslich', 'schlie\u00dflich'),
        ('schliessen', 'schlie\u00dfen'),
        ('Schliessen', 'Schlie\u00dfen'),
        ('schliesst', 'schlie\u00dft'),
        ('Schliesst', 'Schlie\u00dft'),

        # ===== drei\u00dfig (Diphthong ei) =====
        ('Dreissig', 'Drei\u00dfig'),
        ('dreissig', 'drei\u00dfig'),

        # ===== stie\u00df (Diphthong ie, Praeteritum von sto\u00dfen) =====
        ('Stiess', 'Stie\u00df'),
        ('stiess', 'stie\u00df'),

        # ===== entbl\u00f6\u00dft (langes \u00f6) =====
        ('entbl\u00f6sst', 'entbl\u00f6\u00dft'),
        ('Entbl\u00f6sst', 'Entbl\u00f6\u00dft'),

        # ===== ...fl\u00f6\u00dfend (Furchteinfl\u00f6\u00dfend, langes \u00f6) =====
        ('einfl\u00f6ssend', 'einfl\u00f6\u00dfend'),
        ('Einfl\u00f6ssend', 'Einfl\u00f6\u00dfend'),

        # ===== drau\u00dfen (Diphthong au) =====
        ('Draussen', 'Drau\u00dfen'),
        ('draussen', 'drau\u00dfen'),

        # ===== au\u00dfen/au\u00dfer Familie (Diphthong au) =====
        ('Ausserdem', 'Au\u00dferdem'),
        ('ausserdem', 'au\u00dferdem'),
        ('Ausserhalb', 'Au\u00dferhalb'),
        ('ausserhalb', 'au\u00dferhalb'),
        ('Ausser', 'Au\u00dfer'),
        ('ausser', 'au\u00dfer'),
        ('Aussen', 'Au\u00dfen'),
        ('aussen', 'au\u00dfen'),

        # ===== Spa\u00df (langes a) =====
        ('Spass', 'Spa\u00df'),
        ('spass', 'spa\u00df'),

        # ===== blo\u00df (langes o) =====
        ('Bloss', 'Blo\u00df'),
        ('bloss', 'blo\u00df'),

        # ===== gie\u00dfen (Diphthong ie) =====
        ('giessen', 'gie\u00dfen'),
        ('Giessen', 'Gie\u00dfen'),
        ('giesst', 'gie\u00dft'),

        # ===== flie\u00dfen (Diphthong ie) =====
        ('fliessen', 'flie\u00dfen'),
        ('Fliessen', 'Flie\u00dfen'),
        ('fliesst', 'flie\u00dft'),

        # ===== sto\u00dfen Familie (langes o) =====
        ('gestossen', 'gesto\u00dfen'),
        ('Gestossen', 'Gesto\u00dfen'),
        ('stossen', 'sto\u00dfen'),
        ('Stossen', 'Sto\u00dfen'),
        ('st\u00f6sst', 'st\u00f6\u00dft'),

        # ===== rei\u00dfen (Diphthong ei) =====
        ('reissen', 'rei\u00dfen'),
        ('Reissen', 'Rei\u00dfen'),
        ('reisst', 'rei\u00dft'),

        # ===== bei\u00dfen (Diphthong ei) =====
        ('beissen', 'bei\u00dfen'),
        ('Beissen', 'Bei\u00dfen'),
        ('beisst', 'bei\u00dft'),

        # ===== Schwei\u00df (Diphthong ei) =====
        ('Schweiss', 'Schwei\u00df'),
        ('schweiss', 'schwei\u00df'),

        # ===== Ma\u00df (langes a, Praeteritum von messen) =====
        # Vorsicht: "Masse" (kurzes a) bleibt ss
        # Nur in Kontexten wo "mass" als Verb vorkommt
        # ('mass', 'ma\u00df'),  # Zu riskant, daher auskommentiert

        # ===== Scho\u00df (langes o, = Scho\u00df/lap) =====
        # Vorsicht: "schoss" (Praeteritum von schie\u00dfen) hat kurzes o -> bleibt ss
        # ('Schoss', 'Scho\u00df'),  # Zu riskant, da "geschoss-" auch existiert

        # ===== Schei\u00dfe (Diphthong ei) =====
        ('Scheisse', 'Schei\u00dfe'),
        ('scheisse', 'schei\u00dfe'),

        # ===== schiessen (Diphthong ie) =====
        ('schiessen', 'schie\u00dfen'),
        ('Schiessen', 'Schie\u00dfen'),
        ('schiesst', 'schie\u00dft'),
    ]

    changes = 0
    for old, new in replacements:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changes += count
    return text, changes


def process_file(filepath):
    """Verarbeitet eine einzelne Markdown-Datei."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    # Schritt 1: Umlaute konvertieren (idempotent bei bereits konvertierten Dateien)
    text, umlaut_changes = convert_umlauts(original)

    # Schritt 2: False-Positive-Korrekturen
    text, fp_changes = fix_false_positives(text)

    # Schritt 3: ss -> ss konvertieren
    text, ss_changes = convert_ss_to_sz(text)

    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)

    return umlaut_changes, fp_changes, ss_changes


def main():
    print("=" * 60)
    print("  UMLAUT-KONVERTIERUNG + SS-KORREKTUR (Pass 2)")
    print("=" * 60)
    print()

    # Alle .md-Dateien in v2/ sammeln
    md_files = []
    for root, dirs, files in os.walk(V2_DIR):
        for f in sorted(files):
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    # frontmatter.md hinzufuegen
    if os.path.exists(FRONTMATTER):
        md_files.append(FRONTMATTER)

    print(f"  Dateien gefunden: {len(md_files)}")
    print()

    total_umlaut = 0
    total_fp = 0
    total_ss = 0
    changed_files = 0

    for filepath in md_files:
        relpath = os.path.relpath(filepath, _PROJECT_ROOT)
        umlaut_n, fp_n, ss_n = process_file(filepath)

        if umlaut_n > 0 or fp_n > 0 or ss_n > 0:
            changed_files += 1
            parts = []
            if umlaut_n > 0:
                parts.append(f"{umlaut_n} Umlaute")
            if fp_n > 0:
                parts.append(f"{fp_n} FP-Fixes")
            if ss_n > 0:
                parts.append(f"{ss_n} ss->sz")
            print(f"  {relpath}: {', '.join(parts)}")

        total_umlaut += umlaut_n
        total_fp += fp_n
        total_ss += ss_n

    print()
    print("-" * 60)
    print(f"  Geaenderte Dateien: {changed_files}")
    print(f"  Umlaut-Ersetzungen: {total_umlaut}")
    print(f"  False-Positive-Fixes: {total_fp}")
    print(f"  ss->sz-Ersetzungen: {total_ss}")
    print(f"  Gesamt: {total_umlaut + total_fp + total_ss}")
    print("=" * 60)


if __name__ == "__main__":
    main()
