<script>
export default {
  data() {
    return {};
  },
};
</script>


<template>
  <div class="container-fluid msg-container">
    <div class="msg-display"></div>
      <!--<input type="text" class="mt-4 msg-bar ml-5" />-->
      <div class="btn-group btn-group-md options">
        <button class="btn "  @click="somefunc"><img src="/Backspace.png" alt="Backspace Icon" /></button>
        <button class="btn " @click="somefunc"><img src="/clear.png" alt="Clear Icon" /></button>
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
  margin:10px;
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
