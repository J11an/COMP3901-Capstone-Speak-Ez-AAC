<script setup>
import { ref, onMounted } from "vue";
import WordPictureTile from "./WordPictureTile.vue";

//let words = ref([]);
let adjectives = ref([]);
let nouns = ref([]);
let articles = ref([]);
let verbs = ref([]);

function fetchGrid() {
  fetch("api/inital_tree_setting", {
    method: "GET",
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      //words.value = data;
      adjectives.value = data.adjectives;
      articles.value = data.articles;
      nouns.value = data.noun;
      verbs.value = data.verb;
      //console.log(nouns);
    })
    .catch(function (error) {
      console.log(error);
      //console.log("test");
    });
}

onMounted(() => {
  fetchGrid();
});
</script>

<template>
  <div class="container">
    <div class="row align-items-start">
    <div class="col-sm">
      <!--<div v-for="article in articles" class="col" >
        <WordPictureTile :word=article />
      </div>-->
      <div v-for="noun in nouns.slice(0,4)" class="col-sm">
        <WordPictureTile :word=noun />
      </div>
    </div>
    
    <div class="col-sm">
      <div v-for="noun in nouns.slice(0,4)" class="col-sm">
        <WordPictureTile :word=noun />
      </div>
    </div>
    <div class="col-sm">
      <div v-for="verb in verbs.slice(0,4)"  class="col-sm" >
        <WordPictureTile :word=verb />
      </div>
    </div>
    <div class="col-sm">
      <div v-for="adjective in adjectives.slice(0,4)" class="col-sm" >
        <WordPictureTile :word=adjective />
      </div>
    </div>
  </div>
</div>


</template>

<style></style>
