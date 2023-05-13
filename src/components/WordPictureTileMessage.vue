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
      return fetch(`/api/get_word_symbol?word=${word}`, {
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
    speak(){
      this.tts.speak(new SpeechSynthesisUtterance(this.word));
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
          <img :src="img" @error="usePlaceholderImg" alt="Image" />
          <div class="card-content">
            <p>{{ word }}</p>
          </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
.container{
  cursor: pointer;
}

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
  margin: 2px;
}

.card img {
  display: block;
  width: 50px;
  height: 50px;
  object-fit: contain;
  margin: 3px;
}

.card-content {
  padding: 0;
  text-align: center;
  font-size: 22px;
}
</style>
