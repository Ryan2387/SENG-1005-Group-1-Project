document.addEventListener('DOMContentLoaded', () => {
    const flashcard = document.getElementById('flashcard');
    const cardFront = document.getElementById('cardFront');
    const cardBack = document.getElementById('cardBack');
    const flipButton = document.getElementById('flipButton');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const addFlashcardButton = document.getElementById('addFlashcardButton');
    const questionInput = document.getElementById('questionInput');
    const answerInput = document.getElementById('answerInput');

    let flashcards = JSON.parse(localStorage.getItem('flashcards')) || [];
    let currentIndex = 0;

    function updateFlashcard() {
        if (flashcards.length > 0) {
            cardFront.textContent = flashcards[currentIndex].question;
            cardBack.textContent = flashcards[currentIndex].answer;
        }
    }

    addFlashcardButton.addEventListener('click', () => {
        const question = questionInput.value.trim();
        const answer = answerInput.value.trim();

        if (question && answer) {
            flashcards.push({ question, answer });
            localStorage.setItem('flashcards', JSON.stringify(flashcards));
            questionInput.value = '';
            answerInput.value = '';
            updateFlashcard();
        } else {
            alert("Please fill in both question and answer.");
        }
    });

    flipButton.addEventListener('click', () => {
        flashcard.classList.toggle('flipped');
    });

    prevButton.addEventListener('click', () => {
        if (flashcards.length > 0) {
            currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;
            updateFlashcard();
        }
    });

    nextButton.addEventListener('click', () => {
        if (flashcards.length > 0) {
            currentIndex = (currentIndex + 1) % flashcards.length;
            updateFlashcard();
        }
    });

    if (flashcards.length > 0) {
        updateFlashcard();
    }
});
