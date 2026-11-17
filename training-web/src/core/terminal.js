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