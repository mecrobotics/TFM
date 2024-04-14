class View:

    user_prompt=""
    stream = ""

    def __init__(self, st):
        self.stream = st

        self.stream.set_page_config(
            page_title="Agente conversacional",
            page_icon="🤖",
            layout="wide"
        )

        self.stream.title("Agente conversacional")

    def check_messages(self):
        # check for messages in session and create if not exists
        if "messages" not in self.stream.session_state.keys():
            self.stream.session_state.messages = [
                {"role": "assistant", "content": "Hola, soy tu agente de banca"}
            ]

    def display_messages(self):
        # Display all messages
        for message in self.stream.session_state.messages:
            with self.stream.chat_message(message["role"]):
                self.stream.markdown(message["content"], unsafe_allow_html=True)

    def display_user_prompt(self):
        if self.user_prompt is not None:
            self.stream.session_state.messages.append({"role": "user", "content": self.user_prompt})
            with self.stream.chat_message("user"):
                self.stream.write(self.user_prompt)
    
    def set_user_prompt(self):
        self.user_prompt = self.stream.chat_input(placeholder="Escribe aqui tu mensaje:")

    def display_bot_prompt(self, intention, openai, faqs, agente, enrutado):
        if self.stream.session_state.messages[-1]["role"] != "assistant":
            with self.stream.chat_message("assistant"):
                with self.stream.spinner("Cargando..."):
                    intencion = intention.clasificar_intencion(self.user_prompt, openai)
                    # Si la intención es 'ninguna', procesamos la consulta con RAG
                    if intencion == 'ninguna':
                        # Primero, obtenemos el contexto aumentado basado en la consulta del usuario
                        augmented_prompt = faqs.augment_prompt(self.user_prompt)
                        
                        # Luego, en lugar de pasar simplemente la consulta del usuario, pasamos el prompt aumentado
                        ai_response_plain = agente.llm.predict(text=augmented_prompt)
                        self.stream.markdown(ai_response_plain, unsafe_allow_html=True)
                    else:
                        # Si la intención es reconocida y no es 'ninguna', usamos la intención directamente como respuesta
                        ai_response = enrutado.smart_routing(intencion)
                        self.stream.markdown(ai_response, unsafe_allow_html=True) 
                    
            new_ai_message = {"role": "assistant", "content": ai_response_plain if intencion == 'ninguna' else ai_response}
            self.stream.session_state.messages.append(new_ai_message)