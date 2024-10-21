window.onload = function () {
  const messageList = document.getElementById("messageList");

  if (messages.length > 0) {
    messages.forEach(function (message) {
      const li = document.createElement("li");
      li.textContent = message;
      messageList.appendChild(li);
    });
    openModal();
  }
};

function openModal() {
  document.getElementById("messageModal").style.display = "block";
}

function closeModal() {
  document.getElementById("messageModal").style.display = "none";
}

window.onclick = function (event) {
  if (event.target == document.getElementById("messageModal")) {
    closeModal();
  }
};
