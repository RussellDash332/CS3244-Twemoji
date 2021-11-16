# CS3244 Twemoji ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=RussellDash332/CS3244-Twemoji)

**Welcome to our CS3244 group project!**

We will push everything here for new updates. Stay tuned!

## Structure
```
CS3244-Twemoji
├── Datasets
│   ├── Original
│   │   ├── balanced_test_plaintext.txt
│   │   ├── emoji_map_1791.csv
│   │   ├── full_test_plaintext.txt
│   │   ├── full_train_plaintext.txt
│   │   ├── full_valid_plaintext.txt
│   │   ├── img_test_plaintext.txt
│   │   ├── img_train_plaintext.txt
│   │   ├── img_valid_plaintext.txt
│   │   ├── test_balanced_final.csv
│   │   ├── test_text_final.csv
│   │   ├── train_text_final.csv
│   │   └── valid_text_final.csv
│   ├── train_text_emoji_[1-12].csv
│   ├── test_text_emoji_[1-12].csv
│   └── valid_text_emoji_[1-12].csv
│
├── Models
│   ├── BERT
│   ├── DistilBERT-[1,2]
│   ├── LSTM
│   ├── NLTK-sklearn
│   ├── RNN
│   └── XLNet
│
├── Sample Code
│   └── ... (just a sample code)
│
├── .gitignore
├── Cleaning-1.ipynb
├── Cleaning-2.ipynb
├── emojify.py
├── Playground.ipynb
├── README.md
└── requirements.txt
```

## Setup
- Dataset can be found [here](https://uvaauas.figshare.com/articles/dataset/Twemoji_Dataset/5822100).
- For Linux users, to install requirements, run `pip -r install requirements.txt` (currently not up to date because unused).

## About
Collection of 13M tweets divided into training, validation, and test sets for the purposes of predicting emoji based on text and/or images. The data provides the tweet status ID and the emoji annotations associated with it. In the case of image-containing subsets, the image URL is also listed.
- The **full, unbalanced** dataset consists of a random test and validation sets of 1M tweets, with the remainder in the training set.
- The **balanced testset** is a subset of the test set chosen to improve emoji class balance.
- The **image** subsets are image-containing tweets.
- Finally, `emoji_map_1791.csv` provides information regarding the emoji labels and potential metadata.
