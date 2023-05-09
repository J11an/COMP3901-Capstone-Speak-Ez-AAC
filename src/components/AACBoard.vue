<script setup>
import { ref, onMounted } from "vue";
import WordPictureTile from "./WordPictureTile.vue";

//let words = ref([]);
let columns = ref([]);
let toggleVal = ref(false);

function fetchGrid() {
  fetch("api/inital_tree_setting", {
    method: "GET",
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      //console.log(data);
      columns.value = {
        pronoun: data.pronoun,
        noun: data.noun,
        verb: data.verb,
        adjective: data.adjectives,
        article: data.article,
      };
    })
    .catch(function (error) {
      console.log(error);
      //console.log("test");
    });
}

/*function toggleSwitch(){
      let toggleValue;
      toggleValue.value = !toggleVal.value;
    }*/

onMounted(() => {
  fetchGrid();
  /*columns.value = {
      "noun" : [1,1,1,1],
      "verb" : [2,2,2,2],
      "adjective" : [3,3,3,3],
      "article" : [4,4,4,4]
    }*/
});
</script>

<template>
  <div id="board" class="container">
    <div v-if="!toggleVal" class="d-flex flex-wrap justify-content-between mt-3">
      <div v-for="(value, key) in columns" :class="key" :value="value">
        <div v-for="word in value">
          <WordPictureTile image-url="/HelpIcon.png" :word="word" />
        </div>
      </div>
    </div>
  </div>
  <!--<div class="container board">
    <div class="row align-items-start">
    <div class="col-sm">
    <div v-for="article in articles" class="col" >
        <WordPictureTile :word=article />
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
</div>-->
</template>

<style>
div .pronoun button {
  background: blue;
}

div .noun button {
  background: rgb(216, 102, 102);
}

div .article button {
  background: rgb(173, 180, 40);
}

div .adjective button {
  background: rgb(167, 136, 12);
}

div .verb button {
  background: rgb(11, 115, 27);
}
</style>
