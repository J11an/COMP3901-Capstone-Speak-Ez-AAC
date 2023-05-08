<script>
//import { ref } from 'vue';
export default {
  props: {
    msgList: Array,
  },
  data() {
    return {
      currentSentence:"",
    };
  },
  methods:{
    handleBackspace(){
      const sentence = this.currentSentence;
      this.currentSentence = sentence.substring(0,sentence.length-1);
    },
    handleClear(){
      this.currentSentence = "";
    },
    sendMessage(){
      const msgs = this.msgList;
      const sentence = this.currentSentence;
      msgs.push({
          id: msgs[msgs.length-1].id+1,
          msg:sentence,
          from: "LISTENER",
          label: 0
      })
      this.handleClear();
    }


  }
};

</script>


<template>
  <div class="container-fluid msg-container">
    <!--<div class="msg-display"></div>-->
    <input id="input" class="msg-display" v-on:keyup.enter="sendMessage" v-model="currentSentence"/>
      <!--<input type="text" class="mt-4 msg-bar ml-5" />-->
      <div class="btn-group btn-group-md options">
        <button class="btn "  @click="handleBackspace"><img src="/Backspace.png" alt="Backspace Icon" /></button>
        <button class="btn " @click="handleClear"><img src="/clear.png" alt="Clear Icon" /></button>
        <button class="btn " @click="somefunc"><img src="/SpeakerIcon.png" alt="Speaker Icon" /></button>
        <!---<img src="/Backspace.png" alt="Backspace Icon" />
        <img src="/SpeakerIcon.png" alt="Speaker Icon" />-->
      </div>
  </div>
</template>


<style>
.msg-container {
  width:100%;
  height: 100px; /*maybe the size of whatver the title is set to here*/
  margin-top:10px;
  padding: 10px;
  display:flex;
  flex-direction: row;
}

.msg-display{
  height: 100%;
  width: 90%;
  display: flex;
  background: #ffffff;
  border: 2px solid black;
  border-radius: 20px;
  font-size: 2vw;
}

.options{
  display: flex;
  min-width: fit-content;
}

img {
  width: 71px;
  height: 71px;
}
</style>
