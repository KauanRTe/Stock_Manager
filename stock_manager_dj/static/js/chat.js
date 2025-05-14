document.addEventListener("DOMContentLoaded", function() {
    const sendBtn = document.getElementById("send-btn");
    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-messages");

    sendBtn.addEventListener("click", async function(e) {
        e.preventDefault();

        const message = input.value.trim();
        if (!message) return;

        // Mostra a mensagem do usuário
        chatBox.innerHTML += `
            <div class="flex justify-end gap-3 my-4 text-sm text-gray-700">
                <p class="w-auto px-4 py-2 bg-gray-200 rounded-md leading-relaxed">${message}</p>
            </div>
        `;

        input.value = "";

        // Mostra "Aguardando resposta..." antes da resposta real
        const loadingMsgId = `loading-${Date.now()}`;
        chatBox.innerHTML += `
            <div id="${loadingMsgId}" class="flex gap-3 my-4 text-sm text-gray-700">
                <p class="leading-relaxed italic text-gray-500">Aguardando resposta...</p>
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

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
            const respostaFinal = data.resposta;
            const loadingMsg = document.getElementById(loadingMsgId);

            if (respostaFinal) {
                loadingMsg.innerHTML = `<p class="leading-relaxed">${respostaFinal}</p>`;
            } else {
                loadingMsg.innerHTML = `<p class="leading-relaxed text-red-600">Desculpe, não conseguimos entender a resposta da IA.</p>`;
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
