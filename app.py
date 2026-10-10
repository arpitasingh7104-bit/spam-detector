import gradio as gr, joblib

model = joblib.load("model.pkl")

def check(text):
    if not text.strip():
        return "Please type a message."
    label = model.predict([text])[0]
    conf = model.predict_proba([text])[0].max() * 100
    if label == "spam":
        return f"🚫 SPAM ({conf:.1f}% confident)"
    return f"✅ NOT SPAM ({conf:.1f}% confident)"

gr.Interface(
    fn=check,
    inputs=gr.Textbox(lines=4, label="Type or paste a message"),
    outputs=gr.Textbox(label="Result"),
    title="Spam Message Detector",
    description="Checks whether a text message is spam or not.",
).launch()