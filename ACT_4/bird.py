# Belief Revision Simulation — Interactive-friendly Python program
# This code both defines an interactive function you can run locally and
# demonstrates example runs here (so it produces output in this notebook).

# The program follows the rule:
#   "If an animal is a bird, assume it can fly."
# It revises that conclusion if the animal is a known flightless bird
# (e.g., penguin, ostrich). It prints the system's reasoning step-by-step.

def reason_about(animal_name: str, is_bird: bool, known_exceptions=None):
    """
    Returns a tuple (steps:list[str], final_conclusion:str).
    - animal_name: name of the animal (string)
    - is_bird: whether the user classifies it as a bird (True/False)
    - known_exceptions: optional set/list of bird species known to be flightless
    """
    if known_exceptions is None:
        known_exceptions = {
            "penguin", "ostrich", "emu", "kiwi", "cassowary", "rhea",
            "flightless cormorant", "kakapo"  # a few more examples
        }
    steps = []
    animal = animal_name.strip().lower()
    
    steps.append(f"Input: animal = '{animal_name}'")
    steps.append("Starting rule: If an animal is a bird, assume it can fly. (default assumption)")
    
    if not is_bird:
        steps.append("User classification: This animal is NOT a bird.")
        steps.append("Apply rule: The rule does not apply because the animal is not a bird.")
        final = f"Conclusion: The rule doesn't apply to '{animal_name}'. We don't assume it can fly based on the bird-rule."
        steps.append(final)
        return steps, final
    
    # If it's a bird — apply default rule
    steps.append("User classification: This animal IS a bird.")
    steps.append("Default assumption applied: Assume the bird can fly (unless there is evidence otherwise).")
    assumed = f"Assumed conclusion: '{animal_name}' can fly."
    steps.append(assumed)
    
    # Check for known exceptions (belief revision)
    # We'll perform a case-insensitive containment check to catch entries like "Emu" etc.
    # Also support multi-word names
    is_exception = any(exc in animal for exc in known_exceptions) or animal in known_exceptions
    if is_exception:
        steps.append(f"New information check: '{animal_name}' matches known flightless bird(s).")
        steps.append("Belief revision: Withdraw the previous assumption because of the exception.")
        final = f"Revised conclusion: '{animal_name}' cannot fly (exception to the default rule)."
        steps.append(final)
        return steps, final
    else:
        steps.append("No conflicting information found among known exceptions.")
        final = f"Final conclusion: '{animal_name}' can fly (default assumption stands)."
        steps.append(final)
        return steps, final

# Interactive wrapper for local use
def interactive_mode():
    print("=== Belief Revision Simulation ===")
    print("Rule: If an animal is a bird, assume it can fly.\n")
    name = input("Enter an animal name (e.g., 'Sparrow', 'Penguin'): ").strip()
    bird_q = input("Is this animal a bird? (y/n): ").strip().lower()
    is_bird = bird_q.startswith('y')
    steps, conclusion = reason_about(name, is_bird)
    print("\n--------------")
    for s in steps:
        print(s)
    print("\n--- End ---")

# Demonstration runs (kept for --demo mode)
examples = [
    ("Sparrow", True),
    ("Penguin", True),
    ("Bat", False),
    ("Ostrich", True),
    ("Unknown Creature", True)  # a bird not in exceptions
]

def _simple_sample_output(animal: str, is_bird: bool):
    _, final = reason_about(animal, is_bird)
    a = animal.strip()
    a_low = a.lower()

    if not is_bird:
        reason = f"{a} is not a bird."
        conclusion = f"No bird-rule conclusion for {a_low}."
    else:
        is_exception = "cannot fly" in final.lower()
        # choose verb for readability
        verb_do = "do" if a_low.endswith('s') else "does"
        be = "are" if a.endswith('s') else "is"

        if is_exception:
            reason = f"{a} {be} a bird. However, {a_low} {verb_do} not fly."
            conclusion = f"{a_low} cannot fly."
        else:
            reason = f"{a} {be} a bird."
            conclusion = f"{a_low} can fly."

    return f"Input: {a_low}", f"Reasoning: {reason}", f"Conclusion: {conclusion}"

if __name__ == "__main__":
    import sys
    if "--demo" in sys.argv:
        for animal, is_bird in examples:
            lines = _simple_sample_output(animal, is_bird)
            print("\n".join(lines))
            print() 
    else:
        interactive_mode()

