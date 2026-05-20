documents = [{"title": "Extensions Policy",
              "content": "This policy outlines the guidelines for using extensions in our software."
            },
            {"title": "Food Items",
             "content": "Burgers, Fries, and Shakes are popular food items at our restaurant."
            },
            {"title": "Emojis",
             "content": "💖, 👩🏻‍💻, 📱, 🔥"
            }]

def simple_retrieve(question, documents):
    question_words = set(question.lower().split())

    scored_docs = []
    for doc in documents:
        content_words = set(doc['content'].lower().split())
        score = len(question_words.intersection(content_words))
        scored_docs.append((score, doc))
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    return scored_docs[0][1]



def generate_answer(question, retrieved_doc):
    content = retrieved_doc['content']
    question_words = set(question.lower().split())
    content_words = set(content.lower().split())
    score = len(question_words.intersection(content_words))
    if score == 0:
        return "I don't know."
    return content

question = "What is the policy for using extensions?"
retrieved_doc = simple_retrieve(question, documents)
answer = generate_answer(question, retrieved_doc)
print("Question:", question)
print("Retrieved Document:", retrieved_doc['title'])
print("Answer:", answer)