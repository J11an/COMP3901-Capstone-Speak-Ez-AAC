<script>
export default {
  props: {
    tts: Object,
  },

  data() {
    return {
      speech: new SpeechSynthesisUtterance(),
      voices: [],
      selectedVoice: "",
    };
  },
  mounted() {
    this.populateVoiceList();
  },

  methods: {
    populateVoiceList() {
      if (typeof speechSynthesis === "undefined") {
        return;
      }

      this.voices = speechSynthesis.getVoices();

      this.voices.forEach((voice, i) => {
        const option = new Option(`${voice.name} (${voice.lang})`, i);

        if (voice.default) {
          option.textContent += " — DEFAULT";
        }

        option.setAttribute("data-lang", voice.lang);
        option.setAttribute("data-name", voice.name);
        document.getElementById("voiceSelect").options[i] = option;
      });
    },

    setVoice() {
      console.log("voice", document.querySelector("#voiceSelect").value);
      this.speech.voice =
        this.voices[document.querySelector("#voiceSelect").value];
      console.log(this.speech.voice);
    },

    setVolume() {
      this.volume = document.querySelector("#volume").value;
      this.speech.volume = this.volume;
      console.log(this.speech.volume);
      document.querySelector("#volume-label").innerHTML = this.volume;
    },

    setRate() {
      this.rate = document.querySelector("#rate").value;
      this.speech.rate = this.rate;
      console.log(this.speech.rate);
      document.querySelector("#rate-label").innerHTML = this.rate;
    },

    setPitch() {
      this.pitch = document.querySelector("#pitch").value;
      this.speech.pitch = this.pitch;
      document.querySelector("#pitch-label").innerHTML = this.pitch;
    },

    play() {
      this.speech.text = document.querySelector("textarea").value;
      window.speechSynthesis.speak(this.speech);
      console.log(this.speech);
      this.speech.voice;
    },

    pause() {
      window.speechSynthesis.pause();
    },

    cancel() {
      window.speechSynthesis.cancel();
    },

    updateSettings() {
      this.tts = window.speechSynthesis;
    },
  },
};
</script>

<template>
  <div class="container">
    <h1>Settings</h1>
    <br />

    <form class="settings-container" @submit.prevent>
      <label class="form-label">Select voice</label>
      <select
        id="voiceSelect"
        class="form-select"
        v-model="selectedVoice"
        @change="setVoice()"
      ></select>
      <br />
      <label class="form-label">Type here to hear the voice selected</label>
      <textarea
        rows="3"
        class="form-control"
        placeholder="Type here to hear the voice selected"
      ></textarea>
      <div class="btn-group">
        <button id="play" class="btn btn-primary mt-5 me-3" @click="play">
          Speak
        </button>
        <button id="pause" class="btn btn-primary mt-5 me-3" @click="pause">
          Pause
        </button>
        <button id="stop" class="btn btn-primary mt-5 me-3" @click="cancel">
          Stop
        </button>
      </div>

      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        id="volume"
        @input="setVolume()"
        class="slider"
      />
      <span id="volume-label" class="ms-2">1</span>
      <label class="form-label">Volume</label>

      <input
        type="range"
        min="0"
        max="1"
        value="1"
        step="0.1"
        id="rate"
        @input="setRate()"
        class="slider"
      />
      <span id="rate-label" class="ms-2">1</span>
      <label class="form-label">Rate</label>

      <input
        type="range"
        min="0"
        max="1"
        value="1"
        step="0.1"
        id="pitch"
        @input="setPitch"
        class="slider"
      />
      <span id="pitch-label" class="ms-2">1</span>
      <label class="form-label">Pitch</label>
      <br />

      <button @click="updateSettings" class="btn btn-success btn-lg">
        Save Changes
      </button>
    </form>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.settings-container {
  display: flex;
  width: 70%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.btn-group {
  margin-bottom: 30px;
  margin-top: -30px;
}

.ms-2 {
  font-size: x-large;
}
</style>
