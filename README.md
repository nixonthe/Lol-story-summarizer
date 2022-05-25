
# Lol story summarizer

Here you can find parser which I used to parse text data from the original game site and a script.




# Steps to run project

## Step 1:

Clone the project

```bash
  git clone https://github.com/nixonthe/Lol-story-summarizer.git
```

## Step 2:

Install requirements

```bash
  pip install -r requirements.txt
```

## Step 3:

You can download data with my parser. If you want to use already downloaded data then move to step 5. 

## Step 4:

To download data run parser.

```bash
  python scraping.py
```

## Step 5:

To run text summarizer execute this command

```bash
  python summarizer.py
```

Also you can run inference with your own params. With parameter "-c" you select champion's name. Here is the [description](https://huggingface.co/docs/transformers/v4.19.2/en/main_classes/text_generation#transformers.generation_utils.GenerationMixin.generate).

```bash
  python summarizer.py -c Kassadin -nb 2 -t 0.5
```

Enjoy!


## Feedback

If you have any feedback, please reach out to me at glazunovnik@gmail.com

