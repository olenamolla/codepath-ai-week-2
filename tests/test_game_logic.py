from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting the two bugs fixed with Copilot in AI Agent Mode ---

# Bug 1: Hint messages were reversed (Go HIGHER when guess was too high, Go LOWER when too low)
def test_hint_message_too_high_says_go_lower():
    outcome, message = check_guess(70, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"

def test_hint_message_too_low_says_go_higher():
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"

# Bug 2: Lexicographic string comparison gave wrong direction for multi-digit numbers
# when secret was cast to str (happens on even attempts in app.py).
# e.g. "9" > "10" is True lexicographically, so 9 vs '10' was wrongly "Too High".
def test_string_secret_guess_under():
    # 9 < 10, so should be Too Low — lexicographic bug returned Too High
    outcome, message = check_guess(9, '10')
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_string_secret_guess_over():
    # 10 > 9, so should be Too High — lexicographic bug returned Too Low
    outcome, message = check_guess(10, '9')
    assert outcome == "Too High"
    assert "LOWER" in message

# Bug 2b: Exact match with string secret should still return Win
# (50 == '50' is False in Python 3, original fallback missed this)
def test_string_secret_exact_match_is_win():
    outcome, _ = check_guess(50, '50')
    assert outcome == "Win"
