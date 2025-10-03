from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Set up tracer
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

app = Flask(__name__)
tracer = trace.get_tracer(__name__)

@app.route("/")
def hello():
    with tracer.start_as_current_span("hello-span"):
        return "Hello from OpenTelemetry Workshop!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
