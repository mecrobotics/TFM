import streamlit as st
import pandas as pd
import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from decouple import config
from langchain.memory import ConversationBufferWindowMemory
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as Pinecone_vectorstore
from classes.chatbot import Chatbot
from classes.intent import Intent
from classes.knowledgebase import Knowledgebase
from classes.router import Router
from classes.view import View
import time
import os

agente = Chatbot(os, ChatOpenAI, ConversationBufferWindowMemory)

faqs = Knowledgebase(os, Pinecone, time, OpenAIEmbeddings)
faqs.create_vectorstore(Pinecone_vectorstore)

intention = Intent(pd)
enrutado = Router(intention)

vista = View(st)
vista.check_messages()
vista.display_messages()
vista.set_user_prompt()
vista.display_user_prompt()
vista.display_bot_prompt(intention, openai, faqs, agente, enrutado)
