// Afficher l'heure
setInterval(() => document.getElementById('clock').innerText = new Date().toLocaleTimeString(), 1000);

// Fonction pour afficher une animation après un pari
function showAnimation(result) {
    const anim = document.getElementById('animation');
    anim.style.display = 'block';
    anim.innerText = result ? "Gagné !" : "Perdu !";
    setTimeout(() => anim.style.display = 'none', 2000);
}

// Fonction de vérification des réponses au quiz
function checkAnswer(button, correctAnswer) {
    const input = button.previousElementSibling.value;
    const questionDiv = button.parentElement;
    if (input.toLowerCase() === correctAnswer.toLowerCase()) {
        showAnimation(true);
    } else {
        showAnimation(false);
    }
    questionDiv.style.display = "none"; // Remplacer la question
}