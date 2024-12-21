// Afficher l'heure
setInterval(() => document.getElementById('clock').innerText = new Date().toLocaleTimeString(), 1000);

// Fonction qui ouvre/ferme la sidebar
function toggleSidebar(){
    const toggleButton = document.getElementById('toggle-btn')  // Récupère l'élément par l'id 'toggle-btn' et le met dans la constante toggleButton
    const sidebar = document.getElementById('nav')              // Récupère l'élément par l'id 'nav' et le met dans la constante sidebar
    sidebar.classList.toggle('close')                           // Ajoute classe close à sidebar
    toggleButton.classList.toggle('rotate')                     // Ajoute classe rotate toggleButton
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

let quantity = 10; // Valeur initiale

// Met à jour la quantité en fonction de l'incrément (ou décrément)
function updateQuantity(change) {
    quantity += change;               // La quantité augmente avec le param change (10 par défaut)
    if (quantity < 10) quantity = 10; // La quantité minimale est 10
    document.getElementById('quantity').textContent = quantity; // Récupère l'élément quantity et modifie le texte par la nouvelle quantité
}

// Fonction pour placer un pari
function placeBet(player, buttonId, otherbuttonId) {
    const button = document.getElementById(buttonId);   // Récupère l'élément buttonId
    const other_button = document.getElementById(otherbuttonId);

    // Vérifie si un pari a déjà été effectué
    if (button.classList.contains('paried')||other_button.classList.contains('paried')) {          // Si un paris est déjà effectué
        alert(`Vous avez déjà parié ${quantite_pari} points sur ${player}.`);   // Envoie à l'utilisateur qu'il ne peut pas parier
        return;
    }

    // Ajoute la classe pour changer la couleur et signale un pari
    button.classList.add('paried');                     // Un pari est en train d'être effectué donc on ajoute la classe paried
    quantite_pari = quantity                            // Place la quantité parié dans quantite_pari pour savoir combien a-t-on
                                                            // parié même si on change la quantité après
    alert(`Vous avez parié ${quantity} points sur ${player}.`); // Retourne la quantité qu'on a parié sur le joueur
}