from scorpiui.app import app, run_app
from scorpiui.components.button import Button
from scorpiui.components.text_input import TextInput
from flask import render_template

# Store input values
input_values = {}

def on_text_change(value):
    input_values['text_input'] = value
    print("Text input changed:", value)

# Create a TextInput instance
my_text_input = TextInput(
    placeholder="Enter text here...",
    height=30,
    width=200,
    background_color="#ffffff",
    text_color="#000000",
    border_radius="5px",
    text_align="left",
    read_only=False,
    on_change=on_text_change,
    js_code='console.log("Input changed");',
    css_code='border: 1px solid #ccc; padding: 5px;'
)

def on_button_click():
    text = my_text_input.get_value()
    print("Button clicked: " + text)

def on_button2_click():
    print("Button 2 clicked")

# Create button instances with desired properties, JS code, and CSS code
my_button = Button(
    label="Click Me",
    height=50,
    width=150,
    background_color="#3498db",
    text_color = "#ffffff",
    border_radius="12px",
    onclick=on_button_click,
    js_code='alert("Button successfully clicked!");', 
    css_code='border: 5px solid red; color: yellow; text-align: center; font-size: 16px; cursor: pointer;'
)

my_button2 = Button(
    label="Button 2",
    height=50,
    width=150,
    background_color="#3498db",
    text_color = "#ffffff",
    border_radius="12px",
    onclick=on_button2_click,
    js_code='alert("Button 2 successfully clicked!");', 
    css_code='border: 5px solid red;'
)

@app.route('/')
def home():
    button_html = my_button.render()
    button_html2 = my_button2.render()
    input_html = my_text_input.render()

    HTMLcontent = button_html + button_html2 + input_html
    return render_template('base.html', content=HTMLcontent, title="ScorpiUI Test")

if __name__ == '__main__':
    run_app()
