# import math


# def load_vocab():
#     vocab = {}
#     with open('Hackathon1/tf-idf/vocab.txt', 'r') as f:
#         vocab_terms = f.readlines()
#     with open('Hackathon1/tf-idf/idf-values.txt', 'r') as f:
#         idf_values = f.readlines()

#     for (term, idf_value) in zip(vocab_terms, idf_values):
#         vocab[term.strip()] = int(idf_value.strip())

#     return vocab


# def load_documents():
#     documents = []
#     with open('Hackathon1/tf-idf/documents.txt', 'r') as f:
#         documents = f.readlines()
#     documents = [document.strip().split() for document in documents]

#     print('Number of documents: ', len(documents))
#     print('Sample document: ', documents[0])
#     return documents


# def load_inverted_index():
#     inverted_index = {}
#     with open('Hackathon1/tf-idf/inverted-index.txt', 'r') as f:
#         inverted_index_terms = f.readlines()

#     for row_num in range(0, len(inverted_index_terms), 2):
#         term = inverted_index_terms[row_num].strip()
#         documents = inverted_index_terms[row_num+1].strip().split()
#         inverted_index[term] = documents

#     print('Size of inverted index: ', len(inverted_index))
#     return inverted_index


# vocab_idf_values = load_vocab()
# documents = load_documents()
# inverted_index = load_inverted_index()


# def get_tf_dictionary(term):
#     tf_values = {}
#     if term in inverted_index:
#         for document in inverted_index[term]:
#             if document not in tf_values:
#                 tf_values[document] = 1
#             else:
#                 tf_values[document] += 1

#     for document in tf_values:
#         tf_values[document] /= len(documents[int(document)])

#     return tf_values


# def get_idf_value(term):
#     return math.log(len(documents)/vocab_idf_values[term])


# def calculate_sorted_order_of_documents(query_terms):
#     potential_documents = {}
#     for term in query_terms:
#         if vocab_idf_values[term] == 0:
#             continue
#         tf_values_by_document = get_tf_dictionary(term)
#         idf_value = get_idf_value(term)
#         print(term, tf_values_by_document, idf_value)
#         for document in tf_values_by_document:
#             if document not in potential_documents:
#                 potential_documents[document] = tf_values_by_document[document] * idf_value
#             potential_documents[document] += tf_values_by_document[document] * idf_value

#     print(potential_documents)
#     # divite by the length of the query terms
#     for document in potential_documents:
#         potential_documents[document] /= len(query_terms)

#     potential_documents = dict(
#         sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

#     for document_index in potential_documents:
#         print('Document: ', documents[int(document_index)],
#               ' Score: ', potential_documents[document_index])


# query_string = input('Enter your query: ')
# query_terms = [term.lower() for term in query_string.strip().split()]

# print(query_terms)
# calculate_sorted_order_of_documents(query_terms)




# import math

# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

# app = Flask(__name__)


# def load_links():
#     links = {}
#     with open('Qdata/Qindex.txt', 'r') as f:
#         link = f.readlines()
#     links = [links.strip().split() for links in link]
#     return links


# def string_merger(problems):
#     stri = ""
#     for str in problems:
#         stri = stri+" "+str
#     return stri


# def load_problem():
#     problems = {}
#     with open('Qdata/index.txt', 'r') as f:
#         problems = f.readlines()
#     problems = [problem.strip().split() for problem in problems]
#     return problems


# def load_vocab():
#     vocab = {}
#     with open('tf-idf/vocab.txt', 'r') as f:
#         vocab_terms = f.readlines()
#     with open('tf-idf/idf-values.txt', 'r') as f:
#         idf_values = f.readlines()

#     for (term, idf_value) in zip(vocab_terms, idf_values):
#         vocab[term.strip()] = int(idf_value.strip())

#     return vocab


# def load_documents():
#     documents = []
#     with open('tf-idf/documents.txt', 'r') as f:
#         documents = f.readlines()
#     documents = [document.strip().split() for document in documents]

#     print('Number of documents: ', len(documents))
#     print('Sample document: ', documents[0])
#     return documents


# def load_inverted_index():
#     inverted_index = {}
#     with open('tf-idf/inverted-index.txt', 'r') as f:
#         inverted_index_terms = f.readlines()

#     for row_num in range(0, len(inverted_index_terms), 2):
#         term = inverted_index_terms[row_num].strip()
#         documents = inverted_index_terms[row_num + 1].strip().split()
#         inverted_index[term] = documents

#     print('Size of inverted index: ', len(inverted_index))
#     return inverted_index


# vocab_idf_values = load_vocab()
# documents = load_documents()
# inverted_index = load_inverted_index()
# links = load_links()
# problems = load_problem()


# def get_tf_dictionary(term):
#     tf_values = {}
#     if term in inverted_index:
#         for document in inverted_index[term]:
#             if document not in tf_values:
#                 tf_values[document] = 1
#             else:
#                 tf_values[document] += 1

