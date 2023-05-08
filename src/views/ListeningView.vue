<script>
import MessageBarListening from "../components/MessageBarListening.vue";

export default {
  components: { MessageBarListening },

  data() {
    return {
      /*
      * Message Format
      * msg - The contents of the message
      * from - The author of the message, either the listener or speaker
      * */
      messageList: [],
      speakerList: []
    };
  },

  methods: {
    /**
     * Function to scroll to the bottom of the page on a new message added
     */
    scrollToEnd() {
    },
  },

  mounted() {
    const testFromArr = ["SPEAKER","LISTENER"];
    this.speakerList = ["Speaker1", "Speaker2"];
    for (let i = 0; i < 5; i++) {
        const from = testFromArr[Math.round(Math.random())];
        this.messageList.push({
          id: i,
          msg:`This is a test message from the ${from}`,
          from: from,
          label: Math.round(Math.random())
        })
    }
  }



};

</script>

<template>
  <div class="listening-container">

    <!-- Messages container at top -->
    <div class="conversation-container">

      <!-- Go through all messages -->
      <div class="msg-body-container" v-for="message in messageList" v-bind:key="message.id">

        <!-- Section for messages -->
        <section v-if="message.from === 'SPEAKER'" class="speaker-msg">
          <div class="speaker-label">{{ speakerList[message.label] }}</div>
          <div class="speaker-msg">{{ message.msg }}</div>
        </section>

        <section v-else class="listener-msg">
          {{ message.msg }}
        </section>

      </div>

      <div id="anchor"></div>

    </div>


    <!-- Message Bar at Bottom -->
    <MessageBarListening :msg-list="messageList" />
  </div>
</template>

<style>
.conversation-container{
  /*border: solid red 1px;*/
  margin: 10px;
  padding: 10px;
  overflow-anchor: none;
  overflow: scroll;
  min-height: 80vh;
  max-height: 80vh;

  @media(max-height:1040px){
    min-height: 78vh;
    max-height: 78vh;
  }

  @media(max-height:876px){
    min-height: 73vh;
    max-height: 73vh;
  }

  @media(max-height:738px){
    min-height: 69vh;
    max-height: 69vh;
  }

}

#anchor{
  overflow-anchor: auto;
  height: 1px;
}

.msg-body-container{
  display: flex;
  margin: 1vw;
}

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
