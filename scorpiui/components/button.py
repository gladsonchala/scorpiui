import uuid
from jinja2 import Template
from scorpiui.event_handler import register_event

class Button:
    def __init__(self, label, height, width, background_color, text_color, border_radius, onclick, js_code=None, css_code=None):
        self.label = label
        self.height = height
        self.width = width
        self.background_color = background_color
        self.text_color = text_color
        self.border_radius = border_radius
        self.onclick = onclick
        self.js_code = js_code
        self.css_code = css_code
        self.id = uuid.uuid4().hex
        register_event(self.id, self.handle_event)

    def render(self):
        js_event_handler = f"""
        document.getElementById("{self.id}").onclick = function() {{
            fetch('/_event', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{'event_id': '{self.id}'}})
            }});
            {self.js_code if self.js_code else ''}
        }};
        """
        style = f"""
        style="
            height: {self.height}px; 
            width: {self.width}px; 
            background-color: {self.background_color};
            color: {self.text_color}; 
            border-radius: {self.border_radius};
            {self.css_code if self.css_code else ''}
        "
        """
        template = Template("""
        <button id="{{ id }}" class="simple-button" {{ style }}>
          {{ label }}
        </button>
        <script>{{ js_event_handler }}</script>
        """)
        return template.render(
            id=self.id,
            label=self.label,
            style=style,
            js_event_handler=js_event_handler
        )

    def handle_event(self, event_data):
        self.onclick()
