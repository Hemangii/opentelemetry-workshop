from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Set up OpenTelemetry
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

# Get a tracer
tracer = trace.get_tracer(__name__)

def multiply(x, y):
    with tracer.start_as_current_span("multiply_span"):
        print(f"Multiplying {x} and {y}")
        result = x * y
        return result

def main():
    a = 3
    b = 5
    result = multiply(a, b)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()