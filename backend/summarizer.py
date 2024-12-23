from transformers import BartTokenizer, BartForConditionalGeneration

def summarization(text: str) -> str:
    model_name = 'sshleifer/distilbart-cnn-12-6'

    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    inputs = tokenizer([text], return_tensors="pt")
    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=1.,
        temperature=1.
    )
    tgt_text = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return tgt_text[0]
