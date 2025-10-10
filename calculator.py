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

def divide(x, y):
    with tracer.start_as_current_span("divide_span"):
        print(f"Dividing {x} by {y}")
        result = x / y
        return result

def main():
    a = 6
    b = 3

    division_result = divide(a, b)
    print(f"Division Result: {division_result}")

    # Test division by zero
    division_by_zero_result = divide(a, 0)
    print(f"Division by Zero Result: {division_by_zero_result}")

if __name__ == "__main__":
    main()