# telemetry_core.py
import functools

def pipeline_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [PIPELINE TRACE] Activating hardware sequence: '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

@pipeline_monitor
def telemetry_generator(last_name, seed_num, artist):
    """Produces telemetry stream measurements lazily via generator yield loops."""
    base_calc = (len(last_name) + len(artist)) * seed_num
    raw_mock_signals = [base_calc, base_calc + 15, "CORRUPT_SIGNAL", base_calc - 25, 500.5, base_calc + 10]
    
    for signal in raw_mock_signals:
        yield signal

def recursive_anomaly_analysis(signal_value, count=1):
    """Traces abnormal conditions downwards recursively to a safe baseline state."""
    if signal_value <= 100.0:
        return signal_value, count
    return recursive_anomaly_analysis(signal_value - 50.0, count + 1)