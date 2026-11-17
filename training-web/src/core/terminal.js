// TERMINAL

function clearScreen() {
    output.innerHTML="";
}

function say(text="",cls="") {
    const d=document.createElement("div");
    d.textContent=text;
    if(cls)d.className=cls;
    output.append(d);
    output.scrollTop=output.scrollHeight;
}

function blank(){say()}

function setPrompt(text="> ") {
    promptEl.textContent=text;
    cmd.value="";
    cmd.disabled=false;
    cmd.focus({preventScroll:true});
}

function ask(message,fn) {
    say(message);
    handler=fn;
    setPrompt();
}

// PROGRESS BAR: one fraction, depending on the mode.
function progress() {
    let f=0;
    if(state==="answer"||state==="between") {
        const done=state==="answer"?task-1:task;
        if(mode===1)f=done/target;
        else if(mode===2)f=(Date.now()-started)/1000/target;
        else if(mode===3)f=getScore()/target;
    }
    f=Math.min(1,Math.max(0,f||0));
    document.body.style.setProperty("--p",f);
}

setInterval(progress,250);