// SOUND

function beep(freq,duration,delay=0) {
    try {
        const C=window.AudioContext||window.webkitAudioContext;
        if(!C)return;

        audio ||= new C();
        if(audio.state==="suspended")audio.resume();

        const oscillator=audio.createOscillator();
        const gain=audio.createGain();
        const t=audio.currentTime+delay/1000;

        oscillator.type="square";
        oscillator.frequency.value=freq;
        gain.gain.setValueAtTime(.045,t);
        gain.gain.exponentialRampToValueAtTime(
            .001,t+duration/1000
        );

        oscillator.connect(gain);
        gain.connect(audio.destination);
        oscillator.start(t);
        oscillator.stop(t+duration/1000);
    } catch(e){}
}

function successSound() {
    beep(1000,80);
    beep(1200,50,95);
}

function failureSound() {
    beep(200,300);
    beep(170,400,320);
    beep(120,1100,750);
}
