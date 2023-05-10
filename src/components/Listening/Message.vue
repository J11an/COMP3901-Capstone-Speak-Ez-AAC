<script>
export default {
  props:{
    msg: String,
    from: String,
  }
}
</script>

<template>
  <!-- Section for messages -->
  <section v-if="from === 'SPEAKER'" class="speaker-msg">
    <div class="speaker-msg">{{ msg }}</div>
  </section>

  <section v-else class="listener-msg">
    {{ msg }}
  </section>
</template>

<style scoped>
.speaker-msg, .listener-msg{
  font-size: 2vw;
  padding: 1vw;
  border-radius: 25px;
}

.speaker-label{
  margin-left: 20px;
}

.speaker-msg{
  margin-right: auto;
  background-color: #9BB8E3;
}

.listener-msg{
  margin-left: auto;
  background-color: #8EFF9A;
}

</style>