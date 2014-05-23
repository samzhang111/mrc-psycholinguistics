from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Word(Base):
    __tablename__ = 'word'

    # word id (row in the database)
    wid = Column(Integer, primary_key=True)
    # number of letters in word
    nlet = Column(Integer)
    # number of phonemes in word
    nphon = Column(Integer)
    # number of syllables in word
    nsyl = Column(Integer)
    # Kucera and Francis written frequency
    kf_freq = Column(Integer)
    # Kucera and Francis number of categories
    kf_ncats = Column(Integer)
    # K&F number of samples
    kf_nsamp = Column(Integer)
    # Thorndike-Lorge frequency
    tl_freq = Column(Integer)
    # Brown verbal frequency
    brown_freq = Column(Integer)
    # Familiarity
    fam = Column(Integer)
    # Concreteness
    conc = Column(Integer)
    # Imagery
    imag = Column(Integer)
    # Mean Colerado Meaningfulness
    meanc = Column(Integer)
    # Mean Pavio Meaningfulness
    meanp = Column(Integer)
    # Age of Acquisition
    aoa = Column(Integer)
    # Type
    tq2 = Column(String)
    # Part of speech
    wtype = Column(String)
    # PD Part of speech
    pdwtype = Column(String)
    # Alphasyllable
    alphasyl = Column(String)
    # Status
    status = Column(String)
    # Variant phoneme
    var = Column(String)
    # Written capitalized
    cap = Column(String)
    # Irregular plural
    irreg = Column(String)
    # The actual word
    word = Column(String)
    # Phonetic transcription
    phon = Column(String)
    # Edited phonetic transcription
    dphon = Column(String)
    # Stress pattern
    stress = Column(String)

    def __repr__(self):
        s = "<Word(\
id: %d\n\
nlet: %d\n\
nphon: %d\n\
nsyl: %d\n\
kf_freq: %d\n\
kf_ncats: %d\n\
kf_nsamp: %d\n\
tl_freq: %d\n\
brown_freq: %d\n\
fam: %d\n\
conc: %d\n\
imag: %d\n\
meanc: %d\n\
meanp: %d\n\
aoa: %d\n\
tq2: %s\n\
wtype: %s\n\
pdwtype: %s\n\
alphasyl: %s\n\
status: %s\n\
var: %s\n\
cap: %s\n\
irreg: %s\n\
word: %s\n\
phon: %s\n\
dphon: %s\n\
stress: %s)>\n" % (
        self.wid,
        self.nlet,
        self.nphon,
        self.nsyl,
        self.kf_freq,
        self.kf_ncats,
        self.kf_nsamp,
        self.tl_freq,
        self.brown_freq,
        self.fam,
        self.conc,
        self.imag,
        self.meanc,
        self.meanp,
        self.aoa,
        self.tq2,
        self.wtype,
        self.pdwtype,
        self.alphasyl,
        self.status,
        self.var,
        self.cap,
        self.irreg,
        self.word,
        self.phon,
        self.dphon,
        self.stress)

        return s

