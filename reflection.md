# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  It was a nice-looking streamlit app. It allows to choose a difficulty level and guess the secret number. It is supposed to give hints, update the history, count scores, start the new game.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. When I started testing the game, my first attempt already indicated a bug. It incorrectly gives hints about going lower or higher.  (fixed)
  2. The difficulty options are messed up too. 
  3. Once I won or lost, pressing "New Game" button does not allow me to submit new guesses. Although it updates the secret number to a new number. Reloading the page allows to start submitting the new guess, but not the button. (fixed)
  4. Allowed attempts are 8 but it is actually 7.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Copiot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One AI suggestion that was correct was to add a game_id value in Streamlit session state and include it in the guess input key, so each New Game uses a fresh input widget instead of keeping the old text. I verified it manually by entering a guess, clicking New Game, and confirming the input box reset and the new round started cleanly. I also ran pytest and all tests passed after the change.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One AI suggestion that was misleading was the first version of the check_guess fix: it correctly swapped the hint directions and switched to numeric comparison, but it missed the exact-match case when secret was a string. I verified that by running a terminal test and seeing check_guess(50, '50') return Too Low instead of Win. After I added an explicit equality check in the fallback branch, that case passed and the tests were correct

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I ran pytest tests and I verified it was working as expected in the browser.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran was after fixing check_guess. I added targeted cases like check_guess(9, '10'), check_guess(10, '9'), and check_guess(50, '50') to verify the string/int edge cases that were causing wrong hints before. 

- Did AI help you design or understand any tests? How?
Yes, AI helped me design these tests by suggesting edge-case inputs and helping me trace why mixed types were breaking the logic.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the script from top to bottom on every interaction, and the original code was reassigning the secret in a way that didn’t preserve it correctly between reruns.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
In Streamlit, a rerun is like replaying your whole script every time you click a button or type in an input, so any value not protected in session state can reset unexpectedly. I’d explain session state as the app’s memory: it keeps values (like secret number, score, attempts) alive across reruns so the game can continue instead of restarting every click. 

- What change did you make that finally gave the game a stable secret number?
The change that stabilized it was storing secret in st.session_state and only setting it when it didn’t exist yet, then resetting it intentionally only inside the New Game flow. That made the secret persist during guesses and change only when a true new game starts.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit that I want to reuse is asking AI to write the tests. And, of course, explaining me the data flow and technical details of the lines I select. 

- What is one thing you would do differently next time you work with AI on a coding task?
I would spend more time on giving AI a good prompt, using #file and #codebase tags in order to increase the chances of better response and less token usage.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
I have never had such assignments before. The positive thought that I git was "Building apps is going to be faster with AI". Another concerning though was - "AI era programmers need both to learn how to use AI but also must develop good code review/understanding skills at the same time". In general, AI seems incredibly capable.

# adding this to check if Github Commit Message feature will appear