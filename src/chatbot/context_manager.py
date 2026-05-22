from prompts.system_prompt import SYSTEM_PROMPT


class ContextManager:

    def build_context(self, user_input, category, history):

        return f"""
        {SYSTEM_PROMPT}

        Histórico:
        {history}

        Categoria:
        {category}

        Pergunta:
        {user_input}
        """
