
// MENUS

const random = arr => arr[Math.floor(Math.random()*arr.length)];

function menuSubject() {
    clearScreen();
    state="subject";

    say(`Welcome, ${user}.`);
    say("Available subjects:");
    subjects.forEach((s,i)=>say(`${i+1}. ${label(s)}`));

    ask("Choose subject: ",v=>{
        const n=Number(v);
        subject=Number.isInteger(n)&&n>=1&&n<=subjects.length
            ?subjects[n-1]
            :subjects.includes(v.trim().toLowerCase())
                ?v.trim().toLowerCase()
                :random(subjects);

        say(`Selected: ${label(subject)}`);
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
        const picked=Number.isInteger(n)&&n>=1&&n<=available.length
            ?available[n-1]
            :available.find(e=>e.name.toLowerCase()===v.trim().toLowerCase())
                ||random(available);

        exercise=picked.name;
        exerciseId=picked.id;
        menuDifficulty();
    });
}

function menuDifficulty() {
    clearScreen();

    say(`Selected: ${exercise}`);
    say('Difficulty: set 1–4 (default: Normal)');
    say("1. Fixed number of tasks");
    say("2. Fixed time");
    say("3. Target score");

    ask("Training mode: ",v=>{
        if(/^set\s+\d+$/i.test(v)) {
            difficulty=Math.max(1,Math.min(4,Number(v.split(/\s+/)[1])));
            say(`Difficulty: ${difficulty}`);
            return menuDifficulty();
        }

        mode=["1","2","3"].includes(v.trim())
            ?Number(v.trim())
            :1+Math.floor(Math.random()*3);

        const defaults={1:15,2:1,3:100};
        const messages={
            1:"Number of tasks",
            2:"Time in minutes",
            3:"Target score"
        };

        ask(`${messages[mode]} (default ${defaults[mode]}): `,v=>{
            const n=Number(v.trim());
            const valid=v.trim()!==""&&Number.isFinite(n)&&n>0;

            const value=valid?n:defaults[mode];
            target=mode===2?value*60:value;

            begin();
        });
    });
}
