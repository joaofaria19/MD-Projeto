import json
import re
import pdb

model = 'openai/GPT4'

def clean_completion(prompt, completion):
    terminating_chars = ['.','!','?','\n',':']
    
    completion = completion.replace('<|begin_of_text|>','')
    completion = completion.replace('<|assistant|>','')
    completion = completion.replace('<|end_of_text|>','')
    completion = completion.replace('<|end|>','')
    
    prompt_len = len(prompt)
    
    if prompt[-1] in terminating_chars:
        if prompt in completion:
            while prompt in completion:
                index = completion.find(prompt)
                completion = completion.replace(prompt, '', 1)  # Replace only once
                completion = completion[:index] + completion[index:].lstrip('\n.!?: ')
        else:
            completion = completion[prompt_len:len(completion)]   
            index = None
            
            for char in completion:
                if char in terminating_chars:
                    index = completion.index(char)
                    break
            if index:
                completion = completion[index:len(completion)]
                completion = completion.lstrip('\n.!?: ')
    else:
        completion = completion[prompt_len:len(completion)]   
        index = None
        
        for char in completion:
            if char in terminating_chars:
                index = completion.index(char)
                break
        if index:
            completion = completion[index:len(completion)]
            completion = completion.lstrip('\n.!?: ')
        while prompt in completion:
            index = completion.find(prompt)
            completion = completion.replace(prompt, '', 1)  # Replace only once
            completion = completion[:index] + completion[index:].lstrip('\n.!?: ')
                
    return completion.lstrip('\n.!?: ')

def is_code_block(line):
    """Determine if the line contains a code block."""
    return "```" in line

def divide_and_check(text):
    # Split the text into sentences using regular expressions
    text_parsed = False
    result_text = text

    while not text_parsed:
        sentences = re.split(r'(?<=[.!?])\s+', result_text.strip())
        
        
        if re.match(r'[^.!?]+[.!?]$', sentences[-1]):
            last_sentence = sentences[-1]
            parentheses_count = last_sentence.count("(") - last_sentence.count(")")
            pattern = r"(?<!\w)\'"  # Raw string prefix (optional)
            single_quote_count = len(re.findall(pattern, last_sentence))
            double_quote_count = last_sentence.count('"')
            square_bracket_count = last_sentence.count("[') - last_sentence.count(']")
            
            
            if(len(last_sentence) > 1):
                if parentheses_count > 0 or square_bracket_count > 0:
                    sentences = sentences[:-1]
                elif double_quote_count % 2 != 0:
                    sentences = sentences[:-1]
                elif single_quote_count % 2 != 0:
                    sentences = sentences[:-1]
                elif last_sentence[-2].isdigit():
                    sentences = sentences[:-1]
                else:
                    text_parsed = True    
            else:
                sentences = sentences[:-1]
        else:
            sentences = sentences[:-1]
            
        if len(sentences) == 0:
            text_parsed = True
        result_text = ' '.join(sentences)
    
    return result_text

def split_sentences(text):
    """Split text into sentences while handling code blocks separately."""
    valid_flag = True
    
    reason = 'Valid'
    if is_code_block(text):
        valid_flag = False
        reason = 'Code'
    else:
        text = divide_and_check(text[:512])
        if len(text) < 80 or len(text) > 512:
            reason = f'{len(text)} chars'
            valid_flag = False

    return text,valid_flag, reason

def clean_json_data(data):
    valid_data = []
    invalid_data = []
    i = 0
    for entry in data:
        prompt = entry.get("Prompt", "")
        completion = entry.get("Completion", "")
        if len(entry['Completion']) < 80:
            entry['Reason'] = f"{len(entry['Completion'])} chars"
            invalid_data.append(entry)
            print(i, False, f"{len(entry['Completion'])} chars")
        else:
            if model != 'openai/GPT4':
                entry['Completion'] = clean_completion(prompt, completion)
            text,valid,reason = split_sentences(entry['Completion'])
            if valid:
                entry['Completion'] = text
                valid_data.append(entry)
            else:
                entry['Reason'] = reason
                invalid_data.append(entry)
            print(i,valid, reason)
        i+=1
    return valid_data, invalid_data

if __name__ == "__main__":
    with open(model +".json", 'r') as json_file:
        data = json.load(json_file)

    valid_data, invalid_data = clean_json_data(data['answers'])

    filename = model + "_valid.json"

    # Dump the dictionary into the JSON file
    with open(filename, 'w') as json_file:
        json.dump(valid_data, json_file, indent=2, ensure_ascii=False)
        
    filename = model + "_invalid.json"

    # Dump the dictionary into the JSON file
    with open(filename, 'w') as json_file:
        json.dump(invalid_data, json_file, indent=2, ensure_ascii=False)
        
    print(len(valid_data),len(invalid_data))