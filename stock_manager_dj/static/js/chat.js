document.addEventListener("DOMContentLoaded", function() {
    const sendBtn = document.getElementById("send-btn");
    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-messages");
    sendBtn.addEventListener("click", async function(e) {
        e.preventDefault();

        const message = input.value.trim();
        if (!message) return;

        //Mensagem do usuario

        chatBox.innerHTML += `
            <div class="flex justify-end gap-3 my-4 text-sm text-gray-700">
                <p class="w-auto px-4 py-2 bg-gray-200 rounded-md leading-relaxed">${message}</p>
            </div>
         `;
         input.value = "";

         //Envia para o backend
         const response = await fetch("/api/chatbot/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({message})
         });

         const data = await response.json();

         //Mostra a resposta da IA
         chatBox.innerHTML += `
            <div class="flex gap-3 my-4 text-sm text-gray-700">
                <p class="leading-relaxed">${data.response}</p>
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;
    });

    //Funcao para pegar o CSRF

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== ""){
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++){
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) == (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});