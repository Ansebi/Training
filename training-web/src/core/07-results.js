// RESULTS

function finish() {
    clearScreen();

    const seconds=Math.floor((Date.now()-started)/1000);
    score=getScore();

    say("========== TRAINING RESULTS ==========","good");
    say(exercise);
    say(`${accuracy()}% accuracy`);
    say(`${Math.floor(seconds/60)} min ${seconds%60} sec`);
    say(`${correct} correct, ${wrong} incorrect`);
    say(`Your score: ${score}`,"good");
    blank();

    const history=JSON.parse(
        localStorage.getItem("training.history")||"[]"
    );

    history.push({
        date:new Date().toISOString(),
        user,exercise,difficulty,seconds,
        correct,wrong,accuracy:accuracy(),score
    });

    localStorage.setItem(
        "training.history",
        JSON.stringify(history.slice(-300))
    );

    say("Session saved in this browser.");
    say("Press ENTER to return to the menu.");

    state="return";
    handler=null;
    setPrompt();
}
