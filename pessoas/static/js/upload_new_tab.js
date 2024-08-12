function uploadAndOpenInNewTab(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    // Redirecionamento do atributo data-redirect-url
    const redirectUrl = form.getAttribute('data-redirect-url');

    // Criação de um request XMLHttpRequest para retorno
    const xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Abre a nova aba com a URL da view que exibe o JSON
            const newTab = window.open(redirectUrl, '_blank');
            newTab.focus();
        }
    };
    xhr.send(formData);
}
