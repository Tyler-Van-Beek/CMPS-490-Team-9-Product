import time
import openai

def get_api_key(filename):
    """ Given a filename, return the API key in that file """
    try:
        with open(filename, 'r') as f:
            # File should contain a single line, with the API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

LIMIT = 3750
def retrieve(query, index):
    """ Retrieves relevant data from pinecone database based on the query """
    res = openai.Embedding.create(
        input = [query],
        engine = "text-embedding-ada-002"
    )

    # retrieve from Pinecone
    xq = res['data'][0]['embedding']

    # get relevant contexts
    contexts = []
    time_waited = 0
    while (len(contexts) < 3 and time_waited < 60 * 12):
        res = index.query(vector=xq, top_k=3, include_metadata=True)
        contexts = contexts + [
            x['metadata']['text'] for x in res['matches']
        ]
        print(f"Retrieved {len(contexts)} contexts, sleeping for 15 seconds...")
        time.sleep(15)
        time_waited += 15

    if time_waited >= 60 * 12:
        print("Timed out waiting for contexts to be retrieved.")
        contexts = ["No contexts retrieved. Try to answer the question yourself!"]

    # build our prompt with the retrieved contexts included
    prompt_start = (
        "Answer the question based on the context below.\n\n"+
        "Context:\n"
    )
    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:"
    )
    # append contexts until hitting limit
    for i in range(1, len(contexts)):
        if len("\n\n---\n\n".join(contexts[:i])) >= LIMIT:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts[:i-1]) +
                prompt_end
            )
            break
        elif i == len(contexts)-1:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts) +
                prompt_end
            )
    return prompt


def complete(prompt):
    """ Returns a response to the prompt built by retrieve() function """
    # instructions
    sys_prompt = "You are a helpful assistant that always answers questions."
    # query text-davinci-003
    res = openai.ChatCompletion.create(
        model='gpt-4o-mini-2024-07-18',
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return res['choices'][0]['message']['content'].strip()