<script setup>
import { ref } from "vue";
let tts = window.speechSynthesis;

//let voice = tts.getVoices().filter(function (voice) {return voice.lang === 'en';})[0];
//const word = ref(document.querySelector(".card-content > p"))

const props = defineProps({
  word: ref(""),
  imageUrl: ref(""),
});

function addWord() {
  const textbox = document.getElementById("message");
  let child = ref.wordTitle;

  const tile = document.createElement("div");
  tile.setAttribute("class", "card");
  tile.setAttribute("id", "tile");

  const img = document.createElement("img");
  img.setAttribute("src", "/HelpIcon.png");
  img.setAttribute("alt", "Image");
  tile.appendChild(img);

  const cardContent = document.createElement("div");
  cardContent.setAttribute("id", "word");

  const p = document.createElement("p");
  p.textContent = props.word;
  cardContent.appendChild(p);

  tile.appendChild(cardContent);

  textbox.appendChild(tile);
  var utterance = new SpeechSynthesisUtterance(p.textContent);
  tts.speak(utterance);
}
</script>

<template>
  <!--<div class="card aac-card mx-auto" style="width: 18rem">
    <img class="card-img-top img-orientation" :src="imageUrl" alt="" />
    <p class="card-text tile-text">{{ word }}</p>
  </div>-->
  <div class="container">
  <div id="tile" >
    <button :word="word" :image-url="imageUrl" class="card" @click="addWord">
      <img src="/HelpIcon.png" alt="Image" />
      <div class="card-content">
        <p>{{ props.word }}</p>
      </div>
    </button>
  </div>
  </div>
</template>

<style>
/*.img-orientation {
  width: 50px;
  height: 50px;
  justify-self: center;
}

.tile-text {
  font-family: "Thabit";
  font-style: normal;
  font-weight: bold;
  font-size: 32px;
  line-height: 100px;
  text-align: center;
}

.aac-card {
  background: linear-gradient(
      0deg,
      rgba(103, 80, 164, 0.08),
      rgba(103, 80, 164, 0.08)
    ),
    #fffbfe;
  border: 5px solid #000000;
  box-shadow: 0px 2px 6px 2px rgba(0, 0, 0, 0.15);
  border-radius: 48px;
  min-width: 10px;
  min-height: 100px;
  margin: 10px;
}

.aac-card:hover {
  transform: scale(1.01);
  transition: 100ms;
}*/

.card {
  width: 100px;
  height: 100px;
  /*background: linear-gradient(
      0deg,
      rgba(103, 80, 164, 0.08),
      rgba(103, 80, 164, 0.08)
    ),
    #fffbfe;*/
  border: 1px solid #000000;
  box-shadow: 0px 2px 4px 2px rgba(0, 0, 0, 0.15);
  border-radius: 10px;
  overflow: hidden;
  justify-self: center;
  align-items: center;
  margin-bottom: 15px;
}

.card img {
  display: block;
  width: 70%;
  height: 40%;
  object-fit: contain;
  margin: 3px;
}

.card-content {
  padding: 10px;
  text-align: center;
}
</style>
