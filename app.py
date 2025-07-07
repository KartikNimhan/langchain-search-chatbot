import streamlit as st 
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

# Title and description
st.title("🔎 Langchain - Chat with Search")
st.markdown(
    "This chatbot uses Arxiv, Wikipedia, and DuckDuckGo to answer your questions.\n\n"
    "You'll see the agent's reasoning via the Langchain Streamlit callback handler."
)

# Sidebar for API key input
st.sidebar.title("🔐 Settings")
api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")

# Session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle user input
if prompt := st.chat_input(placeholder="What is Machine Learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize Groq LLM
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama3-8b-8192",  # You can also try llama-3-70b if needed
        streaming=True
    )

    # Define tools
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

    wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
    wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

    search = DuckDuckGoSearchRun(name="Search")

    tools = [search, arxiv, wiki]

    # Initialize agent
    search_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True
    )

    # Run agent and display response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
        response = search_agent.run(prompt, callbacks=[st_cb])
        st.write(response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
