document.addEventListener("DOMContentLoaded", function() {
    const sendBtn = document.getElementById("send-btn");
    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-messages");

    sendBtn.addEventListener("click", async function(e) {
        e.preventDefault();

        const message = input.value.trim();
        if (!message) return;

        // Mostra a mensagem do usuário no chat
        const userMsgDiv = document.createElement("div");
        userMsgDiv.className = "flex justify-end gap-3 my-4 text-sm text-gray-700";
        userMsgDiv.innerHTML = `<p class="bg-gray-200 px-3 py-2 rounded-md w-fit max-w-full"> ${message}</p>`
        chatBox.appendChild(userMsgDiv)
        chatBox.scrollTop = chatBox.scrollHeight;

        // Mostra "Aguardando resposta..." enquanto a IA processa a resposta.
        const loadingMsg = document.createElement("div");
        loadingMsg.className = "flex gap-3 my-4 text-sm text-gray-700";
        loadingMsg.id = "loading-msg";
        loadingMsg.innerHTML = `<p class="leading-relaxed text-gray-500 break-words whitespace-normal">Aguardando resposta...</p>`;
        chatBox.appendChild(loadingMsg)

        input.value = "";

        try {
            const response = await fetch("/chatbot-resposta/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: JSON.stringify({ mensagem: message })
            });

            const data = await response.json();

            // Substitui a mensagem de "aguardando..." pela resposta real
            loadingMsg.remove();

            if(data.resposta){
                const iaMsgDiv = document.createElement("div");
                iaMsgDiv.className = "flex gap-3 my-4 text-sm text-gray-700";
                iaMsgDiv.innerHTML = `<p class="bg-blue-100 px-3 py-2 rounded-md w-fit max-w-full text-left">${data.resposta}</p>`;
                chatBox.appendChild(iaMsgDiv);
            }else{
                showError("Desculpe, não conseguimos entender a resposta da IA.")
            }

        } catch (error) {
            console.error("Erro ao obter resposta:", error);
            const loadingMsg = document.getElementById(loadingMsgId);
            if (loadingMsg) {
                loadingMsg.innerHTML = `<p class="leading-relaxed text-red-600">Erro ao se conectar. Tente novamente mais tarde.</p>`;
            }
        }

        chatBox.scrollTop = chatBox.scrollHeight;
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
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