#     for document in tf_values:
#         tf_values[document] /= len(documents[int(document)])

#     return tf_values


# def get_idf_value(term):
#     return math.log(len(documents) / vocab_idf_values[term])


# def calculate_sorted_order_of_documents(query_terms):
#     potential_documents = {}
#     for term in query_terms:
#         if vocab_idf_values[term] == 0:
#             continue
#         tf_values_by_document = get_tf_dictionary(term)
#         idf_value = get_idf_value(term)
#         # print(term, tf_values_by_document, idf_value)
#         for document in tf_values_by_document:
#             if document not in potential_documents:
#                 potential_documents[document] = tf_values_by_document[document] * idf_value
#             potential_documents[document] += tf_values_by_document[document] * idf_value

#     # print(potential_documents)
#     # divite by the length of the query terms
#     for document in potential_documents:
#         potential_documents[document] /= len(query_terms)

#     potential_documents = dict(
#         sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

#     # for document_index in potential_documents:
#     #print('Document: ', documents[int(document_index)], ' Score: ', potential_documents[document_index])
#     # print(string_merger(problems[int(document_index)]))
#     # print('link:',links[int(document_index)])
#     results = []
#     for document_index in potential_documents:
#         results.append({"question name": string_merger(
#             problems[int(document_index)]), "link": str(links[int(document_index)])[2:-2]})

#     return results[:10:]


# #query_string = input('Enter your query: ')
# #query_terms = [term.lower() for term in query_string.strip().split()]
# # print(query_terms)
# # print(calculate_sorted_order_of_documents(query_terms))
# app.config['SECRET_KEY'] = 'your-secret-key'


# class SearchForm(FlaskForm):
#     search = StringField('Enter your search term')
#     submit = SubmitField('Search')


# @app.route("/", methods=['GET', 'POST'])
# def home():
#     form = SearchForm()
#     results = []
#     if form.validate_on_submit():
#         query = form.search.data
#         q_terms = [term.lower() for term in query.strip().split()]
#         results = calculate_sorted_order_of_documents(q_terms)[:20:]
#     return render_template('index.html', form=form, results=results)


















































import math
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


def load_links():
    links = []
    with open('Qdata/Qindex.txt', 'r') as f:
        link = f.readlines()
        links = [line.strip().split() for line in link]
    return links


def string_merger(problems):
    return ' '.join(problems)


def load_problem():
    problems = []
    with open('Qdata/index.txt', 'r') as f:
        problems = f.readlines()
        problems = [line.strip().split() for line in problems]
    return problems


def load_vocab():
    vocab = {}
    with open('tf-idf/vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open('tf-idf/idf-values.txt', 'r') as f:
        idf_values = f.readlines()

    for term, idf_value in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())

    return vocab


def load_documents():
    documents = []
    with open('tf-idf/documents.txt', 'r') as f:
        documents = f.readlines()
        documents = [line.strip().split() for line in documents]

    print('Number of documents:', len(documents))
    print('Sample document:', documents[0])
    return documents


def load_inverted_index():
    inverted_index = {}
    with open('tf-idf/inverted-index.txt', 'r') as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0, len(inverted_index_terms), 2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num + 1].strip().split()
        inverted_index[term] = documents

    print('Size of inverted index:', len(inverted_index))
    return inverted_index


vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()
links = load_links()
problems = load_problem()


def get_tf_dictionary(term):
    tf_values = {}
    if term in inverted_index:
        for document in inverted_index[term]:
            if document not in tf_values:
                tf_values[document] = 1
            else:
                tf_values[document] += 1

    for document in tf_values:
        tf_values[document] /= len(documents[int(document)])

    return tf_values


def get_idf_value(term):
    return math.log(len(documents) / vocab_idf_values[term])


def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {}
    for term in query_terms:
        if vocab_idf_values[term] == 0:
            continue
        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)
        for document in tf_values_by_document:
            if document not in potential_documents:
                potential_documents[document] = tf_values_by_document[document] * idf_value
            potential_documents[document] += tf_values_by_document[document] * idf_value

    for document in potential_documents:
        potential_documents[document] /= len(query_terms)

    potential_documents = dict(
        sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

    results = []
    for document_index in potential_documents:
        results.append({"question_name": string_merger(problems[int(document_index)]),
                        "link": str(links[int(document_index)][0])})
    return results[:10]


class SearchForm(FlaskForm):
    search = StringField('Enter your search term', validators=[DataRequired()])
    submit = SubmitField('Search')


@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        query = form.search.data
        query_terms = [term.lower() for term in query.strip().split()]
        results = calculate_sorted_order_of_documents(query_terms)
        print(results)
    return render_template('index.html', form=form, results=results)



if __name__ == '__main__':
    app.run()
