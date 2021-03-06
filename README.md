# EDA-Chinese
Easy Data Augmentation for NLP on Chinese, based on [EDA_NLP](https://github.com/jasonwei20/eda_nlp/tree/master/code)

## 1. Noted:
1. Input file contains the sentences, one sentence one line
2. Each sentence should be segmented before processing by EDA-Chinese, use space to split the segmentations.
3. Each output sentence will be the sentence with some space to segment.
4. Every line of input file must have a sentence or the script will crash down.
5. Processing speed may be slow in the begining, but it will become more and more faster beacuse of the cache.

## 2. Requirements:
1. [Synonyms](https://github.com/huyingxi/Synonyms):   
    `pip install -U synonyms`  
    Download this package from pip maybe very slow, you can choose to download the source code from the GitHub and install it manually.  
    `python setup.py install`
    
2. Chinese Stop Words: [Baidu stop words](https://github.com/goto456/stopwords)

## 3. How to use:
1. create the data folder to hold the input sentences and augmentation sentences  
`mkdir data`

2. Put your data into `data` folder, chinese sentence need to be segmented and split with space. 

3. Data Augmentation  
`num_aug`: number of augmented sentences per original sentence  
`alpha`: percent of words in each sentence to be changed, details can be found [here](https://arxiv.org/abs/1901.11196)

`python augmentation.py --input ./data/<input_file> --output ./data/<output_file> --num_aug 5 --alpha 0.1`
    
## 4. Refer:
1. [Synonyms](https://github.com/huyingxi/Synonyms)
2. [EDA-blog](https://towardsdatascience.com/these-are-the-easiest-data-augmentation-techniques-in-natural-language-processing-you-can-think-of-88e393fd610)
3. [EDA-Code](https://github.com/jasonwei20/eda_nlp)

Any question please open the issue or send the emails to me which can be found on my GitHub homepage.
