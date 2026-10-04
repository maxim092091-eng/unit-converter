const radios = document.querySelectorAll('input[name="type"]');
const text = document.querySelector("#unit-text");

radios.forEach((radio) => {
  radio.addEventListener("change", () => {
    text.textContent = `Enter the ${radio.value} to convert`;
  });
});
