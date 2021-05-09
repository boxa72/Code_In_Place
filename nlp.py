import nltk.sentiment
#nltk.download('vader_lexicon')

analyzer = nltk.sentiment.SentimentIntensityAnalyzer()

def main():
    user_input = input("? ")
    score = get_sentiment(user_input)
    reaction = get_reaction(score)
    print(reaction)
    print(score)
    print('')

def get_reaction(score):
    """ Param score: float between -1 and +1
        Return: An emoji as string. 
    """
    if score > 0.5:
        return "😁"
    elif score > 0:
        return "🙂"
    elif score == 0:
        return "😐"
    elif score < 0.5:
        return "😢"
    else:
        return "😞"

def get_sentiment(user_input):
    """ 
    Param user_input: any text string.
    Return: a sentiment score between -1 and +1 (float)
    """
    # 1. pass the text into the analyzer.polarity_scores function, part of the nltk package
    scores = analyzer.polarity_scores(user_input)
    # 2. extract the sentiment score. Scores is a dictionary
    sentiment_score = scores['compound']

    return sentiment_score


if __name__ == '__main__':
    main()