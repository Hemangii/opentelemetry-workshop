from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
import requests

# Set up OpenTelemetry
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)



# Get a tracer
tracer = trace.get_tracer(__name__)

def make_api_call(url):
    with tracer.start_as_current_span("api_call_span"):
        print(f"Making API call to {url}")
        response = requests.get(url)
        print(f"Response Status Code: {response.status_code}")
        return response.json()

def main():
    url = "https://www.hku.hk/"  # Example API endpoint
    response_data = make_api_call(url)
    print(f"Response Data: {response_data}")

if __name__ == "__main__":
    main()