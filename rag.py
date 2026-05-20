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

def build_prompt(question, retrieved_doc):
    return f""" 
Use only the context below to answer the question. If you don't know the answer, say you don't know.

context:
{retrieved_doc['content']}

question:
{question}

answer:
"""

question = "What are some popular food items at the restaurant?"

retrieved_doc = simple_retrieve(question, documents)
prompt = build_prompt(question, retrieved_doc)

print("Retrieved Document:", retrieved_doc['title'])
print(prompt)