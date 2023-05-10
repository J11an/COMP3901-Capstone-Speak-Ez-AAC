<script>
import Message from "../components/Listening/Message.vue";

export default {
  components: { Message },
  props: {
    messageList: Array,
  },
};
</script>

<template>
  <!-- Messages container at top -->
  <div class="conversation-container" id="con-container">
    <!-- Go through all messages -->

    <div
      class="msg-body-container"
      v-for="message in messageList"
      v-bind:key="message.id"
    >
      <Message :msg="message.msg" :from="message.from" />
    </div>
  </div>
</template>

<style>
.conversation-container {
  /*border: solid red 1px;*/
  margin: 10px;
  padding: 10px;
  overflow: auto;
  min-height: 80vh;
  max-height: 80vh;

  @media (max-height: 1040px) {
    min-height: 78vh;
    max-height: 78vh;
  }

  @media (max-height: 876px) {
    min-height: 73vh;
    max-height: 73vh;
  }

  @media (max-height: 738px) {
    min-height: 69vh;
    max-height: 69vh;
  }
}

.msg-body-container {
  display: flex;
  margin: 1vw;
}
</style>
