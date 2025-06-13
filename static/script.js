function typeText(element, text, delay = 30) {
  let index = 0;
  const interval = setInterval(() => {
    element.innerHTML += text[index];
    index++;
    if (index >= text.length) clearInterval(interval);
  }, delay);
}

function sendMessage() {
  const userInput = document.getElementById("userInput");
  const message = userInput.value.trim();
  if (!message) return;

  const chatbox = document.getElementById("chatbox");

  // Display user's message
  chatbox.innerHTML += `<div class="message user">${message}</div>`;
  userInput.value = "";
  chatbox.scrollTop = chatbox.scrollHeight;

  // Display "Typing..." indicator
  const botDiv = document.createElement("div");
  botDiv.className = "message bot";
  botDiv.innerHTML = "Typing...";
  chatbox.appendChild(botDiv);
  chatbox.scrollTop = chatbox.scrollHeight;

  // Send to backend
  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  })
    .then(response => response.json())
    .then(data => {
      botDiv.innerHTML = ""; // Clear the "Typing..." text
      typeText(botDiv, data.response); // Simulate typing
      chatbox.scrollTop = chatbox.scrollHeight;
    })
    .catch(error => {
      botDiv.innerHTML = "Error: " + error.message;
    });
}

// Allow sending message with Enter key
document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("userInput");
  input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      sendMessage();
    }
  });
});
