"""
Lexicon Builder and Analyzer Engine for sudo-learn-english.
Generates deterministic CEFR, Oxford 3000/5000, and IPA phonetic metadata.
"""

import json
import os
import re
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "engine" / "data"
BOOKS_DIR = BASE_DIR / "books" / "corpus" / "ebooks"
DATA_DIR.mkdir(exist_ok=True)
BOOKS_DIR.mkdir(exist_ok=True)

LEXICON_FILE = DATA_DIR / "cefr_oxford_lexicon.json"
USER_PROFILE_FILE = DATA_DIR / "user_lexicon.json"

# Core Seed Lexicon with verified CEFR levels, Oxford 3000 flags, and IPA phonetics
BASE_SEED_DATA = {
    # High-yield / Literature & Common Words
    "establish": {"cefr": "B2", "oxford": 3000, "ngsl": 412, "ipa": "/ɪˈstæb.lɪʃ/", "def": "set up or create on a firm or permanent basis"},
    "tie": {"cefr": "A2", "oxford": 3000, "ngsl": 680, "ipa": "/taɪ/", "def": "attach or fasten with string or cord; a bond or connection"},
    "tame": {"cefr": "B2", "oxford": 5000, "ngsl": 3200, "ipa": "/teɪm/", "def": "domesticate an animal; bring under control"},
    "essential": {"cefr": "B1", "oxford": 3000, "ngsl": 520, "ipa": "/ɪˈsen.ʃəl/", "def": "absolutely necessary; extremely important"},
    "invisible": {"cefr": "B2", "oxford": 3000, "ngsl": 1820, "ipa": "/ɪnˈvɪz.ə.bəl/", "def": "unable to be seen; not visible to the eye"},
    "consequence": {"cefr": "B1", "oxford": 3000, "ngsl": 610, "ipa": "/ˈkɒn.sɪ.kwəns/", "def": "a result or effect; importance or relevance"},
    "unique": {"cefr": "B1", "oxford": 3000, "ngsl": 780, "ipa": "/juːˈniːk/", "def": "being the only one of its kind; unlike anything else"},
    "monotonous": {"cefr": "C1", "oxford": 5000, "ngsl": 4500, "ipa": "/məˈnɒt.ən.əs/", "def": "dull, tedious, and repetitious; lacking variety"},
    "perplexed": {"cefr": "B2", "oxford": 5000, "ngsl": 3800, "ipa": "/pəˈplekst/", "def": "completely baffled; very puzzled"},
    "burrow": {"cefr": "B2", "oxford": 5000, "ngsl": 4100, "ipa": "/ˈbʌr.əʊ/", "def": "a hole or tunnel dug by a small animal"},
    "neglect": {"cefr": "B2", "oxford": 3000, "ngsl": 1420, "ipa": "/nɪˈɡlekt/", "def": "fail to care for properly"},
    "rite": {"cefr": "C1", "oxford": 5000, "ngsl": 3900, "ipa": "/raɪt/", "def": "a religious or other solemn ceremony or act"},
    "responsible": {"cefr": "B1", "oxford": 3000, "ngsl": 340, "ipa": "/rɪˈspɒn.sɪ.bəl/", "def": "having an obligation to do something as part of one's role"},
    "ponder": {"cefr": "C1", "oxford": 5000, "ngsl": 3600, "ipa": "/ˈpɒn.dər/", "def": "think about something carefully, especially before making a decision"},
    "thunderstruck": {"cefr": "C2", "oxford": 5000, "ngsl": 6200, "ipa": "/ˈθʌn.də.strʌk/", "def": "extremely surprised or shocked"},
    "apparition": {"cefr": "C2", "oxford": 5000, "ngsl": 5800, "ipa": "/ˌæp.əˈrɪʃ.ən/", "def": "a ghost or ghostlike image of a person"},
    "astonishment": {"cefr": "B2", "oxford": 5000, "ngsl": 2900, "ipa": "/əˈstɒn.ɪʃ.mənt/", "def": "great surprise; amazement"},
    "cumbersome": {"cefr": "C1", "oxford": 5000, "ngsl": 4200, "ipa": "/ˈkʌm.bə.səm/", "def": "large or heavy and therefore difficult to carry or use"},
    "indulgently": {"cefr": "C1", "oxford": 5000, "ngsl": 5100, "ipa": "/ɪnˈdʌl.dʒənt.li/", "def": "in a way that is ready to allow someone what they want"},
    "embarrassed": {"cefr": "B1", "oxford": 3000, "ngsl": 1100, "ipa": "/ɪmˈbær.əst/", "def": "feeling awkward, self-conscious, or ashamed"},
    
    # Who Moved My Cheese Vocabulary
    "maze": {"cefr": "B1", "oxford": 3000, "ngsl": 1850, "ipa": "/meɪz/", "def": "a complex network of paths or passages; a labyrinth"},
    "labyrinth": {"cefr": "C1", "oxford": 5000, "ngsl": 4600, "ipa": "/ˈlæb.ə.rɪnθ/", "def": "a complicated irregular network of passages or paths"},
    "corridor": {"cefr": "B1", "oxford": 3000, "ngsl": 1200, "ipa": "/ˈkɒr.ɪ.dɔːr/", "def": "a long passage in a building from which doors lead into rooms"},
    "chamber": {"cefr": "B2", "oxford": 3000, "ngsl": 1350, "ipa": "/ˈtʃeɪm.bər/", "def": "a large room used for formal or public events"},
    "instinct": {"cefr": "B2", "oxford": 3000, "ngsl": 1400, "ipa": "/ˈɪn.stɪŋkt/", "def": "an innate, typically fixed pattern of behavior in response to certain stimuli"},
    "morsel": {"cefr": "C2", "oxford": 5000, "ngsl": 5400, "ipa": "/ˈmɔː.səl/", "def": "a small piece or amount of food; a mouthful"},
    "arrogance": {"cefr": "C1", "oxford": 5000, "ngsl": 3200, "ipa": "/ˈær.ə.ɡəns/", "def": "an insulting way of thinking or behaving that comes from believing you are better"},
    "inevitable": {"cefr": "B2", "oxford": 3000, "ngsl": 980, "ipa": "/ɪnˈev.ɪ.tə.bəl/", "def": "certain to happen; unavoidable"},
    "overanalyze": {"cefr": "B2", "oxford": 5000, "ngsl": 4800, "ipa": "/ˌəʊ.vərˈæn.əl.aɪz/", "def": "analyze something in too much detail"},
    "holler": {"cefr": "B2", "oxford": 5000, "ngsl": 3100, "ipa": "/ˈhɒl.ər/", "def": "give a loud shout or cry"},
    "injustice": {"cefr": "B2", "oxford": 3000, "ngsl": 1600, "ipa": "/ɪnˈdʒʌs.tɪs/", "def": "lack of fairness or justice"},
    "scoff": {"cefr": "C1", "oxford": 5000, "ngsl": 4300, "ipa": "/skɒf/", "def": "speak to someone or about something in a scornfully derisive way"},
    "folly": {"cefr": "C1", "oxford": 5000, "ngsl": 3700, "ipa": "/ˈfɒl.i/", "def": "lack of good sense; foolishness"},
    "inhibitor": {"cefr": "C1", "oxford": 5000, "ngsl": 4900, "ipa": "/ɪnˈhɪb.ɪ.tər/", "def": "a thing that inhibits, prevents, or slows something down"},
    "prompt": {"cefr": "B2", "oxford": 3000, "ngsl": 890, "ipa": "/prɒmpt/", "def": "cause or bring about an action; encourage"},
    "anticipate": {"cefr": "B2", "oxford": 3000, "ngsl": 720, "ipa": "/ænˈtɪs.ɪ.peɪt/", "def": "regard as probable; expect or predict"},
}

