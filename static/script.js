  function sendMessage() {
    const userInput = document.getElementById("userInput");
    const message = userInput.value.trim();

    if (!message) return;

    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div class="message user">${message}</div>`;
    userInput.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: message })
    })
      .then(response => response.json())
      .then(data => {
        chatbox.innerHTML += `<div class="message bot">${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
      })
      .catch(error => {
        chatbox.innerHTML += `<div class="message bot">Error: ${error}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
      });
  }

  // 👇 Trigger sendMessage() when Enter is pressed in input field
  document.addEventListener("DOMContentLoaded", function () {
    const inputField = document.getElementById("userInput");
    inputField.addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        event.preventDefault(); // Prevent form submission if inside a form
        sendMessage();
      }
    });
  });