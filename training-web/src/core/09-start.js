// START

function boot() {
    clearScreen();

    say("TRAINING CMD");
    say("============");
    say("A little practice. A little pressure.");
    blank();

    ask(
        user
            ?`Welcome back, ${user}. Press ENTER or enter a new name: `
            :"Sign in with your name: ",
        v=>{
            if(v.trim())user=v.trim();
            if(!user)user="Fighter";

            localStorage.setItem("training.lastUser",user);
            menuSubject();
        }
    );
}
