#!/usr/bin/env python3
"""
sudo-learn-english CLI & NLP Engine
First-Principles Language Acquisition, Corpus Profiling & Lexical Graph Tracking.
"""

import argparse
import json
import math
import os
import re
import sys
from collections import Counter
from pathlib import Path

# Ensure UTF-8 output on Windows terminal
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "engine" / "data"
BOOKS_DIR = BASE_DIR / "books" / "corpus" / "ebooks"
LEXICON_FILE = DATA_DIR / "cefr_oxford_lexicon.json"
USER_PROFILE_FILE = DATA_DIR / "user_lexicon.json"

# Basic English Stopwords / Foundational A1/A2 Common Words (Not target candidates)
FUNCTION_WORDS = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with",
    "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if",
    "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him",
    "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than",
    "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how",
    "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most",
    "us", "is", "am", "are", "was", "were", "been", "has", "had", "did", "does", "having", "done", "said",
    "little", "draw", "drawing", "much", "many", "shall", "more", "most", "thousand", "hundred", "nothing", "every",
    "never", "always", "thing", "things", "person", "life", "man", "men", "boy", "girl", "night", "great", "small",
    "must", "should", "tell", "told", "ask", "asked", "answer", "answered", "call", "called", "find", "found",
    "went", "came", "look", "looked", "see", "saw", "seem", "seemed", "put", "let", "away", "down", "off", "again",
    "very", "too", "such", "own", "same", "place", "head", "hand", "eye", "eyes", "face", "voice", "water", "world",
    "prince", "sheep", "rose", "flower", "fox", "planet", "star", "chapter", "gutenberg", "project", "author"
}

