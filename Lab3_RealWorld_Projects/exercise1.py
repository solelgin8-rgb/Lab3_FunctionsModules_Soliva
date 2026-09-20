# exercise1.py
import functools

# Inputs Profile
LAST_NAME = "SOLIVA"
SEED_NUM = 4
FAVORITE_ARTIST = "TAYLOR SWIFT"

execution_log = []

# Decorator to track execution pipelines
def diagnostic_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        execution_log.append(f"Executing step: {func.__name__} with parameters: {args}")
        return func(*args, **kwargs)
    return wrapper
@diagnostic_logger
def generate_readings():
    # Deterministic generation using ASCII keys
    base = (len(LAST_NAME) * SEED_NUM) + len(FAVORITE_ARTIST)
    return [base + 12.5, "BAD_DATA", base - 5.0, 199.9, base * 2.5, "TIMEOUT_ERR"]
@diagnostic_logger
def validate_reading(reading):
    try:
        val = float(reading)
        if val > 150.0:  # Mock clipping bound error check
            raise ValueError("Reading exceeds maximum sensor capacity threshold.")
        return val, "VALID"
    except (TypeError, ValueError) as err:
        return None, f"INVALID_CRITICAL ({type(err).__name__})"
@diagnostic_logger
def classify_reading(val):
    if val < 40.0:
        return "Low (Sub-optimal)"
    elif val <= 100.0:
        return "Nominal (Safe Execution)"
    else:
        return "High Operational Stress"
# Main Routine
if __name__ == "__main__":
    raw_stream = generate_readings()
    valid_data = []
    invalid_count = 0
    classifications = []
    for item in raw_stream:
        clean_val, status = validate_reading(item)
        if status == "VALID":
            valid_data.append(clean_val)
            classifications.append(classify_reading(clean_val))
        else:
            invalid_count += 1
    print("=== ASSESSMENT DATA (EXERCISE 1) ===")
    print(f"Generated Equipment Data: {raw_stream}")
    print(f"Validation Results: {len(valid_data)} Passed | {invalid_count} Failed")
    print(f"Diagnostic Results (Classifications): {classifications}")
    print("\nExecution Log:")
    for line in execution_log:
        print(f"  [LOG] {line}")
    print(f"\nFinal Output: Processing terminated. Core Mean Temp: {sum(valid_data)/len(valid_data):.2f}°C")