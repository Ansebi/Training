Training.registerExercise({
  id: "add_negatives",

  generate(rand, difficulty, settings) {
    const n = rand(10, 100);
    const m = rand(10, 100);

    const nSign = rand(0, 1) === 1 ? -1 : 1;
    const mSign = rand(0, 1) === 1 ? -1 : 1;

    const signedN = n * nSign;
    const signedM = m * mSign;

    const answer = String(signedN + signedM);

    const prompt =
      mSign === 1
        ? `${signedN}+${signedM} = `
        : `${signedN}${signedM} = `;

    return {
      prompt,
      answer
    };
  }
});
