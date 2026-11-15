(() => {
"use strict";

const output=document.querySelector("#output");
const cmd=document.querySelector("#cmd");
const promptEl=document.querySelector("#prompt");

const EXIT=["bye","see ya","exit","goodbye","hasta la vista",
"farewell","dosviduli","off","finish","gg","home",
"i am batman","i'll be back","nooooo"];

// Injected by assemble.py from the enabled src/config/*.json files.
const exercises={{EXERCISE_CONFIG}};
const subjects=[...new Set(exercises.flatMap(e=>e.subjects))].sort();
const label=s=>s.charAt(0).toUpperCase()+s.slice(1);

let state="boot",handler=null;
let user=localStorage.getItem("training.lastUser")||"";
let exercise="",exerciseId="",subject="",mode=1,target=15,difficulty=0;
let correct=0,wrong=0,started=0,question=null,task=0,score=0;
let audio=null;

// ---------------------------------------------------------------
// CORE MODULES (src/core/<name>.js)
// ---------------------------------------------------------------
// @include pycompat
// @include terminal
// @include sound
// @include ascii
// @include maths
// @include scoring
// @include training
// @include results
// @include menus
// @include start


// INPUT

cmd.addEventListener("keydown",event=>{
    if(event.key!=="Enter")return;

    event.preventDefault();

    const value=cmd.value;
    say(promptEl.textContent+value);

    cmd.value="";
    cmd.disabled=true;

    if(handler) {
        const fn=handler;
        handler=null;
        fn(value);
        return;
    }

    if(state==="answer")submitAnswer(value);
    else if(state==="between")nextQuestion();
    else if(state==="return")menuSubject();
});

boot();

})();