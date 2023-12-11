from transformers import T5ForConditionalGeneration, T5Tokenizer

def init_model():
    # initialize the model and tokenizer
    global tokenizer
    global model

    tokenizer = T5Tokenizer.from_pretrained("/application/flanbot/flan-t5-base-sciq")
    model = T5ForConditionalGeneration.from_pretrained("/application/flanbot/flan-t5-base-sciq")
    
    return model

def generate(model, text):
    # encode the input
    input_tokens = tokenizer(text, return_tensors="pt").input_ids
    # generate output
    output_tokens = model.generate(input_tokens)
    # decode the output tokens
    response = tokenizer.decode(output_tokens[0])
    
    # remove the special tokens from the output and return
    return response.replace("<pad>", "").replace("</s>", "").replace("<unk>", "").strip()