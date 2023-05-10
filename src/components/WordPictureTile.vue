<script>
export default {
  props:{
    id: Number,
    word: String,
    symbolURL: String,
    partOfSpeech: String
  },
  data(){
    return{

    }
  }
}
</script>

<template>
  <div class="container">
    <div id="tile">
        <div class="card">
          <img src="/HelpIcon.png" alt="Image" />
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
