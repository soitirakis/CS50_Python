def main():
    prompt = input("Prompt: ")
    print(answer(prompt))

def answer(word):
    word = word.strip().lower()
    if word == '42' or word == 'forty-two' or word == 'forty two':
        return 'Yes'
    return 'No'

main()
