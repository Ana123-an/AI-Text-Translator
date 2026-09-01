import requests
OLLAMA_URL="http://localhost:11434/api/generate"

MODEL="qwen"
#translate text

def translate(text,target):
    prompt=f"""
Translate the text into {target}.
Text:
{text}
"""
    response=requests.post(
        OLLAMA_URL,
        json={
            "model":MODEL,
            "prompt":prompt,
            "stream":False
        }

    )
    return response.json()["response"]

def main():
    while True:
        text=input("Enter the text: ")
        if text.lower()=="exit":
            break
        target=input("Translate to: ")
        result=translate(text,target)
        print(result)

if __name__=="__main__":
    main()
    
    