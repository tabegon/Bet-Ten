// Afficher l'heure
setInterval(() => document.getElementById('clock').innerText = new Date().toLocaleTimeString(), 1000);

// Fonction pour afficher une animation après un pari
function showAnimation(result, correctAnswer) {
    const anim = document.getElementById('animation');
    anim.style.display = 'block';
    anim.innerHTML = result ? "Gagné !" : "Perdu !";
    if (anim.innerHTML == "Perdu !"){
        anim.innerHTML = "Perdu ! <br> la réponse était " + correctAnswer 
    }
    setTimeout(() => anim.style.display = 'none', 2000);
    
};

// Fonction de vérification des réponses au quiz
function checkAnswer(button, correctAnswer) {
    const input = button.previousElementSibling.value;
    const questionDiv = button.parentElement;
    if (input.toLowerCase() == correctAnswer.toLowerCase()) {
        showAnimation(true, correctAnswer);
    } else {
        showAnimation(false, correctAnswer);
    }
    questionDiv.style.display = "none"; // Remplacer la question
};

const users = {nom: "Th30", password: 'tkt', points: 10 }

function enter(){
    var passwordInput = document.forms['formulaire']['mdp'].value;
    var usernameInput = document.forms['formulaire']['name'].value;
    if (usernameInput == users.nom &&
        passwordInput == users.password) {
            open('main.html')};
}


function to_login(){
    if (usernameInput.value !== "" &&
        passwordInput.value !== "") {
            document.location.href='login.html'}
}