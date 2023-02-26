<template>

    <div class="v217_2338">
        <div class="v307_2069"></div>
        <div class="v217_2339"></div>
        <div class="BWHelpIcon"></div>
        <span class="v217_2342">Age</span>
        <div class="v217_2351"></div>
        <div class="name"></div>
        <span class="v217_2363">Enter Age</span>
        <div class="v217_2365"></div>
        <span class="v217_2366">Enter Age</span>
        <div class="v217_2374"></div>
        <div class="v284_7711">
            <div class="v217_2377"></div>
            <div class="v217_2378"></div>
            <div class="v217_2379"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <span class="v522_4233" @click="pad1">1</span>
            <div class="name"> </div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="Backspace"></div>
            <div class="name"></div>
            <div class="name"></div>
            <div class="name"></div>
            <span class="v522_4241" @click="pad7">7</span>
            <span class="v522_4242" @click="pad8">8</span>
            <span class="v522_4243" @click="pad9">9</span>
        </div>
        <div class="v261_18767">
            <div class="v261_18768"></div>
            <div class="v261_18769"></div>
            <div class="v261_18770"></div>
            <div class="v261_18771"></div>
            <div class="v261_18772"></div>
            <div class="v261_18773"></div>
        </div>
        <span class="v307_2067" @click="back">Back</span>
        <span class="v307_2068" @click="next">Next</span>
        <div class="v472_3642">
            <div class="v472_3643">
                <div class="v472_3644"></div>
                <span class="v472_3645" @click="speaking">Speaking</span>
                <div class="v472_3646">
                    <div class="SpeakingScreen"></div>
                </div>
            </div>
            <div class="v472_3648">
                <div class="v472_3649"></div>
                <div class="TypingScreen"></div>
                <span class="v472_3651" @click="typing">Typing</span>
            </div>
            <div class="v472_3652">
                <div class="v472_3653"></div>
                <div class="ListeningScreen"></div>
                <span class="v472_3655" @click="listening">Listening</span>
            </div>
            <div class="v472_3656">
                <div class="v472_3657"></div>
                <span class="v472_3658" @click="savedprhases">Saved Phrases </span>
                <div class="SavedPhrasesScreen"></div>
            </div>
            <div class="v472_3660">
              <div class="v472_3661"></div>
              <span class="v472_3662" @click="categories">Categories</span>
              <div class="Categories"></div>
            </div>
            <div class="v472_3664">
                <div class="v472_3665"></div>
                <div class="LearningScreen"><div>
                <span class="v472_3667" @click="learning">Learning</span>
            </div>
            <div class="v472_3668">
                <div class="v472_3669"></div>
                <div class="ProfileIcon"></div>
                <span class="v472_3671">Profile </span>
            </div>
            <div class="v472_3672">
                <div class="v472_3673"> </div>
                <div class="SettingIcon"> </div>
                <span class="v472_3675" @click="setting">Settings </span>
            </div>
            <div class="v472_3676">
                <div class="v472_3677"></div>
                <div class="HelpIcon"></div>
                <span class="v472_3679" @click="help">Help</span>
            </div>
            <div class="name"></div>
            <div class="v472_3681">
                <div class="v472_3682"></div>

                <span class="v472_3683" @click="newedit">New/Edit Phrases</span>
                <div class="NewEditScreen"></div>
            </div>
        </div>
        <div class="name"></div>
        <div class="name"></div>
        <span class="v522_4230" @click="done">Done</span>
        <span class="v522_4236" @click="pad2">2</span>
        <span class="v522_4237" @click="pad3">3</span>
        <span class="v522_4238" @click="pad4">4</span>
        <span class="v522_4239" @click="pad5">5</span>
        <span class="v522_4240" @click="pad6">6</span>
        <span class="v522_4244" @click="pad0">0</span>
        <div class="name"></div>
    </div>

</template>

<script>

import router from "../router";
export default({
  data() {
    return{
      csrf_token: 'token',
      errors:[],
      message: ''
     

    }
  },
  created(){
    this.getCsrToken();    

  },
  methods:{
    AddAge(){
      let self= this
      fetch("api/adduser/2",{
        method:'POST',
        body:form_data ,
        errors:[],
        message: '',
        headers:{
          'X-CSRFToken': this.csrf_token
        }
      })
    }

  }
})

</script>

<style>

