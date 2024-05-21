import uuid
from jinja2 import Template
from scorpiui.event_handler import register_event

class TextInput:
    def __init__(self, placeholder="", value="", height=None, width=None, background_color=None, text_color=None, border_radius=None, 
                 text_align="left", read_only=False, on_change=None, js_code=None, css_code=None):
        self.placeholder = placeholder
        self.value = value
        self.height = height
        self.width = width
        self.background_color = background_color
        self.text_color = text_color
        self.border_radius = border_radius
        self.text_align = text_align
        self.read_only = read_only
        self.on_change = on_change
        self.js_code = js_code
        self.css_code = css_code
        self.id = uuid.uuid4().hex
        register_event(self.id, self.handle_event)

    def render(self):
        js_event_handler = f"""
        document.getElementById("{self.id}").oninput = function() {{
            fetch('/_event', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{'event_id': '{self.id}', 'value': this.value}})
            }});
            {self.js_code if self.js_code else ''}
        }};
        """
        style = f"""
        style="
            {f'height: {self.height}px;' if self.height else ''}
            {f'width: {self.width}px;' if self.width else ''}
            {f'background-color: {self.background_color};' if self.background_color else ''}
            {f'color: {self.text_color};' if self.text_color else ''}
            {f'border-radius: {self.border_radius};' if self.border_radius else ''}
            text-align: {self.text_align};
            {self.css_code if self.css_code else ''}
        "
        """
        template = Template("""
        <input id="{{ id }}" class="simple-text-input" type="text" placeholder="{{ placeholder }}" value="{{ value }}" {{ style }} {{ 'readonly' if read_only else '' }}>
        <script>{{ js_event_handler }}</script>
        """)
        return template.render(
            id=self.id,
            placeholder=self.placeholder,
            value=self.value,
            style=style,
            js_event_handler=js_event_handler,
            read_only=self.read_only
        )

    def handle_event(self, event_data):
        new_value = event_data['value']
        self.value = new_value
        if self.on_change:
            self.on_change(new_value)

    def get_value(self):
        return str(self.value)
