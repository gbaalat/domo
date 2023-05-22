function action_ventilo(e) {
    // envoie une requête POST à la route /activventilateur, le json {"value ..."} sera dans le corps de la requête POST
    axios.post('/activventilateur', {"value": e.target.value}).then(
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
radios = document.querySelectorAll('input[name="activerventilo"]');
/*  forEach est une méthode des tableaux (ici radios)
    elle applique une fonction (ici "element => {...}" est une fonction anonyme)
    à chaque élément de ce tableau (on ajoute un évènement onChange sur chaque input radio)
*/
radios.forEach(element => {
    element.addEventListener('change', action_ventilo, false);    
});
