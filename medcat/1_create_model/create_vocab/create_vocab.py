from medcat.vocab import Vocab

vocab = Vocab()

MODEL_DIR = "./models/"

# the vocab.txt file need to be in the tab sep format: <token>\t<word_count>\t<vector_embedding_separated_by_spaces>
# Current vocab uses pre-calculated vector embedding from Word2Vec, future use embeddings calculated from BERT tokeniser
# embeddings of 300 dimensions is standard

vocab.add_words('vocab_data.txt', replace=True)
vocab.make_unigram_table()
vocab.save(MODEL_DIR + "basic_vocab.dat")
