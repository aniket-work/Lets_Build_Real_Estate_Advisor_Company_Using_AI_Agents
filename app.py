from data_loader import load_house_data
from criteria_extractor import extract_criteria_via_llm
from house_filter import filter_house
from response_generator import generate_response
from agent import create_agent
from llama_index.core.tools import FunctionTool

def main():
    house_data = load_house_data()

    tools = [
        FunctionTool.from_defaults(fn=extract_criteria_via_llm),
        FunctionTool.from_defaults(fn=lambda criteria: filter_house(criteria, house_data)),
        FunctionTool.from_defaults(fn=generate_response)
    ]

    agent = create_agent(tools)

    try:
        print("\nSending house selection query...")
        query = (
            "I am looking for a house of overall score of 50 and I can only afford up to $68,000 a year in of payout. "
            "I would prefer a relative new  house in California within 500 miles of Berkeley. "
            "Where are my top ten choices for houses I am very likely to get in to?"
        )
        response = agent.chat(query)
        print(f"House selection response: {response}")

    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
        if "Reached max iterations" in str(ve):
            print("The agent reached the maximum number of iterations without completing the task.")
            print("You may need to simplify the query or further increase the max_iterations.")
        import traceback
        traceback.print_exc()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()