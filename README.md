# CS3244-Twemoji

Collection of 13M tweets divided into training, validation, and test sets for the purposes of predicting emoji based on text and/or images. The data provides the tweet status ID and the emoji annotations associated with it. In the case of image-containing subsets, the image URL is also listed.
- The **full, unbalanced** dataset consists of a random test and validation sets of 1M tweets, with the remainder in the training set.
- The **balanced testset** is a subset of the test set chosen to improve emoji class balance.
- The **image** subsets are image-containing tweets.
- Finally, `emoji_map_1791.csv` provides information regarding the emoji labels and potential metadata.
