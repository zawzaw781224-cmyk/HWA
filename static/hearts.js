setInterval(() => {
  const heart = document.createElement("div");
  heart.textContent = "💗";
  heart.style.position = "fixed";
  heart.style.left = Math.random() * 100 + "vw";
  heart.style.bottom = "0";
  heart.style.fontSize = "28px";
  heart.style.animation="floatUp 4s linear";
  document.body.appendChild(heart);

  setTimeout(() => heart.remove(), 4000);
}, 400);