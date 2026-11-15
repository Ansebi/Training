
(() => {
  "use strict";

  const registeredExercises = new Map();

  const screen = document.getElementById("screen");
  const input = document.getElementById("command-input");
  const form = document.getElementById("command-form");
  const status = document.getElementById("status");

  const DEFAULT_TARGET_SCORE = 1000;
  const DEFAULT_FIXED_TIME_SEC = 60;
  const DEFAULT_FIXED_NUMBER_OF_TASKS = 15;

  const EXIT_LIST = [
    "bye", "see ya", "exit", "goodbye",
    "hasta la vista", "farewell", "dosviduli",
    "off", "finish", "gg", "home",
    "i am batman", "i'll be back", "nooooo"
  ];

  const HISTORY_KEY = "training_session_history";
  const USER_KEY = "training_last_user";

  const state = {
    mode: "entrance",
    userName: "",
    lastUser: "",
    subject: null,
    exercise: null,
    question: null,

    difficulty: 1,
    trainingType: "1",

    numberOfTasks: DEFAULT_FIXED_NUMBER_OF_TASKS,
    fixedTime: DEFAULT_FIXED_TIME_SEC,
    targetScore: DEFAULT_TARGET_SCORE,

    correct: 0,
    incorrect: 0,
    percentage: 0,
    score: 0,

    startedAt: 0,
    elapsed: 0,
    minutesElapsed: 0,
    secondsElapsed: 0,

    completedTasks: 0,
    exitRequested: false
  };

  // --------------------------------------------------
  // PUBLIC EXERCISE API
  // --------------------------------------------------

  window.Training = {
    registerExercise(definition) {
      if (!definition || typeof definition.id !== "string") {
        throw new Error("Exercise must have a string ID.");
      }

      if (typeof definition.generate !== "function") {
        throw new Error(
          `Exercise ${definition.id} has no generate() function.`
        );
      }

      if (registeredExercises.has(definition.id)) {
        throw new Error(
          `Duplicate exercise registration: ${definition.id}`
        );
      }

      registeredExercises.set(definition.id, definition);
    },

    randomInt(min, max) {
      return Math.floor(
        Math.random() * (max - min + 1)
      ) + min;
    }
  };

  // --------------------------------------------------
  // CONFIGURATION
  // --------------------------------------------------

  function loadExercises() {
    const configs = window.TRAINING_CONFIG;

    if (!Array.isArray(configs)) {
      throw new Error("Training configuration is missing.");
    }

    return configs
      .filter(config => config.enabled !== false)
      .map(config => {
        const definition = registeredExercises.get(config.id);

        if (!definition) {
          throw new Error(
            `Exercise module not registered: ${config.id}`
          );
        }

        return { config, definition };
      });
  }

  let exercises = [];

  // --------------------------------------------------
  // GENERAL DISPLAY
  // --------------------------------------------------

  function clearScreen() {
    screen.replaceChildren();
  }

  function line(text = "", className = "") {
    const element = document.createElement("div");

    element.className = `line ${className}`;
    element.textContent = String(text);

    screen.appendChild(element);

    return element;
  }

  function blank() {
    line("");
  }

  function setStatus(value) {
    status.textContent = value;
  }

  function focusInput() {
    input.focus();
  }

  function isExit(value) {
    return EXIT_LIST.includes(
      String(value).trim().toLowerCase()
    );
  }

  function banner() {
    line("╔══════════════════════════════════════════════╗");
    line("║                 TRAINING                     ║");
    line("║          MATHEMATICS & LANGUAGE               ║");
    line("╚══════════════════════════════════════════════╝");
    blank();
  }

  function randomItem(items) {
    return items[Math.floor(Math.random() * items.length)];
  }

  // --------------------------------------------------
  // PLAYER ENTRANCE
  // --------------------------------------------------

  function showEntrance() {
    state.mode = "entrance";

    try {
      state.lastUser = localStorage.getItem(USER_KEY) || "";
    } catch (error) {
      state.lastUser = "";
    }

    clearScreen();
    setStatus("WELCOME");

    banner();

    line(`Hello, ${state.lastUser}!`, "highlight");
    blank();
    line("PRESS ENTER");
    line("or sign as a different fighter:");
    blank();

    focusInput();
  }

  function acceptPlayerName(value) {
    const enteredName = value.trim();

    state.userName = enteredName || state.lastUser || "Player";

    if (enteredName) {
      try {
        localStorage.setItem(USER_KEY, state.userName);
      } catch (error) {
        // Player identity is optional.
      }
    }

    clearScreen();

    line(`Okay, ${state.userName}`, "highlight");
    blank();

    showSubjectMenu();
  }

  // --------------------------------------------------
  // SUBJECT AND EXERCISE SELECTION
  // --------------------------------------------------

  function getSubjects() {
    const subjects = new Set();

    exercises.forEach(item => {
      (item.config.subjects || []).forEach(subject => {
        subjects.add(subject);
      });
    });

    return [...subjects].sort();
  }

  function getSubjectExercises(subject) {
    return exercises
      .filter(item =>
        (item.config.subjects || []).includes(subject)
      )
      .sort((a, b) =>
        (a.config.sort_order ?? 9999) -
        (b.config.sort_order ?? 9999) ||
        a.config.name.localeCompare(b.config.name)
      );
  }

  function showSubjectMenu() {
    state.mode = "subjects";
    state.subject = null;
    state.exercise = null;

    clearScreen();
    setStatus("SELECT SUBJECT");

    banner();

    line(`${state.userName}, please choose the subject:`, "highlight");
    blank();

    const subjects = getSubjects();

    subjects.forEach((subject, index) => {
      line(`${index + 1}. ${subject}`);
    });

    blank();
    line("Your choice:");

    focusInput();
  }

  function selectSubject(value) {
    const subjects = getSubjects();

    let index = Number(value) - 1;

    // The original program randomly selected a subject
    // when the input was not a valid subject number.
    if (
      !Number.isInteger(index) ||
      index < 0 ||
      index >= subjects.length
    ) {
      index = Math.floor(Math.random() * subjects.length);
    }

    state.subject = subjects[index];

    showExerciseMenu();
  }

  function showExerciseMenu() {
    state.mode = "exercises";

    clearScreen();
    setStatus(state.subject.toUpperCase());

    line(`${state.subject.toUpperCase()} EXERCISES`, "highlight");
    blank();

    const available = getSubjectExercises(state.subject);

    available.forEach((item, index) => {
      line(`${index + 1}. ${item.config.name}`);
    });

    blank();
    line("Choose the exercise:");

    focusInput();
  }

  function selectExercise(value) {
    const available = getSubjectExercises(state.subject);

    let index = Number(value) - 1;

    if (
      !Number.isInteger(index) ||
      index < 0 ||
      index >= available.length
    ) {
      index = Math.floor(Math.random() * available.length);
    }

    state.exercise = available[index];

    prepareExercise();
  }

  // --------------------------------------------------
  // TRAINING SETUP
  // --------------------------------------------------

  function prepareExercise() {
    const config = state.exercise.config;

    state.difficulty = config.default_difficulty ?? 1;

    state.correct = 0;
    state.incorrect = 0;
    state.percentage = 0;
    state.score = 0;
    state.elapsed = 0;
    state.completedTasks = 0;
    state.exitRequested = false;

    showTrainingTypeMenu();
  }

  function showTrainingTypeMenu() {
    state.mode = "training-type";

    clearScreen();
    setStatus("TRAINING SETUP");

    const config = state.exercise.config;

    line(config.name, "highlight");
    blank();

    line(
      `Difficulty Level: ${
        state.difficulty ? state.difficulty : "Normal"
      }`
    );

    line('To change difficulty, enter e.g. "set 5".');
    blank();

    line("1. Fixed number of tasks");
    line("2. Fixed time");
    line("3. Target score");
    blank();

    line("Choose the type of training:");

    focusInput();
  }

  function chooseTrainingType(value) {
    const command = value.trim();

    if (/^set(?:\s|$)/i.test(command)) {
      const parts = command.split(/\s+/);
      const parsed = Number(parts[1]);

      state.difficulty =
        parts.length === 2 && Number.isInteger(parsed)
          ? parsed
          : 0;

      showTrainingTypeMenu();
      return;
    }

    if (!["1", "2", "3"].includes(command)) {
      line("Invalid training type.", "wrong");
      focusInput();
      return;
    }

    state.trainingType = command;

    if (command === "1") {
      showTaskCountInput();
    } else if (command === "2") {
      showFixedTimeInput();
    } else {
      showTargetScoreInput();
    }
  }

  function showTaskCountInput() {
    state.mode = "task-count";

    clearScreen();
    line("Specify the number of tasks:");
    line(`Press ENTER for default: ${DEFAULT_FIXED_NUMBER_OF_TASKS}`);
    focusInput();
  }

  function showFixedTimeInput() {
    state.mode = "fixed-time";

    clearScreen();
    line("Specify the time for training (minutes):");
    line("Press ENTER for default: 1 minute");
    focusInput();
  }

  function showTargetScoreInput() {
    state.mode = "target-score";

    clearScreen();
    line("Specify the target score:");
    line(`Press ENTER for default: ${DEFAULT_TARGET_SCORE}`);
    focusInput();
  }

  function beginTraining(value) {
    if (state.trainingType === "1") {
      const parsed = Number(value);

      state.numberOfTasks =
        value.trim() === ""
          ? DEFAULT_FIXED_NUMBER_OF_TASKS
          : Number.isInteger(parsed) && parsed > 0
            ? parsed
            : DEFAULT_FIXED_NUMBER_OF_TASKS;
    }

    if (state.trainingType === "2") {
      const parsed = Number(value);

      state.fixedTime =
        value.trim() === ""
          ? DEFAULT_FIXED_TIME_SEC
          : Number.isFinite(parsed) && parsed > 0
            ? parsed * 60
            : DEFAULT_FIXED_TIME_SEC;
    }

    if (state.trainingType === "3") {
      const parsed = Number(value);

      state.targetScore =
        value.trim() === ""
          ? DEFAULT_TARGET_SCORE
          : Number.isFinite(parsed) && parsed > 0
            ? parsed
            : DEFAULT_TARGET_SCORE;
    }

    state.correct = 0;
    state.incorrect = 0;
    state.percentage = 0;
    state.score = 0;
    state.completedTasks = 0;

    state.startedAt = Date.now();
    state.elapsed = 0;

    nextQuestion();
  }

  // --------------------------------------------------
  // SCORE AND TIME
  // Mirrors score_counter.py
  // --------------------------------------------------

  function updateStatistics() {
    const total = state.correct + state.incorrect;

    state.percentage = total
      ? Math.round(
          (state.correct / total * 100) * 10
        ) / 10
      : 0;

    state.elapsed = (Date.now() - state.startedAt) / 1000;

    state.minutesElapsed = Math.floor(state.elapsed / 60);

    state.secondsElapsed = Math.round(
      state.elapsed - state.minutesElapsed * 60
    );

    if (state.secondsElapsed === 60) {
      state.minutesElapsed++;
      state.secondsElapsed = 0;
    }

    const config = state.exercise.config;

    const calcTime =
      state.minutesElapsed * 60 +
      state.secondsElapsed +
      1;

    const standardTime =
      Number(config.standard_completion_time_sec) || 0;

    const speedImpact =
      standardTime * state.correct / calcTime;

    const work = state.correct ** 2;
    const badWork = state.incorrect ** 2;
    const correctness = (state.percentage / 100) ** 2;

    let score = work - badWork;
    score *= correctness;
    score *= speedImpact;

    state.score = Math.round(score);
  }

  function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainder = Math.max(
      0,
      Math.round(seconds % 60)
    );

    return `${minutes}:${String(remainder).padStart(2, "0")}`;
  }

  // --------------------------------------------------
  // SOUND EFFECTS
  // --------------------------------------------------

  function playTone(frequency, duration, volume = 0.08) {
    try {
      const AudioContext =
        window.AudioContext || window.webkitAudioContext;

      if (!AudioContext) return;

      const context = new AudioContext();
      const oscillator = context.createOscillator();
      const gain = context.createGain();

      oscillator.type = "square";
      oscillator.frequency.value = frequency;
      gain.gain.value = volume;

      oscillator.connect(gain);
      gain.connect(context.destination);

      oscillator.start();
      oscillator.stop(context.currentTime + duration / 1000);

      oscillator.onended = () => context.close();

      context.resume();
    } catch (error) {
      // Sound is optional.
    }
  }

  function correctSound() {
    playTone(1000, 80);

    setTimeout(() => {
      playTone(1200, 50);
    }, 90);
  }

  function wrongSound() {
    playTone(200, 300);

    setTimeout(() => {
      playTone(170, 400);
    }, 320);

    setTimeout(() => {
      playTone(120, 1100);
    }, 740);
  }

  // --------------------------------------------------
  // ORIGINAL ASCII FEEDBACK
  // --------------------------------------------------

  function showCongratulations() {
    blank();
    line("     **   **");
    line("     **   **");
    line("");
    line("   *         *");
    line("    *       *");
    line("     *******");
    line("       ***");
    blank();
  }

  function showFailure() {
    blank();
    line("    * *   * *");
    line("     *     *");
    line("    * *   * *");
    blank();
    line("     *******");
    line("    *       *");
    line("   *         *");
    blank();
  }

  // --------------------------------------------------
  // QUESTION GENERATION
  // --------------------------------------------------

  function generateQuestion() {
    const item = state.exercise;

    const generated = item.definition.generate(
      Training.randomInt,
      state.difficulty,
      item.config.settings || {}
    );

    if (!generated || typeof generated !== "object") {
      throw new Error(
        `Exercise ${item.config.id} returned an invalid question.`
      );
    }

    const answers = Array.isArray(generated.answers)
      ? generated.answers
      : [generated.answer];

    if (!answers.length || answers.some(answer => answer === undefined)) {
      throw new Error(
        `Exercise ${item.config.id} did not provide an answer.`
      );
    }

    return {
      prompt: generated.prompt || "",
      inputMessage: generated.inputMessage || "Your answer: ",
      answers: answers.map(answer => String(answer))
    };
  }

  function showProgress() {
    const config = state.exercise.config;

    line(config.name, "highlight");

    if (state.trainingType === "1") {
      line(
        `Tasks complete: ${state.completedTasks}/${state.numberOfTasks}`
      );
    } else if (state.trainingType === "2") {
      const remaining = Math.max(
        0,
        state.fixedTime - state.elapsed
      );

      line(`Time remaining: ${formatTime(remaining)}`);
    } else {
      line(`Score: ${state.score}/${state.targetScore}`);
    }

    line(`Points: ${state.score}`);
    line(`Accuracy: ${state.percentage}%`);
    blank();
  }

  function nextQuestion() {
    clearScreen();
    setStatus("TRAINING");

    try {
      state.question = generateQuestion();
    } catch (error) {
      state.mode = "question-error";

      line("QUESTION GENERATION ERROR", "wrong");
      line(error.message || String(error));
      blank();
      line("Press ENTER to return to the exercise menu.");

      return;
    }

    showProgress();

    if (state.question.prompt) {
      line(state.question.prompt, "highlight");
      blank();
    }

    if (state.question.inputMessage) {
      line(state.question.inputMessage);
    }

    state.mode = "answer";
    focusInput();
  }

  // --------------------------------------------------
  // ANSWER CHECKING
  // --------------------------------------------------

  function checkAnswer(value) {
    const question = state.question;

    // Exit words are counted as incorrect, as in training.py.
    if (isExit(value)) {
      state.incorrect++;
      updateStatistics();
      state.exitRequested = true;
      finishTraining(true);
      return;
    }

    const answer = String(value).trim();

    const correct = question.answers.includes(answer);

    if (correct) {
      state.correct++;

      updateStatistics();

      correctSound();

      state.mode = "correct-feedback";

      clearScreen();
      setStatus("CORRECT");

      line(`Points: ${state.score}`);
      line(`Accuracy: ${state.percentage}%`);

      showCongratulations();

      line("Well done :) Press ENTER");
      focusInput();

      return;
    }

    state.incorrect++;

    updateStatistics();

    wrongSound();

    state.mode = "wrong-feedback";

    clearScreen();
    setStatus("INCORRECT");

    line(`Points: ${state.score}`);
    line(`Accuracy: ${state.percentage}%`);
    blank();

    showFailure();

    line("The correct answer is:", "highlight");
    line(question.inputMessage + question.answers.join("; "));
    blank();

    line("Try again :( Press ENTER");
    focusInput();
  }

  // --------------------------------------------------
  // TRAINING LOOP
  // --------------------------------------------------

  function shouldContinue() {
    if (state.trainingType === "1") {
      return state.completedTasks < state.numberOfTasks;
    }

    if (state.trainingType === "2") {
      return state.elapsed < state.fixedTime;
    }

    return state.score < state.targetScore;
  }

  function continueTraining() {
    state.completedTasks++;

    updateStatistics();

    if (!shouldContinue()) {
      finishTraining(false);
      return;
    }

    nextQuestion();
  }

  // --------------------------------------------------
  // SESSION HISTORY
  // --------------------------------------------------

  function getHistory() {
    try {
      const saved = localStorage.getItem(HISTORY_KEY);
      return saved ? JSON.parse(saved) : [];
    } catch (error) {
      return [];
    }
  }

  function saveSession() {
    const config = state.exercise.config;

    const record = {
      date: new Date().toISOString(),
      user: state.userName,
      subject: state.subject,
      exercise: config.name,
      difficulty: state.difficulty,
      trainingType: state.trainingType,
      minutes: state.minutesElapsed,
      seconds: state.secondsElapsed,
      correct: state.correct,
      total: state.correct + state.incorrect,
      accuracy: state.percentage,
      score: state.score
    };

    const history = getHistory();
    history.push(record);

    try {
      localStorage.setItem(
        HISTORY_KEY,
        JSON.stringify(history)
      );
    } catch (error) {
      // Session can finish even if storage is unavailable.
    }
  }

  function exportHistory() {
    const history = getHistory();

    if (!history.length) {
      line("No saved session history.", "wrong");
      return;
    }

    const columns = [
      "date", "user", "subject", "exercise",
      "difficulty", "trainingType", "minutes",
      "seconds", "correct", "total", "accuracy", "score"
    ];

    const rows = [
      columns.join(";"),
      ...history.map(record =>
        columns.map(key =>
          String(record[key] ?? "").replaceAll(";", ",")
        ).join(";")
      )
    ];

    const blob = new Blob(
      ["\uFEFF" + rows.join("\n")],
      { type: "text/csv;charset=utf-8" }
    );

    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");

    link.href = url;
    link.download = `data_${state.userName}.csv`;
    link.click();

    URL.revokeObjectURL(url);
  }

  // --------------------------------------------------
  // SESSION RESULTS
  // --------------------------------------------------

  function finishTraining(exited) {
    updateStatistics();
    saveSession();

    state.mode = "session-finished";

    clearScreen();
    setStatus(exited ? "SESSION EXITED" : "SESSION COMPLETE");

    if (!exited) {
      line(state.exercise.config.name, "highlight");
      blank();

      line(`${state.percentage}%`);
      line(
        `${state.minutesElapsed} min ${state.secondsElapsed} sec`
      );

      line(
        `${state.correct} out of ${state.correct + state.incorrect}`
      );

      blank();
      line(`Your score: ${state.score}`, "highlight");
      blank();

      showNumericScore(state.score);
    }

    blank();
    line("PRESS ENTER TO CONTINUE");
    line("Type an exit command to leave.");

    focusInput();
  }

  function showNumericScore(score) {
    const digits = [
      [" ** ", "*  *", "*  *", "*  *", " ** "],
      ["   *", "  **", "   *", "   *", "   *"],
      [" ** ", "*  *", "  * ", " *  ", "****"],
      [" ** ", "*  *", "  * ", "*  *", " ** "],
      ["*  *", "*  *", "****", "   *", "   *"],
      ["****", "*   ", "*** ", "   *", "*** "],
      [" ***", "*   ", "****", "*  *", "****"],
      ["****", "   *", "  * ", " *  ", "*   "],
      [" ** ", "*  *", " ** ", "*  *", " ** "],
      ["****", "*  *", "****", "   *", "*** "]
    ];

    const value = String(Math.abs(score));

    for (let row = 0; row < 5; row++) {
      line(
        value
          .split("")
          .map(char => digits[Number(char)][row])
          .join(" ")
      );
    }
  }

  // --------------------------------------------------
  // INPUT ROUTER
  // --------------------------------------------------

  form.addEventListener("submit", event => {
    event.preventDefault();

    const value = input.value;
    input.value = "";

    switch (state.mode) {
      case "entrance":
        acceptPlayerName(value);
        break;

      case "subjects":
        if (value.trim().toLowerCase() === "export") {
          exportHistory();
          break;
        }
        selectSubject(value);
        break;

      case "exercises":
        selectExercise(value);
        break;

      case "training-type":
        chooseTrainingType(value);
        break;

      case "task-count":
      case "fixed-time":
      case "target-score":
        beginTraining(value);
        break;

      case "answer":
        checkAnswer(value);
        break;

      case "correct-feedback":
        continueTraining();
        break;

      case "wrong-feedback":
        if (isExit(value)) {
          state.exitRequested = true;
          finishTraining(true);
        } else {
          continueTraining();
        }
        break;

      case "session-finished":
        if (isExit(value)) {
          state.mode = "finished";
          clearScreen();
          setStatus("EXITED");
          line("Training session ended.", "highlight");
        } else {
          showSubjectMenu();
        }
        break;

      case "question-error":
        showExerciseMenu();
        break;
    }

    focusInput();
  });

  document
    .getElementById("terminal")
    .addEventListener("click", focusInput);

  // --------------------------------------------------
  // START
  // --------------------------------------------------

  exercises = loadExercises();
  showEntrance();

})();
