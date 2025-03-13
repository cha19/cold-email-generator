import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name='extraction_database')

collection.add(
    documents=[
        "this is about chroma db",
        "This is about Gen AI"
    ],
    ids=['id1','id2']

)


all_docs = collection.get()
print(all_docs)


