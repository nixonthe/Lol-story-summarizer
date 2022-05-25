import pandas as pd
import argparse
import torch
from transformers import BartTokenizer, BartForConditionalGeneration

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--champion', '-c', default='Riven')
    args.add_argument('--num_beams', '-nb', default=1, type=int)
    args.add_argument('--temperature', '-t', default=1., type=float)
    parsed_args = args.parse_args()

    df = pd.read_csv('champions_lore.csv')
    model_name = 'sshleifer/distilbart-cnn-12-6'

    text = df[df.champion == parsed_args.champion]['story'].iloc[0]

    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    inputs = tokenizer([text], return_tensors="pt")
    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=parsed_args.num_beams,
        temperature=parsed_args.temperature
    )
    tgt_text = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
    print(tgt_text[0])
