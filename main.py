from llm import get_llm
from prompts import basic_prompt

def run():
    llm = get_llm()

    while True:
        question = input("\nAsk something (or type 'exit'): ")
        if question.lower() == "exit":
            break

        chain = basic_prompt | llm
        response = chain.invoke({"question": question})

        print("\n🤖 Response:")
        print(response.content)

if __name__ == "__main__":
    run()
