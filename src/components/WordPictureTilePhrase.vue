<script>
export default {
  props:{
    id: Number,
    word: String,
    symbol: String,
    partOfSpeech: String,
    tts: Object
  },
  data(){
    return{
      img: this.symbol
    }
  },
  methods : {
    fetchSearchedWordSymbol(word) {
      return fetch(`/api/get_word_symbol?word=${word.toLowerCase()}`, {
        method: "GET",
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          return data
        })
        .catch(function (error) {
          return error
        });
    },
    findSymbol(){
      this.fetchSearchedWordSymbol(this.word).then((data)=>{this.img = data.symbol || '/HelpIcon.png'})
    },
    usePlaceholderImg(){
      this.img = '/HelpIcon.png';
    }
  },
  mounted() {
    if (!this.img){
      this.findSymbol()
    }
  }
}
</script>

<template>
  <div class="container" @click="speak">
    <div id="tile">
        <div class="card">
          <div class="card-content">
            <img :src="img" @error="usePlaceholderImg" alt="Image" />
            <p>{{ word.toUpperCase() }}</p>
          </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
.container{
  cursor: pointer;
}
.container:hover{
  filter: sepia(0.60);
}

.card {
  width: 200px;
  height: 200px;
  /*background: linear-gradient(
      0deg,
      rgba(103, 80, 164, 0.08),
      rgba(103, 80, 164, 0.08)
    ),
    #fffbfe;*/
  border-radius: 10px;
  border: 0;
  overflow: hidden;
  justify-self: center;
  align-items: center;
  margin: 2px;
  background-image: url("/folder.png");
  background-repeat: no-repeat;
  background-size: 200px 200px;
}

.card img {
  display: block;
  width: 65px;
  height: 65px;
  object-fit: contain;
  margin: 3px;
}

.card-content {
  margin-top: auto;
  padding: 0;
  text-align: center;
  display: inline-block;
  overflow-wrap: break-word;
}

p{
  font-size: 18px;
  word-break: break-word;
}
</style>
