#!/usr/bin/env python3
"""
Erweiterte Qualitätsanalyse für Die Geisterspürer Band 1 CYOA.

Prüft Stil-Regeln, die der Validator nicht abdeckt:
1. Satzlänge (Ziel 10-15, Max 18 Wörter)
2. Passiv-Erkennung
3. Dialog-Verben (nur erlaubte)
4. Verbotenes Vokabular
5. Absatzlänge (3-6 Zeilen)
6. Pfad-Gesamtwortanzahl
7. Anführungszeichen-Konsistenz
8. Wortanzahl pro Abschnitt (differenziert nach Typ)

Nutzung:
  python analyze_quality.py
"""

import yaml
import os
import re
import sys
from pathlib import Path
from collections import defaultdict


# ============================================================
# Konfiguration
# ============================================================

_SCRIPT_DIR = Path(__file__).parent
_PROJECT_ROOT = _SCRIPT_DIR.parent
V2_DIR = _PROJECT_ROOT / "Band1" / "CYOA" / "v2"
GRAPH_FILE = V2_DIR / "graph_v2.yaml"
OUTPUT_FILE = _PROJECT_ROOT / "Band1" / "CYOA" / "Analyse_Report.md"

# Erlaubte Dialog-Verben
ERLAUBTE_DIALOG_VERBEN = {
    "sagte", "flüsterte", "rief", "murmelte",
    "zischte", "fragte", "schrie",
}

# Verbotene Dialog-Verben
VERBOTENE_DIALOG_VERBEN = {
    "antwortete", "erklärte", "meinte", "entgegnete",
    "erwiderte", "bemerkte", "versetzte", "seufzte", "stöhnte",
    "knurrte", "brummte",
}

# Verbotenes Vokabular
VERBOTENES_VOKABULAR = [
    "Manifestation", "paranormal", "Entität",
    "observieren", "melancholisch", "transparent",
]

# Passiv-Muster
PASSIV_RE = re.compile(
    r'\b(wurde|wurden|wird|werden)\s+\w+(t|en|et)\b',
    re.IGNORECASE
)

# Anfuehrungszeichen-Muster
GUILLEMETS_RE = re.compile(r'[»«]')
GERADE_QUOTES_RE = re.compile(r'(?<!\w)["\u201e\u201c\u201d]')


# ============================================================
# Hilfsfunktionen
# ============================================================

