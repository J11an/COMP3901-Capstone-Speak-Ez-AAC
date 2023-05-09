<script setup>
import { ref } from "vue";
import WordPictureTile from "./WordPictureTile.vue";

const searchTerm = ref("");
const results = ref([]);

function searchWord() {
  fetch(`api/search/${searchTerm.value}`, {
    method: "POST",
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      //console.log(data);
      results.value = data;
      //console.log(results);
      /*let board = document.getElementById('board');
      board.style.display = "none"*/
    })
    .catch(function (error) {
      console.log(error);
      //console.log("test");
    });
}

function handleClear(){
      searchTerm.value = "";
      results.value="";
      /*let board = document.getElementById('board');
      board.style.display = "flex"*/
}
</script>

<template>
  <div class="container">
    <label for="search">Enter a word to search for here: </label>
    <input name="search" v-model="searchTerm" type="text" placeholder="Search here" @keyup.enter="searchWord"/>
    <span><button id="clear" class="btn" @click="handleClear"><img src="/clear.png" alt="Clear Icon" /> Clear search</button></span>
    <div class="search-results">
      <WordPictureTile :word="result" v-for="result in results" :key="result.id">{{ result }}</WordPictureTile>
    </div>
   
  </div>
</template>

<style>
.search-results{
  display: flex;
  flex-direction: row;
}

#clear img{
  max-width: 100%;
  height:50px;
}

</style>