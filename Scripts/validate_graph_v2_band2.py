#!/usr/bin/env python3
"""
Validiert die CYOA-Graph-Struktur v2 (Time Cave) fuer Die Geisterspuerer Band 1.

Prueft:
1. Alle Abschnitte erreichbar (kein verwaister Content)
2. Alle Pfade fuehren zu einem Ende
3. Keine kaputten Referenzen (Ziel-Abschnitte existieren)
4. Sackgassen korrekt verlinkt (haben return_to)
5. Pfadlaengen im Zielbereich (30-40 Abschnitte pro Durchgang)
6. Time Cave: Pfade konvergieren nicht (ausser C->A/B)
7. Alle MD-Dateien existieren
8. QA: Wortanzahl pro Abschnitt (Ziel: 300-350)
9. QA: Dialog-Anteil (Ziel: 35-45%)
10. QA: Schatten-Praesenz pro Abschnitt
11. QA: Sensorik-Check (mind. 2 Sinneseindruecke)
12. QA: Cliffhanger/Hook am Ende

Nutzung:
  python validate_graph_v2.py              # Validierung + QA-Report auf Konsole
  python validate_graph_v2.py --report     # QA-Report als Markdown in Band1/CYOA/
"""

import yaml
import sys
import os
import re
from pathlib import Path