* {
  box-sizing: border-box;
}
body {
  font-size: 14px;
}
.v217_2338 {
  width: 100%;
  height: 960px;
  background: rgba(255,255,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  overflow: hidden;
}
.v307_2069 {
  width: 216px;
  height: 121px;
  background: rgba(217,217,217,1);
  opacity: 1;
  position: absolute;
  top: 862px;
  left: 55px;
}
.v217_2339 {
  width: 100%;
  height: 91px;
  background: rgba(255,255,255,0.9100000262260437);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 14px;
  box-shadow: 0px 8px 24px rgba(0.5843137502670288, 0.615686297416687, 0.6470588445663452, 0.20000000298023224);
}
.BWHelpIcon {
  width: 143px;
  height: 151px;
  background: url("../public/BWHelpIcon.png");
  opacity: 1;
  position: absolute;
  top: 141px;
  left: 1796px;
}
.v217_2342 {
  width: 64px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 23px;
  left: 70px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 36px;
  opacity: 1;
  text-align: center;
}
.v217_2351 {
  width: 100%;
  height: 172px;
  background: rgba(103,80,164,0.11999999731779099);
  opacity: 1;
  position: absolute;
  top: 126px;
  left: 223px;
  border-top-left-radius: 35px;
  border-top-right-radius: 35px;
  border-bottom-left-radius: 35px;
  border-bottom-right-radius: 35px;
  overflow: hidden;
}
.name {
  color: #fff;
}
.v217_2363 {
  width: 543px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 139px;
  left: 452px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 36px;
  opacity: 1;
  text-align: center;
}
.v217_2365 {
  width: 687px;
  height: 64px;
  background: rgba(217,217,217,1);
  opacity: 1;
  position: absolute;
  top: 206px;
  left: 368px;
  border-top-left-radius: 35px;
  border-top-right-radius: 35px;
  border-bottom-left-radius: 35px;
  border-bottom-right-radius: 35px;
  overflow: hidden;
}
.v217_2366 {
  width: 217px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 222px;
  left: 411px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 34px;
  opacity: 1;
  text-align: left;
}
.v217_2374 {
  width: 216px;
  height: 121px;
  background: rgba(217,217,217,1);
  opacity: 1;
  position: absolute;
  top: 860px;
  left: 1280px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-left-radius: 50px;
  border-bottom-right-radius: 50px;
  overflow: hidden;
}
.v284_7711 {
  width: 736px;
  height: 530px;
  background: url("../public/v284_7711.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 316px;
  left: 368px;
  overflow: hidden;
}
.v217_2377 {
  width: 736px;
  height: 530px;
  background: rgba(217,217,217,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  border-top-left-radius: 35px;
  border-top-right-radius: 35px;
  border-bottom-left-radius: 35px;
  border-bottom-right-radius: 35px;
  overflow: hidden;
}
.v217_2378 {
  width: 100px;
  height: 100px;
  background: rgba(217,217,217,1);
  opacity: 1;
  position: absolute;
  top: 122px;
  left: 58px;
  overflow: hidden;
}
.v217_2379 {
  width: 100px;
  height: 100px;
  background: rgba(217,217,217,1);
  opacity: 1;
  position: absolute;
  top: 122px;
  left: 58px;
  overflow: hidden;
}

.v522_4233 {
  width: 18px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 60px;
  left: 162px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.Backspace {
  width: 71px;
  height: 71px;
  background: url("../public/Backspace.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 431px;
  left: 136px;
  overflow: hidden;
}

.v522_4241 {
  width: 21px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 309px;
  left: 162px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4242 {
  width: 24px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 320px;
  left: 356px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4243 {
  width: 23px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 309px;
  left: 557px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v261_18767 {
  width: 100%;
  height: 36px;
  background: url("../public/v261_18767.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  margin: 4px;
  opacity: 1;
  position: absolute;
  top: 921px;
  left: 224px;
  overflow: hidden;
}
.v261_18768 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18769 {
  width: 200px;
  height: 20px;
  background: rgba(71,177,255,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 204px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18770 {
  width: 200px;
  height: 20px;
  background: rgba(198,211,234,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 408px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18771 {
  width: 200px;
  height: 20px;
  background: rgba(199,211,235,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 612px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18772 {
  width: 200px;
  height: 20px;
  background: rgba(198,211,234,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 816px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v261_18773 {
  width: 200px;
  height: 20px;
  background: rgba(198,211,234,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 612px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  overflow: hidden;
}
.v307_2067 {
  width: 107px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 879px;
  left: 19px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 48px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v307_2068 {
  width: 102px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 879px;
  left: 1314px;
  font-family: DM Sans;
  font-weight: Regular;
  font-size: 48px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v472_3642 {
  width: 100%;
  height: 92px;
  background: rgba(255,255,255,1);
  opacity: 1;
  position: absolute;
  top: 1px;
  left: 214px;
  overflow: hidden;
}
.v472_3643 {
  width: 120px;
  height: 68px;
  background: url("../public/v472_3643.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 12px;
  left: 14px;
  overflow: hidden;
}
.v472_3644 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 20px;
}
.v472_3645 {
  width: 120px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 50px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v472_3646 {
  width: 40px;
  height: 48px;
  background: url("../public/v472_3646.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 40px;
  overflow: hidden;
}
.SpeakingScreen {
  width: 40px;
  height: 48px;
  background: url("../public/SpeakingScreen.png");
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
}
.v472_3648 {
  width: 78px;
  height: 67px;
  background: url("../public/v472_3648.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 155px;
  overflow: hidden;
}
.v472_3649 {
  width: 78px;
  height: 67px;
  background: linear-gradient(rgba(47,224,248,1), rgba(47,176,248,1));
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 0px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
  overflow: hidden;
}
.TypingScreen {
  width: 39px;
  height: 40px;
  background: url("../public/TypingScreen.png");
  opacity: 1;
  position: absolute;
  top: 5px;
  left: 19px;
}
.v472_3651 {
  width: 69px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 47px;
  left: 4px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v472_3652 {
  width: 162px;
  height: 68px;
  background: url("../public/v472_3652.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 10px;
  left: 230px;
  overflow: hidden;
}
.v472_3653 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 40px;
}
.ListeningScreen {
  width: 41px;
  height: 43px;
  background: url("../public/ListeningScreen.png");
  opacity: 1;
  position: absolute;
  top: 5px;
  left: 60px;
}
.v472_3655 {
  width: 162px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 48px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v472_3656 {
  width: 160px;
  height: 68px;
  background: url("../public/v472_3656.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 473px;
  overflow: hidden;
}
.v472_3657 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 40px;
}
.v472_3658 {
  width: 160px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 47px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 11px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.SavedPhrasesScreen {
  width: 38px;
  height: 44px;
  background: url("../public/SavedPhrasesScreen.png");
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 61px;
}
.v472_3660 {
  width: 298px;
  height: 68px;
  background: url("../public/v472_3660.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 508px;
  overflow: hidden;
}
.v472_3661 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 110px;
}
.v472_3662 {
  width: 298px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 45px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.Categories {
  width: 41px;
  height: 45px;
  background: url("../public/Categories.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 4px;
  left: 128px;
  overflow: hidden;
}
.v472_3664 {
  width: 163px;
  height: 69px;
  background: url("../public/v472_3664.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 10px;
  left: 687px;
  overflow: hidden;
}
.v472_3665 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 40px;
}
.LearningScreen {
  width: 39px;
  height: 45px;
  background: url("../public/LearningScreen.png");
  opacity: 1;
  position: absolute;
  top: 2px;
  left: 59px;
}
.v472_3667 {
  width: 163px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 42px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v472_3668 {
  width: 163px;
  height: 72px;
  background: url("../public/v472_3668.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 10px;
  left: 808px;
  overflow: hidden;
}
.v472_3669 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 42px;
}
.ProfileIcon {
  width: 32px;
  height: 40px;
  background: url("../public/ProfileIcon.png");
  opacity: 1;
  position: absolute;
  top: 3px;
  left: 65px;
}
.v472_3671 {
  width: 163px;
  color: url("../public/v472_3671.png");
  position: absolute;
  top: 45px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
}
.v472_3672 {
  width: 164px;
  height: 70px;
  background: url("../public/v472_3672.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 972px;
  overflow: hidden;
}
.v472_3673 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 46px;
}
.SettingIcon {
  width: 40px;
  height: 40px;
  background: url("../public/SettingIcon.png");
  opacity: 1;
  position: absolute;
  top: 5px;
  left: 61px;
}
.v472_3675 {
  width: 164px;
  color: url("../public/v472_3675.png");
  position: absolute;
  top: 45px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.v472_3676 {
  width: 163px;
  height: 71px;
  background: url("../public/v472_3676.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 11px;
  left: 1080px;
  overflow: hidden;
}
.v472_3677 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 43px;
}
.HelpIcon {
  width: 36px;
  height: 36px;
  background: url("../public/HelpIcon.png");
  opacity: 1;
  position: absolute;
  top: 8px;
  left: 64px;
}
.v472_3679 {
  width: 163px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 44px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 12px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}

.v472_3681 {
  width: 160px;
  height: 68px;
  background: url("../public/v472_3681.png");
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  opacity: 1;
  position: absolute;
  top: 12px;
  left: 354px;
  overflow: hidden;
}
.v472_3682 {
  width: 78px;
  height: 68px;
  background: rgba(151,240,252,1);
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 40px;
}
.v472_3683 {
  width: 160px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 47px;
  left: 0px;
  font-family: Inter;
  font-weight: Bold;
  font-size: 10px;
  opacity: 1;
  text-align: center;
  cursor: pointer;
}
.NewEditScreen {
  width: 42px;
  height: 49px;
  background: url("../public/NewEditScreen.png");
  opacity: 1;
  position: absolute;
  top: 0px;
  left: 64px;
}

.v522_4230 {
  width: 95px;
  color: rgba(255,255,255,1);
  position: absolute;
  top: 761px;
  left: 886px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4236 {
  width: 23px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 376px;
  left: 730px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4237 {
  width: 23px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 378px;
  left: 925px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4238 {
  width: 23px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 502px;
  left: 530px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4239 {
  width: 22px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 502px;
  left: 725px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4240 {
  width: 23px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 505px;
  left: 925px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}
.v522_4244 {
  width: 25px;
  color: rgba(0,0,0,1);
  position: absolute;
  top: 760px;
  left: 730px;
  font-family: Georgia;
  font-weight: Regular;
  font-size: 40px;
  opacity: 1;
  text-align: left;
  cursor: pointer;
}

</style>