def init_lexicon():
    """Initializes or expands the static lexicon with fallback default levels."""
    lexicon = {}
    if LEXICON_FILE.exists():
        try:
            with open(LEXICON_FILE, "r", encoding="utf-8") as f:
                lexicon = json.load(f)
        except Exception:
            lexicon = {}
    
    lexicon.update(BASE_SEED_DATA)
    with open(LEXICON_FILE, "w", encoding="utf-8") as f:
        json.dump(lexicon, f, ensure_ascii=False, indent=2)
    return lexicon

def init_user_profile():
    """Initializes user profile if not present."""
    if not USER_PROFILE_FILE.exists():
        profile = {
            "version": "1.0",
            "user": "quentin2001",
            "stats": {
                "total_books_read": 1,
                "total_words_absorbed": 15000,
                "current_level": "Phase 1 (Flow & Confidence)"
            },
            "books": {
                "01-the-little-prince": {
                    "title": "The Little Prince",
                    "status": "completed",
                    "date_completed": "2026-08",
                    "words_count": 15000,
                    "unique_lemmas": 1240,
                    "active_collocations": ["establish ties", "matter of consequence", "in the blink of an eye", "look with the heart"]
                },
                "02-who-moved-my-cheese": {
                    "title": "Who Moved My Cheese?",
                    "status": "reading",
                    "progress_pct": 50,
                    "words_count": 10000,
                    "unique_lemmas": 850,
                    "active_collocations": ["anticipate change", "let go of fear", "laugh at oneself"]
                }
            },
            "known_words": {},
            "target_learning_words": {}
        }
        with open(USER_PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(profile, f, ensure_ascii=False, indent=2)
        return profile
    else:
        with open(USER_PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

if __name__ == "__main__":
    init_lexicon()
    init_user_profile()
    print("Lexicon and User Profile initialized successfully.")
