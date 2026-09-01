"""
Expanded Lexicon & Core Vocabulary Generator for sudo-learn-english.
Enriches data/cefr_oxford_lexicon.json with foundational A1-C2 vocabulary and phonetics.
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)
LEXICON_FILE = DATA_DIR / "cefr_oxford_lexicon.json"

# Expanded CEFR + Oxford 3000 + IPA mapping
COMPREHENSIVE_LEXICON = {
    # A1 Base
    "draw": {"cefr": "A1", "oxford": 3000, "ipa": "/drɔː/", "def": "produce a picture or diagram by making lines and marks"},
    "little": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈlɪt.əl/", "def": "small in size, amount, or degree"},
    "very": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈver.i/", "def": "in a high degree; extremely"},
    "sheep": {"cefr": "A1", "oxford": 3000, "ipa": "/ʃiːp/", "def": "a domesticated animal with a thick woolly coat"},
    "rose": {"cefr": "A1", "oxford": 3000, "ipa": "/rəʊz/", "def": "a fragrant flower with prickly stems"},
    "prince": {"cefr": "A2", "oxford": 3000, "ipa": "/prɪns/", "def": "the son of a monarch"},
    "king": {"cefr": "A1", "oxford": 3000, "ipa": "/kɪŋ/", "def": "the male ruler of an independent state"},
    "flower": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈflaʊ.ər/", "def": "the seed-bearing part of a plant"},
    "fox": {"cefr": "A2", "oxford": 3000, "ipa": "/fɒks/", "def": "a carnivorous mammal of the dog family"},
    "planet": {"cefr": "A2", "oxford": 3000, "ipa": "/ˈplæn.ɪt/", "def": "a celestial body moving in an elliptical orbit around a star"},
    "star": {"cefr": "A1", "oxford": 3000, "ipa": "/stɑːr/", "def": "a fixed luminous point in the night sky"},
    "friend": {"cefr": "A1", "oxford": 3000, "ipa": "/frend/", "def": "a person whom one knows and with whom one has a bond of mutual affection"},
    "grow": {"cefr": "A1", "oxford": 3000, "ipa": "/ɡrəʊ/", "def": "increase in size, quantity, or degree"},
    "grown": {"cefr": "A2", "oxford": 3000, "ipa": "/ɡrəʊn/", "def": "adult, fully developed"},
    "understand": {"cefr": "A1", "oxford": 3000, "ipa": "/ˌʌn.dəˈstænd/", "def": "perceive the intended meaning of words or a language"},
    "great": {"cefr": "A1", "oxford": 3000, "ipa": "/ɡreɪt/", "def": "of an extent, amount, or intensity considerably above the normal"},
    "thousand": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈθaʊ.zənd/", "def": "the number 1,000"},
    "nothing": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈnʌθ.ɪŋ/", "def": "not anything; no single thing"},
    "picture": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈpɪk.tʃər/", "def": "a painting or drawing"},
    "animal": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈæn.ɪ.məl/", "def": "a living organism that feeds on organic matter"},
    "water": {"cefr": "A1", "oxford": 3000, "ipa": "/ˈwɔː.tər/", "def": "a colourless, transparent, odourless liquid"},
    "voice": {"cefr": "A2", "oxford": 3000, "ipa": "/vɔɪs/", "def": "the sound produced in a person's larynx"},
    "heart": {"cefr": "A2", "oxford": 3000, "ipa": "/hɑːt/", "def": "the organ that pumps blood; the central or innermost part"},
    "eye": {"cefr": "A1", "oxford": 3000, "ipa": "/aɪ/", "def": "each of a pair of globular organs in the head through which people see"},
    "secret": {"cefr": "A2", "oxford": 3000, "ipa": "/ˈsiː.krət/", "def": "not known or seen or not meant to be known or seen by others"},
    "wheat": {"cefr": "B1", "oxford": 3000, "ipa": "/wiːt/", "def": "a cereal plant that is the most important kind grown in temperate countries"},
    "gold": {"cefr": "A2", "oxford": 3000, "ipa": "/ɡəʊld/", "def": "a yellow precious metal"},
    "golden": {"cefr": "B1", "oxford": 3000, "ipa": "/ˈɡəʊl.dən/", "def": "colored like gold; precious"},

    # B1 & B2 Core Chunks and Key Literary Terms
    "establish": {"cefr": "B2", "oxford": 3000, "ipa": "/ɪˈstæb.lɪʃ/", "def": "set up or create on a firm or permanent basis"},
    "tie": {"cefr": "A2", "oxford": 3000, "ipa": "/taɪ/", "def": "a bond, connection, or link"},
    "tame": {"cefr": "B2", "oxford": 5000, "ipa": "/teɪm/", "def": "domesticate an animal; establish an affectionate relationship"},
    "essential": {"cefr": "B1", "oxford": 3000, "ipa": "/ɪˈsen.ʃəl/", "def": "absolutely necessary; extremely important"},
    "invisible": {"cefr": "B2", "oxford": 3000, "ipa": "/ɪnˈvɪz.ə.bəl/", "def": "unable to be seen; hidden from sight"},
    "consequence": {"cefr": "B1", "oxford": 3000, "ipa": "/ˈkɒn.sɪ.kwəns/", "def": "a result or effect; importance or serious relevance"},
    "unique": {"cefr": "B1", "oxford": 3000, "ipa": "/juːˈniːk/", "def": "being the only one of its kind; unlike anything else"},
    "monotonous": {"cefr": "C1", "oxford": 5000, "ipa": "/məˈnɒt.ən.əs/", "def": "dull, tedious, and repetitious; lacking in variety and interest"},
    "perplexed": {"cefr": "B2", "oxford": 5000, "ipa": "/pəˈplekst/", "def": "completely baffled; very puzzled"},
    "burrow": {"cefr": "B2", "oxford": 5000, "ipa": "/ˈbʌr.əʊ/", "def": "a hole or tunnel dug by a small animal such as a fox or rabbit"},
    "neglect": {"cefr": "B2", "oxford": 3000, "ipa": "/nɪˈɡlekt/", "def": "fail to care for properly"},
    "rite": {"cefr": "C1", "oxford": 5000, "ipa": "/raɪt/", "def": "a ceremonial act or established social custom"},
    "responsible": {"cefr": "B1", "oxford": 3000, "ipa": "/rɪˈspɒn.sɪ.bəl/", "def": "having an obligation to care for someone or something"},
    "ponder": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈpɒn.dər/", "def": "think about something carefully, especially before making a decision"},
    "thunderstruck": {"cefr": "C2", "oxford": 5000, "ipa": "/ˈθʌn.də.strʌk/", "def": "extremely surprised or shocked"},
    "apparition": {"cefr": "C2", "oxford": 5000, "ipa": "/ˌæp.əˈrɪʃ.ən/", "def": "a remarkable or unexpected appearance of someone or something"},
    "astonishment": {"cefr": "B2", "oxford": 5000, "ipa": "/əˈstɒn.ɪʃ.mənt/", "def": "great surprise; amazement"},
    "cumbersome": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈkʌm.bə.səm/", "def": "large or heavy and therefore difficult to carry or use"},
    "indulgently": {"cefr": "C1", "oxford": 5000, "ipa": "/ɪnˈdʌl.dʒənt.li/", "def": "in a lenient, kind or permissive manner"},
    "embarrassed": {"cefr": "B1", "oxford": 3000, "ipa": "/ɪmˈbær.əst/", "def": "feeling awkward, self-conscious, or ashamed"},
    "primeval": {"cefr": "C2", "oxford": 5000, "ipa": "/praɪˈmiː.vəl/", "def": "of or resembling the earliest ages in the history of the world"},
    "constrictor": {"cefr": "C2", "oxford": 5000, "ipa": "/kənˈstrɪk.tər/", "def": "a snake that kills by coiling around its prey and suffocating it"},
    "disheartened": {"cefr": "C1", "oxford": 5000, "ipa": "/dɪsˈhɑː.tənd/", "def": "having lost determination or confidence; discouraged"},
    "sensible": {"cefr": "B1", "oxford": 3000, "ipa": "/ˈsen.sɪ.bəl/", "def": "possessing or displaying prudence and wise judgement"},
    "shipwrecked": {"cefr": "B2", "oxford": 5000, "ipa": "/ˈʃɪp.rekt/", "def": "left stranded after a ship is destroyed at sea"},

    # Who Moved My Cheese Vocabulary
    "maze": {"cefr": "B1", "oxford": 3000, "ipa": "/meɪz/", "def": "a complex network of paths or passages; a labyrinth"},
    "labyrinth": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈlæb.ə.rɪnθ/", "def": "a complicated irregular network of passages or paths"},
    "corridor": {"cefr": "B1", "oxford": 3000, "ipa": "/ˈkɒr.ɪ.dɔːr/", "def": "a long passage in a building from which doors lead into rooms"},
    "chamber": {"cefr": "B2", "oxford": 3000, "ipa": "/ˈtʃeɪm.bər/", "def": "a large room used for formal or public events"},
    "instinct": {"cefr": "B2", "oxford": 3000, "ipa": "/ˈɪn.stɪŋkt/", "def": "an innate, typically fixed pattern of behavior in response to certain stimuli"},
    "morsel": {"cefr": "C2", "oxford": 5000, "ipa": "/ˈmɔː.səl/", "def": "a small piece or amount of food; a mouthful"},
    "arrogance": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈær.ə.ɡəns/", "def": "an insulting way of thinking or behaving that comes from believing you are better"},
    "inevitable": {"cefr": "B2", "oxford": 3000, "ipa": "/ɪnˈev.ɪ.tə.bəl/", "def": "certain to happen; unavoidable"},
    "overanalyze": {"cefr": "B2", "oxford": 5000, "ipa": "/ˌəʊ.vərˈæn.əl.aɪz/", "def": "analyze something in too much detail"},
    "holler": {"cefr": "B2", "oxford": 5000, "ipa": "/ˈhɒl.ər/", "def": "give a loud shout or cry"},
    "injustice": {"cefr": "B2", "oxford": 3000, "ipa": "/ɪnˈdʒʌs.tɪs/", "def": "lack of fairness or justice"},
    "scoff": {"cefr": "C1", "oxford": 5000, "ipa": "/skɒf/", "def": "speak to someone or about something in a scornfully derisive way"},
    "folly": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈfɒl.i/", "def": "lack of good sense; foolishness"},
    "inhibitor": {"cefr": "C1", "oxford": 5000, "ipa": "/ɪnˈhɪb.ɪ.tər/", "def": "a thing that inhibits, prevents, or slows something down"},
    "prompt": {"cefr": "B2", "oxford": 3000, "ipa": "/prɒmpt/", "def": "cause or bring about an action; encourage"},
    "anticipate": {"cefr": "B2", "oxford": 3000, "ipa": "/ænˈtɪs.ɪ.peɪt/", "def": "regard as probable; expect or predict"},
    "scurry": {"cefr": "B2", "oxford": 5000, "ipa": "/ˈskʌr.i/", "def": "move hurriedly with quick short steps"},
    "routine": {"cefr": "A2", "oxford": 3000, "ipa": "/ruːˈtiːn/", "def": "a sequence of actions regularly followed"},
    "nourish": {"cefr": "B2", "oxford": 5000, "ipa": "/ˈnʌr.ɪʃ/", "def": "provide with the food or other substances necessary for growth, health, and good condition"},
    "nonverbal": {"cefr": "B2", "oxford": 5000, "ipa": "/ˌnɒnˈvɜː.bəl/", "def": "not involving or using words or speech"},
    "nibble": {"cefr": "B2", "oxford": 5000, "ipa": "/ˈnɪb.əl/", "def": "take small bites out of"},
    "arrogance": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈær.ə.ɡəns/", "def": "overbearing pride"},
    "rant": {"cefr": "C1", "oxford": 5000, "ipa": "/rænt/", "def": "speak or shout at length in a wild, impassioned way"},
    "rave": {"cefr": "B2", "oxford": 5000, "ipa": "/reɪv/", "def": "talk wildly or incoherently, as if delirious"},
    "immobilize": {"cefr": "C1", "oxford": 5000, "ipa": "/ɪˈməʊ.bəl.aɪz/", "def": "prevent from moving or operating as normal"},
    "folly": {"cefr": "C1", "oxford": 5000, "ipa": "/ˈfɒl.i/", "def": "foolishness"}
}

def update_lexicon():
    with open(LEXICON_FILE, "w", encoding="utf-8") as f:
        json.dump(COMPREHENSIVE_LEXICON, f, ensure_ascii=False, indent=2)
    print(f"Updated {LEXICON_FILE} with {len(COMPREHENSIVE_LEXICON)} lexical entries.")

if __name__ == "__main__":
    update_lexicon()
