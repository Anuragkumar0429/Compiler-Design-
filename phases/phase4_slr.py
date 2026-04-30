"""
PHASE 4: LR Parsing Table Generator (SLR/LALR Simulator)
DFA-based SLR simulator for validating integer literal tokens
"""

# States
START = "START"
DEC = "DEC"
HEX_PREFIX = "HEX_PREFIX"
HEX = "HEX"
ACCEPT = "ACCEPT"
ERROR = "ERROR"


def is_hex(ch):
    """Check if character is a hex digit"""
    return ch in "0123456789abcdefABCDEF"


def transition(state, ch):
    """Get next state based on current state and character"""
    if state == START:
        if ch.isdigit():
            return DEC
        return ERROR
    
    if state == DEC:
        if ch == "$":
            return ACCEPT
        if ch.isdigit():
            return DEC
        return ERROR
    
    if state == HEX_PREFIX:
        if is_hex(ch):
            return HEX
        return ERROR
    
    if state == HEX:
        if ch == "$":
            return ACCEPT
        if is_hex(ch):
            return HEX
        return ERROR
    
    return ERROR


def slr_parse(token):
    """
    Parse a token using SLR parser
    Returns (is_valid, final_state, trace)
    """
    trace = []
    
    # Check for hex prefix first
    if token.lower().startswith("0x"):
        state = HEX_PREFIX
        rest = token[2:]
        trace.append(f"Detected hex prefix: {token[:2]}")
    else:
        state = START
        rest = token
    
    for ch in rest:
        next_state = transition(state, ch)
        trace.append(f"State: {state}, Input: '{ch}' -> {next_state}")
        state = next_state
        if state == ERROR:
            break
    
    # Add final transition
    final_state = transition(state, "$")
    trace.append(f"State: {state}, Input: '$' -> {final_state}")
    
    return final_state == ACCEPT, final_state, trace


if __name__ == "__main__":
    token = input("Enter token (e.g. 42 or 0xFF): ")
    is_valid, final_state, trace = slr_parse(token)
    
    print("\nSLR Parse Trace:")
    for line in trace:
        print(f"  {line}")
    
    if is_valid:
        print("\n✓ String Accepted by SLR Parser")
    else:
        print(f"\n✗ Parsing Error - Final State: {final_state}")
