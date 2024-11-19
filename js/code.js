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

const users = {nom: "Th30", password: 'tkt', points: 100 };

function enter(){
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    if (usernameInput.value == users.nom &&
        passwordInput.value == users.password) {
            document.location.href='main.html'}
    /* if (usernameInput.value.trim() != '' &&
        passwordInput.value.trim() != '') {
            document.location.href='main.html'} */
}

// Mettre à jour les points de l'utilisateur
function updatePoints() {
    document.getElementById('username').innerText = `Points: ${users.nom}`;
    document.getElementById('user-points').innerText = `Points: ${users.points}`;
}
updatePoints();