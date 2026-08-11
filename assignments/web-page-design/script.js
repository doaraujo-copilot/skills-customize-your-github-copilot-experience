const button = document.getElementById("click-button");
const message = document.getElementById("message");

button.addEventListener("click", () => {
  message.textContent = "Thanks for clicking!";
});
