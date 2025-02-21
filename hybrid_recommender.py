import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

books = pd.read_csv('FinalData.csv')

ratings = pd.read_csv('FinalRatings.csv')

# merging the books and ratings dataset
book_ratings = pd.merge(ratings, books, on='book_id')

def popularity_recommendations():
    # grouping the books by title and count the number of ratings for each
    book_popularity = book_ratings.groupby('title')['rating'].count().reset_index()

    # sorting the books by popularity in descending order
    popular_books = book_popularity.sort_values('rating', ascending=False)

    # returning the top 10 most popular books
    return popular_books['title'].head(10).tolist()



                                       #For Collaboratuve Filtering
# creating a pivot table with user IDs as rows and book titles as columns
user_book_ratings = book_ratings.pivot_table(index='user_id', columns='title', values='rating').fillna(0)

# calculate the cosine similarity between each book based on user ratings
book_similarity = cosine_similarity(user_book_ratings.T) #ekhane transpose korsi karon column borabor ek user er shob rating niye ashchi


                                          #For Content Based Filtering
# initializing the CountVectorizer
cv = CountVectorizer(stop_words='english')

# create a matrix of word counts for each book description
book_matrix = cv.fit_transform(books['Genres'])

# calculate the cosine similarity between each book based on their descriptions
book_content_similarity = cosine_similarity(book_matrix)


                                     #Now Its Time For Hybrid Recommendation


def hybrid_recommendations(title):
    # get the index of the book
    idx = books[books['title'] == title].index[0]

    # getting the similarity scores from collab filtering
    collab_scores = list(enumerate(book_similarity[idx]))

    # get the similarity scores from content based filtering
    content_scores = list(enumerate(book_content_similarity[idx]))

    # combine the scores using a weighted average
    hybrid_scores = [(i, (collab_scores[i][1] + content_scores[i][1])/2) for i in range(len(collab_scores))]

    # sort the scores in descending order
    hybrid_scores = sorted(hybrid_scores, key=lambda x: x[1], reverse=True)

    # get the top 10 book recommendations
    top_books = [books.iloc[i[0]]['title'] for i in hybrid_scores[1:11]]

    return top_books