def load_graph(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_targets(section: dict) -> list:
    """Alle Ziel-Abschnitte eines Abschnitts."""
    targets = []
    if "choices" in section:
        for choice in section["choices"]:
            targets.append(choice["target"])
    if "next" in section:
        targets.append(section["next"])
    return targets


def find_all_paths(sections: dict, start: str = "P1") -> list:
    """Findet alle moeglichen Pfade vom Start bis zu einem Ende."""
    dead_ends = {sid for sid, s in sections.items() if s.get("type") == "dead_end"}
    endings_set = {sid for sid, s in sections.items() if s.get("type") == "ending"}

    paths = []
    max_steps = 120
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        section = sections.get(current)

        if section is None:
            continue

        # Reached an ending
        if current in endings_set:
            paths.append(path)
            continue

        # Dead end - don't count as complete path
        if current in dead_ends:
            continue

        targets = get_targets(section)

        if not targets:
            # Dangling section - no way forward, no ending
            paths.append(path)
            continue

        for target in targets:
            # Skip dead-end branches (they send reader back)
            if target in dead_ends:
                continue
            if len(path) >= max_steps:
                continue
            # Prevent cycles
            if target in path:
                continue
            stack.append((target, path + [target]))

    return paths


def get_path_prefix(sid: str) -> str:
    """Extrahiert den Pfad-Prefix (P, A, B, C, D, E) aus einer Abschnitt-ID."""
    for prefix in ["A_LIB", "AP", "A", "B", "C", "D", "E", "P"]:
        if sid.startswith(prefix):
            return prefix[0]  # Return first char
    return "?"


# ============================================================
# QA-Analyse: Inhaltliche Pruefung der MD-Dateien
# ============================================================

# Schatten-Regex: Alle Formen, wie Schatten im Text auftauchen kann
SCHATTEN_RE = re.compile(
    r'Schatten|Hund|knurr|Knurr|wedel|Wedel|bell|Bell|jaul|Jaul|'
    r'Fell|Pfote|Pfoten|Schnauze|Bernstein|hechel|Hechel|'
    r'winseln|Winseln|Rute|Ohren.*spitz|fletsch',
    re.IGNORECASE
)

# Dialog-Regex: Zeilen mit Anfuehrungszeichen oder Guillemets
DIALOG_RE = re.compile(r'["\u201e\u201c\u201d\u00ab\u00bb]')

# Sensorik-Woerter nach Sinn
SENSE_PATTERNS = {
    'kaelte_waerme': re.compile(
        r'kalt|kälte|eisig|warm|wärme|hitze|frost|kühl|heiß|glühend|fröstel',
        re.IGNORECASE),
    'geruch': re.compile(
        r'roch|riech|Geruch|stank|stink|duft|muffig|modrig|feucht',
        re.IGNORECASE),
    'geraeusch': re.compile(
        r'klopf|knack|knarz|knarr|quietsch|raschel|flüster|rausch|'
        r'polter|donner|klirr|tropf|summ|brumm|heul|schrei|stille|leise|laut',
        re.IGNORECASE),
    'taktil': re.compile(
        r'berühr|griff|fass|spür|zitter|beb|kribbel|rau|glatt|nass|'
        r'kleb|weich|hart|Gänsehaut|Nackenha',
        re.IGNORECASE),
    'visuell': re.compile(
        r'dunk|hell|licht|schimmer|glüh|leuchte|flacker|schatt|'
        r'nebel|trüb|blass|grau|schwarz|rot.*leucht',
        re.IGNORECASE),
}

# Cliffhanger-Indikatoren am Textende
CLIFFHANGER_RE = re.compile(
    r'\?["\s]*$|\.{3}["\s]*$|—["\s]*$|\.\.\.["\s]*$|'
    r'[Ww]eiter mit|[Gg]ehe zu|[Ww]as jetzt',
    re.MULTILINE
)


def analyze_section_content(md_path: Path) -> dict:
    """Analysiert eine MD-Datei auf Qualitaets-Metriken."""
    result = {
        'word_count': 0,
        'line_count': 0,
        'dialog_lines': 0,
        'dialog_pct': 0.0,
        'schatten_count': 0,
        'senses': {},
        'sense_count': 0,
        'has_cliffhanger': False,
        'file_exists': False,
    }

    if not md_path.exists():
        return result

    result['file_exists'] = True
    text = md_path.read_text(encoding='utf-8')

    # Strip markdown header (# Abschnitt ...) and metadata lines
    lines = text.strip().split('\n')
    content_lines = []
    for line in lines:
        stripped = line.strip()
        # Skip headers, empty lines at top, and navigation lines
        if stripped.startswith('#'):
            continue
        if stripped.startswith('---'):
            continue
        if stripped.startswith('*Weiter mit') or stripped.startswith('*Gehe zu'):
            continue
        if stripped.startswith('> **'):
            continue
        content_lines.append(stripped)

    content_text = '\n'.join(content_lines)

    # Word count (nur Prosa, keine Markdown-Syntax)
    words = re.findall(r'\b\w+\b', content_text)
    result['word_count'] = len(words)
    result['line_count'] = len([l for l in content_lines if l.strip()])

    # Dialog-Anteil
    non_empty_lines = [l for l in content_lines if l.strip()]
    if non_empty_lines:
        dialog_lines = sum(1 for l in non_empty_lines if DIALOG_RE.search(l))
        result['dialog_lines'] = dialog_lines
        result['dialog_pct'] = (dialog_lines / len(non_empty_lines)) * 100

    # Schatten-Praesenz
    result['schatten_count'] = len(SCHATTEN_RE.findall(content_text))

    # Sensorik
    for sense_name, pattern in SENSE_PATTERNS.items():
        matches = pattern.findall(content_text)
        if matches:
            result['senses'][sense_name] = len(matches)
    result['sense_count'] = len(result['senses'])

    # Cliffhanger am Ende (letzte 5 Zeilen pruefen)
    last_lines = '\n'.join(content_lines[-5:]) if content_lines else ''
    result['has_cliffhanger'] = bool(CLIFFHANGER_RE.search(last_lines))

    return result


def generate_qa_report(sections: dict, v2_dir: Path) -> dict:
    """Analysiert alle Abschnitte und erzeugt QA-Daten."""
    qa_data = {}

    for sid, section in sorted(sections.items()):
        file_path = section.get("file")
        if not file_path:
            continue

        md_path = v2_dir / file_path
        metrics = analyze_section_content(md_path)
        metrics['title'] = section.get('title', '?')
        metrics['type'] = section.get('type', '?')
        metrics['path_prefix'] = get_path_prefix(sid)
        qa_data[sid] = metrics

    return qa_data


def print_qa_summary(qa_data: dict):
    """Druckt QA-Zusammenfassung auf die Konsole."""
    print("\n" + "=" * 60)
    print("=== QA-ANALYSE: Inhalts-Qualitaet ===")
    print("=" * 60)

    # Filter: nur existierende Dateien, keine Endings/Dead Ends fuer Wortanzahl-Check
    story_sections = {sid: d for sid, d in qa_data.items()
                      if d['file_exists'] and d['type'] in ('story', 'choice')}
    all_existing = {sid: d for sid, d in qa_data.items() if d['file_exists']}

    if not all_existing:
        print("  Keine MD-Dateien gefunden!")
        return

    # --- Wortanzahl ---
    print("\n--- 9. Wortanzahl (Ziel: 300-350) ---")
    word_counts = [d['word_count'] for d in all_existing.values()]
    avg_words = sum(word_counts) / len(word_counts)
    print("  Durchschnitt: {:.0f} Woerter".format(avg_words))
    print("  Min: {} | Max: {}".format(min(word_counts), max(word_counts)))

    under_200 = [(sid, d) for sid, d in all_existing.items() if d['word_count'] < 200]
    under_250 = [(sid, d) for sid, d in all_existing.items()
                 if 200 <= d['word_count'] < 250]
    in_range = [(sid, d) for sid, d in all_existing.items()
                if 250 <= d['word_count'] <= 400]
    over_400 = [(sid, d) for sid, d in all_existing.items() if d['word_count'] > 400]

    print("  < 200 Woerter: {} Abschnitte [KRITISCH]".format(len(under_200)))
    print("  200-249 Woerter: {} Abschnitte [KURZ]".format(len(under_250)))
    print("  250-400 Woerter: {} Abschnitte [OK]".format(len(in_range)))
    print("  > 400 Woerter: {} Abschnitte [LANG]".format(len(over_400)))

    if under_200:
        print("  Kritisch kurz:")
        for sid, d in sorted(under_200, key=lambda x: x[1]['word_count']):
            print("    {} \"{}\": {} Woerter".format(sid, d['title'], d['word_count']))

    # --- Dialog ---
    print("\n--- 10. Dialog-Anteil (Ziel: 35-45%) ---")
    dialog_pcts = [d['dialog_pct'] for d in all_existing.values()]
    avg_dialog = sum(dialog_pcts) / len(dialog_pcts)
    print("  Durchschnitt: {:.1f}%".format(avg_dialog))

    low_dialog = [(sid, d) for sid, d in all_existing.items() if d['dialog_pct'] < 20]
    ok_dialog = [(sid, d) for sid, d in all_existing.items()
                 if 20 <= d['dialog_pct'] < 35]
    good_dialog = [(sid, d) for sid, d in all_existing.items()
                   if 35 <= d['dialog_pct'] <= 50]
    high_dialog = [(sid, d) for sid, d in all_existing.items() if d['dialog_pct'] > 50]

    print("  < 20%: {} Abschnitte [ZU WENIG]".format(len(low_dialog)))
    print("  20-34%: {} Abschnitte [AKZEPTABEL]".format(len(ok_dialog)))
    print("  35-50%: {} Abschnitte [ZIEL]".format(len(good_dialog)))
    print("  > 50%: {} Abschnitte [HOCH]".format(len(high_dialog)))

    # --- Schatten ---
    print("\n--- 11. Schatten-Praesenz (Ziel: mind. 1x) ---")
    no_schatten = [(sid, d) for sid, d in all_existing.items()
                   if d['schatten_count'] == 0 and d['type'] not in ('dead_end',)]
    has_schatten = [(sid, d) for sid, d in all_existing.items()
                    if d['schatten_count'] > 0]
    print("  Mit Schatten: {}/{} Abschnitte".format(
        len(has_schatten), len(all_existing)))

    if no_schatten:
        print("  OHNE Schatten:")
        for sid, d in sorted(no_schatten):
            print("    {} \"{}\"".format(sid, d['title']))

    # --- Sensorik ---
    print("\n--- 12. Sensorik (Ziel: mind. 2 Sinne) ---")
    sense_counts = [d['sense_count'] for d in all_existing.values()]
    avg_senses = sum(sense_counts) / len(sense_counts)
    print("  Durchschnitt: {:.1f} Sinne pro Abschnitt".format(avg_senses))

    low_sense = [(sid, d) for sid, d in all_existing.items() if d['sense_count'] < 2]
    print("  < 2 Sinne: {} Abschnitte".format(len(low_sense)))
    if low_sense:
        for sid, d in sorted(low_sense):
            senses = ', '.join(d['senses'].keys()) if d['senses'] else 'keine'
            print("    {} \"{}\": {} ({})".format(
                sid, d['title'], d['sense_count'], senses))

    # Per-path summary
    print("\n--- 13. Qualitaet nach Pfad ---")
    path_stats = {}
    for sid, d in all_existing.items():
        prefix = d['path_prefix']
        if prefix not in path_stats:
            path_stats[prefix] = {'words': [], 'dialog': [], 'schatten': 0,
                                  'senses': [], 'count': 0}
        path_stats[prefix]['words'].append(d['word_count'])
        path_stats[prefix]['dialog'].append(d['dialog_pct'])
        if d['schatten_count'] > 0:
            path_stats[prefix]['schatten'] += 1
        path_stats[prefix]['senses'].append(d['sense_count'])
        path_stats[prefix]['count'] += 1

    print("  {:>5} {:>6} {:>8} {:>10} {:>8} {:>6}".format(
        'Pfad', 'Anz.', 'Ø Wörter', 'Ø Dialog%', 'Schatten', 'Ø Sinne'))
    for prefix in sorted(path_stats.keys()):
        ps = path_stats[prefix]
        avg_w = sum(ps['words']) / len(ps['words'])
        avg_d = sum(ps['dialog']) / len(ps['dialog'])
        avg_s = sum(ps['senses']) / len(ps['senses'])
        schatten_pct = (ps['schatten'] / ps['count']) * 100
        print("  {:>5} {:>6} {:>8.0f} {:>9.1f}% {:>7.0f}% {:>6.1f}".format(
            prefix, ps['count'], avg_w, avg_d, schatten_pct, avg_s))


def export_qa_markdown(qa_data: dict, output_dir: Path):
    """Exportiert Qualitaets-Analyse als Markdown-Datei."""
    lines = []
    lines.append("# Qualitaets-Analyse — Die Geisterspuerer CYOA Band 1 v2")
    lines.append("")
    lines.append("Automatisch generiert von `Scripts/validate_graph_v2.py --report`")
    lines.append("")
    lines.append("---")
    lines.append("")

    all_existing = {sid: d for sid, d in qa_data.items() if d['file_exists']}
    if not all_existing:
        lines.append("Keine MD-Dateien gefunden.")
        (output_dir / "Qualitaets_Analyse.md").write_text('\n'.join(lines), encoding='utf-8')
        return

    # Gesamt-Statistik
    word_counts = [d['word_count'] for d in all_existing.values()]
    dialog_pcts = [d['dialog_pct'] for d in all_existing.values()]
    sense_counts = [d['sense_count'] for d in all_existing.values()]
    schatten_count = sum(1 for d in all_existing.values() if d['schatten_count'] > 0)

    lines.append("## Gesamt-Statistik")
    lines.append("")
    lines.append("| Metrik | Wert | Ziel |")
    lines.append("|--------|------|------|")
    lines.append("| Abschnitte | {} | — |".format(len(all_existing)))
    lines.append("| Ø Wortanzahl | {:.0f} | 300-350 |".format(
        sum(word_counts) / len(word_counts)))
    lines.append("| Min / Max Woerter | {} / {} | — |".format(
        min(word_counts), max(word_counts)))
    lines.append("| Ø Dialog-Anteil | {:.1f}% | 35-45% |".format(
        sum(dialog_pcts) / len(dialog_pcts)))
    lines.append("| Schatten-Praesenz | {}/{} ({:.0f}%) | 100% |".format(
        schatten_count, len(all_existing),
        (schatten_count / len(all_existing)) * 100))
    lines.append("| Ø Sinneseindruecke | {:.1f} | ≥ 2 |".format(
        sum(sense_counts) / len(sense_counts)))
    lines.append("")

    # Per-path stats
    lines.append("## Nach Pfad")
    lines.append("")
    lines.append("| Pfad | Abschnitte | Ø Woerter | Ø Dialog% | Schatten% | Ø Sinne |")
    lines.append("|------|------------|-----------|-----------|-----------|---------|")

    path_stats = {}
    for sid, d in all_existing.items():
        prefix = d['path_prefix']
        if prefix not in path_stats:
            path_stats[prefix] = {'words': [], 'dialog': [], 'schatten': 0,
                                  'senses': [], 'count': 0}
        path_stats[prefix]['words'].append(d['word_count'])
        path_stats[prefix]['dialog'].append(d['dialog_pct'])
        if d['schatten_count'] > 0:
            path_stats[prefix]['schatten'] += 1
        path_stats[prefix]['senses'].append(d['sense_count'])
        path_stats[prefix]['count'] += 1

    for prefix in sorted(path_stats.keys()):
        ps = path_stats[prefix]
        avg_w = sum(ps['words']) / len(ps['words'])
        avg_d = sum(ps['dialog']) / len(ps['dialog'])
        avg_s = sum(ps['senses']) / len(ps['senses'])
        schatten_pct = (ps['schatten'] / ps['count']) * 100
        lines.append("| {} | {} | {:.0f} | {:.1f}% | {:.0f}% | {:.1f} |".format(
            prefix, ps['count'], avg_w, avg_d, schatten_pct, avg_s))

    lines.append("")

    # Detail-Tabelle pro Abschnitt
    lines.append("## Detail pro Abschnitt")
    lines.append("")
    lines.append("| ID | Titel | Woerter | Dialog% | Schatten | Sinne | Bewertung |")
    lines.append("|----|-------|---------|---------|----------|-------|-----------|")

    for sid in sorted(all_existing.keys()):
        d = all_existing[sid]
        # Bewertung: 1-10
        score = _calculate_score(d)
        senses_str = str(d['sense_count'])
        schatten_str = str(d['schatten_count'])
        status = _score_emoji(score)
        lines.append("| {} | {} | {} | {:.0f}% | {} | {} | {} {} |".format(
            sid, d['title'], d['word_count'], d['dialog_pct'],
            schatten_str, senses_str, score, status))

    lines.append("")

    # Probleme
    lines.append("## Handlungsbedarf")
    lines.append("")

    # Zu kurze Abschnitte
    under_250 = [(sid, d) for sid, d in all_existing.items() if d['word_count'] < 250]
    if under_250:
        lines.append("### Zu kurz (< 250 Woerter)")
        lines.append("")
        for sid, d in sorted(under_250, key=lambda x: x[1]['word_count']):
            deficit = 300 - d['word_count']
            lines.append("- **{}** \"{}\": {} Woerter (braucht +{})".format(
                sid, d['title'], d['word_count'], deficit))
        lines.append("")

    # Ohne Schatten
    no_schatten = [(sid, d) for sid, d in all_existing.items()
                   if d['schatten_count'] == 0]
    if no_schatten:
        lines.append("### Ohne Schatten-Mention")
        lines.append("")
        for sid, d in sorted(no_schatten):
            lines.append("- **{}** \"{}\"".format(sid, d['title']))
        lines.append("")

    # Wenig Dialog
    low_dialog = [(sid, d) for sid, d in all_existing.items() if d['dialog_pct'] < 15]
    if low_dialog:
        lines.append("### Sehr wenig Dialog (< 15%)")
        lines.append("")
        for sid, d in sorted(low_dialog):
            lines.append("- **{}** \"{}\": {:.0f}%".format(
                sid, d['title'], d['dialog_pct']))
        lines.append("")

    # Wenig Sensorik
    low_sense = [(sid, d) for sid, d in all_existing.items() if d['sense_count'] < 2]
    if low_sense:
        lines.append("### Wenig Sensorik (< 2 Sinne)")
        lines.append("")
        for sid, d in sorted(low_sense):
            senses = ', '.join(d['senses'].keys()) if d['senses'] else 'keine'
            lines.append("- **{}** \"{}\": {} ({})".format(
                sid, d['title'], d['sense_count'], senses))
        lines.append("")

    output_path = output_dir / "Qualitaets_Analyse.md"
    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print("  Qualitaets-Analyse geschrieben: {}".format(output_path))


def export_crossref_markdown(sections: dict, qa_data: dict, v2_dir: Path, output_dir: Path):
    """Exportiert Cross-Referenz-Analyse als Markdown-Datei."""
    lines = []
    lines.append("# Cross-Referenz-Analyse — Die Geisterspuerer CYOA Band 1 v2")
    lines.append("")
    lines.append("Automatisch generiert von `Scripts/validate_graph_v2.py --report`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Wissens-Tracking: Was wird auf welchem Pfad enthuellt?
    lines.append("## Wissens-Enthuellungen pro Pfad")
    lines.append("")
    lines.append("Prueft: Wissen Nora/Theo in jedem Abschnitt nur, was sie auf diesem")
    lines.append("spezifischen Pfad erfahren haben?")
    lines.append("")

    # Key plot points to track
    key_knowledge = {
        'Lina': re.compile(r'Lina\s+Vogt|Lina.*1974|Lina.*gestorben|Lina.*Tod', re.IGNORECASE),
        'Silber': re.compile(r'Frau\s+Silber|Silbers?\s+(Wohnung|Methode|Tagebuch|Brief|Arbeit)', re.IGNORECASE),
        'Graven': re.compile(r'Graven|Alwin|Gruender|Gründer|1823', re.IGNORECASE),
        'Karte': re.compile(r'Karte.*Markierung|zwölf.*Punkt|zwoelf.*Punkt|12.*Markierung', re.IGNORECASE),
        'Methode': re.compile(r'Methode|Zuhoeren.*befreit|zuhören.*befreit|vorlesen', re.IGNORECASE),
        'Held': re.compile(r'Frau\s+Held|Nachbarin.*Held|Held.*Schluessel|Held.*Schlüssel', re.IGNORECASE),
    }

    for prefix_name, prefix_filter in [('Prolog', 'P'), ('Pfad A', 'A'),
                                         ('Pfad B', 'B'), ('Pfad C', 'C')]:
        lines.append("### {}".format(prefix_name))
        lines.append("")
        relevant = {sid: d for sid, d in qa_data.items()
                    if d.get('path_prefix') == prefix_filter[0] and d['file_exists']}

        for sid in sorted(relevant.keys()):
            file_path = sections.get(sid, {}).get("file")
            if not file_path:
                continue
            md_path = v2_dir / file_path
            if not md_path.exists():
                continue
            text = md_path.read_text(encoding='utf-8')
            found = []
            for knowledge_name, pattern in key_knowledge.items():
                if pattern.search(text):
                    found.append(knowledge_name)
            if found:
                lines.append("- **{}**: {}".format(sid, ', '.join(found)))

        lines.append("")

    # Incoming edges: Welche Abschnitte haben mehrere Eingaenge?
    lines.append("## Mehrfach-Eingaenge")
    lines.append("")
    lines.append("Abschnitte, die von mehr als einer Quelle erreicht werden:")
    lines.append("")

    incoming = {}
    for sid, section in sections.items():
        targets = get_targets(section)
        for target in targets:
            if target not in incoming:
                incoming[target] = []
            incoming[target].append(sid)

    multi_incoming = {sid: sources for sid, sources in incoming.items()
                      if len(sources) > 1}
    if multi_incoming:
        for sid in sorted(multi_incoming.keys()):
            sources = multi_incoming[sid]
            title = sections.get(sid, {}).get('title', '?')
            lines.append("- **{}** \"{}\": ← {}".format(
                sid, title, ', '.join(sorted(sources))))
    else:
        lines.append("Keine (reiner Time Cave).")
    lines.append("")

    # Verwaiste Abschnitte (keine eingehende Kante ausser P1)
    all_referenced = set()
    for sid, section in sections.items():
        for target in get_targets(section):
            all_referenced.add(target)
        if section.get("type") == "dead_end" and "return_to" in section:
            all_referenced.add(section["return_to"])

    unreachable = set(sections.keys()) - all_referenced - {"P1"}
    if unreachable:
        lines.append("## Verwaiste Abschnitte (nicht erreichbar)")
        lines.append("")
        for sid in sorted(unreachable):
            title = sections[sid].get('title', '?')
            stype = sections[sid].get('type', '?')
            lines.append("- **{}** \"{}\" ({})".format(sid, title, stype))
        lines.append("")

    # Graven-Verteilung
    lines.append("## Graven-Mentions pro Pfad")
    lines.append("")
    graven_re = re.compile(r'Graven|Alwin|Gruender|Gründer|1823', re.IGNORECASE)
    graven_by_path = {}
    for sid, section in sorted(sections.items()):
        file_path = section.get("file")
        if not file_path:
            continue
        md_path = v2_dir / file_path
        if not md_path.exists():
            continue
        text = md_path.read_text(encoding='utf-8')
        matches = graven_re.findall(text)
        if matches:
            prefix = get_path_prefix(sid)
            if prefix not in graven_by_path:
                graven_by_path[prefix] = []
            graven_by_path[prefix].append((sid, len(matches)))

    for prefix in sorted(graven_by_path.keys()):
        entries = graven_by_path[prefix]
        lines.append("- **Pfad {}**: {} Abschnitte".format(prefix, len(entries)))
        for sid, count in entries:
            title = sections.get(sid, {}).get('title', '?')
            lines.append("  - {} \"{}\" ({}x)".format(sid, title, count))
    lines.append("")

    output_path = output_dir / "Cross_Referenz_Analyse.md"
    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print("  Cross-Referenz-Analyse geschrieben: {}".format(output_path))


def _calculate_score(d: dict) -> int:
    """Berechnet eine Bewertung 1-10 basierend auf den Metriken.

    Band-2-Fork (Plan Rev. 3, STIL_REFERENZ): KEIN Wortzahl-Ziel mehr.
    Die Wortzahl-Boni/-Mali sind neutralisiert; nur sehr kurze Abschnitte
    (< 130 Woerter) bleiben als DIAGNOSE-Hinweis (manuell pruefen, nicht auffuellen).
    Dialog-Quote ist ebenfalls kein Ziel mehr -> nur extrem dialogarme Abschnitte
    (< 10%) als leiser Hinweis.
    """
    score = 5  # Basis

    # Wortanzahl: KEIN Ziel mehr. Nur verdaechtig duenne Abschnitte als Diagnose.
    wc = d['word_count']
    if wc < 130:
        score -= 1  # Hinweis: fehlt hier eine Szene? (nicht: "auffuellen")

    # Dialog: kein Ziel. Nur extrem dialogarm als leiser Hinweis.
    dp = d['dialog_pct']
    if dp < 10:
        score -= 1

    # Schatten: +1 wenn vorhanden, -1 wenn fehlend
    if d['schatten_count'] > 0:
        score += 1
    else:
        score -= 1

    # Sensorik: +1 wenn >= 3, -1 wenn < 2
    sc = d['sense_count']
    if sc >= 3:
        score += 1
    elif sc < 2:
        score -= 1

    return max(1, min(10, score))


def _score_emoji(score: int) -> str:
    """Gibt ASCII-Bewertungszeichen zurueck."""
    if score >= 8:
        return "[STARK]"
    elif score >= 6:
        return "[OK]"
    elif score >= 4:
        return "[SCHWACH]"
    else:
        return "[KRITISCH]"


def validate(graph_path: str) -> bool:
    data = load_graph(graph_path)
    sections = data["sections"]
    errors = []
    warnings = []

    section_ids = set(sections.keys())
    endings = {sid for sid, s in sections.items() if s.get("type") == "ending"}
    dead_ends = {sid for sid, s in sections.items() if s.get("type") == "dead_end"}
    choices = {sid for sid, s in sections.items() if s.get("type") == "choice"}
    stories = {sid for sid, s in sections.items() if s.get("type") == "story"}

    # Count by path
    path_counts = {}
    for sid in section_ids:
        prefix = get_path_prefix(sid)
        path_counts[prefix] = path_counts.get(prefix, 0) + 1

    print("=== CYOA Graph v2 Validierung (Time Cave) ===")
    print("Abschnitte gesamt: {}".format(len(sections)))
    print("  Story: {}".format(len(stories)))
    print("  Choice: {}".format(len(choices)))
    print("  Enden: {}".format(len(endings)))
    print("  Sackgassen: {}".format(len(dead_ends)))
    print("  Nach Pfad: {}".format(
        ", ".join("{}={}".format(k, v) for k, v in sorted(path_counts.items()))))
    print()

    # 1. Kaputte Referenzen pruefen
    print("--- 1. Referenz-Pruefung ---")
    all_referenced = set()
    for sid, section in sections.items():
        targets = get_targets(section)
        for target in targets:
            all_referenced.add(target)
            if target not in section_ids:
                errors.append("Abschnitt {}: Verweis auf nicht-existierenden Abschnitt {}".format(sid, target))
        # Check return_to for dead ends
        if section.get("type") == "dead_end" and "return_to" in section:
            rt = section["return_to"]
            all_referenced.add(rt)
            if rt not in section_ids:
                errors.append("Dead End {}: return_to={} existiert nicht".format(sid, rt))

    unreachable = section_ids - all_referenced - {"P1"}
    if unreachable:
        for sid in sorted(unreachable):
            stype = sections[sid].get("type", "?")
            if stype != "ending":
                warnings.append("Abschnitt {} ({}) wird von keinem anderen Abschnitt referenziert".format(
                    sid, sections[sid].get('title', '?')))
    print("  Kaputte Referenzen: {}".format(
        sum(1 for e in errors if 'nicht-existierenden' in e)))
    print("  Nicht referenzierte Abschnitte: {}".format(len(unreachable)))

    # 2. Sackgassen pruefen
    print("\n--- 2. Sackgassen-Pruefung ---")
    for sid in sorted(dead_ends):
        s = sections[sid]
        if "return_to" not in s:
            errors.append("Sackgasse {}: Kein 'return_to' definiert".format(sid))
        if "return_text" not in s:
            warnings.append("Sackgasse {}: Kein 'return_text' definiert".format(sid))
    de_errors = sum(1 for e in errors if 'Sackgasse' in e)
    print("  Sackgassen OK: {}/{}".format(len(dead_ends) - de_errors, len(dead_ends)))

    # 3. Alle Pfade finden
    print("\n--- 3. Pfad-Analyse ---")
    paths = find_all_paths(sections)
    ending_paths = [p for p in paths if p[-1] in endings]
    dangling_paths = [p for p in paths if p[-1] not in endings]

    print("  Vollstaendige Pfade (zu einem Ende): {}".format(len(ending_paths)))
    if dangling_paths:
        print("  Pfade ohne Ende: {}".format(len(dangling_paths)))
        for p in dangling_paths[:5]:
            errors.append("Pfad endet ohne Ende bei Abschnitt {} ({})".format(
                p[-1], sections.get(p[-1], {}).get('title', '?')))

    # 4. Pfadlaengen
    print("\n--- 4. Pfadlaengen ---")
    if ending_paths:
        lengths = [len(p) for p in ending_paths]
        print("  Kuerzester Pfad: {} Abschnitte".format(min(lengths)))
        print("  Laengster Pfad: {} Abschnitte".format(max(lengths)))
        print("  Durchschnitt: {:.1f} Abschnitte".format(sum(lengths) / len(lengths)))

        # Warn if too short or too long
        too_short = [p for p in ending_paths if len(p) < 10]
        too_long = [p for p in ending_paths if len(p) > 50]
        if too_short:
            warnings.append("{} Pfade haben weniger als 10 Abschnitte".format(len(too_short)))
        if too_long:
            warnings.append("{} Pfade haben mehr als 50 Abschnitte".format(len(too_long)))

    # 5. Entscheidungspunkte zaehlen
    print("\n--- 5. Entscheidungspunkte ---")
    print("  Abschnitte mit Entscheidungen: {}".format(len(choices)))

    # Count choices per path
    choice_by_path = {}
    for sid in choices:
        prefix = get_path_prefix(sid)
        choice_by_path[prefix] = choice_by_path.get(prefix, 0) + 1
    print("  Nach Pfad: {}".format(
        ", ".join("{}={}".format(k, v) for k, v in sorted(choice_by_path.items()))))

    # 6. Time Cave Validierung: Konvergenz pruefen
    print("\n--- 6. Time Cave Pruefung ---")
    # Check that no section is reached from multiple different main paths
    # (except C->A/B convergence point)
    convergence_issues = []
    incoming = {}  # section -> set of source paths
    for sid, section in sections.items():
        targets = get_targets(section)
        src_path = get_path_prefix(sid)
        for target in targets:
            if target not in incoming:
                incoming[target] = set()
            incoming[target].add(src_path)

    for sid, sources in incoming.items():
        if len(sources) > 1:
            # C->A/B is the only allowed convergence
            if "C" in sources and len(sources) == 2:
                continue  # C merging into A or B is allowed
            convergence_issues.append(
                "Abschnitt {} wird von mehreren Pfaden erreicht: {}".format(
                    sid, ", ".join(sorted(sources))))

    if convergence_issues:
        for issue in convergence_issues:
            warnings.append("Konvergenz: " + issue)
    print("  Konvergenz-Punkte: {} (Ziel: 0-1)".format(len(convergence_issues)))

    # 7. MD-Dateien pruefen
    print("\n--- 7. Datei-Pruefung ---")
    v2_dir = Path(graph_path).parent
    missing_files = []
    for sid, section in sections.items():
        file_path = section.get("file")
        if file_path:
            full_path = v2_dir / file_path
            if not full_path.exists():
                missing_files.append("{}: {}".format(sid, file_path))
    print("  Fehlende Dateien: {}".format(len(missing_files)))
    if missing_files:
        for mf in missing_files[:10]:
            warnings.append("Datei fehlt: {}".format(mf))
        if len(missing_files) > 10:
            warnings.append("... und {} weitere".format(len(missing_files) - 10))

    # 8. Enden auflisten
    print("\n--- 8. Enden ---")
    for sid in sorted(endings):
        s = sections[sid]
        # Count paths reaching this ending
        reached = sum(1 for p in ending_paths if p[-1] == sid)
        family = s.get("family", "?")
        tone = s.get("tone", "?")
        print("  {}: \"{}\" ({}|{}) -- {} Pfade".format(
            sid, s.get('title', '?'), family, tone, reached))

    unreached_endings = [sid for sid in endings
                         if not any(p[-1] == sid for p in ending_paths)]
    if unreached_endings:
        for sid in unreached_endings:
            # Codewort-System-Enden (Geheim-Ende) werden NICHT ueber eine Graph-Kante
            # erreicht, sondern durch Eingabe der gesammelten Codewoerter. Das ist
            # gewollt (wie Band 1 E24) -> Warnung statt Fehler.
            if sections[sid].get("codewort_system"):
                req = sections[sid].get("requires", [])
                warnings.append(
                    "Geheim-Ende {} erreichbar nur per Codewort {} (kein Graph-Pfad, gewollt)".format(
                        sid, "+".join(req)))
            else:
                errors.append("Ende {} ist ueber keinen Pfad erreichbar".format(sid))

    # 9-13. QA-Analyse
    qa_data = generate_qa_report(sections, v2_dir)
    if qa_data:
        print_qa_summary(qa_data)

    # Zusammenfassung
    print("\n" + "=" * 40)
    if errors:
        print("\n[FEHLER] ({} Stueck):".format(len(errors)))
        for e in errors:
            print("  - {}".format(e))
    if warnings:
        print("\n[WARNUNGEN] ({} Stueck):".format(len(warnings)))
        for w in warnings:
            print("  - {}".format(w))
    if not errors and not warnings:
        print("\n[OK] Alle Pruefungen bestanden!")
    elif not errors:
        print("\n[OK] Keine Fehler, aber {} Warnung(en)".format(len(warnings)))
    else:
        print("\n[FEHLER] {} Fehler gefunden".format(len(errors)))

    return len(errors) == 0, qa_data, sections, v2_dir


if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    graph_path = project_root / "Band2" / "CYOA" / "graph_v2.yaml"

    export_report = "--report" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        graph_path = Path(args[0])

    if not graph_path.exists():
        print("Fehler: {} nicht gefunden".format(graph_path))
        sys.exit(1)

    success, qa_data, sections, v2_dir = validate(str(graph_path))

    if export_report and qa_data:
        output_dir = project_root / "Band2" / "CYOA"
        print("\n=== Exportiere QA-Reports ===")
        export_qa_markdown(qa_data, output_dir)
        export_crossref_markdown(sections, qa_data, v2_dir, output_dir)
        print("\nReports geschrieben nach: {}".format(output_dir))

    sys.exit(0 if success else 1)
