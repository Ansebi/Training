// MENUS

function menuSubject() {
    clearScreen();
    state="subject";

    say(`Welcome, ${user}.`);
    say("Available subjects:");
    subjects.forEach((s,i)=>say(`${i+1}. ${label(s)}`));

    ask("Choose subject: ",v=>{
        const n=Number(v);
        const picked=Number.isInteger(n)&&n>=1&&n<=subjects.length
            ?subjects[n-1]
            :subjects.find(s=>s===v.trim().toLowerCase());

        if(!picked) {
            say("Invalid choice.");
            return menuSubject();
        }

        subject=picked;
        menuExercise();
    });
}

function menuExercise() {
    clearScreen();
    state="exercise";

    const available=exercises.filter(e=>e.subjects.includes(subject));

    say(`${label(subject)} exercises:`);
    available.forEach((e,i)=>say(`${i+1}. ${e.name}`));

    ask("Choose exercise: ",v=>{
        const n=Number(v);

        if(!Number.isInteger(n)||n<1||n>available.length) {
            say("Invalid choice.");
            return menuExercise();
        }

        exercise=available[n-1].name;
        exerciseId=available[n-1].id;
        menuDifficulty();
    });
}

function menuDifficulty() {
    clearScreen();

    say(`Selected: ${exercise}`);
    say('Set difficulty with "set N" (1–4).');
    say("Default is Normal.");
    say("1. Fixed number of tasks");
    say("2. Fixed time");
    say("3. Target score");

    ask("Choose training mode (or set N): ",v=>{
        if(/^set\s+\d+$/i.test(v)) {
            difficulty=Math.max(1,Math.min(4,Number(v.split(/\s+/)[1])));
            say(`Difficulty set to ${difficulty}.`);
            return menuDifficulty();
        }

        if(!["1","2","3"].includes(v)) {
            say("Please enter 1, 2, or 3.");
            return menuDifficulty();
        }

        mode=Number(v);

        const message=mode===1
            ?"Number of tasks (default 15): "
            :mode===2
                ?"Time in minutes (default 1): "
                :"Target score (default 100): ";

        ask(message,n=>{
            n=n.trim();

            if(mode===1)target=n?Math.max(1,parseInt(n,10)||15):15;
            if(mode===2)target=(n?Math.max(.1,Number(n)||1):1)*60;
            if(mode===3)target=n?Math.max(1,parseInt(n,10)||100):100;

            begin();
        });
    });
}
