from os.path import join
from codecs import open

def build_dataset(split, make_vocab=True, data_dir="./ResumeNER"):
    assert split in ["train", "dev", "test"]

    word_lists = []
    tag_lists = []
    with open(join(data_dir, split+".char.bmes"), "r", encoding="utf-8") as f:
        word_list = []
        tag_list = [] 
        for line in f:
            # one paragraph is segerated by \n
            if line!="\n":
                word, tag = line.strip("\n").split()
                word_list.append(word)
                tag_list.append(tag)
            else:
                word_lists.append(word_list)
                tag_lists.append(tag_list)
                word_list = []
                tag_list = []
    
    # if require vocab
    if make_vocab:
        word2id = build_map(word_lists)
        tag2id = build_map(tag_lists)
        return word_lists, tag_lists, word2id, tag2id
    else:
        return word_lists, tag_lists


def build_map(lists):
    maps = {}
    for list_ in lists:
        for e in list_:
            if e not in maps:
                maps[e] = len(maps)

    return maps
            



if __name__ == "__main__":
    word_lists, tag_lists, word2id, tag2id = build_dataset("train", True, "./ResumeNER")
    print("word_lists count:", "\t", len(word_lists))
    print("tag_lists count:", "\t", len(tag_lists))
    print("word2id size:", "\t", len(word2id))
    print("tag2id size:", "\t", len(tag2id))













