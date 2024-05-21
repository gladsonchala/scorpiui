# ScorpiUI

`ScorpiUI` is a Python-based UI library designed to simplify frontend development for Python backend developers. With ScorpiUI, you can create dynamic and interactive web applications using Python alone, reducing the need for traditional frontend technologies such as HTML, CSS, and JavaScript.

## Features

- **Pythonic Development**: ScorpiUI allows you to define UI components, handle events, and execute JavaScript code entirely in Python, making frontend development more accessible to Python developers.
  
- **Customizable Components**: ScorpiUI provides a range of customizable UI components, including buttons, forms, modals, and more, allowing you to create rich user interfaces tailored to your application's needs.
  
- **Event Handling**: Easily handle user interactions and events with Python functions, making it straightforward to implement dynamic behavior in your web applications.
  
- **CSS Styling**: Customize the appearance of your UI components using custom CSS styles directly within your Python code, ensuring consistent and visually appealing designs.
  
- **JavaScript Execution**: Execute client-side JavaScript code in response to user actions, enabling real-time interactivity and enhancing the user experience.

<!--
## Installation

You can install ScorpiUI using pip:

```bash
pip install scorpiui
```
-->

## Getting Started

Here's a simple example of how to create a button with ScorpiUI:

```python
from scorpiui.app import app, run_app, register_event
from scorpiui.components.button import Button
from flask import render_template

def on_button_click():
    print("Button clicked")

# Create a button instance with the desired properties, JS code, and CSS code
my_button = Button(
    label="Click Me",
    height=50,
    width=150,
    color="#3498db",
    border_radius="12px",
    onclick=on_button_click,
    js_code='alert("Button successfully clicked!");',  # Custom JS code to execute on click
    css_code='border: 2px solid red;'  # Custom CSS code to style the button
)

# Register the event handler
register_event(my_button.id, my_button.handle_event)

@app.route('/')
def home():
    button_html = my_button.render()
    return render_template('base.html', content=button_html)

if __name__ == '__main__':
    run_app()
```

<!--
## Documentation

For detailed usage instructions and documentation, please refer to the [ScorpiUI Documentation](https://github.com/gladsonchala/scorpiui).
-->

## Contributing

Contributions are welcome! If you have any ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/gladsonchala/scorpiui).

## License

ScorpiUI is licensed under the [MIT License](https://opensource.org/licenses/MIT).
