function action_ventilo_manu(e) {
    // envoie une requête POST à la route /activventilateur, le json {"value ..."} sera dans le corps de la requête POST
    axios.post('/activventilateur/manu', {"value": e.target.value}).then(
        // .then() indique la fonction à exécuter à réception de la réponse du serveur
        (response) => {
            let result = response.data;
            console.log(result);
        },
        (error) => {
            console.log(error);
        }
    );
}

function action_ventilo_auto(e) {
    // envoie une requête POST à la route /activventilateur, le json {"value ..."} sera dans le corps de la requête POST
    let value_temp = document.querySelector('input[name="temp"]');
    axios.post('/activventilateur/auto', {"temp": value_temp.value}).then(
        // .then() indique la fonction à exécuter à réception de la réponse du serveur
        (response) => {
            let result = response.data;
            console.log(result);
        },
        (error) => {
            console.log(error);
        }
    );
}

function lumieres(e) {
    // envoie une requête POST à la route /lumieres, le json {"value ..."} sera dans le corps de la requête POST
    axios.post('/lumieres', {"value": e.target.value}).then(
        // .then() indique la fonction à exécuter à réception de la réponse du serveur
        (response) => {
            let result = response.data;
            console.log(result);
        },
        (error) => {
            console.log(error);
        }
    );
}

let radios = document.querySelectorAll('input[name="activerventilo"]');
/*  forEach est une méthode des tableaux (ici radios)
    elle applique une fonction (ici "element => {...}" est une fonction anonyme)
    à chaque élément de ce tableau (on ajoute un évènement onChange sur chaque input radio)
*/
radios.forEach(element => {
    element.addEventListener('change', action_ventilo_manu, false);    
});


let button = document.querySelectorAll('input[name="temp"]');
button.forEach(element => {
    element.addEventListener('change', action_ventilo_auto, false);    
});


let couleurs = document.querySelectorAll('input[name="Couleurs"]');
couleurs.forEach(element => {
    element.addEventListener('change', lumieres, false);    
});

let temp = document.querySelector('#settemp');
temp.addEventListener("click", action_ventilo_auto, false);