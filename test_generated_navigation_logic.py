## A typical test case:
# {
#     "goal_ahead": True,
#     "goal_on_left": False,
#     "goal_on_right": False,
#     "front_blocked": False,
#     "left_blocked": False,
#     "right_blocked": False
# },
# "FORWARD"
## The typical case above is the first entry of TEST_CASES.
## TEST_CASES covers all 2^6 = 64 possible states of the six boolean inputs,
## together with the action the navigation logic must return for each state.

from navigation_logic import decide_action

STATE_KEYS = [
    "goal_ahead",
    "goal_on_left",
    "goal_on_right",
    "front_blocked",
    "left_blocked",
    "right_blocked",
]

TEST_CASES = [
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": True, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": True, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": True, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": True}, "STOP"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": True, "right_blocked": False}, "RIGHT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": True}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": True, "left_blocked": False, "right_blocked": False}, "LEFT"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": True, "right_blocked": False}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": True}, "FORWARD"),
    ({"goal_ahead": False, "goal_on_left": False, "goal_on_right": False, "front_blocked": False, "left_blocked": False, "right_blocked": False}, "FORWARD"),
]


def run_tests():
    if len(TEST_CASES) != 64:
        print(f"Expected 64 test cases, found {len(TEST_CASES)}.")
        return 1

    seen = set()
    for state, _ in TEST_CASES:
        key = tuple(state[name] for name in STATE_KEYS)
        if key in seen:
            print(f"Duplicate test case: {state}")
            return 1
        seen.add(key)

    failures = []
    for state, expected in TEST_CASES:
        result = decide_action(**state)
        if result != expected:
            failures.append((state, expected, result))

    print(f"Ran {len(TEST_CASES)} test cases.")
    if failures:
        print(f"{len(failures)} test case(s) failed:")
        for state, expected, result in failures:
            print(f"  state={state} expected={expected} got={result}")
        return 1

    print("All test cases passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_tests())
