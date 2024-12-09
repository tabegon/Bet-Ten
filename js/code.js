// Afficher l'heure
setInterval(() => document.getElementById('clock').innerText = new Date().toLocaleTimeString(), 1000);


function toggleSidebar(){
    const toggleButton = document.getElementById('toggle-btn')
    const sidebar = document.getElementById('nav')
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
}

// Fonction pour afficher une animation après un pari
function showAnimation(result, correctAnswer) {
    const anim = document.getElementById('animation');  // Récupère l'élément par l'id 'animation' et le met dans la constante anim
    anim.style.display = 'block';                       // Affiche l'élément 
    anim.innerHTML = result ? "Gagné !" : "Perdu !";    // Change le texte html de l'élément en fonction du résultat (Gagné ou Perdu)
    if (anim.innerHTML == "Perdu !"){                   // Si le texte html d'anim est "perdu":
        anim.innerHTML = "Perdu ! <br> la réponse était " + correctAnswer 
    }                                                   // Change le texte html d'anim pour avoir la réponse avec
    setTimeout(() => anim.style.display = 'none', 2000);// Fait disparaître l'élément au bout d'un certain temps
    
};

// Fonction de vérification des réponses au quiz
function checkAnswer(button, correctAnswer) {
    const input = button.previousElementSibling.value;          // Prends la valeur de l'input de la question et la met dans la constante input
    const questionDiv = button.parentElement;                   // Prends la division de la question et la met dans la constante questionDiv
    if (input.toLowerCase() == correctAnswer.toLowerCase()) {   // Si la valeur de l'input est = à la réponse
        showAnimation(true, correctAnswer);                     // Utilise la fonction showAnimation avec comme parmètre: True (bonne réponse)
    } else {                                                        // et le paramètre correctAnswer qui correspond à la réponse
        showAnimation(false, correctAnswer);                    // Utilise la fonction showAnimation avec comme parmètre: False (fausse réponse)
    }                                                               // et le paramètre correctAnswer qui correspond à la réponse
    questionDiv.style.display = "none"; // Supprime la question
};

const users = {nom: "Th30", password: 'tkt', points: 10 };      // Tous les utilisateurs avec leurs mdp et leurs nb de points

// Fonction d'entrée dans le site
function enter(passwordInput, usernameInput){
    if (usernameInput == users.nom &&       // Si la valeur de nom est = au nom de users et
        passwordInput == users.password) {  // la valeur de mdp est = au mdp de users
            open('main.html');              // Ouvre la page web voulue
            close('login.html')};           // Fermer la page actuelle
};

// Fonction qui amène la page login
function to_login(passwordInput, usernameInput){
    if (usernameInput !== "" &&     // Si la valeur de nom est différent à rien et
        passwordInput !== "") {         // la valeur de mdp est différente à rien
            open('login.html');     // Ouvre la page login
            close('register.html')} // Ferme la page actuelle
}