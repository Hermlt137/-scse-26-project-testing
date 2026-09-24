"""Level 2 behavioral tests for the generated navigation logic.

Calls decide_next_move(state) from generated/navigation_logic.py with every
possible robot state and checks that the returned action is a valid action
and the correct expected move for that state.

A state is described by six booleans:

    goal_ahead, goal_on_left, goal_on_right
        Which direction the goal is in. At most one of them is True.
        All three False means the goal is not visible.

    front_blocked, left_blocked, right_blocked
        Which directions are blocked by an obstacle.

The expected action for every state follows the navigation plan:
1. The robot must move toward its goal whenever that direction is safe.
2. The robot must never move into a blocked direction.
3. The robot must stop only when no safe direction is available.

TEST_CASES covers all 2^6 = 64 possible states of the six boolean inputs,
including the states where more than one goal direction is True.

Run the tests with:
    python test_generated_navigation_logic.py
"""

from generated.navigation_logic import decide_next_move

VALID_ACTIONS = ["FORWARD", "LEFT", "RIGHT", "STOP"]

STATE_KEYS = [
    "goal_ahead",
    "goal_on_left",
    "goal_on_right",
    "front_blocked",
    "left_blocked",
    "right_blocked",
]

TEST_CASES = [
    # The sample test case shared with us is the first entry.
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
        result = decide_next_move(state)
        if result not in VALID_ACTIONS:
            failures.append(f"  state={state} returned invalid action {result!r}")
        elif result != expected:
            failures.append(f"  state={state} expected={expected} got={result!r}")

    print(f"Ran {len(TEST_CASES)} test cases.")
    if failures:
        print(f"{len(failures)} test case(s) failed:")
        for failure in failures:
            print(failure)
        return 1

    print("All test cases passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_tests())
