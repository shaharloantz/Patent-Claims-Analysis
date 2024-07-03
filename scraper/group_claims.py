from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation


def group_claims_by_lda(all_claims, num_topics=3, no_top_words=1):

    # Convert claims to TF-IDF features
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(all_claims)

    # Apply LDA
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(X)

    # Get the top words for each topic
    tf_feature_names = vectorizer.get_feature_names_out()
    topic_words = display_topics(lda, tf_feature_names, no_top_words)

    # Group claims by topics
    topics = lda.transform(X)
    grouped_claims = [[] for _ in range(num_topics)]
    for i, topic_prob in enumerate(topics):
        topic = topic_prob.argmax()
        grouped_claims[topic].append(all_claims[i])

    return grouped_claims, topic_words


def display_topics(model, feature_names, no_top_words):
    topic_words = []
    for topic_idx, topic in enumerate(model.components_):
        top_words = [
            feature_names[i] for i in topic.argsort()[: -no_top_words - 1 : -1]
        ]
        topic_words.append(" ".join(top_words))
    return topic_words