def load_graph():
    with open(GRAPH_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_content(md_path):
    """Liest eine MD-Datei und gibt den reinen Prosa-Inhalt zurueck."""
    if not md_path.exists():
        return "", []

    text = md_path.read_text(encoding="utf-8")
    lines = text.strip().split("\n")

    content_lines = []
    for line in lines:
        s = line.strip()
        if s.startswith("#"):
            continue
        if s.startswith("---"):
            continue
        if s.startswith("*Weiter mit") or s.startswith("*Gehe zu") or s.startswith("*Geh zu"):
            continue
        if s.startswith("*Wenn du"):
            continue
        if s.startswith("**") and ("→" in s or "->" in s):
            continue
        if s.startswith("*") and ("Abschnitt" in s or "Ende" in s):
            continue
        content_lines.append(line)  # Originalzeile mit Einrueckung

    return "\n".join(content_lines), content_lines


def split_sentences(text):
    """Teilt Text in Saetze auf."""
    # Bereinige Markdown-Formatierung
    clean = re.sub(r'\*[^*]+\*', '', text)  # Kursiv entfernen
    clean = re.sub(r'\*\*[^*]+\*\*', '', clean)  # Fett entfernen

    # Saetze an . ! ? aufteilen (nicht bei Abkuerzungen)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ»"])', clean)
    # Auch bei Zeilenumbruch nach Satzende
    expanded = []
    for s in sentences:
        parts = re.split(r'(?<=[.!?])\s*\n\s*(?=[A-ZÄÖÜ»"])', s)
        expanded.extend(parts)

    return [s.strip() for s in expanded if s.strip() and len(s.strip()) > 3]


def count_words(text):
    return len(re.findall(r'\b\w+\b', text))


def get_targets(section):
    targets = []
    if "choices" in section:
        for c in section["choices"]:
            targets.append(c["target"])
    if "next" in section:
        targets.append(section["next"])
    return targets


# ============================================================
# Analyse-Funktionen
# ============================================================

def check_sentence_length(content, filename):
    """Prueft Satzlaenge. Ziel: 10-15, Max: 18."""
    issues = []
    sentences = split_sentences(content)

    lengths = []
    for sentence in sentences:
        wc = count_words(sentence)
        if wc < 3:
            continue
        lengths.append(wc)
        if wc > 18:
            # Kuerze den Satz fuer die Ausgabe
            preview = sentence[:80] + "..." if len(sentence) > 80 else sentence
            issues.append({
                "file": filename,
                "words": wc,
                "sentence": preview,
            })

    avg = sum(lengths) / len(lengths) if lengths else 0
    return issues, avg, lengths


def check_passive_voice(content, filename):
    """Erkennt Passiv-Konstruktionen."""
    issues = []
    lines = content.split("\n")
    for i, line in enumerate(lines, 1):
        matches = PASSIV_RE.finditer(line)
        for m in matches:
            # Filtere false positives
            match_text = m.group(0)
            # "wurde still" ist kein Passiv
            if re.search(r'wurde\s+(still|blass|rot|bleich|wach|müde|laut|leise|eng|weit|kalt|warm|hell|dunkel|nass|trocken)', match_text, re.IGNORECASE):
                continue
            preview = line.strip()[:80]
            issues.append({
                "file": filename,
                "line": i,
                "match": match_text,
                "context": preview,
            })
    return issues


def check_dialog_verbs(content, filename):
    """Prueft Dialog-Verben auf Erlaubnis."""
    issues = []
    # Suche nach Mustern wie: sagte X, fluesterte X, etc.
    pattern = re.compile(r'[»«"\u201c\u201d][^»«"\u201c\u201d]*[»«"\u201c\u201d]\s*,?\s*(\w+)\s', re.MULTILINE)
    for m in pattern.finditer(content):
        verb = m.group(1).lower()
        if verb in VERBOTENE_DIALOG_VERBEN:
            context = content[max(0, m.start()-20):m.end()+20].strip()
            issues.append({
                "file": filename,
                "verb": verb,
                "context": context[:80],
            })
    return issues


def check_forbidden_vocab(content, filename):
    """Sucht nach verbotenem Vokabular."""
    issues = []
    for word in VERBOTENES_VOKABULAR:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        for m in pattern.finditer(content):
            context = content[max(0, m.start()-30):m.end()+30].strip()
            issues.append({
                "file": filename,
                "word": word,
                "context": context[:80],
            })
    return issues


def check_paragraph_length(content_lines, filename):
    """Prueft Absatzlaenge (3-6 Zeilen)."""
    issues = []
    paragraphs = []
    current = []

    for line in content_lines:
        if line.strip() == "":
            if current:
                paragraphs.append(current)
                current = []
        else:
            current.append(line)
    if current:
        paragraphs.append(current)

    for i, para in enumerate(paragraphs):
        line_count = len(para)
        if line_count > 6:
            preview = para[0].strip()[:60]
            issues.append({
                "file": filename,
                "paragraph": i + 1,
                "lines": line_count,
                "preview": preview,
            })

    return issues


def check_quote_style(content, filename):
    """Prueft Anfuehrungszeichen-Konsistenz."""
    has_guillemets = bool(GUILLEMETS_RE.search(content))
    has_straight = bool(GERADE_QUOTES_RE.search(content))
    return has_guillemets, has_straight


def calculate_path_wordcounts(sections):
    """Berechnet Gesamt-Wortanzahl fuer jeden Pfad von P1 bis Ende."""
    dead_ends = {sid for sid, s in sections.items() if s.get("type") == "dead_end"}
    endings_set = {sid for sid, s in sections.items() if s.get("type") == "ending"}

    # Cache word counts
    word_counts = {}
    for sid, section in sections.items():
        fp = section.get("file")
        if fp:
            md_path = V2_DIR / fp
            content, _ = get_content(md_path)
            word_counts[sid] = count_words(content)
        else:
            word_counts[sid] = 0

    paths = []
    stack = [("P1", ["P1"])]
    max_steps = 120

    while stack:
        current, path = stack.pop()
        section = sections.get(current)
        if section is None:
            continue

        if current in endings_set:
            total_words = sum(word_counts.get(s, 0) for s in path)
            paths.append({
                "path": path,
                "ending": current,
                "ending_title": section.get("title", "?"),
                "length": len(path),
                "total_words": total_words,
            })
            continue

        if current in dead_ends:
            continue

        targets = get_targets(section)
        if not targets:
            continue

        for target in targets:
            if target in dead_ends:
                continue
            if len(path) >= max_steps:
                continue
            if target in path:
                continue
            stack.append((target, path + [target]))

    return paths


# ============================================================
# Hauptprogramm
# ============================================================

def main():
    data = load_graph()
    sections = data["sections"]

    print("=" * 70)
    print("  ERWEITERTE QUALITÄTSANALYSE — Die Geisterspürer Band 1 CYOA")
    print("=" * 70)

    report = []
    report.append("# Analyse-Report — Die Geisterspürer Band 1 CYOA")
    report.append("")
    report.append("Automatisch generiert von `Scripts/analyze_quality.py`")
    report.append("")

    # ============================================================
    # 1. Satzlaenge
    # ============================================================
    print("\n--- 1. SATZLÄNGE (Ziel: 10-15, Max: 18) ---")
    report.append("## 1. Satzlänge")
    report.append("")

    all_sentence_issues = []
    all_avg_lengths = {}

    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        md_path = V2_DIR / fp
        content, _ = get_content(md_path)
        if not content.strip():
            continue

        issues, avg, lengths = check_sentence_length(content, sid)
        all_sentence_issues.extend(issues)
        if avg > 0:
            all_avg_lengths[sid] = avg

    over_18 = len(all_sentence_issues)
    overall_avg = sum(all_avg_lengths.values()) / len(all_avg_lengths) if all_avg_lengths else 0
    print(f"  Durchschnittliche Satzlänge: {overall_avg:.1f} Wörter")
    print(f"  Sätze über 18 Wörter: {over_18}")

    report.append(f"- Durchschnittliche Satzlänge: **{overall_avg:.1f}** Wörter")
    report.append(f"- Sätze über 18 Wörter: **{over_18}**")
    report.append("")

    if all_sentence_issues:
        report.append("### Zu lange Sätze (>18 Wörter)")
        report.append("")
        report.append("| Abschnitt | Wörter | Satz |")
        report.append("|-----------|--------|------|")
        for issue in sorted(all_sentence_issues, key=lambda x: -x["words"])[:30]:
            satz = issue["sentence"].replace("|", "\\|")
            report.append(f"| {issue['file']} | {issue['words']} | {satz} |")
        if len(all_sentence_issues) > 30:
            report.append(f"| ... | ... | +{len(all_sentence_issues)-30} weitere |")
        report.append("")

        # Top 5 ausgeben
        for issue in sorted(all_sentence_issues, key=lambda x: -x["words"])[:5]:
            print(f"    {issue['file']}: {issue['words']}W — {issue['sentence'][:60]}...")

    # ============================================================
    # 2. Passiv
    # ============================================================
    print(f"\n--- 2. PASSIV-ERKENNUNG ---")
    report.append("## 2. Passiv-Konstruktionen")
    report.append("")

    all_passive = []
    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        content, _ = get_content(V2_DIR / fp)
        issues = check_passive_voice(content, sid)
        all_passive.extend(issues)

    print(f"  Passiv-Konstruktionen gefunden: {len(all_passive)}")
    report.append(f"- Passiv-Konstruktionen: **{len(all_passive)}**")
    report.append("")

    if all_passive:
        report.append("| Abschnitt | Zeile | Passiv | Kontext |")
        report.append("|-----------|-------|--------|---------|")
        for issue in all_passive[:20]:
            report.append(f"| {issue['file']} | {issue['line']} | {issue['match']} | {issue['context'][:50]} |")
        if len(all_passive) > 20:
            report.append(f"| ... | ... | ... | +{len(all_passive)-20} weitere |")
        report.append("")

        for issue in all_passive[:3]:
            print(f"    {issue['file']} Z{issue['line']}: \"{issue['match']}\" — {issue['context'][:50]}")

    # ============================================================
    # 3. Dialog-Verben
    # ============================================================
    print(f"\n--- 3. DIALOG-VERBEN ---")
    report.append("## 3. Dialog-Verben")
    report.append("")

    all_verb_issues = []
    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        content, _ = get_content(V2_DIR / fp)
        issues = check_dialog_verbs(content, sid)
        all_verb_issues.extend(issues)

    print(f"  Verbotene Dialog-Verben: {len(all_verb_issues)}")
    report.append(f"- Verbotene Dialog-Verben: **{len(all_verb_issues)}**")
    report.append(f"- Erlaubt: sagte, flüsterte, rief, murmelte, zischte, fragte")
    report.append("")

    if all_verb_issues:
        report.append("| Abschnitt | Verb | Kontext |")
        report.append("|-----------|------|---------|")
        for issue in all_verb_issues:
            report.append(f"| {issue['file']} | {issue['verb']} | {issue['context'][:60]} |")
        report.append("")

        for issue in all_verb_issues[:5]:
            print(f"    {issue['file']}: \"{issue['verb']}\" — {issue['context'][:50]}")

    # ============================================================
    # 4. Verbotenes Vokabular
    # ============================================================
    print(f"\n--- 4. VERBOTENES VOKABULAR ---")
    report.append("## 4. Verbotenes Vokabular")
    report.append("")

    all_vocab_issues = []
    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        content, _ = get_content(V2_DIR / fp)
        issues = check_forbidden_vocab(content, sid)
        all_vocab_issues.extend(issues)

    print(f"  Verbotene Wörter gefunden: {len(all_vocab_issues)}")
    report.append(f"- Verbotene Wörter: **{len(all_vocab_issues)}**")
    report.append("")

    if all_vocab_issues:
        report.append("| Abschnitt | Wort | Kontext |")
        report.append("|-----------|------|---------|")
        for issue in all_vocab_issues:
            report.append(f"| {issue['file']} | {issue['word']} | {issue['context'][:60]} |")
        report.append("")

    if not all_vocab_issues:
        print("  Keine verbotenen Wörter gefunden!")

    # ============================================================
    # 5. Absatzlaenge
    # ============================================================
    print(f"\n--- 5. ABSATZLÄNGE (Max: 6 Zeilen) ---")
    report.append("## 5. Absatzlänge")
    report.append("")

    all_para_issues = []
    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        _, content_lines = get_content(V2_DIR / fp)
        issues = check_paragraph_length(content_lines, sid)
        all_para_issues.extend(issues)

    print(f"  Absätze über 6 Zeilen: {len(all_para_issues)}")
    report.append(f"- Absätze über 6 Zeilen: **{len(all_para_issues)}**")
    report.append("")

    if all_para_issues:
        report.append("| Abschnitt | Absatz | Zeilen | Anfang |")
        report.append("|-----------|--------|--------|--------|")
        for issue in all_para_issues:
            report.append(f"| {issue['file']} | {issue['paragraph']} | {issue['lines']} | {issue['preview'][:40]} |")
        report.append("")

        for issue in all_para_issues[:3]:
            print(f"    {issue['file']}: Absatz {issue['paragraph']} hat {issue['lines']} Zeilen")

    # ============================================================
    # 6. Anfuehrungszeichen-Konsistenz
    # ============================================================
    print(f"\n--- 6. ANFÜHRUNGSZEICHEN ---")
    report.append("## 6. Anführungszeichen-Konsistenz")
    report.append("")

    guillemet_files = []
    straight_files = []
    mixed_files = []

    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        content, _ = get_content(V2_DIR / fp)
        has_g, has_s = check_quote_style(content, sid)
        if has_g and has_s:
            mixed_files.append(sid)
        elif has_g:
            guillemet_files.append(sid)
        elif has_s:
            straight_files.append(sid)

    print(f"  Guillemets (»«): {len(guillemet_files)} Abschnitte")
    print(f"  Gerade (\"\"): {len(straight_files)} Abschnitte")
    print(f"  GEMISCHT: {len(mixed_files)} Abschnitte")

    report.append(f"- Guillemets (»«): **{len(guillemet_files)}** Abschnitte")
    report.append(f"- Gerade Anführungszeichen: **{len(straight_files)}** Abschnitte")
    report.append(f"- Gemischt (beides): **{len(mixed_files)}** Abschnitte")
    report.append("")

    if mixed_files:
        report.append("### Gemischte Anführungszeichen")
        report.append("")
        for sid in mixed_files:
            report.append(f"- **{sid}**")
        report.append("")

    # ============================================================
    # 7. Pfad-Gesamtwortanzahl
    # ============================================================
    print(f"\n--- 7. PFAD-GESAMTWORTANZAHL ---")
    report.append("## 7. Pfad-Gesamtwortanzahl")
    report.append("")

    path_data = calculate_path_wordcounts(sections)

    if path_data:
        # Gruppieren nach Pfad-Typ
        by_path = defaultdict(list)
        for p in path_data:
            # Bestimme Hauptpfad anhand des 6. Abschnitts (nach P1-P5)
            if len(p["path"]) > 5:
                sixth = p["path"][5]
                if sixth.startswith("A") or sixth.startswith("AP"):
                    by_path["A"].append(p)
                elif sixth.startswith("B"):
                    by_path["B"].append(p)
                elif sixth.startswith("C"):
                    by_path["C"].append(p)
                else:
                    by_path["?"].append(p)
            else:
                by_path["?"].append(p)

        report.append("| Pfad | Kürzester | Längster | Ø Wörter | Ø Abschnitte |")
        report.append("|------|----------|---------|----------|-------------|")

        for pfad in sorted(by_path.keys()):
            routes = by_path[pfad]
            words = [r["total_words"] for r in routes]
            lengths = [r["length"] for r in routes]
            shortest = min(routes, key=lambda r: r["total_words"])
            longest = max(routes, key=lambda r: r["total_words"])
            avg_w = sum(words) / len(words)
            avg_l = sum(lengths) / len(lengths)

            print(f"  Pfad {pfad}: {len(routes)} Routen, {min(words)}-{max(words)} Wörter, Ø {avg_w:.0f}")
            report.append(f"| {pfad} | {min(words)} ({shortest['ending']}) | {max(words)} ({longest['ending']}) | {avg_w:.0f} | {avg_l:.0f} |")

        report.append("")

        # Kuerzeste und laengste Route gesamt
        shortest = min(path_data, key=lambda r: r["total_words"])
        longest = max(path_data, key=lambda r: r["total_words"])

        report.append(f"**Kürzeste Route:** {shortest['total_words']} Wörter → {shortest['ending']} \"{shortest['ending_title']}\" ({shortest['length']} Abschnitte)")
        report.append("")
        report.append(f"**Längste Route:** {longest['total_words']} Wörter → {longest['ending']} \"{longest['ending_title']}\" ({longest['length']} Abschnitte)")
        report.append("")

        print(f"\n  Kürzeste Route: {shortest['total_words']}W -> {shortest['ending']} ({shortest['length']} Abschn.)")
        print(f"  Längste Route:  {longest['total_words']}W -> {longest['ending']} ({longest['length']} Abschn.)")

    # ============================================================
    # 8. Wortanzahl differenziert nach Typ
    # ============================================================
    print(f"\n--- 8. WORTANZAHL NACH TYP ---")
    report.append("## 8. Wortanzahl nach Typ")
    report.append("")

    type_words = defaultdict(list)
    for sid, section in sorted(sections.items()):
        fp = section.get("file")
        if not fp:
            continue
        content, _ = get_content(V2_DIR / fp)
        wc = count_words(content)
        stype = section.get("type", "story")
        type_words[stype].append((sid, section.get("title", "?"), wc))

    report.append("| Typ | Anzahl | Ø Wörter | Min | Max | Ziel |")
    report.append("|-----|--------|----------|-----|-----|------|")

    targets = {"story": "250-400", "choice": "250-400", "dead_end": "150-300", "ending": "200-350"}
    for stype in ["story", "choice", "dead_end", "ending"]:
        entries = type_words.get(stype, [])
        if not entries:
            continue
        words = [e[2] for e in entries]
        avg = sum(words) / len(words)
        ziel = targets.get(stype, "?")
        print(f"  {stype}: {len(entries)} Abschnitte, Ø {avg:.0f}W (Min {min(words)}, Max {max(words)})")
        report.append(f"| {stype} | {len(entries)} | {avg:.0f} | {min(words)} | {max(words)} | {ziel} |")

    report.append("")

    # Zu kurze Abschnitte nach Typ
    short_sections = []
    min_words = {"story": 250, "choice": 250, "dead_end": 150, "ending": 200}
    for stype, entries in type_words.items():
        threshold = min_words.get(stype, 200)
        for sid, title, wc in entries:
            if wc < threshold:
                short_sections.append((sid, title, wc, stype, threshold))

    if short_sections:
        report.append("### Zu kurze Abschnitte")
        report.append("")
        report.append("| Abschnitt | Titel | Wörter | Typ | Minimum |")
        report.append("|-----------|-------|--------|-----|---------|")
        for sid, title, wc, stype, threshold in sorted(short_sections, key=lambda x: x[2]):
            report.append(f"| {sid} | {title} | {wc} | {stype} | {threshold} |")
        report.append("")

    # ============================================================
    # Report schreiben
    # ============================================================
    report.append("---")
    report.append("")
    report.append("*Generiert mit analyze_quality.py*")

    OUTPUT_FILE.write_text("\n".join(report), encoding="utf-8")
    print(f"\n{'=' * 70}")
    print(f"  Report geschrieben: {OUTPUT_FILE}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
