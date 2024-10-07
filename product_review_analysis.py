'''
1. Product Review Analysis
Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords 
such as "good", "excellent", "bad", "poor", and "average". We want you to 
capitalize those keywords then print out each review. 
Print out each review with the keywords in uppercase so they stand out.

'''


print("\n************* Task 1: Keyword Highlighter *******************\n")

    
reviews = ["This product is really good. I'm impressed with its quality.", 
           "The performance of this product is excellent. Highly recommended!",
           "I had a bad experience with this product. It didn't meet my expectations.",
           "Poor quality product. Wouldn't recommend it to anyone.",
           "The product was average. Nothing extraordinary about it."]

keywords = ["good", "excellent", "bad", "poor", "average", "Good", "Excellent", "Bad", "Poor", "Average"]



for review in reviews:
    for keyword in keywords:
        
        review = review.replace(keyword, keyword.upper())

    print(review)

  # This code couldn't get the word Poor because it has a capitalized P.
  # So I had to add the capitalized words on the list. I know there might be some other ways to do this.

'''
  Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  
The function should return the total count of positive and negative words.
'''
print("\n************* Task 2: Sentiment Tally *******************\n")
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_count = 0
negative_count = 0

for review in reviews:
    
    lowercase_review = review.lower() #make lower case
    words = lowercase_review.split()  # Split into words

    # Check each word in the review
    for word in words:
       
        word = word.strip(".,!?")
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

print(f"Positive Words: {positive_count}")
print(f"Negative Words: {negative_count}")

''' Task 3 Review Summary
Implement a script that takes the first 30 characters of a review 
and appends "…" to create a summary. Ensure that the summary does not cut off 
in the middle of a word.

Example: "This product is really good. I'm...",
'''
print("\n************* Task 3: Review Summary *******************\n")


def summary_thirty(review, char_limit = 30):  # set the limit to 30 characters, tested for 40 and other numbers
    if len(review) <= char_limit: 
        return review
    
    first_thirty = review[:char_limit]
    if first_thirty[-1].isalnum(): # if the last character is alphanumeric
        space = first_thirty.rfind(" ") # reverse find the last space
        if space != -1:  # cut off
            first_thirty = first_thirty[:space]

    return first_thirty + "..."


for review in reviews:
    summary = summary_thirty(review)

    print(summary)    

  
    
