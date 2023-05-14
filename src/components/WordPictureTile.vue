<script>
export default {
  props:{
    id: Number,
    word: String,
    symbol: String,
    partOfSpeech: String
  },
  data(){
    return{
      img: this.symbol,
      backgroundColors: {
        noun:'#5FC3FA',
        noun2 : '#5FC3FA',
        pronoun: '#0DB5FA',
        adjectives: '#DECE1F',
        adjectives2: '#DECE1F',
        adverb: '#6BDE33',
        preposition: '#A143DE',
        conjunction: '#FBF62C',
        articles: 'violet',
        verb: '#33DE66',
        verb2: '#33DE66'
      }
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
  <div class="container">
    <div id="tile">
        <div class="card" :style="this.partOfSpeech ? `background-color:${this.backgroundColors[partOfSpeech]}` : 'background-color:#FF8080'">
          <img :src="img" @error="usePlaceholderImg" alt="Image" draggable="false"/>
          <div class="card-content">
            <p class="word">{{ word }}</p>
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
  width: 170px;
  height: 170px;
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
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin: 3px;
}

.card-content {
  padding: 10px;
  text-align: center;
}

.word{
  letter-spacing: 2px;
  font-weight: bolder;
  font-size: 18px;
}
</style>