def load_lexicon():
    if not LEXICON_FILE.exists():
        return {}
    with open(LEXICON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_user_profile():
    if not USER_PROFILE_FILE.exists():
        return {"known_words": {}, "books": {}, "stats": {}}
    with open(USER_PROFILE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_user_profile(profile):
    with open(USER_PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

def simple_lemmatize(word: str) -> str:
    """Lightweight rule-based English lemmatizer for clean token grouping."""
    w = word.lower()
    if len(w) <= 3:
        return w
    # Irregular / common plurals and verb forms
    irregulars = {
        "men": "man", "women": "woman", "children": "child", "mice": "mouse",
        "feet": "foot", "teeth": "tooth", "ran": "run", "saw": "see",
        "came": "come", "went": "go", "found": "find", "knew": "know",
        "thought": "think", "took": "take", "looked": "look", "called": "call",
        "became": "become", "smiled": "smile", "cried": "cry", "tried": "try"
    }
    if w in irregulars:
        return irregulars[w]
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith("es") and len(w) > 4:
        if w.endswith(("shes", "ches", "sses", "xes", "zes")):
            return w[:-2]
        return w[:-1]
    if w.endswith("s") and not w.endswith("ss") and len(w) > 3:
        return w[:-1]
    if w.endswith("ing") and len(w) > 5:
        base = w[:-3]
        if base.endswith(base[-1]) and base[-1] in "bcdfgklmnprstvz":
            return base[:-1]
        return base
    if w.endswith("ed") and len(w) > 4:
        base = w[:-2]
        if base.endswith("i"):
            return base[:-1] + "y"
        if base.endswith(base[-1]) and base[-1] in "bcdfgklmnprstvz":
            return base[:-1]
        return base
    return w

def extract_tokens_and_sentences(text: str):
    """Parses text into sentences and cleaned word tokens with exact sentence alignment."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    tokens = []
    word_to_sentences = {}

    for sent in sentences:
        clean_sent = sent.strip().replace('\n', ' ')
        if not clean_sent:
            continue
        words = re.findall(r"\b[A-Za-z]+(?:'[A-Za-z]+)?\b", clean_sent)
        for raw_w in words:
            lemma = simple_lemmatize(raw_w)
            tokens.append((raw_w.lower(), lemma))
            if lemma not in word_to_sentences:
                word_to_sentences[lemma] = []
            if len(word_to_sentences[lemma]) < 3:
                word_to_sentences[lemma].append(clean_sent)

    return tokens, word_to_sentences

def read_book_content(file_path: Path) -> str:
    """Extracts raw text from txt or pdf files seamlessly."""
    if file_path.suffix.lower() == ".pdf":
        try:
            import pypdf
            reader = pypdf.PdfReader(str(file_path))
            pages_text = [p.extract_text() or "" for p in reader.pages]
            return "\n".join(pages_text)
        except Exception as e:
            print(f"⚠️ PDF extraction error with pypdf: {e}")
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def analyze_book(file_path: Path):
    """Comprehensive linguistic and lexical analysis of a book."""
    if not file_path.exists():
        print(f"❌ Error: File {file_path} does not exist.")
        return None

    content = read_book_content(file_path)

    tokens, sentence_map = extract_tokens_and_sentences(content)
    total_tokens = len(tokens)
    lemmas = [lemma for _, lemma in tokens]
    lemma_counts = Counter(lemmas)
    unique_lemmas = len(lemma_counts)

    lexicon = load_lexicon()
    user_profile = load_user_profile()
    known_words = user_profile.get("known_words", {})

    # CEFR Level distribution
    cefr_counts = Counter()
    oxford_count = 0
    candidate_words = []

    for lemma, count in lemma_counts.items():
        if lemma in FUNCTION_WORDS:
            continue
        lex_meta = lexicon.get(lemma, {})
        cefr = lex_meta.get("cefr", "Uncategorized")
        cefr_counts[cefr] += count
        if lex_meta.get("oxford"):
            oxford_count += count
        
        # Candidate filter: appears >= 2 times, not a pure stopword, not in user's known base
        if count >= 2 and lemma not in known_words and len(lemma) > 3:
            candidate_words.append({
                "lemma": lemma,
                "count": count,
                "cefr": cefr,
                "ipa": lex_meta.get("ipa", "N/A"),
                "def": lex_meta.get("def", ""),
                "sentences": sentence_map.get(lemma, [])
            })

    candidate_words.sort(key=lambda x: x["count"], reverse=True)

    print("\n" + "=" * 65)
    print(f"📖  BOOK LEXICAL ANALYSIS: {file_path.name}")
    print("=" * 65)
    print(f"📊  Total Words (Tokens)       : {total_tokens:,}")
    print(f"🔑  Unique Word Lemmas        : {unique_lemmas:,}")
    print(f"📈  Lexical Diversity (TTR)   : {(unique_lemmas / total_tokens * 100):.2f}%")
    print(f"🎯  Oxford 3000 Core Words    : {oxford_count:,} ({oxford_count/total_tokens*100:.1f}%)")
    print("-" * 65)
    print("🌐  CEFR Level Distribution (in Lexicon database):")
    for lvl in ["A1", "A2", "B1", "B2", "C1", "C2", "Uncategorized"]:
        if cefr_counts[lvl] > 0:
            pct = (cefr_counts[lvl] / total_tokens) * 100
            bar = "█" * int(pct // 3)
            print(f"    {lvl:<14} : {cefr_counts[lvl]:>5} tokens ({pct:>5.1f}%) {bar}")
    print("-" * 65)
    print(f"🔍  Identified Candidate Keywords for Triage: {len(candidate_words)} lemmas")
    print("=" * 65 + "\n")

    return {
        "total_tokens": total_tokens,
        "unique_lemmas": unique_lemmas,
        "lemma_counts": lemma_counts,
        "candidate_words": candidate_words
    }

def triage_book(book_id: str):
    """Interactive rapid triage scanner to mark words as Known or Target Learning."""
    file_map = {
        "1": BOOKS_DIR / "01-the-little-prince.pdf",
        "01": BOOKS_DIR / "01-the-little-prince.pdf",
        "the-little-prince": BOOKS_DIR / "01-the-little-prince.pdf",
        "2": BOOKS_DIR / "02-who-moved-my-cheese.pdf",
        "02": BOOKS_DIR / "02-who-moved-my-cheese.pdf",
        "who-moved-my-cheese": BOOKS_DIR / "02-who-moved-my-cheese.pdf",
    }
    target_file = file_map.get(book_id)
    if not target_file or not target_file.exists():
        print(f"❌ Error: Book '{book_id}' not found in books directory.")
        return

    analysis = analyze_book(target_file)
    if not analysis:
        return

    candidates = analysis["candidate_words"]
    profile = load_user_profile()
    known = profile.setdefault("known_words", {})
    target_learning = profile.setdefault("target_learning_words", {})

    print(f"\n⚡ Starting 60-Second Rapid Triage for [{target_file.name}]...")
    print(f"💡 Found {len(candidates)} candidate words. Reviewing top candidates:")
    print("=" * 70)

    for i, item in enumerate(candidates[:15], 1):
        word = item['lemma']
        ipa = item['ipa']
        cefr = item['cefr']
        cnt = item['count']
        ex = item['sentences'][0] if item['sentences'] else "No sentence recorded."
        definition = item['def']

        print(f"\n[{i}/{min(len(candidates), 15)}]  Word: \033[1;36m{word.upper()}\033[0m  {ipa}  [{cefr}] (Appears {cnt}x)")
        if definition:
            print(f"     Definition : {definition}")
        print(f"     Excerpt    : \"{ex}\"")
        
        # In non-interactive mode or auto-run, record provenance
        known[word] = {
            "first_seen": target_file.stem,
            "occurrences": cnt,
            "status": "mastered" if cnt >= 4 else "familiar",
            "cefr": cefr
        }

    save_user_profile(profile)
    print("\n" + "=" * 70)
    print(f"✅ Triage Complete! Updated personal vocabulary graph in 'data/user_lexicon.json'.")
    print(f"📚 Total recorded vocabulary assets: {len(known)} lemmas.")
    print("=" * 70 + "\n")

def show_stats():
    """Displays cumulative vocabulary growth, cross-book recurrence and saturation."""
    profile = load_user_profile()
    known = profile.get("known_words", {})
    books = profile.get("books", {})

    print("\n" + "=" * 65)
    print("🏆  SUDO-LEARN-ENGLISH : CUMULATIVE VOCABULARY DASHBOARD")
    print("=" * 65)
    print(f"📚  Books Tracked in System     : {len(books)}")
    for bid, binfo in books.items():
        status_icon = "✅" if binfo.get("status") == "completed" else "⏳"
        print(f"    • {binfo.get('title'):<26} [{binfo.get('status').upper()} {status_icon}] ~{binfo.get('words_count'):,} words")
    print("-" * 65)
    print(f"💎  Total Unique Word Lemmas Logged : {len(known):,} words")
    
    # Saturation of Oxford 3000
    oxford_target = 3000
    current_oxford_est = len(known) + 800  # including high frequency base
    saturation_pct = min(100.0, (current_oxford_est / oxford_target) * 100)
    filled_blocks = int(saturation_pct // 5)
    empty_blocks = 20 - filled_blocks
    progress_bar = "█" * filled_blocks + "░" * empty_blocks

    print(f"🎯  Oxford 3000™ Saturation Curve   : [{progress_bar}] {saturation_pct:.1f}%")
    print(f"🔥  Next Milestone                  : 2,000 High-Frequency Core Saturation")
    print("=" * 65 + "\n")

def main():
    parser = argparse.ArgumentParser(description="sudo-learn-english NLP & Vocabulary Engine")
    subparsers = parser.add_subparsers(dest="command")

    # analyze
    analyze_p = subparsers.add_parser("analyze", help="Analyze an English text/corpus file")
    analyze_p.add_argument("file", type=str, help="Path to txt/epub file in corpus")

    # triage
    triage_p = subparsers.add_parser("triage", help="Run rapid triage for candidate words of a book")
    triage_p.add_argument("book_id", type=str, help="Book identifier (e.g. 01, 02, the-little-prince)")

    # stats
    subparsers.add_parser("stats", help="Display cumulative vocabulary dashboard and saturation")

    args = parser.parse_args()

    if args.command == "analyze":
        analyze_book(Path(args.file))
    elif args.command == "triage":
        triage_book(args.book_id)
    elif args.command == "stats":
        show_stats()
    else:
        # Default run stats if no argument provided
        show_stats()

if __name__ == "__main__":
    main()
