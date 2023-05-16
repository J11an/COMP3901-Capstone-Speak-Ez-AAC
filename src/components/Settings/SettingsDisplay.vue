<script>
export default {
  props: {
    tts: Object,
    voiceIsOn: Boolean,
    voice: Number,
    vol: Number,
    speed: Number,
    hardness: Number,
  },

  data() {
    return {
      speech: new SpeechSynthesisUtterance(),
      voices: [],
      selectedVoice: this.voice,
      volume: this.vol,
      rate: this.speed,
      pitch: this.hardness,
      toggleSaveSettings: false,
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

        // if (voice.default) {
        //   option.textContent += " — DEFAULT";
        // }

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
      this.$emit("toggleVoice", false);
      window.speechSynthesis.pause();
    },

    cancel() {
      this.$emit("toggleVoice", true);
      window.speechSynthesis.cancel();
    },

    updateSettings() {
      this.toggleSaveSettings = true;
      this.$emit("updateVoiceSettings", [
        this.voices[document.querySelector("#voiceSelect").value],
        this.volume,
        this.rate,
        this.pitch,
      ]);
      this.hideSaveSettings();
    },
    hideSaveSettings() {
      setTimeout(() => {
        this.toggleSaveSettings = false;
      }, 2500);
    },
  },
};
</script>

<template>
  <Transition name="fade" appear>
    <div class="container">
      <h1>Settings</h1>
      <form class="settings-container" @submit.prevent>
        <h3 :class="voiceIsOn ? 'voice-on' : 'voice-off'"></h3>
        <h3 :class="voiceIsOn ? 'voice-on' : 'voice-off'">
          Voice is {{ voiceIsOn ? "On" : "Off" }}
        </h3>
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

        <div class="controls">
          <div>
            <!-- <span id="volume-label" class="ms-2">1</span> -->
            <input
              type="range"
              min="0"
              max="2"
              step="0.1"
              id="volume"
              @input="setVolume()"
              v-model="volume"
              class="vertical"
              orient="vertical"
            />
            <div>
              <label class="form-label">Volume</label>
            </div>
          </div>
          <div>
            <input
              type="range"
              min="0"
              max="2"
              step="0.1"
              id="rate"
              @input="setRate()"
              v-model="rate"
              class="vertical"
              orient="vertical"
            />
            <div>
              <label class="form-label">Rate</label>
              <!-- <span id="rate-label" class="ms-2">1</span> -->
            </div>
          </div>

          <div>
            <input
              type="range"
              min="0"
              max="2"
              step="0.1"
              id="pitch"
              @input="setPitch"
              v-model="pitch"
              class="vertical"
              orient="vertical"
            />
            <div>
              <!-- <span id="pitch-label" class="ms-2">1</span> -->
              <label class="form-label">Pitch</label>
            </div>
          </div>
        </div>
        <br />

        <button @click="updateSettings" class="btn btn-success btn-lg">
          Save Changes
        </button>
      </form>

      <div v-if="toggleSaveSettings">
        <Transition name="modal">
          <div class="modal-mask">
            <div class="modal-container">
              <div class="modal-header">
                <slot name="header">
                  <p id="modal-title">Save Settings</p>
                </slot>
                <button
                  type="button"
                  class="btn-close"
                  data-mdb-dismiss="modal"
                  aria-label="Close"
                  @click="hideSaveSettings"
                ></button>
              </div>
              <div>
                <div class="success-group">
                  <img class="success-wrapper-btn" src="/checked.png" />
                  <p class="form-message">Settings Updated</p>
                </div>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.voice-off {
  color: crimson;
}

.voice-on {
  color: #3a7bd5;
}

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

.controls {
  display: flex;
  flex-direction: row;
  text-align: center;
}

input.vertical {
  -webkit-appearance: slider-vertical;
  writing-mode: bt-lr;
}

.form-message {
  font-size: 26px;
  font-weight: bolder;
  color: #3a7bd5;
}

.success-wrapper-btn {
  width: 150px;
  height: 150px;
}

.success-group {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.modal-container {
  display: flex;
  flex-direction: column;
  width: 50%;
  height: auto;
}

#modal-title {
  font-size: x-large;
  font-weight: bold;
  margin: 0;
}

.modal-body {
  text-align: center;
  justify-content: center;
  align-items: center;
}

@media screen and (max-width: 425px) {
  .modal-container {
    width: fit-content;
    height: fit-content;
}
}
</style>
