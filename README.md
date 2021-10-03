# CS3244 Twemoji ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=RussellDash332/CS3244-Twemoji)

**Welcome to our CS3244 group project!**

We will push everything here for new updates. Stay tuned!

## Setup
- Dataset can be found [here](https://uvaauas.figshare.com/articles/dataset/Twemoji_Dataset/5822100).
- For Linux users, to install requirements, run `pip -r install requirements.txt`

## About
Collection of 13M tweets divided into training, validation, and test sets for the purposes of predicting emoji based on text and/or images. The data provides the tweet status ID and the emoji annotations associated with it. In the case of image-containing subsets, the image URL is also listed.
- The **full, unbalanced** dataset consists of a random test and validation sets of 1M tweets, with the remainder in the training set.
- The **balanced testset** is a subset of the test set chosen to improve emoji class balance.
- The **image** subsets are image-containing tweets.
- Finally, `emoji_map_1791.csv` provides information regarding the emoji labels and potential metadata.
