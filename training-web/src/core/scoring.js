// SCORING

function accuracy() {
    return correct+wrong
        ?Math.round(correct/(correct+wrong)*1000)/10
        :0;
}

function getScore() {
    const seconds=Math.max(1,Math.floor((Date.now()-started)/1000));
    const speed=5*correct/seconds;

    return Math.round(
        (correct**2-wrong**2)*
        (accuracy()/100)**2*speed
    );
}

function stats() {
    score=getScore();
    const seconds=Math.floor((Date.now()-started)/1000);
    say(`points: ${score}       accuracy: ${accuracy()}%`);
    say(`time: ${Math.floor(seconds/60)}m ${seconds%60}s`);
}
