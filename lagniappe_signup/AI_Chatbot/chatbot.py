import functions
import openai
from pinecone import Pinecone
from pinecone import ServerlessSpec

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key = functions.get_api_key('pinecone_APIkey'))

spec = ServerlessSpec(cloud = 'aws', region = 'us-east-1')
index_name = 'myindex'

# check if index already exists
if index_name not in pc.list_indexes().names():
    # if it doesn't exist, create index
    pc.create_index(
        index_name,
        dimension=1536, # dimensionality of text-embedding-ada-002
        metric='cosine',
        spec=spec
    )
# connect to index
index = pc.Index(index_name)

# add sample context data to index


# get openai api key
openai.api_key = functions.get_api_key('openAI_APIkey')

# testing with an example query
query = (
    "Which training method should I use for sentence transformers when " +
    "I only have pairs of related sentences?"
)

# first retrieve relevant items from Pinecone
query_with_contexts = functions.retrieve(query, index)
# then complete the context-infused query
response = functions.complete(query_with_contexts)

# delete index once done with it
pc.delete_index(index_name)