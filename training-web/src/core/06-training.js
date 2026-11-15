// TRAINING

function begin() {
    clearScreen();

    correct=0;
    wrong=0;
    score=0;
    task=0;
    started=Date.now();

    say(`TRAINING: ${exercise}`,"good");
    say(`Difficulty: ${difficulty||"Normal"}`);
    nextQuestion();
}

function nextQuestion() {
    if(mode===1&&task>=target)return finish();
    if(mode===2&&(Date.now()-started)/1000>=target)return finish();
    if(mode===3&&getScore()>=target)return finish();

    // Clear the previous question and its feedback.
    clearScreen();

    task++;
    question=makeQuestion();

    stats();
    blank();

    if(mode===1)say(`tasks complete: ${task-1}/${target}`);

    if(mode===2) {
        const r=Math.max(0,target-Math.floor((Date.now()-started)/1000));
        say(`time remaining: ${Math.floor(r/60)}:${String(r%60).padStart(2,"0")}`);
    }

    if(mode===3)say(`target score: ${target}`);

    say(question.text);
    state="answer";
    handler=null;
    setPrompt();
}

function submitAnswer(value) {
    if(EXIT.includes(value.toLowerCase()))return finish();

    if(question.answers.includes(value.trim())) {
        correct++;
        say("Yeap — well done :)","good");
        yay();
    } else {
        wrong++;
        say("Nope.","bad");
        boo();
        say(`Your answer: ${value}`);
        say(`The correct answer is: ${question.answers.join(" or ")}`,"good");
    }

    stats();
    blank();
    say("Press ENTER for next task");

    state="between";
    handler=null;
    setPrompt();
}
