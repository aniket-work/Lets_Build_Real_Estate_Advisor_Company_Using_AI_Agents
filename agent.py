from llama_index.core.prompts import PromptTemplate
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from constants import OLLAMA_CONFIG, AGENT_CONFIG


class CustomReActAgent(ReActAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extracted_criteria = None

    def _get_response(self, *args, **kwargs):
        max_iterations = AGENT_CONFIG['max_iterations']
        for i in range(max_iterations):
            try:
                return super()._get_response(*args, **kwargs)
            except ValueError as e:
                if "Reached max iterations" in str(e) and i < max_iterations - 1:
                    print(f"Iteration {i + 1} reached, continuing...")
                    continue
                raise e

    def _process_actions(self, actions):
        for action in actions:
            if action.tool == "extract_criteria_via_llm":
                action.tool_input = action.tool_input['prompt'] if isinstance(action.tool_input, dict) and 'prompt' in action.tool_input else action.tool_input
            elif action.tool == "filter_houses" and self.extracted_criteria:
                action.tool_input = self.extracted_criteria

            result = self._execute_action(action)
            if action.tool == "extract_criteria_via_llm":
                self.extracted_criteria = result

        return actions

    def _execute_action(self, action):
        tool = self.tool_mapping[action.tool]
        try:
            observation = tool(**action.tool_input) if isinstance(action.tool_input, dict) else tool(action.tool_input)
            return observation
        except Exception as e:
            return f"Error: {str(e)}"

def create_agent(tools):
    agent_prompt = PromptTemplate(
        "You are an AI assistant specializing in real estate advisory services. "
        "Answer the following question related to property selection:\n"
        "Human: {query_str}\n"
        "Assistant: Let's approach this step-by-step:\n"
        "1) First, I'll identify the key criteria from your query, such as location, budget, property type, and specific requirements.\n"
        "2) Then, I'll use these criteria to filter through available real estate listings.\n"
        "3) Finally, I'll provide you with a curated list of top property options that match your preferences.\n"
        "Let's begin!\n"
        "{agent_scratchpad}"
    )

    llm = Ollama(model=OLLAMA_CONFIG['model'], request_timeout=OLLAMA_CONFIG['request_timeout'])

    return CustomReActAgent.from_tools(
        tools,
        llm=llm,
        verbose=AGENT_CONFIG['verbose'],
        agent_prompt=agent_prompt,
        max_iterations=AGENT_CONFIG['max_iterations']
    )