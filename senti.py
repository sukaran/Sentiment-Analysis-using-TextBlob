from textblob import TextBlob
sent=input() 
analysis=TextBlob(sent)
if analysis.sentiment.polarity>0:
    print('posiive')
elif analysis.sentiment.polarity==0:
    print('neutral')
else:
    print('negative')

