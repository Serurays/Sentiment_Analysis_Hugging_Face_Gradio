from transformers import pipeline
import gradio as gr

sentiment = pipeline("sentiment-analysis")

def get_sentiment(input_text):
  return sentiment(input_text)

iface = gr.Interface(fn=get_sentiment, inputs="text", outputs=["text"], title="Sentiment Analysis", theme=gr.themes.Monochrome())\

iface.launch(inline=False)
