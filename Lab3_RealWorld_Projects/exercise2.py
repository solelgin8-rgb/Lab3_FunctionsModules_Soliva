# exercise2.py

LAST_NAME = "SOLIVA"
SEED_NUM = 4
FAVORITE_ARTIST = "TAYLOR SWIFT"

call_counter = 0
trace_path = []
log_history = []

def recursive_fault_trace(fault_code, depth=1):
    global call_counter
    call_counter += 1
    
    trace_path.append(fault_code)
    log_history.append(f"Level {depth}: Analyzing fault node ID [{fault_code}]")
    # Predefined recursive base case termination check
    if fault_code <= 10:
        log_history.append(f"Success: Base condition discovered at level {depth}.")
        return fault_code
    # Recursive division step
    next_node = fault_code // 2
    return recursive_fault_trace(next_node, depth + 1)

if __name__ == "__main__":
    # Unique base calculation code string assignment
    initial_fault_code = (len(LAST_NAME) * 10) + (len(FAVORITE_ARTIST) * SEED_NUM)
    final_result = recursive_fault_trace(initial_fault_code)
    
    print("=== ASSESSMENT DATA (EXERCISE 2) ===")
    print(f"Generated Fault Data (Initial Code): {initial_fault_code}")
    print(f"Recursive Trace Sequence: {trace_path}")
    print(f"Number of Recursive Calls: {call_counter}")
    print("\nExecution Log:")
    for step in log_history:
        print(f"  {step}")
    print(f"\nFinal Output: Trace ended. Root fault component flagged at reference index: {final_result}")